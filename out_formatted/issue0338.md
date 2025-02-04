## Issue 0338: C99 seems to exclude **indeterminate value** from being an uninitialized register

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Rich Peterson \<Rich.Peterson@hp.com\>, Rich Peterson (US)  
Date: 2007-03-09  
Reference document: [WG14 N1124](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1124.pdf)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_338.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_338.htm)

### Summary

The following function has undefined behavior under C90, but appears to be  
strictly conforming under C99:

```c
  int foo(void) {
      unsigned char uc;
      return uc + 1 >= 0;
  }
```

If that is true, then a C99 compiler for a real-life architecture like ia64  
that supports trap representations in hardware (via NaT values) cannot in  
general just allocate **auto** variables to registers and leave initialization  
to the source code as it would for most other architectures. Instead it  
would either have to initialize the register or allocate the variable to  
memory. This is because ia64 NaT values only exist in register representations,  
not in memory representations.

**Rationale**

In C90, 3.16 defines **undefined behavior** as "behavior, upon use of a  
non-portable or erroneous program construct, of erroneous data, or of  
indeterminately valued objects, for which the standard imposes no  
requirements...". And 6.5.7 says: "If an object that has automatic storage  
duration is not initialized explicitly, its value is indeterminate." So it  
directly follows that the above function has undefined behavior under C90.

C99 then added a definition for **indeterminate value** (3.17.2): "either an  
unspecified value or a trap representation". The first problem is that the  
type unsigned char specifically is excluded from having any trap  
representations. This would seem to render non-conforming a NaT  
consumption fault when evaluating uc \+ 1 in the example function.  
Furthermore, my reading of 6.2.6.2 "Integer types" is that in order for  
any type to have trap representations, there must be padding bits in the  
in-memory representation of the type. This is because there does not  
appear to be any allowance for padding bits that are present only in the  
register representation of a type, but not in memory.

Since ia64 NaT values clearly exhibit the properties intended for C99  
trap representations, offering one of the few hardware implementations  
of those properties, it seems most likely that either my reading is  
faulty, or that the words do not correctly express the intent. I  
believe the intent of excluding type **unsigned char** from having trap  
representations was to allow it to be used to copy (via memcpy)  
arbitrary memory, in the case that memory might contain trap  
representations for some types. I believe it was not the intent to  
require translators to perform run-time initialization of uninitialized  
auto objects of type **unsigned char** in order to suppress hardware  
detection of programming faults. And I believe it certainly was not the  
intent to require that all trap representations for any type be  
representable in memory, forbidding register-only trap representations  
like NaT values.

Unless someone can find text that supports register-only trap  
representations, I think this deserves a TC.

### Suggested Technical Corrigendum

*Page 6, 3.17.2, change the definition of "indeterminate value"*

Old:  
either an unspecified value or a trap representation

New:  
either an unspecified value or a trap representation; or in  
the case of an object of automatic storage duration whose address  
is never taken, a value that behaves as if it were a trap  
representation, even for types that have no trap representations  
in memory (including type **unsigned char)**

---

Comment from WG14 on 2008-09-12:

### Committee Discussion (for history only)

#### Spring 2007

On some hardware (e.g. Itanium), an 8-bit value may have as many as 257
different values (0-255 and a "Not a Thing" value). However, c99 explicitly
forbids such a value for an unsigned char.

Page 6, 3.17.2, change the definition of *indeterminate value* to:

> either an unspecified value or a trap representation; or in the case of an
> object of automatic storage duration whose address is never taken, a value that
> behaves as if it were a trap representation.

5.1.2.3 para 5 second bullet speaks to this also.

#### Fall 2007

See WG14 e-mail *SC22WG14.11380*

While some agreed with the comments in this email others did not.

#### Spring 2008

Regarding WG14 e-mail *SC22WG14.11380*, the observations about trap
representations are correct, and it is unfortunate that the DR was written in a
way that relied on trap representation terminology and behavior. In fact, the
problem and solution are not really related to *trap representation* as defined
in the standard at all.

A better way to describe the issue might be to talk about use of an
uninitialized object that is eligible to have register storage class (i.e. an
object of automatic storage duration whose address is never taken).

Also the original DR's suggested wording change was made in the definition of
*indeterminate value*. The reason for that was to trigger undefined behavior,
which would have worked in C90, but in C99 the definition of undefined behavior
was changed such that it does not mention indeterminate value.

**Change for C1X:**

> 6.3.2.1 paragraph 2, add a sentence to the end:
>
> > If the lvalue designates an object of automatic storage duration that could have
> > been declared with register storage class (never had its address taken), and
> > that object is uninitialized (not declared with an initializer, and no
> > assignment to it has been performed prior to the use), the behavior is
> > undefined.
