###########################################################
Modifying PE Image Data
###########################################################

Overwrite values
===========================================================

The methods :py:func:`set_bytes_at_rva`, :py:func:`set_bytes_at_offset` exist to allow to easily modify the data in a PE image. They will update the data (propagating all changes) in all places where it's relevant, including the section objects.

:py:func:`set_bytes_at_rva(rva, data)`

Overwrite, with the given string, the bytes at the file offset corresponding to the given RVA. Return ``True`` if successful, ``False`` otherwise. It can fail if the offset is outside the file's boundaries.

:py:func:`set_bytes_at_offset(offset, data)`

Overwrite the bytes at the given file offset with the given string. Return ``True`` if successful, ``False`` otherwise. It can fail if the offset is outside the file's boundaries.

Writing values
===========================================================

Additionally, the following methods exist to write values into the PE image:

:py:func:`set_dword_at_rva(rva, dword)`

Set the double word value at the file offset corresponding to the given RVA.

:py:func:`set_dword_at_offset(offset, dword)`

Set the double word value at the given file offset.

:py:func:`set_word_at_rva(rva, word)`

Set the word value at the file offset corresponding to the given RVA.

:py:func:`set_word_at_offset(offset, word)`

Set the word value at the given file offset.

:py:func:`set_qword_at_rva(rva, qword)`

Set the quad-word value at the file offset corresponding to the given RVA.

:py:func:`set_qword_at_offset(offset, qword)`

Set the quad-word value at the given file offset.