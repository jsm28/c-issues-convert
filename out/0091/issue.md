Item 28 \- multibyte encodings

Does a locale with the following encoding of multibyte characters conform to the
C Standard?

The 99 characters of the basic execution character set have codes 1 to 99, in
the order mentioned in subclause 5.2.1.1 (so `'A' == 1`, `'a' == 27`, `'0' ==
53`, `'!' == 63`, `'\n' == 99`).

The extended execution character set consists of 16,256 (127 `*` 128\) two-byte
characters. For each two-byte character, the first byte is between 1 and 127
inclusive, and the second byte is between 128 and 255 inclusive.

Note that any sequence of bytes can unambiguously be broken into multibyte
characters, but the basic characters are prefixes of other characters.
