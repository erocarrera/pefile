import unittest

import pefile
import peutils
from export_test import PE_32, PE_64


class TestSignatureGeneration(unittest.TestCase):
    def test_entry_point_signature_round_trip(self):
        for data in (PE_32, PE_64):
            for buffer_type in (bytes, bytearray):
                with self.subTest(
                    bits=32 if data is PE_32 else 64, buffer_type=buffer_type
                ):
                    with pefile.PE(data=buffer_type(data), fast_load=True) as pe:
                        section = pe.sections[0]
                        pe.OPTIONAL_HEADER.AddressOfEntryPoint = section.VirtualAddress
                        payload = b"\x00\x41\x80\xff"
                        self.assertTrue(
                            pe.set_bytes_at_offset(section.PointerToRawData, payload)
                        )
                        database = peutils.SignatureDatabase()
                        signature = database.generate_ep_signature(
                            pe, "sample", sig_length=4
                        )
                        self.assertIn("signature = 00 41 80 ff\n", signature)
                        self.assertIn("ep_only = true\n", signature)
                        database.load(data=signature)
                        self.assertEqual(
                            database.match_data(payload), (0, [["sample"]])
                        )

    def test_section_signature_round_trip(self):
        for data in (PE_32, PE_64):
            with self.subTest(bits=32 if data is PE_32 else 64):
                with pefile.PE(data=bytes(data), fast_load=True) as pe:
                    section = pe.sections[0]
                    section.Name = b".test\x00\x80\xff"
                    payload = b"\xff\x80\x41\x00"
                    self.assertTrue(
                        pe.set_bytes_at_offset(section.PointerToRawData, payload)
                    )
                    database = peutils.SignatureDatabase()
                    signature = database.generate_section_signatures(
                        pe, "sample", sig_length=4
                    )
                    self.assertIn("[sample Section(1/1,.test)]\n", signature)
                    self.assertIn("signature = ff 80 41 00\n", signature)
                    self.assertIn("section_start_only = true\n", signature)
                    database.load(data=signature)
                    self.assertEqual(
                        database.match_data(payload, section_start_only=True),
                        (0, [["sample Section(1/1,.test)"]]),
                    )

    def test_skip_short_sections(self):
        with pefile.PE(data=bytes(PE_32), fast_load=True) as pe:
            pe.sections[0].SizeOfRawData = 3
            self.assertEqual(
                peutils.SignatureDatabase().generate_section_signatures(
                    pe, "sample", 4
                ),
                "\n",
            )


if __name__ == "__main__":
    unittest.main()
