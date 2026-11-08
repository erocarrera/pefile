import unittest

import peutils


def database_for(pattern, name="sample", section_start_only=False):
    return peutils.SignatureDatabase(
        data=(
            f"[{name}]\nsignature = {pattern}\nep_only = true\n"
            f"section_start_only = {str(section_start_only).lower()}\n"
        )
    )


class TestNibbleWildcards(unittest.TestCase):
    def test_high_nibble_wildcard(self):
        database = database_for("?a 42")
        for byte in range(256):
            with self.subTest(byte=byte):
                result = database.match_data(bytes([byte, 0x42]))
                if byte in range(0x0A, 0x100, 0x10):
                    self.assertEqual(result, (0, [["sample"]]))
                else:
                    self.assertEqual(result, [])

    def test_low_nibble_wildcard(self):
        database = database_for("a? 42")
        for byte in range(256):
            with self.subTest(byte=byte):
                result = database.match_data(bytes([byte, 0x42]))
                if byte in range(0xA0, 0xB0):
                    self.assertEqual(result, (0, [["sample"]]))
                else:
                    self.assertEqual(result, [])

    def test_nibble_wildcards_at_end(self):
        for pattern, data in [("42 A?", b"B\xab"), ("42 ?A", b"B\xba")]:
            with self.subTest(pattern=pattern):
                database = database_for(pattern)
                self.assertEqual(database.match_data(data), (0, [["sample"]]))
                self.assertEqual(database.match_data(data[:1]), [])

    def test_mixed_wildcards_and_exact_matches(self):
        database = database_for("A? ?? ?F 42", "wildcards")
        database.load(data="[exact]\nsignature = AB 12 CF 42\nep_only = true\n")
        self.assertEqual(
            database.match_data(b"\xab\x12\xcfB"),
            (0, [["wildcards"], ["exact"]]),
        )
        self.assertEqual(database.match_data(b"\xab\x12\xcfC"), [])
        self.assertEqual(database.match_data(b"\xab\x12\xcf"), [])

    def test_section_start_matching(self):
        database = database_for("A? ?F", section_start_only=True)
        self.assertEqual(
            database.match_data(b"\xab\xcf", section_start_only=True),
            (0, [["sample"]]),
        )

    def test_load_nibbles_after_exact_signatures(self):
        database = database_for("AB CF", "exact")
        self.assertEqual(database.match_data(b"\xab\xcf"), (0, [["exact"]]))
        database.load(data="[nibbles]\nsignature = A? ?F\nep_only = true\n")
        result = database.match_data(b"\xab\xcf")
        self.assertEqual(result, (0, [["nibbles"], ["exact"]]))

    def test_existing_byte_wildcard(self):
        database = database_for("41 ?? 42")
        self.assertEqual(database.match_data(b"A\xffB"), (0, [["sample"]]))
        self.assertEqual(database.match_data(b"A\xffC"), [])
        self.assertEqual(database.match_data(b"A\xff"), [])


if __name__ == "__main__":
    unittest.main()
