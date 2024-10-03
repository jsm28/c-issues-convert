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
