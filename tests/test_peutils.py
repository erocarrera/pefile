import pytest

import pefile
import peutils
from tests import PE_32, PE_64


class TestSignatureGeneration:
    @pytest.mark.parametrize(
        ("data", "buffer_type"),
        [
            pytest.param(PE_32, bytes, id="32-bit-bytes"),
            pytest.param(PE_32, bytearray, id="32-bit-bytearray"),
            pytest.param(PE_64, bytes, id="64-bit-bytes"),
            pytest.param(PE_64, bytearray, id="64-bit-bytearray"),
        ],
    )
    def test_entry_point_signature_round_trip(self, data, buffer_type):
        with pefile.PE(data=buffer_type(data), fast_load=True) as pe:
            section = pe.sections[0]
            pe.OPTIONAL_HEADER.AddressOfEntryPoint = section.VirtualAddress
            payload = b"\x00\x41\x80\xff"
            assert pe.set_bytes_at_offset(section.PointerToRawData, payload)
            database = peutils.SignatureDatabase()
            signature = database.generate_ep_signature(
                pe, "sample", sig_length=4
            )
            assert "signature = 00 41 80 ff\n" in signature
            assert "ep_only = true\n" in signature
            database.load(data=signature)
            assert database.match_data(payload) == (0, [["sample"]])

    @pytest.mark.parametrize("data", [PE_32, PE_64], ids=["32-bit", "64-bit"])
    def test_section_signature_round_trip(self, data):
        with pefile.PE(data=bytes(data), fast_load=True) as pe:
            section = pe.sections[0]
            section.Name = b".test\x00\x80\xff"
            payload = b"\xff\x80\x41\x00"
            assert pe.set_bytes_at_offset(section.PointerToRawData, payload)
            database = peutils.SignatureDatabase()
            signature = database.generate_section_signatures(
                pe, "sample", sig_length=4
            )
            assert "[sample Section(1/1,.test)]\n" in signature
            assert "signature = ff 80 41 00\n" in signature
            assert "section_start_only = true\n" in signature
            database.load(data=signature)
            assert database.match_data(payload, section_start_only=True) == (0, [["sample Section(1/1,.test)"]])

    def test_skip_short_sections(self):
        with pefile.PE(data=bytes(PE_32), fast_load=True) as pe:
            pe.sections[0].SizeOfRawData = 3
            assert peutils.SignatureDatabase().generate_section_signatures(pe, "sample", 4) == "\n"
