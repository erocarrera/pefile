###########################################################
Modifying PE Image Data
###########################################################

Overwrite values
===========================================================

The methods :py:func:`set_bytes_at_rva`, :py:func:`set_bytes_at_offset` exist to allow
the easy modification of the data in a PE image. They will update the data
(propagating all changes) in all the relevant places, including the section objects.

:py:func:`set_bytes_at_rva`

Overwrite, with the given string, the bytes at the file offset corresponding to the given RVA.
Return Trueif successful, False otherwise. It can fail if the offset is outside the file's boundaries.

:py:func:`set_bytes_at_offset`

Overwrite the bytes at the given file offset with the given string.
Return Trueif successful, False otherwise. It can fail if the offset is outside the file's boundaries.

Writing values
===========================================================

Additionally, the following methods exist to write values into the PE image:

:py:func:`set_dword_at_rva`

Set the double word value at the file offset corresponding to the given RVA.

:py:func:`set_dword_at_offset`

Set the double word value at the given file offset.

:py:func:`set_word_at_rva`

Set the word value at the file offset corresponding to the given RVA.

:py:func:`set_word_at_offset`

Set the word value at the given file offset.

:py:func:`set_qword_at_rva`

Set the quad-word value at the file offset corresponding to the given RVA.

:py:func:`set_qword_at_offset`

Set the quad-word value at the given file offset.