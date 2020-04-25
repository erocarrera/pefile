###########################################################
Usage Examples
###########################################################

Simple code snippets to get you started.

Loading a PE file
===========================================================

Import the module and parse a file.

.. code-block::
    
    import pefile
    pe =  pefile.PE(‘/path/to/pefile.exe’)

Optionally, setting the ``fast_load`` argument to ``True`` will prevent parsing the directories. In large PE files this can make loading significantly faster and it might be a good idea to use it none of the information from the data directories is needed.

.. code-block::
    
    import pefile
    pe =  pefile.PE(‘/path/to/pefile.exe’, fast_load=True)

A later call to the :py:func:`full_load()` method would parse the missing information.

It's also possible to just parse raw PE data:

.. code-block::
    
    pe = pefile.PE(data=str_object_with_pe_file_data)


Reading and writing standard header members
===========================================================

Once the PE file is successfully parsed, the data is readily available as attributes of the PE instance.

.. code-block::
    
    pe.OPTIONAL_HEADER.AddressOfEntryPoint
    pe.OPTIONAL_HEADER.ImageBase
    pe.FILE_HEADER.NumberOfSections

All of these values support assignment.

.. code-block::
    
    pe.OPTIONAL_HEADER.AddressOfEntryPoint = 0xdeadbeef

A subsequent call to ``pe.write`` will write the modified file to disk.

.. code-block::
    
    pe.write(filename='file_to_write.exe')

All the structures and members defined in the PE format should be available with the same names. Some convenient shortcuts exist, for instance the ``sections`` list. Usually, all the structures containing a member ``Characteristics`` (or similar fields of flags) will contain attributes set to ``True`` or ``False`` according to the value of the corresponding flag.

Notes about the write support
-----------------------------------------------------------

- Starting from pefile 1.2 it's possible to write back any changes done to the PE file. One has to be careful with this functionality as it will not be very intelligent reconstructing the PE file. That is, it will not handle displacing structures if that would be needed because a new section/structure has been added.
- The rule of thumb is, if there's room for an additional header/structure to fit then there'll be no problem and pefile will write it.
- All other modifications, i.e. changing individual values in header/structure members should work well.
- One possible useful application of this could be to correct malformed headers used by some malware in order to cause certain analysis tools to malfunction.


Iterating through the sections
===========================================================

Sections are added to a list accesible as the attribute ``sections`` in the PE instance.
The common structure members of the section header are reachable as attributes.

.. code-block::
    
    for section in pe.sections:
      print (section.Name, hex(section.VirtualAddress),
        hex(section.Misc_VirtualSize), section.SizeOfRawData )

Output
-----------------------------------------------------------

.. code-block::
    
    ('.text', '0x1000L', '0x6D72L', 28160L)
    ('.data', '0x8000L', '0x1BA8L', 1536L)
    ('.rsrc', '0xA000L', '0x8948L', 35328L)


Listing the imported symbols
===========================================================

Each directory, if it exists in the PE file being processed, has an entry as ``DIRECTORY_ENTRY_directoryname`` in the PE instance. The imported symbols can be listed as follows:

.. code-block::
    
    # If the PE file was loaded using the fast_load=True argument, we will need to parse the data directories:

    pe.parse_data_directories()

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
      print entry.dll
      for imp in entry.imports:
        print '\t', hex(imp.address), imp.name


Output
-----------------------------------------------------------

.. code-block::
    
    comdlg32.dll
            0x10012A0L PageSetupDlgW
            0x10012A4L FindTextW
            0x10012A8L PrintDlgExW
    [snip]
    SHELL32.dll
            0x1001154L DragFinish
            0x1001158L DragQueryFileW


Listing the exported symbols
===========================================================

Similarly, the exported symbols can be listed as follows:

.. code-block::
    
    for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
      print hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal


Output
-----------------------------------------------------------

.. code-block::
    
    0x7ca0ab4f SHUpdateRecycleBinIcon 336
    0x7cab44c0 SHValidateUNC 173
    0x7ca7b0aa SheChangeDirA 337
    0x7ca7b665 SheChangeDirExA 338
    0x7ca7b3e1 SheChangeDirExW 339
    0x7ca7aec6 SheChangeDirW 340
    0x7ca8baae SheConvertPathW 341


Dumping all the information
===========================================================

.. code-block::
    
    print pe.dump_info()

Will produce a full textial dump of all the parsed information.


Retrieving the bytes at the entry point
===========================================================

We can use *pefile* together with tools like `pydasm <http://dkbza.org/pydasm.html>`__ to build a small disassembler. A toy example might look like the following.

We first fetch the entry point address, the retrieve 100 bytes starting at the entry point and we loop through the data disassembling as we go:

.. code-block::
    
    ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    ep_ava = ep+pe.OPTIONAL_HEADER.ImageBase
    data = pe.get_memory_mapped_image()[ep:ep+100]
    offset = 0
    while offset < len(data):
      i = pydasm.get_instruction(data[offset:], pydasm.MODE_32)
      print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, ep_ava+offset)
      offset += i.length


Output
-----------------------------------------------------------

.. code-block::
    
    push byte 0x70
    push dword 0x1001888
    call 0x1006ca8
    xor ebx,ebx
    push ebx
    mov edi,[0x100114c]
    call edi
    cmp word [eax],0x5a4d
    jnz 0x1006b1d
    mov ecx,[eax+0x3c]
    add ecx,eax
    cmp dword [ecx],0x4550
    jnz 0x1006b1d
    movzx eax,[ecx+0x18


Parsing part of the file
===========================================================

Sometimes we might not want to process an entire file if it's very large. Parsing can be time consuming in some cases an we might only be interested in a subset of the information provided by the headers and directories.

It is possible to indicate *pefile* to only load a minimal set of the headers (up to the NT Headers) with the ``fast_load`` keyword argument and leave the directories unprocessed. The directories can be parsed later on, on demand.

The following example loads the basic headers and then goes on to parse most of the directories avoiding the relocation information.

.. code-block::
    
    pe = pefile.PE(os.sys.argv[1], fast_load=True)
    pe.parse_data_directories( directories=[ 
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_RESOURCE'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_DEBUG'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_TLS'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT'] ] )