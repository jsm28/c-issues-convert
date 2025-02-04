## Issue 0430: `getenv_s`, `maxsize` should be allowed to be zero

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1674](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1674.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

getenv\_s, Annex K.3.6.2.1p2 under Runtime-constraints says:  

**name** shall not be a null pointer. **maxsize** shall neither equal zero nor
be greater than  
**RSIZE\_MAX**. If **maxsize** is not equal to zero, then **value** shall not be
a null pointer.  

Question here is, if maxsize really cannot be 0\.  If it cannot be  
zero, why does the 2nd sentence mention the condition that `(maxsize != 0)`?  

If maxsize can be 0, it would allow the value to be a null pointer  
which allows what is described in 6.6.2.1 of TR24731 (N1173) cleanly:  

The **getenv\_s** function can also be used to get the size needed to  
represent the result. This allows the programmer to first call  
**getenv\_s** to get the size, then allocate a buffer to hold the result,  
and then call **getenv\_s** again to actually obtain the result."  

if maxsize can be zero, then I think we would get the length of string thusly:

```c
    getenv_s(&len, NULL, 0, "HOME");
```

However, since maxsize cannot be 0 which also requires value not to be  
a null pointer, we would need to do something like this:

```c
    getenv_s(&len, something, 1, "HOME");
```

AFAICT, getnenv\_s as specified in C11 exactly matches what was in TR24731
(N1172).  
What is in TR24731 (N1172) does not coincide with what is in the rational  
for TR24731 (N1173).  The wording in TR24731 (N1172) (and by extension  
C11) is awkward and it certainly looks like an update intended to correspond to  
the rational for TR24731 (N1173) was either misapplied or not applied.

### Suggested Technical Corrigendum

Replace Annex K.3.6.2.1p2 second sentence with:  

**maxsize** shall not be greater than **RSIZE\_MAX**.  

K.3.6.2.1p2 would then read thusly:  

**name** shall not be a null pointer.  **maxsize** shall not be greater than  
**RSIZE\_MAX**.  If **maxsize** is not equal to zero, then **value** shall not
be a null pointer.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The proposed change seems appropriate and is consistent with the existing rationale.
* The committee notes that some implementations may need to change to avoid treating a value of zero for **maxsize** as a constraint violation.

### Proposed Technical Corrigendum

Replace Annex K.3.6.2.1p2 second sentence with:  

**maxsize** shall not be greater than **RSIZE\_MAX**.  

K.3.6.2.1p2 would then read thusly:  

**name** shall not be a null pointer.  **maxsize** shall not be greater than  
**RSIZE\_MAX**.  If **maxsize** is not equal to zero, then **value** shall not
be a null pointer.
