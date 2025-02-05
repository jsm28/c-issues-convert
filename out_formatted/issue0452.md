## Issue 0452: Effective Type in Loop Invariant

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Shao Miller  
Date: 2013-09-29  
Reference document: [N1762](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1762.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The definition for "effective type" does not appear to apply to non-lvalue
expressions. This can cause a behavioural difference, in loops.

6.5p6:

> The effective type of an object for an access to its stored value is the
> declared type of the object, if any.87) If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue becomes the effective type of the object for
> that access and for subsequent accesses that do not modify the stored value. If
> a value is copied into an object having no declared type using memcpy or
> memmove, or is copied as an array of character type, then the effective type of
> the modified object for that access and for subsequent accesses that do not
> modify the value is the effective type of the object from which the value is
> copied, if it has one. For all other accesses to an object having no declared
> type, the effective type of the object is simply the type of the lvalue used for
> the access.

Given the following code:

> union u1 {  
> int x;  
> long y;  
> };  
>
> int func1(void) {  
> union u1 o1 \= { 42 };  
>
> return (0, o1).x;  
> }

The `o1` sub-expression in the `return` statement's expression accesses the
stored union value of the object. The comma operator's result has that value,
but it is not an lvalue and so "effective type" does not appear to apply. While
the access to `o1` involves an access to a stored value, the membership operator
can be said to access an object whose value is available, but perhaps not
exactly "stored." `o1.x` is an lvalue, but `(0, o1).x` is not.

6.5.2.3p3:

> A postfix expression followed by the . operator and an identifier designates a
> member of a structure or union object. The value is that of the named member,95)
> and is an lvalue if the first expression is an lvalue. If the first expression
> has qualified type, the result has the so-qualified version of the type of the
> designated member.

6.5p7:

> An object shall have its stored value accessed only by an lvalue expression that
> has one of the following types:88)
>
> * a type compatible with the effective type of the object,
> * a qualified version of a type compatible with the effective type of the object,
> * a type that is the signed or unsigned type corresponding to the effective type of the object,
> * a type that is the signed or unsigned type corresponding to a qualified version of the effective type of the object,
> * an aggregate or union type that includes one of the aforementioned types among its members (including, recursively, a member of a subaggregate or contained union), or
> * a character type.

Given:

> union u2 {  
> int x;  
> long y;  
> char ca\[2\];  
> };  
>
> int func2(void) {  
> union u2 o2 \= { 42 };  
>
> return (0, o2).x;  
> }

We have a similar situation, even though `(0, o2)` yields an object with
temporary lifetime. (Side question: Should the expression `(0, o2).ca == o2.ca`
yield zero, non-zero, or should it be implementation-defined?)

Suppose we have a portable strategy to determine whether or not the object
representations of `int` and `long` are the same. If they are and if we have the
following code:

> union u3 {  
> int x;  
> long y;  
> };  
>
> long func3(void) {  
> union u3 o3;  
>
> o3.x \= 42;  
> return (0, o3).y;  
> }

Are we violating the effective type rules? We might expect type-punning to be
relevant here and the membership operator to be accessing a member value of a
union value.

If the answer is yes, then does the Standard define the effective type of the
non-lvalue expression `0, o3` ?

If the answer is no, then this can cause the loss of an optimization opportunity
in the following code:

> struct s4 {  
> int x;  
> float f;  
> };  
>
> void func4(long \* lp, struct s4 \* s4p) {  
> int c;  
>
> for (c \= 0; c \< (0, \*s4p).i; \+\+c)  
> --\*lp;  
> }

We do not expect `*lp` to alias into `*s4p`, so we might optimize this loop such
that `(0, *s4p).i` is only computed once. If, in another translation unit, it
turned out that these did alias, the optimization would normally be justified
based on a violation of the effective type rules. If there isn't a violation
because of the non-lvalue nature of the comma operator's expression, then the
optimization would not appear to be justified.

### Suggested Technical Corrigendum

None.

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

> The committee did not have adequate time to consider these issues and intends
> that these issues be further refined through consultation with the author.

Apr 2014 meeting

### Committee Discussion

> Further input was not received from the author and will again be solicited.

Oct 2014 meeting

### Committee Discussion

> Discussion with the author clarified these issues, and the paper
> [N1888](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1888.htm) was
> discussed. From that, we extract the following example
>
> > ```c
> > union u2 {
> >     int x;
> >     long y;
> >     char ca[2];
> > };
> >
> > int func2(void) {
> >     union u2 o2 = { .ca = "a" };
> > ```
>
> and question, what is the result of `(0,o2).ca == o2.ca`?
>
> Given that the comma operator doesn't yield an lvalue (6.5.17), and from 6.2.4p8
> such a non-lvalue expression is stated to have automatic storage duration, this
> seems to require that the answer is false, even though this defeats compiler
> optimizations.
>
> The effective type rule 6.5.p6 also does not seem to apply to objects with
> temporary lifetime, and has undesirable consequences.
>
> The direction the committee would like to go is something like:
>
> In 6.2.4p8, append
>
> > An object with temporary lifetime behaves as if it had the declared type of its
> > value. Such an object is known as a *temporary object*. A temporary object need
> > not have a unique address.
>
> Apr 2015 meeting
>
> ### Committee Discussion
>
> > The following words were drafted and approved by the committee as the Proposed
> > Technical Corrigendum.
>
> ### Proposed Committee Response
>
> > To the question "Should the expression `(O, o2).ca == o2.ca` yield zero,
> > non-zero, or should it be implementation defined?" the answer is "implementation
> > defined".
> >
> > With the following changes, the effective type of `O, o3` is defined.
>
> ### Proposed Technical Corrigendum
>
> In 6.2.4p8, append
>
> > An object with temporary lifetime behaves as if it were declared with the type
> > of its value for the purposes of effective type. Such an object need not have a
> > unique address.
> >
> > (add forward reference to 6.5p6 to this section)
