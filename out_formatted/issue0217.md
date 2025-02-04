## Issue 0217: `asctime` limits

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Closed  
Cross-references: [0326](issue0326.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_217.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_217.htm)

### Summary

The definition of the `asctime` function involves a `sprintf` call writing into
a buffer of size 26\. This call will have undefined behaviour if the year being
represented falls outside the range \[-999, 9999]. Since applications may have
relied on the size of 26, this should not be corrected by allowing the
implementation to generate a longer string. This is a defect because the
specification is not self-consistent and does not restrict the domain of the
argument.

### Suggested Technical Corrigendum

Append to 7.23.3.1\[#2]:

> except that if the value of `timeptr->tm_year` is outside the range \[-2899,
> 8099] (and thus the represented year will not fit into four characters) it is
> replaced by up to 4 implementation-defined characters.

---

Comment from WG14 on 2001-09-18:

### Committee Response

From 7.1.4 paragraph 1:

> If an argument to a function has an invalid value (such as a value outside the
> domain of the function, or a pointer outside the address space of the program,
> or a null pointer, or a pointer to non-modifiable storage when the corresponding
> parameter is not const-qualified) or a type (after promotion) not expected by a
> function with variable number of arguments, the behavior is undefined.

Thus, `asctime()` may exhibit undefined behavior if any of the members of
`timeptr` produce undefined behavior in the sample algorithm (for example, if
the `timeptr->tm_wday` is outside the range 0 to 6 the function may index beyond
the end of an array).

As always, the range of undefined behavior permitted includes:

* Corrupting memory
* Aborting the program
* Range checking the argument and returning a failure indicator (e.g., a null pointer)
* Returning truncated results within the traditional 26 byte buffer.

There is no consensus to make the suggested change or any change along this
line.
