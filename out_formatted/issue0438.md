## Issue 0438: `ungetc / ungetwc` and file position after discarding push back problems

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Austin Group, Nick Stoughton (US)  
Date: 2013-06-19  
Reference document: [N1720](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1720.htm), [Austin Group Defect #701](http://austingroupbugs.net/view.php?id=701)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

C11 (and C99 before it) state for both **ungetc()** and **ungetwc()** that

> A successful intervening call (with the stream pointed to by stream) to a file
> positioning function (fseek, fsetpos, or rewind) discards any pushed-back
> characters for the stream. ... The value of the file position indicator for the
> stream after reading or discarding all pushed-back characters shall be the same
> as it was before the characters were pushed back.

(7.21.7.10 p2 \& p5, with similar at 7.29.3.10 p2 \& p5). The "or discarding"
phrasing in p5 makes no sense: all of the listed functions which discard the
push back also \_set\_ the file position. The file position will end up as
whatever the function sets it to, not "the same as it was before the characters
were pushed back".

### Suggested Change

Change

> The value of the file position indicator for the stream after reading or
> discarding all pushed-back characters shall be the same as it was before the
> characters were pushed back.

to

> The value of the file position indicator for the stream after all pushed-back
> characters have been read shall be the same as it was before the characters were
> pushed back.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* This issue arises because of the different architectures of a buffered stream which can hold pushed back characters, and that of the underlying filesystem which honors seek independent of the buffering.
* The committee sentiment is that the suggested changes are nearly correct and have requested that the project editor suggest better wording, subject to further discussion.

Apr 2014 meeting

### Committee Discussion

> The Standard is correct as written because the intent is that the specified file
> position indicator is an intermediate state inside the file positioning function
> after the pushed-back characters are discarded but before the actual seek. That
> gives you a reliable file position from which to do the seek. It's not intended
> that the file positioning function doesn't set the file position indicator.

### Proposed Technical Corrigendum

Add a footnote to 7.21.7.10 paragraph 5, second sentence:

> Note that a file positioning function may further modify the file position
> indicator after discarding any pushed-back characters.

Add a footnote to 7.29.3.10 paragraph 5, second sentence:

> Note that a file positioning function may further modify the file position
> indicator after discarding any pushed-back wide characters.
