## Issue 0287: Floating-point status flags and sequence points

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2003-04-13  
Reference document: [ISO/IEC WG14 C90 DR 087](issue0087.md)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Cross-references: [0087](issue0087.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_287.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_287.htm)

### Summary

The problem is, 6.5 Expressions (which existed in C90) was not updated when the
floating-point status flags were added to C99. Also, the response to C90 DR 087
was not incorporated into C99.

Consider the expression: `a = x*y + w*z;` where all variables are of type
`double` and each of the sub-expressions `x*y` and `w*z` raises the
floating-point overflow exception, which sets the floating-point overflow status
flag as a side-effect. The model used by C99 (5.1.2.3 Program execution, in
particular, paragraph 2 and footnote 11; as well as, 7.6 Floating-point
environment \<fenv.h\>, in particular, paragraph 1; 7.6.2 Floating-point
exceptions; and F.7.1 Environment management) and IEC 60599 / IEEE-754 is that
the status flags are sticky and may be set multiple times as side effects of
floating-point operations between sequence points. Setting the same
floating-point status flag multiple times is well defined: it is set.

Consider the expression: `b = (feclearexcept)(FE_OVERFLOW) +
(feraiseexcept)(FE_OVERFLOW);` which both clears and sets the same
floating-point status flag between two sequence points by the use of functions
(not macros). If the execution of the two functions is allowed to overlap, then
this is undefined behaviour (as the same object is being modified to two
different values at the "same" time (between the same pair of sequence points)).
If functions are atomic (not allowed to overlap execution), then, each function
evaluation is considered a sequence point, and the two modifies are not between
the same two sequence points. That means, there is no undefined behaviour, but
it is unspecified as to which of the two function calls is done first/last. I
understand that draft C89 had words similar to "Function calls are allowed to
overlap.", but that they were removed before C89 became a standard, and that
only those who know that bit of history know that C99 does not allow functions
to overlap execution. C90 Defect Report 087 had as part of its response
"function calls do not overlap", but those words are not in C99.

The same problem exists for `ERRNO`. Consider the expression: `b = (log)(-1.0) +
(exp)(DBL_MAX);` in which `log` sets `errno` to `EDOM`, while `exp` sets `errno`
to `ERANGE`.

Modifying the same status flag twice between two sequence points is a direct
contradiction of 6.5 Expressions, paragraph 2: "Between the previous and next
sequence point an object shall have its stored value modified at most once by
the evaluation of an expression." C99 needs to allow for multiple updates to the
same floating-point status flag.

### Suggested Technical Corrigendum

Add to 6.5 Expressions, paragraph 2, after the first sentance: An exception to
this shall be permitted if the object is a floating-point status flag and the
modification sets the flag.

Add to 6.5 Expressions, paragraph 3, after the last sentance: Function calls, in
the same expression-statement, do not overlap. Another possible place to add
this could be 6.5.2.2 Function calls, paragraph 10\. Possible wording issue:
recursive function calls.

---

Comment from WG14 on 2006-03-29:

### Committee Discussion

Flags are not objects, thus the constraint on modifying objects doesn't apply to
flags.

### Committee Response

As noted in the response to [DR 087](issue0087.md), function calls in the same
expression do not overlap. This has not changed for C99.

### Technical Corrigendum

Add a footnote to 6.5 Expressions, paragraph 2, after the first sentence.

> <sup>\*</sup>A floating-point status flag is not an object and can be set more
> than once within an expression.

Add a footnote to 7.6 Floating-point environment, paragraph 1, after the third
sentence.

> <sup>\*</sup>A floating-point status flag is not an object and can be set more
> than once within an expression.
