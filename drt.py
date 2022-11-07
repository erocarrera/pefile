import struct
from typing import List


# Consts
# the offset of the fields in the load config struct, TODO: define (or find a python definition of) the full struct
DYNAMIC_RELOC_TABLE_OFFSET_FIELD_OFFSET = 0xe0


class IMAGE_DYNAMIC_RELOCATION_TABLE:
    sizeof = 8

    def __init__(self):
        self.version: int = None
        self.size: int = None
        self.dynamic_relocations: List[IMAGE_DYNAMIC_RELOCATION] = None

    @classmethod
    def from_pe(cls, raw_data: bytes, dynamic_reloc_table_offset: int) -> 'IMAGE_DYNAMIC_RELOCATION_TABLE':
        """
        Creates a DRT from the bytes of the relevant section
        :param pe: PE file object
        :param load_config_base_offset: offset to star of load config directory
        :return: IMAGE_DYNAMIC_RELOCATION_TABLE
        """
        drt = cls()
        drt.version, drt.size = struct.unpack('<II', raw_data[dynamic_reloc_table_offset:
                                                              dynamic_reloc_table_offset + drt.sizeof])
        # according to research, version is always 1
        if drt.version != 1:
            return None
        drt.dynamic_relocations = []
        idx = 0
        dynamic_reloc_data = raw_data[dynamic_reloc_table_offset + drt.sizeof:
                                      dynamic_reloc_table_offset + drt.sizeof + drt.size]
        while idx <= drt.size - IMAGE_DYNAMIC_RELOCATION.sizeof:
            reloc = IMAGE_DYNAMIC_RELOCATION.from_bytes(dynamic_reloc_data[idx:])
            idx += reloc.base_reloc_size + IMAGE_DYNAMIC_RELOCATION.sizeof
            drt.dynamic_relocations.append(reloc)
        return drt

    @classmethod
    def from_data(cls, dynamic_relocations: List['IMAGE_DYNAMIC_RELOCATION']) -> 'IMAGE_DYNAMIC_RELOCATION_TABLE':
        """
        Creates a DRT from a list of dynamic relocations
        :param dynamic_relocations: List of dynamic relocations
        :return: DRT
        """
        drt = cls()
        drt.version = 1
        drt.size = 0
        for dynamic_relocation in dynamic_relocations:
            drt.size += dynamic_relocation.base_reloc_size + IMAGE_DYNAMIC_RELOCATION.sizeof
        drt.dynamic_relocations = dynamic_relocations
        return drt

    def __repr__(self) -> str:
        return f"Version: {self.version} | Size: {hex(self.size)}\n" \
               f"Dynamic Relocation Data: {self.dynamic_relocations}"

    def dump(self) -> bytearray:
        """
        Dumps the dynamic relocation table into a packed struct (its raw form in the binary)
        :return: Packed DRT
        """
        packed_drt = bytearray(struct.pack('<II', self.version, self.size))
        for dynamic_relocation in self.dynamic_relocations:
            packed_drt += dynamic_relocation.dump()
        return packed_drt


class IMAGE_DYNAMIC_RELOCATION:
    sizeof = 12

    def __init__(self):
        self.symbol: int = None
        self.base_reloc_size: int = None
        self.base_relocations: List[IMAGE_BASE_RELOCATION] = None

    @classmethod
    def from_bytes(cls, raw_data: bytes) -> 'IMAGE_DYNAMIC_RELOCATION':
        """
        Creates a IMAGE_DYNAMIC_RELOCATION from raw data
        :param raw_data: IMAGE_DYNAMIC_RELOCATION raw data
        :return: IMAGE_DYNAMIC_RELOCATION
        """
        dynamic_reloc = cls()
        dynamic_reloc.symbol, dynamic_reloc.base_reloc_size = struct.unpack('<QI', raw_data[:dynamic_reloc.sizeof])
        reloc_data = raw_data[dynamic_reloc.sizeof:]
        dynamic_reloc.base_relocations = []
        idx = 0
        while idx <= dynamic_reloc.base_reloc_size - IMAGE_BASE_RELOCATION.sizeof:
            reloc = IMAGE_BASE_RELOCATION.from_bytes(reloc_data[idx:])
            idx += reloc.size_of_block
            dynamic_reloc.base_relocations.append(reloc)
        return dynamic_reloc

    @classmethod
    def from_data(cls, symbol: int, base_relocations: List['IMAGE_BASE_RELOCATION']) -> 'IMAGE_DYNAMIC_RELOCATION':
        dynamic_reloc = cls()
        dynamic_reloc.symbol = symbol
        dynamic_reloc.base_reloc_size = sum([reloc.size_of_block for reloc in base_relocations])
        dynamic_reloc.base_relocations = base_relocations
        return dynamic_reloc

    def __repr__(self) -> str:
        return f"Symbol: {hex(self.symbol)} | Base Reloc Size: {hex(self.base_reloc_size)} \n" \
               f"Base Relocations: {self.base_relocations}"

    def dump(self) -> bytearray:
        packed_dynamic_reloc = bytearray(struct.pack('<QI', self.symbol, self.base_reloc_size))
        for base_relocation in self.base_relocations:
            packed_dynamic_reloc += base_relocation.dump()
        return packed_dynamic_reloc


class IMAGE_BASE_RELOCATION:
    sizeof = 8

    def __init__(self):
        self.virtual_address: int = None
        self.size_of_block: int = None
        self.num_of_type_offsets: int = None
        self.type_offsets: List[int] = None
        self.has_padding: bool = None

    @classmethod
    def from_bytes(cls, raw_data: bytes) -> 'IMAGE_BASE_RELOCATION':
        """
        Creates an IMAGE_BASE_RELOCATION object from the raw data
        :param raw_data: raw data of the IMAGE_BASE_RELOCATION
        :return: IMAGE_BASE_RELOCATION object
        """
        base_reloc = cls()
        base_reloc.virtual_address, base_reloc.size_of_block = struct.unpack('<II', raw_data[:base_reloc.sizeof])
        base_reloc.num_of_type_offsets = int((base_reloc.size_of_block - base_reloc.sizeof) / 2)
        base_reloc.type_offsets = [offset + base_reloc.virtual_address for offset in
                                   struct.unpack('<' + 'H' * base_reloc.num_of_type_offsets,
                                                 raw_data[base_reloc.sizeof:base_reloc.sizeof + 2 * base_reloc.num_of_type_offsets])]
        base_reloc.has_padding = False
        # The last type offset is padding if there is an odd number of type offsets in the block
        if base_reloc.type_offsets[-1] - base_reloc.virtual_address == 0:
            base_reloc.type_offsets = base_reloc.type_offsets[:-1]
            base_reloc.has_padding = True

        return base_reloc

    @classmethod
    def from_data(cls, virtual_address: int, type_offsets: List[int]) -> 'IMAGE_BASE_RELOCATION':
        """
        Creates an IMAGE_BASE_RELOCATION object from the given data
        :param virtual_address: virtual address of the base relocation
        :param type_offsets: list of type offsets
        :return: IMAGE_BASE_RELOCATION object
        """
        base_reloc = cls()
        base_reloc.virtual_address = virtual_address
        # If there is an odd number of type offsets, add a padding type offset
        if len(type_offsets) % 2 != 0:
            base_reloc.num_of_type_offsets = len(type_offsets) + 1
            base_reloc.has_padding = True
        else:
            base_reloc.num_of_type_offsets = len(type_offsets)
            base_reloc.has_padding = False
        base_reloc.size_of_block = cls.sizeof + base_reloc.num_of_type_offsets * 2
        base_reloc.type_offsets = type_offsets
        return base_reloc

    def __repr__(self) -> str:
        return f'Virtual Address: {hex(self.virtual_address)} | size of Block: {hex(self.size_of_block)} | ' \
               f'Num of Type Offsets: {self.num_of_type_offsets}\n' \
               f'Type Offsest: {[hex(offset) for offset in self.type_offsets]}'

    def dump(self) -> bytearray:
        # empty bytes at the end for padding
        packed_base_relocation = bytearray(struct.pack('<II' + 'H'*(len(self.type_offsets)), self.virtual_address,
                                                       self.size_of_block,
                                                       *[rva - self.virtual_address for rva in self.type_offsets]))
        if self.has_padding:
            packed_base_relocation += b'\x00\x00'
        return packed_base_relocation

