_pefile_ is a multi-platform [Python](http://python.org) module to read and work with [Portable Executable (aka PE) files](http://en.wikipedia.org/wiki/Portable_Executable). Most of the information in the PE Header is accessible, as well as all the sections, section's information and data.

pefile requires some basic understanding of the layout of a PE file. Armed with it it's possible to explore nearly every single feature of the file.

Some of the tasks that _pefile_ makes possible are:

  * Modifying and writing back to the PE image
  * Header Inspection
  * Sections analysis
  * Retrieving data
  * Warnings for suspicious and malformed values
  * Packer detection with PEiD’s signatures
  * PEiD signature generation

Please, refer to UsageExamples for starting points on how to use _pefile_

In order to work with authenticated binaries, including **Authenticode signatures**, please check the project [verify-sigs](http://code.google.com/p/verify-sigs/)

## Latest changes ##

#### Version: **1.2.10-139** ####
Changes since previous release:
  * Added Mandiant's `ordLookup` to resolve the names for some symbols that are exported only by ordinal numbers.
  * Added a feature requested in [Issue 45](https://code.google.com/p/pefile/issues/detail?id=45) to produce a Python dictionary with all the information dumped by `dump_info()`.

In addition to the new features, the new version provides with the following bugfixes and improvements:
  * Improved the handling of PEs with vast number of invalid import symbols.
  * Improved the handling of invalid symbols in the export directory.
  * Added an upper bound in the maximum number of entries to consider when parsing the delay import directory.
  * Better handling of the Rich Header.
  * Fixed a problem when writing back the contents of the `VS_VERSIONINFO` `StringTable`. `StringTable` key, value string pairs are no longer added to the `StringTable` struct, they polluted the namespace and potentially overwrote real fields in the structure.
  * Improved parsing of PEs with thousands of sections. Sections that appear to be invalid will now be ignored and some of the checks have been optimized for the cases where a file still has many possibly valid sections.
  * Fixed a problem introduced when renaming the DLL Characteristics FLAGS that lead to them not being shown.
  * Merged patches contributed by Ange Albertini adding more subsystem types and warning of Windows 8's problems loading PE files with the entrypoint pointing within the headers.
  * Merged path from `ThreatGrid`'s Wesley Brown. Summary: changed memory mapping usage, revamped to use bytearrays rather than list, complete rewrite of the checksum generation algorithm to be much more memory efficient, and less susceptible to PE bomb attacks.

#### Version: **1.2.10-123** ####
Changes since previous release:
  * Added some safety checks.
  * Small optimization of the checksum algorithm. Thanks to Emmanuel Bourg.

#### Version: **1.2.10-121** ####
Changes since previous release:
  * Fixed a problem parsing section headers.
  * Improved the detection of corrupt resource names.

#### Version: **1.2.10-118** ####
Changes since previous release:
  * Improved the checks being done when parsing the exports and the bound imports directories. The potential data ranges to consider have been constrained further and only strings with certain characteristics will be allowed as module names in the bound forwarders.
  * Attempting to fix [Issue 35](https://code.google.com/p/pefile/issues/detail?id=35) where a big memory allocation is attempted (which can be avoided). When working with large files it could lead to `MemoryError` exceptions.
  * Added a check to verify that a section's calculated ending address does not overlap a subsequent section. If so cut it down to fit.

#### Version: **1.2.10-114** ####
Changes since previous release:
  * Added sanity checks for invalid relocation information. `VirtualAddress` and `SizeOfBlock` are checked against a wide boundary that should never surpass (`SizeOfImage`)
  * Merged the patch from [Issue 32](https://code.google.com/p/pefile/issues/detail?id=32) (and fixed some problems with it) regarding mmap files left open on Python 2.5.x

#### Version: **1.2.10-111** ####
Changes since previous release:
  * Fixed [Issue 10](https://code.google.com/p/pefile/issues/detail?id=10) and [Issue 29](https://code.google.com/p/pefile/issues/detail?id=29) (related) by also parsing strings for `stringfileinfo_struct.Type=0` in addition of `Type=1`
  * Fixed [Issue 26](https://code.google.com/p/pefile/issues/detail?id=26) as suggested by catching early parsing errors with a try in the PE constructor
  * Fixed [Issue 30](https://code.google.com/p/pefile/issues/detail?id=30) parsing 64-bit PE32+ imports
  * As pointed out by Pedram Amini removed a warning about `WRITE` and `EXECUTE` flags set for a section if the section name is 'PAGE' and the PE is a driver. In drivers such combination is legitimate
  * 10 and [Issue 29](https://code.google.com/p/pefile/issues/detail?id=29) to also handle the `VarFileInfo` structure


#### Version: **1.2.10-107** ####
Changes since previous release:
  * Fixed [Issue 27](https://code.google.com/p/pefile/issues/detail?id=27)
  * Enhanced the processing of files with uncommon combinations of `FileAligment` and `PointerToRawData` values
  * As suggested in [Issue 26](https://code.google.com/p/pefile/issues/detail?id=26) a `close()` method was added that closes the mmap of the file
  * Added a check for zero-length files. A `PEFormatError` is now raised on those ([Issue 25](https://code.google.com/p/pefile/issues/detail?id=25))
  * Fixed a couple of small bugs in the parsing of resources
  * The parsing of the resources' version strings had a small flaw where one character outside the range was not caught

#### Version: **1.2.10-102** ####
  * Added a (high) hard-coded limit to the number of directory entries to process. Some specially crafted directories could lead to long processing times


#### Version: **1.2.10-100** ####
  * Added additional check in the resources string parser to avoid some crashes
  * Added Ange Albertini's patch to provide more helpful error messages when pefile meets NE/LE/LX files and ZM (as opposed to MZ) files. The `PEFormatError()` exception raised will inform about the type of file

#### Version: **1.2.10-96** ####
  * Fixed [Issue 12](https://code.google.com/p/pefile/issues/detail?id=12), there was a bug calculating the offset to the `VS_VERSIONINFO` structure that would manifest in some files
  * Added a method to peutils to scan for PEiD signatures in user-provided raw data as opposed to only allowing pefile.PE() instances, it comes handy when feeding data from other tools like IDA
  * Improved handling of cases of unorthodox, although valid, `FileAlignment` and `SectionAlignment` values and combinations of those. It turns out that they have to be in certain relation for some value ranges
  * Fixed [Issue 24](https://code.google.com/p/pefile/issues/detail?id=24)

#### Version: **1.2.10-93** ####
  * Added Ange Albertini's concept code to parse the strings contained in the resources directory. They will now be displayed when calling the `dump_info()` method. If an entry in the resources directory contains strings they will be accessible through `entry.directory.strings` . Also it's possible to retrieve at once all strings found by calling the PE instance's method `get_resources_strings()` which will return a list with all strings found or an list string if none are found or the file has no resources directory
  * Added Ange Albertini's patch to fix some crashes parsing the resources

#### Version: **1.2.10-91** ####
  * Fixed a bug parsing small invalid PE files where the proper exception (PEFormatError) would not be raised and instead pefile would crash
  * Fixed [Issue 22](https://code.google.com/p/pefile/issues/detail?id=22). Some PE files reconstructed from memory dumps contained invalid export entries that led to a crash. Invalid entries are not properly ignored
  * Added a new method `get_overlay_data_start_offset()`. It will return the offset where data starts that it is not described by the PE headers. Commonly referred to as overlay data. If there's no overlay data the method will simply return EOF offset
  * Added a new method `get_overlay()` which will return the data appended to the file and not contained within the area described in the headers
  * Added a new method `trim()` which will return the just data defined by the PE headers, removing any overlay data
#### Version: **1.2.10-89** ####
  * Small fix to be able to retrieve strings outside section boundaries i.e., when a packer keeps strings overlapping headers or in overlays
  * Implemented fixes for sections at unaligned raw offsets. As pointed out by Ange Albertini if those offsets are smaller than the `FileAlignment` they are rounded to 0 by the Windows loader. _pefile_ now emulates such behavior
#### Version: **1.2.10-85** ####
  * mmap is now used to not load into memory the whole file unless working with it requires it. This should enable _pefile_ to parse much larger images in systems with limited memory
  * Thanks to the patch provided by the user mzibricky, _pefile_ should now run in Python 2.2
  * Improved handling of flags. Now section flags can be set by directly assigning to the convenience attributes, i.e. (`pe.sections[0].IMAGE_SCN_MEM_EXECUTE = True`) and the changes will be propagated to the section _Characteristics_ field
#### Version: **1.2.10-63** ####
  * Fixed an "_index out of range_" problem when parsing some unusual import tables
  * Fixed struct module's types to work properly on 64bit architectures. As it was reported by James on the _pefile_ googlegroup, the 'L' type tried to decode 8 bytes into a 64bit long instead of the expected 4 bytes for a dword. 'I' behaves as expected decoding 4 bytes when _pefile_ runs in both 32bit and 64bit architectures
#### Version: **1.2.10-60** ####
  * Besides some small bugfixes in this release I've added functionality to parse the LOAD\_CONFIG data directory. Now one can access this structure's fields like, for instance, `pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.SecurityCookie` or `pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.SEHandlerTable`
#### Version: **1.2.10-56** ####
  * Fixed bug in `contains_offset()`. The end of the section's data on disk was being calculated as `VirtualAddress + SizeOfRawData` instead of the correct: `PointerToRawData + SizeOfRawData`
  * Improved the redering when dumping the file's contents in textual form. The performance of the operation has **greatly** improved
  * `get_data()` calls now use a fixed size argument when possible. Improves the speed of those calls in large files. Fix suggested by Paul, barnabas79 [link](http://groups.google.com/group/pefile/browse_thread/thread/4b289227042d3f14?hl=en)
  * `get_memory_mapped_image()` can now properly return rebased images. The rebased image data is temporary and will be discarded (won't be saved in the instance). To achieve this one should call `relocate_image()` which will make the changes permanent
  * Improved parsing of import table for `PEI-format DLLs` generated with `MingW`
  * Added methods to handle the updating of the section's data upon modification of values in the image's data. (Section's and image's data are kept separately)
  * `generate_checksum()` now makes sure it processes the image with all modifications made to it
  * The `write()` method now only returns the file data if no filename is provided, which is a more intuitive behavior
  * `parse_data_directories()` now supports an optional argument to specify with directories to parse. For instance:
```
# 'fast_load' makes pefile to not load any directory
#
pe = pefile.PE(filepath, fast_load=True)

# the following line will tell pefile to only process the
# resource directory, where the version information is located
#
pe.parse_data_directories( directories=[ DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_RESOURCE'] ] )
```
#### Version: **1.2.9.1** ####
  * Fixed parsing problem on files specifying a `FileAligment` of zero
  * Fixed problem parsing the `Bound Imports directory` when it contained invalid data. In some instances _pefile_ would get caught up trying to make sense of arbitrary data. Now when empty strings are found as module names in the `Bound Import structures` the parsing is aborted
#### Version: **1.2.9** ####
  * Now it's possible to modify the version information by directly assigning new values to the keys, for instance `pe.FileInfo[0].StringTable[0].entries['OriginalFilename'] = 'NewName.exe'`
  * Other common keys are: `LegalCopyright`, `InternalName`, `FileVersion`, `CompanyName`, `ProductName`, `ProductVersion`, `FileDescription`, `OriginalFilename`
  * Added `__str__()` and `__repr__()` methods to _pefile_'s structures. Now it's possible to navigate through the contents much more comfortably from an interactive Python command line. Just typing the name of a structure or doing a print on it will return all the fields and their contents
  * Bugs fixed when parsing the resource information
  * Improved parsing of imported symbols. Import by ordinal and name is much more clear now. The ImportData instances have a new attribute, 'import\_by\_ordinal', indicating whether a symbol is imported by name, in that case the 'ordinal' attributes will contain the ordinal. Otherwise the attribute 'name' will contain the name of the imported symbol.
    * Added `CheckSum` verification and generation methods. `verify_checksum()` will return True/False indicating whether the value in the file's `OptionalHeader CheckSum` field contains the real `CheckSum` of the file. `generate_checksum()` will calculate the checksum over the file's data. If one modifies fields and writes the changes to disk it's possible to update the checksum by reloading the modified field and setting the `CheckSum` field to `generate_checksum()`'s result.
  * Other minor fixes
  * Added missing information when parsing import directory entries. Now the RVA of the Hint/Name entries is reported as an attribute named _hint\_name\_table\_rva_; as well the hint, if present, will be exposed as the attribute _hint_
  * Fixed a minor bug retrieving the relative virtual address of the Hint/Name entries. Only the lower 16 bits where being fetched as opposed to the 31 that had to be read. It seldom was the case that the entries where farther then 64KiB, but it could have happened. Thanks to Halvar for spotting this one
  * Added computation of MD5, SHA-1, SHA-256 and SHA-512 on a per-section basis. The results are always reported when invoking the dump\_info() method in the PE instance. SHA-256 and SHA-512 are calculated only in Python 2.5 onwards which includes them in the hashlib module. The SectionStructure instances now sport the following methods: `get_hash_sha1()`, `get_hash_sha256()`, `get_hash_sha512()`, `get_hash_md5()`
#### Version: **1.2.8** ####
  * As suggested by Jim Clausing. Added computation of _MD5_, _SHA-1_, _SHA-256_ and _SHA-512_ on a per-section basis. The results are always reported when invoking the `dump_info()` method in the `PE` instance. _SHA-256_ and _SHA-512_ are calculated only in Python 2.5 onwards which includes them in the _hashlib_ module. The SectionStructure instances now sport the following methods: `get_hash_sha1()`, `get_hash_sha256()`, `get_hash_sha512()`, `get_hash_md5()`
  * Faster entropy calculation by Gergely Erdelyi
  * Added some intelligence handling unicode strings in the resources information. Strings in the resources seem to always be Pascal style, added support for those
  * Changed some loops iterating using `range()` to use `xrange()` instead. It will make the code more robust/faster whenever invalid large numbers of elements are specified in different arrays
  * As per c1de0x suggestion, added `set_data()` method to `SectionStructure`
  * Added `get_entropy()` method to `SectionStructure`. Now it's only calculated on demand or when doing a `dump_info()`
  * c1de0x pointed out a redundant length check in `__unpack_data__` and `__unpack__`. Now the exception raised by the latter is caught by the former and a warning added if a structure can't be parsed because of missing data
  * Fixed bug parsing export directory. Warning messages are added if it's found to be invalid
  * Fixed bug parsing the IAT. Some broken samples could crash _pefile_. The invalid IAT is now reported in the warnings
  * New method: `relocate_image(new_ImageBase)` will apply the relocation information, if any, to the image
  * `get_memory_mapped_image()` now supports and additional keyword argument, `ImageBase`. By specifying an address it will return a data relocated (if the PE contains relocation information) as if it had been relocated to the new `ImageBase`
  * Added full family of bytes/word/dword/qword manipulation methods (needed by the relocation functionality):
  * `get_data_from_dword(dword)`, `get_dword_from_data(data, offset)`, `get_dword_at_rva(rva)`, `get_dword_from_offset(offset)`, `set_dword_at_rva(rva, dword)`, `set_dword_at_offset(offset, dword)`
  * `get_data_from_word(word)`, `get_word_from_data(data, offset)`, `get_word_at_rva(rva)`, `get_word_from_offset(offset)`, `set_word_at_rva(rva, word)`, `set_word_at_offset(offset, word)`
  * `get_data_from_qword(qword)`, `get_qword_from_data(data, offset)`, `get_qword_at_rva(rva)`, `get_qword_from_offset(offset)`, `set_qword_at_rva(rva, qword)`, `set_qword_at_offset(offset, qword)`
  * `set_bytes_at_rva(rva, data)`, `set_bytes_at_offset(offset, data)`

## Projects and products using _pefile_ ##

  * [Exe Dump Utility](http://utilitymill.com/utility/Exe_Dump_Utility) a web-based _pefile_
  * [VirusTotal](http://www.virustotal.com/)
  * [bbfreeze](http://pypi.python.org/pypi/bbfreeze)
  * **pyemu**: [download](https://www.openrce.org/repositories/browse/codypierce), [whitepaper](https://www.blackhat.com/presentations/bh-usa-07/Pierce/Whitepaper/bh-usa-07-pierce-WP.pdf)
  * [Offensive Computing](http://www.offensivecomputing.net/)
  * [Immunity Debugger 1.1](https://www.openrce.org/blog/view/882/Immunity_Debugger_v1.1_Release)
  * [Core Impact](http://en.wikipedia.org/wiki/Core_Impact)

## Additional resources ##

_Posters_ depicting the PE file format:

  * [Portable Executable Format](http://www.cafepress.com/dkbza.162471691) shows the full view of the headers and structures defined by the Portable Executable format
  * [Portable Executable Format. A File Walkthrough](http://www.cafepress.com/dkbza.164084665) Shows a walkthrough over the raw view of an executable file with the PE format fields laid out over the corresponding areas

A [PDF file](https://www.openrce.org/reference_library/files/reference/PE%20Format.pdf)  that I put together depicting the PE file format. (Hosted in [OpenRCE](https://www.openrce.org/))
(The poster just mentioned is based on this).

The following links provide extended information on the PE format and its structures.

  * [An In-Depth Look into the Win32 Portable Executable File Format](http://msdn.microsoft.com/msdnmag/issues/02/02/PE/default.aspx)
  * [An In-Depth Look into the Win32 Portable Executable File Format, Part 2](http://msdn.microsoft.com/msdnmag/issues/02/03/PE2/default.aspx)
  * [Peering Inside the PE: A Tour of the Win32 Portable Executable File Format](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dndebug/html/msdn_peeringpe.asp)
  * [The Portable Executable File Format](http://www.csn.ul.ie/~caolan/publink/winresdump/winresdump/doc/pefile.html)
  * [Portable Executable File Format](http://www.windowsitlibrary.com/Content/356/11/4.html)
  * [Get icons from Exe or DLL the PE way](http://www.codeproject.com/cpp/GetIconsfromExeorDLLs.asp)
  * [Tutorial 6: Import Table](http://win32assembly.online.fr/pe-tut6.html)
  * [Solar Eclipse's Tiny PE page](http://www.phreedom.org/solar/code/tinype/)
  * [The PE file format](http://webster.cs.ucr.edu/Page_TechDocs/pe.txt)