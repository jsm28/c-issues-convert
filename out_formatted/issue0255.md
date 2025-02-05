## Issue 0255: non-prototyped function calls and argument mismatches

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Cross-references: [0316](issue0316.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_255.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_255.htm)

### Problem

Consider the code:

```c
   #include <stdio.h>
    int f ();
    int main (void)
    {
        return f (0);
    }
    #ifdef PROTO
    int f (unsigned int x)
    #else
    int f (x) unsigned int x;
    #endif
    {
        return printf ("%u\n", x);
    }
```

Now, 6.5.2.2#6 reads:

> \[#6\] If the expression that denotes the called function has a type that does
> not include a prototype, the integer promotions are performed on each argument,
> and arguments that have type float are promoted to double. These are called the
> default argument promotions.  
> \[...\]  
> If the function is defined with a type that includes a prototype, and either the
> prototype ends with an ellipsis (, ...) or the types of the arguments after
> promotion are not compatible with the types of the parameters, the behavior is
> undefined. If the function is defined with a type that does not include a
> prototype, and the types of the arguments after promotion are not compatible
> with those of the parameters after promotion, the behavior is undefined, except
> for the following cases:
>
> * one promoted type is a signed integer type, the other promoted type is the corresponding unsigned integer type, and the value is representable in both types;
> * both types are pointers to qualified or unqualified versions of a character type or `void`.

So the above code is undefined if `PROTO` is defined, but is legitimate if it is
not. This seems inconsistent.

Traditionally, when a function is called and no prototype is in scope, the
implementation applies the default argument promotions to the argument value and
then assumes that is the parameter type. If it isn't, this can cause all kinds
of problems, which is why the undefined behaviour. However, if it is known that
the argument value will be correctly handled by the parameter type, there is no
problem; this is the rationale behind the exceptions.

The exceptions should apply to both cases, no matter how the function is
eventually defined.

### Suggested Technical Corrigendum

Change the part of 6.5.2.2#6 after the omission to:

> If the types of the arguments after promotion are not compatible with those of
> the parameters after promotion 78A), the behavior is undefined, except for the
> following cases:
>
> * one promoted type is a signed integer type, the other promoted type is the corresponding unsigned integer type, and the value is representable in both types;
> * both types are pointers to qualified or unqualified versions of a character type or `void`.
>
> If the function is defined with a type that includes a prototype, and either any
> parameter has a type which is altered by the default argument promotions or the
> prototype ends with an ellipsis (, ...), the behavior is undefined.
>
> 78A) Because of the rule later in this paragraph, it is only necessary to check
> whether the parameter type undergoes promotion when the function is not defined
> using a prototype.

---

Comment from WG14 on 2002-05-15:

### Committee Response

The Committee does not wish to further refine the behavior of calls not in the
scope of prototypes. In practice, this will not be a problem, and the Committee
does not wish to define the behavior.
