import pytest

import pefile
from tests import PE_32, PE_64


class TestImportRepetitionLimit:
    def parse_repeated_imports(self, data, count, **options):
        with pefile.PE(data=bytes(data), fast_load=True, **options) as pe:
            size = 4 if pe.PE_TYPE == pefile.OPTIONAL_HEADER_MAGIC_PE else 8
            rva = pe.sections[0].VirtualAddress
            address = rva + 400
            table_data = address.to_bytes(size, "little") * count + bytes(size)
            assert pe.set_bytes_at_rva(rva, table_data)
            assert pe.set_bytes_at_rva(address, b"\x00\x00repeated_import\x00")
            table = pe.get_import_table(rva)
            if table:
                assert all(entry.AddressOfData == address for entry in table)
            imports = pe.parse_imports(rva, rva, 0)
            assert len(imports) == len(table)
            if imports:
                assert all(entry.name == b"repeated_import" for entry in imports)
            return imports

    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_default_limit(self, data):
        assert len(self.parse_repeated_imports(data, 15)) == 15
        assert self.parse_repeated_imports(data, 19) == []

    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_higher_limit(self, data):
        assert len(self.parse_repeated_imports(data, 19, max_repeated_import_addresses=20)) == 19
        assert self.parse_repeated_imports(data, 21, max_repeated_import_addresses=20) == []

    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_lower_limit(self, data):
        assert self.parse_repeated_imports(data, 4, max_repeated_import_addresses=2) == []

    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_limit_is_per_instance(self, data):
        assert len(self.parse_repeated_imports(data, 19, max_repeated_import_addresses=20)) == 19
        assert self.parse_repeated_imports(data, 19) == []


class TestImportRename:
    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_rename_import_to_shorter_name(self, data):
        """A shorter replacement name must not keep the tail of the old one."""
        with pefile.PE(data=bytes(data), fast_load=True) as pe:
            size = 4 if pe.PE_TYPE == pefile.OPTIONAL_HEADER_MAGIC_PE else 8
            rva = pe.sections[0].VirtualAddress
            address = rva + 400
            table_data = address.to_bytes(size, "little") + bytes(size)
            assert pe.set_bytes_at_rva(rva, table_data)
            # IMAGE_IMPORT_BY_NAME is a 2-byte Hint followed by the name.
            hint = bytes(2)
            assert pe.set_bytes_at_rva(address, hint + b"CreateFileW\x00")
            imports = pe.parse_imports(rva, rva, 0)
            assert imports[0].name == b"CreateFileW"

            imports[0].name = b"Sleep"
            assert pe.get_string_at_rva(address + len(hint)) == b"Sleep"
