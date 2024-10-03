It has been suggested that, at least in the `"C"` locale, the transformed string
output from `strxfrm` will not contain more characters than the original string.
I believe that this suggestion is overly restrictive, and that the standard does
not impose such a restriction on implementations. I am requesting a
clarification from the appropriate standards committee(s). I hope that you will
agree with the following resolution:

> The C Standard does not impose a requirement upon the length of the transformed
> string output from `strxfrm`. (The returned value does indicate the necessary
> length.)

Here are some citations from the C Standard:

Subclause 7.4.1.1 **The `setlocale` function**:

> `LC_COLLATE` affects the behavior of the `strcoll` and `strxfrm` functions... A
> value of `"C"` for `locale` specifies the minimal environment for C
> translation... At program startup, the equivalent of

```c
setlocale(LC_ALL, "C");
```
> is executed.

Subclause 7.11.4.3 **The `strcoll` function**:

> The `strcoll` function compares the string pointed to by `s1` to the string
> pointed to by `s2`, both interpreted as appropriate to the `LC_COLLATE` category
> of the current locale.

Subclause 7.11.4.5 **The `strxfrm` function**:

> The transformation is such that if the `strcmp` function is applied to two
> transformed strings, it returns a value greater than, equal to, or less than
> zero, corresponding to the result of the `strcoll` function applied to the same
> two original strings... The `strxfrm` function returns the length of the
> transformed string (not including the terminating null character). If the value
> returned is `n` or more, the contents of the array pointed to by `s1` are
> indeterminate.

I haven't located any requirement that the `"C"` locale behavior of `strcoll`
must be identical to `strcmp`. Even if there were such a requirement, I haven't
located any requirement that the transformed string must not be longer than the
original string.
