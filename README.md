# pefile

|Master|Develop|
|------|-------|
|[![Build Status](https://travis-ci.org/erocarrera/pefile.svg?branch=master)](https://travis-ci.org/erocarrera/pefile)|[![Build Status](https://travis-ci.org/erocarrera/pefile.svg?branch=develop)](https://travis-ci.org/erocarrera/pefile)|
|[![Coverage Status](https://coveralls.io/repos/github/erocarrera/pefile/badge.svg?branch=master)](https://coveralls.io/github/erocarrera/pefile?branch=master)|[![Coverage Status](https://coveralls.io/repos/erocarrera/pefile/badge.svg?branch=develop)](https://coveralls.io/r/erocarrera/pefile?branch=develop)|


_pefile_ is a multi-platform Python module to parse and work with [Portable Executable (PE) files](http://en.wikipedia.org/wiki/Portable_Executable). Most of the information contained in the PE file headers is accessible, as well as all the sections' details and data.

The structures defined in the Windows header files will be accessible as attributes in the PE instance. The naming of fields/attributes will try to adhere to the naming scheme in those headers. Only shortcuts added for convenience will depart from that convention.

_pefile_ requires some basic understanding of the layout of a PE file — with it, it's possible to explore nearly every single feature of the PE file format.

## Features

Some of the tasks that pefile makes possible are:

* Inspecting headers
* Analyzing of sections' data
* Retrieving embedded data
* [Reading strings from the resources](https://github.com/erocarrera/pefile/blob/wiki/ReadingResourceStrings.md)
* Warnings for suspicious and malformed values
* Basic butchering of PEs, like [writing to some fields](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#reading-and-writing-standard-header-members) and [other parts](https://github.com/erocarrera/pefile/blob/wiki/ModifyingPEImageData.md) of the PE
  * This functionality won't rearrange PE file structures to make room for new fields, so use it with care.
  * Overwriting fields should mostly be safe.
* Packer detection with [PEiD’s signatures](https://github.com/erocarrera/pefile/blob/wiki/PEiDSignatures.md)
* [PEiD signature](https://github.com/erocarrera/pefile/blob/wiki/PEiDSignatures.md)  generation

Please, refer to [Usage Examples](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction) for some code snippets that demonstrate how to use _pefile_.

Here are a few examples of what a dump produced with _pefile_ looks like for different types of files:

* [a packed file](https://github.com/erocarrera/pefile/blob/wiki/FullDump0x90.md)
* [kernel32.dll](https://github.com/erocarrera/pefile/blob/wiki/FullDumpKernel32.md)
* [TinyPE](https://github.com/erocarrera/pefile/blob/wiki/FullDumpTinyPE.md)

To work with authenticated binaries, including **Authenticode signatures**, please check the project [verify-sigs](http://code.google.com/p/verify-sigs).

_pefile_ runs in several pipelines scanning hundreds of thousands of new PE files every day, and, while not perfect, it has grown to be pretty robust over time. That being said, small glitches are found now and then. If you bump into a PE that does not appear to be processed correctly, do report it, please! It will help make pefile a tiny bit more powerful.

## Dependencies

_pefile_ is self-contained. The module has no dependencies; it is endianness independent; and it works on OS X, Windows, and Linux.

## Recent changes

Prompted by the move to GitHub, the need to support Python 3 in addition to resolving a slew of pending issues (some having to do with the old versioning scheme), _pefile_ has changed its version number scheme and from now on it will be using the release date as its version.

## Projects and products using _pefile_

  * Didier Stevens' [pecheck](https://blog.didierstevens.com/2018/06/12/update-pecheck-py-version-0-7-3/), a tool for displaying PE file info, handles PEiD files better then _pefile_ does.
  * [MAEC](http://maec.mitre.org), a standardized language for encoding and communicating high-fidelity information about malware based upon attributes such as behaviors, artifacts, and attack patterns. MAEC [converts](https://github.com/MAECProject/pefile-to-maec) _pefile_'s output into their XML format.
  * [Qiew](https://github.com/mtivadar/qiew), a Hex/File format viewer.
  * [VirusTotal](http://www.virustotal.com/)
  * [bbfreeze](http://pypi.python.org/pypi/bbfreeze)
  * **pyemu**: [download](http://www.openrce.org/repositories/browse/codypierce), [whitepaper](https://www.blackhat.com/presentations/bh-usa-07/Pierce/Whitepaper/bh-usa-07-pierce-WP.pdf)
  * [Immunity Debugger 1.1](http://www.openrce.org/blog/view/882/Immunity_Debugger_v1.1_Release)
  * [PyInstaller](http://www.pyinstaller.org)
  * [Cuckoo](http://docs.cuckoosandbox.org/en/latest)
  * [MultiScanner](https://github.com/MITRECND/multiscanner)

## Additional resources

PDFs of posters depicting the PE file format:

  * [Portable Executable Format Layout](https://docs.google.com/open?id=0B3_wGJkuWLytbnIxY1J5WUs4MEk) shows the full view of the headers and structures defined by the PE format.
  * [Portable Executable Header Walkthrough](https://docs.google.com/open?id=0B3_wGJkuWLytQmc2di0wajB1Xzg) shows the raw view of an executable file with the PE format fields laid out over the corresponding areas.

The following links provide detailed information about the PE format and its structures.

  * [corkami's wiki page about the PE format](https://code.google.com/p/corkami/wiki/PE) has grown to be one of the most in-depth repositories of information about the PE format.
  * [corkami's treasure trove of PE weirdness](https://github.com/corkami/pocs/tree/master/PE)
  * corkami's copy of Solar Eclipse's [Tiny PE](https://code.google.com/p/corkami/source/browse/trunk/misc/MakePE/examples/PE/tinype.asm?r=179)
  * [An In-Depth Look into the Win32 Portable Executable File Format](https://docs.microsoft.com/en-us/archive/msdn-magazine/2002/february/inside-windows-win32-portable-executable-file-format-in-detail)
  * [An In-Depth Look into the Win32 Portable Executable File Format, Part 2](https://docs.microsoft.com/en-us/archive/msdn-magazine/2002/march/inside-windows-an-in-depth-look-into-the-win32-portable-executable-file-format-part-2%20)
  * [The Portable Executable File Format](http://www.csn.ul.ie/~caolan/publink/winresdump/winresdump/doc/pefile.html)
  * [Get icons from Exe or DLL the PE way](https://www.codeproject.com/Articles/9303/Get-icons-from-Exe-or-DLL-the-PE-way)