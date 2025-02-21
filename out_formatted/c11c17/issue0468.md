## Issue 0468: `strncpy_s` clobbers buffer past `null`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Martin Sebor  
Date: 2014-09-19  
Reference document: [N1872](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1872.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

K.3.7.1.4, p5 permits `strncpy_s` to "clobber" characters in the destination
buffer past the terminating `null`:

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns. <sup>420\)</sup>

Footnote 420 explains that the intent is to allow implementations to copy
characters from `s2` to `s1` while simultaneously checking if any of those
characters are null. Such an approach might write a character to every element
of `s1` before discovering that the first element should be set to the null
character.

This intent is to allow efficient implementations to make a single pass over the
source sequence that simultaneously copies characters and checks the runtime
constraints. (Otherwise two passes would be required, one to compute the length
of the source sequence and another to copy it.)

It has been pointed out that the implementation latitude granted by this text
goes too far, since the function only might need to write past the null after a
constraint violation. Otherwise, when all runtime constraints are satisfied, the
function stops copying characters after either the first null is encountered or
all `n` characters have been copied.

Since the mention of unspecified values tends to raise security concerns about
information leakage, and since permitting the implementations to modify the
contents of the destination buffer past the terminating null on success serves
no useful purpose, the requirements on the function can and should be tightened
up.

### Suggested Technical Corrigendum

The proposed corrigendum below tightens up the requirements on the function so
as to leave intact the contents of the destination buffer past the terminating
null on success, while allowing it to clobber its contents on runtime constraint
violation.

Modify K.3.7.1.4, p5 as indicated below:

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns <ins>a non-zero value</ins>.
> <sup>420\)</sup>

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Proposed Technical Corrigendum

Change K.3.7.1.4, p5 from

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns. <sup>420\)</sup>

to

> All elements following the terminating null character (if any) written by
> `strncpy_s` in the array of `s1max` characters pointed to by `s1` take
> unspecified values when `strncpy_s` returns a non-zero value. <sup>420\)</sup>
