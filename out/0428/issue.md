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
