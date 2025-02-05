## Issue 0079: Is the address of a standard library function the same in different translation units?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_079.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_079.html)

Item 16 \- constancy of system library function addresses

(These questions approach the same problem from three slightly different
directions.)

a. If a pointer to a given standard library function (say `strlen`) is evaluated
in two different translation units, and the pointers compared, must they compare
equal?

b. Can a conforming implementation declare a standard library function as having
internal linkage, or must the identifiers with file scope declared in standard
headers have external linkage?

c. If the contents of the header `<string.h>` include the following definition
of `strlen`, is the implementation conforming?

```c
static size_t strlen (const char *__s)
        {
        size_t __len = 0;

        while (*__s++)
                __len++;
        return __len;
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

Since the answer to question (b) is needed for question (a) it is given first.

b) Since, according to the fourth item in subclause 7.1.3, the library function
prototypes are implicitly `extern`, the standard library functions have external
linkage.

a) If the usage of `strlen` is such that standard library functions are referred
to, the pointers must compare equal by the requirements of subclauses 5.1.1.2
and 6.1.2.2.

c) The contents of standard headers are implementation-defined. For instance,
they may contain code written in other languages. It is not the job of this
Committee to mandate implementation. Whatever their contents, including a
standard header must achieve the effects required by the C Standard.
