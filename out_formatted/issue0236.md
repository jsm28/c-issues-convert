## Issue 0236: The interpretation of type based aliasing rule when applied to union objects or allocated objects

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: NCITS J11, Raymond Mak  
Date: 2000-10-18  
Submitted against: C99  
Status: Closed  
Cross-references: [0257](issue0257.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_236.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_236.htm)

**Question**

> This concerns 6.5 paragraph 6 and 7\. Consider the following two pieces of code
> :
>
> ```c
> Example 1
> #define N ? // optimization opportunities if "qi" does not alias "qd"
>    void f(int *qi, double *qd) {
>         int i = *qi + 2;
>         *qd = 3.1;       // hoist this assignment to top of function???
>      *qd *= i;
>      return;
>    }
>    main() {
>       void *vp;
>       int *pi;
>       double *pd;
>       vp = malloc(N);
>       pi = vp;
>       *pi = 7;    // assignment to allocated space thru "p"
>       pd = vp;    // "pi" and "pd" are aliases
>       f(pi, pd);
>       free(vp);
>     }
> Example 2
> // optimization opportunities if "qi" does not alias "qd"
>     void f(int *qi, double *qd) {
>       int i = *qi + 2;
>       *qd = 3.1;       // hoist this assignment to top of function???
>       *qd *= i;
>       return;
>    }
>    main() {
>      union tag {
>        int mi;
>        double md;
>      } u;
>      u.mi = 7;
>      f(&u.mi, &u.md);
>    }
> ```
>
> The two pieces of code are basically the same except that one uses an union
> object and the other an allocated object. The question is whether these are
> conforming programs.
>
> At issue here is the pointers within the function `f`. (This function can be in
> translation unit of its own and have no knowledge about the union or the
> allocated object.)
>
> The spirit of the type-based aliasing rule is to help the optimizer to compute
> aliasing relationship without knowledge about the rest of the program. In this
> particular case, the type-based aliasing rule is meant to allow the optimizer to
> hoist the assignment `*qd = 3.1` to the top of the function. But this
> transformation changes the computation.
>
> 6.5 paragraph 6 allows example 1\. It is not clear if 6.5 paragraph 7 allows
> example 2\. The spirit of type-based aliasing rule is violated.
>
> **Discussion:**
>
> In the second code example above.
>
> Note that 6.5 paragraph 7 states:
>
> > "an aggregate or union type that includes one of the aforementioned types among
> > its members (including, recursively, a member of a subaggregate or contained
> > union)."
>
> Arguably this can be read such that the access through `u.mi` in the above
> causes `u.md` to become undefined. If it were the case that `u.mi` was the
> *active* union member then the assignment:
>
> > ```c
> > *qd = 3.1;
> > ```
>
> is an error since the the store is done using an lvalue of type `double` and the
> *active* member has type `int`. However, an expression such as:
>
> > ```c
> > u.md = 3.14;
> > ```
>
> is legitimate because the union object is used to modify one of it's members and
> (in this case) changes the *active* member.
>
> Similarly:
>
> > ```c
> > pu->md = 1.1;
> > ```
>
> changes the *active* member.
>
> Turning to the first code example above.
>
> Here again the *active* effective type of the allocated space starts out as type
> `int` and the desired semantics are that the assignment:
>
> > ```c
> > *qd = 3.1;
> > ```
>
> is an error because the expression `*qd` has type `double`.
>
> The `char` type should have special privileges. Programs should be able to erase
> the active effective type via:
>
> > ```c
> > memset(vp, 0, sizeof(int));
> > memset(&u, 0, sizeof(union tag));
> > ```
>
> or possible change the active effective type via:
>
> > ```c
> > memcpy(&u, &u2, sizeof(union tag)};
> > ```
>
> or even:
>
> > ```c
> > char *p1 = (char *) &u;
> > char *p2 = (char *) &u2;
> > for (int i = 0; i < sizeof(union tag); i++) {
> >    p1[i] = p2[i];
> > }
> > ```
>
> That is, the `char` types have special alias privileges that let them scribble
> on an object that already has an effective type.
>
> **Suggested change:**
>
> (We offer the following as a starting point for further discussion.)
>
> To tackle the first code example, change 6.5 paragraph 6, second sentence,
>
> From:
>
> > If a value is stored into an object having no declared type through an lvalue
> > having a type that is not a character type, then the type of the lvalue becomes
> > the effective type of the object for that access and for subsequent accesses
> > that do not modify the stored value.
>
> to:
>
> > If a value is stored into an object having no declared type through an lvalue
> > having a type that is not a character type, then the type of the lvalue becomes
> > the effective type of the object for that access and for subsequent accesses.
>
> That is, the last phrase "that do not modify the stored value" is removed.
>
> To tackle the second code example, use the concept of the effective type of an
> union object (i.e. use it to track the active member). Either describe it in the
> rationale, or formally introduce it in the standard.
>
> Effective type of an union object.
>
> > The type of the last member accessed within an union object is the effective
> > type of the union object. For members with types not compatible with the
> > effective type of the union object, the lvalue used for the store shall be the
> > result of member selection from the union.
>
> Note that this forces the union declaration to be visible in the translation
> unit.
>
> If we add this to the standard, add it immediately before 6.5p7.

---

Comment from WG14 on 2006-05-08:

### Committee Discussion

Committee believes that Example 2 violates the aliasing rules in 6.5 paragraph
7:

> "an aggregate or union type that includes one of the aforementioned types among
> its members (including, recursively, a member of a subaggregate or contained
> union)."

In order to not violate the rules, function f in example should be written as:

```c
   union tag {
                int mi;
                double md;
        } u;
        void f(int *qi, double *qd) {
                int i = *qi + 2;
                u.md = 3.1;   // union type must be used when changing effective type
                *qd *= i;
        return;
        }
```

Example 1 is still open. The committee does not think that the suggested wording
is acceptable.

More discussion is found in reflector message #9337, and in the Curacao meeting
minutes [N973](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n973.txt) and in
the Santa Cruz meeting minutes
[N987](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n987.txt).  
The current situation requires more consideration, but general consensus seems
to be;

* Limit the use of pointers to union members,
* Consensus for the visible alias rule exists,
* The requirement of global knowledge is problematic,
* Common understanding is that the union declaration must be visible in the translation unit.

### Committee Response

Both programs invoke undefined behavior, by calling function `f` with pointers
`qi` and `qd` that have different types but designate the same region of
storage. The translator has every right to rearrange accesses to `*qi` and `*qd`
by the usual aliasing rules.
