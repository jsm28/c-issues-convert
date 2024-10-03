It is unclear how the `fscanf` function shall behave when executing directives
that include “ordinary multibyte characters,” especially in the case of
shift-encoded ordinary multibyte characters.

The following statements are described in subclause 7.9.6.2 **The `fscanf`
function** of the current standard:

A directive that is an ordinary multibyte character is executed by reading the
next characters of the stream. If one of the characters differs from one
comprising the directive, the directive fails, and the differing and subsequent
characters remain unread.

Assume a typical shift-encoded directive: `A\*` in 7-bit representation. And
consider two different encoding systems, Latin Alphabet No.1 \- 8859/1 and
German Standard DIN 66 003\. The codes are, for example,

```c
A; in 8859/1: SO 4/4 SI
 A; in DIN 66 003: ESC 2/8 4/11 5/11 ESC 2/8 4/2
```

`where SO` is a Shift-Out code (0/15 \= 0x0F) and **SI** corresponds to a
Shift-In code (0/14). “`ESC 2/8 4/11`” is an escape sequence for the German
Standard DIN 66 003, and “`ESC 2/8 4/2`” is for ISO 646 USA Version (ASCII).

Assuming that a subject sequence includes `A;`, `O;`, and `U;` with the
following 7-bit representations,

```c
in 8859/1: SO 4/4 5/6 5/12 SI
 in DIN 66 003: ESC 2/8 4/11 5/11 5/12 5/13 ESC 2/8 4/2
```

does the “`A;`” directive in the `fscanf` format string match the beginning part
of the“`A;O;U;`” sequence?

At what position of the target sequence shall the “`A;`” directive fail?

One interpretation of this is that because the current standard defined the
behavior of the directive in the `fscanf` format based on the word “character”
(byte), not using the term “multibyte character,” the comparison shall be done
on a byte-by-byte basis. One may conclude that the “`A;`” directive never
matches the “`;”;O;U` sequence in this case.

Another interpretation may lead to an opposite conclusion, saying that the
current standard's statements quoted above do not necessarily mean that such
comparison shall be done on a byte-by-byte basis. Instead, it is read that the
matching shall be done on a “multibyte character by multibyte character basis”
or rather “wide character by wide character basis.” Especially, a “ghost”
sequence like “`ESC ...`” and `SI`*`/`*`SO` characters should not be regarded as
independent ordinary multibyte characters in this case.

Which is a correct interpretation of the current standard?

These different interpretations are caused by the ambiguity of the descriptions
in the current standard. Also, it should be pointed out that the major problem
here is usage of the word “character.” The generic word “character” and the
specific word “character(\=byte)” should be properly discriminated in the
standard.
