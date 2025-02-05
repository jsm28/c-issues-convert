### Problem

Consider the code:

```c
   void jim ();
    void sheila (void);
    // ...   sheila (jim ());   /* Line A */
    jim (sheila ());   /* Line B */
```

Line A violates the constraint of 6.5.2.2#2, that requires the argument to have
a type that can be assigned to the parameter type. But line B doesn't because
that constraint only applies to prototyped functions. 6.5.2.2#4 reads in part:

> \[#4\] An argument may be an expression of any object type.

but this is not a constraint. Should it not be ? After all, the compiler has to
know the type of the argument in order to compile the function call, so it can
check at that point that the argument has a complete object type.

### Suggested Technical Corrigendum

Add a new paragraph #1a following 6.5.2.2#1:

> \[#1a\] Each argument shall have a type which is a completed object type.
