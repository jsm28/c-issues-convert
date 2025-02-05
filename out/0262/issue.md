### Problem

6.7.2.1#3 reads, in part:

> \[#3\] The expression that specifies the width of a bit-field shall be an
> integer constant expression that has nonnegative value that shall not exceed the
> number of bits in an object of the type that is specified if the colon and
> expression are omitted.

Is "the number of bits of the type ..." the width or is it the number of bits in
the object representation ?

Since it might not be practical to make use of padding bits in such an object,
the former would be more sensible.

### Suggested Technical Corrigendum

Change the cited text to read:

> \[#3\] The expression that specifies the width of a bit-field shall be an
> integer constant expression that has nonnegative value that shall not exceed
> **the width of an object** of the type that is specified if the colon and
> expression are omitted.

(bold type shows the changed words)
