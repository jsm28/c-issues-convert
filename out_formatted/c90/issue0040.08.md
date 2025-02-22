## Issue 0040.08: What arithmetic can be performed on a `char` holding a defined character literal value?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Refer to subclause 6.1.2.5, page 22, lines 32-36:

a.

```c
char c = 7; /* implementation defined behavior, since 7 need not
 be a member of the basic execution character set */
```

b.

```c
c = 'a'; /* ok */
 c++; /* implementation defined */
```

c.

```c
c = '1'; /* ok */
 c++; /* ok? */
```

It has been suggested that the above constructs are not implementation defined.

Subclause 6.1.3.4, page 29, lines 30-33:

d.

```c
c = '\07'; /* what is in the source/execution character set is
 given in subclause 5.2.1. Anything else is an extension. */
```

e.

```c
c = '$';
```

It has been suggested that characters may be added to the basic source/execution
character set without implementation defined behavior being invoked. (I guess my
position on this item can be deduced from the text.)

---

Comment from WG14 on 1997-09-23:

### Response

a. Subclause 6.1.2.5 says “An object declared as type `char` is large enough to
store any member of the basic execution character set... If other quantities are
stored in a `char` object, the behavior is implementation-defined: the values
are treated as either signed or nonnegative integers.” Consider this example:

```c
char c = 7;
```

The assignment `c = 7` is not implementation-defined because, from a reasonable
reading of subclause 6.1.2.5, it is clear that the only implementation-defined
behavior here is the signedness of the value of the `char` object.

b. Another example:

```c
c = 'a';
 c++;
```

The increment of `c` after assigning an `'a'` to it is defined by the
implementation because the numeric encoding of `'a'` is defined by the
implementation. If `'a'` were equal to `CHAR_MAX`, the increment could even
cause an overflow (cf. subclause 5.2.1).

c. Another example:

```c
c = '1';
 c++;
```

The increment of `c` after assigning a `'1'` to it is not implementation-defined
because the characters `'0'` through `'9'` are required to be a contiguous range
(cf. subclause 5.2.1). Thus, the result is `'2'`.

d. Another example:

```c
c = '\07';
```

The value of the character constant `'\07'` is defined by the C Standard (cf.
subclause 6.1.3.4, page 29, line 10-13). The implementation-defined behavior of
some escape sequences, described on page 29, lines 30-33, is clarified in the
example on page 30, lines 8-14.

e. Another example:

```c
c = '$';
```

If `$` is in the execution character set, the value of `'$'` is locale-specific
and so must be defined by the implementation (cf. subclause 5.2.1).
