## Issue 0014.01: Is `setjmp` a macro or a function?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Max K. Goff, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-049  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_014.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_014.html)

X/Open Reference Number KRT3.159.1

There are conflicting descriptions of the `setjmp()` interface in ISO 9899:1990.
In subclause 7.6 on page 118, line 8, it is stated that “It is unspecified
whether `setjmp` is a macro or an identifier declared with external linkage.”
Throughout the rest of the standard, however, it is referred to as “the `setjmp`
macro”; in addition, the rationale document states that `setjmp` must be
implemented as a macro. Please clarify whether `setjmp` must be implemented as a
macro, or may be a function as well as a macro, or may just be a function.

---

Comment from WG14 on 1997-09-23:

### Response

The standard states that `setjmp` can be either a macro or a function. It is
referred to as “the `setjmp` macro” just to avoid longwindedness. The rationale
document is incorrect in saying that it must be a macro.
