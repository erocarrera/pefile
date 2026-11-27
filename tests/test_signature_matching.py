import pytest

import peutils


def database_for(pattern, name="sample", section_start_only=False):
    return peutils.SignatureDatabase(
        data=(
            f"[{name}]\nsignature = {pattern}\nep_only = true\n"
            f"section_start_only = {str(section_start_only).lower()}\n"
        )
    )


class TestNibbleWildcards:
    @pytest.mark.parametrize("byte", range(256))
    def test_high_nibble_wildcard(self, byte):
        database = database_for("?a 42")
        result = database.match_data(bytes([byte, 0x42]))
        if byte in range(0x0A, 0x100, 0x10):
            assert result == (0, [["sample"]])
        else:
            assert result == []

    @pytest.mark.parametrize("byte", range(256))
    def test_low_nibble_wildcard(self, byte):
        database = database_for("a? 42")
        result = database.match_data(bytes([byte, 0x42]))
        if byte in range(0xA0, 0xB0):
            assert result == (0, [["sample"]])
        else:
            assert result == []

    @pytest.mark.parametrize(
        ("pattern", "data"),
        [("42 A?", b"B\xab"), ("42 ?A", b"B\xba")],
        ids=["high-nibble", "low-nibble"],
    )
    def test_nibble_wildcards_at_end(self, pattern, data):
        database = database_for(pattern)
        assert database.match_data(data) == (0, [["sample"]])
        assert database.match_data(data[:1]) == []

    def test_mixed_wildcards_and_exact_matches(self):
        database = database_for("A? ?? ?F 42", "wildcards")
        database.load(data="[exact]\nsignature = AB 12 CF 42\nep_only = true\n")
        assert database.match_data(b"\xab\x12\xcfB") == (0, [["wildcards"], ["exact"]])
        assert database.match_data(b"\xab\x12\xcfC") == []
        assert database.match_data(b"\xab\x12\xcf") == []

    def test_section_start_matching(self):
        database = database_for("A? ?F", section_start_only=True)
        assert database.match_data(b"\xab\xcf", section_start_only=True) == (0, [["sample"]])

    def test_load_nibbles_after_exact_signatures(self):
        database = database_for("AB CF", "exact")
        assert database.match_data(b"\xab\xcf") == (0, [["exact"]])
        database.load(data="[nibbles]\nsignature = A? ?F\nep_only = true\n")
        result = database.match_data(b"\xab\xcf")
        assert result == (0, [["nibbles"], ["exact"]])

    def test_existing_byte_wildcard(self):
        database = database_for("41 ?? 42")
        assert database.match_data(b"A\xffB") == (0, [["sample"]])
        assert database.match_data(b"A\xffC") == []
        assert database.match_data(b"A\xff") == []
