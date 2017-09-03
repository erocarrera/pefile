# pefile
|Master|Develop|
|------|-------|
|[![Build Status](https://travis-ci.org/erocarrera/pefile.svg?branch=master)](https://travis-ci.org/erocarrera/pefile)|[![Build Status](https://travis-ci.org/erocarrera/pefile.svg?branch=develop)](https://travis-ci.org/erocarrera/pefile)|
|[![Coverage Status](https://coveralls.io/repos/github/erocarrera/pefile/badge.svg?branch=master)](https://coveralls.io/github/erocarrera/pefile?branch=master)|[![Coverage Status](https://coveralls.io/repos/erocarrera/pefile/badge.svg?branch=develop)](https://coveralls.io/r/erocarrera/pefile?branch=develop)|


_pefile_ is a multi-platform Python module to parse and work with [Portable Executable (aka PE) files](http://en.wikipedia.org/wiki/Portable_Executable). Most of the information contained in the PE headers is accessible as well as all sections' details and their data.

The structures defined in the Windows header files will be accessible as attributes in the PE instance. The naming of fields/attributes will try to adhere to the naming scheme in those headers. Only shortcuts added for convenience will depart from that convention.

pefile requires some basic understanding of the layout of a PE file. Armed with it it's possible to explore nearly every single feature of the file format.

## Features

Some of the tasks that _pefile_ makes possible are:

  * Inspecting headers
  * Analysis of sections' data
  * Retrieving embedded data
  * [Reading strings from the resources](https://github.com/erocarrera/pefile/blob/wiki/ReadingResourceStrings.md)
  * Warnings for suspicious and malformed values
  * Support to [write to some of the fields](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#reading-and-writing-standard-header-members) and to [other parts](https://github.com/erocarrera/pefile/blob/wiki/ModifyingPEImageData.md) of the PE, so it's possible to do some basic butchering of PEs. The functionality won't rearrange structures to make room for new ones, so use it with care. Overwriting fields should mostly be safe.
  * Packer detection with [PEiD’s signatures](https://github.com/erocarrera/pefile/blob/wiki/PEiDSignatures.md)
  * [PEiD signature](https://github.com/erocarrera/pefile/blob/wiki/PEiDSignatures.md) generation

Please, refer to [Usage Examples](https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction) for some code snippets showing how to use _pefile_.

A few examples of what a dump produced with _pefile_ look like can be found [here for a packed file](https://github.com/erocarrera/pefile/blob/wiki/FullDump0x90.md), [here for one of _kernel32.dll_](https://github.com/erocarrera/pefile/blob/wiki/FullDumpKernel32.md) and [here for one of TinyPE](https://github.com/erocarrera/pefile/blob/wiki/FullDumpTinyPE.md).

In order to work with authenticated binaries, including **Authenticode signatures**, please check the project [verify-sigs](http://code.google.com/p/verify-sigs/)

pefile runs in several pipelines scanning hundreds of thousands of new PE files every day and, while not perfect, it has grown to be pretty robust over time. That being said small glitches are found every now and then. If you bump into a PE that does not appear to be processed correctly, do report it please! it will help make pefile a tiny bit more tough.

## Dependencies

pefile is self-contained. It has no dependecies and it is endianness independent, it works on OS X, Windows, and Linux.

## Recent changes

Prompted by the move to GitHub, the need to support Python 3 in addition to resoling a slew of pending issues (some having to do with the old versioning scheme), _pefile_ has changed its version number scheme and from now on it will be using the release date as its version.

## Projects and products using _pefile_

  * [MAEC](http://maec.mitre.org) MAEC is a standardized language for encoding and communicating high-fidelity information about malware based upon attributes such as behaviors, artifacts, and attack patterns. MAEC [converts](https://github.com/MAECProject/pefile-to-maec) _pefile_'s output into their XML format.
  * [Qiew](https://github.com/mtivadar/qiew) Qiew - Hex/File format viewer.
  * [VirusTotal](http://www.virustotal.com/)
  * [bbfreeze](http://pypi.python.org/pypi/bbfreeze)
  * **pyemu**: [download](https://www.openrce.org/repositories/browse/codypierce), [whitepaper](https://www.blackhat.com/presentations/bh-usa-07/Pierce/Whitepaper/bh-usa-07-pierce-WP.pdf)
  * [Offensive Computing](http://www.offensivecomputing.net/)
  * [Immunity Debugger 1.1](https://www.openrce.org/blog/view/882/Immunity_Debugger_v1.1_Release)
  * [PyInstaller](http://www.pyinstaller.org/)
  * [Cuckoo](http://docs.cuckoosandbox.org/en/latest/)
  * [MultiScanner](https://github.com/MITRECND/multiscanner)

## Additional resources

PDFs of posters depicting the PE file format:

  * [Portable Executable Format](https://docs.google.com/open?id=0B3_wGJkuWLytbnIxY1J5WUs4MEk) shows the full view of the headers and structures defined by the Portable Executable format
  * [Portable Executable Format. A File Walkthrough](https://docs.google.com/open?id=0B3_wGJkuWLytQmc2di0wajB1Xzg) Shows a walkthrough over the raw view of an executable file with the PE format fields laid out over the corresponding areas

The following links provide detailed information about the PE format and its structures.

  * [corkami's wiki page about the PE format](https://code.google.com/p/corkami/wiki/PE) has grown to be one of the most in-depth repositories of information about the PE format
  * [corkami's treasure trove of PE weirdness](https://github.com/corkami/pocs/tree/master/PE)
  * [An In-Depth Look into the Win32 Portable Executable File Format](http://msdn.microsoft.com/msdnmag/issues/02/02/PE/default.aspx)
  * [An In-Depth Look into the Win32 Portable Executable File Format, Part 2](http://msdn.microsoft.com/msdnmag/issues/02/03/PE2/default.aspx)
  * [The Portable Executable File Format](http://www.csn.ul.ie/~caolan/publink/winresdump/winresdump/doc/pefile.html)
  * [Get icons from Exe or DLL the PE way](http://www.codeproject.com/cpp/GetIconsfromExeorDLLs.asp)
  * Solar Eclipse's Tiny PE page at "http://www.phreedom.org/solar/code/tinype/" is no longer available, corkami has a copy of TinyPE [here](https://code.google.com/p/corkami/source/browse/trunk/misc/MakePE/examples/PE/tinype.asm?r=179)
