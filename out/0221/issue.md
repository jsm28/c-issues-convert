### Summary

Consider the code extract:

> ```c
> int v [10]; int *p = (v + 9) + 1; int *q = v + 10;
> ```

The relevant part of 6.5.6 paragraph 8 reads:

> If the pointer operand points to an element of an array object, and the array is
> large enough, the result points to an element offset from the original element
> such that the difference of the subscripts of the resulting and original array
> elements equals the integer expression. In other words, if the expression `P`
> points to the *i*-th element of an array object, the expressions `(P)+N`
> (equivalently, `N+(P)`) and `(P)-N` (where `N` has the value n) point to,
> respectively, the *i*\+*n*-th and *i*\-*n*-th elements of the array object,
> provided they exist. Moreover, if the expression `P` points to the last element
> of an array object, the expression `(P)+1` points one past the last element of
> the array object, and if the expression `Q` points one past the last element of
> an array object, the expression `(Q)-1` points to the last element of the array
> object. If both the pointer operand and the result point to elements of the same
> array object, or one past the last element of the array object, the evaluation
> shall not produce an overflow; otherwise, the behavior is undefined.

There is a problem with this wording in that it defines arithmetic of pointers
within the array object properly, but it only defines arithmetic to "one past
the end" when the pointer was previously to the last object. In other words, the
initialization of `p` is correct because `(v + 9)` points to the last element of
an array, but the initialization of `q` is not because the "*i*\+*n*-th" element
does not exist.

This problem also makes common idioms like:

> ```c
> for (p = v; p < v + 10; p++)
> ```

undefined.

It is clear that these constructs are supposed to work, and that the relevant
wording just needs to be adjusted.

### Suggested Technical Corrigendum

Change the cited text to:

> If the pointer operand points to an element of an array object or to one past
> the last element of the array object, and if the array is large enough, the
> result points to an element, or to the location one past the last element,
> offset from the original element such that the difference of the subscripts of
> the resulting and original array elements equals the integer expression. In
> other words, if the expression `P` points to the *i*-th element of an array
> object with *k* elements, or to one past the last element (in which case *i*
> equals *k*), then the expressions `(P)+N` and `N+(P)`, (where `N` has the value
> *n* which may be positive, zero, or negative) both point to the *i*\+*n*-th
> elements of the array object, provided it exists, or if *i*\+*n* equals *k*, to
> one past the last element of the array object. If both the pointer operand and
> the result point to elements of the same array object, or one past the last
> element of the array object (that is, both *i* and *i*\+*n* lie between *0* and
> *k* inclusive), the evaluation shall not produce an overflow; otherwise, the
> behavior is undefined.

Similarly, change the following text in paragraph 9:

> In other words, if the expressions `P` and `Q` point to, respectively, the
> *i*-th and *j*\- th elements of an array object, the expression `(P)-(Q)` has
> the value *i*\-*j* provided the value fits in an object of type `ptrdiff_t`.
> Moreover, if the expression `P` points either to an element of an array object
> or one past the last element of an array object, and the expression `Q` points
> to the last element of the same array object, the expression `((Q)+1)-(P)` has
> the same value as `((Q)-(P))+1` and as `-((P)-((Q)+1))`, and has the value zero
> if the expression `P` points one past the last element of the array object, even
> though the expression `(Q)+1` does not point to an element of the array
> object.<sup>88\)</sup>

to:

> In other words, if the expressions `P` and `Q` point to, respectively, the
> *i*-th and *j*-th elements of an array object with *k* elements, or to one past
> the last element (in which case *i* or *j*, or both, equals *k*), the expression
> `(P)-(Q)` has the value *i*\-*j* provided the value fits in an object of type
> `ptrdiff_t`.<sup>88\)</sup>