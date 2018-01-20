# -*- coding: utf-8 -*-
from __future__ import print_function
from builtins import range

import os
import difflib
from hashlib import sha256
import unittest

import pefile

REGRESSION_TESTS_DIR = 'tests/test_files'

class Test_pefile(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.test_files = self._load_test_files()

    def _load_test_files(self):
        """Load all the test files to be processes"""

        test_files = list()

        for dirpath, dirname, filenames in os.walk(REGRESSION_TESTS_DIR):
            for filename in (f for f in filenames if not f.endswith('.dmp')):
                test_files.append(os.path.join(dirpath, filename))

        return test_files

    def test_pe_image_regression_test(self):
        """Run through all the test files and make sure they run correctly"""

        for idx, pe_filename in enumerate(self.test_files):
            if pe_filename.endswith('fake_PE_no_read_permissions_issue_53'):
                continue
            if pe_filename.endswith('empty_file'):
                continue

            try:
                pe = pefile.PE(pe_filename)
                pe_file_data = pe.dump_info()
                pe_file_dict_data = pe.dump_dict() # Make sure that it does not fail
                pe_file_data = pe_file_data.replace('\n\r', '\n')
            except Exception as excp:
                print('Failed processing [%s]' % os.path.basename(pe_filename))
                raise

            control_data_filename = '%s.dmp' % pe_filename

            if not os.path.exists(control_data_filename):
                print((
                    'Could not find control data file [%s]. '
                    'Assuming first run and generating...') % (
                    os.path.basename(control_data_filename)))
                control_data_f = open(control_data_filename, 'wb')
                control_data_f.write(pe_file_data.encode('utf-8', 'backslashreplace'))
                continue

            control_data_f = open(control_data_filename, 'rb')
            control_data = control_data_f.read()
            control_data_f.close()

            pe_file_data_hash = sha256(pe_file_data.encode('utf-8', 'backslashreplace')).hexdigest()
            control_data_hash = sha256(control_data).hexdigest()

            diff_lines_added_count = 0
            diff_lines_removed_count = 0
            lines_to_ignore = 0

            if control_data_hash != pe_file_data_hash:
                print('Hash differs for [%s]' % os.path.basename(pe_filename))

                diff = difflib.ndiff(
                    control_data.decode('utf-8').splitlines(), pe_file_data.splitlines())

                # check the diff
                for line in diff:
                    # Count all changed lines
                    if line.startswith('+ '):
                        diff_lines_added_count += 1
                        # Window's returns slightly different date strings,
                        # ignore those.
                        if 'TimeDateStamp' in line:
                            lines_to_ignore += 1
                    if line.startswith('- '):
                        diff_lines_removed_count += 1
                        # Same as before, the condition is here, in both
                        # places because we want to count only the lines in
                        # which TimeDateStamp appears that are different, the
                        # identical ones are good.
                        if 'TimeDateStamp' in line:
                            lines_to_ignore += 1


                if (diff_lines_removed_count == diff_lines_added_count and
                    lines_to_ignore ==
                        diff_lines_removed_count + diff_lines_added_count):
                    print (
                        'Differences are in TimeDateStamp formatting, '
                        'ignoring...')

                else:
                    print (
                        'Lines added: %d, lines removed: %d, lines with '
                        'TimeDateStamp: %d' % (
                        diff_lines_added_count, diff_lines_removed_count,
                        lines_to_ignore))

                    # Do the diff again to store it for analysis.
                    diff = difflib.unified_diff(
                        control_data.decode('utf-8').splitlines(), pe_file_data.splitlines())
                    error_diff_f = open('error_diff.txt', 'ab')
                    error_diff_f.write(
                        b'\n________________________________________\n')
                    error_diff_f.write(
                        'Errors for file "{0}":\n'.format(pe_filename).encode('utf-8', 'backslashreplace'))
                    error_diff_f.write(
                        '\n'.join([l for l in diff if not l.startswith(' ')]).encode('utf-8', 'backslashreplace'))
                    error_diff_f.close()
                    print('Diff saved to: error_diff.txt')

            if diff_lines_removed_count == 0:
                try:
                    self.assertEqual(control_data.decode('utf-8'), pe_file_data)
                except AssertionError:
                    diff = difflib.unified_diff(
                        control_data.decode('utf-8').splitlines(), pe_file_data.splitlines())
                    raise AssertionError('\n'.join(diff))

            os.sys.stdout.write('[%d]' % (len(self.test_files) - idx))
            os.sys.stdout.flush()


    def test_selective_loading_integrity(self):
        """Verify integrity of loading the separate elements of the file as
        opposed to do a single pass.
        """

        control_file = os.path.join(REGRESSION_TESTS_DIR, 'MSVBVM60.DLL')
        pe = pefile.PE(control_file, fast_load=True)
        # Load the 16 directories.
        pe.parse_data_directories(directories= list(range(0x10)))

        # Do it all at once.
        pe_full = pefile.PE(control_file, fast_load=False)

        # Verify both methods obtained the same results.
        self.assertEqual(pe_full.dump_info(), pe.dump_info())

        pe.close()
        pe_full.close()


    def test_imphash(self):
        """Test imphash values."""

        self.assertEqual(
            pefile.PE(os.path.join(
                REGRESSION_TESTS_DIR, 'mfc40.dll')).get_imphash(),
            'ef3d32741141a9ffde06721c65ea07b6')

        self.assertEqual(
            pefile.PE(os.path.join(
                REGRESSION_TESTS_DIR, 'kernel32.dll')).get_imphash(),
            '239b8e3d4f9d1860d6ce5efb07b02e2a')

        self.assertEqual(
            pefile.PE(os.path.join(
                REGRESSION_TESTS_DIR,
                '66c74e4c9dbd1d33b22f63cd0318b72dea88f9dbb4d36a3383d3da20b037d42e'
               )).get_imphash(),
            'a781de574e0567285ee1233bf6a57cc0')

        self.assertEqual(
            pefile.PE(os.path.join(
                REGRESSION_TESTS_DIR, '64bit_Binaries/cmd.exe')).get_imphash(),
            'd0058544e4588b1b2290b7f4d830eb0a')


    def test_write_header_fields(self):
        """Verify correct field data modification."""

        # Test version information writing
        control_file = os.path.join(REGRESSION_TESTS_DIR, 'MSVBVM60.DLL')
        pe = pefile.PE(control_file, fast_load=True)
        pe.parse_data_directories(
            directories=[
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_RESOURCE']])

        original_data = pe.write()

        str1 = b'string1'
        str2 = b'str2'
        str3 = b'string3'

        pe.FileInfo[0].StringTable[0].entries[b'FileDescription'] = str1
        pe.FileInfo[0].StringTable[0].entries[b'FileVersion'] = str2
        pe.FileInfo[0].StringTable[0].entries[b'InternalName'] = str3

        new_data = pe.write()

        diff, differences = 0, list()
        for idx in range(len(original_data)):
            if original_data[idx] != new_data[idx]:

                diff += 1
                # Skip the zeroes that pefile automatically adds to pad a new,
                # shorter string, into the space occupied by a longer one.
                if new_data[idx] != 0:
                    differences.append(chr(new_data[idx]))

        # Verify all modifications in the file were the ones we just made
        #
        self.assertEqual(''.join(differences).encode('utf-8', 'backslashreplace'),  str1+str2+str3)

        pe.close()

    def test_nt_headers_exception(self):
        """pefile should fail parsing invalid data (missing NT headers)"""

        # Take a known good file.
        control_file = os.path.join(REGRESSION_TESTS_DIR, 'MSVBVM60.DLL')
        pe = pefile.PE(control_file, fast_load=True)

        # Truncate it at the PE header and add invalid data.
        pe_header_offest = pe.DOS_HEADER.e_lfanew
        corrupted_data = pe.__data__[:pe_header_offest] + b'\0' * (1024*10)

        self.assertRaises(pefile.PEFormatError, pefile.PE, data=corrupted_data)


    def test_dos_header_exception_large_data(self):
        """pefile should fail parsing 10KiB of invalid data
        (missing DOS header).
        """

        # Generate 10KiB of zeroes
        data = b'\0' * (1024*10)

        # Attempt to parse data and verify PE header, a PEFormatError exception
        # is thrown.
        self.assertRaises(pefile.PEFormatError, pefile.PE, data=data)


    def test_dos_header_exception_small_data(self):
        """pefile should fail parsing 64 bytes of invalid data
        (missing DOS header).
        """

        # Generate 64 bytes of zeroes
        data = b'\0' * (64)

        # Attempt to parse data and verify PE header a PEFormatError exception
        # is thrown.
        self.assertRaises(pefile.PEFormatError, pefile.PE, data=data)


    def test_empty_file_exception(self):
        """pefile should fail parsing empty files."""

        # Take a known good file
        control_file = os.path.join(REGRESSION_TESTS_DIR, 'empty_file')
        self.assertRaises(pefile.PEFormatError, pefile.PE, control_file)


    def test_relocated_memory_mapped_image(self):
        """Test different rebasing methods produce the same image"""

        # Take a known good file
        control_file = os.path.join(REGRESSION_TESTS_DIR, 'MSVBVM60.DLL')
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



    def test_entry_point_retrieval_with_overlapping_sections(self):
        # Versions up to and including 114 would not handle overlapping
        # sections correctly. A section size could push the end address
        # beyond the start of the next section, in such cases thes sections's
        # contains_rva() would return true for an address lying in a later
        # section. contains_rva() is used in multiple places to find out
        # from what section's disk-offset to read from, finding an invalid
        # section lead to reading the wrong data.
        # A check is made now that the section's start address + size does not
        # go beyond a subsequent section's start address and if so, it's
        # truncated.
        control_file = os.path.join(REGRESSION_TESTS_DIR,
            '924C62EF97E0B4939E9047B866037BB5BDDA92F9DA6D22F5DEEFC540856CDC0D.'
            'bin__aleph_overlapping_sections')
        pe = pefile.PE(control_file)

        entry_point_data = pe.get_data(
            pe.OPTIONAL_HEADER.AddressOfEntryPoint, 10)

        # this is the correct EP data
        good_ep_data = b'\x55\x8b\xec\x83\xec\x70\x83\x65\xcc\x00'

        self.assertEqual(entry_point_data, good_ep_data)


    def test_entry_point_retrieval_with_unusual_aligments(self):
        # Fixed a bug in pefile <= 1.2.10-93. Fixed in revision 94
        # http://code.google.com/p/pefile/source/detail?r=94

        # this file has FileAlignment == SectionAlignment == 0x200 and
        # its section layout led to older versions of pefile not reading
        # the correct entry point data
        control_file = os.path.join(REGRESSION_TESTS_DIR,
            'BackDoor.Poison.ex_bad_section_and_file_aligments_broke_'
            'pefile_1.2.10-93')
        pe = pefile.PE(control_file)

        entry_point_data = pe.get_data(
            pe.OPTIONAL_HEADER.AddressOfEntryPoint, 32)

        # this is the correct EP data
        good_ep_data = [
            0xb8, 0x00, 0x04, 0x40, 0x00, 0xff, 0xd0, 0x6a, 0x00, 0xe8, 0x00,
            0x00, 0x00, 0x00, 0xff, 0x25, 0x00, 0x02, 0x40, 0x00, 0x44, 0x02,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

        if isinstance(entry_point_data[0], int):
            self.assertEqual([i for i in entry_point_data], good_ep_data)
        else:
            self.assertEqual([ord(i) for i in entry_point_data], good_ep_data)


    def test_entry_point_retrieval_with_unusual_PointerToRawData_values(self):
        # Fixed a bug in pefile <= 1.2.10-106. Fixed in revision 107
        # http://code.google.com/p/pefile/source/detail?r=107

        # this file has abnormal PointerToRawData values that lead to the EP
        # not being correctly retrieved
        control_file = os.path.join(
            REGRESSION_TESTS_DIR, 'unconventional_PointerToRawData_values')
        pe = pefile.PE(control_file)

        entry_point_data = pe.get_data(
            pe.OPTIONAL_HEADER.AddressOfEntryPoint, 32)

        # this is the correct EP data
        good_ep_data = [
            0xbe, 0xe0, 0x11, 0x40, 0x00, 0xff, 0x36, 0xe9, 0xc3, 0x00, 0x00,
            0x00, 0x48, 0x01, 0x0f, 0x01, 0x0b, 0x01, 0x4b, 0x45, 0x52, 0x4e,
            0x45, 0x4c, 0x33, 0x32, 0x2e, 0x44, 0x4c, 0x4c, 0x00, 0x00]

        if isinstance(entry_point_data[0], int):
            self.assertEqual([i for i in entry_point_data], good_ep_data)
        else:
            self.assertEqual([ord(i) for i in entry_point_data], good_ep_data)


    def test_VS_VERSIONINFO_dword_aligment(self):
        # Fixed a bug in pefile < 1.2.10-96. Fixed in revision 96:
        # http://code.google.com/p/pefile/source/detail?r=96
        # Was issue: 12

        control_file = os.path.join(REGRESSION_TESTS_DIR,
            '031.vxe_pefile_1.2.10-95_dword_alignment_was_not_ok_for_'
            'VS_VERSIONINFO')
        pe = pefile.PE(control_file)

        vs_fixedfileinfo_signature = pe.VS_FIXEDFILEINFO.Signature

        # This is the correct VS_FIXEDFILEINFO Signature.
        good_vs_fixedfileinfo_signature = 0xfeef04bd

        self.assertEqual(
                vs_fixedfileinfo_signature, good_vs_fixedfileinfo_signature)

    def test_overlay_github_issue_104(self):
        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            '307a69414b203f1116db677b8bc07130ae2b72cf33cf2ae5a39bf1bd484b587c_overlay_issue_104')
        pe = pefile.PE(control_file_pe)
        overlay_offset = pe.get_overlay_data_start_offset()
        self.assertEqual(overlay_offset, 14848)

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            '3096e39df63c0be68746ea3bbe528c067b6eb45e2d61cc167712c3b1e0966be3_overlay_issue_104')
        pe = pefile.PE(control_file_pe)
        overlay_offset = pe.get_overlay_data_start_offset()
        self.assertEqual(overlay_offset, 93696)

    def test_get_overlay_and_trimming(self):
        """Test method to retrieve overlay data and trim the PE"""

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, '0x90_with_overlay_data.exe')
        pe = pefile.PE(control_file_pe)
        overlay_data = pe.get_overlay()
        trimmed_data = pe.trim()

        # Ensure the overlay data is correct.
        self.assertEqual(overlay_data, bytes(b'A'*186 + b'\n'))

        # Ensure the trim offset is correct.
        self.assertEqual(pe.get_overlay_data_start_offset(), 294912)

        # Ensure the trim data is correct.
        self.assertEqual(len(trimmed_data), 294912)

        control_file_pe = os.path.join(REGRESSION_TESTS_DIR, '0x90.exe')
        pe = pefile.PE(control_file_pe)

        # Ensure the overlay data is correct (should not be any in this case).
        self.assertEqual(pe.get_overlay(), None)

        trimmed_data = pe.trim()

        # Ensure the trim data is correct.
        self.assertEqual(len(trimmed_data), 294912)

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, 'sectionless.exe_corkami_issue_51')
        pe = pefile.PE(control_file_pe)

        # Ensure the overlay data is correct (should not be any in this case).
        self.assertEqual(pe.get_overlay(), None)

    def test_unable_to_read_file(self):
        """Attempting to open a file without read permission for the user
        should result in and error message.
        """

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR, 'fake_PE_no_read_permissions_issue_53')
        self.assertRaises(Exception, pefile.PE, control_file_pe)


    def test_driver_check(self):
        """Test the is_driver check"""

        control_file_pe = os.path.join(
            REGRESSION_TESTS_DIR,
            '075356de51afac92d1c20ba53c966fa145172897a96cfdb1b3bb369edb376a77_driver')

        pe_fast = pefile.PE(control_file_pe, fast_load=True)
        pe_full = pefile.PE(control_file_pe, fast_load=False)

        # Ensure the rebased image is the same as the pre-generated one.
        self.assertEqual(pe_fast.is_driver(), pe_full.is_driver())


    def test_rebased_image(self):
        """Test correctness of rebased images"""

        # Take a known good file.
        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            'pefile_unittest_data__resurrel_malware_rebased_0x400000')
        control_file_f = open(control_file, 'rb')
        control_file_data = control_file_f.read()
        control_file_f.close()

        control_file_pe = os.path.join(REGRESSION_TESTS_DIR, 'e05916.ex_')
        pe = pefile.PE(control_file_pe)
        rebased_data = pe.get_memory_mapped_image(ImageBase=0x400000)

        # Ensure the rebased image is the same as the pre-generated one.
        self.assertEqual(rebased_data, control_file_data)


    def test_checksum(self):
        """Verify correct calculation of checksum"""

        # Take a known good file.
        control_file = os.path.join(REGRESSION_TESTS_DIR, 'MSVBVM60.DLL')
        pe = pefile.PE(control_file)

        # verify_checksum() generates a checksum from the image's data and
        # compares it against the checksum field in the optional header.
        self.assertEqual(pe.verify_checksum(), True)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            'checksum/0031709440C539B47E34B524AF3900248DD35274_bad_checksum')
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), False)
        self.assertEqual(pe.generate_checksum(), 0x16c39)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            'checksum/009763E904C053C1803B26EC0D817AF497DA1BB2_bad_checksum')
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), False)
        self.assertEqual(pe.generate_checksum(), 0x249f7)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            'checksum/00499E3A70A324160A3FE935F10BFB699ACB0954')
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), True)

        control_file = os.path.join(
            REGRESSION_TESTS_DIR,
            'checksum/0011FEECD53D06A6C68C531E0DA7A61C692E76BF')
        pe = pefile.PE(control_file)
        self.assertEqual(pe.verify_checksum(), True)

