import unittest

import pefile
from export_test import PE_32, PE_64


class TestImportRepetitionLimit(unittest.TestCase):
    def parse_repeated_imports(self, data, count, **options):
        with pefile.PE(data=bytes(data), fast_load=True, **options) as pe:
            size = 4 if pe.PE_TYPE == pefile.OPTIONAL_HEADER_MAGIC_PE else 8
            rva = pe.sections[0].VirtualAddress
            address = rva + 400
            table_data = address.to_bytes(size, "little") * count + bytes(size)
            self.assertTrue(pe.set_bytes_at_rva(rva, table_data))
            self.assertTrue(pe.set_bytes_at_rva(address, b"\x00\x00repeated_import\x00"))
            table = pe.get_import_table(rva)
            if table:
                self.assertTrue(all(entry.AddressOfData == address for entry in table))
            imports = pe.parse_imports(rva, rva, 0)
            self.assertEqual(len(imports), len(table))
            if imports:
                self.assertTrue(all(entry.name == b"repeated_import" for entry in imports))
            return imports

    def test_default_limit(self):
        for data in (PE_32, PE_64):
            with self.subTest(bits=32 if data is PE_32 else 64):
                self.assertEqual(len(self.parse_repeated_imports(data, 15)), 15)
                self.assertEqual(self.parse_repeated_imports(data, 19), [])

    def test_higher_limit(self):
        for data in (PE_32, PE_64):
            with self.subTest(bits=32 if data is PE_32 else 64):
                self.assertEqual(
                    len(self.parse_repeated_imports(data, 19, max_repeated_import_addresses=20)),
                    19,
                )
                self.assertEqual(
                    self.parse_repeated_imports(data, 21, max_repeated_import_addresses=20),
                    [],
                )

    def test_lower_limit(self):
        for data in (PE_32, PE_64):
            with self.subTest(bits=32 if data is PE_32 else 64):
                self.assertEqual(
                    self.parse_repeated_imports(data, 4, max_repeated_import_addresses=2),
                    [],
                )

    def test_limit_is_per_instance(self):
        for data in (PE_32, PE_64):
            self.assertEqual(
                len(self.parse_repeated_imports(data, 19, max_repeated_import_addresses=20)),
                19,
            )
            self.assertEqual(self.parse_repeated_imports(data, 19), [])


if __name__ == "__main__":
    unittest.main()
