## Issue 0294: Technical question on C99 `restrict` keyword

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: INCITS, Greg Davis, Green Hills Software  
Date: 2003-08-14  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_294.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_294.htm)

### Summary

I have a question on section 6.7.3.1 of the C99 spec.

Paragraph 4 is where this seems to get complicated.

Question 1\)

> "...Every other lvalue used to access the value of X shall also have its address
> based on P".

Consider the following example:

```c
        #include <stdlib.h>
        char * restrict a, * restrict b;

        void copy(char * restrict dest, char * restrict source)
        {
         int i;
        for (i = 0; i < 10; i++)
            dest[i] = source[i];
        }

        int main()
        {
         a = calloc(10);
         b = calloc(10);
         copy(a, b);
         return 0;
        }
```

Is this a legal program? If so, could you explain the following? From the
standpoint of `main()`, the memory in `a` is modified through the call to
`copy()`. However, it seems to me that based on the definition of *based on*,
the writes that modify `*a` are not *based on* the pointer `a`, but instead
they're based on `dest`. Doesn't this violate the guarantee above?

Question 2\)

> "Every access that modifies X shall be considered also to modify P, for the
> purposes of this subclause." \- Why is this necessary?

Question 3\)

> The same question for the rules on the copying of `restrict` pointers ("If P is
> assigned the value of a pointer expression E that is based on another restrict
> pointer object P2, associated with block B2, then either the execution of B2
> shall begin before the execution of B, or the execution of B2 shall end prior to
> the assignment."). Why is this necessary?

---

Comment from WG14 on 2004-09-28:

### Committee Response

**Question 1\)**

Yes, the program conforms to all requirements in the specification for the
`restrict` qualifier (though the call to function `calloc` should have two
arguments).

Some interpretation of this question is provided to clarify the response. The
response answers the interpretation.

The interpretation of this question is: I can see how the rules are followed for
the `restrict` qualifier on `dest`, relative to the execution of function
`copy`, but I don't see how the rules are followed for the restrict qualifier on
`a`, relative to the execution of `main`.

Here is a spelling out of all the requirements in the specification of the
`restrict` qualifier for this example. The following identify definitions in the
specification of the `restrict` qualifier.

* `D` is the declaration for the identifier `a` and `T` is `char`
* `P` is the object designated by `a`
* `B` is the block of `main`, whose execution includes the call to `copy()`
* `L` is the expression `dest[i]`in `copy()  
   &L == dest+i` which is based on `a`, because `dest` gets its value from `a` upon entry to `copy()` \<-- Key point
* `X` is the object designated by `dest[i]` (which is `a[i]`)
* `X` is modified during the execution of `main`

The requirements in the specification are then:

* `T` is not const-qualified.  
   This is true.
* Every other lvalue used to access the value of `X` ...  
   Vacuously true, because there are no such other lvalues.
* Every access that modifies `X` shall be considered also to modify `P`, for the purposes of this subclause.  
   Vacuous, because `P` itself (which is the pointer object `a`) is not designated by means of another restrict-qualified pointer.
* If `P` is assigned the value of a pointer expression `E` that is based on another restricted pointer object `P2`, ...  
   Vacuously true, because there are no such assignments.

Contrary to what is implied in the question, an lvalue can have its address
based on more than one restricted pointer, provided each is associated with a
different (activation of a) block. In the example, the address of lvalue
`dest[i]` in `copy()` is based not only on `dest` but also on `a` (because
`dest` receives the value of `a` when the call is made).

\[Note that there would be undefined behavior if there were also a reference to
`a[i]` within the body of `copy()`, because the address of that lvalue would not
be based on `dest`.]

**Question 2\)**

This is necessary for the effectiveness of the `restrict` qualifier for multiple
levels of indirection. Consider the example:

```c
 void reverse(char * restrict * restrict dest,
               char * restrict * restrict source)
  {
   int i,j;
   for (i = 0; i < 10; i++)
     for (j = 0; j < 10; j++)
      dest[i][j] = source[i][9-j];
  }
```

Although the objects `dest[i][j]` are modified by the assignment statements, the
pointer objects `dest[i]` are not. Without the clause quoted above, the
top-level `restrict` qualifiers in the declarations of `dest` would have no
effect, and a call of the form `reverse(x,x)` would have defined behavior if the
elements of `x` point to 10 disjoint arrays of 10 chars. With the clause, the
top-level qualifiers have the same effect as if those pointer objects were
modified, so the iterated assignments are asserted to be fully free of aliasing
for the modified objects, and a call of the form `reverse(x,x)` does have
undefined behavior.

**Question 3\)**

This is necessary to allow a translator to assume that two restricted pointers
declared in the same scope cannot be used to alias the same object. Consider an
extreme example for file scope pointers:

```c
   char * restrict p;
    char * restrict q;

    void foo () { p = q; q = p; }
```

After the assignments in a call to `foo()`, each of the two pointers is based on
the other. Without the rules quoted above, this would be allowed and would
effectively enable aliasing despite the qualifiers. This possibility would, in
turn, generally undermine the benefit of the `restrict` qualifier, because a
translator would have to prove that there were no such assignments before taking
advantage of `restrict` qualifiers.

\[The assignments that are allowed are necessary to allow pointer values based
on restricted pointers to be used in argument and return expressions.]
