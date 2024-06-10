import difflib
import os
import sys
import unittest
from hashlib import sha256

import pefile

REGRESSION_TESTS_DIR = "tests/test_files"


class Test_pefile(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.test_files = self._load_test_files()

    def _load_test_files(self):
        """Load all the test files to be processed"""

        test_files = list()

        for dirpath, dirname, filenames in os.walk(REGRESSION_TESTS_DIR):
            for filename in (f for f in filenames if not f.endswith(".dmp")):
                test_files.append(os.path.join(dirpath, filename))

        return test_files

    def test_pe_image_regression_test(self):
        """Run through all the test files and make sure they run correctly"""

        failed = False
        for idx, pe_filename in enumerate(self.test_files):
            if pe_filename.endswith("fake_PE_no_read_permissions_issue_53"):
                continue
            if pe_filename.endswith("empty_file"):
                continue

            try:
                pe = pefile.PE(pe_filename)
                pe_file_data = pe.dump_info()
                pe_file_dict_data = pe.dump_dict()  # Make sure that it does not fail
                pe_file_data = pe_file_data.replace("\n\r", "\n")
            except Exception as excp:
                print(
                    "Failed processing [%s] (%s)"
                    % (os.path.basename(pe_filename), excp)
                )
                failed = True
                continue

            control_data_filename = "%s.dmp" % pe_filename

            if not os.path.exists(control_data_filename):
                print(
                    (
                        "Could not find control data file [%s]. "
                        "Assuming first run and generating..."
                    )
                    % (os.path.basename(control_data_filename))
                )
                control_data_f = open(control_data_filename, "wb")
                control_data_f.write(pe_file_data.encode("utf-8", "backslashreplace"))
                continue

            control_data_f = open(control_data_filename, "rb")
            control_data = control_data_f.read()
            control_data_f.close()

            pe_file_data_hash = sha256(
                pe_file_data.encode("utf-8", "backslashreplace")
            ).hexdigest()
            control_data_hash = sha256(control_data).hexdigest()

            diff_lines_added_count = 0
            diff_lines_removed_count = 0
            lines_to_ignore = 0

            if control_data_hash != pe_file_data_hash:
                print("\nHash differs for [%s]" % os.path.basename(pe_filename))

                control_file_lines = [
                    l for l in control_data.decode("utf-8").splitlines()
                ]
                pefile_lines = pe_file_data.splitlines()

                diff = difflib.ndiff(control_file_lines, pefile_lines)

                # check the diff
                for line in diff:
                    # Count all changed lines
                    if line.startswith("+ "):
                        diff_lines_added_count += 1
                        # Windows returns slightly different date strings,
                        # ignore those.
                        if "TimeDateStamp" in line:
                            lines_to_ignore += 1
                    if line.startswith("- "):
                        diff_lines_removed_count += 1
                        # Same as before, the condition is here, in both
                        # places because we want to count only the lines in
                        # which TimeDateStamp appears that are different, the
                        # identical ones are good.
                        if "TimeDateStamp" in line:
                            lines_to_ignore += 1

                if (
                    diff_lines_removed_count == diff_lines_added_count
                    and lines_to_ignore
                    == diff_lines_removed_count + diff_lines_added_count
                ):
                    print("Differences are in TimeDateStamp formatting, " "ignoring...")

                else:
                    print(
                        "Lines added: %d, lines removed: %d, lines with "
                        "TimeDateStamp: %d"
                        % (
                            diff_lines_added_count,
                            diff_lines_removed_count,
                            lines_to_ignore,
                        )
                    )

                    # Do the diff again to store it for analysis.
                    diff = list(
                        difflib.unified_diff(
                            control_file_lines,
                            pefile_lines,
                            fromfile="expected",
                            tofile="new",
                        )
                    )
                    error_diff_f = open("error_diff.txt", "ab")
                    error_diff_f.write(b"\n________________________________________\n")
                    error_diff_f.write(
                        'Errors for file "{0}":\n'.format(pe_filename).encode(
                            "utf-8", "backslashreplace"
                        )
                    )
                    error_diff_f.write(
                        "\n".join([l for l in diff if not l.startswith(" ")]).encode(
                            "utf-8", "backslashreplace"
                        )
                    )
                    error_diff_f.close()
                    print("\n".join(diff))
                    print("Diff saved to: error_diff.txt")
                    failed = True

            sys.stdout.write("[%d]" % (len(self.test_files) - idx))
            sys.stdout.flush()
        if failed:
            raise AssertionError("One or more errors occured")

    def test_get_rich_header_hash(self):
        """Verify the RICH_HEADER hashes."""

        control_file = os.path.join(REGRESSION_TESTS_DIR, "kernel32.dll")
        pe = pefile.PE(control_file)

        self.assertEqual(pe.get_rich_header_hash(), "b855b76450d1cd0dc4716bb129962b6d")
        self.assertEqual(
            pe.get_rich_header_hash("md5"), "b855b76450d1cd0dc4716bb129962b6d"
        )
        self.assertEqual(
            pe.get_rich_header_hash(algorithm="sha1"),
            "5113650e24988e658e40e6dfb4dcefbe62c1e1a5",
        )
        self.assertEqual(
            pe.get_rich_header_hash(algorithm="sha256"),
            "3a5f34064c2add746936f0a9cff5c02212e625e52c74dc7872409ae508cd6efb",
        )
        self.assertEqual(
            pe.get_rich_header_hash(algorithm="sha512"),
            "3efff532bf25870c4757c7fce6b1812b86e9518b885dc3860de4716cdd78d6ba"
            "5147a6261442c61f13158d439681a9ff50767676b49b0a06a3f618e0526e084f",
        )
        self.assertRaises(Exception, pe.get_rich_header_hash, algorithm="badalgo")

    def test_selective_loading_integrity(self):
        """Verify integrity of loading the separate elements of the file as
        opposed to do a single pass.
        """

        control_file = os.path.join(REGRESSION_TESTS_DIR, "MSVBVM60.DLL")
        pe = pefile.PE(control_file, fast_load=True)
        # Load the 16 directories.
        pe.parse_data_directories(directories=list(range(0x10)))

        # Do it all at once.
        pe_full = pefile.PE(control_file, fast_load=False)

        # Verify both methods obtained the same results.
        self.assertEqual(pe_full.dump_info(), pe.dump_info())

        pe.close()
        pe_full.close()

    def test_imphash(self):
        """Test imphash values."""

        self.assertEqual(
            pefile.PE(os.path.join(REGRESSION_TESTS_DIR, "mfc40.dll")).get_imphash(),
            "ef3d32741141a9ffde06721c65ea07b6",
        )

        self.assertEqual(
            pefile.PE(os.path.join(REGRESSION_TESTS_DIR, "kernel32.dll")).get_imphash(),
            "239b8e3d4f9d1860d6ce5efb07b02e2a",
        )

        self.assertEqual(
            pefile.PE(
                os.path.join(
                    REGRESSION_TESTS_DIR,
                    "66c74e4c9dbd1d33b22f63cd0318b72dea88f9dbb4d36a3383d3da20b037d42e",
                )
            ).get_imphash(),
            "a781de574e0567285ee1233bf6a57cc0",
        )

        self.assertEqual(
            pefile.PE(
                os.path.join(REGRESSION_TESTS_DIR, "64bit_Binaries/cmd.exe")
            ).get_imphash(),
            "d0058544e4588b1b2290b7f4d830eb0a",
        )

    def test_exphash(self):
        """Test exphash values."""

        self.assertEqual(
            pefile.PE(os.path.join(REGRESSION_TESTS_DIR, "mfc40.dll")).get_exphash(),
            "62d630f6941ad56df3b0a079873a82bc",
        )

        self.assertEqual(
            pefile.PE(os.path.join(REGRESSION_TESTS_DIR, "kernel32.dll")).get_exphash(),
            "ce0e98011116b41414acebc1e8c411c9",
        )

        self.assertEqual(
            pefile.PE(
                os.path.join(
                    REGRESSION_TESTS_DIR,
                    "66c74e4c9dbd1d33b22f63cd0318b72dea88f9dbb4d36a3383d3da20b037d42e",
                )
            ).get_exphash(),
            "1f00d8a63daedf9970feb050bad38030",
        )

        self.assertEqual(
            pefile.PE(
                os.path.join(REGRESSION_TESTS_DIR, "64bit_Binaries/cmd.exe")
            ).get_exphash(),
            "",
        )

    def test_write_header_fields(self):
        """Verify correct field data modification."""

        # Test version information writing
        control_file = os.path.join(REGRESSION_TESTS_DIR, "MSVBVM60.DLL")
        pe = pefile.PE(control_file, fast_load=True)
        pe.parse_data_directories(
            directories=[pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_RESOURCE"]]
        )

        original_data = pe.write()

        str1 = b"string1"
        str2 = b"str2"
        str3 = b"string3"

        pe.FileInfo[0][0].StringTable[0].entries[b"FileDescription"] = str1
        pe.FileInfo[0][0].StringTable[0].entries[b"FileVersion"] = str2
        pe.FileInfo[0][0].StringTable[0].entries[b"InternalName"] = str3

        new_data = pe.write()

        diff, differences = 0, list()
        for idx in range(len(original_data)):
            if original_data and new_data and original_data[idx] != new_data[idx]:
                diff += 1
                # Skip the zeroes that pefile automatically adds to pad a new,
                # shorter string, into the space occupied by a longer one.
                if new_data[idx] != 0:
                    differences.append(chr(new_data[idx]))

        # Verify all modifications in the file were the ones we just made
        #
        self.assertEqual(
            "".join(differences).encode("utf-8", "backslashreplace"), str1 + str2 + str3
        )

        pe.close()

    def test_nt_headers_exception(self):
        """pefile should fail parsing invalid data (missing NT headers)"""

        # Take a known good file.
        control_file = os.path.join(REGRESSION_TESTS_DIR, "MSVBVM60.DLL")
        pe = pefile.PE(control_file, fast_load=True)

        # Truncate it at the PE header and add invalid data.
        pe_header_offest = pe.DOS_HEADER.e_lfanew
        self.assertIsNotNone(pe.__data__)
        if pe.__data__:
            corrupted_data = pe.__data__[:pe_header_offest] + b"\0" * (1024 * 10)

            self.assertRaises(pefile.PEFormatError, pefile.PE, data=corrupted_data)

    def test_dos_header_exception_large_data(self):
        """pefile should fail parsing 10KiB of invalid data
        (missing DOS header).
        """

        # Generate 10KiB of zeroes
        data = b"\0" * (1024 * 10)

        # Attempt to parse data and verify PE header, a PEFormatError exception
        # is thrown.
        self.assertRaises(pefile.PEFormatError, pefile.PE, data=data)

    def test_dos_header_exception_small_data(self):
        """pefile should fail parsing 64 bytes of invalid data
        (missing DOS header).
        """

        # Generate 64 bytes of zeroes
        data = b"\0" * (64)

        # Attempt to parse data and verify PE header a PEFormatError exception
        # is thrown.
        self.assertRaises(pefile.PEFormatError, pefile.PE, data=data)

    def test_empty_file_exception(self):
        """pefile should fail parsing empty files."""

        # Take a known good file
        control_file = os.path.join(REGRESSION_TESTS_DIR, "empty_file")
        self.assertRaises(pefile.PEFormatError, pefile.PE, control_file)

    def test_relocated_memory_mapped_image(self):
        """Test different rebasing methods produce the same image"""

        # Take a known good file
        control_file = os.path.join(REGRESSION_TESTS_DIR, "MSVBVM60.DLL")
        pe = pefile.PE(control_file)

        def count_differences(data1, data2):
            diff = 0
            for idx in range(len(data1)):
                if data1[idx] != data2[idx]:
                    diff += 1
            return diff

        original_image_1 = pe.get_memory_mapped_image()
        rebased_image_1 = pe.get_memory_mapped_image(ImageBase=0x1000000)

        differences_1 = count_differences(original_image_1, rebased_image_1)
        self.assertEqual(differences_1, 60624)

        pe = pefile.PE(control_file)

        original_image_2 = pe.get_memory_mapped_image()
        pe.relocate_image(0x1000000)
        rebased_image_2 = pe.get_memory_mapped_image()

        differences_2 = count_differences(original_image_2, rebased_image_2)
        self.assertEqual(differences_2, 60624)

        # Ensure the original image stayed the same
        self.assertEqual(original_image_1, original_image_2)

        # This file used to crash pefile when attempting to relocate it:
        # https://github.com/erocarrera/pefile/issues/314
        control_file = os.path.join(
            REGRESSION_TESTS_DIR, "crash-8499a0bb33aeba8f59a172584abc7ca0ab82a78c"
        )
        pe = pefile.PE(control_file)

    def test_entry_point_retrieval_with_overlapping_sections(self):
        # Versions up to and including 114 would not handle overlapping
        # sections correctly. A section size could push the end address
        # beyond the start of the next section, in such cases the sections'
        # contains_rva() would return true for an address lying in a later
        # section. contains_rva() is used in multiple places to find out
        # from what section's disk-offset to read from, finding an invalid
        # section leads to reading the wrong data.
        # A check is made now that the section's start address + size does not
        # go beyond a subsequent section's start address and if so, it's
        # truncated.
        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "924C62EF97E0B4939E9047B866037BB5BDDA92F9DA6D22F5DEEFC540856CDC0D."
            "bin__aleph_overlapping_sections",
        )
        pe = pefile.PE(control_file)

        entry_point_data = pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 10)

        # this is the correct EP data
        good_ep_data = b"\x55\x8b\xec\x83\xec\x70\x83\x65\xcc\x00"

        self.assertEqual(entry_point_data, good_ep_data)

    def test_entry_point_retrieval_with_unusual_aligments(self):
        # Fixed a bug in pefile <= 1.2.10-93. Fixed in revision 94
        # http://code.google.com/p/pefile/source/detail?r=94

        # this file has FileAlignment == SectionAlignment == 0x200 and
        # its section layout led to older versions of pefile not reading
        # the correct entry point data
        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "BackDoor.Poison.ex_bad_section_and_file_aligments_broke_"
            "pefile_1.2.10-93",
        )
        pe = pefile.PE(control_file)

        self.assertEqual(
            pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 32),
            bytes.fromhex(
                "B800044000FFD06A00E800000000FF2500024000440200000000000000000000"
            ),
        )

    def test_entry_point_retrieval_with_unusual_PointerToRawData_values(self):
        # Fixed a bug in pefile <= 1.2.10-106. Fixed in revision 107
        # http://code.google.com/p/pefile/source/detail?r=107

        # This file has abnormal PointerToRawData values that lead to the EP
        # not being correctly retrieved. The first section's PointerToRawData
        # is 0x10, which is rounded down to zero, it's VirtualAddress is 0x1000.
        # The entry point is at 0x1018, hence it will correspond to reading at
        # offset 0x18 in the file.
        control_file = os.path.join(
            REGRESSION_TESTS_DIR, "unconventional_PointerToRawData_values"
        )
        pe = pefile.PE(control_file)

        self.assertEqual(
            pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 32),
            bytes.fromhex(
                "BEE0114000FF36E9C300000048010F010B014B45524E454C33322E444C4C0000"
            ),
        )
        self.assertEqual(
            pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 32),
            pe.__data__[0x18 : 0x18 + 32],
        )

        # This file is provided in https://github.com/hasherezade/pe-bear/issues/11
        # to reproduce the reported issue.
        # The entry point is at 0x167000, which is at the very beginning of the last
        # section, named ".new". The PointerToRawData of this section is 0x161D28,
        # which gets rounded to 0x161c00 (as if using the default alignment of 0x200),
        # which is the one specified in the OptionalHeader's FileAlignment.
        # Note that modifying the FileAlignment in the OptionalHeader to 0x1000 does
        # not make any difference, the Windows loader still aligns the PointerToRawData
        # to 0x200.
        fname = "pe-bear_issue_11/packed.exe"
        if os.path.exists(os.path.join(REGRESSION_TESTS_DIR, fname)):
            control_file = os.path.join(REGRESSION_TESTS_DIR, fname)
            pe = pefile.PE(control_file)

            self.assertEqual(
                pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 10),
                # This is the correct EP data at file offset 0x161c00 (0x161D28 rounded
                # down with alignment 0x200)
                bytes.fromhex("55f3499ca68cc9e57b9d"),
            )

        # The file has a section with PointerToRawData = VirtualAddress = 0xc. Section
        # data is read starting from zero, as 0xc gets rounded down to zero.
        control_file = os.path.join(REGRESSION_TESTS_DIR, "tiny-1.exe")
        pe = pefile.PE(control_file)

        self.assertEqual(
            pe.get_data(pe.OPTIONAL_HEADER.AddressOfEntryPoint, 10),
            # Data at file offset 0xc
            bytes.fromhex("6a2a58c3000000000000"),
        )

        # The section "whole" has a PointerToRawData = 0x1 which gets rounded down to
        # zero. The whole file is then read and loaded at the section's VirtualAddress,
        # effectively creating a copy.
        control_file = os.path.join(
            REGRESSION_TESTS_DIR, "corkami_ange_testfiles/whole_pe_section.exe"
        )
        pe = pefile.PE(control_file)

        self.assertEqual(
            pe.get_data(0x2000, 10),
            pe.__data__[0:10],
        )

    def test_VS_VERSIONINFO_dword_aligment(self):
        # Fixed a bug in pefile < 1.2.10-96. Fixed in revision 96:
        # http://code.google.com/p/pefile/source/detail?r=96
        # Was issue: 12

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "031.vxe_pefile_1.2.10-95_dword_alignment_was_not_ok_for_" "VS_VERSIONINFO",
        )
        pe = pefile.PE(control_file)

        vs_fixedfileinfo_signature = pe.VS_FIXEDFILEINFO[0].Signature

        # This is the correct VS_FIXEDFILEINFO Signature.
        good_vs_fixedfileinfo_signature = 0xFEEF04BD

        self.assertEqual(vs_fixedfileinfo_signature, good_vs_fixedfileinfo_signature)

    def test_overlay_github_issue_104(self):
        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            "307a69414b203f1116db677b8bc07130ae2b72cf33cf2ae5a39bf1bd484b587c_overlay_issue_104",
        )
        pe = pefile.PE(control_file_pe)
        overlay_offset = pe.get_overlay_data_start_offset()
        self.assertEqual(overlay_offset, 14848)

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            "3096e39df63c0be68746ea3bbe528c067b6eb45e2d61cc167712c3b1e0966be3_overlay_issue_104",
        )
        pe = pefile.PE(control_file_pe)
        overlay_offset = pe.get_overlay_data_start_offset()
        self.assertEqual(overlay_offset, 93696)

    def test_get_overlay_and_trimming(self):
        """Test method to retrieve overlay data and trim the PE"""

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, "0x90_with_overlay_data.exe"
        )
        pe = pefile.PE(control_file_pe)
        overlay_data = pe.get_overlay()
        trimmed_data = pe.trim()

        # Ensure the overlay data is correct.
        self.assertEqual(overlay_data, bytes(b"A" * 186 + b"\n"))

        # Ensure the trim offset is correct.
        self.assertEqual(pe.get_overlay_data_start_offset(), 294912)

        # Ensure the trim data is correct.
        self.assertEqual(len(trimmed_data), 294912)

        control_file_pe = os.path.join(REGRESSION_TESTS_DIR, "0x90.exe")
        pe = pefile.PE(control_file_pe)

        # Ensure the overlay data is correct (should not be any in this case).
        self.assertEqual(pe.get_overlay(), None)

        trimmed_data = pe.trim()

        # Ensure the trim data is correct.
        self.assertEqual(len(trimmed_data), 294912)

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, "sectionless.exe_corkami_issue_51"
        )
        pe = pefile.PE(control_file_pe)

        # Ensure the overlay data is correct (should not be any in this case).
        self.assertEqual(pe.get_overlay(), None)

    def test_unable_to_read_file(self):
        """Attempting to open a file without read permission for the user
        should result in an error message.
        """

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, "fake_PE_no_read_permissions_issue_53"
        )
        self.assertRaises(Exception, pefile.PE, control_file_pe)

    def test_driver_check(self):
        """Test the is_driver check"""

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            "075356de51afac92d1c20ba53c966fa145172897a96cfdb1b3bb369edb376a77_driver",
        )

        pe_fast = pefile.PE(control_file_pe, fast_load=True)
        pe_full = pefile.PE(control_file_pe, fast_load=False)

        # Ensure the rebased image is the same as the pre-generated one.
        self.assertEqual(pe_fast.is_driver(), pe_full.is_driver())

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, "issue_322_plaso_test_driver.sys"
        )

        pe = pefile.PE(control_file_pe, fast_load=False)
        self.assertEqual(pe.is_driver(), True)

    def test_rebased_image(self):
        """Test correctness of rebased images"""

        # Take a known good file.
        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "pefile_unittest_data__resurrel_malware_rebased_0x400000",
        )
        control_file_f = open(control_file, "rb")
        control_file_data = control_file_f.read()
        control_file_f.close()

        control_file_pe = os.path.join(REGRESSION_TESTS_DIR, "e05916.ex_")
        pe = pefile.PE(control_file_pe)
        rebased_data = pe.get_memory_mapped_image(ImageBase=0x400000)

        # Ensure the rebased image is the same as the pre-generated one.
        self.assertEqual(rebased_data, control_file_data)

    def test_checksum(self):
        """Verify correct calculation of checksum"""

        # Take a known good file.
        control_file = os.path.join(REGRESSION_TESTS_DIR, "MSVBVM60.DLL")
        pe = pefile.PE(control_file)

        # verify_checksum() generates a checksum from the image's data and
        # compares it against the checksum field in the optional header.
        self.assertEqual(pe.verify_checksum(), True)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "checksum/0031709440C539B47E34B524AF3900248DD35274_bad_checksum",
        )
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), False)
        self.assertEqual(pe.generate_checksum(), 0x16C39)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            "checksum/009763E904C053C1803B26EC0D817AF497DA1BB2_bad_checksum",
        )
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), False)
        self.assertEqual(pe.generate_checksum(), 0x249F7)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR, "checksum/00499E3A70A324160A3FE935F10BFB699ACB0954"
        )
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), True)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR, "checksum/0011FEECD53D06A6C68C531E0DA7A61C692E76BF"
        )
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), True)
