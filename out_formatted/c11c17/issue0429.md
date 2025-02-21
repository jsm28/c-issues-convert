## Issue 0429: Should `gets_s` discard next input line when `(s == NULL)` ?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1673](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1673.htm) [N1748](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1748.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

gets\_s Annex K.3.5.4.1p2 says:  

"If there is a runtime-constraint violation, s\[0\] is set to the null  
character, and characters are read and discarded from stdin until a  
new-line character is read, or end-of-file or a read error occurs."  

The runtime-constraint violation here can be caused by a null "s"  
pointer.  Should we discard the next input line even if `(s == NULL)` ?  

The way it is written, it looks like the answer is yes.  However it is  
not clear to us that that was the intent.  Note also that s\[0\] cannot be  
set to the null character when `s==NULL`.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The issue is found in Annex K.3.5.4.1p3, not p2.
* The Microsoft implementation appears to treat this as a runtime-constraint violation.
* The Dikumware implementation leaves this behavior unspecified.

Oct 2013 meeting

### Committee Discussion

* Given that footnote 404 already provides guidance on this issue, the author and the committee agree that the answer to the question posed is indeed yes.
* The other issue with respect to `s[0]` cannot be set to the null character when `s==NULL` has been determined to be resolved by the following changes.

### Proposed Technical Corrigendum

In Annex K.3.5.4.1, replace paragraph 3 with the following:

> If there is a runtime-constraint violation, characters are read and discarded
> from `stdin` until a new-line character is read, or end-of-file or a read error
> occurs, and if `s` is not a null pointer `s[0]` is set to the null character.
