## Issue 0037: Can UNICODE or ISO 10646 be used as a multibyte code?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Isai Scheinberg, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-043  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_037.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_037.html)

Subclause 5.2.1.2 **Multibyte characters** states:

> The source character set may contain multibyte characters, used to represent
> members of the extended character set. The execution character set may also
> contain multibyte characters, which need not have the same encoding as for the
> source character set. For both character sets, the following shall hold:
>
> \- The single-byte characters defined in 5.2.1 shall be present.

and, a bit later on:

> \- A byte with all bits zero shall not occur in the second or subsequent bytes
> of a multibyte character.

My interpretation (and all of the experts that I consulted with) of the first
rule, is that the basic character set (A-z, 0-9, etc.) shall be coded in
one-byte code. All multibyte locales that I know (EUC variants, SJIS) follow
this rule. But I may still be wrong.

If the above is true, then both 10646 (other than CM 5\) and UNICODE fail this
rule and cannot be used as multibyte characters. UNICODE also fails the second
rule.

---

Comment from WG14 on 1997-09-23:

### Response

The following answers apply (almost) equally to ISO 10646-1 and UNICODE. They
are expressed in terms of ISO 10646-1.

Clause 3, page 2, lines 18-24 and 40-42 define “byte,” “character,” and
“multibyte character” as follows:

**byte**: The unit of data storage large enough to hold any member of the basic
character set of the execution environment.

**character**: A bit representation that fits in a byte. The representation of
each member of the basic character set in both the source and execution
environments shall fit in a byte.

**multibyte character**: A sequence of one or more bytes representing a member
of the extended character set of either the source or the execution environment.
The extended character set is a superset of the basic character set.”

Therefore, if ISO 10646-1 were used as a basic character set, then by definition
a byte would have to be large enough to hold each member of the ISO 10646-1
character set. Also by definition this would make ISO 10646-1 a valid multibyte
character set.

If a byte were only eight bits long, the following answer would hold. ISO
10646-1 represents, in a particular byte order, the character `'a'` for example
as follows.

```c
0 0 0 97
 ---- 16-bit version
 -------- 32-bit version
```

This fails subclause 5.2.1.2, page 11, lines 30-32:

\- A byte with all bits zero shall be interpreted as a null character
independent of shift state.

\- A byte with all bits zero shall not occur in the second or subsequent bytes
of a multibyte character.

Therefore, 8-bit bytes preclude the use of ISO 10646-1 as a multibyte character
set.
