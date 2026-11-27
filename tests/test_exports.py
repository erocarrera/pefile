import pefile
from tests import PE_32, PE_64

EXPECT_NAMES = [
    (1, "TST!"),
    (2, 'TST"'),
    (3, "TST#"),
    (4, "TST$"),
    (5, "TST%"),
    (6, "TST&"),
    (7, "TST'"),
    (8, "TST("),
    (9, "TST)"),
    (10, "TST*"),
    (11, "TST+"),
    (12, "TST,"),
    (13, "TST-"),
    (14, "TST."),
    (15, "TST/"),
    (16, "TST:"),
    (17, "TST<"),
    (18, "TST>"),
    (19, "TST?"),
    (20, "TST["),
    (21, "TST\\"),
    (22, "TST]"),
    (23, "TST^"),
    (24, "TST_"),
    (25, "TST`"),
    (26, "TST{"),
    (27, "TST|"),
    (28, "TST}"),
    (29, "TST~"),
]


class TestExports:
    def test_exports32(self):
        """Iterate all exports of the 32 bit binary, and validate that they are all accepted."""
        # Update all the symbol addresses to be __ImageBase+0x01
        for idx, _ in enumerate(EXPECT_NAMES):
            PE_32[0x218 + 4 * idx] = 0x01
        pe = pefile.PE(data=PE_32)

        exports = []
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            name = exp.name.decode("utf-8") if exp.name else "-INVALID-"
            exports.append((exp.ordinal, name))

        assert exports == EXPECT_NAMES

    def test_rename_export_to_shorter_name(self):
        """A shorter replacement name must not keep the tail of the old one."""
        data = bytearray(PE_32)
        for idx in range(len(EXPECT_NAMES)):
            data[0x218 + 4 * idx] = 0x01
        pe = pefile.PE(data=data)
        pe.DIRECTORY_ENTRY_EXPORT.symbols[0].name = b"XY"

        pe = pefile.PE(data=pe.write())
        assert pe.DIRECTORY_ENTRY_EXPORT.symbols[0].name == b"XY"
        assert pe.DIRECTORY_ENTRY_EXPORT.symbols[1].name == b'TST"'

    def test_exports64(self):
        """Iterate all exports of the 64 bit binary, and validate that they are all accepted."""
        # Update all the symbol addresses to be __ImageBase+0x01
        for idx, _ in enumerate(EXPECT_NAMES):
            PE_64[0x228 + 4 * idx] = 0x01
        pe = pefile.PE(data=PE_64)

        exports = []
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            name = exp.name.decode("utf-8") if exp.name else "-INVALID-"
            exports.append((exp.ordinal, name))

        assert exports == EXPECT_NAMES
