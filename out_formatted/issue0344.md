## Issue 0344: Casts in preprocessor conditional expressions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, Clark Nelson  
Date: 2007-04-23  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_344.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_344.htm)

### Summary

6.10.1 paragraph 1 states:

> The expression that controls conditional inclusion shall be an integral constant
> expression except that: it shall not contain a cast; ...

The prohibition of casts is vacuous, as pointed out in the footnote in that
paragraph:

> Because the controlling constant expression is evaluated during translation
> phase 4, all identifiers either are or are not macro names — there simply are no
> keywords, enumeration constants, and so on.

As a result, there can be no casts, which require either keywords or identifiers
that resolve to types in order to be recognized as casts.

The prohibition of casts is also misleading: the presence of a "shall not" in a
"Constraints" paragraph suggests that an implementation is required to diagnose
this condition. However, in an example like this:

> ```c
> #if (int)+0
> ```

There is a construct which appears to be a cast, but is not, and is
syntactically and semantically valid.

### Suggested Technical Corrigendum

Change 6.10.1p1:

> The expression that controls conditional inclusion shall be an integer constant
> expression except that: <del>it shall not contain a cast;</del> identifiers
> (including those lexically identical to keywords) are interpreted as described
> below;<sup>141\)</sup> and it may contain unary operator expressions of the form

---

Comment from WG14 on 2007-07-21:

### Technical Corrigendum

Change 6.10.1p1:

> The expression that controls conditional inclusion shall be an integer constant
> expression except that: <del>it shall not contain a cast;</del> identifiers
> (including those lexically identical to keywords) are interpreted as described
> below;<sup>141\)</sup> and it may contain unary operator expressions of the form
