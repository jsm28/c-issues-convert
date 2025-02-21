## Issue 0483: `__LINE__` and `__FILE__` in macro replacement list

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1943](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1943.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Based upon my reading of the standard, it appears that the following are
ambiguous, so are a possible defect.

* The line number associated with a \_\_LINE\_\_ in a macro replacment list. It could be the line number of the macro replacment list or of the macro invocation.
* The source file name associated with a \_\_FILE\_\_ in a macro replacment list. It could be the file name of the macro replacment list or of the macro invocation.

An example of that.

```c
  #line 500
  #define MAC() __LINE__

  #line 1000
 int j = MAC();         /* is this 500 or 1000? */
```

However, 7.2.1.1 requires that the **assert** macro write information about the
call that has a false expression. That information includes the \_\_LINE\_\_ and
\_\_FILE\_\_ preprocessing macros. So, there is a requirement that this specific
macro using \_\_LINE\_\_ and \_\_FILE\_\_ have the line number and file name of
the invocation, not the line number and file name of the replacment list (in
\<assert.h\>).

### Suggested Technical Corrigendum

Add to 6.10.8.1, paragraph 1, item \_\_LINE\_\_:

> The line number associated with a \_\_LINE\_\_ in a macro replacment list is the
> line number of the macro invocation.

Add to 6.10.8.1, paragraph 1, item \_\_FILE\_\_:

> The source file name associated with a \_\_FILE\_\_ in a macro replacment list
> is the source file name of the macro invocation.

---

Comment from WG14 on 2016-10-21:

Oct 2015 meeting

### Committee Discussion

> The committee notes that these issues are also raised in the WG21 C\+\+
> committee document
> [N4220](https://www.open-std.org/jtc1/sc22/wg21/www/docs/papers/2014/n4220.pdf).
> However, the committee also notes that among all implementations “nobody gets
> this wrong” and as such there is no actual confusion, and although there is
> sentiment that the standard might not perfectly express its intent, it is clear
> enough to warrant no change.

### Proposed Committee Response

> The committee believes that since there is no evidence of confusion over the
> intent of the standard in this area by any implementor that there is no defect
> worth correcting at this time.
