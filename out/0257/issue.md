### Problem

6.5.2.3#5 reads:

> \[#5] One special guarantee is made in order to simplify the use of unions: if a
> union contains several structures that share a common initial sequence (see
> below), and if the union object currently contains one of these structures, it
> is permitted to inspect the common initial part of any of them anywhere that a
> declaration of the complete type of the union is visible. Two structures share a
> common initial sequence if corresponding members have compatible types (and, for
> bit-fields, the same widths) for a sequence of one or more initial members.

Two possible reasons have been suggested for this rule.

1. The implementation may put padding between structure members. This rule is necessary to ensure that the common initial sequence uses the same padding in both places, so that the corresponding members occupy the same location.
2. If we consider part of the second example in 6.5.2.3#8:
   ```c
      struct t1 { int m; };
       struct t2 { int m; };
       int f(struct t1 * p1, struct t2 * p2)
       {
           if (p1->m < 0)
               p2->m = -p2->m;
           return p1->m;
       }
   ```
   the rule is necessary for an implementation to realize that `p1` and `p2` might refer the same location.

If (1) is the reason, then the example is a bad one because the two members are
both at the start of their respective structures, and therefore are required to
be at an offset of 0 from the start of the structure (and therefore of the
union). It should be changed to use a member further along a common initial
sequence.

On the other hand, the requirement is not actually very suitable. Consider the
code:

```c
   struct t1 { int x; double y; char z; } s1;
    struct t2 { int i; double q; unsigned long u; } s2;
    void f1 (struct t1 *p) { p->y = sqrt ((double) p->x); }
    void f2 (struct t2 *p) { p->q = sqrt ((double) p->i); }

    union { struct t1 t1; struct t2 t2; } u;
    // Followed by code using the common initial sequence property
```

The implementation might wish to use different padding in structures `t1` and
`t2`. It is prevented from doing so by the existence of the union, but a
one-pass compilation will not become aware of this until after compiling `f1`
and `f2`. Therefore it will have to assume, when deciding the layout of the
structures, that there might be a union. Therefore the rule about a union type
being visible is useless.

If, on the other hand, (2) is the reason, then the wording does not address
enough cases. For example, consider a version of the example in 6.5.2.3#8 where
one member is signed and the other is unsigned.

```c
   struct t1 { signed   int m; };
    struct t2 { unsigned int m; };
    int f(struct t1 * p1, struct t2 * p2)
    {
        if (p1->m > 0)
            p2->m = p2->m * 2;
        return p1->m;
    }
```

There is no common initial sequence but nevertheless many of the same issues
apply. On the other hand, the correct way for a function such as `f` to protect
itself against such aliasing is not to rely on the rule in 6.5.2.3#8, but rather
to use the `restrict` qualifier.

I would suggest, therefore, that (2) is not a valid reason for the rule. As
stated above, a corollary of this discussion is that the "union type must be
visible" rule is useless.

Finally, one of the changes from C90 to C99 was to remove any restriction on
accessing one member of a union when the last store was to a different one. The
rationale was that the behaviour would then depend on the representations of the
values. Since this point is often misunderstood, it might well be worth making
it clear in the Standard.

### Suggested Technical Corrigendum

To address point (1), in 6.5.2.3#8, second example, change the two structures
to:

```c
           struct t1 { double d; int m; };
            struct t2 { double d; int m; };
```

To address the wider point about visibility, change the first part of 6.5.2.3#5
to read:

> \[#5] One special guarantee is made in order to simplify the use of unions: if
> several structure types share a common initial sequence (see below), then
> corresponding members are required to lie at the same offset from the start of
> the union. Therefore if a union contains two or more such structures, the common
> initial part may be inspected using any of them, no matter which one was used to
> store the value.

To address issues about "similar" types raised in point (2) above, change the
second part of #5 to read:

> Two structures share a common initial sequence if corresponding members have
> matching types for a sequence of one or more initial members. Two types, in
> turn, are matching if they are
> 
> * compatible types (and, for bit-fields, the same widths)
> * signed and unsigned versions of the same integer type
> * qualified or unqualified versions of matching types, or
> * pointers to matching types.

To address the issue about "type punning", attach a new footnote 78a to the
words "named member" in 6.5.2.3#3:

> 78a If the member used to access the contents of a union object is not the same
> as the member last used to store a value in the object, the appropriate part of
> the object representation of the value is reinterpreted as an object
> representation in the new type as described in 6.2.6 (a process sometimes called
> "type punning"). This might be a trap representation.

Note: all the above changes are independent of one another, depending on the
committee's view of the issues.
