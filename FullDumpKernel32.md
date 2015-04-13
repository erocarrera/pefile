
```
----------DOS_HEADER----------

[IMAGE_DOS_HEADER]
e_magic:                       0x5A4D    
e_cblp:                        0x90      
e_cp:                          0x3       
e_crlc:                        0x0       
e_cparhdr:                     0x4       
e_minalloc:                    0x0       
e_maxalloc:                    0xFFFF    
e_ss:                          0x0       
e_sp:                          0xB8      
e_csum:                        0x0       
e_ip:                          0x0       
e_cs:                          0x0       
e_lfarlc:                      0x40      
e_ovno:                        0x0       
e_res:                         
e_oemid:                       0x0       
e_oeminfo:                     0x0       
e_res2:                        
e_lfanew:                      0xF8      

----------NT_HEADERS----------

[IMAGE_NT_HEADERS]
Signature:                     0x4550    

----------FILE_HEADER----------

[IMAGE_FILE_HEADER]
Machine:                       0x14C     
NumberOfSections:              0x4       
TimeDateStamp:                 0x3B7DFE0E [Fri Aug 17 22:33:02 2001]
PointerToSymbolTable:          0x0       
NumberOfSymbols:               0x0       
SizeOfOptionalHeader:          0xE0      
Characteristics:               0x210E    
Flags: LOCAL_SYMS_STRIPPED, 32BIT_MACHINE, EXECUTABLE_IMAGE, DLL, LINE_NUMS_STRIPPED

----------OPTIONAL_HEADER----------

[IMAGE_OPTIONAL_HEADER]
Magic:                         0x10B     
MajorLinkerVersion:            0x7       
MinorLinkerVersion:            0x0       
SizeOfCode:                    0x74800   
SizeOfInitializedData:         0x6DE00   
SizeOfUninitializedData:       0x0       
AddressOfEntryPoint:           0x1A241   
BaseOfCode:                    0x1000    
BaseOfData:                    0x71000   
ImageBase:                     0x77E60000
SectionAlignment:              0x1000    
FileAlignment:                 0x200     
MajorOperatingSystemVersion:   0x5       
MinorOperatingSystemVersion:   0x1       
MajorImageVersion:             0x5       
MinorImageVersion:             0x1       
MajorSubsystemVersion:         0x4       
MinorSubsystemVersion:         0x0       
Reserved1:                     0x0       
SizeOfImage:                   0xE5000   
SizeOfHeaders:                 0x400     
CheckSum:                      0xE8792   
Subsystem:                     0x3       
DllCharacteristics:            0x0       
SizeOfStackReserve:            0x40000   
SizeOfStackCommit:             0x1000    
SizeOfHeapReserve:             0x100000  
SizeOfHeapCommit:              0x1000    
LoaderFlags:                   0x0       
NumberOfRvaAndSizes:           0x10      

----------PE Sections----------

[IMAGE_SECTION_HEADER]
Name:                          .text
Misc:                          0x74658   
Misc_PhysicalAddress:          0x74658   
Misc_VirtualSize:              0x74658   
VirtualAddress:                0x1000    
SizeOfRawData:                 0x74800   
PointerToRawData:              0x400     
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0x60000020
Flags: CNT_CODE, MEM_EXECUTE, MEM_READ
Entropy: 6.763254 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          .data
Misc:                          0x28CA    
Misc_PhysicalAddress:          0x28CA    
Misc_VirtualSize:              0x28CA    
VirtualAddress:                0x76000   
SizeOfRawData:                 0x2400    
PointerToRawData:              0x74C00   
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0xC0000040
Flags: MEM_WRITE, CNT_INITIALIZED_DATA, MEM_READ
Entropy: 0.752896 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          .rsrc
Misc:                          0x65ED8   
Misc_PhysicalAddress:          0x65ED8   
Misc_VirtualSize:              0x65ED8   
VirtualAddress:                0x79000   
SizeOfRawData:                 0x66000   
PointerToRawData:              0x77000   
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0x40000040
Flags: CNT_INITIALIZED_DATA, MEM_READ
Entropy: 3.389887 (Min=0.0, Max=8.0)

[IMAGE_SECTION_HEADER]
Name:                          .reloc
Misc:                          0x5310    
Misc_PhysicalAddress:          0x5310    
Misc_VirtualSize:              0x5310    
VirtualAddress:                0xDF000   
SizeOfRawData:                 0x5400    
PointerToRawData:              0xDD000   
PointerToRelocations:          0x0       
PointerToLinenumbers:          0x0       
NumberOfRelocations:           0x0       
NumberOfLinenumbers:           0x0       
Characteristics:               0x42000040
Flags: CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ
Entropy: 6.624523 (Min=0.0, Max=8.0)

----------Directories----------

[IMAGE_DIRECTORY_ENTRY_EXPORT]
VirtualAddress:                0x22140   
Size:                          0x6988    
[IMAGE_DIRECTORY_ENTRY_IMPORT]
VirtualAddress:                0x72DC4   
Size:                          0x28      
[IMAGE_DIRECTORY_ENTRY_RESOURCE]
VirtualAddress:                0x79000   
Size:                          0x65ED8   
[IMAGE_DIRECTORY_ENTRY_EXCEPTION]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_SECURITY]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_BASERELOC]
VirtualAddress:                0xDF000   
Size:                          0x5310    
[IMAGE_DIRECTORY_ENTRY_DEBUG]
VirtualAddress:                0x75620   
Size:                          0x38      
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
VirtualAddress:                0x766A8   
Size:                          0x40      
[IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT]
VirtualAddress:                0x290     
Size:                          0x1C      
[IMAGE_DIRECTORY_ENTRY_IAT]
VirtualAddress:                0x1000    
Size:                          0x608     
[IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR]
VirtualAddress:                0x0       
Size:                          0x0       
[IMAGE_DIRECTORY_ENTRY_RESERVED]
VirtualAddress:                0x0       
Size:                          0x0       

----------Version Information----------

[VS_VERSIONINFO]
Length:                        0x38C     
ValueLength:                   0x34      
Type:                          0x0       

[VS_FIXEDFILEINFO]
Signature:                     0xFEEF04BD
StrucVersion:                  0x10000   
FileVersionMS:                 0x50001   
FileVersionLS:                 0xA280000 
ProductVersionMS:              0x50001   
ProductVersionLS:              0xA280000 
FileFlagsMask:                 0x3F      
FileFlags:                     0x0       
FileOS:                        0x40004   
FileType:                      0x2       
FileSubtype:                   0x0       
FileDateMS:                    0x0       
FileDateLS:                    0x0       

[StringFileInfo]
Length:                        0x2EA     
ValueLength:                   0x0       
Type:                          0x1       

  [StringTable]
  Length:                        0x2C6     
  ValueLength:                   0x0       
  Type:                          0x1       
  LangID: 040904B0

    LegalCopyright: u'\xa9' Microsoft Corporation. All rights reserved.
    InternalName: kernel32
    FileVersion: 5.1.2600.0 (xpclient.010817-1148)
    CompanyName: Microsoft Corporation
    ProductName: Microsoftu'\xae' Windowsu'\xae' Operating System
    ProductVersion: 5.1.2600.0
    FileDescription: Windows NT BASE API Client DLL
    OriginalFilename: kernel32

[VarFileInfo]
Length:                        0x44      
ValueLength:                   0x0       
Type:                          0x1       

  [Var]
  Length:                        0x24      
  ValueLength:                   0x4       
  Type:                          0x0       
    Translation: 0x0409 0x04b0

----------Exported symbols----------

[IMAGE_EXPORT_DIRECTORY]
Characteristics:               0x0       
TimeDateStamp:                 0x3B7DDFD8 [Fri Aug 17 20:24:08 2001]
MajorVersion:                  0x0       
MinorVersion:                  0x0       
Name:                          0x245A8   
Base:                          0x1       
NumberOfFunctions:             0x3A0     
NumberOfNames:                 0x3A0     
AddressOfFunctions:            0x22168   
AddressOfNames:                0x22FE8   
AddressOfNameOrdinals:         0x23E68   

Ordinal      RVA         Name
1          0x00012ADAh    ActivateActCtx
2          0x000082C2h    AddAtomA
3          0x0000D39Fh    AddAtomW
4          0x00065B2Dh    AddConsoleAliasA
5          0x00065AF6h    AddConsoleAliasW
6          0x00052A10h    AddLocalAlternateComputerNameA
7          0x000528FBh    AddLocalAlternateComputerNameW
8          0x00060FFAh    AddRefActCtx
9          0x000287FCh    AddVectoredExceptionHandler forwarder: NTDLL.RtlAddVectoredExceptionHandler
10         0x00066036h    AllocConsole
11         0x00056A36h    AllocateUserPhysicalPages
12         0x0000460Ah    AreFileApisANSI
13         0x0003A305h    AssignProcessToJobObject
14         0x000661E1h    AttachConsole
15         0x00050BF1h    BackupRead
16         0x0004FD9Ch    BackupSeek
17         0x000511D4h    BackupWrite
18         0x0001CF25h    BaseCheckAppcompatCache
19         0x00061349h    BaseCleanupAppcompatCache
20         0x000613C6h    BaseCleanupAppcompatCacheSupport
21         0x000612A2h    BaseDumpAppcompatCache
22         0x0006123Fh    BaseFlushAppcompatCache
23         0x0001D071h    BaseInitAppcompatCache
24         0x0003618Ch    BaseInitAppcompatCacheSupport
25         0x0001CA5Fh    BaseProcessInitPostImport
26         0x00008795h    BaseUpdateAppcompatCache
27         0x00002D7Ah    Beep
28         0x00064FCEh    BeginUpdateResourceA
29         0x00064E82h    BeginUpdateResourceW
30         0x00036C14h    BindIoCompletionCallback
31         0x000608AEh    BuildCommDCBA
32         0x00060888h    BuildCommDCBAndTimeoutsA
33         0x000608D9h    BuildCommDCBAndTimeoutsW
34         0x0006092Ch    BuildCommDCBW
35         0x00057A07h    CallNamedPipeA
36         0x00057856h    CallNamedPipeW
37         0x000583FCh    CancelDeviceWakeupRequest
38         0x00038CFFh    CancelIo
39         0x0005A103h    CancelTimerQueueTimer
40         0x00036E29h    CancelWaitableTimer
41         0x0000DB09h    ChangeTimerQueueTimer
42         0x0005CFE1h    ClearCommBreak
43         0x0005BAC8h    ClearCommError
44         0x000200CDh    CloseConsoleHandle
45         0x00017963h    CloseHandle
46         0x00036C75h    CloseProfileUserMapping
47         0x0003815Eh    CmdBatNotification
48         0x0005CC32h    CommConfigDialogA
49         0x0005CB78h    CommConfigDialogW
50         0x00011702h    CompareFileTime
51         0x000162D0h    CompareStringA
52         0x00017F2Eh    CompareStringW
53         0x000139BBh    ConnectNamedPipe
54         0x0006678Bh    ConsoleMenuControl
55         0x00053AC1h    ContinueDebugEvent
56         0x00003607h    ConvertDefaultLocale
57         0x000396DBh    ConvertFiberToThread
58         0x000397E0h    ConvertThreadToFiber
59         0x0000BD13h    CopyFileA
60         0x000567A9h    CopyFileExA
61         0x0000B350h    CopyFileExW
62         0x00003181h    CopyFileW
63         0x00052E6Dh    CopyLZFile
64         0x00037896h    CreateActCtxA
65         0x00008BECh    CreateActCtxW
66         0x00067498h    CreateConsoleScreenBuffer
67         0x0000808Fh    CreateDirectoryA
68         0x000544BCh    CreateDirectoryExA
69         0x00053B3Eh    CreateDirectoryExW
70         0x00007EFFh    CreateDirectoryW
71         0x000137DEh    CreateEventA
72         0x000130C1h    CreateEventW
73         0x00039715h    CreateFiber
74         0x0003972Dh    CreateFiberEx
75         0x0001A837h    CreateFileA
76         0x00017797h    CreateFileMappingA
77         0x000176D3h    CreateFileMappingW
78         0x000179B1h    CreateFileW
79         0x00060F41h    CreateHardLinkA
80         0x00060DA4h    CreateHardLinkW
81         0x00013B75h    CreateIoCompletionPort
82         0x00060CD2h    CreateJobObjectA
83         0x0003A24Ah    CreateJobObjectW
84         0x00060CACh    CreateJobSet
85         0x00014398h    CreateMailslotA
86         0x000143E2h    CreateMailslotW
87         0x00058B54h    CreateMemoryResourceNotification
88         0x0001C2C4h    CreateMutexA
89         0x0001C243h    CreateMutexW
90         0x00036726h    CreateNamedPipeA
91         0x0000DBF0h    CreateNamedPipeW
92         0x0001727Ah    CreatePipe
93         0x00001BB8h    CreateProcessA
94         0x00008A46h    CreateProcessInternalA
95         0x0001D9F2h    CreateProcessInternalW
96         0x00001B8Ah    CreateProcessW
97         0x0001AA83h    CreateRemoteThread
98         0x00009E9Dh    CreateSemaphoreA
99         0x0000C714h    CreateSemaphoreW
100        0x00060FA0h    CreateSocketHandle
101        0x00060ADAh    CreateTapePartition
102        0x0001AC37h    CreateThread
103        0x00036E4Ch    CreateTimerQueue
104        0x000395BEh    CreateTimerQueueTimer
105        0x0005B1E7h    CreateToolhelp32Snapshot
106        0x0001F1F6h    CreateVirtualBuffer
107        0x00038D29h    CreateWaitableTimerA
108        0x000398F1h    CreateWaitableTimerW
109        0x00012AAEh    DeactivateActCtx
110        0x00053709h    DebugActiveProcess
111        0x00053AFEh    DebugActiveProcessStop
112        0x000536A5h    DebugBreak
113        0x00053754h    DebugBreakProcess
114        0x00053771h    DebugSetProcessKillOnExit
115        0x00054E53h    DefineDosDeviceA
116        0x00039FE1h    DefineDosDeviceW
117        0x0006F0B8h    DelayLoadFailureHook
118        0x0000D505h    DeleteAtom
119        0x00028821h    DeleteCriticalSection forwarder: NTDLL.RtlDeleteCriticalSection
120        0x0003968Fh    DeleteFiber
121        0x00013628h    DeleteFileA
122        0x0001350Eh    DeleteFileW
123        0x0005A0DFh    DeleteTimerQueue
124        0x0005A09Fh    DeleteTimerQueueEx
125        0x00039843h    DeleteTimerQueueTimer
126        0x0005FBE8h    DeleteVolumeMountPointA
127        0x0005F4FFh    DeleteVolumeMountPointW
128        0x00013D45h    DeviceIoControl
129        0x0001C313h    DisableThreadLibraryCalls
130        0x00014050h    DisconnectNamedPipe
131        0x00052277h    DnsHostnameToComputerNameA
132        0x0000D959h    DnsHostnameToComputerNameW
133        0x00014548h    DosDateTimeToFileTime
134        0x00058C1Eh    DosPathToSessionPathA
135        0x0003AFFCh    DosPathToSessionPathW
136        0x00020052h    DuplicateConsoleHandle
137        0x00019CE3h    DuplicateHandle
138        0x00064D1Ah    EndUpdateResourceA
139        0x00064B9Dh    EndUpdateResourceW
140        0x00028840h    EnterCriticalSection forwarder: NTDLL.RtlEnterCriticalSection
141        0x00069262h    EnumCalendarInfoA
142        0x0006927Eh    EnumCalendarInfoExA
143        0x0006B2AFh    EnumCalendarInfoExW
144        0x0006B293h    EnumCalendarInfoW
145        0x000692B0h    EnumDateFormatsA
146        0x000692C8h    EnumDateFormatsExA
147        0x0006B2CBh    EnumDateFormatsExW
148        0x00003C9Eh    EnumDateFormatsW
149        0x000692F6h    EnumLanguageGroupLocalesA
150        0x0006B267h    EnumLanguageGroupLocalesW
151        0x000571D0h    EnumResourceLanguagesA
152        0x0003B67Bh    EnumResourceLanguagesW
153        0x0003A9BEh    EnumResourceNamesA
154        0x0004F6E2h    EnumResourceNamesW
155        0x00057002h    EnumResourceTypesA
156        0x00057306h    EnumResourceTypesW
157        0x00069326h    EnumSystemCodePagesA
158        0x0006B281h    EnumSystemCodePagesW
159        0x0006B676h    EnumSystemGeoID
160        0x000692E0h    EnumSystemLanguageGroupsA
161        0x0006B251h    EnumSystemLanguageGroupsW
162        0x0000363Bh    EnumSystemLocalesA
163        0x0003C50Fh    EnumSystemLocalesW
164        0x0006929Ah    EnumTimeFormatsA
165        0x00003D78h    EnumTimeFormatsW
166        0x00069310h    EnumUILanguagesA
167        0x0003747Bh    EnumUILanguagesW
168        0x000521D2h    EnumerateLocalComputerNamesA
169        0x00052059h    EnumerateLocalComputerNamesW
170        0x00060AAEh    EraseTape
171        0x0005BCCCh    EscapeCommFunction
172        0x00015CB5h    ExitProcess
173        0x00013C49h    ExitThread
174        0x0005D7E8h    ExitVDM
175        0x000068D9h    ExpandEnvironmentStringsA
176        0x0001152Ch    ExpandEnvironmentStringsW
177        0x00065613h    ExpungeConsoleCommandHistoryA
178        0x00065605h    ExpungeConsoleCommandHistoryW
179        0x00056ED2h    ExtendVirtualBuffer
180        0x00058503h    FatalAppExitA
181        0x000584BBh    FatalAppExitW
182        0x0005854Bh    FatalExit
183        0x00013E18h    FileTimeToDosDateTime
184        0x000194BFh    FileTimeToLocalFileTime
185        0x00019424h    FileTimeToSystemTime
186        0x0003AE22h    FillConsoleOutputAttribute
187        0x00067478h    FillConsoleOutputCharacterA
188        0x0003BF1Ah    FillConsoleOutputCharacterW
189        0x00010AC9h    FindActCtxSectionGuid
190        0x0006101Eh    FindActCtxSectionStringA
191        0x0000E449h    FindActCtxSectionStringW
192        0x00004BAAh    FindAtomA
193        0x00038B86h    FindAtomW
194        0x00018EAAh    FindClose
195        0x00007997h    FindCloseChangeNotification
196        0x0003C2E2h    FindFirstChangeNotificationA
197        0x0000789Ch    FindFirstChangeNotificationW
198        0x00015D9Eh    FindFirstFileA
199        0x00054F29h    FindFirstFileExA
200        0x00018848h    FindFirstFileExW
201        0x00018A39h    FindFirstFileW
202        0x0005FD2Bh    FindFirstVolumeA
203        0x0005F8B5h    FindFirstVolumeMountPointA
204        0x0005EA7Fh    FindFirstVolumeMountPointW
205        0x00036A62h    FindFirstVolumeW
206        0x00006A40h    FindNextChangeNotification
207        0x00015E67h    FindNextFileA
208        0x0001F2C4h    FindNextFileW
209        0x0005F7C8h    FindNextVolumeA
210        0x0005F9B6h    FindNextVolumeMountPointA
211        0x0005ECCFh    FindNextVolumeMountPointW
212        0x000367BEh    FindNextVolumeW
213        0x0000CA8Ah    FindResourceA
214        0x0000E5A0h    FindResourceExA
215        0x0001614Ch    FindResourceExW
216        0x000110D8h    FindResourceW
217        0x0003678Dh    FindVolumeClose
218        0x00007997h    FindVolumeMountPointClose
219        0x00067D16h    FlushConsoleInputBuffer
220        0x00013FF9h    FlushFileBuffers
221        0x00004C09h    FlushInstructionCache
222        0x00007228h    FlushViewOfFile
223        0x00069A12h    FoldStringA
224        0x0003AB72h    FoldStringW
225        0x00016A60h    FormatMessageA
226        0x0001F295h    FormatMessageW
227        0x00065E29h    FreeConsole
228        0x0003C5B1h    FreeEnvironmentStringsA
229        0x0001C9E1h    FreeEnvironmentStringsW
230        0x00020618h    FreeLibrary
231        0x0000D93Dh    FreeLibraryAndExitThread
232        0x0000CB14h    FreeResource
233        0x00056A5Dh    FreeUserPhysicalPages
234        0x0001F1E1h    FreeVirtualBuffer
235        0x00067C51h    GenerateConsoleCtrlEvent
236        0x0001A13Fh    GetACP
237        0x0003C5CFh    GetAtomNameA
238        0x0000D4EDh    GetAtomNameW
239        0x0005DFF8h    GetBinaryType
240        0x0005DFF8h    GetBinaryTypeA
241        0x0005DC36h    GetBinaryTypeW
242        0x0001849Fh    GetCPInfo
243        0x00069B79h    GetCPInfoExA
244        0x0006CA21h    GetCPInfoExW
245        0x000693A1h    GetCalendarInfoA
246        0x000037A3h    GetCalendarInfoW
247        0x000611B0h    GetComPlusPackageInstallStatus
248        0x0005CFEFh    GetCommConfig
249        0x0005BD9Dh    GetCommMask
250        0x0005BE1Fh    GetCommModemStatus
251        0x0005BEA1h    GetCommProperties
252        0x0005BF52h    GetCommState
253        0x000380CDh    GetCommTimeouts
254        0x0001C938h    GetCommandLineA
255        0x0001C9DBh    GetCommandLineW
256        0x00055C48h    GetCompressedFileSizeA
257        0x00055B3Eh    GetCompressedFileSizeW
258        0x00005F4Ch    GetComputerNameA
259        0x00051F67h    GetComputerNameExA
260        0x00009BD7h    GetComputerNameExW
261        0x0000C324h    GetComputerNameW
262        0x000651CAh    GetConsoleAliasA
263        0x0006556Ch    GetConsoleAliasExesA
264        0x00065308h    GetConsoleAliasExesLengthA
265        0x00065300h    GetConsoleAliasExesLengthW
266        0x0006555Ah    GetConsoleAliasExesW
267        0x000651A5h    GetConsoleAliasW
268        0x00065448h    GetConsoleAliasesA
269        0x00065299h    GetConsoleAliasesLengthA
270        0x0006528Bh    GetConsoleAliasesLengthW
271        0x00065432h    GetConsoleAliasesW
272        0x000680CCh    GetConsoleCP
273        0x00068D93h    GetConsoleCharType
274        0x000658CEh    GetConsoleCommandHistoryA
275        0x00065783h    GetConsoleCommandHistoryLengthA
276        0x00065775h    GetConsoleCommandHistoryLengthW
277        0x000658B8h    GetConsoleCommandHistoryW
278        0x000678A5h    GetConsoleCursorInfo
279        0x00068670h    GetConsoleCursorMode
280        0x00002F09h    GetConsoleDisplayMode
281        0x00067A58h    GetConsoleFontInfo
282        0x00067B45h    GetConsoleFontSize
283        0x000664A6h    GetConsoleHardwareState
284        0x00065B63h    GetConsoleInputExeNameA
285        0x0006598Ch    GetConsoleInputExeNameW
286        0x000662A8h    GetConsoleInputWaitHandle
287        0x000682ACh    GetConsoleKeyboardLayoutNameA
288        0x000682BAh    GetConsoleKeyboardLayoutNameW
289        0x00019540h    GetConsoleMode
290        0x00068BDAh    GetConsoleNlsMode
291        0x000195BFh    GetConsoleOutputCP
292        0x00068319h    GetConsoleProcessList
293        0x00020121h    GetConsoleScreenBufferInfo
294        0x00067942h    GetConsoleSelectionInfo
295        0x000021ABh    GetConsoleTitleA
296        0x00017255h    GetConsoleTitleW
297        0x000682C8h    GetConsoleWindow
298        0x00069798h    GetCurrencyFormatA
299        0x0006D4A3h    GetCurrencyFormatW
300        0x0003B4C9h    GetCurrentActCtx
301        0x00067BAFh    GetCurrentConsoleFont
302        0x000105FCh    GetCurrentDirectoryA
303        0x00019E1Eh    GetCurrentDirectoryW
304        0x00019C90h    GetCurrentProcess
305        0x00020656h    GetCurrentProcessId
306        0x00013163h    GetCurrentThread
307        0x00017CC4h    GetCurrentThreadId
308        0x00004006h    GetDateFormatA
309        0x0001F849h    GetDateFormatW
310        0x0005CDA8h    GetDefaultCommConfigA
311        0x0005CCEEh    GetDefaultCommConfigW
312        0x0006E1FCh    GetDefaultSortkeySize
313        0x00058397h    GetDevicePowerState
314        0x0000869Bh    GetDiskFreeSpaceA
315        0x000086CCh    GetDiskFreeSpaceExA
316        0x000207B9h    GetDiskFreeSpaceExW
317        0x00008564h    GetDiskFreeSpaceW
318        0x0000C0E3h    GetDriveTypeA
319        0x00017E16h    GetDriveTypeW
320        0x00007702h    GetEnvironmentStrings
321        0x00007702h    GetEnvironmentStringsA
322        0x00017EE1h    GetEnvironmentStringsW
323        0x0001AC5Eh    GetEnvironmentVariableA
324        0x00018147h    GetEnvironmentVariableW
325        0x0001FF65h    GetExitCodeProcess
326        0x0000C9E0h    GetExitCodeThread
327        0x0005B268h    GetExpandedNameA
328        0x0005B2F1h    GetExpandedNameW
329        0x00014CABh    GetFileAttributesA
330        0x00013DF8h    GetFileAttributesExA
331        0x000138C5h    GetFileAttributesExW
332        0x00018536h    GetFileAttributesW
333        0x00012EA0h    GetFileInformationByHandle
334        0x000193EFh    GetFileSize
335        0x000193B7h    GetFileSizeEx
336        0x00013CE2h    GetFileTime
337        0x00018406h    GetFileType
338        0x000568DAh    GetFirmwareEnvironmentVariableA
339        0x000567FBh    GetFirmwareEnvironmentVariableW
340        0x00020357h    GetFullPathNameA
341        0x000181DBh    GetFullPathNameW
342        0x00069338h    GetGeoInfoA
343        0x0006B361h    GetGeoInfoW
344        0x00060F94h    GetHandleContext
345        0x00056B2Ah    GetHandleInformation
346        0x000684FFh    GetLargestConsoleWindowSize
347        0x0002885Eh    GetLastError forwarder: NTDLL.RtlGetLastWin32Error
348        0x0006E21Ch    GetLinguistLangSize
349        0x00010F89h    GetLocalTime
350        0x0001513Ch    GetLocaleInfoA
351        0x00018723h    GetLocaleInfoW
352        0x00036645h    GetLogicalDriveStringsA
353        0x0003B379h    GetLogicalDriveStringsW
354        0x0000C29Dh    GetLogicalDrives
355        0x0003B13Dh    GetLongPathNameA
356        0x00018FF4h    GetLongPathNameW
357        0x00056E3Dh    GetMailslotInfo
358        0x0001A099h    GetModuleFileNameA
359        0x00019FC8h    GetModuleFileNameW
360        0x00019F93h    GetModuleHandleA
361        0x00056FB3h    GetModuleHandleExA
362        0x00037E0Ah    GetModuleHandleExW
363        0x0001A663h    GetModuleHandleW
364        0x0005792Bh    GetNamedPipeHandleStateA
365        0x00057763h    GetNamedPipeHandleStateW
366        0x000575A6h    GetNamedPipeInfo
367        0x000587F2h    GetNativeSystemInfo
368        0x0005D21Bh    GetNextVDMCommand
369        0x0001B19Ch    GetNlsSectionName
370        0x00057BD2h    GetNumaAvailableMemory
371        0x00057C11h    GetNumaAvailableMemoryNode
372        0x00057A73h    GetNumaHighestNodeNumber
373        0x00057B39h    GetNumaNodeProcessorMask
374        0x00057B93h    GetNumaProcessorMap
375        0x00057AB7h    GetNumaProcessorNode
376        0x00069569h    GetNumberFormatA
377        0x000079F8h    GetNumberFormatW
378        0x0006841Bh    GetNumberOfConsoleFonts
379        0x0006846Ch    GetNumberOfConsoleInputEvents
380        0x000679CEh    GetNumberOfConsoleMouseButtons
381        0x0000C703h    GetOEMCP
382        0x0000D62Ch    GetOverlappedResult
383        0x0003A7ACh    GetPriorityClass
384        0x000119F3h    GetPrivateProfileIntA
385        0x00006FC5h    GetPrivateProfileIntW
386        0x00002050h    GetPrivateProfileSectionA
387        0x00001FD2h    GetPrivateProfileSectionNamesA
388        0x0005489Dh    GetPrivateProfileSectionNamesW
389        0x0000FD6Bh    GetPrivateProfileSectionW
390        0x00012C64h    GetPrivateProfileStringA
391        0x0000A9AAh    GetPrivateProfileStringW
392        0x000548B6h    GetPrivateProfileStructA
393        0x000549BEh    GetPrivateProfileStructW
394        0x0001A5FDh    GetProcAddress
395        0x00006ADCh    GetProcessAffinityMask
396        0x00017CB7h    GetProcessHeap
397        0x0003C532h    GetProcessHeaps
398        0x000586A1h    GetProcessIoCounters
399        0x0005866Eh    GetProcessPriorityBoost
400        0x000585FDh    GetProcessShutdownParameters
401        0x00036FF8h    GetProcessTimes
402        0x0001C334h    GetProcessVersion
403        0x00002233h    GetProcessWorkingSetSize
404        0x0000C904h    GetProfileIntA
405        0x000041D5h    GetProfileIntW
406        0x00054CD6h    GetProfileSectionA
407        0x0003A3BEh    GetProfileSectionW
408        0x0000A907h    GetProfileStringA
409        0x00007FD7h    GetProfileStringW
410        0x00013B18h    GetQueuedCompletionStatus
411        0x0000C10Bh    GetShortPathNameA
412        0x0000BE92h    GetShortPathNameW
413        0x0000177Ah    GetStartupInfoA
414        0x000016E6h    GetStartupInfoW
415        0x00019C3Dh    GetStdHandle
416        0x000041EBh    GetStringTypeA
417        0x00038D20h    GetStringTypeExA
418        0x00009E3Ah    GetStringTypeExW
419        0x0001C866h    GetStringTypeW
420        0x0000FCCDh    GetSystemDefaultLCID
421        0x00009B87h    GetSystemDefaultLangID
422        0x00018A4Fh    GetSystemDefaultUILanguage
423        0x000104FCh    GetSystemDirectoryA
424        0x0000A961h    GetSystemDirectoryW
425        0x0001C3A5h    GetSystemInfo
426        0x0000E1B4h    GetSystemPowerStatus
427        0x00001608h    GetSystemTime
428        0x00037149h    GetSystemTimeAdjustment
429        0x0000167Bh    GetSystemTimeAsFileTime
430        0x00010556h    GetSystemWindowsDirectoryA
431        0x0001606Ch    GetSystemWindowsDirectoryW
432        0x000383C8h    GetSystemWow64DirectoryA
433        0x000383C8h    GetSystemWow64DirectoryW
434        0x00060B40h    GetTapeParameters
435        0x00060A2Ah    GetTapePosition
436        0x00060BCFh    GetTapeStatus
437        0x0000AF8Fh    GetTempFileNameA
438        0x0000AE12h    GetTempFileNameW
439        0x0000AD34h    GetTempPathA
440        0x0000AD12h    GetTempPathW
441        0x00037F16h    GetThreadContext
442        0x00017F21h    GetThreadLocale
443        0x00013087h    GetThreadPriority
444        0x00059920h    GetThreadPriorityBoost
445        0x000537B5h    GetThreadSelectorEntry
446        0x0005A00Eh    GetThreadTimes
447        0x0001751Ah    GetTickCount
448        0x00004106h    GetTimeFormatA
449        0x0001F459h    GetTimeFormatW
450        0x00016E3Dh    GetTimeZoneInformation
451        0x00019C94h    GetUserDefaultLCID
452        0x00012D97h    GetUserDefaultLangID
453        0x00018A64h    GetUserDefaultUILanguage
454        0x0006B6F1h    GetUserGeoID
455        0x0005D947h    GetVDMCurrentDirectories
456        0x0001C486h    GetVersion
457        0x0001C657h    GetVersionExA
458        0x0001C61Ch    GetVersionExW
459        0x000081EFh    GetVolumeInformationA
460        0x0002094Fh    GetVolumeInformationW
461        0x0005FAA3h    GetVolumeNameForVolumeMountPointA
462        0x0000A3DBh    GetVolumeNameForVolumeMountPointW
463        0x00006E7Fh    GetVolumePathNameA
464        0x00006C73h    GetVolumePathNameW
465        0x0005FC00h    GetVolumePathNamesForVolumeNameA
466        0x0000A467h    GetVolumePathNamesForVolumeNameW
467        0x000105B0h    GetWindowsDirectoryA
468        0x000161DAh    GetWindowsDirectoryW
469        0x00056AD2h    GetWriteWatch
470        0x0000C674h    GlobalAddAtomA
471        0x0000D36Bh    GlobalAddAtomW
472        0x000136A3h    GlobalAlloc
473        0x0003A9ADh    GlobalCompact
474        0x0000D28Ch    GlobalDeleteAtom
475        0x0000D229h    GlobalFindAtomA
476        0x0000D250h    GlobalFindAtomW
477        0x000569FEh    GlobalFix
478        0x0000C93Dh    GlobalFlags
479        0x00013803h    GlobalFree
480        0x00039F21h    GlobalGetAtomNameA
481        0x0000D4C2h    GlobalGetAtomNameW
482        0x00011B99h    GlobalHandle
483        0x0001166Fh    GlobalLock
484        0x00016C1Ah    GlobalMemoryStatus
485        0x00009756h    GlobalMemoryStatusEx
486        0x0000E341h    GlobalReAlloc
487        0x0000C879h    GlobalSize
488        0x00056A2Dh    GlobalUnWire
489        0x00056A11h    GlobalUnfix
490        0x00011B14h    GlobalUnlock
491        0x00056A24h    GlobalWire
492        0x0005A275h    Heap32First
493        0x0005A13Eh    Heap32ListFirst
494        0x0005A1E5h    Heap32ListNext
495        0x0005A388h    Heap32Next
496        0x00028879h    HeapAlloc forwarder: NTDLL.RtlAllocateHeap
497        0x0000CB19h    HeapCompact
498        0x0001C726h    HeapCreate
499        0x00056BEEh    HeapCreateTagsW
500        0x00016E0Bh    HeapDestroy
501        0x00056BC4h    HeapExtend
502        0x0002888Fh    HeapFree forwarder: NTDLL.RtlFreeHeap
503        0x00056CC4h    HeapLock
504        0x00056E11h    HeapQueryInformation
505        0x00056BF8h    HeapQueryTagW
506        0x000288A1h    HeapReAlloc forwarder: NTDLL.RtlReAllocateHeap
507        0x00056DE8h    HeapSetInformation
508        0x000288B9h    HeapSize forwarder: NTDLL.RtlSizeHeap
509        0x00056C02h    HeapSummary
510        0x00056CD7h    HeapUnlock
511        0x00056C57h    HeapUsage
512        0x0000C924h    HeapValidate
513        0x00056CEAh    HeapWalk
514        0x000365D4h    InitAtomTable
515        0x00019908h    InitializeCriticalSection
516        0x0001C706h    InitializeCriticalSectionAndSpinCount
517        0x000288CBh    InitializeSListHead forwarder: NTDLL.RtlInitializeSListHead
518        0x00019A26h    InterlockedCompareExchange
519        0x000178C5h    InterlockedDecrement
520        0x000175F1h    InterlockedExchange
521        0x00016B5Ch    InterlockedExchangeAdd
522        0x000288E8h    InterlockedFlushSList forwarder: NTDLL.RtlInterlockedFlushSList
523        0x000177EFh    InterlockedIncrement
524        0x00028907h    InterlockedPopEntrySList forwarder: NTDLL.RtlInterlockedPopEntrySList
525        0x00028929h    InterlockedPushEntrySList forwarder: NTDLL.RtlInterlockedPushEntrySList
526        0x000675F7h    InvalidateConsoleDIBits
527        0x0001176Ch    IsBadCodePtr
528        0x0000C91Fh    IsBadHugeReadPtr
529        0x0000C91Ah    IsBadHugeWritePtr
530        0x0001339Ch    IsBadReadPtr
531        0x000145CAh    IsBadStringPtrA
532        0x000141A0h    IsBadStringPtrW
533        0x00013196h    IsBadWritePtr
534        0x00014995h    IsDBCSLeadByte
535        0x000030ADh    IsDBCSLeadByteEx
536        0x00012E92h    IsDebuggerPresent
537        0x00060C7Ah    IsProcessInJob
538        0x0002063Fh    IsProcessorFeaturePresent
539        0x000583D4h    IsSystemResumeAutomatic
540        0x00015243h    IsValidCodePage
541        0x00069EEEh    IsValidLanguageGroup
542        0x000152B8h    IsValidLocale
543        0x00018A96h    IsValidUILanguage
544        0x00038B96h    IsWow64Process
545        0x00017405h    LCMapStringA
546        0x000181F9h    LCMapStringW
547        0x0005BA18h    LZClose
548        0x0005B9ABh    LZCloseFile
549        0x00052DBFh    LZCopy
550        0x0005B57Ch    LZCreateFileW
551        0x0006F9C1h    LZDone
552        0x0005B438h    LZInit
553        0x0005B626h    LZOpenFileA
554        0x0005B6BBh    LZOpenFileW
555        0x0005B7A4h    LZRead
556        0x0005B720h    LZSeek
557        0x0006F58Ah    LZStart
558        0x0002894Ch    LeaveCriticalSection forwarder: NTDLL.RtlLeaveCriticalSection
559        0x000205D8h    LoadLibraryA
560        0x000205B8h    LoadLibraryExA
561        0x0002049Bh    LoadLibraryExW
562        0x0001296Fh    LoadLibraryW
563        0x00058848h    LoadModule
564        0x000160B5h    LoadResource
565        0x00019881h    LocalAlloc
566        0x0003A9ADh    LocalCompact
567        0x00004BC1h    LocalFileTimeToFileTime
568        0x0004F9BFh    LocalFlags
569        0x00019A45h    LocalFree
570        0x0003AAEBh    LocalHandle
571        0x0000CE8Ch    LocalLock
572        0x00013458h    LocalReAlloc
573        0x00056BB3h    LocalShrink
574        0x0000BE07h    LocalSize
575        0x0000CF0Fh    LocalUnlock
576        0x00004E2Bh    LockFile
577        0x00055003h    LockFileEx
578        0x0001C931h    LockResource
579        0x00056A84h    MapUserPhysicalPages
580        0x00056AABh    MapUserPhysicalPagesScatter
581        0x00014D76h    MapViewOfFile
582        0x0001C1BDh    MapViewOfFileEx
583        0x0005A994h    Module32First
584        0x0005A8E2h    Module32FirstW
585        0x0005AAFAh    Module32Next
586        0x0005AA60h    Module32NextW
587        0x00011AFEh    MoveFileA
588        0x000045E4h    MoveFileExA
589        0x000030F1h    MoveFileExW
590        0x00004B7Ch    MoveFileW
591        0x00011A92h    MoveFileWithProgressA
592        0x00011783h    MoveFileWithProgressW
593        0x00012CF4h    MulDiv
594        0x00017CCEh    MultiByteToWideChar
595        0x0001B0D2h    NlsConvertIntegerToString
596        0x00004C8Ah    NlsGetCacheUpdateCount
597        0x00069ECDh    NlsResetProcessLocale
598        0x00057CC7h    NumaVirtualQueryNode
599        0x00020235h    OpenConsoleW
600        0x00002F7Ch    OpenDataFile
601        0x00013AB3h    OpenEventA
602        0x00013A2Bh    OpenEventW
603        0x0000CD4Fh    OpenFile
604        0x0001C815h    OpenFileMappingA
605        0x0001C788h    OpenFileMappingW
606        0x00060D37h    OpenJobObjectA
607        0x00060BE6h    OpenJobObjectW
608        0x0002074Ah    OpenMutexA
609        0x000206C7h    OpenMutexW
610        0x000106B7h    OpenProcess
611        0x00007E82h    OpenProfileUserMapping
612        0x00038B35h    OpenSemaphoreA
613        0x00038C36h    OpenSemaphoreW
614        0x00002348h    OpenThread
615        0x00058F5Dh    OpenWaitableTimerA
616        0x000370E2h    OpenWaitableTimerW
617        0x0003BD34h    OutputDebugStringA
618        0x000539BBh    OutputDebugStringW
619        0x000677FBh    PeekConsoleInputA
620        0x00067817h    PeekConsoleInputW
621        0x00057624h    PeekNamedPipe
622        0x00013BC5h    PostQueuedCompletionStatus
623        0x00060A82h    PrepareTape
624        0x0005666Ah    PrivCopyFileExW
625        0x000558D1h    PrivMoveFileIdentityW
626        0x0005A595h    Process32First
627        0x0005A4E3h    Process32FirstW
628        0x0005A6E9h    Process32Next
629        0x0005A64Fh    Process32NextW
630        0x000107A7h    ProcessIdToSessionId
631        0x0000E314h    PulseEvent
632        0x0005C1F9h    PurgeComm
633        0x00037FA9h    QueryActCtxW
634        0x0002896Ah    QueryDepthSList forwarder: NTDLL.RtlQueryDepthSList
635        0x00001D50h    QueryDosDeviceA
636        0x0000C506h    QueryDosDeviceW
637        0x0003B628h    QueryInformationJobObject
638        0x00058BC9h    QueryMemoryResourceNotification
639        0x000202FCh    QueryPerformanceCounter
640        0x0000D75Bh    QueryPerformanceFrequency
641        0x00054750h    QueryWin31IniFilesMappedToRegistry
642        0x0003C779h    QueueUserAPC
643        0x00013F93h    QueueUserWorkItem
644        0x0000D706h    RaiseException
645        0x00037719h    ReadConsoleA
646        0x00067833h    ReadConsoleInputA
647        0x0006786Bh    ReadConsoleInputExA
648        0x00067888h    ReadConsoleInputExW
649        0x0006784Fh    ReadConsoleInputW
650        0x00066E81h    ReadConsoleOutputA
651        0x000672F2h    ReadConsoleOutputAttribute
652        0x000672B4h    ReadConsoleOutputCharacterA
653        0x000672D3h    ReadConsoleOutputCharacterW
654        0x00066E64h    ReadConsoleOutputW
655        0x0003BFF7h    ReadConsoleW
656        0x0000D68Fh    ReadDirectoryChangesW
657        0x00018B82h    ReadFile
658        0x00038912h    ReadFileEx
659        0x000063AFh    ReadFileScatter
660        0x00001A54h    ReadProcessMemory
661        0x00068894h    RegisterConsoleIME
662        0x0006870Eh    RegisterConsoleOS2
663        0x000663A6h    RegisterConsoleVDM
664        0x0001C4E8h    RegisterWaitForInputIdle
665        0x0000DA5Ah    RegisterWaitForSingleObject
666        0x000364ABh    RegisterWaitForSingleObjectEx
667        0x000569F2h    RegisterWowBaseHandlers
668        0x0005DA7Fh    RegisterWowExec
669        0x00012D91h    ReleaseActCtx
670        0x000176A0h    ReleaseMutex
671        0x00013371h    ReleaseSemaphore
672        0x000104DCh    RemoveDirectoryA
673        0x000103D1h    RemoveDirectoryW
674        0x00052B2Ch    RemoveLocalAlternateComputerNameA
675        0x00052A52h    RemoveLocalAlternateComputerNameW
676        0x00028983h    RemoveVectoredExceptionHandler forwarder: NTDLL.RtlRemoveVectoredExceptionHandler
677        0x000024A3h    ReplaceFile
678        0x000566F3h    ReplaceFileA
679        0x000024A3h    ReplaceFileW
680        0x000583DEh    RequestDeviceWakeup
681        0x00058379h    RequestWakeupLatency
682        0x00014A69h    ResetEvent
683        0x00056B04h    ResetWriteWatch
684        0x000289ABh    RestoreLastError forwarder: NTDLL.RtlRestoreLastWin32Error
685        0x0000E154h    ResumeThread
686        0x000289CAh    RtlCaptureContext forwarder: NTDLL.RtlCaptureContext
687        0x000289E2h    RtlCaptureStackBackTrace forwarder: NTDLL.RtlCaptureStackBackTrace
688        0x00028A01h    RtlFillMemory forwarder: NTDLL.RtlFillMemory
689        0x00028A15h    RtlMoveMemory forwarder: NTDLL.RtlMoveMemory
690        0x00028A29h    RtlUnwind forwarder: NTDLL.RtlUnwind
691        0x00028A39h    RtlZeroMemory forwarder: NTDLL.RtlZeroMemory
692        0x00067FDAh    ScrollConsoleScreenBufferA
693        0x00067FF7h    ScrollConsoleScreenBufferW
694        0x0000CBF9h    SearchPathA
695        0x00011C06h    SearchPathW
696        0x0006C07Eh    SetCPGlobal
697        0x000694EAh    SetCalendarInfoA
698        0x0006A57Ch    SetCalendarInfoW
699        0x000534B0h    SetClientTimeZoneInformation
700        0x0006117Ch    SetComPlusPackageInstallStatus
701        0x0005C27Ch    SetCommBreak
702        0x0005D18Ah    SetCommConfig
703        0x0005C28Ah    SetCommMask
704        0x0005C324h    SetCommState
705        0x0005C625h    SetCommTimeouts
706        0x00051EFBh    SetComputerNameA
707        0x00052009h    SetComputerNameExA
708        0x00051E83h    SetComputerNameExW
709        0x00051D64h    SetComputerNameW
710        0x00067CBDh    SetConsoleActiveScreenBuffer
711        0x00068121h    SetConsoleCP
712        0x000658E4h    SetConsoleCommandHistoryMode
713        0x00016968h    SetConsoleCtrlHandler
714        0x000666E6h    SetConsoleCursor
715        0x00067DCEh    SetConsoleCursorInfo
716        0x0006860Bh    SetConsoleCursorMode
717        0x0003BECAh    SetConsoleCursorPosition
718        0x0006683Ch    SetConsoleDisplayMode
719        0x00068014h    SetConsoleFont
720        0x00066544h    SetConsoleHardwareState
721        0x00068073h    SetConsoleIcon
722        0x00065BE4h    SetConsoleInputExeNameA
723        0x0001973Eh    SetConsoleInputExeNameW
724        0x000665A9h    SetConsoleKeyShortcuts
725        0x00068563h    SetConsoleLocalEUDC
726        0x0006F540h    SetConsoleMaximumWindowSize
727        0x00066655h    SetConsoleMenuClose
728        0x000196EEh    SetConsoleMode
729        0x00068CE4h    SetConsoleNlsMode
730        0x000656D7h    SetConsoleNumberOfCommandsA
731        0x000656C5h    SetConsoleNumberOfCommandsW
732        0x00068767h    SetConsoleOS2OemFormat
733        0x0006820Ch    SetConsoleOutputCP
734        0x00066924h    SetConsolePalette
735        0x00067D6Fh    SetConsoleScreenBufferSize
736        0x0003AE3Fh    SetConsoleTextAttribute
737        0x0006593Dh    SetConsoleTitleA
738        0x0003AE91h    SetConsoleTitleW
739        0x00067E6Ah    SetConsoleWindowInfo
740        0x00028A4Dh    SetCriticalSectionSpinCount forwarder: NTDLL.RtlSetCriticalSectionSpinCount
741        0x000105C5h    SetCurrentDirectoryA
742        0x00019EFEh    SetCurrentDirectoryW
743        0x0005CF1Eh    SetDefaultCommConfigA
744        0x0005CE64h    SetDefaultCommConfigW
745        0x00010192h    SetEndOfFile
746        0x0000BD68h    SetEnvironmentVariableA
747        0x000186CAh    SetEnvironmentVariableW
748        0x00018C17h    SetErrorMode
749        0x00014A3Bh    SetEvent
750        0x00001D17h    SetFileApisToANSI
751        0x00015D75h    SetFileApisToOEM
752        0x00010396h    SetFileAttributesA
753        0x000102A8h    SetFileAttributesW
754        0x00018C81h    SetFilePointer
755        0x00038A54h    SetFilePointerEx
756        0x000552EFh    SetFileShortNameA
757        0x00055229h    SetFileShortNameW
758        0x0001011Ah    SetFileTime
759        0x000551DAh    SetFileValidData
760        0x00056966h    SetFirmwareEnvironmentVariableA
761        0x0005686Eh    SetFirmwareEnvironmentVariableW
762        0x000383C8h    SetHandleContext
763        0x0001C931h    SetHandleCount
764        0x00012FDEh    SetHandleInformation
765        0x0003A2A8h    SetInformationJobObject
766        0x0006903Dh    SetLastConsoleEventActive
767        0x00028A72h    SetLastError forwarder: NTDLL.RtlSetLastWin32Error
768        0x00052D7Dh    SetLocalPrimaryComputerNameA
769        0x00052B6Eh    SetLocalPrimaryComputerNameW
770        0x0004F8D9h    SetLocalTime
771        0x0000F13Bh    SetLocaleInfoA
772        0x0000F1A2h    SetLocaleInfoW
773        0x000144ECh    SetMailslotInfo
774        0x0005841Ah    SetMessageWaitingIndicator
775        0x00013F2Bh    SetNamedPipeHandleState
776        0x0003856Eh    SetPriorityClass
777        0x00058647h    SetProcessAffinityMask
778        0x00037D81h    SetProcessPriorityBoost
779        0x000366E8h    SetProcessShutdownParameters
780        0x0000D8CFh    SetProcessWorkingSetSize
781        0x0001FF2Eh    SetStdHandle
782        0x00058339h    SetSystemPowerState
783        0x00036B7Ch    SetSystemTime
784        0x0000DB3Fh    SetSystemTimeAdjustment
785        0x00060B95h    SetTapeParameters
786        0x000609EBh    SetTapePosition
787        0x000597B5h    SetTermsrvAppInstallMode
788        0x00039124h    SetThreadAffinityMask
789        0x00059953h    SetThreadContext
790        0x0003A151h    SetThreadExecutionState
791        0x0005A074h    SetThreadIdealProcessor
792        0x00015D12h    SetThreadLocale
793        0x000115F7h    SetThreadPriority
794        0x000598ECh    SetThreadPriorityBoost
795        0x00019608h    SetThreadUILanguage
796        0x00053576h    SetTimeZoneInformation
797        0x000360E2h    SetTimerQueueTimer
798        0x0001C9E7h    SetUnhandledExceptionFilter
799        0x0006B79Eh    SetUserGeoID
800        0x0005D843h    SetVDMCurrentDirectories
801        0x000582DCh    SetVolumeLabelA
802        0x00057FBDh    SetVolumeLabelW
803        0x0005FBA2h    SetVolumeMountPointA
804        0x0005EFF4h    SetVolumeMountPointW
805        0x00039959h    SetWaitableTimer
806        0x0005BC0Ch    SetupComm
807        0x00066745h    ShowConsoleCursor
808        0x00058E09h    SignalObjectAndWait
809        0x0001105Fh    SizeofResource
810        0x00001BE6h    Sleep
811        0x00017562h    SleepEx
812        0x00038BD8h    SuspendThread
813        0x00039607h    SwitchToFiber
814        0x0000D52Ch    SwitchToThread
815        0x00017C4Ch    SystemTimeToFileTime
816        0x00052E72h    SystemTimeToTzSpecificLocalTime
817        0x00060C56h    TerminateJobObject
818        0x000016B4h    TerminateProcess
819        0x00015CEBh    TerminateThread
820        0x00010AB7h    TermsrvAppInstallMode
821        0x0005A7A3h    Thread32First
822        0x0005A850h    Thread32Next
823        0x0001C5B4h    TlsAlloc
824        0x00012B29h    TlsFree
825        0x00018B61h    TlsGetValue
826        0x00019B39h    TlsSetValue
827        0x0005A4AAh    Toolhelp32ReadProcessMemory
828        0x00013EACh    TransactNamedPipe
829        0x0005C6C9h    TransmitCommChar
830        0x00056F23h    TrimVirtualBuffer
831        0x00028A8Dh    TryEnterCriticalSection forwarder: NTDLL.RtlTryEnterCriticalSection
832        0x000530B6h    TzSpecificLocalTimeToSystemTime
833        0x00056F7Bh    UTRegister
834        0x0006F3A6h    UTUnRegister
835        0x00059A84h    UnhandledExceptionFilter
836        0x00004EA0h    UnlockFile
837        0x00004ED8h    UnlockFileEx
838        0x00015090h    UnmapViewOfFile
839        0x0006893Fh    UnregisterConsoleIME
840        0x00006BDAh    UnregisterWait
841        0x0000DAC9h    UnregisterWaitEx
842        0x00064ADAh    UpdateResourceA
843        0x000649DAh    UpdateResourceW
844        0x00069049h    VDMConsoleOperation
845        0x0005DE6Ah    VDMOperationStarted
846        0x0000F304h    ValidateLCType
847        0x00004499h    ValidateLocale
848        0x0006A049h    VerLanguageNameA
849        0x00069FD3h    VerLanguageNameW
850        0x00028AAEh    VerSetConditionMask forwarder: NTDLL.VerSetConditionMask
851        0x00019F41h    VerifyConsoleIoHandle
852        0x000022C2h    VerifyVersionInfoA
853        0x00009B9Ch    VerifyVersionInfoW
854        0x0001980Ah    VirtualAlloc
855        0x00019824h    VirtualAllocEx
856        0x00056F3Ch    VirtualBufferExceptionHandler
857        0x00019E34h    VirtualFree
858        0x00019E4Bh    VirtualFreeEx
859        0x00038AF5h    VirtualLock
860        0x0000169Ah    VirtualProtect
861        0x0001C4B7h    VirtualProtectEx
862        0x0001F044h    VirtualQuery
863        0x0001F01Ah    VirtualQueryEx
864        0x000390C9h    VirtualUnlock
865        0x000033B2h    WTSGetActiveConsoleSessionId
866        0x0005C74Ch    WaitCommEvent
867        0x00053A07h    WaitForDebugEvent
868        0x00014C59h    WaitForMultipleObjects
869        0x00014B49h    WaitForMultipleObjectsEx
870        0x00019D5Bh    WaitForSingleObject
871        0x00017800h    WaitForSingleObjectEx
872        0x000578F7h    WaitNamedPipeA
873        0x00038722h    WaitNamedPipeW
874        0x00019924h    WideCharToMultiByte
875        0x000084C6h    WinExec
876        0x00039078h    WriteConsoleA
877        0x00066AABh    WriteConsoleInputA
878        0x000666AEh    WriteConsoleInputVDMA
879        0x000666CAh    WriteConsoleInputVDMW
880        0x00066AC7h    WriteConsoleInputW
881        0x00067165h    WriteConsoleOutputA
882        0x00067459h    WriteConsoleOutputAttribute
883        0x0006741Bh    WriteConsoleOutputCharacterA
884        0x0006743Ah    WriteConsoleOutputCharacterW
885        0x00067148h    WriteConsoleOutputW
886        0x00016052h    WriteConsoleW
887        0x00019D8Ch    WriteFile
888        0x00055141h    WriteFileEx
889        0x00006448h    WriteFileGather
890        0x0003786Dh    WritePrivateProfileSectionA
891        0x0005485Eh    WritePrivateProfileSectionW
892        0x0001070Eh    WritePrivateProfileStringA
893        0x000129F8h    WritePrivateProfileStringW
894        0x00054ACEh    WritePrivateProfileStructA
895        0x00054BC9h    WritePrivateProfileStructW
896        0x00001A90h    WriteProcessMemory
897        0x0003785Bh    WriteProfileSectionA
898        0x00054CECh    WriteProfileSectionW
899        0x000106A1h    WriteProfileStringA
900        0x00012A2Bh    WriteProfileStringW
901        0x00060B0Dh    WriteTapemark
902        0x00061000h    ZombifyActCtx
903        0x0000E4C8h    _hread
904        0x0000D09Bh    _hwrite
905        0x0000E32Eh    _lclose
906        0x0000D071h    _lcreat
907        0x0000E4FDh    _llseek
908        0x00039331h    _lopen
909        0x0000E4C8h    _lread
910        0x0000D09Bh    _lwrite
911        0x00014155h    lstrcat
912        0x00014155h    lstrcatA
913        0x00013640h    lstrcatW
914        0x00016432h    lstrcmp
915        0x00016432h    lstrcmpA
916        0x00018D60h    lstrcmpW
917        0x00016A2Eh    lstrcmpi
918        0x00016A2Eh    lstrcmpiA
919        0x0001AF1Eh    lstrcmpiW
920        0x00013167h    lstrcpy
921        0x00013167h    lstrcpyA
922        0x00013679h    lstrcpyW
923        0x00013BEFh    lstrcpyn
924        0x00013BEFh    lstrcpynA
925        0x0000F65Eh    lstrcpynW
926        0x00014672h    lstrlen
927        0x00014672h    lstrlenA
928        0x00017EF1h    lstrlenW

----------Imported symbols----------

[IMAGE_IMPORT_DESCRIPTOR]
OriginalFirstThunk:            0x72DF6   
Characteristics:               0x72DF6   
TimeDateStamp:                 0xFFFFFFFF [INVALID TIME]
ForwarderChain:                0xFFFFFFFF
Name:                          0x72DEC   
FirstThunk:                    0x1000    

ntdll.dll._wcsnicmp Ord[1323] Bound: 0x77F54B99
ntdll.dll.NtFsControlFile Ord[159] Bound: 0x77F7E8F3
ntdll.dll.NtCreateFile Ord[110] Bound: 0x77F7E603
ntdll.dll.RtlAllocateHeap Ord[394] Bound: 0x77F516F8
ntdll.dll.RtlFreeHeap Ord[568] Bound: 0x77F51597
ntdll.dll.NtOpenFile Ord[191] Bound: 0x77F7EAF3
ntdll.dll.NtQueryInformationFile Ord[227] Bound: 0x77F7ED23
ntdll.dll.NtQueryEaFile Ord[223] Bound: 0x77F7ECE3
ntdll.dll.RtlLengthSecurityDescriptor Ord[673] Bound: 0x77F610D6
ntdll.dll.NtQuerySecurityObject Ord[245] Bound: 0x77F7EE33
ntdll.dll.NtSetEaFile Ord[296] Bound: 0x77F7F153
ntdll.dll.NtSetSecurityObject Ord[315] Bound: 0x77F7F283
ntdll.dll.NtSetInformationFile Ord[302] Bound: 0x77F7F1B3
ntdll.dll.CsrClientCallServer Ord[6] Bound: 0x77F534AF
ntdll.dll.NtDeviceIoControlFile Ord[141] Bound: 0x77F7E7D3
ntdll.dll.NtClose Ord[98] Bound: 0x77F7E543
ntdll.dll.RtlInitUnicodeString Ord[621] Bound: 0x77F7F5DF
ntdll.dll.wcscspn Ord[1396] Bound: 0x77F5FAF7
ntdll.dll.RtlUnicodeToMultiByteSize Ord[825] Bound: 0x77F52611
ntdll.dll.wcslen Ord[1397] Bound: 0x77F51901
ntdll.dll._memicmp Ord[1304] Bound: 0x77FAF94A
ntdll.dll.memmove Ord[1360] Bound: 0x77F81165
ntdll.dll.NtQueryValueKey Ord[254] Bound: 0x77F7EEC3
ntdll.dll.NtOpenKey Ord[194] Bound: 0x77F7EB23
ntdll.dll.NtFlushKey Ord[154] Bound: 0x77F7E8A3
ntdll.dll.NtSetValueKey Ord[325] Bound: 0x77F7F323
ntdll.dll.NtCreateKey Ord[114] Bound: 0x77F7E643
ntdll.dll.RtlNtStatusToDosError Ord[698] Bound: 0x77F51220
ntdll.dll.RtlFreeUnicodeString Ord[573] Bound: 0x77F52599
ntdll.dll.RtlDnsHostNameToComputerName Ord[507] Bound: 0x77F657DB
ntdll.dll.wcsncpy Ord[1400] Bound: 0x77F52916
ntdll.dll.RtlUnicodeStringToAnsiString Ord[818] Bound: 0x77F52633
ntdll.dll.RtlxUnicodeStringToAnsiSize Ord[873] Bound: 0x77FA15E0
ntdll.dll.NlsMbCodePageTag Ord[71] Bound: 0x77FC5010
ntdll.dll.RtlAnsiStringToUnicodeString Ord[397] Bound: 0x77F51502
ntdll.dll.RtlInitAnsiString Ord[615] Bound: 0x77F7F5B3
ntdll.dll.RtlCreateUnicodeStringFromAsciiz Ord[469] Bound: 0x77F52401
ntdll.dll.wcschr Ord[1393] Bound: 0x77F54CF5
ntdll.dll.wcsstr Ord[1404] Bound: 0x77F689E2
ntdll.dll.RtlPrefixString Ord[711] Bound: 0x77F7B09C
ntdll.dll._wcsicmp Ord[1321] Bound: 0x77F56CFC
ntdll.dll.RtlGetFullPathName_U Ord[589] Bound: 0x77F548FA
ntdll.dll.RtlGetCurrentDirectory_U Ord[582] Bound: 0x77F54EC5
ntdll.dll.NtQueryInformationProcess Ord[230] Bound: 0x77F7ED53
ntdll.dll.RtlReleasePebLock Ord[746] Bound: 0x77F52828
ntdll.dll.RtlEqualUnicodeString Ord[535] Bound: 0x77F52838
ntdll.dll.RtlAcquirePebLock Ord[366] Bound: 0x77F527F6
ntdll.dll.RtlFreeAnsiString Ord[566] Bound: 0x77F52599
ntdll.dll.RtlSetCurrentDirectory_U Ord[765] Bound: 0x77F5B37D
ntdll.dll.RtlTimeToTimeFields Ord[803] Bound: 0x77F52A1D
ntdll.dll.NtSetSystemTime Ord[320] Bound: 0x77F7F2D3
ntdll.dll.RtlTimeFieldsToTime Ord[799] Bound: 0x77F5857D
ntdll.dll.NtQuerySystemInformation Ord[250] Bound: 0x77F7EE83
ntdll.dll.NtSetSystemInformation Ord[318] Bound: 0x77F7F2B3
ntdll.dll.RtlCutoverTimeToSystemTime Ord[474] Bound: 0x77FA4F5D
ntdll.dll._allmul Ord[1283] Bound: 0x77F806EE
ntdll.dll.RtlSetTimeZoneInformation Ord[784] Bound: 0x77FA2E0E
ntdll.dll.DbgBreakPoint Ord[15] Bound: 0x77F7F570
ntdll.dll.RtlFreeSid Ord[571] Bound: 0x77F58DA6
ntdll.dll.RtlSetDaclSecurityDescriptor Ord[767] Bound: 0x77F58EC0
ntdll.dll.RtlCreateSecurityDescriptor Ord[463] Bound: 0x77F58E9B
ntdll.dll.RtlAddAccessAllowedAce Ord[372] Bound: 0x77F590CF
ntdll.dll.RtlCreateAcl Ord[453] Bound: 0x77F58F14
ntdll.dll.RtlLengthSid Ord[674] Bound: 0x77F54B5A
ntdll.dll.RtlAllocateAndInitializeSid Ord[392] Bound: 0x77F58DCA
ntdll.dll.DbgPrint Ord[16] Bound: 0x77F7D480
ntdll.dll.NtOpenProcess Ord[198] Bound: 0x77F7EB53
ntdll.dll.CsrGetProcessId Ord[9] Bound: 0x77F96F13
ntdll.dll.DbgUiDebugActiveProcess Ord[25] Bound: 0x77F970F3
ntdll.dll.DbgUiConnectToDbg Ord[22] Bound: 0x77F96FB7
ntdll.dll.DbgUiIssueRemoteBreakin Ord[27] Bound: 0x77F970B9
ntdll.dll.NtSetInformationDebugObject Ord[301] Bound: 0x77F7F1A3
ntdll.dll.DbgUiGetThreadDebugObject Ord[26] Bound: 0x77F97005
ntdll.dll.NtQueryInformationThread Ord[231] Bound: 0x77F7ED63
ntdll.dll.DbgUiConvertStateChangeStructure Ord[24] Bound: 0x77F9712A
ntdll.dll.DbgUiWaitStateChange Ord[31] Bound: 0x77F97025
ntdll.dll.DbgUiContinue Ord[23] Bound: 0x77F97043
ntdll.dll.DbgUiStopDebugging Ord[30] Bound: 0x77F9705F
ntdll.dll.RtlDosPathNameToNtPathName_U Ord[510] Bound: 0x77F5489F
ntdll.dll.RtlIsDosDeviceName_U Ord[655] Bound: 0x77F54B01
ntdll.dll.RtlCreateAtomTable Ord[456] Bound: 0x77F63B06
ntdll.dll.NtAddAtom Ord[81] Bound: 0x77F7E433
ntdll.dll.RtlAddAtomToAtomTable Ord[380] Bound: 0x77F6393B
ntdll.dll.NtFindAtom Ord[151] Bound: 0x77F7E873
ntdll.dll.RtlLookupAtomInAtomTable Ord[680] Bound: 0x77F6026A
ntdll.dll.NtDeleteAtom Ord[135] Bound: 0x77F7E773
ntdll.dll.RtlDeleteAtomFromAtomTable Ord[484] Bound: 0x77F63C61
ntdll.dll.NtQueryInformationAtom Ord[226] Bound: 0x77F7ED13
ntdll.dll.RtlQueryAtomInAtomTable Ord[715] Bound: 0x77F63B98
ntdll.dll.RtlMultiByteToUnicodeN Ord[689] Bound: 0x77F5131B
ntdll.dll.RtlUnicodeToMultiByteN Ord[824] Bound: 0x77F5247D
ntdll.dll.RtlMultiByteToUnicodeSize Ord[690] Bound: 0x77F5FE24
ntdll.dll.RtlPrefixUnicodeString Ord[712] Bound: 0x77F54DC4
ntdll.dll.RtlLeaveCriticalSection Ord[671] Bound: 0x77F7E300
ntdll.dll.RtlEnterCriticalSection Ord[522] Bound: 0x77F7E21F
ntdll.dll.NtEnumerateValueKey Ord[148] Bound: 0x77F7E843
ntdll.dll.RtlIsTextUnicode Ord[660] Bound: 0x77F5FB3A
ntdll.dll.NtReadFile Ord[260] Bound: 0x77F7EF23
ntdll.dll.NtAllocateVirtualMemory Ord[90] Bound: 0x77F7E4C3
ntdll.dll.NtUnlockFile Ord[343] Bound: 0x77F7F443
ntdll.dll.NtLockFile Ord[175] Bound: 0x77F7E9F3
ntdll.dll.RtlAppendUnicodeStringToString Ord[401] Bound: 0x77F56C0B
ntdll.dll.RtlAppendUnicodeToString Ord[402] Bound: 0x77F56B9D
ntdll.dll.RtlCopyUnicodeString Ord[452] Bound: 0x77F56AF9
ntdll.dll.NtFreeVirtualMemory Ord[158] Bound: 0x77F7E8E3
ntdll.dll.NtWriteFile Ord[353] Bound: 0x77F7F4D3
ntdll.dll.RtlCreateUnicodeString Ord[468] Bound: 0x77F58CA1
ntdll.dll.RtlFormatCurrentUserKeyPath Ord[564] Bound: 0x77F56FFC
ntdll.dll.RtlGetLongestNtPathLength Ord[595] Bound: 0x77F5CD0C
ntdll.dll.NtQueryKey Ord[236] Bound: 0x77F7EDB3
ntdll.dll.NtEnumerateKey Ord[146] Bound: 0x77F7E823
ntdll.dll.NtDeleteValueKey Ord[140] Bound: 0x77F7E7C3
ntdll.dll.RtlEqualString Ord[534] Bound: 0x77F5FA39
ntdll.dll.CsrFreeCaptureBuffer Ord[8] Bound: 0x77F5B584
ntdll.dll.CsrCaptureMessageString Ord[4] Bound: 0x77F5F91A
ntdll.dll.CsrAllocateCaptureBuffer Ord[0] Bound: 0x77F5B5D2
ntdll.dll.strncpy Ord[1376] Bound: 0x77F8194F
ntdll.dll.RtlCharToInteger Ord[416] Bound: 0x77F5D59E
ntdll.dll.RtlUpcaseUnicodeChar Ord[832] Bound: 0x77F527D8
ntdll.dll.RtlUpcaseUnicodeString Ord[833] Bound: 0x77F783C5
ntdll.dll.CsrAllocateMessagePointer Ord[1] Bound: 0x77F5B62A
ntdll.dll.NtQueryObject Ord[239] Bound: 0x77F7EDE3
ntdll.dll.wcscmp Ord[1394] Bound: 0x77F61B5B
ntdll.dll.NtQueryDirectoryObject Ord[222] Bound: 0x77F7ECD3
ntdll.dll.NtQuerySymbolicLinkObject Ord[247] Bound: 0x77F7EE53
ntdll.dll.NtOpenSymbolicLinkObject Ord[203] Bound: 0x77F7EBA3
ntdll.dll.NtOpenDirectoryObject Ord[188] Bound: 0x77F7EAC3
ntdll.dll.NtCreateIoCompletion Ord[111] Bound: 0x77F7E613
ntdll.dll.NtSetIoCompletion Ord[310] Bound: 0x77F7F233
ntdll.dll.NtRemoveIoCompletion Ord[268] Bound: 0x77F7EF93
ntdll.dll.NtSetInformationProcess Ord[306] Bound: 0x77F7F1F3
ntdll.dll.NtQueryDirectoryFile Ord[221] Bound: 0x77F7ECC3
ntdll.dll.RtlDeleteCriticalSection Ord[485] Bound: 0x77F53275
ntdll.dll.NtNotifyChangeDirectoryFile Ord[185] Bound: 0x77F7EA93
ntdll.dll.NtWaitForSingleObject Ord[350] Bound: 0x77F7F4A3
ntdll.dll.RtlInitializeCriticalSection Ord[626] Bound: 0x77F534A1
ntdll.dll.RtlCompareMemory Ord[425] Bound: 0x77F82C4B
ntdll.dll.NtQueryVolumeInformationFile Ord[256] Bound: 0x77F7EEE3
ntdll.dll.NtFlushBuffersFile Ord[152] Bound: 0x77F7E883
ntdll.dll.RtlDeactivateActivationContextUnsafeFast Ord[477] Bound: 0x77F5103C
ntdll.dll.RtlActivateActivationContextUnsafeFast Ord[371] Bound: 0x77F51000
ntdll.dll.NtCancelIoFile Ord[95] Bound: 0x77F7E513
ntdll.dll.NtReadFileScatter Ord[261] Bound: 0x77F7EF33
ntdll.dll.NtWriteFileGather Ord[354] Bound: 0x77F7F4E3
ntdll.dll.wcscpy Ord[1395] Bound: 0x77F520B8
ntdll.dll.NtOpenSection Ord[201] Bound: 0x77F7EB83
ntdll.dll.NtMapViewOfSection Ord[183] Bound: 0x77F7EA73
ntdll.dll.NtFlushVirtualMemory Ord[155] Bound: 0x77F7E8B3
ntdll.dll.RtlFlushSecureMemoryCache Ord[563] Bound: 0x77FA58E9
ntdll.dll.NtUnmapViewOfSection Ord[345] Bound: 0x77F7F463
ntdll.dll.NtCreateSection Ord[124] Bound: 0x77F7E6D3
ntdll.dll.NtQueryFullAttributesFile Ord[225] Bound: 0x77F7ED03
ntdll.dll.RtlUnicodeStringToOemString Ord[822] Bound: 0x77F5B9BF
ntdll.dll.swprintf Ord[1383] Bound: 0x77F5B2CA
ntdll.dll.NtQueryAttributesFile Ord[215] Bound: 0x77F7EC63
ntdll.dll.RtlDetermineDosPathNameType_U Ord[505] Bound: 0x77F5452B
ntdll.dll.NtRaiseHardError Ord[259] Bound: 0x77F7EF13
ntdll.dll.NtQuerySystemEnvironmentValueEx Ord[249] Bound: 0x77F7EE73
ntdll.dll.RtlGUIDFromString Ord[575] Bound: 0x77F6ABA5
ntdll.dll.NtSetSystemEnvironmentValueEx Ord[317] Bound: 0x77F7F2A3
ntdll.dll.RtlInitString Ord[620] Bound: 0x77F7F587
ntdll.dll.RtlUnlockHeap Ord[829] Bound: 0x77F5CA2E
ntdll.dll.RtlSetUserValueHeap Ord[788] Bound: 0x77F5DCEA
ntdll.dll.RtlFreeHandle Ord[567] Bound: 0x77F523D1
ntdll.dll.RtlAllocateHandle Ord[393] Bound: 0x77F52394
ntdll.dll.RtlLockHeap Ord[677] Bound: 0x77F5C9E0
ntdll.dll.RtlSizeHeap Ord[789] Bound: 0x77F522F2
ntdll.dll.RtlGetUserInfoHeap Ord[606] Bound: 0x77F5D323
ntdll.dll.RtlReAllocateHeap Ord[737] Bound: 0x77F5722F
ntdll.dll.RtlIsValidHandle Ord[661] Bound: 0x77F5234A
ntdll.dll.RtlCompactHeap Ord[424] Bound: 0x77F65F2C
ntdll.dll.RtlImageNtHeader Ord[611] Bound: 0x77F51924
ntdll.dll.NtProtectVirtualMemory Ord[213] Bound: 0x77F7EC43
ntdll.dll.NtQueryVirtualMemory Ord[255] Bound: 0x77F7EED3
ntdll.dll.NtLockVirtualMemory Ord[178] Bound: 0x77F7EA23
ntdll.dll.NtUnlockVirtualMemory Ord[344] Bound: 0x77F7F453
ntdll.dll.NtFlushInstructionCache Ord[153] Bound: 0x77F7E893
ntdll.dll.NtAllocateUserPhysicalPages Ord[88] Bound: 0x77F7E4A3
ntdll.dll.NtFreeUserPhysicalPages Ord[157] Bound: 0x77F7E8D3
ntdll.dll.NtMapUserPhysicalPages Ord[181] Bound: 0x77F7EA53
ntdll.dll.NtMapUserPhysicalPagesScatter Ord[182] Bound: 0x77F7EA63
ntdll.dll.NtGetWriteWatch Ord[163] Bound: 0x77F7E933
ntdll.dll.NtResetWriteWatch Ord[281] Bound: 0x77F7F063
ntdll.dll.NtSetInformationObject Ord[305] Bound: 0x77F7F1E3
ntdll.dll.NtDuplicateObject Ord[143] Bound: 0x77F7E7F3
ntdll.dll.RtlOemStringToUnicodeString Ord[705] Bound: 0x77F5B829
ntdll.dll.CsrNewThread Ord[11] Bound: 0x77F58A8E
ntdll.dll.CsrClientConnectToServer Ord[7] Bound: 0x77F68D38
ntdll.dll.RtlCreateTagHeap Ord[465] Bound: 0x77F68B5E
ntdll.dll.LdrSetDllManifestProber Ord[63] Bound: 0x77F69767
ntdll.dll.RtlSetThreadPoolStartFunc Ord[783] Bound: 0x77F69750
ntdll.dll._stricmp Ord[1309] Bound: 0x77F52115
ntdll.dll.wcscat Ord[1392] Bound: 0x77F529A4
ntdll.dll.RtlCreateHeap Ord[459] Bound: 0x77F59283
ntdll.dll.RtlDestroyHeap Ord[502] Bound: 0x77F5973B
ntdll.dll.RtlExtendHeap Ord[539] Bound: 0x77FA3261
ntdll.dll.RtlQueryTagHeap Ord[729] Bound: 0x77FA3121
ntdll.dll.RtlUsageHeap Ord[843] Bound: 0x77FA3F21
ntdll.dll.RtlValidateHeap Ord[849] Bound: 0x77F67D35
ntdll.dll.RtlGetProcessHeaps Ord[602] Bound: 0x77F7DCEC
ntdll.dll.RtlWalkHeap Ord[854] Bound: 0x77FA34A3
ntdll.dll.RtlSetHeapInformation Ord[770] Bound: 0x77FA3DFA
ntdll.dll.RtlQueryHeapInformation Ord[718] Bound: 0x77FA3E2F
ntdll.dll.RtlInitializeHandleTable Ord[630] Bound: 0x77F5B018
ntdll.dll.RtlExtendedLargeIntegerDivide Ord[541] Bound: 0x77F83146
ntdll.dll.NtCreateMailslotFile Ord[116] Bound: 0x77F7E653
ntdll.dll.RtlFormatMessage Ord[565] Bound: 0x77F6AD3C
ntdll.dll.RtlFindMessage Ord[555] Bound: 0x77F6AF2E
ntdll.dll.LdrUnloadDll Ord[67] Bound: 0x77F56D49
ntdll.dll.LdrUnloadAlternateResourceModule Ord[66] Bound: 0x77F5E931
ntdll.dll.LdrDisableThreadCalloutsForDll Ord[43] Bound: 0x77F5AC50
ntdll.dll.LdrGetDllHandle Ord[51] Bound: 0x77F56525
ntdll.dll.LdrUnlockLoaderLock Ord[68] Bound: 0x77F52775
ntdll.dll.LdrAddRefDll Ord[39] Bound: 0x77F9775E
ntdll.dll.RtlComputePrivatizedDllName_U Ord[432] Bound: 0x77F97F50
ntdll.dll.RtlPcToFileHeader Ord[708] Bound: 0x77F7A1C6
ntdll.dll.LdrLockLoaderLock Ord[58] Bound: 0x77F526D1
ntdll.dll.RtlGetVersion Ord[607] Bound: 0x77F581C4
ntdll.dll.RtlVerifyVersionInfo Ord[852] Bound: 0x77F61447
ntdll.dll.RtlUnicodeStringToInteger Ord[820] Bound: 0x77F58862
ntdll.dll.LdrLoadAlternateResourceModule Ord[56] Bound: 0x77F5C856
ntdll.dll.RtlDosApplyFileIsolationRedirection_Ustr Ord[509] Bound: 0x77F55E96
ntdll.dll.LdrLoadDll Ord[57] Bound: 0x77F569D2
ntdll.dll.LdrGetProcedureAddress Ord[53] Bound: 0x77F51B46
ntdll.dll.LdrFindResource_U Ord[49] Bound: 0x77F540AB
ntdll.dll.LdrAccessResource Ord[38] Bound: 0x77F540C5
ntdll.dll.LdrFindResourceDirectory_U Ord[47] Bound: 0x77F582C0
ntdll.dll.RtlImageDirectoryEntryToData Ord[610] Bound: 0x77F5185B
ntdll.dll._strcmpi Ord[1308] Bound: 0x77F52115
ntdll.dll.NtSetInformationThread Ord[307] Bound: 0x77F7F203
ntdll.dll.NtOpenThreadToken Ord[205] Bound: 0x77F7EBC3
ntdll.dll.NtCreateNamedPipeFile Ord[118] Bound: 0x77F7E673
ntdll.dll.RtlDefaultNpAcl Ord[481] Bound: 0x77F7C102
ntdll.dll.RtlDosSearchPath_Ustr Ord[512] Bound: 0x77F5D189
ntdll.dll.RtlInitUnicodeStringEx Ord[622] Bound: 0x77F54E47
ntdll.dll.RtlQueryEnvironmentVariable_U Ord[717] Bound: 0x77F55CE2
ntdll.dll.RtlAnsiCharToUnicodeChar Ord[395] Bound: 0x77F5CB43
ntdll.dll.RtlIntegerToChar Ord[639] Bound: 0x77F5873F
ntdll.dll.NtSetVolumeInformationFile Ord[326] Bound: 0x77F7F333
ntdll.dll.NtQueryPerformanceCounter Ord[241] Bound: 0x77F7EE03
ntdll.dll.sprintf Ord[1365] Bound: 0x77F6A963
ntdll.dll.NtPowerInformation Ord[209] Bound: 0x77F7EC03
ntdll.dll.NtInitiatePowerAction Ord[168] Bound: 0x77F7E983
ntdll.dll.NtSetThreadExecutionState Ord[321] Bound: 0x77F7F2E3
ntdll.dll.NtRequestWakeupLatency Ord[279] Bound: 0x77F7F043
ntdll.dll.NtGetDevicePowerState Ord[161] Bound: 0x77F7E913
ntdll.dll.NtIsSystemResumeAutomatic Ord[170] Bound: 0x77F7E9A3
ntdll.dll.NtRequestDeviceWakeup Ord[276] Bound: 0x77F7F013
ntdll.dll.NtCancelDeviceWakeupRequest Ord[94] Bound: 0x77F7E503
ntdll.dll.NtWriteVirtualMemory Ord[356] Bound: 0x77F7F503
ntdll.dll.LdrShutdownProcess Ord[64] Bound: 0x77F6B0AF
ntdll.dll.NtTerminateProcess Ord[335] Bound: 0x77F7F3C3
ntdll.dll.RtlRaiseStatus Ord[734] Bound: 0x77FA73EE
ntdll.dll.RtlSetEnvironmentVariable Ord[768] Bound: 0x77F5BA4A
ntdll.dll.RtlExpandEnvironmentStrings_U Ord[538] Bound: 0x77F5718D
ntdll.dll.NtReadVirtualMemory Ord[263] Bound: 0x77F7EF53
ntdll.dll.RtlCompareUnicodeString Ord[428] Bound: 0x77F58B97
ntdll.dll.RtlQueryRegistryValues Ord[727] Bound: 0x77F7A8D5
ntdll.dll.NtCreateJobSet Ord[113] Bound: 0x77F7E633
ntdll.dll.NtCreateJobObject Ord[112] Bound: 0x77F7E623
ntdll.dll.NtIsProcessInJob Ord[169] Bound: 0x77F7E993
ntdll.dll.RtlEqualSid Ord[533] Bound: 0x77F58E4E
ntdll.dll.RtlSubAuthoritySid Ord[795] Bound: 0x77F5B037
ntdll.dll.RtlInitializeSid Ord[635] Bound: 0x77F58E71
ntdll.dll.NtQueryInformationToken Ord[232] Bound: 0x77F7ED73
ntdll.dll.NtOpenProcessToken Ord[199] Bound: 0x77F7EB63
ntdll.dll.NtResumeThread Ord[284] Bound: 0x77F7F093
ntdll.dll.NtAssignProcessToJobObject Ord[92] Bound: 0x77F7E4E3
ntdll.dll.CsrCaptureMessageMultiUnicodeStringsInPlace Ord[3] Bound: 0x77F62157
ntdll.dll.NtCreateThread Ord[127] Bound: 0x77F7E703
ntdll.dll.NtCreateProcessEx Ord[122] Bound: 0x77F7E6B3
ntdll.dll.LdrQueryImageFileExecutionOptions Ord[60] Bound: 0x77F68AEC
ntdll.dll.RtlDestroyEnvironment Ord[500] Bound: 0x77F65BDE
ntdll.dll.NtQuerySection Ord[244] Bound: 0x77F7EE23
ntdll.dll.NtQueryInformationJobObject Ord[228] Bound: 0x77F7ED33
ntdll.dll.RtlGetNativeSystemInformation Ord[596] Bound: 0x77F7EE83
ntdll.dll.RtlxAnsiStringToUnicodeSize Ord[871] Bound: 0x77FA15FE
ntdll.dll.NtOpenEvent Ord[189] Bound: 0x77F7EAD3
ntdll.dll.NtQueryEvent Ord[224] Bound: 0x77F7ECF3
ntdll.dll.NtTerminateThread Ord[336] Bound: 0x77F7F3D3
ntdll.dll.RtlxOemStringToUnicodeSize Ord[872] Bound: 0x77FA15FE
ntdll.dll.NlsMbOemCodePageTag Ord[72] Bound: 0x77FC5018
ntdll.dll.RtlxUnicodeStringToOemSize Ord[874] Bound: 0x77FA15E0
ntdll.dll.NtAdjustPrivilegesToken Ord[84] Bound: 0x77F7E463
ntdll.dll.RtlImpersonateSelf Ord[614] Bound: 0x77F5D7A6
ntdll.dll.RtlDestroyProcessParameters Ord[503] Bound: 0x77F68B0D
ntdll.dll.RtlCreateProcessParameters Ord[460] Bound: 0x77F6A21A
ntdll.dll.RtlInitializeCriticalSectionAndSpinCount Ord[627] Bound: 0x77F53355
ntdll.dll.NtSetEvent Ord[297] Bound: 0x77F7F163
ntdll.dll.NtClearEvent Ord[97] Bound: 0x77F7E533
ntdll.dll.NtPulseEvent Ord[214] Bound: 0x77F7EC53
ntdll.dll.NtCreateSemaphore Ord[125] Bound: 0x77F7E6E3
ntdll.dll.NtOpenSemaphore Ord[202] Bound: 0x77F7EB93
ntdll.dll.NtReleaseSemaphore Ord[267] Bound: 0x77F7EF83
ntdll.dll.NtCreateMutant Ord[117] Bound: 0x77F7E663
ntdll.dll.NtOpenMutant Ord[196] Bound: 0x77F7EB33
ntdll.dll.NtReleaseMutant Ord[266] Bound: 0x77F7EF73
ntdll.dll.NtSignalAndWaitForSingleObject Ord[328] Bound: 0x77F7F353
ntdll.dll.NtWaitForMultipleObjects Ord[349] Bound: 0x77F7F493
ntdll.dll.NtDelayExecution Ord[134] Bound: 0x77F7E763
ntdll.dll.NtCreateTimer Ord[128] Bound: 0x77F7E713
ntdll.dll.NtOpenTimer Ord[207] Bound: 0x77F7EBE3
ntdll.dll.NtSetTimer Ord[322] Bound: 0x77F7F2F3
ntdll.dll.NtCancelTimer Ord[96] Bound: 0x77F7E523
ntdll.dll.NtCreateEvent Ord[108] Bound: 0x77F7E5E3
ntdll.dll.RtlCopyLuid Ord[443] Bound: 0x77F56C9E
ntdll.dll.strchr Ord[1369] Bound: 0x77F815FD
ntdll.dll.strrchr Ord[1378] Bound: 0x77F81A86
ntdll.dll.wcsrchr Ord[1402] Bound: 0x77F56C6E
ntdll.dll.RtlReleaseActivationContext Ord[744] Bound: 0x77F5C014
ntdll.dll.RtlActivateActivationContextEx Ord[370] Bound: 0x77F5F002
ntdll.dll.RtlQueryInformationActivationContext Ord[720] Bound: 0x77F5351E
ntdll.dll.NtOpenThread Ord[204] Bound: 0x77F7EBB3
ntdll.dll.LdrShutdownThread Ord[65] Bound: 0x77F57AB1
ntdll.dll.RtlFreeThreadActivationContextStack Ord[572] Bound: 0x77F57B95
ntdll.dll.NtGetContextThread Ord[160] Bound: 0x77F7E903
ntdll.dll.NtSetContextThread Ord[291] Bound: 0x77F7F103
ntdll.dll.NtSuspendThread Ord[332] Bound: 0x77F7F393
ntdll.dll.RtlRaiseException Ord[733] Bound: 0x77F51124
ntdll.dll.tolower Ord[1385] Bound: 0x77F79B39
ntdll.dll.CsrIdentifyAlertableThread Ord[10] Bound: 0x77F96EA7
ntdll.dll.RtlApplicationVerifierStop Ord[403] Bound: 0x77F9A6E2
ntdll.dll.RtlClearBits Ord[421] Bound: 0x77F619C2
ntdll.dll.RtlFindClearBitsAndSet Ord[550] Bound: 0x77F5AD72
ntdll.dll.RtlAreBitsSet Ord[409] Bound: 0x77F61964
ntdll.dll.NtQueueApcThread Ord[257] Bound: 0x77F7EEF3
ntdll.dll.NtYieldExecution Ord[357] Bound: 0x77F7F513
ntdll.dll.RtlRegisterWait Ord[743] Bound: 0x77F64C50
ntdll.dll.RtlDeregisterWait Ord[497] Bound: 0x77F64906
ntdll.dll.RtlDeregisterWaitEx Ord[498] Bound: 0x77F64A9C
ntdll.dll.RtlQueueWorkItem Ord[732] Bound: 0x77F5C1AB
ntdll.dll.RtlSetIoCompletionCallback Ord[772] Bound: 0x77F7B41C
ntdll.dll.RtlCreateTimerQueue Ord[467] Bound: 0x77F791F2
ntdll.dll.RtlCreateTimer Ord[466] Bound: 0x77F78ADC
ntdll.dll.RtlUpdateTimer Ord[840] Bound: 0x77F64769
ntdll.dll.RtlDeleteTimer Ord[494] Bound: 0x77F78827
ntdll.dll.RtlDeleteTimerQueueEx Ord[496] Bound: 0x77FA24FB
ntdll.dll.RtlDestroyQueryDebugBuffer Ord[504] Bound: 0x77F98E02
ntdll.dll.RtlQueryProcessDebugInformation Ord[724] Bound: 0x77F9961A
ntdll.dll.RtlCreateQueryDebugBuffer Ord[461] Bound: 0x77F98D21
ntdll.dll.RtlCreateEnvironment Ord[458] Bound: 0x77F65B8B
ntdll.dll.RtlFreeOemString Ord[569] Bound: 0x77F65576
ntdll.dll.strstr Ord[1380] Bound: 0x77F81AEA
ntdll.dll.toupper Ord[1386] Bound: 0x77F633A8
ntdll.dll.isdigit Ord[1340] Bound: 0x77F79B62
ntdll.dll.atol Ord[1331] Bound: 0x77F613DA
ntdll.dll.NtOpenJobObject Ord[193] Bound: 0x77F7EB13
ntdll.dll.NtTerminateJobObject Ord[334] Bound: 0x77F7F3B3
ntdll.dll.NtSetInformationJobObject Ord[303] Bound: 0x77F7F1C3
ntdll.dll.RtlAddRefActivationContext Ord[387] Bound: 0x77F51946
ntdll.dll.RtlZombifyActivationContext Ord[859] Bound: 0x77F9B520
ntdll.dll.RtlActivateActivationContext Ord[369] Bound: 0x77F5F176
ntdll.dll.RtlDeactivateActivationContext Ord[476] Bound: 0x77F5F1B0
ntdll.dll.RtlFindActivationContextSectionString Ord[547] Bound: 0x77F5580E
ntdll.dll.DbgPrintEx Ord[17] Bound: 0x77F5B6EE
ntdll.dll.RtlFindActivationContextSectionGuid Ord[546] Bound: 0x77F5F6DA
ntdll.dll.RtlGetActiveActivationContext Ord[578] Bound: 0x77F58294
ntdll.dll.LdrDestroyOutOfProcessImage Ord[42] Bound: 0x77F688E8
ntdll.dll.LdrAccessOutOfProcessResource Ord[37] Bound: 0x77F622C8
ntdll.dll.LdrFindCreateProcessManifest Ord[45] Bound: 0x77F6859A
ntdll.dll.LdrCreateOutOfProcessImage Ord[41] Bound: 0x77F68784
ntdll.dll.RtlNtStatusToDosErrorNoTeb Ord[699] Bound: 0x77F51257
ntdll.dll.RtlpApplyLengthFunction Ord[860] Bound: 0x77F62014
ntdll.dll.RtlGetLengthWithoutLastFullDosOrNtPathElement Ord[593] Bound: 0x77F622FB
ntdll.dll.RtlpEnsureBufferSize Ord[861] Bound: 0x77F68BDA
ntdll.dll.RtlMultiAppendUnicodeStringBuffer Ord[688] Bound: 0x77F684ED
ntdll.dll._snwprintf Ord[1306] Bound: 0x77F5B323
ntdll.dll.RtlCreateActivationContext Ord[454] Bound: 0x77F630F5
ntdll.dll._allshl Ord[1286] Bound: 0x77F80811
ntdll.dll.RtlNtPathNameToDosPathName Ord[697] Bound: 0x77F63819
ntdll.dll.wcsncmp Ord[1399] Bound: 0x77F5D074
ntdll.dll.CsrCaptureMessageBuffer Ord[2] Bound: 0x77F6AFFE
ntdll.dll.NtQueryInstallUILanguage Ord[233] Bound: 0x77F7ED83
ntdll.dll.NtQueryDefaultUILanguage Ord[220] Bound: 0x77F7ECB3
ntdll.dll.wcspbrk Ord[1401] Bound: 0x77F6437A
ntdll.dll._wcslwr Ord[1322] Bound: 0x77F6815F
ntdll.dll._wtol Ord[1327] Bound: 0x77F7D55E
ntdll.dll.RtlIntegerToUnicodeString Ord[640] Bound: 0x77F587E9
ntdll.dll.RtlOpenCurrentUser Ord[707] Bound: 0x77F57129
ntdll.dll.RtlLengthRequiredSid Ord[672] Bound: 0x77F5EF27
ntdll.dll.RtlGetDaclSecurityDescriptor Ord[584] Bound: 0x77F61258
ntdll.dll.NtCreateDirectoryObject Ord[107] Bound: 0x77F7E5D3
ntdll.dll.NtQueryDefaultLocale Ord[219] Bound: 0x77F7ECA3
ntdll.dll._strlwr Ord[1310] Bound: 0x77F7D79D
ntdll.dll.RtlUnwind Ord[831] Bound: 0x77F6183E

----------Bound imports----------

[IMAGE_BOUND_IMPORT_DESCRIPTOR]
TimeDateStamp:                 0x3B7DE01E [Fri Aug 17 20:25:18 2001]
OffsetModuleName:              0x10      
NumberOfModuleForwarderRefs:   0x0       
DLL: ntdll.dll

----------Resource directory----------

[IMAGE_RESOURCE_DIRECTORY]
Characteristics:               0x0       
TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
MajorVersion:                  0x0       
MinorVersion:                  0x0       
NumberOfNamedEntries:          0x0       
NumberOfIdEntries:             0x3       
  Id: [0x6] (RT_STRING)
  [IMAGE_RESOURCE_DIRECTORY_ENTRY]
  Name:                          0x6       
  OffsetToData:                  0x80000028
    [IMAGE_RESOURCE_DIRECTORY]
    Characteristics:               0x0       
    TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
    MajorVersion:                  0x0       
    MinorVersion:                  0x0       
    NumberOfNamedEntries:          0x0       
    NumberOfIdEntries:             0x66      
      Id: [0x1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x1       
      OffsetToData:                  0x80000398
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xD58     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD7AA8   
            Size:                          0x4E4     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x2]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x2       
      OffsetToData:                  0x800003B0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xD68     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD7F90   
            Size:                          0x3BA     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x3]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x3       
      OffsetToData:                  0x800003C8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xD78     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD8350   
            Size:                          0x3F8     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4       
      OffsetToData:                  0x800003E0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xD88     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD8748   
            Size:                          0x33C     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x5]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x5       
      OffsetToData:                  0x800003F8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xD98     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD8A88   
            Size:                          0x37A     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x6]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x6       
      OffsetToData:                  0x80000410
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDA8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD8E08   
            Size:                          0x26E     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x7]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x7       
      OffsetToData:                  0x80000428
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDB8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD9078   
            Size:                          0x2CA     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x8]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x8       
      OffsetToData:                  0x80000440
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDC8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD9348   
            Size:                          0x29A     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x9]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x9       
      OffsetToData:                  0x80000458
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDD8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD95E8   
            Size:                          0x374     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xA]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xA       
      OffsetToData:                  0x80000470
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDE8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD9960   
            Size:                          0x32C     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xB]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xB       
      OffsetToData:                  0x80000488
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xDF8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD9C90   
            Size:                          0x2FE     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC       
      OffsetToData:                  0x800004A0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE08     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xD9F90   
            Size:                          0x33C     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xD]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xD       
      OffsetToData:                  0x800004B8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE18     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDA2D0   
            Size:                          0x452     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xE]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xE       
      OffsetToData:                  0x800004D0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE28     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDA728   
            Size:                          0x3E0     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xF]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xF       
      OffsetToData:                  0x800004E8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE38     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDAB08   
            Size:                          0x3C4     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x10]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x10      
      OffsetToData:                  0x80000500
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE48     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDAED0   
            Size:                          0x420     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x11]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x11      
      OffsetToData:                  0x80000518
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE58     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDB2F0   
            Size:                          0x1D6     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x13]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x13      
      OffsetToData:                  0x80000530
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE68     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDB4C8   
            Size:                          0x8E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x14]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x14      
      OffsetToData:                  0x80000548
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE78     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDB558   
            Size:                          0x512     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x15]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x15      
      OffsetToData:                  0x80000560
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE88     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDBA70   
            Size:                          0x3D6     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x16]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x16      
      OffsetToData:                  0x80000578
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xE98     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDBE48   
            Size:                          0x42A     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x17]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x17      
      OffsetToData:                  0x80000590
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xEA8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC278   
            Size:                          0xA0      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x1C]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x1C      
      OffsetToData:                  0x800005A8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xEB8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC318   
            Size:                          0x5C      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x20]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x20      
      OffsetToData:                  0x800005C0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xEC8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC378   
            Size:                          0x6A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x2D]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x2D      
      OffsetToData:                  0x800005D8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xED8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC3E8   
            Size:                          0x50      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x2E]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x2E      
      OffsetToData:                  0x800005F0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xEE8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC438   
            Size:                          0x68      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x2F]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x2F      
      OffsetToData:                  0x80000608
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xEF8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC4A0   
            Size:                          0x56      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x31]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x31      
      OffsetToData:                  0x80000620
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF08     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC4F8   
            Size:                          0x4E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x36]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x36      
      OffsetToData:                  0x80000638
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF18     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC548   
            Size:                          0x22E     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x37]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x37      
      OffsetToData:                  0x80000650
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF28     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC778   
            Size:                          0x1CA     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x3B]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x3B      
      OffsetToData:                  0x80000668
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF38     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDC948   
            Size:                          0xC8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x3C]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x3C      
      OffsetToData:                  0x80000680
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF48     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDCA10   
            Size:                          0xB4      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x41]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x41      
      OffsetToData:                  0x80000698
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF58     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7A3E0   
            Size:                          0x3C4     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x42]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x42      
      OffsetToData:                  0x800006B0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF68     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7AB38   
            Size:                          0x2AE     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x43]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x43      
      OffsetToData:                  0x800006C8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF78     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7ADE8   
            Size:                          0x264     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x44]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x44      
      OffsetToData:                  0x800006E0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF88     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B050   
            Size:                          0x132     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x45]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x45      
      OffsetToData:                  0x800006F8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xF98     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B668   
            Size:                          0x174     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x46]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x46      
      OffsetToData:                  0x80000710
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFA8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B7E0   
            Size:                          0xA8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x47]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x47      
      OffsetToData:                  0x80000728
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFB8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDCAC8   
            Size:                          0x3E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x48]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x48      
      OffsetToData:                  0x80000740
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFC8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDCB08   
            Size:                          0x402     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4F]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4F      
      OffsetToData:                  0x80000758
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFD8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDCF10   
            Size:                          0x1F2     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x56]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x56      
      OffsetToData:                  0x80000770
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFE8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD108   
            Size:                          0x52      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x81]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x81      
      OffsetToData:                  0x80000788
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0xFF8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B188   
            Size:                          0x1C0     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x82]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x82      
      OffsetToData:                  0x800007A0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1008    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B348   
            Size:                          0x15E     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x83]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x83      
      OffsetToData:                  0x800007B8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1018    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B888   
            Size:                          0x56      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x84]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x84      
      OffsetToData:                  0x800007D0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1028    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B8E0   
            Size:                          0x76      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x85]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x85      
      OffsetToData:                  0x800007E8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1038    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B958   
            Size:                          0x56      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC1      
      OffsetToData:                  0x80000800
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1048    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B4A8   
            Size:                          0x1BE     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC2]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC2      
      OffsetToData:                  0x80000818
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1058    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7B9B0   
            Size:                          0x52      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x101]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x101     
      OffsetToData:                  0x80000830
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1068    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7BA08   
            Size:                          0x1A6     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x141]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x141     
      OffsetToData:                  0x80000848
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1078    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7BBB0   
            Size:                          0x1DA     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x181]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x181     
      OffsetToData:                  0x80000860
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1088    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7BD90   
            Size:                          0xFC      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x1C1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x1C1     
      OffsetToData:                  0x80000878
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1098    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7BE90   
            Size:                          0xF4      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x201]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x201     
      OffsetToData:                  0x80000890
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10A8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7BF88   
            Size:                          0xB0      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x241]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x241     
      OffsetToData:                  0x800008A8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10B8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C038   
            Size:                          0xB8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x272]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x272     
      OffsetToData:                  0x800008C0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10C8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD160   
            Size:                          0x242     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x273]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x273     
      OffsetToData:                  0x800008D8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10D8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD3A8   
            Size:                          0xAC      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x276]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x276     
      OffsetToData:                  0x800008F0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10E8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD458   
            Size:                          0x54      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x277]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x277     
      OffsetToData:                  0x80000908
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x10F8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD4B0   
            Size:                          0x80      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x281]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x281     
      OffsetToData:                  0x80000920
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1108    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C0F0   
            Size:                          0x9C      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x2C1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x2C1     
      OffsetToData:                  0x80000938
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1118    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C190   
            Size:                          0xD2      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x301]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x301     
      OffsetToData:                  0x80000950
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1128    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C268   
            Size:                          0xB8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x341]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x341     
      OffsetToData:                  0x80000968
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1138    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C320   
            Size:                          0xD8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x381]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x381     
      OffsetToData:                  0x80000980
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1148    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C3F8   
            Size:                          0x7E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x3B2]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x3B2     
      OffsetToData:                  0x80000998
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1158    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD530   
            Size:                          0x40      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x3C1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x3C1     
      OffsetToData:                  0x800009B0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1168    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C478   
            Size:                          0x86      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x401]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x401     
      OffsetToData:                  0x800009C8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1178    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C500   
            Size:                          0x7A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x441]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x441     
      OffsetToData:                  0x800009E0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1188    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C580   
            Size:                          0x62      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x481]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x481     
      OffsetToData:                  0x800009F8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1198    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C5E8   
            Size:                          0x56      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4C1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4C1     
      OffsetToData:                  0x80000A10
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11A8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C640   
            Size:                          0x5A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4CB]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4CB     
      OffsetToData:                  0x80000A28
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11B8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD570   
            Size:                          0xC8      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4E3]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4E3     
      OffsetToData:                  0x80000A40
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11C8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD638   
            Size:                          0x14A     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4E9]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4E9     
      OffsetToData:                  0x80000A58
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11D8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD788   
            Size:                          0x102     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4EA]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4EA     
      OffsetToData:                  0x80000A70
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11E8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD890   
            Size:                          0x46      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4F3]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4F3     
      OffsetToData:                  0x80000A88
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x11F8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD8D8   
            Size:                          0x8A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4F4]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4F4     
      OffsetToData:                  0x80000AA0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1208    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDD968   
            Size:                          0x1D2     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4F5]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4F5     
      OffsetToData:                  0x80000AB8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1218    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDB40   
            Size:                          0xC0      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x4FD]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x4FD     
      OffsetToData:                  0x80000AD0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1228    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDC00   
            Size:                          0xD2      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x501]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x501     
      OffsetToData:                  0x80000AE8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1238    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C6A0   
            Size:                          0x62      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x517]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x517     
      OffsetToData:                  0x80000B00
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1248    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDCD8   
            Size:                          0xA6      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x519]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x519     
      OffsetToData:                  0x80000B18
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1258    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDD80   
            Size:                          0x94      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x51A]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x51A     
      OffsetToData:                  0x80000B30
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1268    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDE18   
            Size:                          0x74      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x51B]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x51B     
      OffsetToData:                  0x80000B48
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1278    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDE90   
            Size:                          0x5E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x51C]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x51C     
      OffsetToData:                  0x80000B60
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1288    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDEF0   
            Size:                          0x92      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x51D]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x51D     
      OffsetToData:                  0x80000B78
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1298    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDDF88   
            Size:                          0xB4      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x523]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x523     
      OffsetToData:                  0x80000B90
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12A8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE040   
            Size:                          0xC6      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x530]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x530     
      OffsetToData:                  0x80000BA8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12B8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE108   
            Size:                          0x44      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x557]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x557     
      OffsetToData:                  0x80000BC0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12C8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE150   
            Size:                          0x5A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x60F]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x60F     
      OffsetToData:                  0x80000BD8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12D8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEE98   
            Size:                          0x3C      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x6FB]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x6FB     
      OffsetToData:                  0x80000BF0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12E8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE1B0   
            Size:                          0x5A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x6FC]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x6FC     
      OffsetToData:                  0x80000C08
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x12F8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE210   
            Size:                          0x254     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0x96D]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x96D     
      OffsetToData:                  0x80000C20
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1308    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE468   
            Size:                          0x7C      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC43]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC43     
      OffsetToData:                  0x80000C38
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1318    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE4E8   
            Size:                          0x14E     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC44]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC44     
      OffsetToData:                  0x80000C50
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1328    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE638   
            Size:                          0xEE      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xC70]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xC70     
      OffsetToData:                  0x80000C68
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1338    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE728   
            Size:                          0x2A4     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xCAE]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xCAE     
      OffsetToData:                  0x80000C80
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1348    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDE9D0   
            Size:                          0x4E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xCAF]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xCAF     
      OffsetToData:                  0x80000C98
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1358    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEA20   
            Size:                          0xD0      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xCED]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xCED     
      OffsetToData:                  0x80000CB0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1368    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEAF0   
            Size:                          0x6E      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xD6A]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xD6A     
      OffsetToData:                  0x80000CC8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1378    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEB60   
            Size:                          0x6A      
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xDEB]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xDEB     
      OffsetToData:                  0x80000CE0
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1388    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEBD0   
            Size:                          0x156     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xDEC]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xDEC     
      OffsetToData:                  0x80000CF8
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x1398    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDED28   
            Size:                          0x10C     
            CodePage:                      0x0       
            Reserved:                      0x0       
      Id: [0xFDF]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0xFDF     
      OffsetToData:                  0x80000D10
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x13A8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0xDEE38   
            Size:                          0x60      
            CodePage:                      0x0       
            Reserved:                      0x0       

  Id: [0xB] (RT_MESSAGETABLE)
  [IMAGE_RESOURCE_DIRECTORY_ENTRY]
  Name:                          0xB       
  OffsetToData:                  0x80000368
    [IMAGE_RESOURCE_DIRECTORY]
    Characteristics:               0x0       
    TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
    MajorVersion:                  0x0       
    MinorVersion:                  0x0       
    NumberOfNamedEntries:          0x0       
    NumberOfIdEntries:             0x1       
      Id: [0x1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x1       
      OffsetToData:                  0x80000D28
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x13B8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7C708   
            Size:                          0x5B3A0   
            CodePage:                      0x0       
            Reserved:                      0x0       

  Id: [0x10] (RT_VERSION)
  [IMAGE_RESOURCE_DIRECTORY_ENTRY]
  Name:                          0x10      
  OffsetToData:                  0x80000380
    [IMAGE_RESOURCE_DIRECTORY]
    Characteristics:               0x0       
    TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
    MajorVersion:                  0x0       
    MinorVersion:                  0x0       
    NumberOfNamedEntries:          0x0       
    NumberOfIdEntries:             0x1       
      Id: [0x1]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x1       
      OffsetToData:                  0x80000D40
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Wed Dec 31 16:00:00 1969]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x13C8    
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x7A7A8   
            Size:                          0x38C     
            CodePage:                      0x0       
            Reserved:                      0x0       


----------Debug information----------

[IMAGE_DEBUG_DIRECTORY]
Characteristics:               0x0       
TimeDateStamp:                 0x3B7DDFD8 [Fri Aug 17 20:24:08 2001]
MajorVersion:                  0x0       
MinorVersion:                  0x0       
Type:                          0x2       
SizeOfData:                    0x1D      
AddressOfRawData:              0x72CA4   
PointerToRawData:              0x720A4   
Type: IMAGE_DEBUG_TYPE_CODEVIEW

[IMAGE_DEBUG_DIRECTORY]
Characteristics:               0x0       
TimeDateStamp:                 0x3B7DDFD8 [Fri Aug 17 20:24:08 2001]
MajorVersion:                  0x0       
MinorVersion:                  0x0       
Type:                          0xA       
SizeOfData:                    0x0       
AddressOfRawData:              0x0       
PointerToRawData:              0x0       
Type: IMAGE_DEBUG_TYPE_RESERVED10

----------Base relocations----------

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1000    
SizeOfBlock:                   0xB8      
    00001631h HIGHLOW
    000016C5h HIGHLOW
    0000177Dh HIGHLOW
    00001794h HIGHLOW
    0000179Fh HIGHLOW
    000017B8h HIGHLOW
    000017C4h HIGHLOW
    000017C9h HIGHLOW
    000017DCh HIGHLOW
    000017E8h HIGHLOW
    000017F4h HIGHLOW
    00001800h HIGHLOW
    0000180Ch HIGHLOW
    00001818h HIGHLOW
    00001824h HIGHLOW
    00001830h HIGHLOW
    0000183Dh HIGHLOW
    0000184Eh HIGHLOW
    0000185Eh HIGHLOW
    0000186Ah HIGHLOW
    00001876h HIGHLOW
    00001882h HIGHLOW
    0000188Ah HIGHLOW
    00001892h HIGHLOW
    0000189Ah HIGHLOW
    000018B0h HIGHLOW
    000018C6h HIGHLOW
    000018E9h HIGHLOW
    0000190Ch HIGHLOW
    0000191Dh HIGHLOW
    0000192Ah HIGHLOW
    00001936h HIGHLOW
    00001942h HIGHLOW
    0000194Eh HIGHLOW
    0000195Ah HIGHLOW
    00001966h HIGHLOW
    00001972h HIGHLOW
    0000197Eh HIGHLOW
    0000198Ah HIGHLOW
    00001996h HIGHLOW
    000019A2h HIGHLOW
    000019AEh HIGHLOW
    000019BCh HIGHLOW
    000019CAh HIGHLOW
    000019F5h HIGHLOW
    000019FAh HIGHLOW
    00001A06h HIGHLOW
    00001A12h HIGHLOW
    00001A1Eh HIGHLOW
    00001A29h HIGHLOW
    00001A35h HIGHLOW
    00001A41h HIGHLOW
    00001A4Fh HIGHLOW
    00001A69h HIGHLOW
    00001A9Fh HIGHLOW
    00001AE3h HIGHLOW
    00001B15h HIGHLOW
    00001B74h HIGHLOW
    00001C00h HIGHLOW
    00001C12h HIGHLOW
    00001C24h HIGHLOW
    00001C2Fh HIGHLOW
    00001C7Ch HIGHLOW
    00001C98h HIGHLOW
    00001CA4h HIGHLOW
    00001CADh HIGHLOW
    00001D18h HIGHLOW
    00001D1Dh HIGHLOW
    00001D22h HIGHLOW
    00001D27h HIGHLOW
    00001D2Dh HIGHLOW
    00001D31h HIGHLOW
    00001D37h HIGHLOW
    00001D3Bh HIGHLOW
    00001D6Ah HIGHLOW
    00001D83h HIGHLOW
    00001DA6h HIGHLOW
    00001DAFh HIGHLOW
    00001DF8h HIGHLOW
    00001E15h HIGHLOW
    00001E4Eh HIGHLOW
    00001E66h HIGHLOW
    00001E99h HIGHLOW
    00001EA9h HIGHLOW
    00001EE1h HIGHLOW
    00001F16h HIGHLOW
    00001F59h HIGHLOW
    00001F65h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2000    
SizeOfBlock:                   0x68      
    000021CDh HIGHLOW
    000021D9h HIGHLOW
    000021F2h HIGHLOW
    0000224Bh HIGHLOW
    00002285h HIGHLOW
    0000238Bh HIGHLOW
    00002473h HIGHLOW
    00002482h HIGHLOW
    000024A9h HIGHLOW
    000024FBh HIGHLOW
    0000254Ah HIGHLOW
    000025C1h HIGHLOW
    00002617h HIGHLOW
    000026F4h HIGHLOW
    00002775h HIGHLOW
    000027A1h HIGHLOW
    00002808h HIGHLOW
    00002814h HIGHLOW
    0000282Fh HIGHLOW
    00002921h HIGHLOW
    00002943h HIGHLOW
    0000294Fh HIGHLOW
    0000299Bh HIGHLOW
    000029C3h HIGHLOW
    000029CFh HIGHLOW
    00002A1Eh HIGHLOW
    00002A42h HIGHLOW
    00002A6Fh HIGHLOW
    00002AABh HIGHLOW
    00002BDAh HIGHLOW
    00002BEFh HIGHLOW
    00002BFAh HIGHLOW
    00002C09h HIGHLOW
    00002D61h HIGHLOW
    00002D6Ah HIGHLOW
    00002D8Fh HIGHLOW
    00002D9Ah HIGHLOW
    00002DD1h HIGHLOW
    00002DDBh HIGHLOW
    00002E11h HIGHLOW
    00002E26h HIGHLOW
    00002EC4h HIGHLOW
    00002F00h HIGHLOW
    00002F0Fh HIGHLOW
    00002F40h HIGHLOW
    00002F58h HIGHLOW
    00002FC9h HIGHLOW
    00002FF2h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3000    
SizeOfBlock:                   0x84      
    00003021h HIGHLOW
    0000304Bh HIGHLOW
    0000305Bh HIGHLOW
    000030A4h HIGHLOW
    000030C0h HIGHLOW
    000030CBh HIGHLOW
    00003122h HIGHLOW
    00003132h HIGHLOW
    00003153h HIGHLOW
    00003245h HIGHLOW
    00003258h HIGHLOW
    0000326Bh HIGHLOW
    00003272h HIGHLOW
    0000329Bh HIGHLOW
    000032A2h HIGHLOW
    00003323h HIGHLOW
    0000334Bh HIGHLOW
    00003360h HIGHLOW
    0000339Eh HIGHLOW
    00003450h HIGHLOW
    00003495h HIGHLOW
    000034A9h HIGHLOW
    000034EAh HIGHLOW
    000034F6h HIGHLOW
    000036A5h HIGHLOW
    000036F8h HIGHLOW
    00003777h HIGHLOW
    0000377Ch HIGHLOW
    000037B3h HIGHLOW
    000037D3h HIGHLOW
    0000388Fh HIGHLOW
    000038B0h HIGHLOW
    000038EEh HIGHLOW
    000038FEh HIGHLOW
    00003A03h HIGHLOW
    00003C3Ch HIGHLOW
    00003CBAh HIGHLOW
    00003CCCh HIGHLOW
    00003D1Dh HIGHLOW
    00003D22h HIGHLOW
    00003D5Dh HIGHLOW
    00003D62h HIGHLOW
    00003D92h HIGHLOW
    00003DA6h HIGHLOW
    00003DDCh HIGHLOW
    00003DE1h HIGHLOW
    00003E8Eh HIGHLOW
    00003E9Fh HIGHLOW
    00003EF6h HIGHLOW
    00003EFBh HIGHLOW
    00003F45h HIGHLOW
    00003F6Bh HIGHLOW
    00003F7Ch HIGHLOW
    00003F82h HIGHLOW
    00003F9Eh HIGHLOW
    00003FA4h HIGHLOW
    00003FA9h HIGHLOW
    00003FB9h HIGHLOW
    00003FDCh HIGHLOW
    00003FE6h HIGHLOW
    00003FECh HIGHLOW
    00003000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4000    
SizeOfBlock:                   0x98      
    00004314h HIGHLOW
    00004319h HIGHLOW
    00004332h HIGHLOW
    00004361h HIGHLOW
    000043BBh HIGHLOW
    000043C0h HIGHLOW
    0000440Ch HIGHLOW
    00004411h HIGHLOW
    00004483h HIGHLOW
    000044B0h HIGHLOW
    000044B8h HIGHLOW
    000044C0h HIGHLOW
    000044C5h HIGHLOW
    000044D1h HIGHLOW
    000044DEh HIGHLOW
    00004528h HIGHLOW
    00004548h HIGHLOW
    0000460Ch HIGHLOW
    00004614h HIGHLOW
    00004638h HIGHLOW
    0000463Dh HIGHLOW
    00004666h HIGHLOW
    000046A7h HIGHLOW
    000046ADh HIGHLOW
    000046B6h HIGHLOW
    000046BEh HIGHLOW
    000046CAh HIGHLOW
    000046D7h HIGHLOW
    000046F7h HIGHLOW
    0000470Dh HIGHLOW
    000047ADh HIGHLOW
    000047BDh HIGHLOW
    000047DDh HIGHLOW
    0000488Ah HIGHLOW
    00004906h HIGHLOW
    0000491Ah HIGHLOW
    000049B5h HIGHLOW
    000049CCh HIGHLOW
    000049D9h HIGHLOW
    000049FEh HIGHLOW
    00004A0Bh HIGHLOW
    00004A45h HIGHLOW
    00004A98h HIGHLOW
    00004AA5h HIGHLOW
    00004AAAh HIGHLOW
    00004AAFh HIGHLOW
    00004ACDh HIGHLOW
    00004ADAh HIGHLOW
    00004ADFh HIGHLOW
    00004AE4h HIGHLOW
    00004B0Ch HIGHLOW
    00004B19h HIGHLOW
    00004B1Eh HIGHLOW
    00004B23h HIGHLOW
    00004BA1h HIGHLOW
    00004C1Bh HIGHLOW
    00004C8Bh HIGHLOW
    00004D5Bh HIGHLOW
    00004D61h HIGHLOW
    00004DADh HIGHLOW
    00004DBBh HIGHLOW
    00004DC1h HIGHLOW
    00004DF4h HIGHLOW
    00004DFAh HIGHLOW
    00004E10h HIGHLOW
    00004E16h HIGHLOW
    00004E76h HIGHLOW
    00004F24h HIGHLOW
    00004FE3h HIGHLOW
    00004FEAh HIGHLOW
    00004FFEh HIGHLOW
    00004000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5000    
SizeOfBlock:                   0x94      
    00005025h HIGHLOW
    0000512Ch HIGHLOW
    0000514Fh HIGHLOW
    00005162h HIGHLOW
    0000519Dh HIGHLOW
    000051B0h HIGHLOW
    000052D9h HIGHLOW
    0000532Eh HIGHLOW
    0000533Eh HIGHLOW
    000053D1h HIGHLOW
    0000540Ah HIGHLOW
    00005444h HIGHLOW
    00005457h HIGHLOW
    00005477h HIGHLOW
    000054A0h HIGHLOW
    000054AAh HIGHLOW
    000054C5h HIGHLOW
    000054DAh HIGHLOW
    00005537h HIGHLOW
    00005542h HIGHLOW
    00005558h HIGHLOW
    0000557Fh HIGHLOW
    00005590h HIGHLOW
    000055B1h HIGHLOW
    000055F0h HIGHLOW
    0000563Fh HIGHLOW
    0000568Ah HIGHLOW
    00005730h HIGHLOW
    00005743h HIGHLOW
    0000578Eh HIGHLOW
    000057B0h HIGHLOW
    000057C3h HIGHLOW
    000057D8h HIGHLOW
    000057E1h HIGHLOW
    000057E8h HIGHLOW
    0000587Bh HIGHLOW
    0000588Eh HIGHLOW
    000058D5h HIGHLOW
    000058E8h HIGHLOW
    0000591Dh HIGHLOW
    00005930h HIGHLOW
    00005965h HIGHLOW
    00005978h HIGHLOW
    0000599Eh HIGHLOW
    000059CFh HIGHLOW
    000059E1h HIGHLOW
    00005CD9h HIGHLOW
    00005CF4h HIGHLOW
    00005D02h HIGHLOW
    00005D67h HIGHLOW
    00005D71h HIGHLOW
    00005DAEh HIGHLOW
    00005DBDh HIGHLOW
    00005DC3h HIGHLOW
    00005E70h HIGHLOW
    00005E8Ah HIGHLOW
    00005E99h HIGHLOW
    00005EADh HIGHLOW
    00005ECBh HIGHLOW
    00005EDFh HIGHLOW
    00005EFDh HIGHLOW
    00005F18h HIGHLOW
    00005F33h HIGHLOW
    00005F43h HIGHLOW
    00005F67h HIGHLOW
    00005F70h HIGHLOW
    00005FAFh HIGHLOW
    00005FB4h HIGHLOW
    00005FDDh HIGHLOW
    00005FF8h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6000    
SizeOfBlock:                   0x78      
    0000602Bh HIGHLOW
    00006035h HIGHLOW
    00006063h HIGHLOW
    0000611Fh HIGHLOW
    0000621Ch HIGHLOW
    00006246h HIGHLOW
    00006266h HIGHLOW
    00006272h HIGHLOW
    0000629Bh HIGHLOW
    000062ADh HIGHLOW
    000062BCh HIGHLOW
    000062E9h HIGHLOW
    000062F5h HIGHLOW
    00006312h HIGHLOW
    00006321h HIGHLOW
    0000634Ah HIGHLOW
    00006389h HIGHLOW
    00006390h HIGHLOW
    000063B2h HIGHLOW
    00006412h HIGHLOW
    0000644Bh HIGHLOW
    000064ABh HIGHLOW
    0000687Bh HIGHLOW
    00006893h HIGHLOW
    00006906h HIGHLOW
    00006916h HIGHLOW
    00006943h HIGHLOW
    0000694Ch HIGHLOW
    0000696Dh HIGHLOW
    0000699Ah HIGHLOW
    000069B2h HIGHLOW
    000069BCh HIGHLOW
    00006A4Ah HIGHLOW
    00006A4Fh HIGHLOW
    00006A5Fh HIGHLOW
    00006A95h HIGHLOW
    00006AF1h HIGHLOW
    00006B06h HIGHLOW
    00006BBBh HIGHLOW
    00006BEBh HIGHLOW
    00006C39h HIGHLOW
    00006CA1h HIGHLOW
    00006CABh HIGHLOW
    00006CDAh HIGHLOW
    00006D24h HIGHLOW
    00006DC8h HIGHLOW
    00006E47h HIGHLOW
    00006E82h HIGHLOW
    00006ED4h HIGHLOW
    00006EE0h HIGHLOW
    00006F09h HIGHLOW
    00006F18h HIGHLOW
    00006F5Fh HIGHLOW
    00006FA7h HIGHLOW
    00006FBCh HIGHLOW
    00006000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x7000    
SizeOfBlock:                   0x88      
    00007019h HIGHLOW
    00007032h HIGHLOW
    0000703Eh HIGHLOW
    00007077h HIGHLOW
    0000707Ch HIGHLOW
    000070BAh HIGHLOW
    000070BFh HIGHLOW
    000070ECh HIGHLOW
    000070F1h HIGHLOW
    00007132h HIGHLOW
    00007137h HIGHLOW
    00007164h HIGHLOW
    00007169h HIGHLOW
    000071A2h HIGHLOW
    000071A7h HIGHLOW
    000071F4h HIGHLOW
    00007211h HIGHLOW
    0000724Ah HIGHLOW
    000072AFh HIGHLOW
    000073C5h HIGHLOW
    000073CAh HIGHLOW
    0000742Ch HIGHLOW
    000074D1h HIGHLOW
    000074DAh HIGHLOW
    00007592h HIGHLOW
    0000766Bh HIGHLOW
    00007670h HIGHLOW
    000076A2h HIGHLOW
    000076A7h HIGHLOW
    000076E2h HIGHLOW
    000076E7h HIGHLOW
    00007742h HIGHLOW
    00007752h HIGHLOW
    00007781h HIGHLOW
    000077C1h HIGHLOW
    000077F6h HIGHLOW
    000077FBh HIGHLOW
    00007827h HIGHLOW
    0000782Dh HIGHLOW
    00007843h HIGHLOW
    00007849h HIGHLOW
    000078B3h HIGHLOW
    0000790Dh HIGHLOW
    00007923h HIGHLOW
    00007938h HIGHLOW
    0000793Dh HIGHLOW
    00007949h HIGHLOW
    00007972h HIGHLOW
    00007978h HIGHLOW
    00007A04h HIGHLOW
    00007A4Eh HIGHLOW
    00007A5Ah HIGHLOW
    00007E94h HIGHLOW
    00007E9Bh HIGHLOW
    00007EA2h HIGHLOW
    00007ED8h HIGHLOW
    00007EEBh HIGHLOW
    00007F18h HIGHLOW
    00007F95h HIGHLOW
    00007FADh HIGHLOW
    00007FBCh HIGHLOW
    00007FF5h HIGHLOW
    00007FFDh HIGHLOW
    00007000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x8000    
SizeOfBlock:                   0x80      
    00008043h HIGHLOW
    00008054h HIGHLOW
    00008068h HIGHLOW
    000080F6h HIGHLOW
    000080FDh HIGHLOW
    00008102h HIGHLOW
    00008128h HIGHLOW
    0000815Dh HIGHLOW
    0000817Eh HIGHLOW
    000081F2h HIGHLOW
    0000833Bh HIGHLOW
    000083A4h HIGHLOW
    00008406h HIGHLOW
    00008412h HIGHLOW
    0000842Fh HIGHLOW
    00008442h HIGHLOW
    00008458h HIGHLOW
    000084ACh HIGHLOW
    00008513h HIGHLOW
    0000852Ah HIGHLOW
    00008559h HIGHLOW
    0000858Bh HIGHLOW
    000085D2h HIGHLOW
    000085EEh HIGHLOW
    00008603h HIGHLOW
    0000860Eh HIGHLOW
    00008711h HIGHLOW
    00008798h HIGHLOW
    0000887Fh HIGHLOW
    000088CCh HIGHLOW
    00008901h HIGHLOW
    0000890Dh HIGHLOW
    00008913h HIGHLOW
    00008919h HIGHLOW
    00008921h HIGHLOW
    00008927h HIGHLOW
    0000892Ch HIGHLOW
    0000896Fh HIGHLOW
    0000897Eh HIGHLOW
    00008993h HIGHLOW
    000089A3h HIGHLOW
    000089C5h HIGHLOW
    000089DFh HIGHLOW
    000089E6h HIGHLOW
    00008A01h HIGHLOW
    00008A3Dh HIGHLOW
    00008A4Ch HIGHLOW
    00008A86h HIGHLOW
    00008B2Bh HIGHLOW
    00008B4Fh HIGHLOW
    00008BA2h HIGHLOW
    00008BF2h HIGHLOW
    00008D2Dh HIGHLOW
    00008DA1h HIGHLOW
    00008E4Dh HIGHLOW
    00008E82h HIGHLOW
    00008E90h HIGHLOW
    00008F0Eh HIGHLOW
    00008F19h HIGHLOW
    00008000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x9000    
SizeOfBlock:                   0x84      
    0000914Ch HIGHLOW
    000091B4h HIGHLOW
    000091BDh HIGHLOW
    000091CCh HIGHLOW
    0000922Dh HIGHLOW
    00009252h HIGHLOW
    00009277h HIGHLOW
    00009292h HIGHLOW
    000092F7h HIGHLOW
    00009306h HIGHLOW
    00009323h HIGHLOW
    0000932Bh HIGHLOW
    00009339h HIGHLOW
    00009344h HIGHLOW
    0000934Bh HIGHLOW
    00009365h HIGHLOW
    00009393h HIGHLOW
    000093CFh HIGHLOW
    000093DAh HIGHLOW
    000093F3h HIGHLOW
    00009423h HIGHLOW
    00009534h HIGHLOW
    0000953Fh HIGHLOW
    00009611h HIGHLOW
    00009676h HIGHLOW
    00009694h HIGHLOW
    000096A5h HIGHLOW
    000096B6h HIGHLOW
    00009725h HIGHLOW
    00009780h HIGHLOW
    00009785h HIGHLOW
    000097C4h HIGHLOW
    000097EEh HIGHLOW
    00009829h HIGHLOW
    00009866h HIGHLOW
    00009880h HIGHLOW
    000098DAh HIGHLOW
    00009911h HIGHLOW
    00009AF2h HIGHLOW
    00009B89h HIGHLOW
    00009BAEh HIGHLOW
    00009C14h HIGHLOW
    00009C43h HIGHLOW
    00009C5Ah HIGHLOW
    00009C99h HIGHLOW
    00009CB3h HIGHLOW
    00009D41h HIGHLOW
    00009D5Fh HIGHLOW
    00009D64h HIGHLOW
    00009D82h HIGHLOW
    00009D87h HIGHLOW
    00009D97h HIGHLOW
    00009E11h HIGHLOW
    00009E17h HIGHLOW
    00009E42h HIGHLOW
    00009E4Bh HIGHLOW
    00009E84h HIGHLOW
    00009EDBh HIGHLOW
    00009EE8h HIGHLOW
    00009F35h HIGHLOW
    00009F67h HIGHLOW
    00009FE2h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xA000    
SizeOfBlock:                   0x88      
    0000A059h HIGHLOW
    0000A08Eh HIGHLOW
    0000A0A8h HIGHLOW
    0000A0D3h HIGHLOW
    0000A0DCh HIGHLOW
    0000A12Bh HIGHLOW
    0000A134h HIGHLOW
    0000A190h HIGHLOW
    0000A198h HIGHLOW
    0000A1BAh HIGHLOW
    0000A3A9h HIGHLOW
    0000A414h HIGHLOW
    0000A41Fh HIGHLOW
    0000A463h HIGHLOW
    0000A479h HIGHLOW
    0000A587h HIGHLOW
    0000A590h HIGHLOW
    0000A5D9h HIGHLOW
    0000A603h HIGHLOW
    0000A60Ch HIGHLOW
    0000A639h HIGHLOW
    0000A71Ah HIGHLOW
    0000A723h HIGHLOW
    0000A7C5h HIGHLOW
    0000A930h HIGHLOW
    0000A958h HIGHLOW
    0000A964h HIGHLOW
    0000A975h HIGHLOW
    0000A981h HIGHLOW
    0000A988h HIGHLOW
    0000A98Fh HIGHLOW
    0000A9A0h HIGHLOW
    0000A9EEh HIGHLOW
    0000AA0Eh HIGHLOW
    0000AA41h HIGHLOW
    0000AA59h HIGHLOW
    0000AA7Dh HIGHLOW
    0000AAA3h HIGHLOW
    0000AB3Bh HIGHLOW
    0000AB5Ah HIGHLOW
    0000ABAAh HIGHLOW
    0000ABE1h HIGHLOW
    0000AC0Ch HIGHLOW
    0000AC7Eh HIGHLOW
    0000AC87h HIGHLOW
    0000ACD0h HIGHLOW
    0000AD09h HIGHLOW
    0000AD56h HIGHLOW
    0000AD5Dh HIGHLOW
    0000AD88h HIGHLOW
    0000ADB7h HIGHLOW
    0000AE27h HIGHLOW
    0000AE42h HIGHLOW
    0000AEAAh HIGHLOW
    0000AEDFh HIGHLOW
    0000AF07h HIGHLOW
    0000AF19h HIGHLOW
    0000AF30h HIGHLOW
    0000AF37h HIGHLOW
    0000AF3Eh HIGHLOW
    0000AF4Fh HIGHLOW
    0000AF7Eh HIGHLOW
    0000AFD2h HIGHLOW
    0000AFDBh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xB000    
SizeOfBlock:                   0x68      
    0000B008h HIGHLOW
    0000B024h HIGHLOW
    0000B036h HIGHLOW
    0000B04Dh HIGHLOW
    0000B062h HIGHLOW
    0000B170h HIGHLOW
    0000B194h HIGHLOW
    0000B1DDh HIGHLOW
    0000B1E9h HIGHLOW
    0000B20Dh HIGHLOW
    0000B328h HIGHLOW
    0000B353h HIGHLOW
    0000B3A6h HIGHLOW
    0000B420h HIGHLOW
    0000B57Ah HIGHLOW
    0000B5AAh HIGHLOW
    0000B663h HIGHLOW
    0000B742h HIGHLOW
    0000B7BAh HIGHLOW
    0000B7EFh HIGHLOW
    0000B823h HIGHLOW
    0000B923h HIGHLOW
    0000B996h HIGHLOW
    0000B9E6h HIGHLOW
    0000B9F8h HIGHLOW
    0000BA63h HIGHLOW
    0000BAAFh HIGHLOW
    0000BB23h HIGHLOW
    0000BB3Ch HIGHLOW
    0000BB8Dh HIGHLOW
    0000BD59h HIGHLOW
    0000BD71h HIGHLOW
    0000BD81h HIGHLOW
    0000BDA1h HIGHLOW
    0000BDD4h HIGHLOW
    0000BE0Ah HIGHLOW
    0000BE1Eh HIGHLOW
    0000BE24h HIGHLOW
    0000BE3Fh HIGHLOW
    0000BE45h HIGHLOW
    0000BE61h HIGHLOW
    0000BE67h HIGHLOW
    0000BE74h HIGHLOW
    0000BE7Ah HIGHLOW
    0000BE98h HIGHLOW
    0000BF03h HIGHLOW
    0000BF2Dh HIGHLOW
    0000BFCAh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xC000    
SizeOfBlock:                   0xDC      
    0000C024h HIGHLOW
    0000C08Dh HIGHLOW
    0000C111h HIGHLOW
    0000C1A0h HIGHLOW
    0000C1CCh HIGHLOW
    0000C1F8h HIGHLOW
    0000C207h HIGHLOW
    0000C236h HIGHLOW
    0000C23Bh HIGHLOW
    0000C2B1h HIGHLOW
    0000C2DAh HIGHLOW
    0000C2E5h HIGHLOW
    0000C33Eh HIGHLOW
    0000C352h HIGHLOW
    0000C360h HIGHLOW
    0000C365h HIGHLOW
    0000C39Dh HIGHLOW
    0000C3BBh HIGHLOW
    0000C3E3h HIGHLOW
    0000C3F3h HIGHLOW
    0000C420h HIGHLOW
    0000C45Fh HIGHLOW
    0000C46Fh HIGHLOW
    0000C48Eh HIGHLOW
    0000C49Ah HIGHLOW
    0000C4F2h HIGHLOW
    0000C50Ch HIGHLOW
    0000C527h HIGHLOW
    0000C531h HIGHLOW
    0000C560h HIGHLOW
    0000C5B3h HIGHLOW
    0000C5F9h HIGHLOW
    0000C605h HIGHLOW
    0000C662h HIGHLOW
    0000C698h HIGHLOW
    0000C704h HIGHLOW
    0000C747h HIGHLOW
    0000C77Bh HIGHLOW
    0000C781h HIGHLOW
    0000C793h HIGHLOW
    0000C79Ah HIGHLOW
    0000C7BFh HIGHLOW
    0000C7CEh HIGHLOW
    0000C7D4h HIGHLOW
    0000C7EDh HIGHLOW
    0000C7F3h HIGHLOW
    0000C7FDh HIGHLOW
    0000C803h HIGHLOW
    0000C84Dh HIGHLOW
    0000C862h HIGHLOW
    0000C87Ch HIGHLOW
    0000C890h HIGHLOW
    0000C896h HIGHLOW
    0000C8B1h HIGHLOW
    0000C8B7h HIGHLOW
    0000C8D3h HIGHLOW
    0000C8D9h HIGHLOW
    0000C8E6h HIGHLOW
    0000C8ECh HIGHLOW
    0000C932h HIGHLOW
    0000C940h HIGHLOW
    0000C953h HIGHLOW
    0000C959h HIGHLOW
    0000C976h HIGHLOW
    0000C97Ch HIGHLOW
    0000C9BCh HIGHLOW
    0000C9C2h HIGHLOW
    0000C9F5h HIGHLOW
    0000CA28h HIGHLOW
    0000CA3Dh HIGHLOW
    0000CA5Fh HIGHLOW
    0000CA6Ch HIGHLOW
    0000CA8Dh HIGHLOW
    0000CB1Fh HIGHLOW
    0000CB33h HIGHLOW
    0000CB43h HIGHLOW
    0000CB85h HIGHLOW
    0000CC49h HIGHLOW
    0000CC52h HIGHLOW
    0000CC91h HIGHLOW
    0000CCC8h HIGHLOW
    0000CD27h HIGHLOW
    0000CD31h HIGHLOW
    0000CD55h HIGHLOW
    0000CE8Fh HIGHLOW
    0000CEA6h HIGHLOW
    0000CEACh HIGHLOW
    0000CEBDh HIGHLOW
    0000CEC3h HIGHLOW
    0000CEFBh HIGHLOW
    0000CF01h HIGHLOW
    0000CF12h HIGHLOW
    0000CF2Eh HIGHLOW
    0000CF34h HIGHLOW
    0000CF43h HIGHLOW
    0000CF49h HIGHLOW
    0000CF7Dh HIGHLOW
    0000CF83h HIGHLOW
    0000CFA0h HIGHLOW
    0000CFA6h HIGHLOW
    0000CFB9h HIGHLOW
    0000CFC0h HIGHLOW
    0000CFD6h HIGHLOW
    0000CFE7h HIGHLOW
    0000CFEDh HIGHLOW
    0000C000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xD000    
SizeOfBlock:                   0x78      
    0000D003h HIGHLOW
    0000D009h HIGHLOW
    0000D158h HIGHLOW
    0000D184h HIGHLOW
    0000D1AEh HIGHLOW
    0000D1EDh HIGHLOW
    0000D245h HIGHLOW
    0000D27Ah HIGHLOW
    0000D29Dh HIGHLOW
    0000D2C9h HIGHLOW
    0000D2F3h HIGHLOW
    0000D322h HIGHLOW
    0000D363h HIGHLOW
    0000D37Dh HIGHLOW
    0000D389h HIGHLOW
    0000D399h HIGHLOW
    0000D3FCh HIGHLOW
    0000D460h HIGHLOW
    0000D469h HIGHLOW
    0000D486h HIGHLOW
    0000D4B9h HIGHLOW
    0000D4E1h HIGHLOW
    0000D51Bh HIGHLOW
    0000D52Eh HIGHLOW
    0000D5CCh HIGHLOW
    0000D6E5h HIGHLOW
    0000D728h HIGHLOW
    0000D752h HIGHLOW
    0000D76Bh HIGHLOW
    0000D7A6h HIGHLOW
    0000D7AFh HIGHLOW
    0000D7C0h HIGHLOW
    0000D7D7h HIGHLOW
    0000D801h HIGHLOW
    0000D88Eh HIGHLOW
    0000D8B5h HIGHLOW
    0000D906h HIGHLOW
    0000D97Fh HIGHLOW
    0000D9E3h HIGHLOW
    0000D9EAh HIGHLOW
    0000DA12h HIGHLOW
    0000DA55h HIGHLOW
    0000DAA4h HIGHLOW
    0000DADAh HIGHLOW
    0000DB12h HIGHLOW
    0000DB2Dh HIGHLOW
    0000DB5Eh HIGHLOW
    0000DC31h HIGHLOW
    0000DD4Ah HIGHLOW
    0000DD76h HIGHLOW
    0000DE01h HIGHLOW
    0000DE8Fh HIGHLOW
    0000DEBBh HIGHLOW
    0000DEC7h HIGHLOW
    0000DF59h HIGHLOW
    0000D000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xE000    
SizeOfBlock:                   0x98      
    0000E061h HIGHLOW
    0000E118h HIGHLOW
    0000E160h HIGHLOW
    0000E1C9h HIGHLOW
    0000E250h HIGHLOW
    0000E2C8h HIGHLOW
    0000E31Ch HIGHLOW
    0000E344h HIGHLOW
    0000E388h HIGHLOW
    0000E38Eh HIGHLOW
    0000E3ABh HIGHLOW
    0000E3B1h HIGHLOW
    0000E3FDh HIGHLOW
    0000E40Bh HIGHLOW
    0000E411h HIGHLOW
    0000E434h HIGHLOW
    0000E43Ah HIGHLOW
    0000E484h HIGHLOW
    0000E4ADh HIGHLOW
    0000E534h HIGHLOW
    0000E542h HIGHLOW
    0000E548h HIGHLOW
    0000E561h HIGHLOW
    0000E567h HIGHLOW
    0000E573h HIGHLOW
    0000E5A3h HIGHLOW
    0000E633h HIGHLOW
    0000E657h HIGHLOW
    0000E672h HIGHLOW
    0000E677h HIGHLOW
    0000E69Eh HIGHLOW
    0000E6A3h HIGHLOW
    0000E7C9h HIGHLOW
    0000E7E0h HIGHLOW
    0000E80Ah HIGHLOW
    0000E83Bh HIGHLOW
    0000E87Ch HIGHLOW
    0000E8ADh HIGHLOW
    0000E8F5h HIGHLOW
    0000E91Dh HIGHLOW
    0000E960h HIGHLOW
    0000E97Bh HIGHLOW
    0000E99Dh HIGHLOW
    0000EA3Dh HIGHLOW
    0000EA6Eh HIGHLOW
    0000EAAFh HIGHLOW
    0000EAE0h HIGHLOW
    0000EB21h HIGHLOW
    0000EB52h HIGHLOW
    0000EB6Ah HIGHLOW
    0000EB85h HIGHLOW
    0000EBC9h HIGHLOW
    0000EC05h HIGHLOW
    0000EC8Eh HIGHLOW
    0000ECCFh HIGHLOW
    0000ECDBh HIGHLOW
    0000ED15h HIGHLOW
    0000EDA6h HIGHLOW
    0000EDC6h HIGHLOW
    0000EE50h HIGHLOW
    0000EE60h HIGHLOW
    0000EEB0h HIGHLOW
    0000EEB5h HIGHLOW
    0000EF09h HIGHLOW
    0000EF19h HIGHLOW
    0000EF54h HIGHLOW
    0000EF85h HIGHLOW
    0000EFADh HIGHLOW
    0000EFD1h HIGHLOW
    0000EFECh HIGHLOW
    0000EFF1h HIGHLOW
    0000E000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0xF000    
SizeOfBlock:                   0xA4      
    0000F01Bh HIGHLOW
    0000F020h HIGHLOW
    0000F0FEh HIGHLOW
    0000F11Eh HIGHLOW
    0000F12Bh HIGHLOW
    0000F1AEh HIGHLOW
    0000F1D8h HIGHLOW
    0000F1E3h HIGHLOW
    0000F237h HIGHLOW
    0000F264h HIGHLOW
    0000F2B9h HIGHLOW
    0000F2D2h HIGHLOW
    0000F2EDh HIGHLOW
    0000F2F4h HIGHLOW
    0000F324h HIGHLOW
    0000F359h HIGHLOW
    0000F422h HIGHLOW
    0000F428h HIGHLOW
    0000F454h HIGHLOW
    0000F511h HIGHLOW
    0000F521h HIGHLOW
    0000F581h HIGHLOW
    0000F588h HIGHLOW
    0000F5A4h HIGHLOW
    0000F5DDh HIGHLOW
    0000F614h HIGHLOW
    0000F661h HIGHLOW
    0000F6E1h HIGHLOW
    0000F74Eh HIGHLOW
    0000F75Ch HIGHLOW
    0000F769h HIGHLOW
    0000F7A8h HIGHLOW
    0000F7C0h HIGHLOW
    0000F7CAh HIGHLOW
    0000F7CFh HIGHLOW
    0000F807h HIGHLOW
    0000F80Eh HIGHLOW
    0000F814h HIGHLOW
    0000F820h HIGHLOW
    0000F82Eh HIGHLOW
    0000F83Ch HIGHLOW
    0000F850h HIGHLOW
    0000F856h HIGHLOW
    0000F870h HIGHLOW
    0000F876h HIGHLOW
    0000F898h HIGHLOW
    0000F89Dh HIGHLOW
    0000F8A9h HIGHLOW
    0000F931h HIGHLOW
    0000F96Bh HIGHLOW
    0000F9AAh HIGHLOW
    0000F9BEh HIGHLOW
    0000F9C6h HIGHLOW
    0000F9CEh HIGHLOW
    0000F9D6h HIGHLOW
    0000F9DEh HIGHLOW
    0000F9E6h HIGHLOW
    0000F9F1h HIGHLOW
    0000F9F7h HIGHLOW
    0000FA86h HIGHLOW
    0000FB13h HIGHLOW
    0000FB1Ch HIGHLOW
    0000FBEEh HIGHLOW
    0000FC3Ah HIGHLOW
    0000FC83h HIGHLOW
    0000FC94h HIGHLOW
    0000FCCEh HIGHLOW
    0000FDDFh HIGHLOW
    0000FDF2h HIGHLOW
    0000FE24h HIGHLOW
    0000FE2Fh HIGHLOW
    0000FEAEh HIGHLOW
    0000FEF0h HIGHLOW
    0000FF0Dh HIGHLOW
    0000FF71h HIGHLOW
    0000FFB6h HIGHLOW
    0000FFEEh HIGHLOW
    0000F000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x10000   
SizeOfBlock:                   0xA0      
    0001002Fh HIGHLOW
    0001004Dh HIGHLOW
    000100A2h HIGHLOW
    000100BCh HIGHLOW
    000100C1h HIGHLOW
    00010172h HIGHLOW
    000101BBh HIGHLOW
    000101CDh HIGHLOW
    0001025Ah HIGHLOW
    00010295h HIGHLOW
    000102BFh HIGHLOW
    000102ECh HIGHLOW
    00010346h HIGHLOW
    00010375h HIGHLOW
    00010380h HIGHLOW
    000103ECh HIGHLOW
    0001041Ah HIGHLOW
    00010470h HIGHLOW
    0001049Ah HIGHLOW
    000104B3h HIGHLOW
    000104BEh HIGHLOW
    00010505h HIGHLOW
    0001050Ch HIGHLOW
    00010516h HIGHLOW
    00010538h HIGHLOW
    00010542h HIGHLOW
    0001055Fh HIGHLOW
    00010566h HIGHLOW
    00010570h HIGHLOW
    00010592h HIGHLOW
    0001059Ch HIGHLOW
    000105B1h HIGHLOW
    000105E4h HIGHLOW
    00010628h HIGHLOW
    0001063Ch HIGHLOW
    00010667h HIGHLOW
    000106FAh HIGHLOW
    00010747h HIGHLOW
    00010750h HIGHLOW
    00010765h HIGHLOW
    00010772h HIGHLOW
    00010779h HIGHLOW
    0001077Eh HIGHLOW
    00010785h HIGHLOW
    0001079Bh HIGHLOW
    000107F6h HIGHLOW
    0001080Fh HIGHLOW
    00010827h HIGHLOW
    0001086Eh HIGHLOW
    0001088Fh HIGHLOW
    0001089Bh HIGHLOW
    000108A7h HIGHLOW
    000108C8h HIGHLOW
    000108F4h HIGHLOW
    0001091Ah HIGHLOW
    0001094Ch HIGHLOW
    00010976h HIGHLOW
    000109D7h HIGHLOW
    00010AB9h HIGHLOW
    00010B10h HIGHLOW
    00010B65h HIGHLOW
    00010BA7h HIGHLOW
    00010BD8h HIGHLOW
    00010C73h HIGHLOW
    00010C78h HIGHLOW
    00010CBAh HIGHLOW
    00010CDFh HIGHLOW
    00010CF4h HIGHLOW
    00010D01h HIGHLOW
    00010D4Dh HIGHLOW
    00010D67h HIGHLOW
    00010DB0h HIGHLOW
    00010E63h HIGHLOW
    00010EA5h HIGHLOW
    00010F56h HIGHLOW
    00010FE2h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x11000   
SizeOfBlock:                   0x80      
    00011062h HIGHLOW
    000110A4h HIGHLOW
    000110B0h HIGHLOW
    000110C1h HIGHLOW
    000110D4h HIGHLOW
    000110DBh HIGHLOW
    000111DAh HIGHLOW
    000113CDh HIGHLOW
    000114B0h HIGHLOW
    000114FCh HIGHLOW
    0001154Ch HIGHLOW
    00011576h HIGHLOW
    000115B1h HIGHLOW
    0001161Fh HIGHLOW
    00011672h HIGHLOW
    00011689h HIGHLOW
    0001168Fh HIGHLOW
    000116A0h HIGHLOW
    000116A6h HIGHLOW
    000116DEh HIGHLOW
    000116E4h HIGHLOW
    00011742h HIGHLOW
    00011789h HIGHLOW
    000117AFh HIGHLOW
    000117D4h HIGHLOW
    0001185Bh HIGHLOW
    0001187Dh HIGHLOW
    000118D8h HIGHLOW
    000118E4h HIGHLOW
    00011906h HIGHLOW
    0001193Dh HIGHLOW
    0001195Eh HIGHLOW
    0001198Eh HIGHLOW
    000119A5h HIGHLOW
    000119EAh HIGHLOW
    00011ADAh HIGHLOW
    00011B17h HIGHLOW
    00011B31h HIGHLOW
    00011B37h HIGHLOW
    00011B48h HIGHLOW
    00011B4Eh HIGHLOW
    00011B84h HIGHLOW
    00011B8Ah HIGHLOW
    00011B9Ch HIGHLOW
    00011BA7h HIGHLOW
    00011BADh HIGHLOW
    00011BC9h HIGHLOW
    00011BCFh HIGHLOW
    00011BECh HIGHLOW
    00011BF2h HIGHLOW
    00011C2Eh HIGHLOW
    00011CEEh HIGHLOW
    00011D36h HIGHLOW
    00011DD8h HIGHLOW
    00011E06h HIGHLOW
    00011E3Ch HIGHLOW
    00011E9Bh HIGHLOW
    00011ECEh HIGHLOW
    00011ED7h HIGHLOW
    00011000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x12000   
SizeOfBlock:                   0x98      
    0001210Dh HIGHLOW
    00012113h HIGHLOW
    00012125h HIGHLOW
    0001213Fh HIGHLOW
    00012147h HIGHLOW
    0001214Fh HIGHLOW
    0001216Dh HIGHLOW
    00012193h HIGHLOW
    000121ACh HIGHLOW
    000122C2h HIGHLOW
    000122E7h HIGHLOW
    000122FDh HIGHLOW
    00012307h HIGHLOW
    0001231Eh HIGHLOW
    00012331h HIGHLOW
    00012357h HIGHLOW
    00012368h HIGHLOW
    000123B1h HIGHLOW
    000123DBh HIGHLOW
    000123F3h HIGHLOW
    00012420h HIGHLOW
    0001246Bh HIGHLOW
    0001248Bh HIGHLOW
    0001249Bh HIGHLOW
    000124B1h HIGHLOW
    000124E9h HIGHLOW
    0001258Ah HIGHLOW
    000125C4h HIGHLOW
    000125CDh HIGHLOW
    000125ECh HIGHLOW
    00012656h HIGHLOW
    000128C3h HIGHLOW
    000128CAh HIGHLOW
    000128D2h HIGHLOW
    000128D8h HIGHLOW
    000128DEh HIGHLOW
    000128EDh HIGHLOW
    000128FAh HIGHLOW
    00012901h HIGHLOW
    00012909h HIGHLOW
    00012915h HIGHLOW
    0001291Bh HIGHLOW
    00012923h HIGHLOW
    00012956h HIGHLOW
    00012963h HIGHLOW
    0001299Eh HIGHLOW
    000129A5h HIGHLOW
    000129B6h HIGHLOW
    000129EFh HIGHLOW
    00012A50h HIGHLOW
    00012A5Bh HIGHLOW
    00012A84h HIGHLOW
    00012A8Fh HIGHLOW
    00012AD0h HIGHLOW
    00012AF1h HIGHLOW
    00012B2Ch HIGHLOW
    00012B40h HIGHLOW
    00012B66h HIGHLOW
    00012B82h HIGHLOW
    00012B99h HIGHLOW
    00012BB4h HIGHLOW
    00012BEBh HIGHLOW
    00012BF8h HIGHLOW
    00012CCDh HIGHLOW
    00012D93h HIGHLOW
    00012DA4h HIGHLOW
    00012E59h HIGHLOW
    00012ECEh HIGHLOW
    00012EFAh HIGHLOW
    00012F83h HIGHLOW
    00012F8Ch HIGHLOW
    00012000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x13000   
SizeOfBlock:                   0xB8      
    00013027h HIGHLOW
    00013058h HIGHLOW
    0001309Ch HIGHLOW
    000130FCh HIGHLOW
    0001316Ah HIGHLOW
    00013199h HIGHLOW
    000131A3h HIGHLOW
    0001337Fh HIGHLOW
    00013393h HIGHLOW
    0001339Fh HIGHLOW
    000133A9h HIGHLOW
    00013400h HIGHLOW
    0001345Bh HIGHLOW
    0001349Ch HIGHLOW
    000134A2h HIGHLOW
    000134C1h HIGHLOW
    000134CFh HIGHLOW
    000134D5h HIGHLOW
    000134EAh HIGHLOW
    000134F0h HIGHLOW
    00013529h HIGHLOW
    00013556h HIGHLOW
    000135AFh HIGHLOW
    000135E6h HIGHLOW
    000135FFh HIGHLOW
    0001360Ah HIGHLOW
    00013643h HIGHLOW
    00013658h HIGHLOW
    0001367Ch HIGHLOW
    00013691h HIGHLOW
    000136A6h HIGHLOW
    000136DAh HIGHLOW
    000136E0h HIGHLOW
    000136EFh HIGHLOW
    000136F6h HIGHLOW
    00013717h HIGHLOW
    00013726h HIGHLOW
    0001372Ch HIGHLOW
    00013745h HIGHLOW
    0001374Bh HIGHLOW
    00013755h HIGHLOW
    0001375Bh HIGHLOW
    000137B7h HIGHLOW
    000137C6h HIGHLOW
    000137CCh HIGHLOW
    00013806h HIGHLOW
    00013814h HIGHLOW
    0001382Eh HIGHLOW
    00013834h HIGHLOW
    00013847h HIGHLOW
    0001384Eh HIGHLOW
    00013864h HIGHLOW
    00013875h HIGHLOW
    0001387Bh HIGHLOW
    00013891h HIGHLOW
    00013897h HIGHLOW
    000138ABh HIGHLOW
    000138B1h HIGHLOW
    000138F0h HIGHLOW
    00013939h HIGHLOW
    0001394Fh HIGHLOW
    00013A04h HIGHLOW
    00013A3Eh HIGHLOW
    00013A53h HIGHLOW
    00013A8Fh HIGHLOW
    00013AD8h HIGHLOW
    00013AE5h HIGHLOW
    00013B06h HIGHLOW
    00013B12h HIGHLOW
    00013B3Bh HIGHLOW
    00013BB1h HIGHLOW
    00013BDDh HIGHLOW
    00013BF2h HIGHLOW
    00013C4Ch HIGHLOW
    00013C6Fh HIGHLOW
    00013C7Eh HIGHLOW
    00013CA0h HIGHLOW
    00013CAFh HIGHLOW
    00013D0Ah HIGHLOW
    00013D48h HIGHLOW
    00013DA4h HIGHLOW
    00013E49h HIGHLOW
    00013EAFh HIGHLOW
    00013EF6h HIGHLOW
    00013F39h HIGHLOW
    00013FA1h HIGHLOW
    00013FC7h HIGHLOW
    00013000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x14000   
SizeOfBlock:                   0x48      
    0001403Dh HIGHLOW
    0001406Dh HIGHLOW
    00014158h HIGHLOW
    000141A3h HIGHLOW
    000143B3h HIGHLOW
    000143C0h HIGHLOW
    000143F1h HIGHLOW
    00014406h HIGHLOW
    00014493h HIGHLOW
    000144C3h HIGHLOW
    0001452Bh HIGHLOW
    0001453Fh HIGHLOW
    000145A9h HIGHLOW
    000145CDh HIGHLOW
    0001465Bh HIGHLOW
    00014675h HIGHLOW
    00014996h HIGHLOW
    000149CCh HIGHLOW
    00014A00h HIGHLOW
    00014A0Bh HIGHLOW
    00014A43h HIGHLOW
    00014A6Fh HIGHLOW
    00014AC3h HIGHLOW
    00014B19h HIGHLOW
    00014B4Ch HIGHLOW
    00014B73h HIGHLOW
    00014BD4h HIGHLOW
    00014C54h HIGHLOW
    00014F25h HIGHLOW
    00014F35h HIGHLOW
    00014FC3h HIGHLOW
    00014FF4h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x15000   
SizeOfBlock:                   0xD8      
    00015029h HIGHLOW
    00015044h HIGHLOW
    0001504Fh HIGHLOW
    00015076h HIGHLOW
    0001507Ch HIGHLOW
    00015099h HIGHLOW
    0001521Fh HIGHLOW
    00015249h HIGHLOW
    00015274h HIGHLOW
    00015280h HIGHLOW
    0001530Bh HIGHLOW
    00015312h HIGHLOW
    00015318h HIGHLOW
    0001531Dh HIGHLOW
    00015328h HIGHLOW
    00015335h HIGHLOW
    0001533Ah HIGHLOW
    0001533Fh HIGHLOW
    00015355h HIGHLOW
    00015361h HIGHLOW
    0001536Eh HIGHLOW
    00015373h HIGHLOW
    00015378h HIGHLOW
    0001538Eh HIGHLOW
    0001539Ah HIGHLOW
    000153A7h HIGHLOW
    000153ACh HIGHLOW
    000153B1h HIGHLOW
    00015404h HIGHLOW
    0001542Ah HIGHLOW
    0001543Ah HIGHLOW
    0001545Bh HIGHLOW
    000154E6h HIGHLOW
    000154EBh HIGHLOW
    0001551Bh HIGHLOW
    00015520h HIGHLOW
    00015550h HIGHLOW
    00015555h HIGHLOW
    0001558Ch HIGHLOW
    00015591h HIGHLOW
    000155C7h HIGHLOW
    000155CCh HIGHLOW
    000155F9h HIGHLOW
    000155FEh HIGHLOW
    0001562Bh HIGHLOW
    00015630h HIGHLOW
    0001565Dh HIGHLOW
    00015662h HIGHLOW
    0001568Fh HIGHLOW
    00015694h HIGHLOW
    000156BDh HIGHLOW
    000156C2h HIGHLOW
    000156F2h HIGHLOW
    000156F7h HIGHLOW
    00015901h HIGHLOW
    00015906h HIGHLOW
    00015941h HIGHLOW
    00015946h HIGHLOW
    00015975h HIGHLOW
    0001599Bh HIGHLOW
    000159A0h HIGHLOW
    00015A0Ah HIGHLOW
    00015A0Fh HIGHLOW
    00015A4Fh HIGHLOW
    00015A54h HIGHLOW
    00015A9Eh HIGHLOW
    00015AA3h HIGHLOW
    00015AF2h HIGHLOW
    00015AF7h HIGHLOW
    00015B3Bh HIGHLOW
    00015B40h HIGHLOW
    00015B6Fh HIGHLOW
    00015B94h HIGHLOW
    00015B99h HIGHLOW
    00015BD0h HIGHLOW
    00015C53h HIGHLOW
    00015C60h HIGHLOW
    00015C68h HIGHLOW
    00015C76h HIGHLOW
    00015C9Bh HIGHLOW
    00015CCEh HIGHLOW
    00015CD4h HIGHLOW
    00015D00h HIGHLOW
    00015D13h HIGHLOW
    00015D4Bh HIGHLOW
    00015D56h HIGHLOW
    00015D76h HIGHLOW
    00015D7Bh HIGHLOW
    00015D80h HIGHLOW
    00015D85h HIGHLOW
    00015D8Bh HIGHLOW
    00015D8Fh HIGHLOW
    00015D95h HIGHLOW
    00015D99h HIGHLOW
    00015DEAh HIGHLOW
    00015DF0h HIGHLOW
    00015E1Bh HIGHLOW
    00015E4Eh HIGHLOW
    00015E9Bh HIGHLOW
    00015EA1h HIGHLOW
    00015ECDh HIGHLOW
    00015EFEh HIGHLOW
    00015F94h HIGHLOW
    00015000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x16000   
SizeOfBlock:                   0xEC      
    00016015h HIGHLOW
    0001606Fh HIGHLOW
    00016080h HIGHLOW
    0001608Ch HIGHLOW
    00016093h HIGHLOW
    0001609Ah HIGHLOW
    000160ABh HIGHLOW
    000160B8h HIGHLOW
    000160FAh HIGHLOW
    00016118h HIGHLOW
    00016148h HIGHLOW
    0001614Fh HIGHLOW
    000161DBh HIGHLOW
    000163F6h HIGHLOW
    00016424h HIGHLOW
    00016563h HIGHLOW
    00016569h HIGHLOW
    00016591h HIGHLOW
    0001659Ch HIGHLOW
    000165A6h HIGHLOW
    000165B1h HIGHLOW
    000165C7h HIGHLOW
    000165D5h HIGHLOW
    000165DAh HIGHLOW
    000165EAh HIGHLOW
    000165F9h HIGHLOW
    0001661Ah HIGHLOW
    00016657h HIGHLOW
    0001667Eh HIGHLOW
    00016691h HIGHLOW
    000166AFh HIGHLOW
    000166B5h HIGHLOW
    000166CBh HIGHLOW
    000166D6h HIGHLOW
    000166DCh HIGHLOW
    000166F2h HIGHLOW
    000166FDh HIGHLOW
    00016703h HIGHLOW
    00016719h HIGHLOW
    00016724h HIGHLOW
    0001672Ah HIGHLOW
    00016740h HIGHLOW
    0001674Bh HIGHLOW
    00016751h HIGHLOW
    00016769h HIGHLOW
    00016777h HIGHLOW
    0001678Fh HIGHLOW
    000167AFh HIGHLOW
    000167B5h HIGHLOW
    000167DFh HIGHLOW
    000167EDh HIGHLOW
    000167F7h HIGHLOW
    0001681Bh HIGHLOW
    00016847h HIGHLOW
    00016865h HIGHLOW
    0001686Bh HIGHLOW
    00016871h HIGHLOW
    00016891h HIGHLOW
    0001689Eh HIGHLOW
    000168BFh HIGHLOW
    000168CCh HIGHLOW
    000168D0h HIGHLOW
    000168E0h HIGHLOW
    000168E6h HIGHLOW
    000168ECh HIGHLOW
    000168F7h HIGHLOW
    000168FDh HIGHLOW
    00016903h HIGHLOW
    00016913h HIGHLOW
    0001691Eh HIGHLOW
    00016934h HIGHLOW
    0001693Dh HIGHLOW
    00016948h HIGHLOW
    00016957h HIGHLOW
    0001696Bh HIGHLOW
    00016972h HIGHLOW
    0001698Fh HIGHLOW
    000169A8h HIGHLOW
    000169AEh HIGHLOW
    000169BDh HIGHLOW
    000169D3h HIGHLOW
    000169E3h HIGHLOW
    000169EAh HIGHLOW
    000169F5h HIGHLOW
    000169F9h HIGHLOW
    00016A07h HIGHLOW
    00016A0Eh HIGHLOW
    00016A13h HIGHLOW
    00016A19h HIGHLOW
    00016A22h HIGHLOW
    00016A9Fh HIGHLOW
    00016AA8h HIGHLOW
    00016B29h HIGHLOW
    00016B4Fh HIGHLOW
    00016B94h HIGHLOW
    00016BA4h HIGHLOW
    00016BBBh HIGHLOW
    00016BC8h HIGHLOW
    00016BE5h HIGHLOW
    00016C39h HIGHLOW
    00016C6Fh HIGHLOW
    00016C97h HIGHLOW
    00016CC3h HIGHLOW
    00016CE4h HIGHLOW
    00016D14h HIGHLOW
    00016D50h HIGHLOW
    00016D76h HIGHLOW
    00016DA0h HIGHLOW
    00016E13h HIGHLOW
    00016E74h HIGHLOW
    00016E88h HIGHLOW
    00016FC0h HIGHLOW
    00016FC5h HIGHLOW
    00016FFCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x17000   
SizeOfBlock:                   0x80      
    00017001h HIGHLOW
    00017033h HIGHLOW
    00017038h HIGHLOW
    0001706Fh HIGHLOW
    00017074h HIGHLOW
    000170B1h HIGHLOW
    000170B6h HIGHLOW
    00017132h HIGHLOW
    00017171h HIGHLOW
    00017196h HIGHLOW
    000171ABh HIGHLOW
    000171E2h HIGHLOW
    000171F6h HIGHLOW
    00017210h HIGHLOW
    00017230h HIGHLOW
    0001724Ch HIGHLOW
    000172A6h HIGHLOW
    000172BCh HIGHLOW
    000172C3h HIGHLOW
    000172D7h HIGHLOW
    000172EFh HIGHLOW
    0001734Fh HIGHLOW
    00017372h HIGHLOW
    000173D2h HIGHLOW
    000174E2h HIGHLOW
    0001755Dh HIGHLOW
    00017565h HIGHLOW
    0001758Dh HIGHLOW
    000175B3h HIGHLOW
    00017613h HIGHLOW
    0001768Eh HIGHLOW
    000176A8h HIGHLOW
    000176C1h HIGHLOW
    00017715h HIGHLOW
    0001772Ah HIGHLOW
    00017773h HIGHLOW
    000177B9h HIGHLOW
    000177C6h HIGHLOW
    00017803h HIGHLOW
    0001782Bh HIGHLOW
    00017887h HIGHLOW
    000178B9h HIGHLOW
    0001799Fh HIGHLOW
    000179E3h HIGHLOW
    00017A27h HIGHLOW
    00017AB9h HIGHLOW
    00017B6Eh HIGHLOW
    00017BD2h HIGHLOW
    00017C96h HIGHLOW
    00017CEBh HIGHLOW
    00017CFAh HIGHLOW
    00017D08h HIGHLOW
    00017E28h HIGHLOW
    00017E3Eh HIGHLOW
    00017E9Ah HIGHLOW
    00017EF4h HIGHLOW
    00017F10h HIGHLOW
    00017F40h HIGHLOW
    00017F54h HIGHLOW
    00017000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x18000   
SizeOfBlock:                   0x6C      
    00018171h HIGHLOW
    00018199h HIGHLOW
    000181F0h HIGHLOW
    000181FDh HIGHLOW
    0001821Bh HIGHLOW
    00018464h HIGHLOW
    000184B1h HIGHLOW
    000184C3h HIGHLOW
    000184D0h HIGHLOW
    0001854Dh HIGHLOW
    00018597h HIGHLOW
    000185ADh HIGHLOW
    000186D6h HIGHLOW
    0001870Fh HIGHLOW
    0001872Fh HIGHLOW
    00018755h HIGHLOW
    000187BDh HIGHLOW
    000187D0h HIGHLOW
    000187D5h HIGHLOW
    00018880h HIGHLOW
    000188A8h HIGHLOW
    00018947h HIGHLOW
    000189FCh HIGHLOW
    00018A14h HIGHLOW
    00018A25h HIGHLOW
    00018A52h HIGHLOW
    00018A5Fh HIGHLOW
    00018A6Eh HIGHLOW
    00018AA2h HIGHLOW
    00018AA8h HIGHLOW
    00018B02h HIGHLOW
    00018B85h HIGHLOW
    00018BEDh HIGHLOW
    00018C43h HIGHLOW
    00018C60h HIGHLOW
    00018CD2h HIGHLOW
    00018D1Dh HIGHLOW
    00018DB8h HIGHLOW
    00018E5Eh HIGHLOW
    00018E73h HIGHLOW
    00018E97h HIGHLOW
    00018EADh HIGHLOW
    00018ED6h HIGHLOW
    00018EEFh HIGHLOW
    00018EF6h HIGHLOW
    00018F13h HIGHLOW
    00018F2Ah HIGHLOW
    00018FC8h HIGHLOW
    00018FFAh HIGHLOW
    00018000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x19000   
SizeOfBlock:                   0x90      
    00019069h HIGHLOW
    00019083h HIGHLOW
    00019096h HIGHLOW
    000190ACh HIGHLOW
    00019163h HIGHLOW
    000191D3h HIGHLOW
    0001924Fh HIGHLOW
    000192D9h HIGHLOW
    00019337h HIGHLOW
    000193CEh HIGHLOW
    0001944Ah HIGHLOW
    0001950Ah HIGHLOW
    00019513h HIGHLOW
    00019546h HIGHLOW
    00019580h HIGHLOW
    00019594h HIGHLOW
    000195F2h HIGHLOW
    00019635h HIGHLOW
    0001964Ah HIGHLOW
    00019698h HIGHLOW
    000196B9h HIGHLOW
    000196C1h HIGHLOW
    00019726h HIGHLOW
    00019741h HIGHLOW
    00019762h HIGHLOW
    00019768h HIGHLOW
    00019773h HIGHLOW
    0001977Dh HIGHLOW
    00019796h HIGHLOW
    0001979Ch HIGHLOW
    000197DAh HIGHLOW
    00019827h HIGHLOW
    00019850h HIGHLOW
    00019870h HIGHLOW
    00019884h HIGHLOW
    000198BAh HIGHLOW
    000198C9h HIGHLOW
    000198CFh HIGHLOW
    0001990Eh HIGHLOW
    00019938h HIGHLOW
    00019948h HIGHLOW
    00019956h HIGHLOW
    00019A1Dh HIGHLOW
    00019A48h HIGHLOW
    00019A66h HIGHLOW
    00019A6Ch HIGHLOW
    00019AB9h HIGHLOW
    00019AC8h HIGHLOW
    00019C06h HIGHLOW
    00019CB1h HIGHLOW
    00019CBEh HIGHLOW
    00019CCAh HIGHLOW
    00019CE6h HIGHLOW
    00019D44h HIGHLOW
    00019D72h HIGHLOW
    00019D8Fh HIGHLOW
    00019DF7h HIGHLOW
    00019E2Bh HIGHLOW
    00019E61h HIGHLOW
    00019EC1h HIGHLOW
    00019EE7h HIGHLOW
    00019EF2h HIGHLOW
    00019F0Ch HIGHLOW
    00019F7Bh HIGHLOW
    00019FB8h HIGHLOW
    00019FBEh HIGHLOW
    00019FC4h HIGHLOW
    00019FCBh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1A000   
SizeOfBlock:                   0xF0      
    0001A05Eh HIGHLOW
    0001A0B2h HIGHLOW
    0001A0BBh HIGHLOW
    0001A0F6h HIGHLOW
    0001A11Ch HIGHLOW
    0001A129h HIGHLOW
    0001A133h HIGHLOW
    0001A140h HIGHLOW
    0001A170h HIGHLOW
    0001A17Bh HIGHLOW
    0001A188h HIGHLOW
    0001A18Fh HIGHLOW
    0001A19Ch HIGHLOW
    0001A1A2h HIGHLOW
    0001A1A8h HIGHLOW
    0001A1AEh HIGHLOW
    0001A1D9h HIGHLOW
    0001A207h HIGHLOW
    0001A20Ch HIGHLOW
    0001A211h HIGHLOW
    0001A216h HIGHLOW
    0001A21Bh HIGHLOW
    0001A22Ah HIGHLOW
    0001A25Dh HIGHLOW
    0001A265h HIGHLOW
    0001A28Ah HIGHLOW
    0001A28Fh HIGHLOW
    0001A294h HIGHLOW
    0001A299h HIGHLOW
    0001A2A3h HIGHLOW
    0001A2B6h HIGHLOW
    0001A2BBh HIGHLOW
    0001A2C5h HIGHLOW
    0001A2CAh HIGHLOW
    0001A2D0h HIGHLOW
    0001A2DBh HIGHLOW
    0001A2E1h HIGHLOW
    0001A2E8h HIGHLOW
    0001A2F6h HIGHLOW
    0001A309h HIGHLOW
    0001A326h HIGHLOW
    0001A346h HIGHLOW
    0001A352h HIGHLOW
    0001A358h HIGHLOW
    0001A35Eh HIGHLOW
    0001A369h HIGHLOW
    0001A374h HIGHLOW
    0001A37Fh HIGHLOW
    0001A398h HIGHLOW
    0001A3A0h HIGHLOW
    0001A3A9h HIGHLOW
    0001A3B2h HIGHLOW
    0001A3BAh HIGHLOW
    0001A3D1h HIGHLOW
    0001A3D9h HIGHLOW
    0001A3DEh HIGHLOW
    0001A3E3h HIGHLOW
    0001A3E9h HIGHLOW
    0001A3F7h HIGHLOW
    0001A402h HIGHLOW
    0001A40Ch HIGHLOW
    0001A425h HIGHLOW
    0001A45Ah HIGHLOW
    0001A460h HIGHLOW
    0001A472h HIGHLOW
    0001A47Ch HIGHLOW
    0001A486h HIGHLOW
    0001A5B1h HIGHLOW
    0001A5DCh HIGHLOW
    0001A5F9h HIGHLOW
    0001A61Bh HIGHLOW
    0001A65Fh HIGHLOW
    0001A691h HIGHLOW
    0001A70Bh HIGHLOW
    0001A7C5h HIGHLOW
    0001A817h HIGHLOW
    0001A824h HIGHLOW
    0001A888h HIGHLOW
    0001A897h HIGHLOW
    0001A8DAh HIGHLOW
    0001A917h HIGHLOW
    0001A925h HIGHLOW
    0001A9D5h HIGHLOW
    0001AA61h HIGHLOW
    0001AA89h HIGHLOW
    0001AB0Dh HIGHLOW
    0001AB3Bh HIGHLOW
    0001AB5Ah HIGHLOW
    0001AB77h HIGHLOW
    0001ABB7h HIGHLOW
    0001ABF7h HIGHLOW
    0001AC2Eh HIGHLOW
    0001AC6Eh HIGHLOW
    0001AC7Eh HIGHLOW
    0001ACBFh HIGHLOW
    0001ACC6h HIGHLOW
    0001ACE5h HIGHLOW
    0001AD04h HIGHLOW
    0001AD23h HIGHLOW
    0001AD45h HIGHLOW
    0001AD51h HIGHLOW
    0001AD71h HIGHLOW
    0001AD81h HIGHLOW
    0001AD86h HIGHLOW
    0001AD90h HIGHLOW
    0001ADA1h HIGHLOW
    0001ADD7h HIGHLOW
    0001AE3Ah HIGHLOW
    0001AE46h HIGHLOW
    0001AE71h HIGHLOW
    0001AEC6h HIGHLOW
    0001AEF8h HIGHLOW
    0001AF86h HIGHLOW
    0001AFC3h HIGHLOW
    0001AFECh HIGHLOW
    0001A000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1B000   
SizeOfBlock:                   0x11C     
    0001B01Dh HIGHLOW
    0001B0FDh HIGHLOW
    0001B1E7h HIGHLOW
    0001B25Fh HIGHLOW
    0001B267h HIGHLOW
    0001B26Dh HIGHLOW
    0001B28Ah HIGHLOW
    0001B294h HIGHLOW
    0001B29Ah HIGHLOW
    0001B303h HIGHLOW
    0001B331h HIGHLOW
    0001B339h HIGHLOW
    0001B33Fh HIGHLOW
    0001B35Dh HIGHLOW
    0001B368h HIGHLOW
    0001B36Eh HIGHLOW
    0001B38Fh HIGHLOW
    0001B3D8h HIGHLOW
    0001B3DEh HIGHLOW
    0001B405h HIGHLOW
    0001B446h HIGHLOW
    0001B44Fh HIGHLOW
    0001B46Ah HIGHLOW
    0001B487h HIGHLOW
    0001B4ABh HIGHLOW
    0001B4D7h HIGHLOW
    0001B508h HIGHLOW
    0001B51Ah HIGHLOW
    0001B54Ch HIGHLOW
    0001B55Ah HIGHLOW
    0001B57Bh HIGHLOW
    0001B5A7h HIGHLOW
    0001B5FFh HIGHLOW
    0001B61Ch HIGHLOW
    0001B62Eh HIGHLOW
    0001B63Dh HIGHLOW
    0001B646h HIGHLOW
    0001B651h HIGHLOW
    0001B6B5h HIGHLOW
    0001B6F8h HIGHLOW
    0001B716h HIGHLOW
    0001B738h HIGHLOW
    0001B77Bh HIGHLOW
    0001B7B1h HIGHLOW
    0001B809h HIGHLOW
    0001B81Fh HIGHLOW
    0001B829h HIGHLOW
    0001B8DDh HIGHLOW
    0001B947h HIGHLOW
    0001B959h HIGHLOW
    0001B96Ch HIGHLOW
    0001B97Fh HIGHLOW
    0001B999h HIGHLOW
    0001B9AFh HIGHLOW
    0001B9C5h HIGHLOW
    0001B9DBh HIGHLOW
    0001B9F1h HIGHLOW
    0001B9FDh HIGHLOW
    0001BA0Fh HIGHLOW
    0001BA19h HIGHLOW
    0001BA3Fh HIGHLOW
    0001BA4Eh HIGHLOW
    0001BA60h HIGHLOW
    0001BA73h HIGHLOW
    0001BA8Ah HIGHLOW
    0001BA94h HIGHLOW
    0001BABEh HIGHLOW
    0001BAC9h HIGHLOW
    0001BADAh HIGHLOW
    0001BAECh HIGHLOW
    0001BAFBh HIGHLOW
    0001BB0Fh HIGHLOW
    0001BB14h HIGHLOW
    0001BB1Ah HIGHLOW
    0001BB1Eh HIGHLOW
    0001BB24h HIGHLOW
    0001BB28h HIGHLOW
    0001BB30h HIGHLOW
    0001BB91h HIGHLOW
    0001BB97h HIGHLOW
    0001BBA1h HIGHLOW
    0001BBA8h HIGHLOW
    0001BBAFh HIGHLOW
    0001BBC4h HIGHLOW
    0001BBCAh HIGHLOW
    0001BBD0h HIGHLOW
    0001BBD6h HIGHLOW
    0001BBEDh HIGHLOW
    0001BBF4h HIGHLOW
    0001BC17h HIGHLOW
    0001BC1Ch HIGHLOW
    0001BC29h HIGHLOW
    0001BC3Eh HIGHLOW
    0001BC44h HIGHLOW
    0001BC56h HIGHLOW
    0001BC5Dh HIGHLOW
    0001BC6Ah HIGHLOW
    0001BC76h HIGHLOW
    0001BC96h HIGHLOW
    0001BC9Fh HIGHLOW
    0001BCB8h HIGHLOW
    0001BCC5h HIGHLOW
    0001BCE8h HIGHLOW
    0001BD13h HIGHLOW
    0001BD25h HIGHLOW
    0001BD2Bh HIGHLOW
    0001BD3Bh HIGHLOW
    0001BD51h HIGHLOW
    0001BD5Bh HIGHLOW
    0001BD87h HIGHLOW
    0001BD96h HIGHLOW
    0001BDB4h HIGHLOW
    0001BDC3h HIGHLOW
    0001BDE2h HIGHLOW
    0001BDF1h HIGHLOW
    0001BE12h HIGHLOW
    0001BE21h HIGHLOW
    0001BE3Fh HIGHLOW
    0001BE4Eh HIGHLOW
    0001BE67h HIGHLOW
    0001BE72h HIGHLOW
    0001BEBAh HIGHLOW
    0001BED3h HIGHLOW
    0001BEDEh HIGHLOW
    0001BF1Ch HIGHLOW
    0001BF2Dh HIGHLOW
    0001BF4Ah HIGHLOW
    0001BF5Bh HIGHLOW
    0001BF78h HIGHLOW
    0001BF8Bh HIGHLOW
    0001BF91h HIGHLOW
    0001BFA2h HIGHLOW
    0001BFAEh HIGHLOW
    0001BFB4h HIGHLOW
    0001BFBDh HIGHLOW
    0001BFC5h HIGHLOW
    0001BFCBh HIGHLOW
    0001B000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1C000   
SizeOfBlock:                   0xD4      
    0001C029h HIGHLOW
    0001C03Eh HIGHLOW
    0001C050h HIGHLOW
    0001C06Ah HIGHLOW
    0001C087h HIGHLOW
    0001C09Bh HIGHLOW
    0001C0A9h HIGHLOW
    0001C0B9h HIGHLOW
    0001C0C1h HIGHLOW
    0001C0C9h HIGHLOW
    0001C0CEh HIGHLOW
    0001C0D5h HIGHLOW
    0001C0DAh HIGHLOW
    0001C0E6h HIGHLOW
    0001C0EEh HIGHLOW
    0001C0F4h HIGHLOW
    0001C11Ch HIGHLOW
    0001C144h HIGHLOW
    0001C157h HIGHLOW
    0001C17Ah HIGHLOW
    0001C181h HIGHLOW
    0001C1A1h HIGHLOW
    0001C1A9h HIGHLOW
    0001C20Dh HIGHLOW
    0001C257h HIGHLOW
    0001C26Ch HIGHLOW
    0001C28Fh HIGHLOW
    0001C2E6h HIGHLOW
    0001C2F3h HIGHLOW
    0001C330h HIGHLOW
    0001C337h HIGHLOW
    0001C368h HIGHLOW
    0001C3AEh HIGHLOW
    0001C4BDh HIGHLOW
    0001C4EDh HIGHLOW
    0001C4F6h HIGHLOW
    0001C4FCh HIGHLOW
    0001C503h HIGHLOW
    0001C52Ah HIGHLOW
    0001C547h HIGHLOW
    0001C54Fh HIGHLOW
    0001C554h HIGHLOW
    0001C596h HIGHLOW
    0001C5B0h HIGHLOW
    0001C5B7h HIGHLOW
    0001C5D4h HIGHLOW
    0001C5E5h HIGHLOW
    0001C617h HIGHLOW
    0001C634h HIGHLOW
    0001C645h HIGHLOW
    0001C6E3h HIGHLOW
    0001C6F3h HIGHLOW
    0001C714h HIGHLOW
    0001C72Eh HIGHLOW
    0001C773h HIGHLOW
    0001C79Bh HIGHLOW
    0001C7B0h HIGHLOW
    0001C7F6h HIGHLOW
    0001C83Ah HIGHLOW
    0001C847h HIGHLOW
    0001C8C9h HIGHLOW
    0001C91Ah HIGHLOW
    0001C939h HIGHLOW
    0001C95Fh HIGHLOW
    0001C966h HIGHLOW
    0001C96Bh HIGHLOW
    0001C978h HIGHLOW
    0001C982h HIGHLOW
    0001C9A8h HIGHLOW
    0001C9C2h HIGHLOW
    0001C9CFh HIGHLOW
    0001C9DCh HIGHLOW
    0001C9ECh HIGHLOW
    0001C9F2h HIGHLOW
    0001CA47h HIGHLOW
    0001CA8Ch HIGHLOW
    0001CAA9h HIGHLOW
    0001CAAEh HIGHLOW
    0001CAE4h HIGHLOW
    0001CAEDh HIGHLOW
    0001CB0Ch HIGHLOW
    0001CB1Dh HIGHLOW
    0001CB2Ch HIGHLOW
    0001CC1Bh HIGHLOW
    0001CCAEh HIGHLOW
    0001CCB3h HIGHLOW
    0001CCD7h HIGHLOW
    0001CCDDh HIGHLOW
    0001CCE3h HIGHLOW
    0001CD0Dh HIGHLOW
    0001CD1Ah HIGHLOW
    0001CD3Ah HIGHLOW
    0001CD72h HIGHLOW
    0001CDC4h HIGHLOW
    0001CE2Bh HIGHLOW
    0001CE37h HIGHLOW
    0001CE51h HIGHLOW
    0001CE58h HIGHLOW
    0001CE95h HIGHLOW
    0001CF0Ch HIGHLOW
    0001CF12h HIGHLOW
    0001CF28h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1D000   
SizeOfBlock:                   0x68      
    0001D074h HIGHLOW
    0001D07Eh HIGHLOW
    0001D084h HIGHLOW
    0001D08Fh HIGHLOW
    0001D0A3h HIGHLOW
    0001D0C3h HIGHLOW
    0001D0D1h HIGHLOW
    0001D117h HIGHLOW
    0001D139h HIGHLOW
    0001D159h HIGHLOW
    0001D2D8h HIGHLOW
    0001D2DDh HIGHLOW
    0001D2E3h HIGHLOW
    0001D2FFh HIGHLOW
    0001D37Ah HIGHLOW
    0001D3A8h HIGHLOW
    0001D3DBh HIGHLOW
    0001D3E5h HIGHLOW
    0001D413h HIGHLOW
    0001D41Fh HIGHLOW
    0001D441h HIGHLOW
    0001D4B2h HIGHLOW
    0001D4BEh HIGHLOW
    0001D4F9h HIGHLOW
    0001D53Eh HIGHLOW
    0001D612h HIGHLOW
    0001D63Ah HIGHLOW
    0001D643h HIGHLOW
    0001D6DBh HIGHLOW
    0001D716h HIGHLOW
    0001D7CAh HIGHLOW
    0001D809h HIGHLOW
    0001D968h HIGHLOW
    0001D9F8h HIGHLOW
    0001DBA3h HIGHLOW
    0001DBC7h HIGHLOW
    0001DCBCh HIGHLOW
    0001DCC5h HIGHLOW
    0001DCD3h HIGHLOW
    0001DD2Ah HIGHLOW
    0001DD33h HIGHLOW
    0001DD43h HIGHLOW
    0001DE11h HIGHLOW
    0001DE47h HIGHLOW
    0001DE53h HIGHLOW
    0001DF37h HIGHLOW
    0001DFEAh HIGHLOW
    0001D000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1E000   
SizeOfBlock:                   0x8C      
    0001E0CBh HIGHLOW
    0001E111h HIGHLOW
    0001E192h HIGHLOW
    0001E1E5h HIGHLOW
    0001E238h HIGHLOW
    0001E2C9h HIGHLOW
    0001E358h HIGHLOW
    0001E360h HIGHLOW
    0001E371h HIGHLOW
    0001E382h HIGHLOW
    0001E38Ah HIGHLOW
    0001E3B7h HIGHLOW
    0001E3BFh HIGHLOW
    0001E3DBh HIGHLOW
    0001E3E3h HIGHLOW
    0001E4B8h HIGHLOW
    0001E4DCh HIGHLOW
    0001E691h HIGHLOW
    0001E799h HIGHLOW
    0001E7AEh HIGHLOW
    0001E7C8h HIGHLOW
    0001E7E3h HIGHLOW
    0001E828h HIGHLOW
    0001E8BAh HIGHLOW
    0001E8E0h HIGHLOW
    0001E8EEh HIGHLOW
    0001E8F9h HIGHLOW
    0001E909h HIGHLOW
    0001E91Bh HIGHLOW
    0001E9B3h HIGHLOW
    0001E9B9h HIGHLOW
    0001E9BEh HIGHLOW
    0001E9EEh HIGHLOW
    0001E9F4h HIGHLOW
    0001EA08h HIGHLOW
    0001EA3Ch HIGHLOW
    0001EA58h HIGHLOW
    0001EA8Ch HIGHLOW
    0001EAA4h HIGHLOW
    0001EACDh HIGHLOW
    0001EADEh HIGHLOW
    0001EB12h HIGHLOW
    0001EB18h HIGHLOW
    0001EB1Eh HIGHLOW
    0001EB49h HIGHLOW
    0001EB62h HIGHLOW
    0001EB91h HIGHLOW
    0001EBA5h HIGHLOW
    0001EBABh HIGHLOW
    0001EBBAh HIGHLOW
    0001EBC7h HIGHLOW
    0001EBCDh HIGHLOW
    0001EC09h HIGHLOW
    0001ED22h HIGHLOW
    0001ED93h HIGHLOW
    0001EE51h HIGHLOW
    0001EE87h HIGHLOW
    0001EEC4h HIGHLOW
    0001EEE3h HIGHLOW
    0001EEF1h HIGHLOW
    0001EF04h HIGHLOW
    0001EF50h HIGHLOW
    0001EF74h HIGHLOW
    0001EFF7h HIGHLOW
    0001EFFCh HIGHLOW
    0001E000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x1F000   
SizeOfBlock:                   0x6C      
    0001F031h HIGHLOW
    0001F05Eh HIGHLOW
    0001F119h HIGHLOW
    0001F159h HIGHLOW
    0001F166h HIGHLOW
    0001F1A1h HIGHLOW
    0001F2C7h HIGHLOW
    0001F2F3h HIGHLOW
    0001F36Bh HIGHLOW
    0001F38Bh HIGHLOW
    0001F3C7h HIGHLOW
    0001F3E0h HIGHLOW
    0001F416h HIGHLOW
    0001F429h HIGHLOW
    0001F463h HIGHLOW
    0001F477h HIGHLOW
    0001F605h HIGHLOW
    0001F70Eh HIGHLOW
    0001F7B3h HIGHLOW
    0001F7B8h HIGHLOW
    0001F813h HIGHLOW
    0001F854h HIGHLOW
    0001F86Fh HIGHLOW
    0001F8EDh HIGHLOW
    0001F8F2h HIGHLOW
    0001FA21h HIGHLOW
    0001FA37h HIGHLOW
    0001FB35h HIGHLOW
    0001FBCFh HIGHLOW
    0001FC81h HIGHLOW
    0001FD48h HIGHLOW
    0001FD58h HIGHLOW
    0001FDC9h HIGHLOW
    0001FDFAh HIGHLOW
    0001FE1Eh HIGHLOW
    0001FE40h HIGHLOW
    0001FE59h HIGHLOW
    0001FE78h HIGHLOW
    0001FE8Fh HIGHLOW
    0001FE9Eh HIGHLOW
    0001FEA4h HIGHLOW
    0001FEAAh HIGHLOW
    0001FEC7h HIGHLOW
    0001FED8h HIGHLOW
    0001FEECh HIGHLOW
    0001FEFDh HIGHLOW
    0001FF11h HIGHLOW
    0001FF26h HIGHLOW
    0001FF8Ch HIGHLOW
    0001FFC1h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x20000   
SizeOfBlock:                   0xB0      
    000200ABh HIGHLOW
    000200FFh HIGHLOW
    00020127h HIGHLOW
    00020161h HIGHLOW
    00020179h HIGHLOW
    000201D3h HIGHLOW
    000201E8h HIGHLOW
    000201F3h HIGHLOW
    00020204h HIGHLOW
    0002021Ah HIGHLOW
    00020238h HIGHLOW
    00020249h HIGHLOW
    00020290h HIGHLOW
    000202B9h HIGHLOW
    000202DAh HIGHLOW
    000202E3h HIGHLOW
    0002030Ah HIGHLOW
    00020335h HIGHLOW
    00020344h HIGHLOW
    00020395h HIGHLOW
    0002039Eh HIGHLOW
    000203B9h HIGHLOW
    000203CAh HIGHLOW
    00020421h HIGHLOW
    00020431h HIGHLOW
    0002044Bh HIGHLOW
    00020458h HIGHLOW
    00020479h HIGHLOW
    0002048Dh HIGHLOW
    0002049Eh HIGHLOW
    000204D3h HIGHLOW
    000204E1h HIGHLOW
    00020530h HIGHLOW
    0002057Dh HIGHLOW
    00020596h HIGHLOW
    000205E2h HIGHLOW
    000205ECh HIGHLOW
    0002060Eh HIGHLOW
    00020614h HIGHLOW
    00020678h HIGHLOW
    00020695h HIGHLOW
    0002069Eh HIGHLOW
    000206ACh HIGHLOW
    000206DAh HIGHLOW
    000206EFh HIGHLOW
    0002072Bh HIGHLOW
    0002076Fh HIGHLOW
    0002077Ch HIGHLOW
    000207B0h HIGHLOW
    000207E0h HIGHLOW
    00020827h HIGHLOW
    00020843h HIGHLOW
    0002084Ch HIGHLOW
    00020874h HIGHLOW
    00020924h HIGHLOW
    00020952h HIGHLOW
    0002098Eh HIGHLOW
    00020A07h HIGHLOW
    00020A3Fh HIGHLOW
    00020A85h HIGHLOW
    00020A91h HIGHLOW
    00020AC0h HIGHLOW
    00020B2Dh HIGHLOW
    00020B4Ch HIGHLOW
    00020B5Ch HIGHLOW
    00020B68h HIGHLOW
    00020B8Dh HIGHLOW
    00020BB4h HIGHLOW
    00020BEBh HIGHLOW
    00020C38h HIGHLOW
    00020CB8h HIGHLOW
    00020D4Ch HIGHLOW
    00020D50h HIGHLOW
    00020ED8h HIGHLOW
    00020F00h HIGHLOW
    00020F78h HIGHLOW
    00020F84h HIGHLOW
    00020F88h HIGHLOW
    00020F90h HIGHLOW
    00020FE0h HIGHLOW
    00020FE8h HIGHLOW
    00020FECh HIGHLOW
    00020FF4h HIGHLOW
    00020FF8h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x21000   
SizeOfBlock:                   0x18C     
    00021008h HIGHLOW
    00021016h HIGHLOW
    0002101Ah HIGHLOW
    0002101Eh HIGHLOW
    00021022h HIGHLOW
    00021026h HIGHLOW
    0002102Ah HIGHLOW
    0002102Eh HIGHLOW
    00021032h HIGHLOW
    00021038h HIGHLOW
    0002103Ch HIGHLOW
    00021040h HIGHLOW
    00021044h HIGHLOW
    00021328h HIGHLOW
    00021338h HIGHLOW
    00021348h HIGHLOW
    00021350h HIGHLOW
    00021354h HIGHLOW
    00021360h HIGHLOW
    0002136Ch HIGHLOW
    00021370h HIGHLOW
    00021380h HIGHLOW
    00021390h HIGHLOW
    000214B0h HIGHLOW
    000214BCh HIGHLOW
    000214C0h HIGHLOW
    000214CCh HIGHLOW
    000214D0h HIGHLOW
    000214DCh HIGHLOW
    000214E0h HIGHLOW
    00021550h HIGHLOW
    0002155Ch HIGHLOW
    00021560h HIGHLOW
    0002156Ch HIGHLOW
    00021570h HIGHLOW
    0002157Ch HIGHLOW
    00021580h HIGHLOW
    0002158Ch HIGHLOW
    00021594h HIGHLOW
    00021598h HIGHLOW
    000215A4h HIGHLOW
    000215B0h HIGHLOW
    000215D4h HIGHLOW
    000215D8h HIGHLOW
    000215E4h HIGHLOW
    000215E8h HIGHLOW
    000215F4h HIGHLOW
    000215F8h HIGHLOW
    000216ACh HIGHLOW
    000216B0h HIGHLOW
    000216B4h HIGHLOW
    000216B8h HIGHLOW
    000216BCh HIGHLOW
    000216C0h HIGHLOW
    000216C4h HIGHLOW
    000216C8h HIGHLOW
    000216CCh HIGHLOW
    000216D0h HIGHLOW
    000216D4h HIGHLOW
    000216D8h HIGHLOW
    000216DCh HIGHLOW
    000216E0h HIGHLOW
    000216E4h HIGHLOW
    000216E8h HIGHLOW
    000216ECh HIGHLOW
    000216F0h HIGHLOW
    000216F4h HIGHLOW
    000216F8h HIGHLOW
    000216FCh HIGHLOW
    00021700h HIGHLOW
    00021704h HIGHLOW
    00021708h HIGHLOW
    0002170Ch HIGHLOW
    00021710h HIGHLOW
    00021714h HIGHLOW
    00021718h HIGHLOW
    0002171Ch HIGHLOW
    00021720h HIGHLOW
    00021724h HIGHLOW
    00021728h HIGHLOW
    0002172Ch HIGHLOW
    00021730h HIGHLOW
    00021734h HIGHLOW
    00021738h HIGHLOW
    0002173Ch HIGHLOW
    00021740h HIGHLOW
    00021744h HIGHLOW
    00021748h HIGHLOW
    0002174Ch HIGHLOW
    00021750h HIGHLOW
    00021754h HIGHLOW
    00021758h HIGHLOW
    0002175Ch HIGHLOW
    00021760h HIGHLOW
    00021764h HIGHLOW
    00021784h HIGHLOW
    00021788h HIGHLOW
    000217E4h HIGHLOW
    000217E8h HIGHLOW
    000217F4h HIGHLOW
    000217F8h HIGHLOW
    00021804h HIGHLOW
    00021808h HIGHLOW
    00021818h HIGHLOW
    00021824h HIGHLOW
    00021828h HIGHLOW
    00021834h HIGHLOW
    00021838h HIGHLOW
    00021858h HIGHLOW
    00021868h HIGHLOW
    00021874h HIGHLOW
    00021878h HIGHLOW
    00021884h HIGHLOW
    00021888h HIGHLOW
    00021894h HIGHLOW
    00021898h HIGHLOW
    000218A4h HIGHLOW
    000218A8h HIGHLOW
    000218B4h HIGHLOW
    000218B8h HIGHLOW
    000218C4h HIGHLOW
    000218C8h HIGHLOW
    000218D4h HIGHLOW
    000218D8h HIGHLOW
    000218E4h HIGHLOW
    000218E8h HIGHLOW
    000218F0h HIGHLOW
    000218F4h HIGHLOW
    000218FCh HIGHLOW
    00021900h HIGHLOW
    00021910h HIGHLOW
    0002191Ch HIGHLOW
    00021920h HIGHLOW
    0002192Ch HIGHLOW
    00021930h HIGHLOW
    00021938h HIGHLOW
    0002193Ch HIGHLOW
    00021944h HIGHLOW
    00021948h HIGHLOW
    00021954h HIGHLOW
    00021958h HIGHLOW
    00021964h HIGHLOW
    00021968h HIGHLOW
    00021974h HIGHLOW
    00021978h HIGHLOW
    00021988h HIGHLOW
    00021B9Ch HIGHLOW
    00021BA0h HIGHLOW
    00021BA4h HIGHLOW
    00021BA8h HIGHLOW
    00021BACh HIGHLOW
    00021BB0h HIGHLOW
    00021BB4h HIGHLOW
    00021BB8h HIGHLOW
    00021BBCh HIGHLOW
    00021BC0h HIGHLOW
    00021BE0h HIGHLOW
    00021BE4h HIGHLOW
    00021BE8h HIGHLOW
    00021BECh HIGHLOW
    00021BF0h HIGHLOW
    00021BF4h HIGHLOW
    00021BF8h HIGHLOW
    00021BFCh HIGHLOW
    00021C00h HIGHLOW
    00021C04h HIGHLOW
    00021C10h HIGHLOW
    00021C1Ch HIGHLOW
    00021C20h HIGHLOW
    00021C28h HIGHLOW
    00021C2Ch HIGHLOW
    00021C34h HIGHLOW
    00021C38h HIGHLOW
    00021C44h HIGHLOW
    00021C48h HIGHLOW
    00021C54h HIGHLOW
    00021C58h HIGHLOW
    00021C6Ch HIGHLOW
    00021C84h HIGHLOW
    00021C98h HIGHLOW
    00021CA0h HIGHLOW
    00021CA8h HIGHLOW
    00021CB0h HIGHLOW
    00021CB8h HIGHLOW
    00021CC0h HIGHLOW
    00021CC8h HIGHLOW
    00021D8Ch HIGHLOW
    00021D94h HIGHLOW
    00021EE4h HIGHLOW
    00021EF8h HIGHLOW
    00021FA4h HIGHLOW
    00021FB0h HIGHLOW
    00021FE8h HIGHLOW
    00021000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x22000   
SizeOfBlock:                   0x10      
    0002209Ch HIGHLOW
    000220FCh HIGHLOW
    00022100h HIGHLOW
    00022138h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x28000   
SizeOfBlock:                   0x1D4     
    00028AD0h HIGHLOW
    00028ADCh HIGHLOW
    00028AE0h HIGHLOW
    00028AECh HIGHLOW
    00028AF0h HIGHLOW
    00028AF4h HIGHLOW
    00028AF8h HIGHLOW
    00028AFCh HIGHLOW
    00028B00h HIGHLOW
    00028B04h HIGHLOW
    00028B08h HIGHLOW
    00028B0Ch HIGHLOW
    00028B10h HIGHLOW
    00028B14h HIGHLOW
    00028B18h HIGHLOW
    00028B1Ch HIGHLOW
    00028B20h HIGHLOW
    00028B24h HIGHLOW
    00028B28h HIGHLOW
    00028B2Ch HIGHLOW
    00028B30h HIGHLOW
    00028B34h HIGHLOW
    00028B38h HIGHLOW
    00028B3Ch HIGHLOW
    00028B40h HIGHLOW
    00028B44h HIGHLOW
    00028B48h HIGHLOW
    00028B4Ch HIGHLOW
    00028B50h HIGHLOW
    00028B54h HIGHLOW
    00028B58h HIGHLOW
    00028B5Ch HIGHLOW
    00028B60h HIGHLOW
    00028B64h HIGHLOW
    00028B68h HIGHLOW
    00028B6Ch HIGHLOW
    00028B70h HIGHLOW
    00028B74h HIGHLOW
    00028B78h HIGHLOW
    00028B7Ch HIGHLOW
    00028B80h HIGHLOW
    00028B84h HIGHLOW
    00028B88h HIGHLOW
    00028B8Ch HIGHLOW
    00028B90h HIGHLOW
    00028B94h HIGHLOW
    00028B98h HIGHLOW
    00028B9Ch HIGHLOW
    00028BA0h HIGHLOW
    00028BA4h HIGHLOW
    00028BA8h HIGHLOW
    00028BACh HIGHLOW
    00028BB0h HIGHLOW
    00028BB4h HIGHLOW
    00028BB8h HIGHLOW
    00028BBCh HIGHLOW
    00028BC0h HIGHLOW
    00028BC4h HIGHLOW
    00028BC8h HIGHLOW
    00028BCCh HIGHLOW
    00028BD0h HIGHLOW
    00028BD4h HIGHLOW
    00028BD8h HIGHLOW
    00028BDCh HIGHLOW
    00028BE0h HIGHLOW
    00028BE4h HIGHLOW
    00028BE8h HIGHLOW
    00028BECh HIGHLOW
    00028BF0h HIGHLOW
    00028BF4h HIGHLOW
    00028BF8h HIGHLOW
    00028BFCh HIGHLOW
    00028C00h HIGHLOW
    00028C04h HIGHLOW
    00028C08h HIGHLOW
    00028C0Ch HIGHLOW
    00028C10h HIGHLOW
    00028C14h HIGHLOW
    00028C18h HIGHLOW
    00028C1Ch HIGHLOW
    00028C20h HIGHLOW
    00028C24h HIGHLOW
    00028C28h HIGHLOW
    00028C2Ch HIGHLOW
    00028C30h HIGHLOW
    00028C34h HIGHLOW
    00028C38h HIGHLOW
    00028C3Ch HIGHLOW
    00028C40h HIGHLOW
    00028C44h HIGHLOW
    00028C48h HIGHLOW
    00028C4Ch HIGHLOW
    00028C50h HIGHLOW
    00028C54h HIGHLOW
    00028C58h HIGHLOW
    00028C5Ch HIGHLOW
    00028CECh HIGHLOW
    00028CF0h HIGHLOW
    00028CF8h HIGHLOW
    00028CFCh HIGHLOW
    00028D04h HIGHLOW
    00028D08h HIGHLOW
    00028D18h HIGHLOW
    00028D1Ch HIGHLOW
    00028D20h HIGHLOW
    00028D24h HIGHLOW
    00028D28h HIGHLOW
    00028D2Ch HIGHLOW
    00028D30h HIGHLOW
    00028D34h HIGHLOW
    00028D38h HIGHLOW
    00028D3Ch HIGHLOW
    00028D40h HIGHLOW
    00028D44h HIGHLOW
    00028D48h HIGHLOW
    00028D4Ch HIGHLOW
    00028D50h HIGHLOW
    00028D54h HIGHLOW
    00028D58h HIGHLOW
    00028D5Ch HIGHLOW
    00028D60h HIGHLOW
    00028D64h HIGHLOW
    00028D74h HIGHLOW
    00028D78h HIGHLOW
    00028D88h HIGHLOW
    00028D94h HIGHLOW
    00028D98h HIGHLOW
    00028DA4h HIGHLOW
    00028DA8h HIGHLOW
    00028DB4h HIGHLOW
    00028DB8h HIGHLOW
    00028DC0h HIGHLOW
    00028DC4h HIGHLOW
    00028DCCh HIGHLOW
    00028DD0h HIGHLOW
    00028DD8h HIGHLOW
    00028DDCh HIGHLOW
    00028DE0h HIGHLOW
    00028DE8h HIGHLOW
    00028DECh HIGHLOW
    00028DF4h HIGHLOW
    00028DF8h HIGHLOW
    00028E00h HIGHLOW
    00028E04h HIGHLOW
    00028E0Ch HIGHLOW
    00028E14h HIGHLOW
    00028E18h HIGHLOW
    00028E20h HIGHLOW
    00028E24h HIGHLOW
    00028E28h HIGHLOW
    00028E30h HIGHLOW
    00028E34h HIGHLOW
    00028E38h HIGHLOW
    00028E3Ch HIGHLOW
    00028E40h HIGHLOW
    00028E44h HIGHLOW
    00028E48h HIGHLOW
    00028E4Ch HIGHLOW
    00028E54h HIGHLOW
    00028E58h HIGHLOW
    00028E60h HIGHLOW
    00028E64h HIGHLOW
    00028E6Ch HIGHLOW
    00028E70h HIGHLOW
    00028E78h HIGHLOW
    00028E80h HIGHLOW
    00028E84h HIGHLOW
    00028E88h HIGHLOW
    00028E90h HIGHLOW
    00028E98h HIGHLOW
    00028E9Ch HIGHLOW
    00028EA0h HIGHLOW
    00028EA8h HIGHLOW
    00028EACh HIGHLOW
    00028EB4h HIGHLOW
    00028EB8h HIGHLOW
    00028EC0h HIGHLOW
    00028EC4h HIGHLOW
    00028ECCh HIGHLOW
    00028ED0h HIGHLOW
    00028ED8h HIGHLOW
    00028EDCh HIGHLOW
    00028EE4h HIGHLOW
    00028EE8h HIGHLOW
    00028EF0h HIGHLOW
    00028EF4h HIGHLOW
    00028EFCh HIGHLOW
    00028F00h HIGHLOW
    00028F08h HIGHLOW
    00028F0Ch HIGHLOW
    00028F14h HIGHLOW
    00028F18h HIGHLOW
    00028F20h HIGHLOW
    00028F24h HIGHLOW
    00028F2Ch HIGHLOW
    00028F30h HIGHLOW
    00028F38h HIGHLOW
    00028F3Ch HIGHLOW
    00028F44h HIGHLOW
    00028F48h HIGHLOW
    00028F50h HIGHLOW
    00028F54h HIGHLOW
    00028F5Ch HIGHLOW
    00028F64h HIGHLOW
    00028F68h HIGHLOW
    00028F6Ch HIGHLOW
    00028F74h HIGHLOW
    00028F78h HIGHLOW
    00028F80h HIGHLOW
    00028F84h HIGHLOW
    00028F8Ch HIGHLOW
    00028F90h HIGHLOW
    00028F98h HIGHLOW
    00028F9Ch HIGHLOW
    00028FA4h HIGHLOW
    00028FA8h HIGHLOW
    00028FB0h HIGHLOW
    00028FB8h HIGHLOW
    00028FBCh HIGHLOW
    00028FC0h HIGHLOW
    00028FC8h HIGHLOW
    00028FD0h HIGHLOW
    00028FD4h HIGHLOW
    00028FD8h HIGHLOW
    00028FE0h HIGHLOW
    00028FE4h HIGHLOW
    00028FECh HIGHLOW
    00028FF0h HIGHLOW
    00028FF8h HIGHLOW
    00028FFCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x29000   
SizeOfBlock:                   0x2B8     
    00029004h HIGHLOW
    00029008h HIGHLOW
    00029010h HIGHLOW
    00029014h HIGHLOW
    0002901Ch HIGHLOW
    00029020h HIGHLOW
    00029028h HIGHLOW
    0002902Ch HIGHLOW
    00029034h HIGHLOW
    00029038h HIGHLOW
    00029040h HIGHLOW
    00029044h HIGHLOW
    0002904Ch HIGHLOW
    00029050h HIGHLOW
    00029058h HIGHLOW
    0002905Ch HIGHLOW
    00029064h HIGHLOW
    00029068h HIGHLOW
    00029070h HIGHLOW
    00029074h HIGHLOW
    0002907Ch HIGHLOW
    00029080h HIGHLOW
    00029088h HIGHLOW
    00029090h HIGHLOW
    00029094h HIGHLOW
    00029098h HIGHLOW
    000290A0h HIGHLOW
    000290A4h HIGHLOW
    000290ACh HIGHLOW
    000290B4h HIGHLOW
    000290B8h HIGHLOW
    000290BCh HIGHLOW
    000290C4h HIGHLOW
    000290CCh HIGHLOW
    000290D0h HIGHLOW
    000290D4h HIGHLOW
    000290DCh HIGHLOW
    000290E0h HIGHLOW
    000290E8h HIGHLOW
    000290ECh HIGHLOW
    000290F4h HIGHLOW
    000290F8h HIGHLOW
    00029100h HIGHLOW
    00029104h HIGHLOW
    0002910Ch HIGHLOW
    00029110h HIGHLOW
    00029118h HIGHLOW
    0002911Ch HIGHLOW
    00029124h HIGHLOW
    00029128h HIGHLOW
    00029130h HIGHLOW
    00029134h HIGHLOW
    0002913Ch HIGHLOW
    00029140h HIGHLOW
    00029148h HIGHLOW
    0002914Ch HIGHLOW
    00029154h HIGHLOW
    00029158h HIGHLOW
    00029160h HIGHLOW
    00029164h HIGHLOW
    0002916Ch HIGHLOW
    00029170h HIGHLOW
    00029178h HIGHLOW
    0002917Ch HIGHLOW
    00029180h HIGHLOW
    00029184h HIGHLOW
    00029188h HIGHLOW
    0002918Ch HIGHLOW
    00029190h HIGHLOW
    00029194h HIGHLOW
    00029198h HIGHLOW
    0002919Ch HIGHLOW
    000291A0h HIGHLOW
    000291A4h HIGHLOW
    000291A8h HIGHLOW
    000291B0h HIGHLOW
    000291B4h HIGHLOW
    000291B8h HIGHLOW
    000291C0h HIGHLOW
    000291C4h HIGHLOW
    000291CCh HIGHLOW
    000291D0h HIGHLOW
    000291D8h HIGHLOW
    000291DCh HIGHLOW
    000291E4h HIGHLOW
    000291E8h HIGHLOW
    000291ECh HIGHLOW
    000291F0h HIGHLOW
    000291F4h HIGHLOW
    000291FCh HIGHLOW
    00029200h HIGHLOW
    00029204h HIGHLOW
    00029208h HIGHLOW
    0002920Ch HIGHLOW
    00029214h HIGHLOW
    00029218h HIGHLOW
    0002921Ch HIGHLOW
    00029220h HIGHLOW
    00029224h HIGHLOW
    0002922Ch HIGHLOW
    00029230h HIGHLOW
    00029238h HIGHLOW
    0002923Ch HIGHLOW
    00029240h HIGHLOW
    00029244h HIGHLOW
    00029248h HIGHLOW
    00029250h HIGHLOW
    00029254h HIGHLOW
    0002925Ch HIGHLOW
    00029264h HIGHLOW
    00029268h HIGHLOW
    0002926Ch HIGHLOW
    00029274h HIGHLOW
    00029278h HIGHLOW
    00029280h HIGHLOW
    00029284h HIGHLOW
    00029288h HIGHLOW
    0002928Ch HIGHLOW
    00029290h HIGHLOW
    000297BCh HIGHLOW
    000297C4h HIGHLOW
    000297CCh HIGHLOW
    000297D4h HIGHLOW
    000297DCh HIGHLOW
    000297E4h HIGHLOW
    000297ECh HIGHLOW
    000297F4h HIGHLOW
    000297FCh HIGHLOW
    00029804h HIGHLOW
    0002980Ch HIGHLOW
    00029814h HIGHLOW
    0002981Ch HIGHLOW
    00029824h HIGHLOW
    0002982Ch HIGHLOW
    00029834h HIGHLOW
    0002983Ch HIGHLOW
    00029844h HIGHLOW
    0002984Ch HIGHLOW
    00029854h HIGHLOW
    0002985Ch HIGHLOW
    00029864h HIGHLOW
    0002986Ch HIGHLOW
    00029874h HIGHLOW
    0002987Ch HIGHLOW
    00029884h HIGHLOW
    0002988Ch HIGHLOW
    00029894h HIGHLOW
    0002989Ch HIGHLOW
    000298A4h HIGHLOW
    000298ACh HIGHLOW
    000298B4h HIGHLOW
    000298BCh HIGHLOW
    000298C4h HIGHLOW
    000298CCh HIGHLOW
    000298D4h HIGHLOW
    000298DCh HIGHLOW
    000298E4h HIGHLOW
    000298ECh HIGHLOW
    000298F4h HIGHLOW
    000298FCh HIGHLOW
    00029904h HIGHLOW
    0002990Ch HIGHLOW
    00029914h HIGHLOW
    0002991Ch HIGHLOW
    00029924h HIGHLOW
    0002992Ch HIGHLOW
    00029934h HIGHLOW
    0002993Ch HIGHLOW
    00029944h HIGHLOW
    0002994Ch HIGHLOW
    00029954h HIGHLOW
    0002995Ch HIGHLOW
    00029964h HIGHLOW
    0002996Ch HIGHLOW
    00029974h HIGHLOW
    0002997Ch HIGHLOW
    00029984h HIGHLOW
    0002998Ch HIGHLOW
    00029994h HIGHLOW
    0002999Ch HIGHLOW
    000299A4h HIGHLOW
    000299ACh HIGHLOW
    000299B4h HIGHLOW
    000299BCh HIGHLOW
    000299C4h HIGHLOW
    000299CCh HIGHLOW
    000299D4h HIGHLOW
    000299DCh HIGHLOW
    000299E4h HIGHLOW
    000299ECh HIGHLOW
    000299F4h HIGHLOW
    000299FCh HIGHLOW
    00029A04h HIGHLOW
    00029A0Ch HIGHLOW
    00029A14h HIGHLOW
    00029A1Ch HIGHLOW
    00029A24h HIGHLOW
    00029A2Ch HIGHLOW
    00029A34h HIGHLOW
    00029A3Ch HIGHLOW
    00029A44h HIGHLOW
    00029A4Ch HIGHLOW
    00029A54h HIGHLOW
    00029A5Ch HIGHLOW
    00029A64h HIGHLOW
    00029A6Ch HIGHLOW
    00029A74h HIGHLOW
    00029A7Ch HIGHLOW
    00029A84h HIGHLOW
    00029A8Ch HIGHLOW
    00029A94h HIGHLOW
    00029A9Ch HIGHLOW
    00029AA4h HIGHLOW
    00029AACh HIGHLOW
    00029AB4h HIGHLOW
    00029ABCh HIGHLOW
    00029AC4h HIGHLOW
    00029ACCh HIGHLOW
    00029AD4h HIGHLOW
    00029ADCh HIGHLOW
    00029AE4h HIGHLOW
    00029AECh HIGHLOW
    00029AF4h HIGHLOW
    00029AFCh HIGHLOW
    00029B04h HIGHLOW
    00029B0Ch HIGHLOW
    00029B14h HIGHLOW
    00029B1Ch HIGHLOW
    00029B24h HIGHLOW
    00029B2Ch HIGHLOW
    00029B34h HIGHLOW
    00029B3Ch HIGHLOW
    00029B40h HIGHLOW
    00029B44h HIGHLOW
    00029B48h HIGHLOW
    00029B4Ch HIGHLOW
    00029B50h HIGHLOW
    00029B54h HIGHLOW
    00029B58h HIGHLOW
    00029B5Ch HIGHLOW
    00029B60h HIGHLOW
    00029B64h HIGHLOW
    00029B68h HIGHLOW
    00029B6Ch HIGHLOW
    00029BF4h HIGHLOW
    00029BFCh HIGHLOW
    00029C04h HIGHLOW
    00029C0Ch HIGHLOW
    00029C14h HIGHLOW
    00029C1Ch HIGHLOW
    00029C24h HIGHLOW
    00029C2Ch HIGHLOW
    00029C34h HIGHLOW
    00029C3Ch HIGHLOW
    00029C44h HIGHLOW
    00029C4Ch HIGHLOW
    00029C54h HIGHLOW
    00029C5Ch HIGHLOW
    00029C64h HIGHLOW
    00029C6Ch HIGHLOW
    00029C70h HIGHLOW
    00029C74h HIGHLOW
    00029C78h HIGHLOW
    00029C7Ch HIGHLOW
    00029C80h HIGHLOW
    00029C84h HIGHLOW
    00029C88h HIGHLOW
    00029C8Ch HIGHLOW
    00029C90h HIGHLOW
    00029C94h HIGHLOW
    00029C98h HIGHLOW
    00029C9Ch HIGHLOW
    00029CA0h HIGHLOW
    00029CA4h HIGHLOW
    00029CA8h HIGHLOW
    00029CACh HIGHLOW
    00029CB0h HIGHLOW
    00029CB4h HIGHLOW
    00029CB8h HIGHLOW
    00029CBCh HIGHLOW
    00029CC0h HIGHLOW
    00029CC4h HIGHLOW
    00029CC8h HIGHLOW
    00029CCCh HIGHLOW
    00029CD0h HIGHLOW
    00029CD4h HIGHLOW
    00029CD8h HIGHLOW
    00029CDCh HIGHLOW
    00029CE0h HIGHLOW
    00029CE4h HIGHLOW
    00029E34h HIGHLOW
    00029E38h HIGHLOW
    00029E3Ch HIGHLOW
    00029E40h HIGHLOW
    00029E68h HIGHLOW
    00029E6Ch HIGHLOW
    00029E70h HIGHLOW
    00029E74h HIGHLOW
    00029EBCh HIGHLOW
    00029EC4h HIGHLOW
    00029ECCh HIGHLOW
    00029ED4h HIGHLOW
    00029EDCh HIGHLOW
    00029EE4h HIGHLOW
    00029EECh HIGHLOW
    00029EF4h HIGHLOW
    00029EFCh HIGHLOW
    00029F04h HIGHLOW
    00029F0Ch HIGHLOW
    00029F14h HIGHLOW
    00029F1Ch HIGHLOW
    00029F24h HIGHLOW
    00029F2Ch HIGHLOW
    00029F34h HIGHLOW
    00029F3Ch HIGHLOW
    00029F44h HIGHLOW
    00029F4Ch HIGHLOW
    00029F54h HIGHLOW
    00029F5Ch HIGHLOW
    00029F64h HIGHLOW
    00029F6Ch HIGHLOW
    00029F74h HIGHLOW
    00029F7Ch HIGHLOW
    00029F84h HIGHLOW
    00029F8Ch HIGHLOW
    00029F94h HIGHLOW
    00029F9Ch HIGHLOW
    00029FA4h HIGHLOW
    00029FACh HIGHLOW
    00029FB4h HIGHLOW
    00029FBCh HIGHLOW
    00029FC4h HIGHLOW
    00029FCCh HIGHLOW
    00029FD4h HIGHLOW
    00029FDCh HIGHLOW
    00029FE0h HIGHLOW
    00029FE4h HIGHLOW
    00029FE8h HIGHLOW
    00029FECh HIGHLOW
    00029FF0h HIGHLOW
    00029FF4h HIGHLOW
    00029FF8h HIGHLOW
    00029FFCh HIGHLOW
    00029000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2A000   
SizeOfBlock:                   0x2DC     
    0002A000h HIGHLOW
    0002A004h HIGHLOW
    0002A008h HIGHLOW
    0002A00Ch HIGHLOW
    0002A010h HIGHLOW
    0002A014h HIGHLOW
    0002A018h HIGHLOW
    0002A01Ch HIGHLOW
    0002A020h HIGHLOW
    0002A024h HIGHLOW
    0002A028h HIGHLOW
    0002A02Ch HIGHLOW
    0002A158h HIGHLOW
    0002A15Ch HIGHLOW
    0002A160h HIGHLOW
    0002A164h HIGHLOW
    0002A168h HIGHLOW
    0002A16Ch HIGHLOW
    0002A170h HIGHLOW
    0002A174h HIGHLOW
    0002A178h HIGHLOW
    0002A17Ch HIGHLOW
    0002A180h HIGHLOW
    0002A184h HIGHLOW
    0002A188h HIGHLOW
    0002A18Ch HIGHLOW
    0002A190h HIGHLOW
    0002A194h HIGHLOW
    0002A198h HIGHLOW
    0002A19Ch HIGHLOW
    0002A1A0h HIGHLOW
    0002A1A4h HIGHLOW
    0002A1A8h HIGHLOW
    0002A1ACh HIGHLOW
    0002A1B0h HIGHLOW
    0002A1B4h HIGHLOW
    0002A1B8h HIGHLOW
    0002A1BCh HIGHLOW
    0002A1C0h HIGHLOW
    0002A1C4h HIGHLOW
    0002A1C8h HIGHLOW
    0002A1CCh HIGHLOW
    0002A1D0h HIGHLOW
    0002A1D4h HIGHLOW
    0002A1D8h HIGHLOW
    0002A1DCh HIGHLOW
    0002A1E0h HIGHLOW
    0002A1E4h HIGHLOW
    0002A1E8h HIGHLOW
    0002A1ECh HIGHLOW
    0002A40Ch HIGHLOW
    0002A410h HIGHLOW
    0002A414h HIGHLOW
    0002A418h HIGHLOW
    0002A41Ch HIGHLOW
    0002A420h HIGHLOW
    0002A424h HIGHLOW
    0002A428h HIGHLOW
    0002A42Ch HIGHLOW
    0002A430h HIGHLOW
    0002A434h HIGHLOW
    0002A438h HIGHLOW
    0002A43Ch HIGHLOW
    0002A440h HIGHLOW
    0002A444h HIGHLOW
    0002A448h HIGHLOW
    0002A44Ch HIGHLOW
    0002A450h HIGHLOW
    0002A454h HIGHLOW
    0002A458h HIGHLOW
    0002A45Ch HIGHLOW
    0002A460h HIGHLOW
    0002A464h HIGHLOW
    0002A468h HIGHLOW
    0002A46Ch HIGHLOW
    0002A470h HIGHLOW
    0002A474h HIGHLOW
    0002A478h HIGHLOW
    0002A47Ch HIGHLOW
    0002A480h HIGHLOW
    0002A484h HIGHLOW
    0002A488h HIGHLOW
    0002A48Ch HIGHLOW
    0002A490h HIGHLOW
    0002A494h HIGHLOW
    0002A498h HIGHLOW
    0002A49Ch HIGHLOW
    0002A4A0h HIGHLOW
    0002A4A4h HIGHLOW
    0002A4A8h HIGHLOW
    0002A4ACh HIGHLOW
    0002A4B0h HIGHLOW
    0002A4B4h HIGHLOW
    0002A4B8h HIGHLOW
    0002A4BCh HIGHLOW
    0002A4C0h HIGHLOW
    0002A4C4h HIGHLOW
    0002A4C8h HIGHLOW
    0002A4CCh HIGHLOW
    0002A4D0h HIGHLOW
    0002A4D4h HIGHLOW
    0002A4D8h HIGHLOW
    0002A4DCh HIGHLOW
    0002A4E0h HIGHLOW
    0002A4E4h HIGHLOW
    0002A4E8h HIGHLOW
    0002A4ECh HIGHLOW
    0002A4F0h HIGHLOW
    0002A4F4h HIGHLOW
    0002A4F8h HIGHLOW
    0002A4FCh HIGHLOW
    0002A500h HIGHLOW
    0002A504h HIGHLOW
    0002A508h HIGHLOW
    0002A50Ch HIGHLOW
    0002A510h HIGHLOW
    0002A514h HIGHLOW
    0002A518h HIGHLOW
    0002A51Ch HIGHLOW
    0002A520h HIGHLOW
    0002A524h HIGHLOW
    0002A528h HIGHLOW
    0002A52Ch HIGHLOW
    0002A530h HIGHLOW
    0002A534h HIGHLOW
    0002A538h HIGHLOW
    0002A53Ch HIGHLOW
    0002A540h HIGHLOW
    0002A544h HIGHLOW
    0002A548h HIGHLOW
    0002A54Ch HIGHLOW
    0002A550h HIGHLOW
    0002A554h HIGHLOW
    0002A558h HIGHLOW
    0002A55Ch HIGHLOW
    0002A560h HIGHLOW
    0002A564h HIGHLOW
    0002A568h HIGHLOW
    0002A56Ch HIGHLOW
    0002A570h HIGHLOW
    0002A574h HIGHLOW
    0002A578h HIGHLOW
    0002A57Ch HIGHLOW
    0002A580h HIGHLOW
    0002A584h HIGHLOW
    0002A588h HIGHLOW
    0002A58Ch HIGHLOW
    0002A590h HIGHLOW
    0002A594h HIGHLOW
    0002A598h HIGHLOW
    0002A59Ch HIGHLOW
    0002A5A0h HIGHLOW
    0002A5A4h HIGHLOW
    0002A5A8h HIGHLOW
    0002A5ACh HIGHLOW
    0002A5B0h HIGHLOW
    0002A5B4h HIGHLOW
    0002A5B8h HIGHLOW
    0002A5BCh HIGHLOW
    0002A5C0h HIGHLOW
    0002A5C4h HIGHLOW
    0002A5C8h HIGHLOW
    0002A5CCh HIGHLOW
    0002A5D0h HIGHLOW
    0002A5D4h HIGHLOW
    0002A5D8h HIGHLOW
    0002A5DCh HIGHLOW
    0002A5E0h HIGHLOW
    0002A5E4h HIGHLOW
    0002A5E8h HIGHLOW
    0002A5ECh HIGHLOW
    0002A5F0h HIGHLOW
    0002A5F4h HIGHLOW
    0002A5F8h HIGHLOW
    0002A5FCh HIGHLOW
    0002A600h HIGHLOW
    0002A604h HIGHLOW
    0002A608h HIGHLOW
    0002A60Ch HIGHLOW
    0002A610h HIGHLOW
    0002A614h HIGHLOW
    0002A618h HIGHLOW
    0002A61Ch HIGHLOW
    0002A620h HIGHLOW
    0002A624h HIGHLOW
    0002A628h HIGHLOW
    0002A62Ch HIGHLOW
    0002AAF0h HIGHLOW
    0002AAF4h HIGHLOW
    0002AAF8h HIGHLOW
    0002AAFCh HIGHLOW
    0002AB00h HIGHLOW
    0002AB04h HIGHLOW
    0002AB08h HIGHLOW
    0002AB0Ch HIGHLOW
    0002AB10h HIGHLOW
    0002AB14h HIGHLOW
    0002AB18h HIGHLOW
    0002AB1Ch HIGHLOW
    0002AB20h HIGHLOW
    0002AB24h HIGHLOW
    0002AB28h HIGHLOW
    0002AB2Ch HIGHLOW
    0002AB30h HIGHLOW
    0002AB34h HIGHLOW
    0002ABF0h HIGHLOW
    0002ABF4h HIGHLOW
    0002ABF8h HIGHLOW
    0002ABFCh HIGHLOW
    0002AC00h HIGHLOW
    0002AC04h HIGHLOW
    0002AC08h HIGHLOW
    0002AC0Ch HIGHLOW
    0002AC10h HIGHLOW
    0002AC14h HIGHLOW
    0002AC18h HIGHLOW
    0002AC1Ch HIGHLOW
    0002AC20h HIGHLOW
    0002AC24h HIGHLOW
    0002AC28h HIGHLOW
    0002AC2Ch HIGHLOW
    0002AC30h HIGHLOW
    0002AC34h HIGHLOW
    0002AC38h HIGHLOW
    0002AC3Ch HIGHLOW
    0002AC40h HIGHLOW
    0002AC44h HIGHLOW
    0002AC48h HIGHLOW
    0002AC4Ch HIGHLOW
    0002AC50h HIGHLOW
    0002AC54h HIGHLOW
    0002AC58h HIGHLOW
    0002AC5Ch HIGHLOW
    0002AC60h HIGHLOW
    0002AC64h HIGHLOW
    0002AC68h HIGHLOW
    0002AC6Ch HIGHLOW
    0002AC70h HIGHLOW
    0002AC74h HIGHLOW
    0002AC78h HIGHLOW
    0002AC7Ch HIGHLOW
    0002AC80h HIGHLOW
    0002AC84h HIGHLOW
    0002AC88h HIGHLOW
    0002AC8Ch HIGHLOW
    0002AC90h HIGHLOW
    0002AC94h HIGHLOW
    0002AC98h HIGHLOW
    0002AC9Ch HIGHLOW
    0002ACA0h HIGHLOW
    0002ACA4h HIGHLOW
    0002ACA8h HIGHLOW
    0002ACACh HIGHLOW
    0002AE2Ch HIGHLOW
    0002AE34h HIGHLOW
    0002AE3Ch HIGHLOW
    0002AE44h HIGHLOW
    0002AE4Ch HIGHLOW
    0002AE54h HIGHLOW
    0002AE5Ch HIGHLOW
    0002AE64h HIGHLOW
    0002AE6Ch HIGHLOW
    0002AE70h HIGHLOW
    0002AE74h HIGHLOW
    0002AE78h HIGHLOW
    0002AE7Ch HIGHLOW
    0002AE80h HIGHLOW
    0002AE84h HIGHLOW
    0002AE88h HIGHLOW
    0002AE8Ch HIGHLOW
    0002AE90h HIGHLOW
    0002AE94h HIGHLOW
    0002AE98h HIGHLOW
    0002AE9Ch HIGHLOW
    0002AEA0h HIGHLOW
    0002AEA4h HIGHLOW
    0002AEA8h HIGHLOW
    0002AEACh HIGHLOW
    0002AEB0h HIGHLOW
    0002AEB4h HIGHLOW
    0002AEB8h HIGHLOW
    0002AEBCh HIGHLOW
    0002AEC0h HIGHLOW
    0002AEC4h HIGHLOW
    0002AEC8h HIGHLOW
    0002AECCh HIGHLOW
    0002AED0h HIGHLOW
    0002AED4h HIGHLOW
    0002AED8h HIGHLOW
    0002AEDCh HIGHLOW
    0002AEE0h HIGHLOW
    0002AEE4h HIGHLOW
    0002AEE8h HIGHLOW
    0002AEECh HIGHLOW
    0002AEF0h HIGHLOW
    0002AEF4h HIGHLOW
    0002AEF8h HIGHLOW
    0002AEFCh HIGHLOW
    0002AF00h HIGHLOW
    0002AF04h HIGHLOW
    0002AF08h HIGHLOW
    0002AF0Ch HIGHLOW
    0002AF10h HIGHLOW
    0002AF14h HIGHLOW
    0002AF18h HIGHLOW
    0002AF1Ch HIGHLOW
    0002AF20h HIGHLOW
    0002AF24h HIGHLOW
    0002AF28h HIGHLOW
    0002AF2Ch HIGHLOW
    0002AF30h HIGHLOW
    0002AF34h HIGHLOW
    0002AF38h HIGHLOW
    0002AF3Ch HIGHLOW
    0002AF40h HIGHLOW
    0002AF44h HIGHLOW
    0002AF48h HIGHLOW
    0002AF4Ch HIGHLOW
    0002AF50h HIGHLOW
    0002AF54h HIGHLOW
    0002AF58h HIGHLOW
    0002AF5Ch HIGHLOW
    0002AF60h HIGHLOW
    0002AF64h HIGHLOW
    0002AF68h HIGHLOW
    0002AF6Ch HIGHLOW
    0002AF70h HIGHLOW
    0002AF74h HIGHLOW
    0002AF78h HIGHLOW
    0002AF7Ch HIGHLOW
    0002AF80h HIGHLOW
    0002AF84h HIGHLOW
    0002AF88h HIGHLOW
    0002AF8Ch HIGHLOW
    0002AF90h HIGHLOW
    0002AF94h HIGHLOW
    0002AF98h HIGHLOW
    0002AF9Ch HIGHLOW
    0002AFA0h HIGHLOW
    0002AFA4h HIGHLOW
    0002AFA8h HIGHLOW
    0002AFACh HIGHLOW
    0002AFB0h HIGHLOW
    0002AFB4h HIGHLOW
    0002AFB8h HIGHLOW
    0002AFBCh HIGHLOW
    0002AFC0h HIGHLOW
    0002AFC4h HIGHLOW
    0002AFC8h HIGHLOW
    0002AFCCh HIGHLOW
    0002AFD0h HIGHLOW
    0002AFD4h HIGHLOW
    0002AFD8h HIGHLOW
    0002AFDCh HIGHLOW
    0002AFE0h HIGHLOW
    0002AFE4h HIGHLOW
    0002AFE8h HIGHLOW
    0002AFECh HIGHLOW
    0002AFF0h HIGHLOW
    0002AFF4h HIGHLOW
    0002AFF8h HIGHLOW
    0002AFFCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2B000   
SizeOfBlock:                   0x1C4     
    0002B000h HIGHLOW
    0002B004h HIGHLOW
    0002B008h HIGHLOW
    0002B00Ch HIGHLOW
    0002B010h HIGHLOW
    0002B014h HIGHLOW
    0002B018h HIGHLOW
    0002B01Ch HIGHLOW
    0002B020h HIGHLOW
    0002B024h HIGHLOW
    0002B028h HIGHLOW
    0002B02Ch HIGHLOW
    0002B030h HIGHLOW
    0002B034h HIGHLOW
    0002B038h HIGHLOW
    0002B03Ch HIGHLOW
    0002B040h HIGHLOW
    0002B044h HIGHLOW
    0002B048h HIGHLOW
    0002B04Ch HIGHLOW
    0002B050h HIGHLOW
    0002B054h HIGHLOW
    0002B058h HIGHLOW
    0002B05Ch HIGHLOW
    0002B060h HIGHLOW
    0002B064h HIGHLOW
    0002B068h HIGHLOW
    0002B06Ch HIGHLOW
    0002B070h HIGHLOW
    0002B074h HIGHLOW
    0002B078h HIGHLOW
    0002B07Ch HIGHLOW
    0002B080h HIGHLOW
    0002B084h HIGHLOW
    0002B088h HIGHLOW
    0002B08Ch HIGHLOW
    0002B090h HIGHLOW
    0002B094h HIGHLOW
    0002B098h HIGHLOW
    0002B09Ch HIGHLOW
    0002B0A0h HIGHLOW
    0002B0A4h HIGHLOW
    0002B0A8h HIGHLOW
    0002B0ACh HIGHLOW
    0002B0B0h HIGHLOW
    0002B0B4h HIGHLOW
    0002B0B8h HIGHLOW
    0002B0BCh HIGHLOW
    0002B0C0h HIGHLOW
    0002B0C4h HIGHLOW
    0002B0C8h HIGHLOW
    0002B0CCh HIGHLOW
    0002B0D0h HIGHLOW
    0002B0D4h HIGHLOW
    0002B0D8h HIGHLOW
    0002B0DCh HIGHLOW
    0002B0E0h HIGHLOW
    0002B0E4h HIGHLOW
    0002B0E8h HIGHLOW
    0002B0ECh HIGHLOW
    0002B0F0h HIGHLOW
    0002B0F4h HIGHLOW
    0002B0F8h HIGHLOW
    0002B0FCh HIGHLOW
    0002B100h HIGHLOW
    0002B104h HIGHLOW
    0002B108h HIGHLOW
    0002B10Ch HIGHLOW
    0002B110h HIGHLOW
    0002B114h HIGHLOW
    0002B118h HIGHLOW
    0002B11Ch HIGHLOW
    0002B938h HIGHLOW
    0002B93Ch HIGHLOW
    0002B940h HIGHLOW
    0002B944h HIGHLOW
    0002B948h HIGHLOW
    0002B94Ch HIGHLOW
    0002B950h HIGHLOW
    0002B954h HIGHLOW
    0002B958h HIGHLOW
    0002B95Ch HIGHLOW
    0002B960h HIGHLOW
    0002B964h HIGHLOW
    0002B968h HIGHLOW
    0002B96Ch HIGHLOW
    0002BA04h HIGHLOW
    0002BA0Ch HIGHLOW
    0002BA14h HIGHLOW
    0002BA1Ch HIGHLOW
    0002BA24h HIGHLOW
    0002BA2Ch HIGHLOW
    0002BA34h HIGHLOW
    0002BA3Ch HIGHLOW
    0002BA44h HIGHLOW
    0002BA4Ch HIGHLOW
    0002BA54h HIGHLOW
    0002BA5Ch HIGHLOW
    0002BA64h HIGHLOW
    0002BA6Ch HIGHLOW
    0002BA74h HIGHLOW
    0002BA7Ch HIGHLOW
    0002BA84h HIGHLOW
    0002BA8Ch HIGHLOW
    0002BA94h HIGHLOW
    0002BA9Ch HIGHLOW
    0002BAA4h HIGHLOW
    0002BAACh HIGHLOW
    0002BAB4h HIGHLOW
    0002BABCh HIGHLOW
    0002BAC4h HIGHLOW
    0002BACCh HIGHLOW
    0002BAD4h HIGHLOW
    0002BADCh HIGHLOW
    0002BAE4h HIGHLOW
    0002BAECh HIGHLOW
    0002BAF4h HIGHLOW
    0002BAFCh HIGHLOW
    0002BB04h HIGHLOW
    0002BB0Ch HIGHLOW
    0002BB14h HIGHLOW
    0002BB1Ch HIGHLOW
    0002BB24h HIGHLOW
    0002BB2Ch HIGHLOW
    0002BB34h HIGHLOW
    0002BB3Ch HIGHLOW
    0002BB44h HIGHLOW
    0002BB4Ch HIGHLOW
    0002BB50h HIGHLOW
    0002BB54h HIGHLOW
    0002BB58h HIGHLOW
    0002BB5Ch HIGHLOW
    0002BB60h HIGHLOW
    0002BB64h HIGHLOW
    0002BB68h HIGHLOW
    0002BB6Ch HIGHLOW
    0002BB70h HIGHLOW
    0002BB74h HIGHLOW
    0002BB78h HIGHLOW
    0002BB7Ch HIGHLOW
    0002BB80h HIGHLOW
    0002BB84h HIGHLOW
    0002BB88h HIGHLOW
    0002BB8Ch HIGHLOW
    0002BB90h HIGHLOW
    0002BB94h HIGHLOW
    0002BB98h HIGHLOW
    0002BB9Ch HIGHLOW
    0002BBA0h HIGHLOW
    0002BBA4h HIGHLOW
    0002BBA8h HIGHLOW
    0002BBACh HIGHLOW
    0002BBB0h HIGHLOW
    0002BBB4h HIGHLOW
    0002BBB8h HIGHLOW
    0002BBBCh HIGHLOW
    0002BBC0h HIGHLOW
    0002BBC4h HIGHLOW
    0002BBC8h HIGHLOW
    0002BBCCh HIGHLOW
    0002BBD0h HIGHLOW
    0002BBD4h HIGHLOW
    0002BBD8h HIGHLOW
    0002BBDCh HIGHLOW
    0002BBE0h HIGHLOW
    0002BBE4h HIGHLOW
    0002BBE8h HIGHLOW
    0002BBECh HIGHLOW
    0002BBF0h HIGHLOW
    0002BBF4h HIGHLOW
    0002BBF8h HIGHLOW
    0002BBFCh HIGHLOW
    0002BC00h HIGHLOW
    0002BC04h HIGHLOW
    0002BC08h HIGHLOW
    0002BC0Ch HIGHLOW
    0002BC10h HIGHLOW
    0002BC14h HIGHLOW
    0002BC18h HIGHLOW
    0002BC1Ch HIGHLOW
    0002BC20h HIGHLOW
    0002BC24h HIGHLOW
    0002BC28h HIGHLOW
    0002BC2Ch HIGHLOW
    0002BC30h HIGHLOW
    0002BC34h HIGHLOW
    0002BC38h HIGHLOW
    0002BC3Ch HIGHLOW
    0002BC40h HIGHLOW
    0002BC44h HIGHLOW
    0002BC48h HIGHLOW
    0002BC4Ch HIGHLOW
    0002BC50h HIGHLOW
    0002BC54h HIGHLOW
    0002BC58h HIGHLOW
    0002BC5Ch HIGHLOW
    0002BC60h HIGHLOW
    0002BC64h HIGHLOW
    0002BC68h HIGHLOW
    0002BC6Ch HIGHLOW
    0002BC70h HIGHLOW
    0002BC74h HIGHLOW
    0002BC78h HIGHLOW
    0002BC7Ch HIGHLOW
    0002BC80h HIGHLOW
    0002BC84h HIGHLOW
    0002BC88h HIGHLOW
    0002BC8Ch HIGHLOW
    0002BC90h HIGHLOW
    0002BC94h HIGHLOW
    0002BC98h HIGHLOW
    0002BC9Ch HIGHLOW
    0002BCA0h HIGHLOW
    0002BCA4h HIGHLOW
    0002BCA8h HIGHLOW
    0002BCACh HIGHLOW
    0002BCB0h HIGHLOW
    0002BCB4h HIGHLOW
    0002BCB8h HIGHLOW
    0002BCBCh HIGHLOW
    0002BCC0h HIGHLOW
    0002BCC4h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2C000   
SizeOfBlock:                   0x29C     
    0002C078h HIGHLOW
    0002C07Ch HIGHLOW
    0002C080h HIGHLOW
    0002C084h HIGHLOW
    0002C088h HIGHLOW
    0002C08Ch HIGHLOW
    0002C0E4h HIGHLOW
    0002C0ECh HIGHLOW
    0002C0F4h HIGHLOW
    0002C0FCh HIGHLOW
    0002C104h HIGHLOW
    0002C10Ch HIGHLOW
    0002C114h HIGHLOW
    0002C11Ch HIGHLOW
    0002C124h HIGHLOW
    0002C12Ch HIGHLOW
    0002C134h HIGHLOW
    0002C13Ch HIGHLOW
    0002C144h HIGHLOW
    0002C148h HIGHLOW
    0002C14Ch HIGHLOW
    0002C150h HIGHLOW
    0002C154h HIGHLOW
    0002C158h HIGHLOW
    0002C15Ch HIGHLOW
    0002C160h HIGHLOW
    0002C164h HIGHLOW
    0002C168h HIGHLOW
    0002C16Ch HIGHLOW
    0002C170h HIGHLOW
    0002C174h HIGHLOW
    0002C178h HIGHLOW
    0002C17Ch HIGHLOW
    0002C180h HIGHLOW
    0002C184h HIGHLOW
    0002C188h HIGHLOW
    0002C18Ch HIGHLOW
    0002C190h HIGHLOW
    0002C194h HIGHLOW
    0002C198h HIGHLOW
    0002C19Ch HIGHLOW
    0002C1A0h HIGHLOW
    0002C1A4h HIGHLOW
    0002C1A8h HIGHLOW
    0002C1ACh HIGHLOW
    0002C2F8h HIGHLOW
    0002C2FCh HIGHLOW
    0002C300h HIGHLOW
    0002C304h HIGHLOW
    0002C308h HIGHLOW
    0002C30Ch HIGHLOW
    0002C310h HIGHLOW
    0002C314h HIGHLOW
    0002C318h HIGHLOW
    0002C31Ch HIGHLOW
    0002C320h HIGHLOW
    0002C324h HIGHLOW
    0002C328h HIGHLOW
    0002C32Ch HIGHLOW
    0002C330h HIGHLOW
    0002C334h HIGHLOW
    0002C338h HIGHLOW
    0002C33Ch HIGHLOW
    0002C340h HIGHLOW
    0002C344h HIGHLOW
    0002C348h HIGHLOW
    0002C34Ch HIGHLOW
    0002C350h HIGHLOW
    0002C354h HIGHLOW
    0002C358h HIGHLOW
    0002C35Ch HIGHLOW
    0002C360h HIGHLOW
    0002C364h HIGHLOW
    0002C368h HIGHLOW
    0002C36Ch HIGHLOW
    0002C370h HIGHLOW
    0002C374h HIGHLOW
    0002C378h HIGHLOW
    0002C37Ch HIGHLOW
    0002C380h HIGHLOW
    0002C384h HIGHLOW
    0002C388h HIGHLOW
    0002C38Ch HIGHLOW
    0002C390h HIGHLOW
    0002C394h HIGHLOW
    0002C398h HIGHLOW
    0002C39Ch HIGHLOW
    0002C3A0h HIGHLOW
    0002C3A4h HIGHLOW
    0002C3A8h HIGHLOW
    0002C3ACh HIGHLOW
    0002C3B0h HIGHLOW
    0002C3B4h HIGHLOW
    0002C3B8h HIGHLOW
    0002C3BCh HIGHLOW
    0002C3C0h HIGHLOW
    0002C3C4h HIGHLOW
    0002C3C8h HIGHLOW
    0002C3CCh HIGHLOW
    0002C3D0h HIGHLOW
    0002C3D4h HIGHLOW
    0002C3D8h HIGHLOW
    0002C3DCh HIGHLOW
    0002C3E0h HIGHLOW
    0002C3E4h HIGHLOW
    0002C3E8h HIGHLOW
    0002C3ECh HIGHLOW
    0002C3F0h HIGHLOW
    0002C3F4h HIGHLOW
    0002C3F8h HIGHLOW
    0002C3FCh HIGHLOW
    0002C400h HIGHLOW
    0002C404h HIGHLOW
    0002C408h HIGHLOW
    0002C40Ch HIGHLOW
    0002C410h HIGHLOW
    0002C414h HIGHLOW
    0002C418h HIGHLOW
    0002C41Ch HIGHLOW
    0002C420h HIGHLOW
    0002C424h HIGHLOW
    0002C428h HIGHLOW
    0002C42Ch HIGHLOW
    0002C430h HIGHLOW
    0002C434h HIGHLOW
    0002C438h HIGHLOW
    0002C43Ch HIGHLOW
    0002C440h HIGHLOW
    0002C444h HIGHLOW
    0002C448h HIGHLOW
    0002C44Ch HIGHLOW
    0002C450h HIGHLOW
    0002C454h HIGHLOW
    0002C458h HIGHLOW
    0002C45Ch HIGHLOW
    0002C460h HIGHLOW
    0002C464h HIGHLOW
    0002C468h HIGHLOW
    0002C46Ch HIGHLOW
    0002C470h HIGHLOW
    0002C474h HIGHLOW
    0002C478h HIGHLOW
    0002C47Ch HIGHLOW
    0002C480h HIGHLOW
    0002C484h HIGHLOW
    0002C488h HIGHLOW
    0002C48Ch HIGHLOW
    0002C490h HIGHLOW
    0002C494h HIGHLOW
    0002C498h HIGHLOW
    0002C49Ch HIGHLOW
    0002C4A0h HIGHLOW
    0002C4A4h HIGHLOW
    0002C4A8h HIGHLOW
    0002C4ACh HIGHLOW
    0002C4B0h HIGHLOW
    0002C4B4h HIGHLOW
    0002C4B8h HIGHLOW
    0002C4BCh HIGHLOW
    0002C4C0h HIGHLOW
    0002C4C4h HIGHLOW
    0002C4C8h HIGHLOW
    0002C4CCh HIGHLOW
    0002C4D0h HIGHLOW
    0002C4D4h HIGHLOW
    0002C4D8h HIGHLOW
    0002C4DCh HIGHLOW
    0002C4E0h HIGHLOW
    0002C4E4h HIGHLOW
    0002C4E8h HIGHLOW
    0002C4ECh HIGHLOW
    0002C4F0h HIGHLOW
    0002C4F4h HIGHLOW
    0002C4F8h HIGHLOW
    0002C4FCh HIGHLOW
    0002C500h HIGHLOW
    0002C504h HIGHLOW
    0002C508h HIGHLOW
    0002C50Ch HIGHLOW
    0002C510h HIGHLOW
    0002C514h HIGHLOW
    0002C970h HIGHLOW
    0002C974h HIGHLOW
    0002C978h HIGHLOW
    0002C97Ch HIGHLOW
    0002C980h HIGHLOW
    0002C984h HIGHLOW
    0002C988h HIGHLOW
    0002C98Ch HIGHLOW
    0002C990h HIGHLOW
    0002C994h HIGHLOW
    0002C998h HIGHLOW
    0002C99Ch HIGHLOW
    0002C9A0h HIGHLOW
    0002C9A4h HIGHLOW
    0002C9A8h HIGHLOW
    0002C9ACh HIGHLOW
    0002C9B0h HIGHLOW
    0002C9B4h HIGHLOW
    0002C9B8h HIGHLOW
    0002C9BCh HIGHLOW
    0002C9C0h HIGHLOW
    0002C9C4h HIGHLOW
    0002C9C8h HIGHLOW
    0002C9CCh HIGHLOW
    0002C9D0h HIGHLOW
    0002C9D4h HIGHLOW
    0002C9D8h HIGHLOW
    0002C9DCh HIGHLOW
    0002C9E0h HIGHLOW
    0002C9E4h HIGHLOW
    0002C9E8h HIGHLOW
    0002C9ECh HIGHLOW
    0002C9F0h HIGHLOW
    0002C9F4h HIGHLOW
    0002C9F8h HIGHLOW
    0002C9FCh HIGHLOW
    0002CA00h HIGHLOW
    0002CA04h HIGHLOW
    0002CA08h HIGHLOW
    0002CA0Ch HIGHLOW
    0002CA10h HIGHLOW
    0002CA14h HIGHLOW
    0002CA18h HIGHLOW
    0002CA1Ch HIGHLOW
    0002CA20h HIGHLOW
    0002CA24h HIGHLOW
    0002CA28h HIGHLOW
    0002CA2Ch HIGHLOW
    0002CA30h HIGHLOW
    0002CA34h HIGHLOW
    0002CA38h HIGHLOW
    0002CA3Ch HIGHLOW
    0002CA40h HIGHLOW
    0002CA44h HIGHLOW
    0002CA48h HIGHLOW
    0002CA4Ch HIGHLOW
    0002CCDCh HIGHLOW
    0002CCE0h HIGHLOW
    0002CCF8h HIGHLOW
    0002CCFCh HIGHLOW
    0002CD18h HIGHLOW
    0002CD20h HIGHLOW
    0002CD28h HIGHLOW
    0002CD30h HIGHLOW
    0002CD38h HIGHLOW
    0002CD40h HIGHLOW
    0002CD48h HIGHLOW
    0002CD4Ch HIGHLOW
    0002CD50h HIGHLOW
    0002CD54h HIGHLOW
    0002CD58h HIGHLOW
    0002CD5Ch HIGHLOW
    0002CD60h HIGHLOW
    0002CD64h HIGHLOW
    0002CD68h HIGHLOW
    0002CDB4h HIGHLOW
    0002CDBCh HIGHLOW
    0002CDC4h HIGHLOW
    0002CDCCh HIGHLOW
    0002CDD4h HIGHLOW
    0002CDDCh HIGHLOW
    0002CDE4h HIGHLOW
    0002CDECh HIGHLOW
    0002CDF4h HIGHLOW
    0002CDFCh HIGHLOW
    0002CE04h HIGHLOW
    0002CE0Ch HIGHLOW
    0002CE14h HIGHLOW
    0002CE1Ch HIGHLOW
    0002CE24h HIGHLOW
    0002CE2Ch HIGHLOW
    0002CE34h HIGHLOW
    0002CE3Ch HIGHLOW
    0002CE44h HIGHLOW
    0002CE4Ch HIGHLOW
    0002CE54h HIGHLOW
    0002CE5Ch HIGHLOW
    0002CE64h HIGHLOW
    0002CE6Ch HIGHLOW
    0002CE74h HIGHLOW
    0002CE7Ch HIGHLOW
    0002CE84h HIGHLOW
    0002CE8Ch HIGHLOW
    0002CE94h HIGHLOW
    0002CE9Ch HIGHLOW
    0002CEA4h HIGHLOW
    0002CEACh HIGHLOW
    0002CEB4h HIGHLOW
    0002CEBCh HIGHLOW
    0002CEC4h HIGHLOW
    0002CECCh HIGHLOW
    0002CED4h HIGHLOW
    0002CEDCh HIGHLOW
    0002CEE4h HIGHLOW
    0002CEECh HIGHLOW
    0002CEF4h HIGHLOW
    0002CEFCh HIGHLOW
    0002CF04h HIGHLOW
    0002CF0Ch HIGHLOW
    0002CF14h HIGHLOW
    0002CF1Ch HIGHLOW
    0002CF24h HIGHLOW
    0002CF2Ch HIGHLOW
    0002CF34h HIGHLOW
    0002CF3Ch HIGHLOW
    0002CF44h HIGHLOW
    0002CF4Ch HIGHLOW
    0002CF54h HIGHLOW
    0002CF5Ch HIGHLOW
    0002CF64h HIGHLOW
    0002CF6Ch HIGHLOW
    0002CF74h HIGHLOW
    0002CF7Ch HIGHLOW
    0002CF84h HIGHLOW
    0002CF8Ch HIGHLOW
    0002CF94h HIGHLOW
    0002CF9Ch HIGHLOW
    0002CFA4h HIGHLOW
    0002CFACh HIGHLOW
    0002CFB4h HIGHLOW
    0002CFBCh HIGHLOW
    0002CFC4h HIGHLOW
    0002CFCCh HIGHLOW
    0002CFD4h HIGHLOW
    0002CFDCh HIGHLOW
    0002CFE4h HIGHLOW
    0002CFECh HIGHLOW
    0002CFF4h HIGHLOW
    0002CFFCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2D000   
SizeOfBlock:                   0x30C     
    0002D004h HIGHLOW
    0002D00Ch HIGHLOW
    0002D014h HIGHLOW
    0002D01Ch HIGHLOW
    0002D020h HIGHLOW
    0002D024h HIGHLOW
    0002D028h HIGHLOW
    0002D02Ch HIGHLOW
    0002D030h HIGHLOW
    0002D034h HIGHLOW
    0002D038h HIGHLOW
    0002D03Ch HIGHLOW
    0002D040h HIGHLOW
    0002D044h HIGHLOW
    0002D048h HIGHLOW
    0002D04Ch HIGHLOW
    0002D050h HIGHLOW
    0002D054h HIGHLOW
    0002D058h HIGHLOW
    0002D05Ch HIGHLOW
    0002D060h HIGHLOW
    0002D064h HIGHLOW
    0002D068h HIGHLOW
    0002D06Ch HIGHLOW
    0002D070h HIGHLOW
    0002D074h HIGHLOW
    0002D078h HIGHLOW
    0002D07Ch HIGHLOW
    0002D080h HIGHLOW
    0002D084h HIGHLOW
    0002D088h HIGHLOW
    0002D08Ch HIGHLOW
    0002D090h HIGHLOW
    0002D094h HIGHLOW
    0002D098h HIGHLOW
    0002D09Ch HIGHLOW
    0002D0A0h HIGHLOW
    0002D0A4h HIGHLOW
    0002D0A8h HIGHLOW
    0002D0ACh HIGHLOW
    0002D0B0h HIGHLOW
    0002D0B4h HIGHLOW
    0002D0B8h HIGHLOW
    0002D0BCh HIGHLOW
    0002D0C0h HIGHLOW
    0002D0C4h HIGHLOW
    0002D0C8h HIGHLOW
    0002D0CCh HIGHLOW
    0002D0D0h HIGHLOW
    0002D0D4h HIGHLOW
    0002D0D8h HIGHLOW
    0002D0DCh HIGHLOW
    0002D0E0h HIGHLOW
    0002D0E4h HIGHLOW
    0002D0E8h HIGHLOW
    0002D0ECh HIGHLOW
    0002D0F0h HIGHLOW
    0002D0F4h HIGHLOW
    0002D0F8h HIGHLOW
    0002D0FCh HIGHLOW
    0002D100h HIGHLOW
    0002D104h HIGHLOW
    0002D108h HIGHLOW
    0002D10Ch HIGHLOW
    0002D110h HIGHLOW
    0002D114h HIGHLOW
    0002D118h HIGHLOW
    0002D11Ch HIGHLOW
    0002D120h HIGHLOW
    0002D124h HIGHLOW
    0002D128h HIGHLOW
    0002D12Ch HIGHLOW
    0002D130h HIGHLOW
    0002D134h HIGHLOW
    0002D138h HIGHLOW
    0002D13Ch HIGHLOW
    0002D140h HIGHLOW
    0002D144h HIGHLOW
    0002D148h HIGHLOW
    0002D14Ch HIGHLOW
    0002D150h HIGHLOW
    0002D154h HIGHLOW
    0002D434h HIGHLOW
    0002D43Ch HIGHLOW
    0002D444h HIGHLOW
    0002D44Ch HIGHLOW
    0002D454h HIGHLOW
    0002D45Ch HIGHLOW
    0002D464h HIGHLOW
    0002D46Ch HIGHLOW
    0002D474h HIGHLOW
    0002D47Ch HIGHLOW
    0002D484h HIGHLOW
    0002D48Ch HIGHLOW
    0002D494h HIGHLOW
    0002D49Ch HIGHLOW
    0002D4A4h HIGHLOW
    0002D4ACh HIGHLOW
    0002D4B4h HIGHLOW
    0002D4BCh HIGHLOW
    0002D4C4h HIGHLOW
    0002D4CCh HIGHLOW
    0002D4D4h HIGHLOW
    0002D4DCh HIGHLOW
    0002D4E4h HIGHLOW
    0002D4ECh HIGHLOW
    0002D4F4h HIGHLOW
    0002D4FCh HIGHLOW
    0002D504h HIGHLOW
    0002D50Ch HIGHLOW
    0002D514h HIGHLOW
    0002D51Ch HIGHLOW
    0002D524h HIGHLOW
    0002D52Ch HIGHLOW
    0002D534h HIGHLOW
    0002D53Ch HIGHLOW
    0002D544h HIGHLOW
    0002D54Ch HIGHLOW
    0002D554h HIGHLOW
    0002D55Ch HIGHLOW
    0002D564h HIGHLOW
    0002D56Ch HIGHLOW
    0002D574h HIGHLOW
    0002D57Ch HIGHLOW
    0002D584h HIGHLOW
    0002D58Ch HIGHLOW
    0002D594h HIGHLOW
    0002D59Ch HIGHLOW
    0002D5A4h HIGHLOW
    0002D5ACh HIGHLOW
    0002D5B4h HIGHLOW
    0002D5BCh HIGHLOW
    0002D5C4h HIGHLOW
    0002D5CCh HIGHLOW
    0002D5D4h HIGHLOW
    0002D5DCh HIGHLOW
    0002D5E4h HIGHLOW
    0002D5ECh HIGHLOW
    0002D5F0h HIGHLOW
    0002D5F4h HIGHLOW
    0002D5F8h HIGHLOW
    0002D5FCh HIGHLOW
    0002D600h HIGHLOW
    0002D604h HIGHLOW
    0002D608h HIGHLOW
    0002D60Ch HIGHLOW
    0002D610h HIGHLOW
    0002D614h HIGHLOW
    0002D618h HIGHLOW
    0002D61Ch HIGHLOW
    0002D6B4h HIGHLOW
    0002D6BCh HIGHLOW
    0002D6C4h HIGHLOW
    0002D6CCh HIGHLOW
    0002D6D4h HIGHLOW
    0002D6DCh HIGHLOW
    0002D6E4h HIGHLOW
    0002D6ECh HIGHLOW
    0002D6F4h HIGHLOW
    0002D6F8h HIGHLOW
    0002D6FCh HIGHLOW
    0002D700h HIGHLOW
    0002D704h HIGHLOW
    0002D708h HIGHLOW
    0002D70Ch HIGHLOW
    0002D710h HIGHLOW
    0002D714h HIGHLOW
    0002D718h HIGHLOW
    0002D71Ch HIGHLOW
    0002D780h HIGHLOW
    0002D784h HIGHLOW
    0002D788h HIGHLOW
    0002D78Ch HIGHLOW
    0002D790h HIGHLOW
    0002D794h HIGHLOW
    0002D798h HIGHLOW
    0002D79Ch HIGHLOW
    0002D7A0h HIGHLOW
    0002D7A4h HIGHLOW
    0002D7A8h HIGHLOW
    0002D7ACh HIGHLOW
    0002D7B0h HIGHLOW
    0002D7B4h HIGHLOW
    0002D7B8h HIGHLOW
    0002D7BCh HIGHLOW
    0002D7C0h HIGHLOW
    0002D7C4h HIGHLOW
    0002D7C8h HIGHLOW
    0002D7CCh HIGHLOW
    0002D7D0h HIGHLOW
    0002D7D4h HIGHLOW
    0002D7D8h HIGHLOW
    0002D7DCh HIGHLOW
    0002D7E0h HIGHLOW
    0002D7E4h HIGHLOW
    0002D7E8h HIGHLOW
    0002D7ECh HIGHLOW
    0002D7F0h HIGHLOW
    0002D7F4h HIGHLOW
    0002D7F8h HIGHLOW
    0002D7FCh HIGHLOW
    0002D800h HIGHLOW
    0002D804h HIGHLOW
    0002D808h HIGHLOW
    0002D80Ch HIGHLOW
    0002D810h HIGHLOW
    0002D814h HIGHLOW
    0002D818h HIGHLOW
    0002D81Ch HIGHLOW
    0002D820h HIGHLOW
    0002D824h HIGHLOW
    0002D828h HIGHLOW
    0002D82Ch HIGHLOW
    0002D830h HIGHLOW
    0002D834h HIGHLOW
    0002D838h HIGHLOW
    0002D83Ch HIGHLOW
    0002D840h HIGHLOW
    0002D844h HIGHLOW
    0002D848h HIGHLOW
    0002D84Ch HIGHLOW
    0002D850h HIGHLOW
    0002D854h HIGHLOW
    0002D858h HIGHLOW
    0002D85Ch HIGHLOW
    0002D860h HIGHLOW
    0002D864h HIGHLOW
    0002D868h HIGHLOW
    0002D86Ch HIGHLOW
    0002D870h HIGHLOW
    0002D874h HIGHLOW
    0002D878h HIGHLOW
    0002D87Ch HIGHLOW
    0002D880h HIGHLOW
    0002D884h HIGHLOW
    0002D888h HIGHLOW
    0002D88Ch HIGHLOW
    0002D890h HIGHLOW
    0002D894h HIGHLOW
    0002D898h HIGHLOW
    0002D89Ch HIGHLOW
    0002D8A0h HIGHLOW
    0002D8A4h HIGHLOW
    0002D8A8h HIGHLOW
    0002D8ACh HIGHLOW
    0002D8B0h HIGHLOW
    0002D8B4h HIGHLOW
    0002D8B8h HIGHLOW
    0002D8BCh HIGHLOW
    0002D8C0h HIGHLOW
    0002D8C4h HIGHLOW
    0002D8C8h HIGHLOW
    0002D8CCh HIGHLOW
    0002D8D0h HIGHLOW
    0002D8D4h HIGHLOW
    0002D8D8h HIGHLOW
    0002D8DCh HIGHLOW
    0002D8E0h HIGHLOW
    0002D8E4h HIGHLOW
    0002D8E8h HIGHLOW
    0002D8ECh HIGHLOW
    0002D8F0h HIGHLOW
    0002D8F4h HIGHLOW
    0002D8F8h HIGHLOW
    0002D8FCh HIGHLOW
    0002D900h HIGHLOW
    0002D904h HIGHLOW
    0002D908h HIGHLOW
    0002D90Ch HIGHLOW
    0002D910h HIGHLOW
    0002D914h HIGHLOW
    0002D918h HIGHLOW
    0002D91Ch HIGHLOW
    0002D920h HIGHLOW
    0002D924h HIGHLOW
    0002D928h HIGHLOW
    0002D92Ch HIGHLOW
    0002D930h HIGHLOW
    0002D934h HIGHLOW
    0002D938h HIGHLOW
    0002D93Ch HIGHLOW
    0002D940h HIGHLOW
    0002D944h HIGHLOW
    0002D948h HIGHLOW
    0002D94Ch HIGHLOW
    0002D950h HIGHLOW
    0002D954h HIGHLOW
    0002D958h HIGHLOW
    0002D95Ch HIGHLOW
    0002D960h HIGHLOW
    0002D964h HIGHLOW
    0002D968h HIGHLOW
    0002D96Ch HIGHLOW
    0002D970h HIGHLOW
    0002D974h HIGHLOW
    0002D978h HIGHLOW
    0002D97Ch HIGHLOW
    0002D980h HIGHLOW
    0002D984h HIGHLOW
    0002D988h HIGHLOW
    0002D98Ch HIGHLOW
    0002D990h HIGHLOW
    0002D994h HIGHLOW
    0002D998h HIGHLOW
    0002D99Ch HIGHLOW
    0002D9A0h HIGHLOW
    0002D9A4h HIGHLOW
    0002D9A8h HIGHLOW
    0002D9ACh HIGHLOW
    0002D9B0h HIGHLOW
    0002D9B4h HIGHLOW
    0002D9B8h HIGHLOW
    0002D9BCh HIGHLOW
    0002D9C0h HIGHLOW
    0002D9C4h HIGHLOW
    0002D9C8h HIGHLOW
    0002D9CCh HIGHLOW
    0002D9D0h HIGHLOW
    0002D9D4h HIGHLOW
    0002D9D8h HIGHLOW
    0002D9DCh HIGHLOW
    0002D9E0h HIGHLOW
    0002D9E4h HIGHLOW
    0002D9E8h HIGHLOW
    0002D9ECh HIGHLOW
    0002D9F0h HIGHLOW
    0002D9F4h HIGHLOW
    0002D9F8h HIGHLOW
    0002D9FCh HIGHLOW
    0002DA00h HIGHLOW
    0002DA04h HIGHLOW
    0002DA08h HIGHLOW
    0002DA0Ch HIGHLOW
    0002DA10h HIGHLOW
    0002DA14h HIGHLOW
    0002DA18h HIGHLOW
    0002DA1Ch HIGHLOW
    0002DA20h HIGHLOW
    0002DA24h HIGHLOW
    0002DA28h HIGHLOW
    0002DA2Ch HIGHLOW
    0002DA30h HIGHLOW
    0002DA34h HIGHLOW
    0002DA38h HIGHLOW
    0002DA3Ch HIGHLOW
    0002DA40h HIGHLOW
    0002DA44h HIGHLOW
    0002DA48h HIGHLOW
    0002DA4Ch HIGHLOW
    0002DA50h HIGHLOW
    0002DA54h HIGHLOW
    0002DA58h HIGHLOW
    0002DA5Ch HIGHLOW
    0002DA60h HIGHLOW
    0002DA64h HIGHLOW
    0002DA68h HIGHLOW
    0002DA6Ch HIGHLOW
    0002DA70h HIGHLOW
    0002DA74h HIGHLOW
    0002DA78h HIGHLOW
    0002DA7Ch HIGHLOW
    0002DA80h HIGHLOW
    0002DA84h HIGHLOW
    0002DA88h HIGHLOW
    0002DA8Ch HIGHLOW
    0002DA90h HIGHLOW
    0002DA94h HIGHLOW
    0002DA98h HIGHLOW
    0002DA9Ch HIGHLOW
    0002DAA0h HIGHLOW
    0002DAA4h HIGHLOW
    0002DAA8h HIGHLOW
    0002DAACh HIGHLOW
    0002DAB0h HIGHLOW
    0002DAB4h HIGHLOW
    0002DAB8h HIGHLOW
    0002DABCh HIGHLOW
    0002DAC0h HIGHLOW
    0002DAC4h HIGHLOW
    0002DAC8h HIGHLOW
    0002DACCh HIGHLOW
    0002DAD0h HIGHLOW
    0002DAD4h HIGHLOW
    0002DAD8h HIGHLOW
    0002DADCh HIGHLOW
    0002D000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2E000   
SizeOfBlock:                   0x168     
    0002E580h HIGHLOW
    0002E584h HIGHLOW
    0002E588h HIGHLOW
    0002E58Ch HIGHLOW
    0002E590h HIGHLOW
    0002E594h HIGHLOW
    0002E598h HIGHLOW
    0002E59Ch HIGHLOW
    0002E5A0h HIGHLOW
    0002E5A4h HIGHLOW
    0002E5A8h HIGHLOW
    0002E5ACh HIGHLOW
    0002E5B0h HIGHLOW
    0002E5B4h HIGHLOW
    0002E5B8h HIGHLOW
    0002E5BCh HIGHLOW
    0002E5C0h HIGHLOW
    0002E5C4h HIGHLOW
    0002E5C8h HIGHLOW
    0002E5CCh HIGHLOW
    0002E5D0h HIGHLOW
    0002E5D4h HIGHLOW
    0002E5D8h HIGHLOW
    0002E5DCh HIGHLOW
    0002E5E0h HIGHLOW
    0002E5E4h HIGHLOW
    0002E5E8h HIGHLOW
    0002E5ECh HIGHLOW
    0002E748h HIGHLOW
    0002E74Ch HIGHLOW
    0002E750h HIGHLOW
    0002E754h HIGHLOW
    0002E758h HIGHLOW
    0002E75Ch HIGHLOW
    0002E760h HIGHLOW
    0002E764h HIGHLOW
    0002E768h HIGHLOW
    0002E76Ch HIGHLOW
    0002E770h HIGHLOW
    0002E774h HIGHLOW
    0002E778h HIGHLOW
    0002E77Ch HIGHLOW
    0002E840h HIGHLOW
    0002E844h HIGHLOW
    0002E848h HIGHLOW
    0002E84Ch HIGHLOW
    0002E850h HIGHLOW
    0002E854h HIGHLOW
    0002E858h HIGHLOW
    0002E85Ch HIGHLOW
    0002E860h HIGHLOW
    0002E864h HIGHLOW
    0002E868h HIGHLOW
    0002E86Ch HIGHLOW
    0002E870h HIGHLOW
    0002E874h HIGHLOW
    0002E878h HIGHLOW
    0002E87Ch HIGHLOW
    0002E880h HIGHLOW
    0002E884h HIGHLOW
    0002E888h HIGHLOW
    0002E88Ch HIGHLOW
    0002E890h HIGHLOW
    0002E894h HIGHLOW
    0002E898h HIGHLOW
    0002E89Ch HIGHLOW
    0002E8A0h HIGHLOW
    0002E8A4h HIGHLOW
    0002E8A8h HIGHLOW
    0002E8ACh HIGHLOW
    0002E8B0h HIGHLOW
    0002E8B4h HIGHLOW
    0002E8B8h HIGHLOW
    0002E8BCh HIGHLOW
    0002E8C0h HIGHLOW
    0002E8C4h HIGHLOW
    0002E8C8h HIGHLOW
    0002E8CCh HIGHLOW
    0002E8D0h HIGHLOW
    0002E8D4h HIGHLOW
    0002E8D8h HIGHLOW
    0002E8DCh HIGHLOW
    0002E8E0h HIGHLOW
    0002E8E4h HIGHLOW
    0002E8E8h HIGHLOW
    0002E8ECh HIGHLOW
    0002E8F0h HIGHLOW
    0002E8F4h HIGHLOW
    0002E8F8h HIGHLOW
    0002E8FCh HIGHLOW
    0002E900h HIGHLOW
    0002E904h HIGHLOW
    0002E908h HIGHLOW
    0002E90Ch HIGHLOW
    0002E910h HIGHLOW
    0002E914h HIGHLOW
    0002E918h HIGHLOW
    0002E91Ch HIGHLOW
    0002E920h HIGHLOW
    0002E924h HIGHLOW
    0002E928h HIGHLOW
    0002E92Ch HIGHLOW
    0002E930h HIGHLOW
    0002E934h HIGHLOW
    0002E938h HIGHLOW
    0002E93Ch HIGHLOW
    0002E940h HIGHLOW
    0002E944h HIGHLOW
    0002E948h HIGHLOW
    0002E94Ch HIGHLOW
    0002E950h HIGHLOW
    0002E954h HIGHLOW
    0002E958h HIGHLOW
    0002E95Ch HIGHLOW
    0002E960h HIGHLOW
    0002E964h HIGHLOW
    0002E968h HIGHLOW
    0002E96Ch HIGHLOW
    0002E970h HIGHLOW
    0002E974h HIGHLOW
    0002E978h HIGHLOW
    0002E97Ch HIGHLOW
    0002E980h HIGHLOW
    0002E984h HIGHLOW
    0002E988h HIGHLOW
    0002E98Ch HIGHLOW
    0002E990h HIGHLOW
    0002E994h HIGHLOW
    0002E998h HIGHLOW
    0002E99Ch HIGHLOW
    0002ED9Ch HIGHLOW
    0002EDA0h HIGHLOW
    0002EDA4h HIGHLOW
    0002EDA8h HIGHLOW
    0002EDACh HIGHLOW
    0002EDB0h HIGHLOW
    0002EDB4h HIGHLOW
    0002EDB8h HIGHLOW
    0002EDBCh HIGHLOW
    0002EDC0h HIGHLOW
    0002EDC4h HIGHLOW
    0002EDC8h HIGHLOW
    0002EDCCh HIGHLOW
    0002EDD0h HIGHLOW
    0002EE58h HIGHLOW
    0002EE5Ch HIGHLOW
    0002EE60h HIGHLOW
    0002EE64h HIGHLOW
    0002EE68h HIGHLOW
    0002EE6Ch HIGHLOW
    0002EEA0h HIGHLOW
    0002EEA4h HIGHLOW
    0002EEA8h HIGHLOW
    0002EEACh HIGHLOW
    0002EEB0h HIGHLOW
    0002EEB4h HIGHLOW
    0002EEB8h HIGHLOW
    0002EEBCh HIGHLOW
    0002EEC0h HIGHLOW
    0002EEC4h HIGHLOW
    0002EEC8h HIGHLOW
    0002EECCh HIGHLOW
    0002EED0h HIGHLOW
    0002EED4h HIGHLOW
    0002EED8h HIGHLOW
    0002EEDCh HIGHLOW
    0002EEE0h HIGHLOW
    0002EEE4h HIGHLOW
    0002EEE8h HIGHLOW
    0002EEECh HIGHLOW
    0002EEF0h HIGHLOW
    0002EEF4h HIGHLOW
    0002EEF8h HIGHLOW
    0002EEFCh HIGHLOW
    0002EF00h HIGHLOW
    0002EF04h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x2F000   
SizeOfBlock:                   0x2D0     
    0002F04Ch HIGHLOW
    0002F050h HIGHLOW
    0002F054h HIGHLOW
    0002F058h HIGHLOW
    0002F080h HIGHLOW
    0002F084h HIGHLOW
    0002F088h HIGHLOW
    0002F08Ch HIGHLOW
    0002F090h HIGHLOW
    0002F094h HIGHLOW
    0002F098h HIGHLOW
    0002F09Ch HIGHLOW
    0002F0A0h HIGHLOW
    0002F0A4h HIGHLOW
    0002F0A8h HIGHLOW
    0002F0ACh HIGHLOW
    0002F0B0h HIGHLOW
    0002F0B4h HIGHLOW
    0002F0B8h HIGHLOW
    0002F0BCh HIGHLOW
    0002F0C0h HIGHLOW
    0002F0C4h HIGHLOW
    0002F0C8h HIGHLOW
    0002F0CCh HIGHLOW
    0002F0D0h HIGHLOW
    0002F0D4h HIGHLOW
    0002F0D8h HIGHLOW
    0002F0DCh HIGHLOW
    0002F0E0h HIGHLOW
    0002F0E4h HIGHLOW
    0002F0E8h HIGHLOW
    0002F0ECh HIGHLOW
    0002F0F0h HIGHLOW
    0002F0F4h HIGHLOW
    0002F0F8h HIGHLOW
    0002F0FCh HIGHLOW
    0002F100h HIGHLOW
    0002F104h HIGHLOW
    0002F108h HIGHLOW
    0002F10Ch HIGHLOW
    0002F110h HIGHLOW
    0002F114h HIGHLOW
    0002F118h HIGHLOW
    0002F11Ch HIGHLOW
    0002F120h HIGHLOW
    0002F124h HIGHLOW
    0002F128h HIGHLOW
    0002F12Ch HIGHLOW
    0002F328h HIGHLOW
    0002F32Ch HIGHLOW
    0002F330h HIGHLOW
    0002F334h HIGHLOW
    0002F338h HIGHLOW
    0002F33Ch HIGHLOW
    0002F340h HIGHLOW
    0002F344h HIGHLOW
    0002F348h HIGHLOW
    0002F34Ch HIGHLOW
    0002F350h HIGHLOW
    0002F354h HIGHLOW
    0002F358h HIGHLOW
    0002F35Ch HIGHLOW
    0002F360h HIGHLOW
    0002F364h HIGHLOW
    0002F368h HIGHLOW
    0002F36Ch HIGHLOW
    0002F370h HIGHLOW
    0002F374h HIGHLOW
    0002F378h HIGHLOW
    0002F37Ch HIGHLOW
    0002F380h HIGHLOW
    0002F384h HIGHLOW
    0002F388h HIGHLOW
    0002F38Ch HIGHLOW
    0002F390h HIGHLOW
    0002F394h HIGHLOW
    0002F398h HIGHLOW
    0002F39Ch HIGHLOW
    0002F3A0h HIGHLOW
    0002F3A4h HIGHLOW
    0002F3A8h HIGHLOW
    0002F3ACh HIGHLOW
    0002F3B0h HIGHLOW
    0002F3B4h HIGHLOW
    0002F3B8h HIGHLOW
    0002F3BCh HIGHLOW
    0002F3C0h HIGHLOW
    0002F3C4h HIGHLOW
    0002F3C8h HIGHLOW
    0002F3CCh HIGHLOW
    0002F3D0h HIGHLOW
    0002F3D4h HIGHLOW
    0002F5C0h HIGHLOW
    0002F5C4h HIGHLOW
    0002F5C8h HIGHLOW
    0002F5CCh HIGHLOW
    0002F5D0h HIGHLOW
    0002F5D4h HIGHLOW
    0002F5D8h HIGHLOW
    0002F5DCh HIGHLOW
    0002F5E0h HIGHLOW
    0002F5E4h HIGHLOW
    0002F630h HIGHLOW
    0002F634h HIGHLOW
    0002F650h HIGHLOW
    0002F654h HIGHLOW
    0002F658h HIGHLOW
    0002F65Ch HIGHLOW
    0002F660h HIGHLOW
    0002F664h HIGHLOW
    0002F668h HIGHLOW
    0002F66Ch HIGHLOW
    0002F670h HIGHLOW
    0002F674h HIGHLOW
    0002F678h HIGHLOW
    0002F67Ch HIGHLOW
    0002F680h HIGHLOW
    0002F684h HIGHLOW
    0002F688h HIGHLOW
    0002F68Ch HIGHLOW
    0002F690h HIGHLOW
    0002F694h HIGHLOW
    0002F698h HIGHLOW
    0002F69Ch HIGHLOW
    0002F6A0h HIGHLOW
    0002F6A4h HIGHLOW
    0002F6A8h HIGHLOW
    0002F6ACh HIGHLOW
    0002F798h HIGHLOW
    0002F79Ch HIGHLOW
    0002F7A0h HIGHLOW
    0002F7A4h HIGHLOW
    0002F7A8h HIGHLOW
    0002F7ACh HIGHLOW
    0002F7B0h HIGHLOW
    0002F7B4h HIGHLOW
    0002F7B8h HIGHLOW
    0002F7BCh HIGHLOW
    0002F7C0h HIGHLOW
    0002F7C4h HIGHLOW
    0002F7C8h HIGHLOW
    0002F7CCh HIGHLOW
    0002F860h HIGHLOW
    0002F864h HIGHLOW
    0002F868h HIGHLOW
    0002F884h HIGHLOW
    0002F88Ch HIGHLOW
    0002F894h HIGHLOW
    0002F89Ch HIGHLOW
    0002F8A4h HIGHLOW
    0002F8ACh HIGHLOW
    0002F8B4h HIGHLOW
    0002F8BCh HIGHLOW
    0002F8C4h HIGHLOW
    0002F8CCh HIGHLOW
    0002F8D4h HIGHLOW
    0002F8DCh HIGHLOW
    0002F8E4h HIGHLOW
    0002F8ECh HIGHLOW
    0002F8F4h HIGHLOW
    0002F8FCh HIGHLOW
    0002F904h HIGHLOW
    0002F90Ch HIGHLOW
    0002F914h HIGHLOW
    0002F91Ch HIGHLOW
    0002F924h HIGHLOW
    0002F92Ch HIGHLOW
    0002F934h HIGHLOW
    0002F93Ch HIGHLOW
    0002F944h HIGHLOW
    0002F94Ch HIGHLOW
    0002F954h HIGHLOW
    0002F95Ch HIGHLOW
    0002F964h HIGHLOW
    0002F96Ch HIGHLOW
    0002F974h HIGHLOW
    0002F97Ch HIGHLOW
    0002F984h HIGHLOW
    0002F98Ch HIGHLOW
    0002F994h HIGHLOW
    0002F99Ch HIGHLOW
    0002F9A4h HIGHLOW
    0002F9ACh HIGHLOW
    0002F9B4h HIGHLOW
    0002F9BCh HIGHLOW
    0002F9C4h HIGHLOW
    0002F9C8h HIGHLOW
    0002F9CCh HIGHLOW
    0002F9D0h HIGHLOW
    0002F9D4h HIGHLOW
    0002F9D8h HIGHLOW
    0002F9DCh HIGHLOW
    0002F9E0h HIGHLOW
    0002F9E4h HIGHLOW
    0002FA48h HIGHLOW
    0002FA4Ch HIGHLOW
    0002FA50h HIGHLOW
    0002FA54h HIGHLOW
    0002FA58h HIGHLOW
    0002FA5Ch HIGHLOW
    0002FA60h HIGHLOW
    0002FA64h HIGHLOW
    0002FA68h HIGHLOW
    0002FA6Ch HIGHLOW
    0002FA70h HIGHLOW
    0002FA74h HIGHLOW
    0002FA78h HIGHLOW
    0002FA7Ch HIGHLOW
    0002FA80h HIGHLOW
    0002FA84h HIGHLOW
    0002FA88h HIGHLOW
    0002FA8Ch HIGHLOW
    0002FA90h HIGHLOW
    0002FA94h HIGHLOW
    0002FA98h HIGHLOW
    0002FA9Ch HIGHLOW
    0002FAA0h HIGHLOW
    0002FAA4h HIGHLOW
    0002FAA8h HIGHLOW
    0002FAACh HIGHLOW
    0002FAB0h HIGHLOW
    0002FAB4h HIGHLOW
    0002FAB8h HIGHLOW
    0002FABCh HIGHLOW
    0002FAC0h HIGHLOW
    0002FAC4h HIGHLOW
    0002FAC8h HIGHLOW
    0002FACCh HIGHLOW
    0002FAD0h HIGHLOW
    0002FAD4h HIGHLOW
    0002FAD8h HIGHLOW
    0002FADCh HIGHLOW
    0002FAE0h HIGHLOW
    0002FAE4h HIGHLOW
    0002FAE8h HIGHLOW
    0002FAECh HIGHLOW
    0002FAF0h HIGHLOW
    0002FAF4h HIGHLOW
    0002FAF8h HIGHLOW
    0002FAFCh HIGHLOW
    0002FB00h HIGHLOW
    0002FB04h HIGHLOW
    0002FB08h HIGHLOW
    0002FB0Ch HIGHLOW
    0002FB10h HIGHLOW
    0002FB14h HIGHLOW
    0002FB18h HIGHLOW
    0002FB1Ch HIGHLOW
    0002FB20h HIGHLOW
    0002FB24h HIGHLOW
    0002FB28h HIGHLOW
    0002FB2Ch HIGHLOW
    0002FB30h HIGHLOW
    0002FB34h HIGHLOW
    0002FB38h HIGHLOW
    0002FB3Ch HIGHLOW
    0002FB40h HIGHLOW
    0002FB44h HIGHLOW
    0002FB48h HIGHLOW
    0002FB4Ch HIGHLOW
    0002FB50h HIGHLOW
    0002FB54h HIGHLOW
    0002FB58h HIGHLOW
    0002FB5Ch HIGHLOW
    0002FB60h HIGHLOW
    0002FB64h HIGHLOW
    0002FB68h HIGHLOW
    0002FB6Ch HIGHLOW
    0002FB70h HIGHLOW
    0002FB74h HIGHLOW
    0002FB78h HIGHLOW
    0002FB7Ch HIGHLOW
    0002FB80h HIGHLOW
    0002FB84h HIGHLOW
    0002FB88h HIGHLOW
    0002FB8Ch HIGHLOW
    0002FB90h HIGHLOW
    0002FB94h HIGHLOW
    0002FB98h HIGHLOW
    0002FB9Ch HIGHLOW
    0002FBA0h HIGHLOW
    0002FBA4h HIGHLOW
    0002FBA8h HIGHLOW
    0002FBACh HIGHLOW
    0002FBB0h HIGHLOW
    0002FBB4h HIGHLOW
    0002FBB8h HIGHLOW
    0002FBBCh HIGHLOW
    0002FBC0h HIGHLOW
    0002FBC4h HIGHLOW
    0002FBC8h HIGHLOW
    0002FBCCh HIGHLOW
    0002FBD0h HIGHLOW
    0002FBD4h HIGHLOW
    0002FBD8h HIGHLOW
    0002FBDCh HIGHLOW
    0002FBE0h HIGHLOW
    0002FBE4h HIGHLOW
    0002FBE8h HIGHLOW
    0002FBECh HIGHLOW
    0002FBF0h HIGHLOW
    0002FBF4h HIGHLOW
    0002FBF8h HIGHLOW
    0002FBFCh HIGHLOW
    0002FC00h HIGHLOW
    0002FC04h HIGHLOW
    0002FC08h HIGHLOW
    0002FC0Ch HIGHLOW
    0002FC10h HIGHLOW
    0002FC14h HIGHLOW
    0002FC18h HIGHLOW
    0002FC1Ch HIGHLOW
    0002FC20h HIGHLOW
    0002FC24h HIGHLOW
    0002FC28h HIGHLOW
    0002FC2Ch HIGHLOW
    0002FC30h HIGHLOW
    0002FC34h HIGHLOW
    0002FC38h HIGHLOW
    0002FC3Ch HIGHLOW
    0002FC40h HIGHLOW
    0002FC44h HIGHLOW
    0002FC48h HIGHLOW
    0002FC4Ch HIGHLOW
    0002FC50h HIGHLOW
    0002FC54h HIGHLOW
    0002FC58h HIGHLOW
    0002FC5Ch HIGHLOW
    0002FC60h HIGHLOW
    0002FC64h HIGHLOW
    0002FC68h HIGHLOW
    0002FC6Ch HIGHLOW
    0002FC70h HIGHLOW
    0002FC74h HIGHLOW
    0002FC78h HIGHLOW
    0002FC7Ch HIGHLOW
    0002FC80h HIGHLOW
    0002FC84h HIGHLOW
    0002FC88h HIGHLOW
    0002FC8Ch HIGHLOW
    0002FC90h HIGHLOW
    0002FC94h HIGHLOW
    0002FC98h HIGHLOW
    0002FC9Ch HIGHLOW
    0002FCA0h HIGHLOW
    0002FCA4h HIGHLOW
    0002FCA8h HIGHLOW
    0002FCACh HIGHLOW
    0002FCB0h HIGHLOW
    0002FCB4h HIGHLOW
    0002FCB8h HIGHLOW
    0002FCBCh HIGHLOW
    0002FCC0h HIGHLOW
    0002FCC4h HIGHLOW
    0002FCC8h HIGHLOW
    0002FCCCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x30000   
SizeOfBlock:                   0x1E8     
    0003032Ch HIGHLOW
    00030334h HIGHLOW
    0003033Ch HIGHLOW
    00030344h HIGHLOW
    0003034Ch HIGHLOW
    00030354h HIGHLOW
    0003035Ch HIGHLOW
    00030364h HIGHLOW
    0003036Ch HIGHLOW
    00030374h HIGHLOW
    00030378h HIGHLOW
    0003037Ch HIGHLOW
    00030380h HIGHLOW
    00030384h HIGHLOW
    00030388h HIGHLOW
    0003038Ch HIGHLOW
    00030390h HIGHLOW
    00030394h HIGHLOW
    00030398h HIGHLOW
    0003039Ch HIGHLOW
    000303A0h HIGHLOW
    000303A4h HIGHLOW
    000303A8h HIGHLOW
    000303ACh HIGHLOW
    0003043Ch HIGHLOW
    00030440h HIGHLOW
    00030460h HIGHLOW
    00030464h HIGHLOW
    00030468h HIGHLOW
    0003046Ch HIGHLOW
    00030494h HIGHLOW
    00030498h HIGHLOW
    0003049Ch HIGHLOW
    000304A0h HIGHLOW
    000304E0h HIGHLOW
    000304E4h HIGHLOW
    000304E8h HIGHLOW
    000304ECh HIGHLOW
    000304F0h HIGHLOW
    000304F4h HIGHLOW
    000304F8h HIGHLOW
    000304FCh HIGHLOW
    00030500h HIGHLOW
    00030504h HIGHLOW
    00030508h HIGHLOW
    0003050Ch HIGHLOW
    00030510h HIGHLOW
    00030514h HIGHLOW
    00030518h HIGHLOW
    0003051Ch HIGHLOW
    00030520h HIGHLOW
    00030524h HIGHLOW
    00030528h HIGHLOW
    0003052Ch HIGHLOW
    000305E8h HIGHLOW
    000305ECh HIGHLOW
    000305F0h HIGHLOW
    000305F4h HIGHLOW
    000305F8h HIGHLOW
    000305FCh HIGHLOW
    00030600h HIGHLOW
    00030604h HIGHLOW
    00030608h HIGHLOW
    0003060Ch HIGHLOW
    00030610h HIGHLOW
    00030614h HIGHLOW
    00030618h HIGHLOW
    0003061Ch HIGHLOW
    00030620h HIGHLOW
    00030624h HIGHLOW
    00030628h HIGHLOW
    0003062Ch HIGHLOW
    00030630h HIGHLOW
    00030634h HIGHLOW
    00030638h HIGHLOW
    0003063Ch HIGHLOW
    00030640h HIGHLOW
    00030644h HIGHLOW
    00030648h HIGHLOW
    0003064Ch HIGHLOW
    00030650h HIGHLOW
    00030654h HIGHLOW
    00030658h HIGHLOW
    0003065Ch HIGHLOW
    00030660h HIGHLOW
    00030664h HIGHLOW
    00030668h HIGHLOW
    0003066Ch HIGHLOW
    00030670h HIGHLOW
    00030674h HIGHLOW
    00030678h HIGHLOW
    0003067Ch HIGHLOW
    00030680h HIGHLOW
    00030684h HIGHLOW
    00030688h HIGHLOW
    0003068Ch HIGHLOW
    00030690h HIGHLOW
    00030694h HIGHLOW
    00030698h HIGHLOW
    0003069Ch HIGHLOW
    000306A0h HIGHLOW
    000306A4h HIGHLOW
    000306A8h HIGHLOW
    000306ACh HIGHLOW
    000306B0h HIGHLOW
    000306B4h HIGHLOW
    000306B8h HIGHLOW
    000306BCh HIGHLOW
    000306C0h HIGHLOW
    000306C4h HIGHLOW
    000306C8h HIGHLOW
    000306CCh HIGHLOW
    000306D0h HIGHLOW
    000306D4h HIGHLOW
    000306D8h HIGHLOW
    000306DCh HIGHLOW
    000306E0h HIGHLOW
    000306E4h HIGHLOW
    000306E8h HIGHLOW
    000306ECh HIGHLOW
    000306F0h HIGHLOW
    000306F4h HIGHLOW
    000306F8h HIGHLOW
    000306FCh HIGHLOW
    00030700h HIGHLOW
    00030704h HIGHLOW
    00030708h HIGHLOW
    0003070Ch HIGHLOW
    00030710h HIGHLOW
    00030714h HIGHLOW
    00030718h HIGHLOW
    0003071Ch HIGHLOW
    00030720h HIGHLOW
    00030724h HIGHLOW
    00030728h HIGHLOW
    0003072Ch HIGHLOW
    00030730h HIGHLOW
    00030734h HIGHLOW
    00030738h HIGHLOW
    0003073Ch HIGHLOW
    00030740h HIGHLOW
    00030744h HIGHLOW
    00030748h HIGHLOW
    0003074Ch HIGHLOW
    00030750h HIGHLOW
    00030754h HIGHLOW
    00030758h HIGHLOW
    0003075Ch HIGHLOW
    00030760h HIGHLOW
    00030764h HIGHLOW
    00030768h HIGHLOW
    0003076Ch HIGHLOW
    00030770h HIGHLOW
    00030774h HIGHLOW
    00030778h HIGHLOW
    0003077Ch HIGHLOW
    00030780h HIGHLOW
    00030784h HIGHLOW
    00030788h HIGHLOW
    0003078Ch HIGHLOW
    00030790h HIGHLOW
    00030794h HIGHLOW
    00030798h HIGHLOW
    0003079Ch HIGHLOW
    000307A0h HIGHLOW
    000307A4h HIGHLOW
    000307A8h HIGHLOW
    000307ACh HIGHLOW
    000307B0h HIGHLOW
    000307B4h HIGHLOW
    000307B8h HIGHLOW
    000307BCh HIGHLOW
    000307C0h HIGHLOW
    000307C4h HIGHLOW
    000307C8h HIGHLOW
    000307CCh HIGHLOW
    000307D0h HIGHLOW
    000307D4h HIGHLOW
    000307D8h HIGHLOW
    000307DCh HIGHLOW
    000307E0h HIGHLOW
    000307E4h HIGHLOW
    000307E8h HIGHLOW
    000307ECh HIGHLOW
    000307F0h HIGHLOW
    000307F4h HIGHLOW
    000307F8h HIGHLOW
    000307FCh HIGHLOW
    00030800h HIGHLOW
    00030804h HIGHLOW
    00030808h HIGHLOW
    0003080Ch HIGHLOW
    00030810h HIGHLOW
    00030814h HIGHLOW
    00030818h HIGHLOW
    0003081Ch HIGHLOW
    00030820h HIGHLOW
    00030824h HIGHLOW
    00030828h HIGHLOW
    0003082Ch HIGHLOW
    00030830h HIGHLOW
    00030834h HIGHLOW
    00030838h HIGHLOW
    0003083Ch HIGHLOW
    00030DE8h HIGHLOW
    00030DECh HIGHLOW
    00030DF0h HIGHLOW
    00030DF4h HIGHLOW
    00030E30h HIGHLOW
    00030E34h HIGHLOW
    00030E38h HIGHLOW
    00030E3Ch HIGHLOW
    00030E40h HIGHLOW
    00030E44h HIGHLOW
    00030E48h HIGHLOW
    00030E4Ch HIGHLOW
    00030E50h HIGHLOW
    00030E54h HIGHLOW
    00030E58h HIGHLOW
    00030E5Ch HIGHLOW
    00030E60h HIGHLOW
    00030E64h HIGHLOW
    00030E68h HIGHLOW
    00030E6Ch HIGHLOW
    00030E70h HIGHLOW
    00030E74h HIGHLOW
    00030E78h HIGHLOW
    00030E7Ch HIGHLOW
    00030E80h HIGHLOW
    00030E84h HIGHLOW
    00030E88h HIGHLOW
    00030E8Ch HIGHLOW
    00030F88h HIGHLOW
    00030F8Ch HIGHLOW
    00030F90h HIGHLOW
    00030F94h HIGHLOW
    00030FC8h HIGHLOW
    00030FCCh HIGHLOW
    00030FD0h HIGHLOW
    00030FD4h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x31000   
SizeOfBlock:                   0x254     
    00031018h HIGHLOW
    0003101Ch HIGHLOW
    00031020h HIGHLOW
    00031024h HIGHLOW
    00031028h HIGHLOW
    0003102Ch HIGHLOW
    00031030h HIGHLOW
    00031034h HIGHLOW
    00031038h HIGHLOW
    0003103Ch HIGHLOW
    00031040h HIGHLOW
    00031044h HIGHLOW
    00031048h HIGHLOW
    0003104Ch HIGHLOW
    00031050h HIGHLOW
    00031054h HIGHLOW
    00031058h HIGHLOW
    0003105Ch HIGHLOW
    00031060h HIGHLOW
    00031064h HIGHLOW
    00031068h HIGHLOW
    0003106Ch HIGHLOW
    00031070h HIGHLOW
    00031074h HIGHLOW
    00031078h HIGHLOW
    0003107Ch HIGHLOW
    00031080h HIGHLOW
    00031084h HIGHLOW
    00031088h HIGHLOW
    0003108Ch HIGHLOW
    00031090h HIGHLOW
    00031094h HIGHLOW
    00031098h HIGHLOW
    0003109Ch HIGHLOW
    000310A0h HIGHLOW
    000310A4h HIGHLOW
    000310A8h HIGHLOW
    000310ACh HIGHLOW
    000310B0h HIGHLOW
    000310B4h HIGHLOW
    000310B8h HIGHLOW
    000310BCh HIGHLOW
    000310C0h HIGHLOW
    000310C4h HIGHLOW
    000310C8h HIGHLOW
    000310CCh HIGHLOW
    000310D0h HIGHLOW
    000310D4h HIGHLOW
    000310D8h HIGHLOW
    000310DCh HIGHLOW
    000310E0h HIGHLOW
    000310E4h HIGHLOW
    000310E8h HIGHLOW
    000310ECh HIGHLOW
    000310F0h HIGHLOW
    000310F4h HIGHLOW
    000310F8h HIGHLOW
    000310FCh HIGHLOW
    00031100h HIGHLOW
    00031104h HIGHLOW
    00031108h HIGHLOW
    0003110Ch HIGHLOW
    00031110h HIGHLOW
    00031114h HIGHLOW
    00031118h HIGHLOW
    0003111Ch HIGHLOW
    00031120h HIGHLOW
    00031124h HIGHLOW
    00031128h HIGHLOW
    0003112Ch HIGHLOW
    00031130h HIGHLOW
    00031134h HIGHLOW
    00031138h HIGHLOW
    0003113Ch HIGHLOW
    00031140h HIGHLOW
    00031144h HIGHLOW
    00031148h HIGHLOW
    0003114Ch HIGHLOW
    00031150h HIGHLOW
    00031154h HIGHLOW
    00031488h HIGHLOW
    0003148Ch HIGHLOW
    000314B0h HIGHLOW
    000314B4h HIGHLOW
    000314B8h HIGHLOW
    000314BCh HIGHLOW
    000314C0h HIGHLOW
    000314C4h HIGHLOW
    000314C8h HIGHLOW
    000314CCh HIGHLOW
    000314D0h HIGHLOW
    000314D4h HIGHLOW
    000314D8h HIGHLOW
    000314DCh HIGHLOW
    000314E0h HIGHLOW
    000314E4h HIGHLOW
    000314E8h HIGHLOW
    000314ECh HIGHLOW
    00031598h HIGHLOW
    0003159Ch HIGHLOW
    000315A0h HIGHLOW
    000315A4h HIGHLOW
    000315A8h HIGHLOW
    000315ACh HIGHLOW
    000315B0h HIGHLOW
    000315B4h HIGHLOW
    000315B8h HIGHLOW
    000315BCh HIGHLOW
    000315C0h HIGHLOW
    000315C4h HIGHLOW
    000315C8h HIGHLOW
    000315CCh HIGHLOW
    000315D0h HIGHLOW
    000315D4h HIGHLOW
    00031694h HIGHLOW
    00031698h HIGHLOW
    0003169Ch HIGHLOW
    000316A0h HIGHLOW
    000316A4h HIGHLOW
    000316A8h HIGHLOW
    000316DCh HIGHLOW
    000316E4h HIGHLOW
    000316ECh HIGHLOW
    000316F4h HIGHLOW
    000316FCh HIGHLOW
    00031700h HIGHLOW
    00031704h HIGHLOW
    00031708h HIGHLOW
    0003170Ch HIGHLOW
    00031710h HIGHLOW
    00031714h HIGHLOW
    0003175Ch HIGHLOW
    00031764h HIGHLOW
    0003176Ch HIGHLOW
    00031774h HIGHLOW
    0003177Ch HIGHLOW
    00031784h HIGHLOW
    0003178Ch HIGHLOW
    00031794h HIGHLOW
    0003179Ch HIGHLOW
    000317A4h HIGHLOW
    000317ACh HIGHLOW
    000317B4h HIGHLOW
    000317BCh HIGHLOW
    000317C4h HIGHLOW
    000317CCh HIGHLOW
    000317D4h HIGHLOW
    000317DCh HIGHLOW
    000317E4h HIGHLOW
    000317ECh HIGHLOW
    000317F4h HIGHLOW
    000317FCh HIGHLOW
    00031804h HIGHLOW
    0003180Ch HIGHLOW
    00031814h HIGHLOW
    0003181Ch HIGHLOW
    00031824h HIGHLOW
    0003182Ch HIGHLOW
    00031834h HIGHLOW
    00031838h HIGHLOW
    0003183Ch HIGHLOW
    00031840h HIGHLOW
    00031844h HIGHLOW
    00031848h HIGHLOW
    0003184Ch HIGHLOW
    00031850h HIGHLOW
    00031854h HIGHLOW
    00031858h HIGHLOW
    0003185Ch HIGHLOW
    00031860h HIGHLOW
    00031864h HIGHLOW
    00031868h HIGHLOW
    0003186Ch HIGHLOW
    00031870h HIGHLOW
    00031874h HIGHLOW
    00031890h HIGHLOW
    00031894h HIGHLOW
    00031898h HIGHLOW
    0003189Ch HIGHLOW
    000318A0h HIGHLOW
    000318A4h HIGHLOW
    000318A8h HIGHLOW
    000318ACh HIGHLOW
    000318B0h HIGHLOW
    000318B4h HIGHLOW
    000318B8h HIGHLOW
    000318BCh HIGHLOW
    000318C0h HIGHLOW
    000318C4h HIGHLOW
    000318C8h HIGHLOW
    000318CCh HIGHLOW
    000318D0h HIGHLOW
    000318D4h HIGHLOW
    000318D8h HIGHLOW
    000318DCh HIGHLOW
    00031A08h HIGHLOW
    00031A0Ch HIGHLOW
    00031A10h HIGHLOW
    00031A14h HIGHLOW
    00031A18h HIGHLOW
    00031A1Ch HIGHLOW
    00031A20h HIGHLOW
    00031A24h HIGHLOW
    00031A28h HIGHLOW
    00031A2Ch HIGHLOW
    00031A30h HIGHLOW
    00031A34h HIGHLOW
    00031A38h HIGHLOW
    00031A3Ch HIGHLOW
    00031A40h HIGHLOW
    00031A44h HIGHLOW
    00031A48h HIGHLOW
    00031A4Ch HIGHLOW
    00031A50h HIGHLOW
    00031A54h HIGHLOW
    00031A58h HIGHLOW
    00031A5Ch HIGHLOW
    00031A60h HIGHLOW
    00031A64h HIGHLOW
    00031A68h HIGHLOW
    00031A6Ch HIGHLOW
    00031A70h HIGHLOW
    00031A74h HIGHLOW
    00031A78h HIGHLOW
    00031A7Ch HIGHLOW
    00031A80h HIGHLOW
    00031A84h HIGHLOW
    00031A88h HIGHLOW
    00031A8Ch HIGHLOW
    00031A90h HIGHLOW
    00031A94h HIGHLOW
    00031A98h HIGHLOW
    00031A9Ch HIGHLOW
    00031AA0h HIGHLOW
    00031AA4h HIGHLOW
    00031AA8h HIGHLOW
    00031AACh HIGHLOW
    00031AB0h HIGHLOW
    00031AB4h HIGHLOW
    00031AB8h HIGHLOW
    00031ABCh HIGHLOW
    00031AC0h HIGHLOW
    00031AC4h HIGHLOW
    00031AC8h HIGHLOW
    00031ACCh HIGHLOW
    00031AD0h HIGHLOW
    00031AD4h HIGHLOW
    00031AD8h HIGHLOW
    00031ADCh HIGHLOW
    00031AE0h HIGHLOW
    00031AE4h HIGHLOW
    00031AE8h HIGHLOW
    00031AECh HIGHLOW
    00031AF0h HIGHLOW
    00031AF4h HIGHLOW
    00031AF8h HIGHLOW
    00031AFCh HIGHLOW
    00031B00h HIGHLOW
    00031B04h HIGHLOW
    00031B08h HIGHLOW
    00031B0Ch HIGHLOW
    00031B10h HIGHLOW
    00031B14h HIGHLOW
    00031B18h HIGHLOW
    00031B1Ch HIGHLOW
    00031B20h HIGHLOW
    00031B24h HIGHLOW
    00031B28h HIGHLOW
    00031B2Ch HIGHLOW
    00031B30h HIGHLOW
    00031B34h HIGHLOW
    00031B38h HIGHLOW
    00031B3Ch HIGHLOW
    00031B40h HIGHLOW
    00031B44h HIGHLOW
    00031B48h HIGHLOW
    00031B4Ch HIGHLOW
    00031FC0h HIGHLOW
    00031FC4h HIGHLOW
    00031FC8h HIGHLOW
    00031FCCh HIGHLOW
    00031FD0h HIGHLOW
    00031FD4h HIGHLOW
    00031FD8h HIGHLOW
    00031FDCh HIGHLOW
    00031FE0h HIGHLOW
    00031FE4h HIGHLOW
    00031FE8h HIGHLOW
    00031FECh HIGHLOW
    00031FF0h HIGHLOW
    00031FF4h HIGHLOW
    00031FF8h HIGHLOW
    00031FFCh HIGHLOW
    00031000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x32000   
SizeOfBlock:                   0x25C     
    00032000h HIGHLOW
    00032004h HIGHLOW
    00032008h HIGHLOW
    0003200Ch HIGHLOW
    00032010h HIGHLOW
    00032014h HIGHLOW
    00032018h HIGHLOW
    0003201Ch HIGHLOW
    00032020h HIGHLOW
    00032024h HIGHLOW
    00032028h HIGHLOW
    0003202Ch HIGHLOW
    00032030h HIGHLOW
    00032034h HIGHLOW
    00032038h HIGHLOW
    0003203Ch HIGHLOW
    00032040h HIGHLOW
    00032044h HIGHLOW
    00032048h HIGHLOW
    0003204Ch HIGHLOW
    00032050h HIGHLOW
    00032054h HIGHLOW
    00032058h HIGHLOW
    0003205Ch HIGHLOW
    00032060h HIGHLOW
    00032064h HIGHLOW
    00032068h HIGHLOW
    0003206Ch HIGHLOW
    00032070h HIGHLOW
    00032074h HIGHLOW
    00032078h HIGHLOW
    0003207Ch HIGHLOW
    00032080h HIGHLOW
    00032084h HIGHLOW
    00032088h HIGHLOW
    0003208Ch HIGHLOW
    00032090h HIGHLOW
    00032094h HIGHLOW
    00032098h HIGHLOW
    0003209Ch HIGHLOW
    000320A0h HIGHLOW
    000320A4h HIGHLOW
    0003233Ch HIGHLOW
    00032340h HIGHLOW
    00032358h HIGHLOW
    00032360h HIGHLOW
    00032368h HIGHLOW
    00032370h HIGHLOW
    00032378h HIGHLOW
    0003237Ch HIGHLOW
    00032380h HIGHLOW
    00032384h HIGHLOW
    00032388h HIGHLOW
    0003238Ch HIGHLOW
    00032390h HIGHLOW
    000323B0h HIGHLOW
    000323B4h HIGHLOW
    000323B8h HIGHLOW
    000323BCh HIGHLOW
    000323C0h HIGHLOW
    000323C4h HIGHLOW
    000323C8h HIGHLOW
    000323CCh HIGHLOW
    000323D0h HIGHLOW
    000323D4h HIGHLOW
    00032430h HIGHLOW
    00032434h HIGHLOW
    00032438h HIGHLOW
    0003243Ch HIGHLOW
    00032440h HIGHLOW
    00032444h HIGHLOW
    00032448h HIGHLOW
    0003244Ch HIGHLOW
    00032450h HIGHLOW
    00032454h HIGHLOW
    00032458h HIGHLOW
    0003245Ch HIGHLOW
    00032460h HIGHLOW
    00032464h HIGHLOW
    00032468h HIGHLOW
    0003246Ch HIGHLOW
    0003250Ch HIGHLOW
    00032510h HIGHLOW
    00032538h HIGHLOW
    0003253Ch HIGHLOW
    00032540h HIGHLOW
    00032544h HIGHLOW
    00032548h HIGHLOW
    0003254Ch HIGHLOW
    00032550h HIGHLOW
    00032554h HIGHLOW
    00032558h HIGHLOW
    0003255Ch HIGHLOW
    00032560h HIGHLOW
    00032564h HIGHLOW
    00032568h HIGHLOW
    0003256Ch HIGHLOW
    00032570h HIGHLOW
    00032574h HIGHLOW
    00032578h HIGHLOW
    0003257Ch HIGHLOW
    00032580h HIGHLOW
    00032584h HIGHLOW
    00032588h HIGHLOW
    0003258Ch HIGHLOW
    00032590h HIGHLOW
    00032594h HIGHLOW
    00032598h HIGHLOW
    0003259Ch HIGHLOW
    000325A0h HIGHLOW
    000325A4h HIGHLOW
    000325A8h HIGHLOW
    000325ACh HIGHLOW
    000325B0h HIGHLOW
    000325B4h HIGHLOW
    000325B8h HIGHLOW
    000325BCh HIGHLOW
    000325C0h HIGHLOW
    000325C4h HIGHLOW
    000325C8h HIGHLOW
    000325CCh HIGHLOW
    000325D0h HIGHLOW
    000325D4h HIGHLOW
    00032758h HIGHLOW
    0003275Ch HIGHLOW
    00032760h HIGHLOW
    00032764h HIGHLOW
    00032768h HIGHLOW
    0003276Ch HIGHLOW
    00032770h HIGHLOW
    00032774h HIGHLOW
    000327DCh HIGHLOW
    000327E0h HIGHLOW
    000327E4h HIGHLOW
    000327E8h HIGHLOW
    000327ECh HIGHLOW
    000327F0h HIGHLOW
    000327F4h HIGHLOW
    000327F8h HIGHLOW
    00032850h HIGHLOW
    00032854h HIGHLOW
    00032868h HIGHLOW
    0003286Ch HIGHLOW
    00032870h HIGHLOW
    00032874h HIGHLOW
    00032878h HIGHLOW
    0003287Ch HIGHLOW
    00032880h HIGHLOW
    00032884h HIGHLOW
    00032888h HIGHLOW
    0003288Ch HIGHLOW
    00032890h HIGHLOW
    00032894h HIGHLOW
    00032898h HIGHLOW
    0003289Ch HIGHLOW
    000328A0h HIGHLOW
    000328A4h HIGHLOW
    000328A8h HIGHLOW
    000328ACh HIGHLOW
    000328B0h HIGHLOW
    000328B4h HIGHLOW
    000328B8h HIGHLOW
    000328BCh HIGHLOW
    000328C0h HIGHLOW
    000328C4h HIGHLOW
    000328C8h HIGHLOW
    000328CCh HIGHLOW
    000328D0h HIGHLOW
    000328D4h HIGHLOW
    000328D8h HIGHLOW
    000328DCh HIGHLOW
    000328E0h HIGHLOW
    000328E4h HIGHLOW
    000328E8h HIGHLOW
    000328ECh HIGHLOW
    000328F0h HIGHLOW
    000328F4h HIGHLOW
    000328F8h HIGHLOW
    000328FCh HIGHLOW
    00032900h HIGHLOW
    00032904h HIGHLOW
    00032908h HIGHLOW
    0003290Ch HIGHLOW
    00032910h HIGHLOW
    00032914h HIGHLOW
    00032918h HIGHLOW
    0003291Ch HIGHLOW
    00032AD8h HIGHLOW
    00032ADCh HIGHLOW
    00032AE0h HIGHLOW
    00032AE4h HIGHLOW
    00032AE8h HIGHLOW
    00032AECh HIGHLOW
    00032AF0h HIGHLOW
    00032AF4h HIGHLOW
    00032AF8h HIGHLOW
    00032AFCh HIGHLOW
    00032B00h HIGHLOW
    00032B04h HIGHLOW
    00032B08h HIGHLOW
    00032B0Ch HIGHLOW
    00032B10h HIGHLOW
    00032B14h HIGHLOW
    00032B18h HIGHLOW
    00032B1Ch HIGHLOW
    00032B20h HIGHLOW
    00032B24h HIGHLOW
    00032B28h HIGHLOW
    00032B2Ch HIGHLOW
    00032B30h HIGHLOW
    00032B34h HIGHLOW
    00032B38h HIGHLOW
    00032B3Ch HIGHLOW
    00032B40h HIGHLOW
    00032B44h HIGHLOW
    00032B48h HIGHLOW
    00032B4Ch HIGHLOW
    00032B50h HIGHLOW
    00032B54h HIGHLOW
    00032B58h HIGHLOW
    00032B5Ch HIGHLOW
    00032B60h HIGHLOW
    00032B64h HIGHLOW
    00032B68h HIGHLOW
    00032B6Ch HIGHLOW
    00032B70h HIGHLOW
    00032B74h HIGHLOW
    00032B78h HIGHLOW
    00032B7Ch HIGHLOW
    00032B80h HIGHLOW
    00032B84h HIGHLOW
    00032B88h HIGHLOW
    00032B8Ch HIGHLOW
    00032B90h HIGHLOW
    00032B94h HIGHLOW
    00032B98h HIGHLOW
    00032B9Ch HIGHLOW
    00032BA0h HIGHLOW
    00032BA4h HIGHLOW
    00032BA8h HIGHLOW
    00032BACh HIGHLOW
    00032BB0h HIGHLOW
    00032BB4h HIGHLOW
    00032BB8h HIGHLOW
    00032BBCh HIGHLOW
    00032BC0h HIGHLOW
    00032BC4h HIGHLOW
    00032BC8h HIGHLOW
    00032BCCh HIGHLOW
    00032BD0h HIGHLOW
    00032BD4h HIGHLOW
    00032BD8h HIGHLOW
    00032BDCh HIGHLOW
    00032BE0h HIGHLOW
    00032BE4h HIGHLOW
    00032BE8h HIGHLOW
    00032BECh HIGHLOW
    00032BF0h HIGHLOW
    00032BF4h HIGHLOW
    00032BF8h HIGHLOW
    00032BFCh HIGHLOW
    00032C00h HIGHLOW
    00032C04h HIGHLOW
    00032C08h HIGHLOW
    00032C0Ch HIGHLOW
    00032C10h HIGHLOW
    00032C14h HIGHLOW
    00032C18h HIGHLOW
    00032C1Ch HIGHLOW
    00032C20h HIGHLOW
    00032C24h HIGHLOW
    00032C28h HIGHLOW
    00032C2Ch HIGHLOW
    00032C30h HIGHLOW
    00032C34h HIGHLOW
    00032C38h HIGHLOW
    00032C3Ch HIGHLOW
    00032C40h HIGHLOW
    00032C44h HIGHLOW
    00032C48h HIGHLOW
    00032C4Ch HIGHLOW
    00032C50h HIGHLOW
    00032C54h HIGHLOW
    00032C58h HIGHLOW
    00032C5Ch HIGHLOW
    00032C60h HIGHLOW
    00032C64h HIGHLOW
    00032C68h HIGHLOW
    00032C6Ch HIGHLOW
    00032C70h HIGHLOW
    00032C74h HIGHLOW
    00032C78h HIGHLOW
    00032C7Ch HIGHLOW
    00032C80h HIGHLOW
    00032C84h HIGHLOW
    00032C88h HIGHLOW
    00032C8Ch HIGHLOW
    00032000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x33000   
SizeOfBlock:                   0x2E4     
    00033100h HIGHLOW
    00033104h HIGHLOW
    00033108h HIGHLOW
    0003310Ch HIGHLOW
    00033110h HIGHLOW
    00033114h HIGHLOW
    00033118h HIGHLOW
    0003311Ch HIGHLOW
    00033120h HIGHLOW
    00033124h HIGHLOW
    00033128h HIGHLOW
    0003312Ch HIGHLOW
    00033130h HIGHLOW
    00033134h HIGHLOW
    00033138h HIGHLOW
    0003313Ch HIGHLOW
    00033140h HIGHLOW
    00033144h HIGHLOW
    00033148h HIGHLOW
    0003314Ch HIGHLOW
    00033150h HIGHLOW
    00033154h HIGHLOW
    00033158h HIGHLOW
    0003315Ch HIGHLOW
    00033160h HIGHLOW
    00033164h HIGHLOW
    00033168h HIGHLOW
    0003316Ch HIGHLOW
    00033170h HIGHLOW
    00033174h HIGHLOW
    00033178h HIGHLOW
    0003317Ch HIGHLOW
    00033180h HIGHLOW
    00033184h HIGHLOW
    00033188h HIGHLOW
    0003318Ch HIGHLOW
    00033190h HIGHLOW
    00033194h HIGHLOW
    000332E0h HIGHLOW
    000332E4h HIGHLOW
    000332E8h HIGHLOW
    000332ECh HIGHLOW
    000332F0h HIGHLOW
    000332F4h HIGHLOW
    000332F8h HIGHLOW
    000332FCh HIGHLOW
    00033300h HIGHLOW
    00033304h HIGHLOW
    00033308h HIGHLOW
    0003330Ch HIGHLOW
    00033310h HIGHLOW
    00033314h HIGHLOW
    00033318h HIGHLOW
    0003331Ch HIGHLOW
    00033320h HIGHLOW
    00033324h HIGHLOW
    00033328h HIGHLOW
    0003332Ch HIGHLOW
    00033330h HIGHLOW
    00033334h HIGHLOW
    00033338h HIGHLOW
    0003333Ch HIGHLOW
    00033340h HIGHLOW
    00033344h HIGHLOW
    00033348h HIGHLOW
    0003334Ch HIGHLOW
    00033350h HIGHLOW
    00033354h HIGHLOW
    00033358h HIGHLOW
    0003335Ch HIGHLOW
    00033360h HIGHLOW
    00033364h HIGHLOW
    00033368h HIGHLOW
    0003336Ch HIGHLOW
    00033370h HIGHLOW
    00033374h HIGHLOW
    00033378h HIGHLOW
    0003337Ch HIGHLOW
    00033380h HIGHLOW
    00033384h HIGHLOW
    00033388h HIGHLOW
    0003338Ch HIGHLOW
    00033390h HIGHLOW
    00033394h HIGHLOW
    00033398h HIGHLOW
    0003339Ch HIGHLOW
    000333A0h HIGHLOW
    000333A4h HIGHLOW
    000333A8h HIGHLOW
    000333ACh HIGHLOW
    000333B0h HIGHLOW
    000333B4h HIGHLOW
    000333B8h HIGHLOW
    000333BCh HIGHLOW
    000333C0h HIGHLOW
    000333C4h HIGHLOW
    000333C8h HIGHLOW
    000333CCh HIGHLOW
    000333D0h HIGHLOW
    000333D4h HIGHLOW
    000333D8h HIGHLOW
    000333DCh HIGHLOW
    000333E0h HIGHLOW
    000333E4h HIGHLOW
    000333E8h HIGHLOW
    000333ECh HIGHLOW
    0003363Ch HIGHLOW
    00033640h HIGHLOW
    00033650h HIGHLOW
    00033654h HIGHLOW
    00033658h HIGHLOW
    0003365Ch HIGHLOW
    00033660h HIGHLOW
    00033664h HIGHLOW
    00033668h HIGHLOW
    0003366Ch HIGHLOW
    00033670h HIGHLOW
    00033674h HIGHLOW
    00033678h HIGHLOW
    0003367Ch HIGHLOW
    00033680h HIGHLOW
    00033684h HIGHLOW
    00033688h HIGHLOW
    0003368Ch HIGHLOW
    00033690h HIGHLOW
    00033694h HIGHLOW
    00033698h HIGHLOW
    0003369Ch HIGHLOW
    000336A0h HIGHLOW
    000336A4h HIGHLOW
    000336A8h HIGHLOW
    000336ACh HIGHLOW
    000336B0h HIGHLOW
    000336B4h HIGHLOW
    000336B8h HIGHLOW
    000336BCh HIGHLOW
    000336C0h HIGHLOW
    000336C4h HIGHLOW
    000336C8h HIGHLOW
    000336CCh HIGHLOW
    000336D0h HIGHLOW
    000336D4h HIGHLOW
    000336D8h HIGHLOW
    000336DCh HIGHLOW
    000336E0h HIGHLOW
    000336E4h HIGHLOW
    000336E8h HIGHLOW
    000336ECh HIGHLOW
    000336F0h HIGHLOW
    000336F4h HIGHLOW
    000336F8h HIGHLOW
    000336FCh HIGHLOW
    00033700h HIGHLOW
    00033704h HIGHLOW
    00033708h HIGHLOW
    0003370Ch HIGHLOW
    00033710h HIGHLOW
    00033714h HIGHLOW
    00033718h HIGHLOW
    0003371Ch HIGHLOW
    00033720h HIGHLOW
    00033724h HIGHLOW
    00033728h HIGHLOW
    0003372Ch HIGHLOW
    00033730h HIGHLOW
    00033734h HIGHLOW
    00033738h HIGHLOW
    0003373Ch HIGHLOW
    00033740h HIGHLOW
    00033744h HIGHLOW
    00033748h HIGHLOW
    0003374Ch HIGHLOW
    00033750h HIGHLOW
    00033754h HIGHLOW
    00033758h HIGHLOW
    0003375Ch HIGHLOW
    00033760h HIGHLOW
    00033764h HIGHLOW
    00033768h HIGHLOW
    0003376Ch HIGHLOW
    00033770h HIGHLOW
    00033774h HIGHLOW
    000339F0h HIGHLOW
    000339F4h HIGHLOW
    000339F8h HIGHLOW
    000339FCh HIGHLOW
    00033A00h HIGHLOW
    00033A04h HIGHLOW
    00033A08h HIGHLOW
    00033A0Ch HIGHLOW
    00033A10h HIGHLOW
    00033A14h HIGHLOW
    00033A18h HIGHLOW
    00033A1Ch HIGHLOW
    00033A20h HIGHLOW
    00033A24h HIGHLOW
    00033A28h HIGHLOW
    00033A2Ch HIGHLOW
    00033A30h HIGHLOW
    00033A34h HIGHLOW
    00033A38h HIGHLOW
    00033A3Ch HIGHLOW
    00033A40h HIGHLOW
    00033A44h HIGHLOW
    00033A48h HIGHLOW
    00033A4Ch HIGHLOW
    00033A50h HIGHLOW
    00033A54h HIGHLOW
    00033A58h HIGHLOW
    00033A5Ch HIGHLOW
    00033A60h HIGHLOW
    00033A64h HIGHLOW
    00033A68h HIGHLOW
    00033A6Ch HIGHLOW
    00033A70h HIGHLOW
    00033A74h HIGHLOW
    00033A78h HIGHLOW
    00033A7Ch HIGHLOW
    00033A80h HIGHLOW
    00033A84h HIGHLOW
    00033A88h HIGHLOW
    00033A8Ch HIGHLOW
    00033A90h HIGHLOW
    00033A94h HIGHLOW
    00033A98h HIGHLOW
    00033A9Ch HIGHLOW
    00033AA0h HIGHLOW
    00033AA4h HIGHLOW
    00033AA8h HIGHLOW
    00033AACh HIGHLOW
    00033AB0h HIGHLOW
    00033AB4h HIGHLOW
    00033AB8h HIGHLOW
    00033ABCh HIGHLOW
    00033C8Ch HIGHLOW
    00033C90h HIGHLOW
    00033C94h HIGHLOW
    00033C98h HIGHLOW
    00033C9Ch HIGHLOW
    00033CA0h HIGHLOW
    00033CA4h HIGHLOW
    00033CA8h HIGHLOW
    00033CACh HIGHLOW
    00033CB0h HIGHLOW
    00033D3Ch HIGHLOW
    00033D40h HIGHLOW
    00033D44h HIGHLOW
    00033D48h HIGHLOW
    00033D4Ch HIGHLOW
    00033D50h HIGHLOW
    00033D54h HIGHLOW
    00033D58h HIGHLOW
    00033D5Ch HIGHLOW
    00033DBCh HIGHLOW
    00033DC4h HIGHLOW
    00033DC8h HIGHLOW
    00033DCCh HIGHLOW
    00033DD0h HIGHLOW
    00033DD4h HIGHLOW
    00033DD8h HIGHLOW
    00033DDCh HIGHLOW
    00033DE0h HIGHLOW
    00033DE4h HIGHLOW
    00033DE8h HIGHLOW
    00033DECh HIGHLOW
    00033E50h HIGHLOW
    00033E54h HIGHLOW
    00033E58h HIGHLOW
    00033E5Ch HIGHLOW
    00033E60h HIGHLOW
    00033E64h HIGHLOW
    00033E68h HIGHLOW
    00033E6Ch HIGHLOW
    00033E70h HIGHLOW
    00033E74h HIGHLOW
    00033E78h HIGHLOW
    00033E7Ch HIGHLOW
    00033E80h HIGHLOW
    00033E84h HIGHLOW
    00033E88h HIGHLOW
    00033E8Ch HIGHLOW
    00033E90h HIGHLOW
    00033E94h HIGHLOW
    00033E98h HIGHLOW
    00033E9Ch HIGHLOW
    00033EA0h HIGHLOW
    00033EA4h HIGHLOW
    00033EA8h HIGHLOW
    00033EACh HIGHLOW
    00033EB0h HIGHLOW
    00033EB4h HIGHLOW
    00033EB8h HIGHLOW
    00033EBCh HIGHLOW
    00033EC0h HIGHLOW
    00033EC4h HIGHLOW
    00033EC8h HIGHLOW
    00033ECCh HIGHLOW
    00033ED0h HIGHLOW
    00033ED4h HIGHLOW
    00033ED8h HIGHLOW
    00033EDCh HIGHLOW
    00033EE0h HIGHLOW
    00033EE4h HIGHLOW
    00033EE8h HIGHLOW
    00033EECh HIGHLOW
    00033EF0h HIGHLOW
    00033EF4h HIGHLOW
    00033EF8h HIGHLOW
    00033EFCh HIGHLOW
    00033F00h HIGHLOW
    00033F04h HIGHLOW
    00033F08h HIGHLOW
    00033F0Ch HIGHLOW
    00033F10h HIGHLOW
    00033F14h HIGHLOW
    00033F18h HIGHLOW
    00033F1Ch HIGHLOW
    00033F20h HIGHLOW
    00033F24h HIGHLOW
    00033F28h HIGHLOW
    00033F2Ch HIGHLOW
    00033F30h HIGHLOW
    00033F34h HIGHLOW
    00033F38h HIGHLOW
    00033F3Ch HIGHLOW
    00033F40h HIGHLOW
    00033F44h HIGHLOW
    00033F48h HIGHLOW
    00033F4Ch HIGHLOW
    00033F50h HIGHLOW
    00033F54h HIGHLOW
    00033F58h HIGHLOW
    00033F5Ch HIGHLOW
    00033F60h HIGHLOW
    00033F64h HIGHLOW
    00033F68h HIGHLOW
    00033F6Ch HIGHLOW
    00033F70h HIGHLOW
    00033F74h HIGHLOW
    00033F78h HIGHLOW
    00033F7Ch HIGHLOW
    00033F80h HIGHLOW
    00033F84h HIGHLOW
    00033F88h HIGHLOW
    00033F8Ch HIGHLOW
    00033F90h HIGHLOW
    00033F94h HIGHLOW
    00033F98h HIGHLOW
    00033F9Ch HIGHLOW
    00033FA0h HIGHLOW
    00033FA4h HIGHLOW
    00033FA8h HIGHLOW
    00033FACh HIGHLOW
    00033FB0h HIGHLOW
    00033FB4h HIGHLOW
    00033FB8h HIGHLOW
    00033FBCh HIGHLOW
    00033FC0h HIGHLOW
    00033FC4h HIGHLOW
    00033FC8h HIGHLOW
    00033FCCh HIGHLOW
    00033FD0h HIGHLOW
    00033FD4h HIGHLOW
    00033FD8h HIGHLOW
    00033FDCh HIGHLOW
    00033000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x34000   
SizeOfBlock:                   0x1DC     
    000344CCh HIGHLOW
    000344D0h HIGHLOW
    000344D4h HIGHLOW
    000344D8h HIGHLOW
    000344DCh HIGHLOW
    000344E0h HIGHLOW
    000344E4h HIGHLOW
    000344E8h HIGHLOW
    000344ECh HIGHLOW
    000344F0h HIGHLOW
    00034580h HIGHLOW
    00034584h HIGHLOW
    00034588h HIGHLOW
    0003458Ch HIGHLOW
    00034590h HIGHLOW
    00034594h HIGHLOW
    00034598h HIGHLOW
    0003459Ch HIGHLOW
    000345A0h HIGHLOW
    000345A4h HIGHLOW
    000345A8h HIGHLOW
    000345ACh HIGHLOW
    000345B0h HIGHLOW
    000345B4h HIGHLOW
    000345B8h HIGHLOW
    000345BCh HIGHLOW
    000345C0h HIGHLOW
    000345C4h HIGHLOW
    000345C8h HIGHLOW
    000345CCh HIGHLOW
    000345D0h HIGHLOW
    000345D4h HIGHLOW
    0003469Ch HIGHLOW
    000346A4h HIGHLOW
    000346ACh HIGHLOW
    000346B4h HIGHLOW
    000346BCh HIGHLOW
    000346C4h HIGHLOW
    000346CCh HIGHLOW
    000346D4h HIGHLOW
    000346DCh HIGHLOW
    000346E4h HIGHLOW
    000346ECh HIGHLOW
    000346F4h HIGHLOW
    000346FCh HIGHLOW
    00034704h HIGHLOW
    0003470Ch HIGHLOW
    00034710h HIGHLOW
    00034714h HIGHLOW
    00034718h HIGHLOW
    0003471Ch HIGHLOW
    00034720h HIGHLOW
    00034724h HIGHLOW
    00034728h HIGHLOW
    0003472Ch HIGHLOW
    00034730h HIGHLOW
    00034734h HIGHLOW
    00034738h HIGHLOW
    0003473Ch HIGHLOW
    00034740h HIGHLOW
    00034744h HIGHLOW
    00034748h HIGHLOW
    0003474Ch HIGHLOW
    00034750h HIGHLOW
    00034754h HIGHLOW
    00034758h HIGHLOW
    0003475Ch HIGHLOW
    00034760h HIGHLOW
    00034764h HIGHLOW
    00034768h HIGHLOW
    0003476Ch HIGHLOW
    00034770h HIGHLOW
    00034774h HIGHLOW
    00034778h HIGHLOW
    0003477Ch HIGHLOW
    00034780h HIGHLOW
    00034784h HIGHLOW
    00034788h HIGHLOW
    0003478Ch HIGHLOW
    00034790h HIGHLOW
    00034794h HIGHLOW
    00034798h HIGHLOW
    0003479Ch HIGHLOW
    000347A0h HIGHLOW
    000347A4h HIGHLOW
    00034948h HIGHLOW
    0003494Ch HIGHLOW
    00034950h HIGHLOW
    00034954h HIGHLOW
    00034958h HIGHLOW
    0003495Ch HIGHLOW
    00034960h HIGHLOW
    00034964h HIGHLOW
    00034968h HIGHLOW
    0003496Ch HIGHLOW
    00034970h HIGHLOW
    00034974h HIGHLOW
    00034978h HIGHLOW
    0003497Ch HIGHLOW
    00034980h HIGHLOW
    00034984h HIGHLOW
    00034988h HIGHLOW
    0003498Ch HIGHLOW
    00034990h HIGHLOW
    00034994h HIGHLOW
    00034998h HIGHLOW
    0003499Ch HIGHLOW
    000349A0h HIGHLOW
    000349A4h HIGHLOW
    000349A8h HIGHLOW
    000349ACh HIGHLOW
    000349B0h HIGHLOW
    000349B4h HIGHLOW
    000349B8h HIGHLOW
    000349BCh HIGHLOW
    000349C0h HIGHLOW
    000349C4h HIGHLOW
    000349C8h HIGHLOW
    000349CCh HIGHLOW
    000349D0h HIGHLOW
    000349D4h HIGHLOW
    000349D8h HIGHLOW
    000349DCh HIGHLOW
    000349E0h HIGHLOW
    000349E4h HIGHLOW
    000349E8h HIGHLOW
    000349ECh HIGHLOW
    000349F0h HIGHLOW
    000349F4h HIGHLOW
    000349F8h HIGHLOW
    000349FCh HIGHLOW
    00034A00h HIGHLOW
    00034A04h HIGHLOW
    00034A08h HIGHLOW
    00034A0Ch HIGHLOW
    00034A10h HIGHLOW
    00034A14h HIGHLOW
    00034A18h HIGHLOW
    00034A1Ch HIGHLOW
    00034A24h HIGHLOW
    00034A2Ch HIGHLOW
    00034A34h HIGHLOW
    00034C68h HIGHLOW
    00034C6Ch HIGHLOW
    00034C70h HIGHLOW
    00034C74h HIGHLOW
    00034CA4h HIGHLOW
    00034CACh HIGHLOW
    00034CB4h HIGHLOW
    00034CBCh HIGHLOW
    00034CC4h HIGHLOW
    00034CCCh HIGHLOW
    00034CD4h HIGHLOW
    00034CDCh HIGHLOW
    00034CE4h HIGHLOW
    00034CECh HIGHLOW
    00034CF4h HIGHLOW
    00034CFCh HIGHLOW
    00034D04h HIGHLOW
    00034D0Ch HIGHLOW
    00034D14h HIGHLOW
    00034D1Ch HIGHLOW
    00034D24h HIGHLOW
    00034D2Ch HIGHLOW
    00034D34h HIGHLOW
    00034D3Ch HIGHLOW
    00034D44h HIGHLOW
    00034D48h HIGHLOW
    00034D4Ch HIGHLOW
    00034D50h HIGHLOW
    00034D54h HIGHLOW
    00034D58h HIGHLOW
    00034D5Ch HIGHLOW
    00034D60h HIGHLOW
    00034D64h HIGHLOW
    00034D68h HIGHLOW
    00034D6Ch HIGHLOW
    00034D70h HIGHLOW
    00034D74h HIGHLOW
    00034E20h HIGHLOW
    00034E24h HIGHLOW
    00034E28h HIGHLOW
    00034E2Ch HIGHLOW
    00034E30h HIGHLOW
    00034E34h HIGHLOW
    00034E38h HIGHLOW
    00034E3Ch HIGHLOW
    00034E40h HIGHLOW
    00034E44h HIGHLOW
    00034E48h HIGHLOW
    00034E4Ch HIGHLOW
    00034E50h HIGHLOW
    00034E54h HIGHLOW
    00034E58h HIGHLOW
    00034E5Ch HIGHLOW
    00034E60h HIGHLOW
    00034E64h HIGHLOW
    00034E68h HIGHLOW
    00034E6Ch HIGHLOW
    00034E70h HIGHLOW
    00034E74h HIGHLOW
    00034F70h HIGHLOW
    00034F74h HIGHLOW
    00034F88h HIGHLOW
    00034F8Ch HIGHLOW
    00034F90h HIGHLOW
    00034F94h HIGHLOW
    00034F98h HIGHLOW
    00034F9Ch HIGHLOW
    00034FA0h HIGHLOW
    00034FA4h HIGHLOW
    00034FA8h HIGHLOW
    00034FACh HIGHLOW
    00034FB0h HIGHLOW
    00034FB4h HIGHLOW
    00034FB8h HIGHLOW
    00034FBCh HIGHLOW
    00034FC0h HIGHLOW
    00034FC4h HIGHLOW
    00034FC8h HIGHLOW
    00034FCCh HIGHLOW
    00034FD0h HIGHLOW
    00034FD4h HIGHLOW
    00034FD8h HIGHLOW
    00034FDCh HIGHLOW
    00034FE0h HIGHLOW
    00034FE4h HIGHLOW
    00034FE8h HIGHLOW
    00034FECh HIGHLOW
    00034FF0h HIGHLOW
    00034FF4h HIGHLOW
    00034FF8h HIGHLOW
    00034FFCh HIGHLOW
    00034000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x35000   
SizeOfBlock:                   0x140     
    00035000h HIGHLOW
    00035004h HIGHLOW
    00035008h HIGHLOW
    0003500Ch HIGHLOW
    00035010h HIGHLOW
    00035014h HIGHLOW
    00035018h HIGHLOW
    0003501Ch HIGHLOW
    00035020h HIGHLOW
    00035024h HIGHLOW
    00035028h HIGHLOW
    0003502Ch HIGHLOW
    00035030h HIGHLOW
    00035034h HIGHLOW
    00035038h HIGHLOW
    0003503Ch HIGHLOW
    00035040h HIGHLOW
    00035044h HIGHLOW
    00035048h HIGHLOW
    0003504Ch HIGHLOW
    00035050h HIGHLOW
    00035054h HIGHLOW
    00035058h HIGHLOW
    0003505Ch HIGHLOW
    00035060h HIGHLOW
    00035064h HIGHLOW
    00035068h HIGHLOW
    0003506Ch HIGHLOW
    00035070h HIGHLOW
    00035074h HIGHLOW
    00035078h HIGHLOW
    0003507Ch HIGHLOW
    00035080h HIGHLOW
    00035084h HIGHLOW
    00035088h HIGHLOW
    0003508Ch HIGHLOW
    00035090h HIGHLOW
    00035094h HIGHLOW
    00035098h HIGHLOW
    0003509Ch HIGHLOW
    000350A0h HIGHLOW
    000350A4h HIGHLOW
    000350A8h HIGHLOW
    000350ACh HIGHLOW
    000350B0h HIGHLOW
    000350B4h HIGHLOW
    000350B8h HIGHLOW
    000350BCh HIGHLOW
    000350C0h HIGHLOW
    000350C4h HIGHLOW
    000350C8h HIGHLOW
    000350CCh HIGHLOW
    000350D0h HIGHLOW
    000350D4h HIGHLOW
    000350D8h HIGHLOW
    000350DCh HIGHLOW
    000350E0h HIGHLOW
    000350E4h HIGHLOW
    000350E8h HIGHLOW
    000350ECh HIGHLOW
    000350F0h HIGHLOW
    000350F4h HIGHLOW
    000350F8h HIGHLOW
    000350FCh HIGHLOW
    00035100h HIGHLOW
    00035104h HIGHLOW
    00035108h HIGHLOW
    0003510Ch HIGHLOW
    00035110h HIGHLOW
    00035114h HIGHLOW
    00035118h HIGHLOW
    0003511Ch HIGHLOW
    00035120h HIGHLOW
    00035124h HIGHLOW
    00035128h HIGHLOW
    0003512Ch HIGHLOW
    00035130h HIGHLOW
    00035134h HIGHLOW
    00035138h HIGHLOW
    0003513Ch HIGHLOW
    000354F4h HIGHLOW
    000354FCh HIGHLOW
    00035504h HIGHLOW
    00035508h HIGHLOW
    00035514h HIGHLOW
    00035518h HIGHLOW
    00035528h HIGHLOW
    00035530h HIGHLOW
    00035534h HIGHLOW
    000355C0h HIGHLOW
    000355CCh HIGHLOW
    000355D0h HIGHLOW
    000355E0h HIGHLOW
    000355F0h HIGHLOW
    000357E0h HIGHLOW
    000357F8h HIGHLOW
    000358F4h HIGHLOW
    00035950h HIGHLOW
    00035960h HIGHLOW
    00035974h HIGHLOW
    00035978h HIGHLOW
    00035984h HIGHLOW
    00035988h HIGHLOW
    00035998h HIGHLOW
    000359D8h HIGHLOW
    000359E0h HIGHLOW
    000359E4h HIGHLOW
    000359F0h HIGHLOW
    00035A1Ch HIGHLOW
    00035A20h HIGHLOW
    00035B0Ch HIGHLOW
    00035B10h HIGHLOW
    00035B20h HIGHLOW
    00035B2Ch HIGHLOW
    00035B30h HIGHLOW
    00035B3Ch HIGHLOW
    00035B40h HIGHLOW
    00035B5Ch HIGHLOW
    00035B60h HIGHLOW
    00035B84h HIGHLOW
    00035B88h HIGHLOW
    00035B94h HIGHLOW
    00035B98h HIGHLOW
    00035BB8h HIGHLOW
    00035BC0h HIGHLOW
    00035BC4h HIGHLOW
    00035BCAh HIGHLOW
    00035C12h HIGHLOW
    00035C29h HIGHLOW
    00035C44h HIGHLOW
    00035C4Ch HIGHLOW
    00035C66h HIGHLOW
    00035C78h HIGHLOW
    00035C95h HIGHLOW
    00035CA5h HIGHLOW
    00035CDCh HIGHLOW
    00035CFAh HIGHLOW
    00035DE3h HIGHLOW
    00035DEDh HIGHLOW
    00035E20h HIGHLOW
    00035E3Dh HIGHLOW
    00035E46h HIGHLOW
    00035E79h HIGHLOW
    00035E90h HIGHLOW
    00035EA8h HIGHLOW
    00035EB0h HIGHLOW
    00035ECBh HIGHLOW
    00035EEAh HIGHLOW
    00035F08h HIGHLOW
    00035F24h HIGHLOW
    00035F4Ch HIGHLOW
    00035F62h HIGHLOW
    00035F72h HIGHLOW
    00035FBFh HIGHLOW
    00035FDCh HIGHLOW
    00035000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x36000   
SizeOfBlock:                   0xCC      
    00036029h HIGHLOW
    00036038h HIGHLOW
    00036047h HIGHLOW
    00036061h HIGHLOW
    000360EEh HIGHLOW
    000360FEh HIGHLOW
    0003611Eh HIGHLOW
    00036136h HIGHLOW
    0003613Dh HIGHLOW
    0003614Bh HIGHLOW
    00036168h HIGHLOW
    0003617Bh HIGHLOW
    00036183h HIGHLOW
    000361C5h HIGHLOW
    000361D8h HIGHLOW
    000361F5h HIGHLOW
    0003620Ch HIGHLOW
    00036228h HIGHLOW
    0003623Bh HIGHLOW
    00036250h HIGHLOW
    0003625Dh HIGHLOW
    0003627Bh HIGHLOW
    00036295h HIGHLOW
    000362B3h HIGHLOW
    000362C5h HIGHLOW
    000362D1h HIGHLOW
    000362E3h HIGHLOW
    00036308h HIGHLOW
    00036316h HIGHLOW
    0003632Ah HIGHLOW
    00036342h HIGHLOW
    00036356h HIGHLOW
    0003637Bh HIGHLOW
    0003638Eh HIGHLOW
    00036397h HIGHLOW
    000363BBh HIGHLOW
    000363D6h HIGHLOW
    000363E1h HIGHLOW
    000363F5h HIGHLOW
    000364F2h HIGHLOW
    0003651Bh HIGHLOW
    00036528h HIGHLOW
    0003652Dh HIGHLOW
    00036532h HIGHLOW
    00036550h HIGHLOW
    0003655Dh HIGHLOW
    00036562h HIGHLOW
    00036567h HIGHLOW
    00036585h HIGHLOW
    00036592h HIGHLOW
    00036597h HIGHLOW
    0003659Ch HIGHLOW
    000365BDh HIGHLOW
    000365CBh HIGHLOW
    000365E5h HIGHLOW
    000365ECh HIGHLOW
    0003662Ah HIGHLOW
    0003666Ah HIGHLOW
    0003670Eh HIGHLOW
    00036741h HIGHLOW
    0003674Eh HIGHLOW
    000367A1h HIGHLOW
    00036A36h HIGHLOW
    00036A79h HIGHLOW
    00036AA7h HIGHLOW
    00036AB0h HIGHLOW
    00036ADCh HIGHLOW
    00036B47h HIGHLOW
    00036B50h HIGHLOW
    00036BCAh HIGHLOW
    00036BEFh HIGHLOW
    00036C35h HIGHLOW
    00036C56h HIGHLOW
    00036C7Ch HIGHLOW
    00036C85h HIGHLOW
    00036C8Ch HIGHLOW
    00036C95h HIGHLOW
    00036CE2h HIGHLOW
    00036CE8h HIGHLOW
    00036D26h HIGHLOW
    00036D32h HIGHLOW
    00036D48h HIGHLOW
    00036D4Fh HIGHLOW
    00036D66h HIGHLOW
    00036D6Dh HIGHLOW
    00036D79h HIGHLOW
    00036D92h HIGHLOW
    00036DA5h HIGHLOW
    00036DD9h HIGHLOW
    00036E03h HIGHLOW
    00036E1Ah HIGHLOW
    00036E31h HIGHLOW
    00036E56h HIGHLOW
    00036ED6h HIGHLOW
    00036F01h HIGHLOW
    00036F54h HIGHLOW
    00036F8Bh HIGHLOW
    00036000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x37000   
SizeOfBlock:                   0x68      
    0003700Dh HIGHLOW
    0003706Ah HIGHLOW
    000370A7h HIGHLOW
    000370B2h HIGHLOW
    000370FBh HIGHLOW
    00037136h HIGHLOW
    0003715Bh HIGHLOW
    000372C0h HIGHLOW
    000372FCh HIGHLOW
    000374FEh HIGHLOW
    00037503h HIGHLOW
    0003752Fh HIGHLOW
    0003759Bh HIGHLOW
    000375BAh HIGHLOW
    00037606h HIGHLOW
    00037668h HIGHLOW
    00037698h HIGHLOW
    000376A7h HIGHLOW
    000376AEh HIGHLOW
    000376B5h HIGHLOW
    000376CFh HIGHLOW
    000376DFh HIGHLOW
    00037765h HIGHLOW
    0003777Fh HIGHLOW
    00037844h HIGHLOW
    00037944h HIGHLOW
    00037967h HIGHLOW
    000379E5h HIGHLOW
    000379ECh HIGHLOW
    000379F2h HIGHLOW
    000379FEh HIGHLOW
    00037A03h HIGHLOW
    00037A08h HIGHLOW
    00037A1Ch HIGHLOW
    00037ABEh HIGHLOW
    00037AFDh HIGHLOW
    00037B92h HIGHLOW
    00037BA2h HIGHLOW
    00037BCBh HIGHLOW
    00037BF2h HIGHLOW
    00037CC5h HIGHLOW
    00037CD1h HIGHLOW
    00037D05h HIGHLOW
    00037D12h HIGHLOW
    00037D9Ch HIGHLOW
    00037DE8h HIGHLOW
    00037F20h HIGHLOW
    00037000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x38000   
SizeOfBlock:                   0x88      
    00038042h HIGHLOW
    00038100h HIGHLOW
    00038152h HIGHLOW
    00038195h HIGHLOW
    000381F8h HIGHLOW
    00038226h HIGHLOW
    0003825Ah HIGHLOW
    00038298h HIGHLOW
    0003829Dh HIGHLOW
    000382C3h HIGHLOW
    000382E0h HIGHLOW
    000382FAh HIGHLOW
    00038301h HIGHLOW
    0003830Fh HIGHLOW
    0003831Ch HIGHLOW
    00038322h HIGHLOW
    00038373h HIGHLOW
    00038389h HIGHLOW
    00038394h HIGHLOW
    0003839Ah HIGHLOW
    0003842Ah HIGHLOW
    0003843Eh HIGHLOW
    00038461h HIGHLOW
    000384C2h HIGHLOW
    000384DEh HIGHLOW
    000384F7h HIGHLOW
    00038517h HIGHLOW
    00038526h HIGHLOW
    000385B7h HIGHLOW
    00038696h HIGHLOW
    00038731h HIGHLOW
    0003877Eh HIGHLOW
    00038794h HIGHLOW
    00038799h HIGHLOW
    000387AFh HIGHLOW
    000387C5h HIGHLOW
    00038803h HIGHLOW
    00038830h HIGHLOW
    00038839h HIGHLOW
    00038898h HIGHLOW
    000388B5h HIGHLOW
    000388CBh HIGHLOW
    000388D4h HIGHLOW
    00038930h HIGHLOW
    00038974h HIGHLOW
    000389D3h HIGHLOW
    00038A97h HIGHLOW
    00038AD6h HIGHLOW
    00038B0Fh HIGHLOW
    00038B5Ah HIGHLOW
    00038B67h HIGHLOW
    00038BA9h HIGHLOW
    00038BE4h HIGHLOW
    00038C49h HIGHLOW
    00038C5Eh HIGHLOW
    00038C9Ah HIGHLOW
    00038D0Dh HIGHLOW
    00038D4Bh HIGHLOW
    00038D58h HIGHLOW
    00038DF8h HIGHLOW
    00038E19h HIGHLOW
    00038E60h HIGHLOW
    00038FA4h HIGHLOW
    00038FBEh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x39000   
SizeOfBlock:                   0x60      
    00039011h HIGHLOW
    000390E3h HIGHLOW
    00039111h HIGHLOW
    0003913Ah HIGHLOW
    00039159h HIGHLOW
    000391CBh HIGHLOW
    000393ABh HIGHLOW
    000393B3h HIGHLOW
    000393B8h HIGHLOW
    00039407h HIGHLOW
    00039460h HIGHLOW
    000394AFh HIGHLOW
    000394C7h HIGHLOW
    000395D1h HIGHLOW
    000395DCh HIGHLOW
    000395F3h HIGHLOW
    000396BDh HIGHLOW
    000396D2h HIGHLOW
    0003970Dh HIGHLOW
    0003974Eh HIGHLOW
    00039757h HIGHLOW
    000397BFh HIGHLOW
    000397F0h HIGHLOW
    000397F9h HIGHLOW
    0003984Ch HIGHLOW
    00039863h HIGHLOW
    0003989Bh HIGHLOW
    000398A1h HIGHLOW
    0003990Ah HIGHLOW
    00039934h HIGHLOW
    00039984h HIGHLOW
    000399D1h HIGHLOW
    00039AEDh HIGHLOW
    00039B12h HIGHLOW
    00039B21h HIGHLOW
    00039CDEh HIGHLOW
    00039D09h HIGHLOW
    00039DEDh HIGHLOW
    00039DF9h HIGHLOW
    00039E22h HIGHLOW
    00039E63h HIGHLOW
    00039F0Ch HIGHLOW
    00039FD4h HIGHLOW
    00039FEBh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3A000   
SizeOfBlock:                   0xA0      
    0003A034h HIGHLOW
    0003A05Bh HIGHLOW
    0003A06Eh HIGHLOW
    0003A09Dh HIGHLOW
    0003A0C6h HIGHLOW
    0003A0CDh HIGHLOW
    0003A13Eh HIGHLOW
    0003A15Dh HIGHLOW
    0003A1EBh HIGHLOW
    0003A1F6h HIGHLOW
    0003A209h HIGHLOW
    0003A25Fh HIGHLOW
    0003A27Fh HIGHLOW
    0003A2E2h HIGHLOW
    0003A313h HIGHLOW
    0003A341h HIGHLOW
    0003A35Dh HIGHLOW
    0003A3D5h HIGHLOW
    0003A3DFh HIGHLOW
    0003A495h HIGHLOW
    0003A63Ch HIGHLOW
    0003A640h HIGHLOW
    0003A66Ch HIGHLOW
    0003A670h HIGHLOW
    0003A678h HIGHLOW
    0003A67Ch HIGHLOW
    0003A722h HIGHLOW
    0003A726h HIGHLOW
    0003A72Ah HIGHLOW
    0003A72Eh HIGHLOW
    0003A732h HIGHLOW
    0003A736h HIGHLOW
    0003A73Ah HIGHLOW
    0003A73Eh HIGHLOW
    0003A742h HIGHLOW
    0003A746h HIGHLOW
    0003A74Ah HIGHLOW
    0003A7BEh HIGHLOW
    0003A909h HIGHLOW
    0003A90Eh HIGHLOW
    0003A935h HIGHLOW
    0003A95Bh HIGHLOW
    0003A9B1h HIGHLOW
    0003A9B7h HIGHLOW
    0003A9C1h HIGHLOW
    0003A9F6h HIGHLOW
    0003AAE2h HIGHLOW
    0003AAEEh HIGHLOW
    0003AAF9h HIGHLOW
    0003AAFFh HIGHLOW
    0003AB1Bh HIGHLOW
    0003AB21h HIGHLOW
    0003AB3Eh HIGHLOW
    0003AB44h HIGHLOW
    0003AC57h HIGHLOW
    0003ACDCh HIGHLOW
    0003ACE0h HIGHLOW
    0003ACECh HIGHLOW
    0003ACF0h HIGHLOW
    0003AD24h HIGHLOW
    0003AD9Eh HIGHLOW
    0003ADF8h HIGHLOW
    0003AE79h HIGHLOW
    0003AE94h HIGHLOW
    0003AEF5h HIGHLOW
    0003AF0Ch HIGHLOW
    0003AF1Eh HIGHLOW
    0003AF25h HIGHLOW
    0003AF62h HIGHLOW
    0003AF7Fh HIGHLOW
    0003AF93h HIGHLOW
    0003AFE4h HIGHLOW
    0003AFE8h HIGHLOW
    0003AFF4h HIGHLOW
    0003AFF8h HIGHLOW
    0003AFFFh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3B000   
SizeOfBlock:                   0x8C      
    0003B009h HIGHLOW
    0003B041h HIGHLOW
    0003B063h HIGHLOW
    0003B076h HIGHLOW
    0003B07Dh HIGHLOW
    0003B0D0h HIGHLOW
    0003B143h HIGHLOW
    0003B1D2h HIGHLOW
    0003B1FEh HIGHLOW
    0003B22Ah HIGHLOW
    0003B239h HIGHLOW
    0003B380h HIGHLOW
    0003B389h HIGHLOW
    0003B3ACh HIGHLOW
    0003B401h HIGHLOW
    0003B441h HIGHLOW
    0003B44Ch HIGHLOW
    0003B45Ch HIGHLOW
    0003B466h HIGHLOW
    0003B4DCh HIGHLOW
    0003B500h HIGHLOW
    0003B55Dh HIGHLOW
    0003B581h HIGHLOW
    0003B58Ah HIGHLOW
    0003B5ACh HIGHLOW
    0003B5CEh HIGHLOW
    0003B5F0h HIGHLOW
    0003B65Bh HIGHLOW
    0003B67Eh HIGHLOW
    0003B6CBh HIGHLOW
    0003B79Dh HIGHLOW
    0003B7ADh HIGHLOW
    0003B8BEh HIGHLOW
    0003B91Ch HIGHLOW
    0003B927h HIGHLOW
    0003B99Ah HIGHLOW
    0003B9A7h HIGHLOW
    0003B9D1h HIGHLOW
    0003BA66h HIGHLOW
    0003BA9Ch HIGHLOW
    0003BAB6h HIGHLOW
    0003BAF4h HIGHLOW
    0003BB07h HIGHLOW
    0003BB23h HIGHLOW
    0003BB53h HIGHLOW
    0003BC21h HIGHLOW
    0003BC37h HIGHLOW
    0003BC41h HIGHLOW
    0003BC57h HIGHLOW
    0003BC6Ch HIGHLOW
    0003BC8Ah HIGHLOW
    0003BCF6h HIGHLOW
    0003BD3Ah HIGHLOW
    0003BDACh HIGHLOW
    0003BDB0h HIGHLOW
    0003BDC0h HIGHLOW
    0003BDFCh HIGHLOW
    0003BE00h HIGHLOW
    0003BE14h HIGHLOW
    0003BE18h HIGHLOW
    0003BE20h HIGHLOW
    0003BE24h HIGHLOW
    0003BE84h HIGHLOW
    0003BE89h HIGHLOW
    0003BF02h HIGHLOW
    0003B000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3C000   
SizeOfBlock:                   0x60      
    0003C0CBh HIGHLOW
    0003C0DBh HIGHLOW
    0003C15Fh HIGHLOW
    0003C2FDh HIGHLOW
    0003C30Ah HIGHLOW
    0003C397h HIGHLOW
    0003C3CCh HIGHLOW
    0003C3FCh HIGHLOW
    0003C4B7h HIGHLOW
    0003C538h HIGHLOW
    0003C58Eh HIGHLOW
    0003C593h HIGHLOW
    0003C5C5h HIGHLOW
    0003C5F6h HIGHLOW
    0003C5FFh HIGHLOW
    0003C79Ah HIGHLOW
    0003C7BCh HIGHLOW
    0003C7C5h HIGHLOW
    0003C7D9h HIGHLOW
    0003C80Eh HIGHLOW
    0003C833h HIGHLOW
    0003C83Ch HIGHLOW
    0003C850h HIGHLOW
    0003C920h HIGHLOW
    0003C92Bh HIGHLOW
    0003C932h HIGHLOW
    0003C940h HIGHLOW
    0003C947h HIGHLOW
    0003C94Eh HIGHLOW
    0003C982h HIGHLOW
    0003C9EBh HIGHLOW
    0003CA9Fh HIGHLOW
    0003CAA4h HIGHLOW
    0003CAC9h HIGHLOW
    0003CAE7h HIGHLOW
    0003CB3Bh HIGHLOW
    0003CB57h HIGHLOW
    0003CB7Dh HIGHLOW
    0003CB8Eh HIGHLOW
    0003CBE5h HIGHLOW
    0003CC8Bh HIGHLOW
    0003CCAEh HIGHLOW
    0003CDDAh HIGHLOW
    0003C000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3D000   
SizeOfBlock:                   0x78      
    0003D028h HIGHLOW
    0003D415h HIGHLOW
    0003D41Bh HIGHLOW
    0003D440h HIGHLOW
    0003D44Eh HIGHLOW
    0003D454h HIGHLOW
    0003D469h HIGHLOW
    0003D46Fh HIGHLOW
    0003D52Fh HIGHLOW
    0003D5D7h HIGHLOW
    0003D61Ch HIGHLOW
    0003D6B2h HIGHLOW
    0003D6E7h HIGHLOW
    0003D70Bh HIGHLOW
    0003D749h HIGHLOW
    0003D74Eh HIGHLOW
    0003D761h HIGHLOW
    0003D766h HIGHLOW
    0003D76Eh HIGHLOW
    0003D773h HIGHLOW
    0003D77Ah HIGHLOW
    0003D77Fh HIGHLOW
    0003D7D0h HIGHLOW
    0003D7F4h HIGHLOW
    0003D800h HIGHLOW
    0003D840h HIGHLOW
    0003D870h HIGHLOW
    0003D898h HIGHLOW
    0003D8D5h HIGHLOW
    0003D9F9h HIGHLOW
    0003DA15h HIGHLOW
    0003DA7Eh HIGHLOW
    0003DB01h HIGHLOW
    0003DB1Dh HIGHLOW
    0003DB4Ah HIGHLOW
    0003DB6Ah HIGHLOW
    0003DBA2h HIGHLOW
    0003DBE2h HIGHLOW
    0003DC03h HIGHLOW
    0003DC1Eh HIGHLOW
    0003DCA2h HIGHLOW
    0003DCE8h HIGHLOW
    0003DD5Dh HIGHLOW
    0003DD66h HIGHLOW
    0003DD8Dh HIGHLOW
    0003DD96h HIGHLOW
    0003DDB7h HIGHLOW
    0003DED0h HIGHLOW
    0003DEE7h HIGHLOW
    0003DEF0h HIGHLOW
    0003DF08h HIGHLOW
    0003DF29h HIGHLOW
    0003DF96h HIGHLOW
    0003DF9Ch HIGHLOW
    0003DFB4h HIGHLOW
    0003DFD7h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3E000   
SizeOfBlock:                   0x54      
    0003E033h HIGHLOW
    0003E0A1h HIGHLOW
    0003E0DCh HIGHLOW
    0003E11Dh HIGHLOW
    0003E167h HIGHLOW
    0003E18Ah HIGHLOW
    0003E1BAh HIGHLOW
    0003E1DDh HIGHLOW
    0003E1E6h HIGHLOW
    0003E254h HIGHLOW
    0003E25Ch HIGHLOW
    0003E266h HIGHLOW
    0003E26Dh HIGHLOW
    0003E2D4h HIGHLOW
    0003E3B6h HIGHLOW
    0003E4CFh HIGHLOW
    0003E4F0h HIGHLOW
    0003E527h HIGHLOW
    0003E548h HIGHLOW
    0003E5C6h HIGHLOW
    0003E5D2h HIGHLOW
    0003E5FBh HIGHLOW
    0003E837h HIGHLOW
    0003E843h HIGHLOW
    0003E896h HIGHLOW
    0003E8A6h HIGHLOW
    0003E8D4h HIGHLOW
    0003E93Ch HIGHLOW
    0003EAEFh HIGHLOW
    0003EAF8h HIGHLOW
    0003ED2Ch HIGHLOW
    0003EEBEh HIGHLOW
    0003EEE1h HIGHLOW
    0003EEFEh HIGHLOW
    0003EF2Bh HIGHLOW
    0003EF45h HIGHLOW
    0003EFD3h HIGHLOW
    0003E000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x3F000   
SizeOfBlock:                   0x68      
    0003F02Ch HIGHLOW
    0003F044h HIGHLOW
    0003F04Dh HIGHLOW
    0003F08Dh HIGHLOW
    0003F0BBh HIGHLOW
    0003F0C3h HIGHLOW
    0003F0CDh HIGHLOW
    0003F0FAh HIGHLOW
    0003F129h HIGHLOW
    0003F158h HIGHLOW
    0003F161h HIGHLOW
    0003F1D0h HIGHLOW
    0003F202h HIGHLOW
    0003F289h HIGHLOW
    0003F369h HIGHLOW
    0003F3ADh HIGHLOW
    0003F3BAh HIGHLOW
    0003F3EBh HIGHLOW
    0003F3FDh HIGHLOW
    0003F437h HIGHLOW
    0003F4C5h HIGHLOW
    0003F59Fh HIGHLOW
    0003F5E4h HIGHLOW
    0003F6C2h HIGHLOW
    0003F703h HIGHLOW
    0003F712h HIGHLOW
    0003F7C1h HIGHLOW
    0003F834h HIGHLOW
    0003F8CCh HIGHLOW
    0003F8E6h HIGHLOW
    0003F9A2h HIGHLOW
    0003F9BDh HIGHLOW
    0003F9C6h HIGHLOW
    0003F9F4h HIGHLOW
    0003FA85h HIGHLOW
    0003FAF3h HIGHLOW
    0003FB25h HIGHLOW
    0003FB31h HIGHLOW
    0003FB8Fh HIGHLOW
    0003FB9Dh HIGHLOW
    0003FBE1h HIGHLOW
    0003FC93h HIGHLOW
    0003FCE7h HIGHLOW
    0003FDCEh HIGHLOW
    0003FE91h HIGHLOW
    0003FE9Ah HIGHLOW
    0003FEB9h HIGHLOW
    0003FF3Ch HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x40000   
SizeOfBlock:                   0x50      
    0004004Ah HIGHLOW
    00040060h HIGHLOW
    00040068h HIGHLOW
    00040083h HIGHLOW
    000400A6h HIGHLOW
    000400F3h HIGHLOW
    00040122h HIGHLOW
    0004024Eh HIGHLOW
    00040264h HIGHLOW
    0004029Fh HIGHLOW
    000402B2h HIGHLOW
    000405E1h HIGHLOW
    000405EDh HIGHLOW
    00040618h HIGHLOW
    00040640h HIGHLOW
    000406BCh HIGHLOW
    00040736h HIGHLOW
    000407D4h HIGHLOW
    000407F2h HIGHLOW
    000409B0h HIGHLOW
    000409EAh HIGHLOW
    00040A83h HIGHLOW
    00040AC5h HIGHLOW
    00040B07h HIGHLOW
    00040BB4h HIGHLOW
    00040D28h HIGHLOW
    00040D40h HIGHLOW
    00040D4Ch HIGHLOW
    00040D73h HIGHLOW
    00040E8Ch HIGHLOW
    00040EB5h HIGHLOW
    00040EC6h HIGHLOW
    00040EEFh HIGHLOW
    00040F41h HIGHLOW
    00040F70h HIGHLOW
    00040FBEh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x41000   
SizeOfBlock:                   0x4C      
    00041005h HIGHLOW
    000410E0h HIGHLOW
    0004112Fh HIGHLOW
    00041188h HIGHLOW
    000411DCh HIGHLOW
    00041209h HIGHLOW
    00041236h HIGHLOW
    00041466h HIGHLOW
    000414E4h HIGHLOW
    000415B9h HIGHLOW
    000416F5h HIGHLOW
    00041755h HIGHLOW
    00041761h HIGHLOW
    00041787h HIGHLOW
    000417ADh HIGHLOW
    00041832h HIGHLOW
    00041980h HIGHLOW
    00041997h HIGHLOW
    000419E5h HIGHLOW
    000419EEh HIGHLOW
    000419FFh HIGHLOW
    00041AE1h HIGHLOW
    00041B0Ch HIGHLOW
    00041B15h HIGHLOW
    00041B2Ah HIGHLOW
    00041BA5h HIGHLOW
    00041C06h HIGHLOW
    00041D39h HIGHLOW
    00041D65h HIGHLOW
    00041EACh HIGHLOW
    00041F27h HIGHLOW
    00041F55h HIGHLOW
    00041F97h HIGHLOW
    00041000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x42000   
SizeOfBlock:                   0x60      
    000420A0h HIGHLOW
    000420E0h HIGHLOW
    00042187h HIGHLOW
    000421B2h HIGHLOW
    000421C1h HIGHLOW
    000422BDh HIGHLOW
    00042392h HIGHLOW
    0004240Ch HIGHLOW
    00042412h HIGHLOW
    00042451h HIGHLOW
    00042457h HIGHLOW
    00042479h HIGHLOW
    00042480h HIGHLOW
    00042498h HIGHLOW
    0004249Eh HIGHLOW
    000424B0h HIGHLOW
    000424BEh HIGHLOW
    000424C4h HIGHLOW
    000424DAh HIGHLOW
    000424ECh HIGHLOW
    000424FAh HIGHLOW
    00042500h HIGHLOW
    00042535h HIGHLOW
    0004253Bh HIGHLOW
    000426F0h HIGHLOW
    00042857h HIGHLOW
    00042861h HIGHLOW
    00042895h HIGHLOW
    00042925h HIGHLOW
    00042B44h HIGHLOW
    00042BF3h HIGHLOW
    00042C4Ch HIGHLOW
    00042C5Eh HIGHLOW
    00042C8Ah HIGHLOW
    00042CA9h HIGHLOW
    00042CB5h HIGHLOW
    00042D46h HIGHLOW
    00042D81h HIGHLOW
    00042EDDh HIGHLOW
    00042EFCh HIGHLOW
    00042F08h HIGHLOW
    00042F36h HIGHLOW
    00042FB0h HIGHLOW
    00042000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x43000   
SizeOfBlock:                   0xB4      
    00043053h HIGHLOW
    00043076h HIGHLOW
    000430C0h HIGHLOW
    0004317Ch HIGHLOW
    0004318Eh HIGHLOW
    0004321Dh HIGHLOW
    00043224h HIGHLOW
    00043261h HIGHLOW
    0004326Ah HIGHLOW
    00043282h HIGHLOW
    00043299h HIGHLOW
    000432A8h HIGHLOW
    000432B6h HIGHLOW
    000432D3h HIGHLOW
    000432E2h HIGHLOW
    000432F2h HIGHLOW
    000432FBh HIGHLOW
    00043328h HIGHLOW
    00043360h HIGHLOW
    00043375h HIGHLOW
    000433AEh HIGHLOW
    00043454h HIGHLOW
    00043493h HIGHLOW
    000434A9h HIGHLOW
    00043518h HIGHLOW
    00043522h HIGHLOW
    00043529h HIGHLOW
    0004355Eh HIGHLOW
    00043575h HIGHLOW
    00043585h HIGHLOW
    0004358Fh HIGHLOW
    00043676h HIGHLOW
    0004370Eh HIGHLOW
    0004372Ch HIGHLOW
    00043737h HIGHLOW
    0004374Fh HIGHLOW
    000437CAh HIGHLOW
    00043811h HIGHLOW
    0004382Ah HIGHLOW
    00043836h HIGHLOW
    00043842h HIGHLOW
    000438ADh HIGHLOW
    000438CFh HIGHLOW
    000438F6h HIGHLOW
    000439C0h HIGHLOW
    000439DAh HIGHLOW
    000439FEh HIGHLOW
    00043A3Ah HIGHLOW
    00043A68h HIGHLOW
    00043ACFh HIGHLOW
    00043AD9h HIGHLOW
    00043BC1h HIGHLOW
    00043CB7h HIGHLOW
    00043CBEh HIGHLOW
    00043CDCh HIGHLOW
    00043CF3h HIGHLOW
    00043D3Ch HIGHLOW
    00043D43h HIGHLOW
    00043D55h HIGHLOW
    00043D62h HIGHLOW
    00043D7Fh HIGHLOW
    00043DBDh HIGHLOW
    00043DC6h HIGHLOW
    00043DE8h HIGHLOW
    00043DF4h HIGHLOW
    00043DF9h HIGHLOW
    00043E01h HIGHLOW
    00043E35h HIGHLOW
    00043E3Eh HIGHLOW
    00043E4Eh HIGHLOW
    00043E69h HIGHLOW
    00043E72h HIGHLOW
    00043E7Dh HIGHLOW
    00043E8Bh HIGHLOW
    00043EA4h HIGHLOW
    00043EACh HIGHLOW
    00043ECEh HIGHLOW
    00043F22h HIGHLOW
    00043F52h HIGHLOW
    00043F6Ah HIGHLOW
    00043F77h HIGHLOW
    00043F93h HIGHLOW
    00043FA3h HIGHLOW
    00043FD4h HIGHLOW
    00043FE8h HIGHLOW
    00043FF9h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x44000   
SizeOfBlock:                   0xA0      
    00044023h HIGHLOW
    0004402Ch HIGHLOW
    00044045h HIGHLOW
    0004404Eh HIGHLOW
    00044058h HIGHLOW
    0004409Ah HIGHLOW
    000440CEh HIGHLOW
    000440D8h HIGHLOW
    000440E8h HIGHLOW
    00044108h HIGHLOW
    00044113h HIGHLOW
    0004412Bh HIGHLOW
    0004414Ch HIGHLOW
    00044160h HIGHLOW
    00044192h HIGHLOW
    000441C0h HIGHLOW
    000441F3h HIGHLOW
    0004421Dh HIGHLOW
    00044234h HIGHLOW
    00044243h HIGHLOW
    00044272h HIGHLOW
    00044289h HIGHLOW
    0004436Eh HIGHLOW
    000443A0h HIGHLOW
    000443C1h HIGHLOW
    00044431h HIGHLOW
    00044455h HIGHLOW
    0004445Fh HIGHLOW
    00044494h HIGHLOW
    000444BBh HIGHLOW
    000444DFh HIGHLOW
    00044518h HIGHLOW
    00044675h HIGHLOW
    00044778h HIGHLOW
    000447AFh HIGHLOW
    000447D0h HIGHLOW
    00044805h HIGHLOW
    0004482Fh HIGHLOW
    0004485Ch HIGHLOW
    00044868h HIGHLOW
    00044890h HIGHLOW
    00044897h HIGHLOW
    000448C4h HIGHLOW
    000448E9h HIGHLOW
    000449D2h HIGHLOW
    00044AA7h HIGHLOW
    00044B20h HIGHLOW
    00044B62h HIGHLOW
    00044B77h HIGHLOW
    00044B96h HIGHLOW
    00044BEAh HIGHLOW
    00044C02h HIGHLOW
    00044C35h HIGHLOW
    00044C6Ch HIGHLOW
    00044CA8h HIGHLOW
    00044CB6h HIGHLOW
    00044CCBh HIGHLOW
    00044E2Ah HIGHLOW
    00044E32h HIGHLOW
    00044E43h HIGHLOW
    00044E71h HIGHLOW
    00044E7Dh HIGHLOW
    00044EA9h HIGHLOW
    00044EF2h HIGHLOW
    00044EF7h HIGHLOW
    00044F08h HIGHLOW
    00044F36h HIGHLOW
    00044F42h HIGHLOW
    00044F68h HIGHLOW
    00044F89h HIGHLOW
    00044F8Eh HIGHLOW
    00044F9Fh HIGHLOW
    00044FCDh HIGHLOW
    00044FD9h HIGHLOW
    00044FFFh HIGHLOW
    00044000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x45000   
SizeOfBlock:                   0xE0      
    000450C0h HIGHLOW
    000450C6h HIGHLOW
    000450CFh HIGHLOW
    000450D5h HIGHLOW
    000450EFh HIGHLOW
    000450F4h HIGHLOW
    000450FBh HIGHLOW
    0004510Bh HIGHLOW
    00045110h HIGHLOW
    00045117h HIGHLOW
    0004515Eh HIGHLOW
    00045181h HIGHLOW
    0004519Bh HIGHLOW
    000451A4h HIGHLOW
    000451B0h HIGHLOW
    000451C5h HIGHLOW
    000451FCh HIGHLOW
    00045250h HIGHLOW
    0004526Bh HIGHLOW
    00045277h HIGHLOW
    0004527Eh HIGHLOW
    0004528Bh HIGHLOW
    000452D2h HIGHLOW
    000452DEh HIGHLOW
    000452EEh HIGHLOW
    000452FCh HIGHLOW
    0004535Ah HIGHLOW
    00045371h HIGHLOW
    00045385h HIGHLOW
    0004539Eh HIGHLOW
    000453A7h HIGHLOW
    000453E1h HIGHLOW
    00045416h HIGHLOW
    0004543Ah HIGHLOW
    0004547Ch HIGHLOW
    000454FCh HIGHLOW
    00045549h HIGHLOW
    00045585h HIGHLOW
    000455C5h HIGHLOW
    000455F4h HIGHLOW
    00045634h HIGHLOW
    00045745h HIGHLOW
    00045797h HIGHLOW
    00045897h HIGHLOW
    000458ABh HIGHLOW
    000458B6h HIGHLOW
    000458BCh HIGHLOW
    000458C6h HIGHLOW
    000458CCh HIGHLOW
    000458D6h HIGHLOW
    000458DCh HIGHLOW
    000458E6h HIGHLOW
    000458ECh HIGHLOW
    000458F6h HIGHLOW
    000458FCh HIGHLOW
    00045906h HIGHLOW
    0004590Ch HIGHLOW
    00045916h HIGHLOW
    0004591Ch HIGHLOW
    00045926h HIGHLOW
    0004592Ch HIGHLOW
    00045936h HIGHLOW
    0004593Ch HIGHLOW
    00045946h HIGHLOW
    0004594Ch HIGHLOW
    00045956h HIGHLOW
    0004595Ch HIGHLOW
    00045966h HIGHLOW
    0004596Ch HIGHLOW
    00045976h HIGHLOW
    0004599Bh HIGHLOW
    000459C3h HIGHLOW
    000459D9h HIGHLOW
    000459EEh HIGHLOW
    00045A04h HIGHLOW
    00045A5Bh HIGHLOW
    00045A65h HIGHLOW
    00045A7Fh HIGHLOW
    00045A9Bh HIGHLOW
    00045AABh HIGHLOW
    00045AB6h HIGHLOW
    00045B07h HIGHLOW
    00045B79h HIGHLOW
    00045BA6h HIGHLOW
    00045C15h HIGHLOW
    00045C3Ch HIGHLOW
    00045C8Fh HIGHLOW
    00045C94h HIGHLOW
    00045C9Fh HIGHLOW
    00045CABh HIGHLOW
    00045CEBh HIGHLOW
    00045D15h HIGHLOW
    00045D25h HIGHLOW
    00045D38h HIGHLOW
    00045D42h HIGHLOW
    00045DADh HIGHLOW
    00045DCCh HIGHLOW
    00045DEBh HIGHLOW
    00045E85h HIGHLOW
    00045E95h HIGHLOW
    00045EAEh HIGHLOW
    00045F30h HIGHLOW
    00045F45h HIGHLOW
    00045F5Ah HIGHLOW
    00045F6Ah HIGHLOW
    00045F7Ah HIGHLOW
    00045FFEh HIGHLOW
    00045000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x46000   
SizeOfBlock:                   0x78      
    00046003h HIGHLOW
    00046051h HIGHLOW
    00046101h HIGHLOW
    00046107h HIGHLOW
    0004610Fh HIGHLOW
    00046186h HIGHLOW
    000461F8h HIGHLOW
    000462EAh HIGHLOW
    000462FDh HIGHLOW
    0004635Ch HIGHLOW
    00046385h HIGHLOW
    00046398h HIGHLOW
    000463F7h HIGHLOW
    0004657Fh HIGHLOW
    000465D5h HIGHLOW
    0004671Fh HIGHLOW
    00046752h HIGHLOW
    00046794h HIGHLOW
    000467BEh HIGHLOW
    000467E9h HIGHLOW
    000467F2h HIGHLOW
    0004680Ch HIGHLOW
    00046871h HIGHLOW
    00046889h HIGHLOW
    00046902h HIGHLOW
    0004691Eh HIGHLOW
    00046B50h HIGHLOW
    00046C1Bh HIGHLOW
    00046C95h HIGHLOW
    00046C9Ah HIGHLOW
    00046CB3h HIGHLOW
    00046CCDh HIGHLOW
    00046CD6h HIGHLOW
    00046D1Eh HIGHLOW
    00046D30h HIGHLOW
    00046D35h HIGHLOW
    00046D4Ch HIGHLOW
    00046D51h HIGHLOW
    00046DAAh HIGHLOW
    00046DAFh HIGHLOW
    00046DC4h HIGHLOW
    00046DC9h HIGHLOW
    00046DD0h HIGHLOW
    00046DD5h HIGHLOW
    00046E78h HIGHLOW
    00046E8Fh HIGHLOW
    00046E94h HIGHLOW
    00046EC2h HIGHLOW
    00046F04h HIGHLOW
    00046F09h HIGHLOW
    00046F3Ch HIGHLOW
    00046F41h HIGHLOW
    00046F74h HIGHLOW
    00046FB2h HIGHLOW
    00046FB7h HIGHLOW
    00046000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x47000   
SizeOfBlock:                   0xB0      
    00047016h HIGHLOW
    0004701Bh HIGHLOW
    00047026h HIGHLOW
    0004702Bh HIGHLOW
    000470B3h HIGHLOW
    000470B8h HIGHLOW
    000470EDh HIGHLOW
    00047105h HIGHLOW
    0004713Ch HIGHLOW
    0004714Fh HIGHLOW
    00047161h HIGHLOW
    000471B5h HIGHLOW
    000471C1h HIGHLOW
    0004722Fh HIGHLOW
    00047234h HIGHLOW
    00047270h HIGHLOW
    000472B7h HIGHLOW
    00047304h HIGHLOW
    0004731Bh HIGHLOW
    00047320h HIGHLOW
    00047335h HIGHLOW
    0004733Ah HIGHLOW
    000473ADh HIGHLOW
    000473CDh HIGHLOW
    000473D2h HIGHLOW
    000473DCh HIGHLOW
    000473E1h HIGHLOW
    00047401h HIGHLOW
    00047419h HIGHLOW
    00047434h HIGHLOW
    00047455h HIGHLOW
    00047540h HIGHLOW
    00047583h HIGHLOW
    00047588h HIGHLOW
    000475B8h HIGHLOW
    000475BDh HIGHLOW
    000475C9h HIGHLOW
    000475CEh HIGHLOW
    000475FEh HIGHLOW
    0004764Ch HIGHLOW
    00047651h HIGHLOW
    000476E9h HIGHLOW
    000476FAh HIGHLOW
    0004770Ch HIGHLOW
    00047730h HIGHLOW
    00047781h HIGHLOW
    000477A2h HIGHLOW
    000477BDh HIGHLOW
    000477E7h HIGHLOW
    000478A5h HIGHLOW
    000478B5h HIGHLOW
    000478BAh HIGHLOW
    000478CAh HIGHLOW
    000478CFh HIGHLOW
    000478E8h HIGHLOW
    000478F3h HIGHLOW
    0004791Ah HIGHLOW
    0004793Ch HIGHLOW
    000479A9h HIGHLOW
    000479BCh HIGHLOW
    00047A0Bh HIGHLOW
    00047A3Ah HIGHLOW
    00047A6Ah HIGHLOW
    00047A90h HIGHLOW
    00047AA7h HIGHLOW
    00047B40h HIGHLOW
    00047B4Fh HIGHLOW
    00047B78h HIGHLOW
    00047B8Bh HIGHLOW
    00047BD7h HIGHLOW
    00047C01h HIGHLOW
    00047C17h HIGHLOW
    00047C8Eh HIGHLOW
    00047CECh HIGHLOW
    00047D22h HIGHLOW
    00047D62h HIGHLOW
    00047D96h HIGHLOW
    00047DF9h HIGHLOW
    00047EADh HIGHLOW
    00047F4Bh HIGHLOW
    00047F82h HIGHLOW
    00047FBDh HIGHLOW
    00047FDEh HIGHLOW
    00047000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x48000   
SizeOfBlock:                   0x34      
    0004800Ch HIGHLOW
    0004805Eh HIGHLOW
    00048080h HIGHLOW
    000480A2h HIGHLOW
    000480CAh HIGHLOW
    00048142h HIGHLOW
    00048164h HIGHLOW
    00048186h HIGHLOW
    000481AEh HIGHLOW
    000481D7h HIGHLOW
    0004822Ah HIGHLOW
    000487B0h HIGHLOW
    000487ECh HIGHLOW
    00048917h HIGHLOW
    0004897Dh HIGHLOW
    000489A2h HIGHLOW
    00048A6Eh HIGHLOW
    00048BA8h HIGHLOW
    00048C57h HIGHLOW
    00048CB5h HIGHLOW
    00048CD5h HIGHLOW
    00048F16h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x49000   
SizeOfBlock:                   0x5C      
    000490D8h HIGHLOW
    00049101h HIGHLOW
    00049138h HIGHLOW
    00049144h HIGHLOW
    0004915Eh HIGHLOW
    00049163h HIGHLOW
    0004916Eh HIGHLOW
    00049454h HIGHLOW
    00049459h HIGHLOW
    0004949Dh HIGHLOW
    000494A2h HIGHLOW
    000494F8h HIGHLOW
    000494FDh HIGHLOW
    00049562h HIGHLOW
    00049572h HIGHLOW
    000495DBh HIGHLOW
    00049611h HIGHLOW
    0004963Dh HIGHLOW
    0004964Dh HIGHLOW
    00049683h HIGHLOW
    0004968Fh HIGHLOW
    000496BDh HIGHLOW
    0004973Bh HIGHLOW
    00049780h HIGHLOW
    00049845h HIGHLOW
    0004994Fh HIGHLOW
    00049AADh HIGHLOW
    00049AB8h HIGHLOW
    00049B34h HIGHLOW
    00049BBDh HIGHLOW
    00049C0Fh HIGHLOW
    00049C28h HIGHLOW
    00049CB6h HIGHLOW
    00049CF0h HIGHLOW
    00049D83h HIGHLOW
    00049DD1h HIGHLOW
    00049E10h HIGHLOW
    00049E59h HIGHLOW
    00049E5Eh HIGHLOW
    00049E8Ah HIGHLOW
    00049E9Ah HIGHLOW
    00049000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4A000   
SizeOfBlock:                   0x4C      
    0004A01Ah HIGHLOW
    0004A061h HIGHLOW
    0004A09Ah HIGHLOW
    0004A0E1h HIGHLOW
    0004A129h HIGHLOW
    0004A12Eh HIGHLOW
    0004A17Eh HIGHLOW
    0004A19Bh HIGHLOW
    0004A219h HIGHLOW
    0004A281h HIGHLOW
    0004A2B5h HIGHLOW
    0004A309h HIGHLOW
    0004A391h HIGHLOW
    0004A487h HIGHLOW
    0004A503h HIGHLOW
    0004A60Dh HIGHLOW
    0004A6BEh HIGHLOW
    0004A716h HIGHLOW
    0004A7BCh HIGHLOW
    0004A824h HIGHLOW
    0004A858h HIGHLOW
    0004A8ACh HIGHLOW
    0004A934h HIGHLOW
    0004AA2Bh HIGHLOW
    0004AAE1h HIGHLOW
    0004AC19h HIGHLOW
    0004ACDCh HIGHLOW
    0004AD8Ah HIGHLOW
    0004AE3Dh HIGHLOW
    0004AE92h HIGHLOW
    0004AF35h HIGHLOW
    0004AFA0h HIGHLOW
    0004AFD2h HIGHLOW
    0004A000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4B000   
SizeOfBlock:                   0x3C      
    0004B025h HIGHLOW
    0004B041h HIGHLOW
    0004B0AEh HIGHLOW
    0004B1A0h HIGHLOW
    0004B24Fh HIGHLOW
    0004B321h HIGHLOW
    0004B351h HIGHLOW
    0004B4D6h HIGHLOW
    0004B4DFh HIGHLOW
    0004B4F8h HIGHLOW
    0004B50Bh HIGHLOW
    0004B512h HIGHLOW
    0004B583h HIGHLOW
    0004B617h HIGHLOW
    0004B63Ch HIGHLOW
    0004B69Eh HIGHLOW
    0004B8B5h HIGHLOW
    0004B915h HIGHLOW
    0004B995h HIGHLOW
    0004B9F8h HIGHLOW
    0004BA70h HIGHLOW
    0004BAB0h HIGHLOW
    0004BAD5h HIGHLOW
    0004BAE6h HIGHLOW
    0004BBCFh HIGHLOW
    0004BBDCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4C000   
SizeOfBlock:                   0x40      
    0004C583h HIGHLOW
    0004C58Ah HIGHLOW
    0004C5A3h HIGHLOW
    0004C5C6h HIGHLOW
    0004C65Fh HIGHLOW
    0004C6A3h HIGHLOW
    0004C6B3h HIGHLOW
    0004C6CDh HIGHLOW
    0004C6FCh HIGHLOW
    0004C740h HIGHLOW
    0004C747h HIGHLOW
    0004C760h HIGHLOW
    0004C783h HIGHLOW
    0004C822h HIGHLOW
    0004C866h HIGHLOW
    0004C87Ah HIGHLOW
    0004C8B9h HIGHLOW
    0004C8DCh HIGHLOW
    0004C975h HIGHLOW
    0004C9ACh HIGHLOW
    0004C9B7h HIGHLOW
    0004C9C7h HIGHLOW
    0004CE7Ah HIGHLOW
    0004CE9Dh HIGHLOW
    0004CF3Ah HIGHLOW
    0004CF71h HIGHLOW
    0004CF7Ch HIGHLOW
    0004CF8Ch HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4D000   
SizeOfBlock:                   0x44      
    0004D235h HIGHLOW
    0004D23Ah HIGHLOW
    0004D30Ch HIGHLOW
    0004D380h HIGHLOW
    0004D385h HIGHLOW
    0004D3A7h HIGHLOW
    0004D3ACh HIGHLOW
    0004D3D0h HIGHLOW
    0004D3D5h HIGHLOW
    0004D3FCh HIGHLOW
    0004D401h HIGHLOW
    0004D425h HIGHLOW
    0004D42Ah HIGHLOW
    0004D476h HIGHLOW
    0004D47Bh HIGHLOW
    0004D4D7h HIGHLOW
    0004D52Bh HIGHLOW
    0004D5FCh HIGHLOW
    0004D7ABh HIGHLOW
    0004D822h HIGHLOW
    0004DBA7h HIGHLOW
    0004DC18h HIGHLOW
    0004DC2Ch HIGHLOW
    0004DCE4h HIGHLOW
    0004DF3Dh HIGHLOW
    0004DF5Eh HIGHLOW
    0004DF7Dh HIGHLOW
    0004DF93h HIGHLOW
    0004DFB4h HIGHLOW
    0004DFF8h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4E000   
SizeOfBlock:                   0x54      
    0004E049h HIGHLOW
    0004E0B2h HIGHLOW
    0004E0D0h HIGHLOW
    0004E0EEh HIGHLOW
    0004E119h HIGHLOW
    0004E144h HIGHLOW
    0004E166h HIGHLOW
    0004E184h HIGHLOW
    0004E1A1h HIGHLOW
    0004E1C1h HIGHLOW
    0004E1E5h HIGHLOW
    0004E24Ah HIGHLOW
    0004E295h HIGHLOW
    0004E2C4h HIGHLOW
    0004E2E0h HIGHLOW
    0004E30Ah HIGHLOW
    0004E325h HIGHLOW
    0004E339h HIGHLOW
    0004E384h HIGHLOW
    0004E3B7h HIGHLOW
    0004E3E7h HIGHLOW
    0004E408h HIGHLOW
    0004E46Fh HIGHLOW
    0004E4E3h HIGHLOW
    0004E513h HIGHLOW
    0004E540h HIGHLOW
    0004E549h HIGHLOW
    0004E54Fh HIGHLOW
    0004E57Ah HIGHLOW
    0004E599h HIGHLOW
    0004E5C3h HIGHLOW
    0004E5CAh HIGHLOW
    0004E5EEh HIGHLOW
    0004E61Ah HIGHLOW
    0004E645h HIGHLOW
    0004E67Fh HIGHLOW
    0004E68Ah HIGHLOW
    0004EC90h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x4F000   
SizeOfBlock:                   0x38      
    0004F6E5h HIGHLOW
    0004F71Ch HIGHLOW
    0004F7BAh HIGHLOW
    0004F7DAh HIGHLOW
    0004F7E6h HIGHLOW
    0004F80Ch HIGHLOW
    0004F8C2h HIGHLOW
    0004F8F7h HIGHLOW
    0004F963h HIGHLOW
    0004F99Bh HIGHLOW
    0004F9C2h HIGHLOW
    0004F9D5h HIGHLOW
    0004F9DBh HIGHLOW
    0004F9FEh HIGHLOW
    0004FA04h HIGHLOW
    0004FA2Fh HIGHLOW
    0004FA35h HIGHLOW
    0004FA8Ah HIGHLOW
    0004FA90h HIGHLOW
    0004FAA1h HIGHLOW
    0004FAA7h HIGHLOW
    0004FD59h HIGHLOW
    0004FD82h HIGHLOW
    0004FD89h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x50000   
SizeOfBlock:                   0x38      
    0005009Dh HIGHLOW
    000501AFh HIGHLOW
    000501E0h HIGHLOW
    00050217h HIGHLOW
    0005022Ah HIGHLOW
    00050245h HIGHLOW
    000503E9h HIGHLOW
    00050604h HIGHLOW
    00050714h HIGHLOW
    0005085Eh HIGHLOW
    00050890h HIGHLOW
    0005095Dh HIGHLOW
    00050A13h HIGHLOW
    00050A67h HIGHLOW
    00050B27h HIGHLOW
    00050BAEh HIGHLOW
    00050C47h HIGHLOW
    00050C82h HIGHLOW
    00050CCCh HIGHLOW
    00050DEFh HIGHLOW
    00050ED9h HIGHLOW
    00050F31h HIGHLOW
    00050F8Fh HIGHLOW
    00050000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x51000   
SizeOfBlock:                   0xC0      
    0005101Fh HIGHLOW
    00051193h HIGHLOW
    000512F3h HIGHLOW
    000513AEh HIGHLOW
    000513C0h HIGHLOW
    000513D5h HIGHLOW
    000513DCh HIGHLOW
    0005140Bh HIGHLOW
    00051429h HIGHLOW
    0005148Ah HIGHLOW
    000514DCh HIGHLOW
    00051528h HIGHLOW
    000515ABh HIGHLOW
    000515CEh HIGHLOW
    000515F6h HIGHLOW
    00051642h HIGHLOW
    00051681h HIGHLOW
    00051697h HIGHLOW
    000516B0h HIGHLOW
    000516BFh HIGHLOW
    000516C8h HIGHLOW
    000516E1h HIGHLOW
    00051720h HIGHLOW
    00051743h HIGHLOW
    00051752h HIGHLOW
    0005175Bh HIGHLOW
    00051777h HIGHLOW
    00051788h HIGHLOW
    00051794h HIGHLOW
    000517FDh HIGHLOW
    00051849h HIGHLOW
    00051867h HIGHLOW
    00051873h HIGHLOW
    000518EDh HIGHLOW
    0005194Ch HIGHLOW
    00051955h HIGHLOW
    0005197Bh HIGHLOW
    000519DEh HIGHLOW
    000519FDh HIGHLOW
    00051A02h HIGHLOW
    00051A27h HIGHLOW
    00051A37h HIGHLOW
    00051A82h HIGHLOW
    00051A87h HIGHLOW
    00051A9Dh HIGHLOW
    00051AC4h HIGHLOW
    00051ADFh HIGHLOW
    00051AEFh HIGHLOW
    00051B2Bh HIGHLOW
    00051B30h HIGHLOW
    00051B69h HIGHLOW
    00051B6Eh HIGHLOW
    00051B90h HIGHLOW
    00051B95h HIGHLOW
    00051BC2h HIGHLOW
    00051BC8h HIGHLOW
    00051BEDh HIGHLOW
    00051BF6h HIGHLOW
    00051C10h HIGHLOW
    00051C41h HIGHLOW
    00051C53h HIGHLOW
    00051C58h HIGHLOW
    00051C82h HIGHLOW
    00051C87h HIGHLOW
    00051CB6h HIGHLOW
    00051CD5h HIGHLOW
    00051CDCh HIGHLOW
    00051CF3h HIGHLOW
    00051D22h HIGHLOW
    00051D2Bh HIGHLOW
    00051D4Fh HIGHLOW
    00051D71h HIGHLOW
    00051D8Ch HIGHLOW
    00051DADh HIGHLOW
    00051DB4h HIGHLOW
    00051DDBh HIGHLOW
    00051DE0h HIGHLOW
    00051E18h HIGHLOW
    00051E28h HIGHLOW
    00051E4Bh HIGHLOW
    00051E62h HIGHLOW
    00051E6Bh HIGHLOW
    00051E9Bh HIGHLOW
    00051EC0h HIGHLOW
    00051EC7h HIGHLOW
    00051F20h HIGHLOW
    00051F30h HIGHLOW
    00051F51h HIGHLOW
    00051F92h HIGHLOW
    00051F9Bh HIGHLOW
    00051FC8h HIGHLOW
    00051FF1h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x52000   
SizeOfBlock:                   0x8C      
    00052018h HIGHLOW
    00052028h HIGHLOW
    0005204Eh HIGHLOW
    000520C5h HIGHLOW
    000520CEh HIGHLOW
    00052181h HIGHLOW
    00052238h HIGHLOW
    00052251h HIGHLOW
    0005225Ah HIGHLOW
    00052288h HIGHLOW
    000522DAh HIGHLOW
    00052307h HIGHLOW
    0005230Eh HIGHLOW
    00052334h HIGHLOW
    00052347h HIGHLOW
    00052352h HIGHLOW
    000523E4h HIGHLOW
    000523EFh HIGHLOW
    00052424h HIGHLOW
    0005245Bh HIGHLOW
    00052479h HIGHLOW
    00052497h HIGHLOW
    000524B5h HIGHLOW
    000524E3h HIGHLOW
    000524EEh HIGHLOW
    0005251Bh HIGHLOW
    00052566h HIGHLOW
    00052580h HIGHLOW
    000525B7h HIGHLOW
    000525C2h HIGHLOW
    000525EAh HIGHLOW
    00052700h HIGHLOW
    00052709h HIGHLOW
    0005275Ah HIGHLOW
    00052772h HIGHLOW
    00052778h HIGHLOW
    0005279Dh HIGHLOW
    000527BCh HIGHLOW
    000527C5h HIGHLOW
    0005284Bh HIGHLOW
    00052854h HIGHLOW
    0005288Ch HIGHLOW
    000528C2h HIGHLOW
    00052938h HIGHLOW
    0005293Dh HIGHLOW
    0005294Ch HIGHLOW
    00052954h HIGHLOW
    00052989h HIGHLOW
    00052992h HIGHLOW
    000529E8h HIGHLOW
    00052A02h HIGHLOW
    00052A74h HIGHLOW
    00052A79h HIGHLOW
    00052A85h HIGHLOW
    00052AC5h HIGHLOW
    00052ACEh HIGHLOW
    00052B1Ah HIGHLOW
    00052BAEh HIGHLOW
    00052BF7h HIGHLOW
    00052BFDh HIGHLOW
    00052C27h HIGHLOW
    00052CB7h HIGHLOW
    00052DD1h HIGHLOW
    00052EBAh HIGHLOW
    00052FBCh HIGHLOW
    00052000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x53000   
SizeOfBlock:                   0x64      
    000530FCh HIGHLOW
    00053200h HIGHLOW
    00053383h HIGHLOW
    000534D9h HIGHLOW
    000534FFh HIGHLOW
    00053517h HIGHLOW
    00053550h HIGHLOW
    0005355Bh HIGHLOW
    000535BDh HIGHLOW
    0005367Dh HIGHLOW
    00053697h HIGHLOW
    000536BAh HIGHLOW
    000536F0h HIGHLOW
    0005373Ch HIGHLOW
    000537D0h HIGHLOW
    00053809h HIGHLOW
    0005385Fh HIGHLOW
    00053949h HIGHLOW
    000539A6h HIGHLOW
    000539CBh HIGHLOW
    000539DBh HIGHLOW
    000539E8h HIGHLOW
    000539FFh HIGHLOW
    00053A78h HIGHLOW
    00053B23h HIGHLOW
    00053B60h HIGHLOW
    00053B98h HIGHLOW
    00053C15h HIGHLOW
    00053C38h HIGHLOW
    00053C59h HIGHLOW
    00053C76h HIGHLOW
    00053C9Eh HIGHLOW
    00053CFCh HIGHLOW
    00053D16h HIGHLOW
    00053D1Fh HIGHLOW
    00053D3Ch HIGHLOW
    00053D52h HIGHLOW
    00053D73h HIGHLOW
    00053D89h HIGHLOW
    00053E26h HIGHLOW
    00053E65h HIGHLOW
    00053E6Eh HIGHLOW
    00053E8Eh HIGHLOW
    00053F10h HIGHLOW
    00053FFBh HIGHLOW
    00053000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x54000   
SizeOfBlock:                   0x88      
    00054004h HIGHLOW
    00054035h HIGHLOW
    0005403Eh HIGHLOW
    00054050h HIGHLOW
    0005407Eh HIGHLOW
    0005409Eh HIGHLOW
    000540CBh HIGHLOW
    000541DEh HIGHLOW
    000541F5h HIGHLOW
    000541FEh HIGHLOW
    00054285h HIGHLOW
    000542B0h HIGHLOW
    000542C9h HIGHLOW
    000542D2h HIGHLOW
    0005430Ah HIGHLOW
    00054313h HIGHLOW
    0005432Bh HIGHLOW
    000543D9h HIGHLOW
    00054464h HIGHLOW
    00054472h HIGHLOW
    0005449Fh HIGHLOW
    000544FAh HIGHLOW
    0005453Ch HIGHLOW
    00054558h HIGHLOW
    0005456Dh HIGHLOW
    000545C8h HIGHLOW
    000546D5h HIGHLOW
    00054766h HIGHLOW
    0005476Eh HIGHLOW
    000547A7h HIGHLOW
    000548F8h HIGHLOW
    000549B0h HIGHLOW
    000549FFh HIGHLOW
    00054AC0h HIGHLOW
    00054B28h HIGHLOW
    00054B59h HIGHLOW
    00054B64h HIGHLOW
    00054B7Fh HIGHLOW
    00054B91h HIGHLOW
    00054BBCh HIGHLOW
    00054C26h HIGHLOW
    00054C59h HIGHLOW
    00054C67h HIGHLOW
    00054C87h HIGHLOW
    00054C99h HIGHLOW
    00054CC9h HIGHLOW
    00054D01h HIGHLOW
    00054D4Bh HIGHLOW
    00054D6Dh HIGHLOW
    00054D79h HIGHLOW
    00054DA4h HIGHLOW
    00054DAEh HIGHLOW
    00054DBCh HIGHLOW
    00054DECh HIGHLOW
    00054E26h HIGHLOW
    00054E5Dh HIGHLOW
    00054E73h HIGHLOW
    00054EE6h HIGHLOW
    00054F1Bh HIGHLOW
    00054F7Bh HIGHLOW
    00054F81h HIGHLOW
    00054FADh HIGHLOW
    00054FDCh HIGHLOW
    00054000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x55000   
SizeOfBlock:                   0x94      
    0005508Ah HIGHLOW
    000550AEh HIGHLOW
    000550E2h HIGHLOW
    00055114h HIGHLOW
    0005513Ch HIGHLOW
    0005515Fh HIGHLOW
    00055187h HIGHLOW
    000551A6h HIGHLOW
    00055210h HIGHLOW
    00055263h HIGHLOW
    0005527Ah HIGHLOW
    00055283h HIGHLOW
    000552AAh HIGHLOW
    000552BEh HIGHLOW
    000552D5h HIGHLOW
    00055370h HIGHLOW
    000553C8h HIGHLOW
    000553DAh HIGHLOW
    00055429h HIGHLOW
    0005545Ah HIGHLOW
    00055483h HIGHLOW
    000554EDh HIGHLOW
    000554FCh HIGHLOW
    00055562h HIGHLOW
    00055568h HIGHLOW
    00055580h HIGHLOW
    0005558Dh HIGHLOW
    00055594h HIGHLOW
    000555A7h HIGHLOW
    0005561Eh HIGHLOW
    00055627h HIGHLOW
    00055647h HIGHLOW
    0005566Ch HIGHLOW
    00055677h HIGHLOW
    0005571Ah HIGHLOW
    00055725h HIGHLOW
    0005573Bh HIGHLOW
    00055748h HIGHLOW
    0005575Dh HIGHLOW
    00055771h HIGHLOW
    0005579Fh HIGHLOW
    00055821h HIGHLOW
    00055863h HIGHLOW
    00055896h HIGHLOW
    000558D7h HIGHLOW
    000559F4h HIGHLOW
    00055A3Bh HIGHLOW
    00055AB9h HIGHLOW
    00055ACBh HIGHLOW
    00055ADAh HIGHLOW
    00055B01h HIGHLOW
    00055B1Ch HIGHLOW
    00055B55h HIGHLOW
    00055BC1h HIGHLOW
    00055BD7h HIGHLOW
    00055BFBh HIGHLOW
    00055C15h HIGHLOW
    00055C22h HIGHLOW
    00055C6Dh HIGHLOW
    00055C7Bh HIGHLOW
    00055C93h HIGHLOW
    00055CA0h HIGHLOW
    00055CC6h HIGHLOW
    00055CD2h HIGHLOW
    00055CFFh HIGHLOW
    00055D48h HIGHLOW
    00055DC2h HIGHLOW
    00055DEEh HIGHLOW
    00055EB7h HIGHLOW
    00055FE3h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x56000   
SizeOfBlock:                   0x7C      
    0005602Bh HIGHLOW
    00056060h HIGHLOW
    000560BFh HIGHLOW
    0005618Ah HIGHLOW
    00056196h HIGHLOW
    000561F3h HIGHLOW
    000561FCh HIGHLOW
    00056212h HIGHLOW
    00056241h HIGHLOW
    00056278h HIGHLOW
    00056297h HIGHLOW
    000564D5h HIGHLOW
    00056526h HIGHLOW
    00056544h HIGHLOW
    000565CAh HIGHLOW
    0005663Eh HIGHLOW
    0005666Dh HIGHLOW
    00056749h HIGHLOW
    000567F0h HIGHLOW
    00056816h HIGHLOW
    00056833h HIGHLOW
    00056855h HIGHLOW
    00056889h HIGHLOW
    000568A6h HIGHLOW
    000568C1h HIGHLOW
    000568E3h HIGHLOW
    000568F3h HIGHLOW
    0005692Bh HIGHLOW
    0005694Ch HIGHLOW
    0005696Fh HIGHLOW
    0005697Fh HIGHLOW
    000569B7h HIGHLOW
    000569D8h HIGHLOW
    000569F7h HIGHLOW
    00056A44h HIGHLOW
    00056A6Bh HIGHLOW
    00056A92h HIGHLOW
    00056AB9h HIGHLOW
    00056AEBh HIGHLOW
    00056B11h HIGHLOW
    00056B84h HIGHLOW
    00056BB7h HIGHLOW
    00056BBDh HIGHLOW
    00056BD5h HIGHLOW
    00056BF4h HIGHLOW
    00056BFEh HIGHLOW
    00056C31h HIGHLOW
    00056C96h HIGHLOW
    00056CCCh HIGHLOW
    00056CDFh HIGHLOW
    00056D40h HIGHLOW
    00056E54h HIGHLOW
    00056EB8h HIGHLOW
    00056EEDh HIGHLOW
    00056F7Ch HIGHLOW
    00056F8Eh HIGHLOW
    00056FA5h HIGHLOW
    00056000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x57000   
SizeOfBlock:                   0x78      
    00057005h HIGHLOW
    00057026h HIGHLOW
    000570B2h HIGHLOW
    000570D1h HIGHLOW
    000570DDh HIGHLOW
    000570FFh HIGHLOW
    000571B4h HIGHLOW
    000571D3h HIGHLOW
    0005721Fh HIGHLOW
    00057309h HIGHLOW
    0005732Ah HIGHLOW
    000573B9h HIGHLOW
    000573D9h HIGHLOW
    000573E5h HIGHLOW
    0005740Bh HIGHLOW
    000574B5h HIGHLOW
    000574DCh HIGHLOW
    000574F6h HIGHLOW
    00057511h HIGHLOW
    00057522h HIGHLOW
    0005753Eh HIGHLOW
    0005757Bh HIGHLOW
    000575BDh HIGHLOW
    00057627h HIGHLOW
    0005763Fh HIGHLOW
    0005764Bh HIGHLOW
    0005767Ch HIGHLOW
    00057691h HIGHLOW
    0005774Ch HIGHLOW
    0005776Dh HIGHLOW
    00057825h HIGHLOW
    00057859h HIGHLOW
    00057920h HIGHLOW
    0005795Bh HIGHLOW
    00057964h HIGHLOW
    000579ACh HIGHLOW
    000579BBh HIGHLOW
    000579E2h HIGHLOW
    00057A22h HIGHLOW
    00057A2Fh HIGHLOW
    00057A87h HIGHLOW
    00057AE2h HIGHLOW
    00057B55h HIGHLOW
    00057BB8h HIGHLOW
    00057BF7h HIGHLOW
    00057C2Dh HIGHLOW
    00057D2Fh HIGHLOW
    00057D74h HIGHLOW
    00057D7Dh HIGHLOW
    00057DB6h HIGHLOW
    00057E56h HIGHLOW
    00057E5Fh HIGHLOW
    00057F80h HIGHLOW
    00057FC3h HIGHLOW
    00057FE9h HIGHLOW
    00057000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x58000   
SizeOfBlock:                   0xDC      
    0005803Eh HIGHLOW
    00058084h HIGHLOW
    000580E5h HIGHLOW
    0005810Ah HIGHLOW
    0005813Eh HIGHLOW
    0005814Ah HIGHLOW
    00058160h HIGHLOW
    000581D1h HIGHLOW
    0005822Ah HIGHLOW
    00058236h HIGHLOW
    0005827Ah HIGHLOW
    000582B6h HIGHLOW
    000582D7h HIGHLOW
    000582EAh HIGHLOW
    0005832Eh HIGHLOW
    00058361h HIGHLOW
    0005837Fh HIGHLOW
    000583A3h HIGHLOW
    000583D6h HIGHLOW
    000583E4h HIGHLOW
    00058402h HIGHLOW
    0005842Ch HIGHLOW
    00058433h HIGHLOW
    0005843Bh HIGHLOW
    00058442h HIGHLOW
    00058455h HIGHLOW
    0005845Bh HIGHLOW
    0005846Bh HIGHLOW
    00058473h HIGHLOW
    0005847Eh HIGHLOW
    00058497h HIGHLOW
    000584B0h HIGHLOW
    000584CAh HIGHLOW
    000584E9h HIGHLOW
    0005851Eh HIGHLOW
    0005852Bh HIGHLOW
    00058561h HIGHLOW
    0005859Dh HIGHLOW
    000585ADh HIGHLOW
    000585BFh HIGHLOW
    000585C8h HIGHLOW
    000585D4h HIGHLOW
    00058617h HIGHLOW
    00058656h HIGHLOW
    00058680h HIGHLOW
    000586B1h HIGHLOW
    000586D9h HIGHLOW
    000586F0h HIGHLOW
    00058715h HIGHLOW
    0005871Eh HIGHLOW
    00058758h HIGHLOW
    00058793h HIGHLOW
    000587BFh HIGHLOW
    000587E6h HIGHLOW
    000587FBh HIGHLOW
    0005884Eh HIGHLOW
    0005888Ch HIGHLOW
    00058898h HIGHLOW
    000588A3h HIGHLOW
    000588FEh HIGHLOW
    0005890Ah HIGHLOW
    0005891Ch HIGHLOW
    00058935h HIGHLOW
    0005897Fh HIGHLOW
    000589AEh HIGHLOW
    000589C5h HIGHLOW
    000589FFh HIGHLOW
    00058A15h HIGHLOW
    00058A3Ah HIGHLOW
    00058A52h HIGHLOW
    00058A65h HIGHLOW
    00058AA8h HIGHLOW
    00058AEBh HIGHLOW
    00058B19h HIGHLOW
    00058B71h HIGHLOW
    00058B78h HIGHLOW
    00058B83h HIGHLOW
    00058BAFh HIGHLOW
    00058BF1h HIGHLOW
    00058C21h HIGHLOW
    00058C64h HIGHLOW
    00058C74h HIGHLOW
    00058CBBh HIGHLOW
    00058CD0h HIGHLOW
    00058CE0h HIGHLOW
    00058D22h HIGHLOW
    00058D4Ch HIGHLOW
    00058D89h HIGHLOW
    00058D92h HIGHLOW
    00058D9Dh HIGHLOW
    00058DB0h HIGHLOW
    00058DBBh HIGHLOW
    00058DCEh HIGHLOW
    00058DD9h HIGHLOW
    00058DECh HIGHLOW
    00058DF7h HIGHLOW
    00058E0Ch HIGHLOW
    00058E34h HIGHLOW
    00058EB0h HIGHLOW
    00058EEDh HIGHLOW
    00058EF5h HIGHLOW
    00058F30h HIGHLOW
    00058F58h HIGHLOW
    00058F7Eh HIGHLOW
    00058F8Bh HIGHLOW
    00058000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x59000   
SizeOfBlock:                   0xD0      
    00059028h HIGHLOW
    00059035h HIGHLOW
    0005903Fh HIGHLOW
    00059087h HIGHLOW
    000590A5h HIGHLOW
    000590C2h HIGHLOW
    0005911Ch HIGHLOW
    00059131h HIGHLOW
    00059153h HIGHLOW
    00059160h HIGHLOW
    000591B3h HIGHLOW
    000591C1h HIGHLOW
    0005922Ah HIGHLOW
    00059237h HIGHLOW
    00059241h HIGHLOW
    0005928Fh HIGHLOW
    000592ADh HIGHLOW
    000592CAh HIGHLOW
    00059331h HIGHLOW
    00059346h HIGHLOW
    0005937Bh HIGHLOW
    0005938Bh HIGHLOW
    000593A9h HIGHLOW
    000593D3h HIGHLOW
    000593FAh HIGHLOW
    0005940Dh HIGHLOW
    00059444h HIGHLOW
    00059460h HIGHLOW
    00059475h HIGHLOW
    000594A0h HIGHLOW
    000594BCh HIGHLOW
    000594CAh HIGHLOW
    00059516h HIGHLOW
    0005956Ah HIGHLOW
    0005958Fh HIGHLOW
    000595CDh HIGHLOW
    000595FFh HIGHLOW
    0005960Ah HIGHLOW
    00059640h HIGHLOW
    00059682h HIGHLOW
    00059723h HIGHLOW
    0005975Bh HIGHLOW
    0005978Ah HIGHLOW
    000597F4h HIGHLOW
    00059808h HIGHLOW
    00059835h HIGHLOW
    0005986Ah HIGHLOW
    00059874h HIGHLOW
    0005987Bh HIGHLOW
    00059889h HIGHLOW
    00059894h HIGHLOW
    0005989Ah HIGHLOW
    000598ABh HIGHLOW
    000598BBh HIGHLOW
    000598DBh HIGHLOW
    00059907h HIGHLOW
    00059932h HIGHLOW
    0005995Dh HIGHLOW
    00059978h HIGHLOW
    00059993h HIGHLOW
    000599BFh HIGHLOW
    000599F2h HIGHLOW
    00059A46h HIGHLOW
    00059A54h HIGHLOW
    00059A8Ah HIGHLOW
    00059AD7h HIGHLOW
    00059B08h HIGHLOW
    00059B18h HIGHLOW
    00059B20h HIGHLOW
    00059B26h HIGHLOW
    00059B2Eh HIGHLOW
    00059B36h HIGHLOW
    00059B55h HIGHLOW
    00059B6Fh HIGHLOW
    00059B83h HIGHLOW
    00059BB9h HIGHLOW
    00059C2Ch HIGHLOW
    00059C31h HIGHLOW
    00059C50h HIGHLOW
    00059C55h HIGHLOW
    00059C64h HIGHLOW
    00059CA9h HIGHLOW
    00059CD1h HIGHLOW
    00059CFAh HIGHLOW
    00059D07h HIGHLOW
    00059D47h HIGHLOW
    00059DD4h HIGHLOW
    00059DF9h HIGHLOW
    00059E28h HIGHLOW
    00059E35h HIGHLOW
    00059EEDh HIGHLOW
    00059F04h HIGHLOW
    00059F0Ah HIGHLOW
    00059F89h HIGHLOW
    00059FB0h HIGHLOW
    00059FBFh HIGHLOW
    00059FE6h HIGHLOW
    00059FF0h HIGHLOW
    00059FFFh HIGHLOW
    00059000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5A000   
SizeOfBlock:                   0x70      
    0005A023h HIGHLOW
    0005A084h HIGHLOW
    0005A0B0h HIGHLOW
    0005A0EEh HIGHLOW
    0005A10Ch HIGHLOW
    0005A126h HIGHLOW
    0005A180h HIGHLOW
    0005A1C9h HIGHLOW
    0005A221h HIGHLOW
    0005A25Bh HIGHLOW
    0005A299h HIGHLOW
    0005A2B7h HIGHLOW
    0005A2C6h HIGHLOW
    0005A36Ch HIGHLOW
    0005A3A6h HIGHLOW
    0005A3C2h HIGHLOW
    0005A3CFh HIGHLOW
    0005A447h HIGHLOW
    0005A490h HIGHLOW
    0005A52Ch HIGHLOW
    0005A579h HIGHLOW
    0005A68Eh HIGHLOW
    0005A6CFh HIGHLOW
    0005A7E9h HIGHLOW
    0005A834h HIGHLOW
    0005A88Ch HIGHLOW
    0005A8C8h HIGHLOW
    0005A92Bh HIGHLOW
    0005A978h HIGHLOW
    0005AA9Fh HIGHLOW
    0005AAE0h HIGHLOW
    0005ABC0h HIGHLOW
    0005AC0Ch HIGHLOW
    0005AC4Ah HIGHLOW
    0005AC66h HIGHLOW
    0005AC89h HIGHLOW
    0005ACC3h HIGHLOW
    0005ACD7h HIGHLOW
    0005ACF9h HIGHLOW
    0005AD18h HIGHLOW
    0005AD2Ah HIGHLOW
    0005AD3Fh HIGHLOW
    0005AE36h HIGHLOW
    0005AE67h HIGHLOW
    0005AE97h HIGHLOW
    0005AEA0h HIGHLOW
    0005AEE1h HIGHLOW
    0005AF0Bh HIGHLOW
    0005AF1Bh HIGHLOW
    0005AF52h HIGHLOW
    0005AFC2h HIGHLOW
    0005A000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5B000   
SizeOfBlock:                   0x7C      
    0005B074h HIGHLOW
    0005B0DCh HIGHLOW
    0005B1D0h HIGHLOW
    0005B1DCh HIGHLOW
    0005B303h HIGHLOW
    0005B333h HIGHLOW
    0005B3A0h HIGHLOW
    0005B3B7h HIGHLOW
    0005B3BEh HIGHLOW
    0005B3C7h HIGHLOW
    0005B3D6h HIGHLOW
    0005B3E2h HIGHLOW
    0005B3EBh HIGHLOW
    0005B404h HIGHLOW
    0005B410h HIGHLOW
    0005B42Bh HIGHLOW
    0005B447h HIGHLOW
    0005B451h HIGHLOW
    0005B457h HIGHLOW
    0005B465h HIGHLOW
    0005B4BAh HIGHLOW
    0005B4C0h HIGHLOW
    0005B4C5h HIGHLOW
    0005B4D2h HIGHLOW
    0005B4DBh HIGHLOW
    0005B4E6h HIGHLOW
    0005B53Ah HIGHLOW
    0005B545h HIGHLOW
    0005B54Bh HIGHLOW
    0005B554h HIGHLOW
    0005B55Fh HIGHLOW
    0005B565h HIGHLOW
    0005B586h HIGHLOW
    0005B6CDh HIGHLOW
    0005B6FDh HIGHLOW
    0005B750h HIGHLOW
    0005B7F4h HIGHLOW
    0005B9D3h HIGHLOW
    0005B9DDh HIGHLOW
    0005BA40h HIGHLOW
    0005BA4Ah HIGHLOW
    0005BA8Eh HIGHLOW
    0005BAB6h HIGHLOW
    0005BB10h HIGHLOW
    0005BB23h HIGHLOW
    0005BC82h HIGHLOW
    0005BC95h HIGHLOW
    0005BCE4h HIGHLOW
    0005BD48h HIGHLOW
    0005BD5Bh HIGHLOW
    0005BDD3h HIGHLOW
    0005BDE6h HIGHLOW
    0005BE55h HIGHLOW
    0005BE68h HIGHLOW
    0005BF02h HIGHLOW
    0005BF17h HIGHLOW
    0005BF8Dh HIGHLOW
    0005BFBBh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5C000   
SizeOfBlock:                   0xA4      
    0005C023h HIGHLOW
    0005C07Eh HIGHLOW
    0005C0E9h HIGHLOW
    0005C230h HIGHLOW
    0005C243h HIGHLOW
    0005C2DAh HIGHLOW
    0005C2EDh HIGHLOW
    0005C385h HIGHLOW
    0005C39Ah HIGHLOW
    0005C500h HIGHLOW
    0005C533h HIGHLOW
    0005C597h HIGHLOW
    0005C5DEh HIGHLOW
    0005C67Dh HIGHLOW
    0005C690h HIGHLOW
    0005C700h HIGHLOW
    0005C713h HIGHLOW
    0005C788h HIGHLOW
    0005C7D9h HIGHLOW
    0005C7ECh HIGHLOW
    0005C837h HIGHLOW
    0005C84Bh HIGHLOW
    0005C854h HIGHLOW
    0005C86Eh HIGHLOW
    0005C88Ch HIGHLOW
    0005C8ADh HIGHLOW
    0005C8B9h HIGHLOW
    0005C8D3h HIGHLOW
    0005C8E1h HIGHLOW
    0005C8EFh HIGHLOW
    0005C8FDh HIGHLOW
    0005C933h HIGHLOW
    0005C959h HIGHLOW
    0005C965h HIGHLOW
    0005C984h HIGHLOW
    0005C9DCh HIGHLOW
    0005C9F2h HIGHLOW
    0005CA0Fh HIGHLOW
    0005CA16h HIGHLOW
    0005CA2Bh HIGHLOW
    0005CA38h HIGHLOW
    0005CA79h HIGHLOW
    0005CAB1h HIGHLOW
    0005CAB9h HIGHLOW
    0005CAC7h HIGHLOW
    0005CAD4h HIGHLOW
    0005CAECh HIGHLOW
    0005CAF8h HIGHLOW
    0005CB29h HIGHLOW
    0005CB55h HIGHLOW
    0005CB7Bh HIGHLOW
    0005CBC3h HIGHLOW
    0005CC10h HIGHLOW
    0005CC35h HIGHLOW
    0005CC47h HIGHLOW
    0005CC5Ch HIGHLOW
    0005CC68h HIGHLOW
    0005CCA2h HIGHLOW
    0005CCE9h HIGHLOW
    0005CCF1h HIGHLOW
    0005CD39h HIGHLOW
    0005CD86h HIGHLOW
    0005CDABh HIGHLOW
    0005CDBDh HIGHLOW
    0005CDD2h HIGHLOW
    0005CDDEh HIGHLOW
    0005CE18h HIGHLOW
    0005CE5Fh HIGHLOW
    0005CE67h HIGHLOW
    0005CEAFh HIGHLOW
    0005CEFCh HIGHLOW
    0005CF21h HIGHLOW
    0005CF3Ah HIGHLOW
    0005CF4Fh HIGHLOW
    0005CF5Bh HIGHLOW
    0005CF95h HIGHLOW
    0005CFDCh HIGHLOW
    0005C000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5D000   
SizeOfBlock:                   0x88      
    0005D02Fh HIGHLOW
    0005D03Fh HIGHLOW
    0005D134h HIGHLOW
    0005D149h HIGHLOW
    0005D1C3h HIGHLOW
    0005D1D6h HIGHLOW
    0005D221h HIGHLOW
    0005D244h HIGHLOW
    0005D3C3h HIGHLOW
    0005D3DFh HIGHLOW
    0005D4D1h HIGHLOW
    0005D4E3h HIGHLOW
    0005D5BAh HIGHLOW
    0005D5C9h HIGHLOW
    0005D769h HIGHLOW
    0005D7CBh HIGHLOW
    0005D825h HIGHLOW
    0005D838h HIGHLOW
    0005D849h HIGHLOW
    0005D891h HIGHLOW
    0005D8B3h HIGHLOW
    0005D8CCh HIGHLOW
    0005D8E8h HIGHLOW
    0005D8F1h HIGHLOW
    0005D932h HIGHLOW
    0005D94Dh HIGHLOW
    0005D98Ch HIGHLOW
    0005D9BBh HIGHLOW
    0005D9F5h HIGHLOW
    0005DA29h HIGHLOW
    0005DA6Dh HIGHLOW
    0005DAB1h HIGHLOW
    0005DACAh HIGHLOW
    0005DAE5h HIGHLOW
    0005DB76h HIGHLOW
    0005DBB5h HIGHLOW
    0005DBD6h HIGHLOW
    0005DBF5h HIGHLOW
    0005DC06h HIGHLOW
    0005DC17h HIGHLOW
    0005DC25h HIGHLOW
    0005DC3Ch HIGHLOW
    0005DC64h HIGHLOW
    0005DCCCh HIGHLOW
    0005DCF2h HIGHLOW
    0005DD00h HIGHLOW
    0005DDA8h HIGHLOW
    0005DDD5h HIGHLOW
    0005DE4Ah HIGHLOW
    0005DE65h HIGHLOW
    0005DE91h HIGHLOW
    0005DEA9h HIGHLOW
    0005DEC4h HIGHLOW
    0005DEC9h HIGHLOW
    0005DEFFh HIGHLOW
    0005DF2Eh HIGHLOW
    0005DF62h HIGHLOW
    0005DF6Fh HIGHLOW
    0005DF83h HIGHLOW
    0005DF91h HIGHLOW
    0005DFBEh HIGHLOW
    0005DFD6h HIGHLOW
    0005DFEAh HIGHLOW
    0005D000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5E000   
SizeOfBlock:                   0xA0      
    0005E014h HIGHLOW
    0005E045h HIGHLOW
    0005E077h HIGHLOW
    0005E087h HIGHLOW
    0005E0BFh HIGHLOW
    0005E12Dh HIGHLOW
    0005E1A7h HIGHLOW
    0005E294h HIGHLOW
    0005E2C4h HIGHLOW
    0005E343h HIGHLOW
    0005E3CDh HIGHLOW
    0005E425h HIGHLOW
    0005E468h HIGHLOW
    0005E49Ch HIGHLOW
    0005E558h HIGHLOW
    0005E565h HIGHLOW
    0005E56Ch HIGHLOW
    0005E579h HIGHLOW
    0005E59Fh HIGHLOW
    0005E5B7h HIGHLOW
    0005E5D9h HIGHLOW
    0005E5E6h HIGHLOW
    0005E635h HIGHLOW
    0005E63Ch HIGHLOW
    0005E654h HIGHLOW
    0005E65Bh HIGHLOW
    0005E6E2h HIGHLOW
    0005E6EAh HIGHLOW
    0005E6F6h HIGHLOW
    0005E726h HIGHLOW
    0005E739h HIGHLOW
    0005E749h HIGHLOW
    0005E769h HIGHLOW
    0005E785h HIGHLOW
    0005E79Ch HIGHLOW
    0005E849h HIGHLOW
    0005E865h HIGHLOW
    0005E86Eh HIGHLOW
    0005E966h HIGHLOW
    0005E995h HIGHLOW
    0005E9B5h HIGHLOW
    0005E9BEh HIGHLOW
    0005E9E3h HIGHLOW
    0005EA51h HIGHLOW
    0005EA6Ah HIGHLOW
    0005EA8Bh HIGHLOW
    0005EAB3h HIGHLOW
    0005EAE1h HIGHLOW
    0005EAEAh HIGHLOW
    0005EB0Fh HIGHLOW
    0005EB1Dh HIGHLOW
    0005EB5Ah HIGHLOW
    0005EB99h HIGHLOW
    0005EBCAh HIGHLOW
    0005EBD3h HIGHLOW
    0005EC43h HIGHLOW
    0005EC64h HIGHLOW
    0005ECC1h HIGHLOW
    0005ECF9h HIGHLOW
    0005ED02h HIGHLOW
    0005ED26h HIGHLOW
    0005ED34h HIGHLOW
    0005ED51h HIGHLOW
    0005ED70h HIGHLOW
    0005ED79h HIGHLOW
    0005ED95h HIGHLOW
    0005EDFFh HIGHLOW
    0005EE1Dh HIGHLOW
    0005EE92h HIGHLOW
    0005EEA9h HIGHLOW
    0005EED2h HIGHLOW
    0005EEDBh HIGHLOW
    0005EEF7h HIGHLOW
    0005EF69h HIGHLOW
    0005EF8Bh HIGHLOW
    0005EFD0h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x5F000   
SizeOfBlock:                   0x88      
    0005F02Fh HIGHLOW
    0005F1C1h HIGHLOW
    0005F206h HIGHLOW
    0005F20Fh HIGHLOW
    0005F318h HIGHLOW
    0005F36Ah HIGHLOW
    0005F372h HIGHLOW
    0005F399h HIGHLOW
    0005F3A7h HIGHLOW
    0005F3C8h HIGHLOW
    0005F3E7h HIGHLOW
    0005F423h HIGHLOW
    0005F440h HIGHLOW
    0005F449h HIGHLOW
    0005F478h HIGHLOW
    0005F510h HIGHLOW
    0005F567h HIGHLOW
    0005F5AEh HIGHLOW
    0005F5B7h HIGHLOW
    0005F775h HIGHLOW
    0005F78Eh HIGHLOW
    0005F7B3h HIGHLOW
    0005F7CBh HIGHLOW
    0005F80Bh HIGHLOW
    0005F817h HIGHLOW
    0005F845h HIGHLOW
    0005F854h HIGHLOW
    0005F8B0h HIGHLOW
    0005F8B8h HIGHLOW
    0005F90Ah HIGHLOW
    0005F916h HIGHLOW
    0005F945h HIGHLOW
    0005F954h HIGHLOW
    0005F9B1h HIGHLOW
    0005F9B9h HIGHLOW
    0005F9F9h HIGHLOW
    0005FA05h HIGHLOW
    0005FA33h HIGHLOW
    0005FA42h HIGHLOW
    0005FA9Eh HIGHLOW
    0005FAA6h HIGHLOW
    0005FAF8h HIGHLOW
    0005FB04h HIGHLOW
    0005FB32h HIGHLOW
    0005FB41h HIGHLOW
    0005FB9Dh HIGHLOW
    0005FBDDh HIGHLOW
    0005FC03h HIGHLOW
    0005FC55h HIGHLOW
    0005FC61h HIGHLOW
    0005FCBAh HIGHLOW
    0005FD26h HIGHLOW
    0005FD2Eh HIGHLOW
    0005FD6Eh HIGHLOW
    0005FD7Ah HIGHLOW
    0005FDA6h HIGHLOW
    0005FDB5h HIGHLOW
    0005FE12h HIGHLOW
    0005FE53h HIGHLOW
    0005FE61h HIGHLOW
    0005FE92h HIGHLOW
    0005FEC9h HIGHLOW
    0005FED7h HIGHLOW
    0005FF46h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x60000   
SizeOfBlock:                   0x98      
    00060063h HIGHLOW
    000600A2h HIGHLOW
    00060144h HIGHLOW
    0006021Ah HIGHLOW
    0006022Ah HIGHLOW
    0006024Ah HIGHLOW
    00060264h HIGHLOW
    000602A4h HIGHLOW
    000602CEh HIGHLOW
    000602D4h HIGHLOW
    000602D9h HIGHLOW
    00060316h HIGHLOW
    00060337h HIGHLOW
    00060354h HIGHLOW
    00060365h HIGHLOW
    00060396h HIGHLOW
    0006039Bh HIGHLOW
    000603C9h HIGHLOW
    000603F5h HIGHLOW
    00060412h HIGHLOW
    00060439h HIGHLOW
    0006045Eh HIGHLOW
    0006047Bh HIGHLOW
    000604B6h HIGHLOW
    0006051Ch HIGHLOW
    00060531h HIGHLOW
    0006054Bh HIGHLOW
    0006057Fh HIGHLOW
    00060594h HIGHLOW
    000605BDh HIGHLOW
    000605D3h HIGHLOW
    000605E8h HIGHLOW
    0006060Ah HIGHLOW
    00060626h HIGHLOW
    00060642h HIGHLOW
    0006065Eh HIGHLOW
    0006067Ah HIGHLOW
    00060696h HIGHLOW
    000606B2h HIGHLOW
    000606CEh HIGHLOW
    000606EAh HIGHLOW
    00060703h HIGHLOW
    0006071Ch HIGHLOW
    00060749h HIGHLOW
    000608E8h HIGHLOW
    000608F8h HIGHLOW
    00060921h HIGHLOW
    0006093Bh HIGHLOW
    0006094Bh HIGHLOW
    00060971h HIGHLOW
    000609B7h HIGHLOW
    00060C02h HIGHLOW
    00060C3Dh HIGHLOW
    00060C64h HIGHLOW
    00060C84h HIGHLOW
    00060CBAh HIGHLOW
    00060CF4h HIGHLOW
    00060D01h HIGHLOW
    00060D58h HIGHLOW
    00060D65h HIGHLOW
    00060DA7h HIGHLOW
    00060DDFh HIGHLOW
    00060E37h HIGHLOW
    00060E6Bh HIGHLOW
    00060E77h HIGHLOW
    00060E9Bh HIGHLOW
    00060EC2h HIGHLOW
    00060EF5h HIGHLOW
    00060F10h HIGHLOW
    00060F2Bh HIGHLOW
    00060F89h HIGHLOW
    00060FFCh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x61000   
SizeOfBlock:                   0x84      
    00061006h HIGHLOW
    00061099h HIGHLOW
    00061100h HIGHLOW
    00061120h HIGHLOW
    00061139h HIGHLOW
    00061198h HIGHLOW
    000611CDh HIGHLOW
    000611E6h HIGHLOW
    000611F8h HIGHLOW
    0006121Ah HIGHLOW
    00061223h HIGHLOW
    0006122Eh HIGHLOW
    00061242h HIGHLOW
    000612C2h HIGHLOW
    000612D0h HIGHLOW
    000612E0h HIGHLOW
    000612F2h HIGHLOW
    0006131Eh HIGHLOW
    00061336h HIGHLOW
    00061358h HIGHLOW
    00061368h HIGHLOW
    0006136Dh HIGHLOW
    0006137Dh HIGHLOW
    00061384h HIGHLOW
    00061389h HIGHLOW
    00061390h HIGHLOW
    0006139Ch HIGHLOW
    000613A3h HIGHLOW
    000613A8h HIGHLOW
    000613B8h HIGHLOW
    000613BFh HIGHLOW
    000613DBh HIGHLOW
    00061408h HIGHLOW
    00061463h HIGHLOW
    0006156Fh HIGHLOW
    00061584h HIGHLOW
    000615B3h HIGHLOW
    000615D6h HIGHLOW
    000615FDh HIGHLOW
    00061615h HIGHLOW
    00061634h HIGHLOW
    0006164Dh HIGHLOW
    00061669h HIGHLOW
    0006172Eh HIGHLOW
    0006177Dh HIGHLOW
    000617B5h HIGHLOW
    00061805h HIGHLOW
    0006181Ah HIGHLOW
    000618BCh HIGHLOW
    00061963h HIGHLOW
    0006197Ch HIGHLOW
    000619D3h HIGHLOW
    00061B27h HIGHLOW
    00061BAEh HIGHLOW
    00061C0Eh HIGHLOW
    00061C23h HIGHLOW
    00061C67h HIGHLOW
    00061C7Ah HIGHLOW
    00061DA0h HIGHLOW
    00061DDCh HIGHLOW
    00061DEFh HIGHLOW
    00061F15h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x62000   
SizeOfBlock:                   0x34      
    000622D9h HIGHLOW
    000622E9h HIGHLOW
    000623C9h HIGHLOW
    00062469h HIGHLOW
    000624E6h HIGHLOW
    00062518h HIGHLOW
    0006252Bh HIGHLOW
    000626A1h HIGHLOW
    000626FCh HIGHLOW
    0006282Fh HIGHLOW
    0006283Fh HIGHLOW
    000628F4h HIGHLOW
    000629DCh HIGHLOW
    000629EFh HIGHLOW
    00062A8Fh HIGHLOW
    00062B6Bh HIGHLOW
    00062BD4h HIGHLOW
    00062C15h HIGHLOW
    00062DC8h HIGHLOW
    00062E09h HIGHLOW
    00062FD2h HIGHLOW
    00062FE2h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x63000   
SizeOfBlock:                   0x3C      
    000630ADh HIGHLOW
    0006321Ch HIGHLOW
    0006327Ah HIGHLOW
    00063364h HIGHLOW
    00063393h HIGHLOW
    0006342Fh HIGHLOW
    0006343Fh HIGHLOW
    0006351Fh HIGHLOW
    000635BFh HIGHLOW
    0006363Ch HIGHLOW
    0006366Eh HIGHLOW
    00063681h HIGHLOW
    000637F7h HIGHLOW
    00063852h HIGHLOW
    00063985h HIGHLOW
    00063995h HIGHLOW
    00063A4Ah HIGHLOW
    00063B32h HIGHLOW
    00063B45h HIGHLOW
    00063BE5h HIGHLOW
    00063CC1h HIGHLOW
    00063D2Ah HIGHLOW
    00063D6Bh HIGHLOW
    00063F1Eh HIGHLOW
    00063F5Fh HIGHLOW
    00063000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x64000   
SizeOfBlock:                   0x50      
    00064128h HIGHLOW
    00064138h HIGHLOW
    00064203h HIGHLOW
    00064372h HIGHLOW
    000643D0h HIGHLOW
    000644BAh HIGHLOW
    000644E9h HIGHLOW
    00064556h HIGHLOW
    00064585h HIGHLOW
    0006459Ah HIGHLOW
    00064619h HIGHLOW
    00064670h HIGHLOW
    00064717h HIGHLOW
    00064776h HIGHLOW
    000647EAh HIGHLOW
    000647FFh HIGHLOW
    00064A44h HIGHLOW
    00064A57h HIGHLOW
    00064AC7h HIGHLOW
    00064AEDh HIGHLOW
    00064AF4h HIGHLOW
    00064B82h HIGHLOW
    00064BF2h HIGHLOW
    00064BFFh HIGHLOW
    00064C2Eh HIGHLOW
    00064D90h HIGHLOW
    00064DA4h HIGHLOW
    00064DFBh HIGHLOW
    00064E4Bh HIGHLOW
    00064E6Bh HIGHLOW
    00064ED8h HIGHLOW
    00064F1Dh HIGHLOW
    00064F95h HIGHLOW
    00064FE9h HIGHLOW
    00064FF6h HIGHLOW
    00064000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x65000   
SizeOfBlock:                   0xC8      
    0006500Fh HIGHLOW
    00065030h HIGHLOW
    000650F9h HIGHLOW
    00065114h HIGHLOW
    00065151h HIGHLOW
    00065179h HIGHLOW
    00065193h HIGHLOW
    0006522Ch HIGHLOW
    00065249h HIGHLOW
    0006525Bh HIGHLOW
    00065262h HIGHLOW
    00065276h HIGHLOW
    000652D9h HIGHLOW
    000652EDh HIGHLOW
    00065316h HIGHLOW
    00065369h HIGHLOW
    00065397h HIGHLOW
    000653B9h HIGHLOW
    000653E6h HIGHLOW
    000653FEh HIGHLOW
    00065412h HIGHLOW
    0006541Eh HIGHLOW
    00065464h HIGHLOW
    00065499h HIGHLOW
    000654C3h HIGHLOW
    000654D8h HIGHLOW
    0006550Bh HIGHLOW
    00065526h HIGHLOW
    0006553Ah HIGHLOW
    00065546h HIGHLOW
    000655BDh HIGHLOW
    000655DFh HIGHLOW
    000655F1h HIGHLOW
    000655F8h HIGHLOW
    00065666h HIGHLOW
    00065683h HIGHLOW
    00065695h HIGHLOW
    0006569Ch HIGHLOW
    000656B0h HIGHLOW
    00065728h HIGHLOW
    0006574Ch HIGHLOW
    0006575Eh HIGHLOW
    00065765h HIGHLOW
    00065797h HIGHLOW
    000657E3h HIGHLOW
    0006580Eh HIGHLOW
    00065836h HIGHLOW
    00065869h HIGHLOW
    00065884h HIGHLOW
    00065898h HIGHLOW
    000658A4h HIGHLOW
    00065916h HIGHLOW
    0006592Ah HIGHLOW
    00065940h HIGHLOW
    0006598Fh HIGHLOW
    0006599Bh HIGHLOW
    000659B5h HIGHLOW
    000659BBh HIGHLOW
    000659C5h HIGHLOW
    000659F6h HIGHLOW
    000659FCh HIGHLOW
    00065A72h HIGHLOW
    00065A82h HIGHLOW
    00065AC6h HIGHLOW
    00065ACDh HIGHLOW
    00065ADBh HIGHLOW
    00065B97h HIGHLOW
    00065BBAh HIGHLOW
    00065BFFh HIGHLOW
    00065C0Ch HIGHLOW
    00065C40h HIGHLOW
    00065C7Bh HIGHLOW
    00065CA7h HIGHLOW
    00065D0Eh HIGHLOW
    00065D24h HIGHLOW
    00065D42h HIGHLOW
    00065D60h HIGHLOW
    00065DC3h HIGHLOW
    00065DF4h HIGHLOW
    00065E03h HIGHLOW
    00065E2Ch HIGHLOW
    00065E33h HIGHLOW
    00065E61h HIGHLOW
    00065E6Dh HIGHLOW
    00065E7Fh HIGHLOW
    00065E9Bh HIGHLOW
    00065EA1h HIGHLOW
    00065EB6h HIGHLOW
    00065EFDh HIGHLOW
    00065F0Dh HIGHLOW
    00065F46h HIGHLOW
    00065F6Dh HIGHLOW
    00065F82h HIGHLOW
    00065FA8h HIGHLOW
    00065FBBh HIGHLOW
    00065FCDh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x66000   
SizeOfBlock:                   0xA8      
    00066031h HIGHLOW
    0006603Ch HIGHLOW
    0006604Bh HIGHLOW
    00066051h HIGHLOW
    000660EDh HIGHLOW
    00066159h HIGHLOW
    0006615Eh HIGHLOW
    000661B3h HIGHLOW
    000661D6h HIGHLOW
    000661DCh HIGHLOW
    000661E7h HIGHLOW
    000661F6h HIGHLOW
    000661FCh HIGHLOW
    00066248h HIGHLOW
    0006624Dh HIGHLOW
    00066278h HIGHLOW
    0006629Dh HIGHLOW
    000662A3h HIGHLOW
    000662A9h HIGHLOW
    000662B4h HIGHLOW
    000662EEh HIGHLOW
    0006632Dh HIGHLOW
    0006637Fh HIGHLOW
    00066393h HIGHLOW
    000663ACh HIGHLOW
    00066400h HIGHLOW
    00066420h HIGHLOW
    00066439h HIGHLOW
    00066444h HIGHLOW
    00066459h HIGHLOW
    000664ACh HIGHLOW
    000664E6h HIGHLOW
    000664FAh HIGHLOW
    00066582h HIGHLOW
    00066591h HIGHLOW
    000665EEh HIGHLOW
    0006660Eh HIGHLOW
    00066628h HIGHLOW
    00066633h HIGHLOW
    00066642h HIGHLOW
    00066687h HIGHLOW
    00066696h HIGHLOW
    0006671Eh HIGHLOW
    0006672Dh HIGHLOW
    0006677Dh HIGHLOW
    000667C9h HIGHLOW
    00066815h HIGHLOW
    00066824h HIGHLOW
    00066842h HIGHLOW
    0006685Ch HIGHLOW
    0006689Fh HIGHLOW
    000668B3h HIGHLOW
    000668C2h HIGHLOW
    000668CFh HIGHLOW
    000668DAh HIGHLOW
    000668E5h HIGHLOW
    0006692Bh HIGHLOW
    00066934h HIGHLOW
    0006693Eh HIGHLOW
    0006695Bh HIGHLOW
    0006696Ah HIGHLOW
    00066977h HIGHLOW
    000669A0h HIGHLOW
    000669E9h HIGHLOW
    00066A05h HIGHLOW
    00066A4Bh HIGHLOW
    00066A56h HIGHLOW
    00066A7Dh HIGHLOW
    00066C26h HIGHLOW
    00066CFCh HIGHLOW
    00066D2Ah HIGHLOW
    00066D59h HIGHLOW
    00066E03h HIGHLOW
    00066E23h HIGHLOW
    00066E45h HIGHLOW
    00066EA4h HIGHLOW
    00066F99h HIGHLOW
    00066FC0h HIGHLOW
    00066FE9h HIGHLOW
    00066000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x67000   
SizeOfBlock:                   0x9C      
    0006708Bh HIGHLOW
    0006709Fh HIGHLOW
    000670BFh HIGHLOW
    000670E1h HIGHLOW
    00067106h HIGHLOW
    00067126h HIGHLOW
    00067188h HIGHLOW
    000671D7h HIGHLOW
    000671FDh HIGHLOW
    00067222h HIGHLOW
    0006725Dh HIGHLOW
    00067272h HIGHLOW
    0006729Bh HIGHLOW
    00067317h HIGHLOW
    00067366h HIGHLOW
    0006737Fh HIGHLOW
    000673BBh HIGHLOW
    000673C6h HIGHLOW
    000673EDh HIGHLOW
    0006749Eh HIGHLOW
    0006753Ch HIGHLOW
    0006755Dh HIGHLOW
    00067597h HIGHLOW
    000675A2h HIGHLOW
    000675B7h HIGHLOW
    000675FDh HIGHLOW
    00067652h HIGHLOW
    0006766Bh HIGHLOW
    0006769Ch HIGHLOW
    00067710h HIGHLOW
    00067736h HIGHLOW
    0006775Eh HIGHLOW
    000677A4h HIGHLOW
    000677B9h HIGHLOW
    000677E2h HIGHLOW
    000678ABh HIGHLOW
    000678E5h HIGHLOW
    0006792Eh HIGHLOW
    00067948h HIGHLOW
    00067979h HIGHLOW
    000679BAh HIGHLOW
    000679D4h HIGHLOW
    00067A05h HIGHLOW
    00067A44h HIGHLOW
    00067A5Eh HIGHLOW
    00067A9Eh HIGHLOW
    00067AC5h HIGHLOW
    00067ADAh HIGHLOW
    00067B0Eh HIGHLOW
    00067B29h HIGHLOW
    00067B36h HIGHLOW
    00067B7Dh HIGHLOW
    00067B91h HIGHLOW
    00067BB5h HIGHLOW
    00067BF8h HIGHLOW
    00067C3Dh HIGHLOW
    00067C96h HIGHLOW
    00067CAAh HIGHLOW
    00067CEFh HIGHLOW
    00067D03h HIGHLOW
    00067D48h HIGHLOW
    00067D5Ch HIGHLOW
    00067DA7h HIGHLOW
    00067DBBh HIGHLOW
    00067DD4h HIGHLOW
    00067E29h HIGHLOW
    00067E42h HIGHLOW
    00067E70h HIGHLOW
    00067ECBh HIGHLOW
    00067EE4h HIGHLOW
    00067F12h HIGHLOW
    00067F99h HIGHLOW
    00067FB2h HIGHLOW
    00067000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x68000   
SizeOfBlock:                   0xD4      
    0006804Ch HIGHLOW
    00068060h HIGHLOW
    000680A5h HIGHLOW
    000680B9h HIGHLOW
    000680FCh HIGHLOW
    00068110h HIGHLOW
    0006815Ah HIGHLOW
    00068173h HIGHLOW
    00068183h HIGHLOW
    0006818Eh HIGHLOW
    000681A3h HIGHLOW
    000681ACh HIGHLOW
    000681FEh HIGHLOW
    00068226h HIGHLOW
    00068268h HIGHLOW
    00068298h HIGHLOW
    000682F4h HIGHLOW
    00068308h HIGHLOW
    0006831Fh HIGHLOW
    00068362h HIGHLOW
    00068386h HIGHLOW
    0006839Bh HIGHLOW
    000683C8h HIGHLOW
    000683E3h HIGHLOW
    000683F7h HIGHLOW
    00068403h HIGHLOW
    00068447h HIGHLOW
    0006845Bh HIGHLOW
    00068472h HIGHLOW
    000684ACh HIGHLOW
    000684EBh HIGHLOW
    00068531h HIGHLOW
    0006854Fh HIGHLOW
    000685B0h HIGHLOW
    000685C9h HIGHLOW
    000685DBh HIGHLOW
    000685E2h HIGHLOW
    000685F6h HIGHLOW
    00068649h HIGHLOW
    0006865Dh HIGHLOW
    00068676h HIGHLOW
    000686B0h HIGHLOW
    000686FAh HIGHLOW
    00068740h HIGHLOW
    0006874Fh HIGHLOW
    00068799h HIGHLOW
    000687A8h HIGHLOW
    000687C6h HIGHLOW
    00068804h HIGHLOW
    00068822h HIGHLOW
    00068837h HIGHLOW
    0006883Eh HIGHLOW
    00068853h HIGHLOW
    00068918h HIGHLOW
    00068927h HIGHLOW
    0006895Ah HIGHLOW
    0006898Eh HIGHLOW
    000689A8h HIGHLOW
    000689DDh HIGHLOW
    00068A68h HIGHLOW
    00068A84h HIGHLOW
    00068ABAh HIGHLOW
    00068AC5h HIGHLOW
    00068AE4h HIGHLOW
    00068AF9h HIGHLOW
    00068B02h HIGHLOW
    00068BD0h HIGHLOW
    00068BE0h HIGHLOW
    00068C1Eh HIGHLOW
    00068C29h HIGHLOW
    00068C4Ah HIGHLOW
    00068C5Fh HIGHLOW
    00068C87h HIGHLOW
    00068C90h HIGHLOW
    00068CC7h HIGHLOW
    00068CD6h HIGHLOW
    00068D20h HIGHLOW
    00068D39h HIGHLOW
    00068D49h HIGHLOW
    00068D54h HIGHLOW
    00068D5Fh HIGHLOW
    00068D75h HIGHLOW
    00068D84h HIGHLOW
    00068D99h HIGHLOW
    00068DDCh HIGHLOW
    00068E1Bh HIGHLOW
    00068E3Dh HIGHLOW
    00068EAAh HIGHLOW
    00068EE4h HIGHLOW
    00068EF4h HIGHLOW
    00068F06h HIGHLOW
    00068F0Ch HIGHLOW
    00068F32h HIGHLOW
    00068F41h HIGHLOW
    00068F66h HIGHLOW
    00068F6Ch HIGHLOW
    00068F72h HIGHLOW
    00068F78h HIGHLOW
    00068F9Dh HIGHLOW
    00068FC0h HIGHLOW
    00068FFDh HIGHLOW
    00068000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x69000   
SizeOfBlock:                   0x5C      
    00069003h HIGHLOW
    00069034h HIGHLOW
    0006903Fh HIGHLOW
    0006904Fh HIGHLOW
    000690DFh HIGHLOW
    000690F7h HIGHLOW
    00069113h HIGHLOW
    00069132h HIGHLOW
    0006914Ch HIGHLOW
    000691C4h HIGHLOW
    000691F5h HIGHLOW
    00069242h HIGHLOW
    0006924Eh HIGHLOW
    00069457h HIGHLOW
    000694DFh HIGHLOW
    0006955Dh HIGHLOW
    00069643h HIGHLOW
    000696C0h HIGHLOW
    000696F2h HIGHLOW
    0006988Fh HIGHLOW
    00069923h HIGHLOW
    00069955h HIGHLOW
    00069A65h HIGHLOW
    00069AC1h HIGHLOW
    00069AFEh HIGHLOW
    00069B10h HIGHLOW
    00069B3Ah HIGHLOW
    00069B61h HIGHLOW
    00069BC3h HIGHLOW
    00069CC0h HIGHLOW
    00069D86h HIGHLOW
    00069EE4h HIGHLOW
    00069F0Fh HIGHLOW
    00069F17h HIGHLOW
    00069F1Eh HIGHLOW
    00069F24h HIGHLOW
    00069F31h HIGHLOW
    00069F36h HIGHLOW
    00069F3Bh HIGHLOW
    00069F55h HIGHLOW
    00069F64h HIGHLOW
    00069FA1h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6A000   
SizeOfBlock:                   0xB4      
    0006A073h HIGHLOW
    0006A0ACh HIGHLOW
    0006A0BAh HIGHLOW
    0006A0E0h HIGHLOW
    0006A0FFh HIGHLOW
    0006A137h HIGHLOW
    0006A153h HIGHLOW
    0006A178h HIGHLOW
    0006A1D2h HIGHLOW
    0006A1E7h HIGHLOW
    0006A218h HIGHLOW
    0006A246h HIGHLOW
    0006A274h HIGHLOW
    0006A2A2h HIGHLOW
    0006A2CCh HIGHLOW
    0006A2F3h HIGHLOW
    0006A321h HIGHLOW
    0006A34Fh HIGHLOW
    0006A376h HIGHLOW
    0006A3A0h HIGHLOW
    0006A3C3h HIGHLOW
    0006A3EDh HIGHLOW
    0006A411h HIGHLOW
    0006A434h HIGHLOW
    0006A44Eh HIGHLOW
    0006A4A5h HIGHLOW
    0006A4BEh HIGHLOW
    0006A4D7h HIGHLOW
    0006A4ECh HIGHLOW
    0006A501h HIGHLOW
    0006A516h HIGHLOW
    0006A53Ah HIGHLOW
    0006A56Ah HIGHLOW
    0006A587h HIGHLOW
    0006A592h HIGHLOW
    0006A59Eh HIGHLOW
    0006A5E0h HIGHLOW
    0006A646h HIGHLOW
    0006A656h HIGHLOW
    0006A6CFh HIGHLOW
    0006A6D9h HIGHLOW
    0006A6E0h HIGHLOW
    0006A6E6h HIGHLOW
    0006A6F2h HIGHLOW
    0006A6F7h HIGHLOW
    0006A6FCh HIGHLOW
    0006A716h HIGHLOW
    0006A722h HIGHLOW
    0006A728h HIGHLOW
    0006A750h HIGHLOW
    0006A7D9h HIGHLOW
    0006A7E9h HIGHLOW
    0006A81Bh HIGHLOW
    0006A82Bh HIGHLOW
    0006A89Fh HIGHLOW
    0006A8D6h HIGHLOW
    0006A941h HIGHLOW
    0006A97Ah HIGHLOW
    0006A9FDh HIGHLOW
    0006AA0Dh HIGHLOW
    0006AA3Ch HIGHLOW
    0006AAB3h HIGHLOW
    0006AABDh HIGHLOW
    0006AAC4h HIGHLOW
    0006AACAh HIGHLOW
    0006AAD6h HIGHLOW
    0006AADBh HIGHLOW
    0006AAE0h HIGHLOW
    0006AAFAh HIGHLOW
    0006AB06h HIGHLOW
    0006AB0Ch HIGHLOW
    0006AB95h HIGHLOW
    0006ABD0h HIGHLOW
    0006ABE7h HIGHLOW
    0006ABF6h HIGHLOW
    0006AC12h HIGHLOW
    0006AC1Eh HIGHLOW
    0006AC32h HIGHLOW
    0006AC3Eh HIGHLOW
    0006AC6Ch HIGHLOW
    0006AC8Ch HIGHLOW
    0006ACD1h HIGHLOW
    0006ACD8h HIGHLOW
    0006AEF4h HIGHLOW
    0006AF0Eh HIGHLOW
    0006A000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6B000   
SizeOfBlock:                   0x50      
    0006B176h HIGHLOW
    0006B2E4h HIGHLOW
    0006B2FFh HIGHLOW
    0006B36Eh HIGHLOW
    0006B398h HIGHLOW
    0006B3A4h HIGHLOW
    0006B3DFh HIGHLOW
    0006B418h HIGHLOW
    0006B433h HIGHLOW
    0006B496h HIGHLOW
    0006B54Eh HIGHLOW
    0006B55Ah HIGHLOW
    0006B697h HIGHLOW
    0006B6B1h HIGHLOW
    0006B6D9h HIGHLOW
    0006B715h HIGHLOW
    0006B71Ch HIGHLOW
    0006B736h HIGHLOW
    0006B792h HIGHLOW
    0006B7BDh HIGHLOW
    0006B7E0h HIGHLOW
    0006B83Ah HIGHLOW
    0006B841h HIGHLOW
    0006B85Dh HIGHLOW
    0006B8B3h HIGHLOW
    0006B8FDh HIGHLOW
    0006B98Bh HIGHLOW
    0006B9BFh HIGHLOW
    0006BA04h HIGHLOW
    0006BAB8h HIGHLOW
    0006BACEh HIGHLOW
    0006BAF6h HIGHLOW
    0006BB2Ah HIGHLOW
    0006BB6Fh HIGHLOW
    0006BBC6h HIGHLOW
    0006B000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6C000   
SizeOfBlock:                   0x5C      
    0006C083h HIGHLOW
    0006C089h HIGHLOW
    0006C232h HIGHLOW
    0006C90Ch HIGHLOW
    0006C91Dh HIGHLOW
    0006C924h HIGHLOW
    0006C92Ah HIGHLOW
    0006C935h HIGHLOW
    0006C941h HIGHLOW
    0006C946h HIGHLOW
    0006C94Bh HIGHLOW
    0006C965h HIGHLOW
    0006C976h HIGHLOW
    0006C98Eh HIGHLOW
    0006C994h HIGHLOW
    0006C9B3h HIGHLOW
    0006C9C3h HIGHLOW
    0006C9E9h HIGHLOW
    0006C9EFh HIGHLOW
    0006C9FBh HIGHLOW
    0006CA07h HIGHLOW
    0006CA0Ch HIGHLOW
    0006CA13h HIGHLOW
    0006CA18h HIGHLOW
    0006CA67h HIGHLOW
    0006CA76h HIGHLOW
    0006CAC2h HIGHLOW
    0006CAC9h HIGHLOW
    0006CAE2h HIGHLOW
    0006CB05h HIGHLOW
    0006CBA5h HIGHLOW
    0006CBE1h HIGHLOW
    0006CBE7h HIGHLOW
    0006CBF4h HIGHLOW
    0006CBFAh HIGHLOW
    0006CC0Ch HIGHLOW
    0006CDAAh HIGHLOW
    0006CDB1h HIGHLOW
    0006CE8Ah HIGHLOW
    0006CE9Ah HIGHLOW
    0006CFB0h HIGHLOW
    0006CFB5h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6D000   
SizeOfBlock:                   0x4C      
    0006D013h HIGHLOW
    0006D4ADh HIGHLOW
    0006D4CEh HIGHLOW
    0006D4DBh HIGHLOW
    0006D51Dh HIGHLOW
    0006D5A6h HIGHLOW
    0006D5ABh HIGHLOW
    0006D5CDh HIGHLOW
    0006D5D2h HIGHLOW
    0006D5F6h HIGHLOW
    0006D5FBh HIGHLOW
    0006D61Fh HIGHLOW
    0006D624h HIGHLOW
    0006D648h HIGHLOW
    0006D64Dh HIGHLOW
    0006D671h HIGHLOW
    0006D676h HIGHLOW
    0006D6C5h HIGHLOW
    0006D6CAh HIGHLOW
    0006D71Ah HIGHLOW
    0006D71Fh HIGHLOW
    0006D7A4h HIGHLOW
    0006D812h HIGHLOW
    0006D9B0h HIGHLOW
    0006D9BFh HIGHLOW
    0006D9D0h HIGHLOW
    0006DA30h HIGHLOW
    0006DA6Dh HIGHLOW
    0006DA7Dh HIGHLOW
    0006DABBh HIGHLOW
    0006DCA0h HIGHLOW
    0006DEF7h HIGHLOW
    0006DEFDh HIGHLOW
    0006DFDBh HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6E000   
SizeOfBlock:                   0x9C      
    0006E053h HIGHLOW
    0006E05Eh HIGHLOW
    0006E083h HIGHLOW
    0006E1FEh HIGHLOW
    0006E21Eh HIGHLOW
    0006E2B5h HIGHLOW
    0006E2F5h HIGHLOW
    0006E32Ah HIGHLOW
    0006E33Ah HIGHLOW
    0006E35Bh HIGHLOW
    0006E372h HIGHLOW
    0006E382h HIGHLOW
    0006E3D7h HIGHLOW
    0006E3E2h HIGHLOW
    0006E3F5h HIGHLOW
    0006E401h HIGHLOW
    0006E406h HIGHLOW
    0006E43Eh HIGHLOW
    0006E451h HIGHLOW
    0006E463h HIGHLOW
    0006E476h HIGHLOW
    0006E487h HIGHLOW
    0006E4B4h HIGHLOW
    0006E4BCh HIGHLOW
    0006E4C3h HIGHLOW
    0006E4C9h HIGHLOW
    0006E4D5h HIGHLOW
    0006E4DAh HIGHLOW
    0006E4DFh HIGHLOW
    0006E4F9h HIGHLOW
    0006E504h HIGHLOW
    0006E543h HIGHLOW
    0006E56Ch HIGHLOW
    0006E57Fh HIGHLOW
    0006E5C0h HIGHLOW
    0006E5CFh HIGHLOW
    0006E5E8h HIGHLOW
    0006E604h HIGHLOW
    0006E629h HIGHLOW
    0006E781h HIGHLOW
    0006E7ADh HIGHLOW
    0006E7B7h HIGHLOW
    0006E7BCh HIGHLOW
    0006E7D0h HIGHLOW
    0006E7F3h HIGHLOW
    0006E7F8h HIGHLOW
    0006E835h HIGHLOW
    0006E877h HIGHLOW
    0006E889h HIGHLOW
    0006E8E7h HIGHLOW
    0006E8F2h HIGHLOW
    0006E92Eh HIGHLOW
    0006E940h HIGHLOW
    0006E94Ah HIGHLOW
    0006E97Fh HIGHLOW
    0006E99Ah HIGHLOW
    0006E9C4h HIGHLOW
    0006E9D0h HIGHLOW
    0006EA0Bh HIGHLOW
    0006EA10h HIGHLOW
    0006EA4Dh HIGHLOW
    0006EA5Bh HIGHLOW
    0006EA73h HIGHLOW
    0006EB08h HIGHLOW
    0006EBA7h HIGHLOW
    0006ECBCh HIGHLOW
    0006ED18h HIGHLOW
    0006ED34h HIGHLOW
    0006ED3Bh HIGHLOW
    0006ED49h HIGHLOW
    0006ED73h HIGHLOW
    0006EE84h HIGHLOW
    0006EF68h HIGHLOW
    0006EF94h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x6F000   
SizeOfBlock:                   0x38      
    0006F02Fh HIGHLOW
    0006F074h HIGHLOW
    0006FDACh HIGHLOW
    0006FDB2h HIGHLOW
    0006FDB8h HIGHLOW
    0006FDBEh HIGHLOW
    0006FDC4h HIGHLOW
    0006FDCAh HIGHLOW
    0006FDD0h HIGHLOW
    0006FDD6h HIGHLOW
    0006FDDCh HIGHLOW
    0006FDE2h HIGHLOW
    0006FDE8h HIGHLOW
    0006FDEEh HIGHLOW
    0006FDF4h HIGHLOW
    0006FDFAh HIGHLOW
    0006FE00h HIGHLOW
    0006FE06h HIGHLOW
    0006FE0Ch HIGHLOW
    0006FE12h HIGHLOW
    0006FE18h HIGHLOW
    0006FE1Eh HIGHLOW
    0006FE24h HIGHLOW
    0006F000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x70000   
SizeOfBlock:                   0x5C      
    00070195h HIGHLOW
    0007019Dh HIGHLOW
    000703FFh HIGHLOW
    00070740h HIGHLOW
    00070771h HIGHLOW
    0007079Ch HIGHLOW
    000707CDh HIGHLOW
    000707F3h HIGHLOW
    00070B28h HIGHLOW
    00070B38h HIGHLOW
    00070B48h HIGHLOW
    00070C50h HIGHLOW
    00070C60h HIGHLOW
    00070C88h HIGHLOW
    00070C98h HIGHLOW
    00070CA8h HIGHLOW
    00070CD8h HIGHLOW
    00070D04h HIGHLOW
    00070D08h HIGHLOW
    00070D2Ch HIGHLOW
    00070D30h HIGHLOW
    00070D3Ch HIGHLOW
    00070D40h HIGHLOW
    00070D4Ch HIGHLOW
    00070D50h HIGHLOW
    00070D5Ch HIGHLOW
    00070D60h HIGHLOW
    00070D98h HIGHLOW
    00070DA0h HIGHLOW
    00070DA4h HIGHLOW
    00070DB0h HIGHLOW
    00070DC0h HIGHLOW
    00070DCCh HIGHLOW
    00070E3Ch HIGHLOW
    00070E40h HIGHLOW
    00070EDCh HIGHLOW
    00070EE0h HIGHLOW
    00070EF0h HIGHLOW
    00070F00h HIGHLOW
    00070F7Ch HIGHLOW
    00070F80h HIGHLOW
    00070000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x71000   
SizeOfBlock:                   0xE4      
    000710CCh HIGHLOW
    000710D0h HIGHLOW
    000710DCh HIGHLOW
    000710E0h HIGHLOW
    000711A8h HIGHLOW
    000711B4h HIGHLOW
    000711F0h HIGHLOW
    00071200h HIGHLOW
    00071228h HIGHLOW
    00071238h HIGHLOW
    00071260h HIGHLOW
    00071270h HIGHLOW
    000712A4h HIGHLOW
    000712A8h HIGHLOW
    000712B4h HIGHLOW
    000712B8h HIGHLOW
    000712C4h HIGHLOW
    000712C8h HIGHLOW
    000712D8h HIGHLOW
    00071358h HIGHLOW
    00071440h HIGHLOW
    00071450h HIGHLOW
    00071460h HIGHLOW
    00071470h HIGHLOW
    00071480h HIGHLOW
    00071490h HIGHLOW
    00071558h HIGHLOW
    000715DCh HIGHLOW
    000715E0h HIGHLOW
    000716D4h HIGHLOW
    000716D8h HIGHLOW
    000716E4h HIGHLOW
    000716E8h HIGHLOW
    000716F4h HIGHLOW
    000716F8h HIGHLOW
    00071704h HIGHLOW
    00071708h HIGHLOW
    00071714h HIGHLOW
    00071718h HIGHLOW
    00071728h HIGHLOW
    00071738h HIGHLOW
    00071768h HIGHLOW
    00071798h HIGHLOW
    000717A8h HIGHLOW
    000717B4h HIGHLOW
    000717B8h HIGHLOW
    000717C4h HIGHLOW
    000717C8h HIGHLOW
    000717D4h HIGHLOW
    000717D8h HIGHLOW
    000717E4h HIGHLOW
    000717E8h HIGHLOW
    00071814h HIGHLOW
    00071818h HIGHLOW
    00071820h HIGHLOW
    00071824h HIGHLOW
    0007182Ch HIGHLOW
    00071830h HIGHLOW
    0007183Ch HIGHLOW
    00071840h HIGHLOW
    0007184Ch HIGHLOW
    00071850h HIGHLOW
    0007185Ch HIGHLOW
    00071860h HIGHLOW
    00071868h HIGHLOW
    0007186Ch HIGHLOW
    00071874h HIGHLOW
    00071878h HIGHLOW
    00071880h HIGHLOW
    00071884h HIGHLOW
    0007188Ch HIGHLOW
    00071890h HIGHLOW
    0007189Ch HIGHLOW
    000718A0h HIGHLOW
    000718A8h HIGHLOW
    000718ACh HIGHLOW
    000718B4h HIGHLOW
    000718B8h HIGHLOW
    000718C4h HIGHLOW
    000718C8h HIGHLOW
    000718D4h HIGHLOW
    000718D8h HIGHLOW
    000718E4h HIGHLOW
    000718E8h HIGHLOW
    000718F4h HIGHLOW
    000718F8h HIGHLOW
    00071904h HIGHLOW
    00071908h HIGHLOW
    00071914h HIGHLOW
    00071918h HIGHLOW
    00071924h HIGHLOW
    00071928h HIGHLOW
    00071934h HIGHLOW
    00071938h HIGHLOW
    00071944h HIGHLOW
    00071948h HIGHLOW
    00071954h HIGHLOW
    00071958h HIGHLOW
    00071964h HIGHLOW
    00071968h HIGHLOW
    00071A6Ch HIGHLOW
    00071A70h HIGHLOW
    00071A7Ch HIGHLOW
    00071A80h HIGHLOW
    00071A8Ch HIGHLOW
    00071A90h HIGHLOW
    00071A9Ch HIGHLOW
    00071AA8h HIGHLOW
    00071AB4h HIGHLOW
    00071AB8h HIGHLOW

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x72000   
SizeOfBlock:                   0x88      
    00072CC1h HIGHLOW
    00072CC5h HIGHLOW
    00072CC9h HIGHLOW
    00072CCDh HIGHLOW
    00072CD1h HIGHLOW
    00072CD5h HIGHLOW
    00072CD9h HIGHLOW
    00072CDDh HIGHLOW
    00072CE1h HIGHLOW
    00072CE5h HIGHLOW
    00072CE9h HIGHLOW
    00072CEDh HIGHLOW
    00072CF1h HIGHLOW
    00072CF5h HIGHLOW
    00072CF9h HIGHLOW
    00072CFDh HIGHLOW
    00072D01h HIGHLOW
    00072D05h HIGHLOW
    00072D09h HIGHLOW
    00072D0Dh HIGHLOW
    00072D11h HIGHLOW
    00072D15h HIGHLOW
    00072D19h HIGHLOW
    00072D1Dh HIGHLOW
    00072D21h HIGHLOW
    00072D25h HIGHLOW
    00072D29h HIGHLOW
    00072D2Dh HIGHLOW
    00072D31h HIGHLOW
    00072D35h HIGHLOW
    00072D39h HIGHLOW
    00072D3Dh HIGHLOW
    00072D41h HIGHLOW
    00072D45h HIGHLOW
    00072D49h HIGHLOW
    00072D4Dh HIGHLOW
    00072D51h HIGHLOW
    00072D55h HIGHLOW
    00072D60h HIGHLOW
    00072D64h HIGHLOW
    00072D68h HIGHLOW
    00072D6Ch HIGHLOW
    00072D70h HIGHLOW
    00072D74h HIGHLOW
    00072D78h HIGHLOW
    00072D7Ch HIGHLOW
    00072D80h HIGHLOW
    00072D84h HIGHLOW
    00072D88h HIGHLOW
    00072D8Ch HIGHLOW
    00072D90h HIGHLOW
    00072D94h HIGHLOW
    00072D98h HIGHLOW
    00072D9Ch HIGHLOW
    00072DA0h HIGHLOW
    00072DA4h HIGHLOW
    00072DA8h HIGHLOW
    00072DACh HIGHLOW
    00072DB0h HIGHLOW
    00072DB4h HIGHLOW
    00072DB8h HIGHLOW
    00072DBCh HIGHLOW
    00072DC0h HIGHLOW
    00072000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x76000   
SizeOfBlock:                   0x48      
    0007600Ch HIGHLOW
    00076010h HIGHLOW
    00076014h HIGHLOW
    00076018h HIGHLOW
    0007601Ch HIGHLOW
    00076050h HIGHLOW
    000760B0h HIGHLOW
    00076104h HIGHLOW
    00076110h HIGHLOW
    00076118h HIGHLOW
    0007611Ch HIGHLOW
    00076344h HIGHLOW
    0007637Ch HIGHLOW
    00076388h HIGHLOW
    000763A8h HIGHLOW
    000763B0h HIGHLOW
    0007661Ch HIGHLOW
    0007662Ch HIGHLOW
    00076634h HIGHLOW
    00076650h HIGHLOW
    0007665Ch HIGHLOW
    00076668h HIGHLOW
    00076674h HIGHLOW
    00076680h HIGHLOW
    0007668Ch HIGHLOW
    000766C8h HIGHLOW
    000768D0h HIGHLOW
    000768F0h HIGHLOW
    000769C8h HIGHLOW
    000769DCh HIGHLOW
    000769E0h HIGHLOW
    00076000h ABSOLUTE

[IMAGE_BASE_RELOCATION]
VirtualAddress:                0x78000   
SizeOfBlock:                   0xAC      
    00078220h HIGHLOW
    0007823Ch HIGHLOW
    00078240h HIGHLOW
    00078248h HIGHLOW
    0007824Ch HIGHLOW
    00078298h HIGHLOW
    000782A4h HIGHLOW
    000782B8h HIGHLOW
    000782BCh HIGHLOW
    000782C0h HIGHLOW
    000782C4h HIGHLOW
    000782C8h HIGHLOW
    000782CCh HIGHLOW
    000782D0h HIGHLOW
    000782D4h HIGHLOW
    000782D8h HIGHLOW
    000782DCh HIGHLOW
    000782E0h HIGHLOW
    000782E4h HIGHLOW
    000782E8h HIGHLOW
    000782ECh HIGHLOW
    000782F0h HIGHLOW
    000782F4h HIGHLOW
    000782F8h HIGHLOW
    000782FCh HIGHLOW
    00078300h HIGHLOW
    00078304h HIGHLOW
    00078308h HIGHLOW
    0007830Ch HIGHLOW
    00078310h HIGHLOW
    00078314h HIGHLOW
    00078318h HIGHLOW
    0007831Ch HIGHLOW
    00078320h HIGHLOW
    00078324h HIGHLOW
    00078328h HIGHLOW
    0007832Ch HIGHLOW
    00078330h HIGHLOW
    00078334h HIGHLOW
    00078338h HIGHLOW
    0007833Ch HIGHLOW
    00078340h HIGHLOW
    00078344h HIGHLOW
    00078348h HIGHLOW
    0007834Ch HIGHLOW
    00078350h HIGHLOW
    00078354h HIGHLOW
    00078358h HIGHLOW
    0007835Ch HIGHLOW
    00078360h HIGHLOW
    00078364h HIGHLOW
    00078368h HIGHLOW
    0007836Ch HIGHLOW
    00078370h HIGHLOW
    00078374h HIGHLOW
    00078378h HIGHLOW
    0007837Ch HIGHLOW
    00078380h HIGHLOW
    00078384h HIGHLOW
    00078388h HIGHLOW
    0007838Ch HIGHLOW
    00078390h HIGHLOW
    00078394h HIGHLOW
    00078398h HIGHLOW
    0007839Ch HIGHLOW
    000783A0h HIGHLOW
    000783A4h HIGHLOW
    000783A8h HIGHLOW
    000783ACh HIGHLOW
    000783B0h HIGHLOW
    000783B4h HIGHLOW
    000783B8h HIGHLOW
    000783BCh HIGHLOW
    000783C0h HIGHLOW
    000783C4h HIGHLOW
    000783C8h HIGHLOW
    000783CCh HIGHLOW
    000783D0h HIGHLOW
    000783D4h HIGHLOW
    000783D8h HIGHLOW
    000783DCh HIGHLOW
    000783E0h HIGHLOW
```