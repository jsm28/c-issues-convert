### Summary

**K.3.7.2.2 The strncat\_s function**  
The **strncat\_s()** has a constraint that neither **s1max** nor **n** shall be
greater than **RSIZE\_MAX.**  
Both s1max and n are defined as representing a number of char sized characters.  

**K.3.9.2.1.2 The wcsncpy\_s function**  
The same constraint is given for the function the **wcsncat\_s()** function,
i.e. that neither **s1max** nor **n** shall be greater than **RSIZE\_MAX**.  For
**wcsncat\_s(), s1max** and **n** are defined as representing a number of
**wchar\_t** sized characters.  On most implementations the size of a wide
characters is many times the size of a char.  On Solaris it is 4 time the size.   

**K.3.4 Integer types \<stdint.h\>** is defined as follows  
1 The header **\<stdint.h\>** defines a macro.  
2 The macro is  

**RSIZE\_MAX**  

which expands to a value 386\) of type **size\_t**. Functions that have
parameters of type **rsize\_t** consider it a runtime-constraint violation if
the values of those parameters are greater than **RSIZE\_MAX**.  

386\) The macro **RSIZE\_MAX** need not expand to a constant expression.  

**Recommended practice**  

3 Extremely large object sizes are frequently a sign that an object's size was
calculated incorrectly. For example, negative numbers appear as very large
positive numbers when converted to an unsigned type like size\_t. Also, some
implementations do not support objects as large as the maximum value that can be
represented by type size\_t.  

4 For those reasons, it is sometimes beneficial to restrict the range of object
sizes to detect programming errors. For implementations targeting machines with
large address spaces, it is recommended that **RSIZE\_MAX** be defined as the
smaller of the size of the largest object supported or **(SIZE\_MAX \>\> 1\)**,
even if this limit is smaller than the size of some legitimate, but very large,
objects. Implementations targeting machines with small address spaces may wish
to define **RSIZE\_MAX** as **SIZE\_MAX**, which means that there is no object
size that is considered a runtime-constraint violation.

---

The recommended practice implies **RSIZE\_MAX** represents maximum object sizes.  

Footnote 386\) implies an implementation can adjust what **RSIZE\_MAX** expands
to depending upon the context in which it is being used.  But what I don't
understand is how, the user can take advantage of **RSIZE\_MAX** to check the
values of n and s1max prior to calling the function **wcsncpy\_s** in order to
avoid violating the runtime constraint error.  There is no context in which the
implementation can expand **RSIZE\_MAX** to the value they need.  

Example:

```c
  if ((s1max <= RSIZE_MAX) & (n <= RSIZE_MAX))
     error = wcsncpy_s (s1, s1max, s2 n);  // Assume no other runtime constraints
     if (error != 0) {
        // Since RSIZE_MAX is not a constant expression
        // Can this ever occur due to s1max or n being greater than RSIZE_MAX?
     }
  }
```

Is a conforming implementation allowed  to return a non-zero value for
**wcsncpy\_s()** in the example above?  

N1147 the Rationale for TR24731 explains implementations might wish to adjust
the value of **RSIZE\_MAX** dynamically, and gives several scenarios for doing
so. None of which seem germane to the questions raised here.

---

So what is the purpose of providing the macro **RSIZE\_MAX**?  
If the purpose is to limit all buffer sizes to **RSIZE\_MAX**, it's use in
constraints for wide character functions appear to be malformed.  

The definitions of **wcsncpy\_s()** and **strncat\_s()** have constraints that
treat their arguments that represent character counts as if those counts
represent the size of an object that can be tested against **RSIZE\_MAX** in the
same way.  But those character counts represent characters of very different
sizes.  And thus very different object sizes.  Maybe the constraint error for
**wcsncpy\_s()** arguments **smax1** and **n** should be rewritten as something
like:  

Neither **(s1max \* sizeof(wchar\_t))** nor **(n \* sizeof(wchar\_t))** shall be
greater than **RSIZE\_MAX**.  

Other functions where max argument represent the number of  
wchar\_t or multi-byte characters and may need similar changes  
include:  

**mbstowcs\_s  
wcstombs\_s  
snwprintf\_s  
swprintf\_s  
swscanf\_s  
vsnwprintf\_s  
vswprintf\_s  
wcscpy\_s  
wcsncpy\_s  
wmemcpy\_s  
wmemmove\_s  
wcscat\_s  
wcstok\_s  
wcrtomb\_s  
mbsrtowcs\_s  
wcsrtombs\_s**

### Suggested Technical Corrigendum
