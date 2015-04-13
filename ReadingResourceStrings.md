# Introduction #

The following [document](http://www.skynet.ie/~caolan/publink/winresdump/winresdump/doc/resfmt.txt) has some useful notes on how resource strings are stored within the resources section in a PE file. Quoting directly from the document:

```
 4.8 String Table Resources 
 
 These tables are constructed in blocks of 16 strings.  The 
 organization of these blocks of 16 is determined by the IDs given to 
 the various strings.  The lowest four bits of the ID determine a 
 string s position in the block.  The upper twelve bits determine 
 which block the string is in.  Each block of 16 strings is stored as 
 one resource entry.  Each string or error table resource block is 
 stored as follows: 
 
    [Normal resource header (type = 6 for strings)] 
     
    [Block of 16 strings.  The strings are Pascal style with a WORD 
    length preceding the string.  16 strings are always written, even 
    if not all slots are full.  Any slots in the block with no string 
    have a zero WORD for the length.] 
     
 It is important to note that the various blocks need not be written 
 out in numerical order in the resource file.  Each block is assigned 
 an ordinal ID.  This ID is the high 12 bits of the string IDs in the 
 block plus one (ordinal IDs can t be zero).  The blocks are written 
 to the .RES file in the order the blocks are encountered in the .RC 
 file, while the CVTRES utility will cause them to become ordered in 
 the COFF object, and hence the image file. 
```

# Details #

Hence, to extract those string from the file, we can write a small Python script using _pefile_.

First we need to read the directory entry for the resources and see if there's an entry of type RT\_STRING (value 6).

```
print [entry.id for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries]
```

Would produce something like `(3, 4, 5, 6, 9, 14, 24)`. Therefore we know that in this specific PE file the RT\_STRING directory entry is at index 3.

A dump of the corresponding resource directory entry looks like:
```
  Id: [0x6] (RT_STRING)
  [IMAGE_RESOURCE_DIRECTORY_ENTRY]
  Name:                          0x6       
  OffsetToData:                  0x80000108
    [IMAGE_RESOURCE_DIRECTORY]
    Characteristics:               0x0       
    TimeDateStamp:                 0x0        [Thu Jan  1 00:00:00 1970 UTC]
    MajorVersion:                  0x0       
    MinorVersion:                  0x0       
    NumberOfNamedEntries:          0x0       
    NumberOfIdEntries:             0x1       
      Id: [0x7]
      [IMAGE_RESOURCE_DIRECTORY_ENTRY]
      Name:                          0x7       
      OffsetToData:                  0x80000320
        [IMAGE_RESOURCE_DIRECTORY]
        Characteristics:               0x0       
        TimeDateStamp:                 0x0        [Thu Jan  1 00:00:00 1970 UTC]
        MajorVersion:                  0x0       
        MinorVersion:                  0x0       
        NumberOfNamedEntries:          0x0       
        NumberOfIdEntries:             0x1       
          [IMAGE_RESOURCE_DIRECTORY_ENTRY]
          Name:                          0x409     
          OffsetToData:                  0x4B8     
            [IMAGE_RESOURCE_DATA_ENTRY]
            OffsetToData:                  0x251F0   
            Size:                          0x48      
            CodePage:                      0x0       
            Reserved:                      0x0       
```


We need to iterate through all the directory entries under the RT\_STRING directory and read the data entries in order to be able to reach the actual string data.

We can iterate through the entries with the following code:

(the strings will be saved in the _strings_ list)

```
# The List will contain all the extracted Unicode strings
#
strings = list()

# Fetch the index of the resource directory entry containing the strings
#
rt_string_idx = [
  entry.id for entry in 
  pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_STRING'])

# Get the directory entry
#
rt_string_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_string_idx]

# For each of the entries (which will each contain a block of 16 strings)
#
for entry in rt_string_directory.directory.entries:

  # Get the RVA of the string data and
  # size of the string data
  #
  data_rva = entry.directory.entries[0].data.struct.OffsetToData
  size = entry.directory.entries[0].data.struct.Size
  print 'Directory entry at RVA', hex(data_rva), 'of size', hex(size)

  # Retrieve the actual data and start processing the strings
  #
  data = pe.get_memory_mapped_image()[data_rva:data_rva+size]
  offset = 0
  while True:
    # Exit once there's no more data to read
    if offset>=size:
      break
    # Fetch the length of the unicode string
    #
    ustr_length = pe.get_word_from_data(data[offset:offset+2], 0)
    offset += 2

    # If the string is empty, skip it
    if ustr_length==0:
      continue

    # Get the Unicode string
    #
    ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=ustr_length)
    offset += ustr_length*2
    strings.append(ustr)
    print 'String of length', ustr_length, 'at offset', offset
```