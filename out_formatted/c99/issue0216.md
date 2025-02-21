## Issue 0216: Source character encodings

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_216.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_216.htm)

### Summary

The Standard is clear that the basic source character set need not have the same
encoding as the basic execution character set, and that while the latter must be
all positive, there is no such requirement on the former:

6.2.5:

> \[#3\] \[...\] If a member of the basic execution character set is stored in a
> char object, its value is guaranteed to be positive.

6.10.1:

> \[#3\] \[...\] Whether the numeric value for these character constants matches
> the value obtained when an identical character constant occurs in an expression
> (other than within a `#if` or `#elif` directive) is
> implementation-defined.<sup>141\)</sup> Also, whether a single-character
> character constant may have a negative value is implementation-defined.

However, there are two problems with this. Firstly, the cited wording in 6.2.5
conflicts with the definition of the basic execution character set:

5.2.1:

> \[#2\] \[...\] A byte with all bits set to 0, called the *null character*, shall
> exist in the basic execution character set; it is used to terminate a character
> string.

in that zero is not positive. Secondly, it is not clear whether a source
character constant can have the value zero; in other words, can:

```c
  #if !'A'
    #error Character A is zero
    #endif
```

reach the `#error` directive ?

### Suggested Technical Corrigendum

Change the cited wording in 6.2.5 to:

> #3\] \[...\] If a member of the basic execution character set (other than the
> null character) is stored in a char object, its value is guaranteed to be
> positive.

and the last part of the cited wording in 6.10.1 to:

> \[#3\] \[...\] Also, whether a single-character character constant may have a
> negative value is implementation-defined (nevertheless, it may not be zero).

---

Comment from WG14 on 2000-11-02:

### Committee Response

Regarding the `#error` directive, 6.10.1 paragraph 3 states:

> The resulting tokens compose the controlling constant expression which is
> evaluated according to the rules of 6.6, except that all signed integer types
> and all unsigned integer types act as if they have the same representation as,
> respectively, the types `intmax_t` and `uintmax_t` defined in the header
> `<stdint.h>`. This includes interpreting character constants, which may involve
> converting escape sequences into execution character set members. Whether the
> numeric value for these character constants matches the value obtained when an
> identical character constant occurs in an expression (other than within a `#if`
> or `#elif` directive) is implementation-defined.

The evaluation of the controlling constant expression according to the rules of
6.6 implies that character constants are converted into an execution character
set (translation phase 5\) just as it also implies that preprocessor tokens
representing integer constants are translated into integer constants
(translation phase 7).

Thus, all character constants operated upon by `#if` have been translated to
*some* execution character set. The liberty given by 6.10.1 paragraph 3 that
allows the value of character constants to differ in preprocessor versus
non-preprocessor expressions exists to allow cross-compilers to use a standalone
"native" preprocessor that is unaware of the cross-compiled target and its
execution character set.

Thus, in your example, the `#error` directive can never be reached on a
conforming implementation.

### Technical Corrigendum

Change the cited wording in 6.2.5 to:

> \[#3\] \[...\] If a member of the basic execution character set is stored in a
> char object, its value is guaranteed to be non-negative.
