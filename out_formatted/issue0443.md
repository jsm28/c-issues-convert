## Issue 0443: Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 4

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Joseph Myers  
Date: 2013-07-21  
Reference document: [N1730](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1730.pdf)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Some issues with floating point in C11 have been identified as part of the UK
review of the N1711 draft of TS 18661-1. While such issues relate to the general
area of C bindings to IEC 60559:2011, and so could be addressed in the TS on
that basis, since the issues also apply to C11 as-is it may be more appropriate
to address some or all of these issues as Defect Reports with a view to having a
normative fix in a future TC to C11 rather than only having a fix in conjunction
with the new bindings.

Issue 4: Floating-point state not being an object

The description of the floating-point environment in C11 fails to make
sufficiently clear what is or is not an object (C11 footnote 205 is not
normative, and so cannot be used to that effect); it uses terms such as "system
variable" without saying what that is. Simply moving that footnote to normative
text would fix this issue:

> Move the contents of footnote 205 (C11 subclause 7.6) to the end of 5.1.2.3#2.

---

Comment from WG14 on 2015-04-17:

Oct 2013 meeting

### Committee Discussion

* The committee agrees that the floating point environment is not an object and must be stated in normative terms instead of in non-normative footnote 205\.
* The environment may be modified more than once in an expression without inducing undefined behavior, this is just "how it works".
* The floating-point environment is described in the standard using an otherwise undefined term "system variable" having 7.6p2 thread storage duration, implying that it is an object, and so this is perhaps the actual manifestation of the defect that requires correction.
* The floating-point environment is technically an actor, not an object, having a model of its behavior defined purely by messages as its internal "piece of state" is not directly visible. In this case the messages are the macros and functions, as are the electronic signals from the floating-point computational units to consult and honor the desired floating point modal behaviors, and the electronic signals that record "auxiliary information" in the model for floating point exceptions.
* In any case, the floating point environment implementation is not described by the abstract C machine, only its operations.
* The committee prefers that this be cleared up in 7.6, by moving the second sentence and possibly the first sentence into normative text.

Apr 2014 meeting

### Committee Discussion

> The committee discusses this issue further and could not see an actual defect:
> there are no misinterpretations stated or implied.

### Proposed Committee Response

> Since operations on the floating point environment are well defined there is no
> need to normatively define anything further about its implementation. The
> footnote adds clarity and should remain as is.
