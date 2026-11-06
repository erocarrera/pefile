import struct

import pytest

import pefile


def make_pe(name=b"/4", strings=b".debug_info\0"):
    data = bytearray(512)
    data[:2] = b"MZ"
    struct.pack_into("<I", data, 0x3C, 0x80)
    data[0x80:0x84] = b"PE\0\0"
    struct.pack_into("<HHIIIHH", data, 0x84, 0x8664, 1, 0, 512, 0, 240, 0x22)
    struct.pack_into("<H", data, 0x98, 0x20B)
    struct.pack_into("<II", data, 0x98 + 32, 4096, 512)
    struct.pack_into("<II", data, 0x98 + 56, 8192, 512)
    struct.pack_into("<I", data, 0x98 + 108, 16)
    data[392:400] = name.ljust(8, b"\0")
    return bytes(data) + struct.pack("<I", len(strings) + 4) + strings


def test_coff_long_section_name():
    data = make_pe()
    with pefile.PE(data=data) as pe:
        section = pe.sections[0]
        assert section.get_name() == b".debug_info"
        assert section.Name == b"/4\0\0\0\0\0\0"
        assert pe.write() == data


@pytest.mark.parametrize(
    "name",
    [
        b".text",
        b"12345678",
        b"\xffname",
        b"/abc",
        b"/0",
        b"/3",
        b"/999",
        b"/+4",
        b"//4",
    ],
)
def test_short_or_invalid_section_name(name):
    with pefile.PE(data=make_pe(name)) as pe:
        assert pe.sections[0].get_name() == name


@pytest.mark.parametrize(
    ("strings", "expected"),
    [(b"\xffname\0", b"\xffname"), (b"first\0second\0", b"first"), (b"\0", b"")],
)
def test_resolved_names_are_bounded_bytes(strings, expected):
    with pefile.PE(data=make_pe(strings=strings)) as pe:
        assert pe.sections[0].get_name() == expected


@pytest.mark.parametrize(
    "change",
    ["missing", "truncated-header", "truncated-table", "small-length", "unterminated"],
)
def test_invalid_string_table_retains_raw_name(change):
    data = bytearray(make_pe())
    if change == "missing":
        struct.pack_into("<I", data, 0x84 + 8, 0)
    elif change == "truncated-header":
        del data[514:]
    elif change == "truncated-table":
        del data[-1:]
    elif change == "small-length":
        struct.pack_into("<I", data, 512, 3)
    else:
        data[-1] = ord("x")
    with pefile.PE(data=bytes(data)) as pe:
        assert pe.sections[0].get_name() == b"/4"


def test_string_table_follows_symbol_records():
    data = bytearray(make_pe())
    struct.pack_into("<I", data, 0x84 + 12, 2)
    data[512:512] = bytes(36)
    with pefile.PE(data=bytes(data)) as pe:
        assert pe.sections[0].get_name() == b".debug_info"


def test_offset_selects_later_string():
    with pefile.PE(data=make_pe(b"/10", b"first\0second\0")) as pe:
        assert pe.sections[0].get_name() == b"second"
