## Issue 0260: indeterminate values and identical representations

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Cross-references: [0451](issue0451.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_260.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_260.htm)

### Problem

This is an intermingling of something that started out as two separate
questions:

1. if an object holds an indeterminate value, can that value change other than by an explicit action of the program ?
2. if two objects hold identical representations derived from different sources, can they be used exchangeably ?

However, after much discussion the UK C Panel decided that they were better
treated together. Both involve the concept of the "provenance" of a value.

Consider the code:

```c
 char *p;
    unsigned char cp [sizeof p];
    p = malloc (SOME_VALUE);
    // Assume the allocation succeeds
    // Other code omitted that does not alter p.  memcpy (cp, &p, sizeof p);
    (free)(p); // Point X
               // ...
               // Point Y  if (memcmp (cp, &p, sizeof p))
              // ...
```

After the call to `free` the value of `p` is indeterminate. Is the
implementation allowed, at this point (point X), to change this indeterminate
value (presumably through compiler magic) so that the `memcmp` function sees a
difference, or must the value remain constant ? Can it make the change later,
between points X and Y ?

It is suggested that this is implied by 6.2.4#2:

> An object \[...\] retains its last-stored value throughout its lifetime.

particularly if each byte of an object is also an object.

On the other hand, such a requirement would eliminate useful optimisation and
debugging opportunities. (As an example of an optimisation, if `p` has been
loaded into a register and then modified, it need not be written back to memory;
as an example of a debugging opportunity, `p` could be set to a null pointer or
to a detectable value).

\[Note that where an object contains padding, 6.2.6.1#6 and #7 allows the value
of padding bits and bytes to change whenever the object changes.\]

If an implementation *is* allowed to change the value of `p`, then consider the
code:

```c
 char *p, *q, *r;
    p = malloc (SOME_VALUE);
    // Assume the allocation succeeds  q = p;
    r = p + 1;
    // Other code omitted that does not alter p, q, or r  (free)(p);
    // Point Z
```

Can it change the value of q or r at point Z ? What about later ?

Now consider the code:

```c
 int *p, *q;
    p = malloc (sizeof (int)); assert (p != NULL);
    (free)(p);
    q = malloc (sizeof (int)); assert (q != NULL);
    if (memcmp (&p, &q, sizeof p) == 0)
    {
        // Assume this point is reached
        *p = 42;  // Line A
```

Is the assignment valid (because an assignment using `*q` would have been, and
the two variables hold identical values) ? Or is it invalid because the
last-stored value of `p` is now indeterminate (because of the `free`) ?

Similarly, consider the code:

```c
 int x, y;
    int *p, *q;
    p = &x + 1;
    q = &y;
    if (memcmp (&p, &q, sizeof p) == 0)
    {
        // Assume this point is reached     *q = 42; p [-1] = 42;   // Line B     *p = 42; q [-1] = 42;   // Line C
```

The assignments on line B are clearly valid, but what about those on line C ?
After all, `p` and `q` are identical, even in their hidden bits. What if we then
add:

```c
     int *r;
        remote_memcpy (&r, &p, sizeof p);   // See note      *r = 42;      // Line D      r [-1] = 42;  // Line E
```

(The function `remote_memcpy` is identical to `memcpy`, but it is done in
another translation unit so that the compiler cannot associate special semantics
with it.) Which, if either, of the assignments is allowed ?

Another example is the program:

```c
 static int *p;
    void f (int n)
    {
        int sum = 0;
        int *q = &n;
        if (memcmp (&p, &q, sizeof p) == 0)
            for (int i = 0; i < n; i++)
                sum += i, p [i] = 0;
        p = &n;
    }
    int main (void)
    {
        int x;
        p = &x;
        f (1);
        f (6);
        return 0;
    }
```

On the first call to `f` the test is false. Therefore `p` is set to point to
`n`. The value of `p` becomes indeterminate at the end of the call, but on most
implementations this will have no effect. On the second call the test is true.
Therefore the first time round the loop `p [0]`, which is `n`, will be set to 0
and the loop will terminate.

However, most implementations would reasonably assume that `n` is not changed by
anything in the loop and generate code accordingly. If the behaviour were
undefined for some reason, such an implementation would be conforming. But is it
strictly-conforming or is it undefined ?

Finally, note that we can generate a similar situation without giving the
compiler any clue in advance:

```c
 void f (int vec [], int n)
    {
        void *vp;
        int *p;
        printf ("%p or %p", (void *) vec, (void *) &n);    // Line Q      scanf ("%p", &vp); p = vp;
        for (int i = 0; i < n; i++)
            p [i] = 0;
    }
```

The user could ensure that `p` is set to either of the values printed. If a
debugger is used, it isn't even necessary to retain line Q to determine the
value to enter on `stdin`, and therefore the compiler has no warning that the
address of `n` is being taken.

**Resolution**

After much discussion, the UK C Panel came to a number of conclusions as to what
it would be desirable for the Standard to mean. These can be expressed as three
requirements.

1. The implementation is entitled to take account of the provenance of a pointer value when determining what actions are and are not defined. Thus the assignments on lines A and C involve undefined behaviour. Similarly line D would be undefined and line E valid, though in practice a compiler would probably assume that `p` could point anywhere.
2. Where a pointer value becomes indeterminate because the object pointed to has reached the end of its lifetime, all objects whose effective type is a pointer and that point to the same object acquire an indeterminate value. Thus `p` at point X, and `p`, `q`, and `r` at point Z, can all change their value.
3. At any time that the compiler can determine that an object contains an indeterminate value, even if the type of the object does not have trap representations, the object may change value arbitrarily. Thus `p` need not have the same values at lines X and Y. As soon as the object is given an explicit value, this behaviour stops.

### Suggested Technical Corrigendum

Change 3.17.2 to:

> \[#1\] *indeterminate value*  
> a value which, at any given moment, could be either an unspecified value or a
> trap representation.
>
> \[#2\] While an object holds an indeterminate value it is *indeterminate*.
> Successive reads from an object that is indeterminate might return different
> results. Storing a value in an object, other than an indeterminate value, means
> that the object is no longer indeterminate.

Change the last sentence of 6.2.4#2 from:

> The value of a pointer becomes indeterminate when the object it points to
> reaches the end of its lifetime.

to:

> When an object reaches the end of its lifetime, any object with an effective
> type that is a pointer type and that points to that object becomes
> indeterminate.

\[Various uses of the word "indeterminate" could be tidied up, but this is the
only one where the meaning needs to change.\]

Add a new paragraph to 6.5.3.2:

> \[#5\] The implementation is permitted to use the derivation of a pointer value
> in determining whether or not access through that pointer is undefined
> behaviour, even if the pointer compares equal to, or has the same representation
> as, a different pointer for which the access would be permitted. For example, if
> two objects with the same type have non-overlapping lifetimes and happened to
> occupy the same address, a pointer to one cannot be used to access the other.

\[The `*` operator seems a reasonable place to put this. However, it could
equally be elsewhere.\]

---

Comment from WG14 on 2004-09-28:

### Committee Discussion (for history only)

Result does not mean the same as value. This is undefined because 6.5.6#8 has a
'shall' in it. The bits have to stay the same. 6.4.2 applies.

A bit pattern \+ type does not imply a unique value. There can be more than one
bit pattern that represents the same value. C only requires that an object with
a determinate value retain that value during its lifetime unless a an explicit
action (assignment, increment, decrement or through such functions as `memcpy`
and `memmove`) change that value to another one or renders the value
indeterminate.

An indeterminate value may be represented by any bit pattern. The C Standard
lays down no requirement that two inspections of the bits representing a given
value will observe the same bit-pattern only that the observed pattern on each
occasion will be a valid representation of the value.

In addition the C Standard does not prohibit an implementation from tracking the
provenance of the bit-pattern representing a value. An indeterminate value
happening to have a bit pattern that is identical to a bit pattern representing
a determinate value is not sufficient to allow access to the indeterminate value
free from undefined behavior.

In reaching our response we noted that requiring immutable bit patterns for
indeterminate values would reduce optimization opportunities. For example, it
would require tracking of the actual bit-patterns of indeterminate values if the
memory containing them were paged out. That seems an unnecessary constraint on
optimizers with no compensatory benefit to programmers.

### Committee Response

Question 1:

> Values may have any bit-pattern that validly represents them and the
> implementation is free to move between alternate representations (for example,
> it may normalize pointers, floating-point representations etc.). In the case of
> an indeterminate value all bit-patterns are valid representations and the actual
> bit-pattern may change without direct action of the program.

Question 2:

> If two objects have identical bit-pattern representations and their types are
> the same they may still compare as unequal (for example if one object has an
> indeterminate value) and if one is an indeterminate value attempting to read
> such an object invokes undefined behavior. Implementations are permitted to
> track the origins of a bit-pattern and treat those representing an indeterminate
> value as distinct from those representing a determined value. They may also
> treat pointers based on different origins as distinct even though they are
> bitwise identical.

Note that using assignment or bitwise copying via `memcpy` or `memmove` of a
determinate value makes the destination acquire the same determinate value.
