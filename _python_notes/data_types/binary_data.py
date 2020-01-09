#!/usr/bin/env python

from struct import Struct

"""
File
    Can be opened in binary mode.
    Allows "raw", or non-delimited reads, which does not treat newlines and carriage returns as special.
    read()
        In binary mode, read() will return a bytes object (array of 8-bit integers), not a Python string (array of Unicode characters.

decode()
    Convert the bytes object to a string.
encode()
    Convert Python string to bytes object.
write()
    Write raw data to a file.
seek()
    Position the next read.
tell()
    Determine the current location within the file.

Networks
    Use binary data.
    Convert to a standard if mixing platforms.
    Need to know layout of data.

Webpages
    Typically encoded as ASCII or UTF-8 (represented by bytes object, which is an arrya of bytes).
"""


"""
Struct
    Translate between Python and native/standard formats
    Format string describes data layout
        Each code is a letter representing a data type, cand can be preceded with a size or repeat count (depending on data type),
        and a prefix which specifies the byte order and alignment.
    Instantiate Struct with a format string representing the binary data layout.
    unpack()
        From Struct instance call to decode a binary strea
    pack()
        From Struct instance call to encode a binary strea
    size
        Property is the number of bytes needed for the data
    Native
        Byte order or alignment refers to the same byte order or alignment used by the C compoiler on the current platform.
        Default
    Standard
        Refers to a standar set of sizes for typical numerical objects, such as shorts, ints, longs, floats and doubles.
"""


"""
Struct Format Codes

Format      C Type              Python Type         Standard size   Notes
------------------------------------------------------------------------------
x           pad byte            no value            n/a             
c           char                bytes of length 1   1
b           signed char         integer             1               (1), (3)
B           unsigned char       integer             1               (3)
?           _Bool               bool                1               (1)
h           short               integer             2               (3)
H           unsigned short      integer             2               (3)
i           int                 integer             4               (3)
I           unsigned int        integer             4               (3)
l           long                integer             4               (3)
L           unsigned long       integer             4               (3)
q           long long           integer             8               (2), (3)
Q           unsigned long long  integer             8               (2), (3)
n           ssize_t             integer                             (4)
N           size_t              integer                             (4)
f           float               float               4               (5)
d           double              float               8               (5)
s           char[]              bytes
p           char[]              bytes
P           void *              integer                             (6)

Notes
1. The '?' conversion code corresponds to the _Bool type defined by C99. If this type is not available, it is simulated using a char. In standard mode, it is always represented by one byte.
2. The 'q' and 'Q' conversion codes are available in native mode only if the platform C compiler supports C long long, or, on Windows, __int64. They are always available in standard modes.
3. When attempting to pack a non-integer using any of the integer conversion codes, if the non- integer has a index() method then that method is called to convert the argument to an integer before packing.
4. The 'n' and 'N' conversion codes are only available for the native size (selected as the default or with the '@' byte order character). For the standard size, you can use whichever of the other integer formats fits your application.
5. For the 'f' and 'd' conversion codes, the packed representation uses the IEEE 754 binary32 (for 'f') or binary64 (for 'd') format, regardless of the floating-point format used by the platform.
6. The 'P' format character is only available for the native byte ordering (selected as the default or with the '@' byte order character). The byte order character '=' chooses to use little- or big- endian ordering based on the host system. The struct module does not interpret this as native ordering, so the 'P' format is not available.

Struct byte order/size/alignment flags

Flag        Byte order      Size and byte alignment
----------------------------------------------------
@ default   Native          Native
=           Native          Standard
<           Little-endian   Standard
> or !      Big-endian      Standard
"""

# Mixed values/types
values = 7, 6, 42.3, b'Guido'

# Create struct instance with desired data layout
demo = Struct('iif10s')

# Size property gives size of data in bytes
print("Size of data: {} bytes".format(demo.size))

# pack() converts values into binary stream using format
binary_stream = demo.pack(*values)

# unpack() converts binary stream into list of values
int1, int2, float1, raw_bytes = demo.unpack(binary_stream)

# decode() raw bytes into a string
# rstrip() off trailing null bytes (that were added by pack())
str1 = raw_bytes.decode().rstrip('\x00')

print(raw_bytes)
print(int1, int2, float1, str1)


"""
Read binary
    Add "b" to "r", "w", or "a" for binary mode
"""
print('--> read binary')

with open("data/parrot.txt", "rb") as parrot_in:
    while True:
        # print out a file 10 bytes at a time
        chunk = parrot_in.read(10)
        # read "rb" returns bytes, not str
        if chunk == b"":
            break
        # Use decode() to convert bytes to str
        print(chunk.decode())
