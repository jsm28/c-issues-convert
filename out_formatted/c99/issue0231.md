## Issue 0231: Semantics of *text-line* and *non-directive*

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Makoto Noda (Japan)  
Date: 2000-04-14  
Submitted against: C99  
Status: Closed  
Cross-references: [0448](../c11c17/issue0448.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_231.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_231.htm)

### Summary

The semantics of *text-line* and *non-directive* are not specified in the C99
Standard.

**Question**  
Are *text-line* and *non-directive* implementation-defined ?

---

Comment from WG14 on 2001-09-18:

### Committee Response

The standard is correct, but provide the following words with the response, and
include them in the Rationale document:

> Neither *text-line* nor *non-directive* is implementation defined. They are
> strictly defined as sequences of *pp-tokens* followed by *new-line*. Each of
> these rules represents a placeholder for an intermediate state in the phases of
> translation, and is expressed as a non-terminal since it has no associated
> semantics at this phase.  
>
> However, these sequences of *pp-tokens* are still subject to normal processing
> in the subsequent phases of translation.
