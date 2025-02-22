## Issue 0156: Should calls to `fsetpos` with positions in closed and reopened streams be undefined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_156.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_156.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned. This Defect Report has been
prepared with considerable help from Mark Brader, Jutta Degener, Ronald
Guilmette, and a person whose employment conditions require anonymity. However,
except where stated, opinions expressed or implied should not be assumed to be
those of any person other than myself.*

Defect Report UK 004: Closed streams

Calls to `fsetpos` with positions in closed and reopened streams are permitted,
but should be undefined.

The definition of `fsetpos` (subclause 7.9.9.3) requires the `fpos_t` argument
to have a value generated by a successful call to `fgetpos` on the same stream.
However, it does not require the stream to refer to the same file. If the stream
does not so refer, the effect should be explicitly undefined.

### Suggested Technical Corrigendum:

In subclause 7.9.9.3, change:

... an earlier call to the `fgetpos` function on the same stream.

to:

... an earlier call to the `fgetpos` function on the same stream; there shall
not have been an intervening call to the `fclose` or `freopen` function with
that stream.

---

Comment from WG14 on 1997-09-23:

Technical Corrigendum

In subclause 7.9.9.2, page 145, change:

... an earlier successful call to the `ftell` function on the same stream ...

to:

... an earlier successful call to the `ftell` function on a stream associated
with the same file ...

In subclause 7.9.9.3, page 146, change:

... an earlier successful call to the `fgetpos` function on the same stream.

to:

... an earlier successful call to the `fgetpos` function on a stream associated
with the same file.
