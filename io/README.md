# File operations
  open()
      2nd arg is access mode
      "w" - writing: overwrites the entire file
      "r" - reading a text file
      "a" - appending to a new or existing file
      "rb" - reading a binary file
      "wb" - writing to a binary file
  .write()
  .close()

  with keyword - auto closes file to avoid memory leaks.

## Read file
  No concept of buffer, but you can specify number of bytes to read (e.g. read(25)).
  file.read() - Reads the entire file including new line characters.
  file.read(n) - Reads n number of characters from the file.
  file.readlines() - Reads all the lines into a list.
  file.readline(n) - Reads n line number from the file.
  file.seek(offset, whence) - Navigate within the file.
  file.tell() - Get the current location within the file.

Remember Python will pick up where it left off when reading lines/files.
This means if you read the entire file (i.e. read()) then any subsequent calls won't read anything
since you've already read the entire file.
