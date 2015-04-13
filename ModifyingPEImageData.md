The methods "set\_bytes\_at\_rva", "set\_bytes\_at\_offset" exist to allow to easily modify the data in a PE image. They will update the data (propagating all changes) in all places where it's relevant, including the section objects.

  * `set_bytes_at_rva(rva, data)`
_Overwrite, with the given string, the bytes at the file offset corresponding to the given RVA.
Return True if successful, False otherwise. It can fail if the
offset is outside the file's boundaries._

  * `set_bytes_at_offset(offset, data)`
_Overwrite the bytes at the given file offset with the given string.
Return True if successful, False otherwise. It can fail if the
offset is outside the file's boundaries._

Additionally the following exist to write values into the PE image:

  * `set_dword_at_rva(rva, dword)`
_Set the double word value at the file offset corresponding to the given RVA._

  * `set_dword_at_offset(offset, dword)`
_Set the double word value at the given file offset._

  * `set_word_at_rva(rva, word)`
_Set the word value at the file offset corresponding to the given RVA._

  * `set_word_at_offset(offset, word)`
_Set the word value at the given file offset._

  * `set_qword_at_rva(rva, qword)`
_Set the quad-word value at the file offset corresponding to the given RVA._

  * `set_qword_at_offset(offset, qword)`
_Set the quad-word value at the given file offset._