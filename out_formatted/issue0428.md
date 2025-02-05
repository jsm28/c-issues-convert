## Issue 0428: runtime-constraint issue with sprintf family of routines in Annex K

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Douglas Walls  
Date: 2013-02-11  
Reference document: [N1672](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1672.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0433](issue0433.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

snprintf\_s  (Annex K.3.5.3.5)  

In the "Runtime-constraints" section, K.3.5.3.5p2 first sentence it says:  

"Neither s nor format shall be a null pointer. n shall neither equal  
zero nor be greater than RSIZE\_MAX."  

So,

```c
    if (n == 0 || n > RSIZE_MAX)
        /* runtime constraints violation */
```

This is clear. However the next paragraph K.3.5.3.5p3, says this about "s":  

"If there is a runtime-constraint violation, then if s is not a null  
pointer and n is greater than zero and less than RSIZE\_MAX, then the  
snprintf\_s function sets s\[0\] to the null character."  

So, it takes action when (n \< RSIZE\_MAX)

```c
        if (s != NULL && n > 0 && n < RSIZE_MAX)
            s[0] = '\0';
```

Question here is, what if n equals RSIZE\_MAX? Should we still reset  
s\[0\]?  

If I were to say this looks like a typo, would WG14 agree with me?  

That is the text of K.3.5.3.5p3 should be:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  snprintf\_s function sets s\[0\] to the null character.  
    
This issue applies to all the sprintf family of routines in Annex K

### Suggested Technical Corrigendum

snprintf\_s  
Replace K.3.5.3.5p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  snprintf\_s function sets s\[0\] to the null character.  

sprintf\_s  
Replace K.3.5.3.6p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  sprintf\_s function sets s\[0\] to the null character.  

vsnprintf\_s  
Replace K.3.5.3.12p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  vsnprintf\_s function sets s\[0\] to the null character.  

vsprintf\_s  
Replace K.3.5.3.13p3 with:  

  If there is a runtime-constraint violation, then if s is not a null  
  pointer and n is greater than zero and not greater than RSIZE\_MAX, then the  
  vsprintf\_s function sets s\[0\] to the null character.

---

Comment from WG14 on 2017-11-03:

Apr 2013 meeting

### Committee Discussion

* The committee agrees with the assessment and the suggested changes.
* There are, however, other places where similar changes are needed.

Oct 2013 meeting

### Committee Discussion

* Further investigation confirmed that there were several other functions that also need similar corrections to their runtime constraints. All of these additional functions also need additional corrections as specified in [DR433,](issue0433.md) and the full resolution of both this defect and the additional issue will be found in the Proposed Technical Corrigendum of [DR433.](issue0433.md)
* That list is:
  + K.3.9.1.3 The snwprintf\_s function
  + K.3.9.1.4 The swprintf\_s function
  + K.3.9.1.8 The vsnwprintf\_s function
  + K.3.9.1.9 The vswprintf\_s function
  + K.3.9.3.2.1 The mbsrtowcs\_s function
  + K.3.9.3.2.2 The wcsrtombs\_s function
* It is noted that with these changes that K.3.5.1.2 `tmpname_s` will have wording inconsistent with respect to these modifications.
* Consistent wording would be, in K.3.5.1.2p2 replace "less than or equal to RSIZE\_MAX" with "not greater than RSIZE\_MAX".
* As such, the committee continues to accept unchanged the Proposed Technical Corrigendum as partial fulfillment of this defect, and that full resolution of the other similar defects will be found in [DR433.](issue0433.md)

### Proposed Technical Corrigendum

snprintf\_s  
Replace K.3.5.3.5p3 with:  

If there is a runtime-constraint violation, then if s is not a null   pointer
and n is greater than zero and not greater than RSIZE\_MAX, then the  
snprintf\_s function sets s\[0\] to the null character.

sprintf\_s  
Replace K.3.5.3.6p3 with:  

If there is a runtime-constraint violation, then if s is not a null pointer and
n is greater than zero and not greater than RSIZE\_MAX, then the sprintf\_s
function sets s\[0\] to the null character.

vsnprintf\_s  
Replace K.3.5.3.12p3 with:  

If there is a runtime-constraint violation, then if s is not a null pointer and
n is greater than zero and not greater than RSIZE\_MAX, then the   vsnprintf\_s
function sets s\[0\] to the null character.

vsprintf\_s  
Replace K.3.5.3.13p3 with:  

If there is a runtime-constraint violation, then if s is not a null   pointer
and n is greater than zero and not greater than RSIZE\_MAX, then the  
vsprintf\_s function sets s\[0\] to the null character.
