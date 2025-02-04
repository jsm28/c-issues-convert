## Issue 0250: non-directives within macro arguments

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Cross-references: [0303](issue0303.md), [0448](issue0448.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_250.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_250.htm)

### Problem

Consider the code:

```c
  #define nothing(x) // Nothing    /* Case 1 */
    nothing (
    #include <stdio.h>
    )
    /* Case 2 */
    nothing (
    #nonstandard
    )
```

6.10.3#11 reads in part:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives, the behavior is undefined.

This clearly covers case 1\. However, it is not clear whether or not case 2 is a
preprocessing directive. It is a "non-directive", but is that also a directive ?
If case 2 is a directive, it is undefined behaviour. If it is not, then case 2
is strictly-conforming and macro-expands to nothing.

Since non-directives are only valid as extensions, it might be more sensible for
them to behave as directives do and make the behaviour undefined in this case.

### Suggested Technical Corrigendum

In 6.10.3#11, change the last sentence to:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives or as non-directives (that is,
> the first pre-processing token on a line is a `#)`, the behavior is undefined.

---

Comment from WG14 on 2002-03-06:

### Committee Response

The Committee believes the Standard is correct (preprocessing directive includes
non-directive), therefore, the anwser to the question on this is *yes*.

### Technical Corrigendum

In 6.10 #2, italicize the term "preprocessing directive".

In 6.10.3 paragraph 11, last sentence. After "preprocessing directives", add the
following footnote.

> Despite the name, a non-directive is a preprocessing directive.
