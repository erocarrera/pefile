
```
----------Parsing Warnings----------

Suspicious NumberOfRvaAndSizes in the Optional Header. Normal values are never larger than 0x10, the value is: 0x32334c45

Error parsing the import table. Invalid data at RVA: 0x400000

Error parsing the Import directory. Invalid Import data at RVA: 0x60

Error parsing export directory at RVA: 0x6c6c642e

----------DOS_HEADER----------

[IMAGE_DOS_HEADER]
e_magic:                       0x5A4D    
e_cblp:                        0x0       
e_cp:                          0x4550    
e_crlc:                        0x0       
e_cparhdr:                     0x14C     
e_minalloc:                    0x1       
e_maxalloc:                    0x2A6A    
e_ss:                          0xC358    
e_sp:                          0x0       
e_csum:                        0x0       
e_ip:                          0x0       
e_cs:                          0x0       
e_lfarlc:                      0x4       
e_ovno:                        0x103     
e_res:                         Ä
e_oemid:                       0x0       
e_oeminfo:                     0x0       
e_res2:                        yy@
e_lfanew:                      0x4       

----------NT_HEADERS----------

[IMAGE_NT_HEADERS]
Signature:                     0x4550    

----------FILE_HEADER----------

[IMAGE_FILE_HEADER]
Machine:                       0x14C     
NumberOfSections:              0x1       
TimeDateStamp:                 0xC3582A6A [INVALID TIME]
PointerToSymbolTable:          0x0       
NumberOfSymbols:               0x0       
SizeOfOptionalHeader:          0x4       
Characteristics:               0x103     
Flags: 32BIT_MACHINE, EXECUTABLE_IMAGE, RELOCS_STRIPPED

----------OPTIONAL_HEADER----------

[IMAGE_OPTIONAL_HEADER]
Magic:                         0x10B     
MajorLinkerVersion:            0x8       
MinorLinkerVersion:            0x0       
SizeOfCode:                    0x80000001
SizeOfInitializedData:         0x0       
SizeOfUninitializedData:       0x79      
AddressOfEntryPoint:           0xC       
BaseOfCode:                    0x79      
BaseOfData:                    0xC       
ImageBase:                     0x400000  
SectionAlignment:              0x4       
FileAlignment:                 0x4       
MajorOperatingSystemVersion:   0x74      
MinorOperatingSystemVersion:   0x0       
MajorImageVersion:             0x20      
MinorImageVersion:             0x0       
MajorSubsystemVersion:         0x4       
MinorSubsystemVersion:         0x0       
Reserved1:                     0x0       
SizeOfImage:                   0x104     
SizeOfHeaders:                 0x88      
CheckSum:                      0x0       
Subsystem:                     0x2       
DllCharacteristics:            0x0       
SizeOfStackReserve:            0x0       
SizeOfStackCommit:             0x0       
SizeOfHeapReserve:             0x0       
SizeOfHeapCommit:              0x0       
LoaderFlags:                   0x4E52454B
NumberOfRvaAndSizes:           0x32334C45

----------PE Sections----------

[IMAGE_SECTION_HEADER]
Name:                          Ä
Misc:                          0x79      
Misc_PhysicalAddress:          0x79      
Misc_VirtualSize:              0x79      
VirtualAddress:                0xC       
SizeOfRawData:                 0x79      
PointerToRawData:              0xC       
PointerToRelocations:          0x400000  
PointerToLinenumbers:          0x4       
NumberOfRelocations:           0x4       
NumberOfLinenumbers:           0x0       
Characteristics:               0x74      
Flags: CNT_CODE, CNT_INITIALIZED_DATA
Entropy: 2.382261 (Min=0.0, Max=8.0)

----------Directories----------

[IMAGE_DIRECTORY_ENTRY_EXPORT]
VirtualAddress:                0x6C6C642E
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_IMPORT]
VirtualAddress:                0x38      
Size:                          0x0       

----------Imported symbols----------

[IMAGE_IMPORT_DESCRIPTOR]
OriginalFirstThunk:            0x400000  
Characteristics:               0x400000  
TimeDateStamp:                 0x4        [Wed Dec 31 16:00:04 1969]
ForwarderChain:                0x4       
Name:                          0x74      
FirstThunk:                    0x20      

KERNEL32.dll.None Ord[1]
```