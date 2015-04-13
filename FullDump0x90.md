
```
----------Parsing Warnings----------

Suspicious NumberOfRvaAndSizes in the Optional Header. Normal values are never larger than 0x10, the value is: 0xdfffddde

Error parsing section 2. SizeOfRawData is larger than file.

----------DOS_HEADER----------

[IMAGE_DOS_HEADER]
e_magic:                       0x5A4D    
e_cblp:                        0x50      
e_cp:                          0x2       
e_crlc:                        0x0       
e_cparhdr:                     0x4       
e_minalloc:                    0xF       
e_maxalloc:                    0xFFFF    
e_ss:                          0x0       
e_sp:                          0xB8      
e_csum:                        0x0       
e_ip:                          0x0       
e_cs:                          0x0       
e_lfarlc:                      0x40      
e_ovno:                        0x1A      
e_res:                         
e_oemid:                       0x0       
e_oeminfo:                     0x0       
e_res2:                        
e_lfanew:                      0x100     

----------NT_HEADERS----------

[IMAGE_NT_HEADERS]
Signature:                     0x4550    

----------FILE_HEADER----------

[IMAGE_FILE_HEADER]
Machine:                       0x14C     
NumberOfSections:              0x4       
TimeDateStamp:                 0x851C3163 [INVALID TIME]
PointerToSymbolTable:          0x74726144
NumberOfSymbols:               0x455068  
SizeOfOptionalHeader:          0xE0      
Characteristics:               0x818F    
Flags: LOCAL_SYMS_STRIPPED, 32BIT_MACHINE, BYTES_REVERSED_LO, EXECUTABLE_IMAGE, LINE_NUMS_STRIPPED, BYTES_REVERSED_HI, RELOCS_STRIPPED

----------OPTIONAL_HEADER----------

[IMAGE_OPTIONAL_HEADER]
Magic:                         0x10B     
MajorLinkerVersion:            0x2       
MinorLinkerVersion:            0x19      
SizeOfCode:                    0x200     
SizeOfInitializedData:         0x45400   
SizeOfUninitializedData:       0x0       
AddressOfEntryPoint:           0x2000    
BaseOfCode:                    0x1000    
BaseOfData:                    0x2000    
ImageBase:                     0xDE0000  
SectionAlignment:              0x1000    
FileAlignment:                 0x1000    
MajorOperatingSystemVersion:   0x1       
MinorOperatingSystemVersion:   0x0       
MajorImageVersion:             0x0       
MinorImageVersion:             0x0       
MajorSubsystemVersion:         0x4       
MinorSubsystemVersion:         0x0       
Reserved1:                     0x0       
SizeOfImage:                   0x49000   
SizeOfHeaders:                 0x1000    
CheckSum:                      0x0       
Subsystem:                     0x3       
DllCharacteristics:            0x0       
SizeOfStackReserve:            0x100000  
SizeOfStackCommit:             0x2000    
SizeOfHeapReserve:             0x100000  
SizeOfHeapCommit:              0x1000    
LoaderFlags:                   0xABDBFFDE
NumberOfRvaAndSizes:           0xDFFFDDDE

----------PE Sections----------

[IMAGE_SECTION_HEADER]
Name:                          CODE
Misc:                          0x1000    
Misc_PhysicalAddress:          0x1000    
Misc_VirtualSize:              0x1000    
VirtualAddress:                0x1000    
SizeOfRawData:                 0x1000    
PointerToRawData:              0x1000    
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0xE0000020
Flags: MEM_WRITE, CNT_CODE, MEM_EXECUTE, MEM_READ
Entropy: 0.061089 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          DATA
Misc:                          0x45000   
Misc_PhysicalAddress:          0x45000   
Misc_VirtualSize:              0x45000   
VirtualAddress:                0x2000    
SizeOfRawData:                 0x45000   
PointerToRawData:              0x2000    
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0xC0000040
Flags: MEM_WRITE, CNT_INITIALIZED_DATA, MEM_READ
Entropy: 7.980693 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          NicolasB
Misc:                          0x1000    
Misc_PhysicalAddress:          0x1000    
Misc_VirtualSize:              0x1000    
VirtualAddress:                0x47000   
SizeOfRawData:                 0xEFEFADFF
PointerToRawData:              0x47000   
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0xC0000040
Flags: MEM_WRITE, CNT_INITIALIZED_DATA, MEM_READ
Entropy: 0.607433 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          .idata
Misc:                          0x1000    
Misc_PhysicalAddress:          0x1000    
Misc_VirtualSize:              0x1000    
VirtualAddress:                0x48000   
SizeOfRawData:                 0x1000    
PointerToRawData:              0x47000   
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0xC0000040
Flags: MEM_WRITE, CNT_INITIALIZED_DATA, MEM_READ
Entropy: 0.607433 (Min=0.0, Max=8.0)

----------Directories----------

[IMAGE_DIRECTORY_ENTRY_EXPORT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_IMPORT]
VirtualAddress:                0x48000   
Size:                          0xBE      
[IMAGE_DIRECTORY_ENTRY_RESOURCE]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_EXCEPTION]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_SECURITY]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_BASERELOC]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_DEBUG]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_COPYRIGHT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_GLOBALPTR]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_TLS]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_IAT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_RESERVED]
VirtualAddress:                0x0       
Size:                          0x0       

----------Imported symbols----------

[IMAGE_IMPORT_DESCRIPTOR]
OriginalFirstThunk:            0x4803C   
Characteristics:               0x4803C   
TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
ForwarderChain:                0x0       
Name:                          0x4806C   
FirstThunk:                    0x48054   

msvcrt.dll.printf Ord[740] Bound: 0x77C1186A

[IMAGE_IMPORT_DESCRIPTOR]
OriginalFirstThunk:            0x48044   
Characteristics:               0x48044   
TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
ForwarderChain:                0x0       
Name:                          0x48077   
FirstThunk:                    0x4805C   

KERNEL32.dll.GetTickCount Ord[458] Bound: 0x7C8092AC
KERNEL32.dll.GetCommandLineA Ord[258] Bound: 0x7C812C8D
KERNEL32.dll.ExitProcess Ord[175] Bound: 0x7C81CAA2
```