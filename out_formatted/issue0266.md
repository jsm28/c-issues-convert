## Issue 0266: overflow of `sizeof`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_266.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_266.htm)

### Problem

Consider the following code:

```c
  char x [SIZE_MAX / 2][SIZE_MAX / 2];
    size_t s = sizeof x;
```

The size of `x` cannot be fitted into an object of type `size_t`. Assuming that
`SIZE_MAX` is 65535, what is the value of `s` ? More generally, which of the
following is, or should be, the case ?

1. The value is reduced modulo `(SIZE_MAX + 1)`.
2. The behaviour is undefined (or perhaps implementation-defined).
3. The program is forbidden to use `sizeof` with such a large argument.
4. The implementation must ensure that no object can be larger than `SIZE_MAX` bytes.

6.5.3.4#2 says in part:

> \[#2\] The `sizeof` operator yields the size (in bytes) of its operand, which
> may be an expression or the parenthesized name of a type. The size is determined
> from the type of the operand. The result is an integer.

Note that there is no indication that the result may be other than the correct
size.

### Suggested Technical Corrigendum

One of:

1. Append to 6.5.3.4#4:
   > If the size is too large to fit in an object of type `size_t`, it is converted
   > to that type in the manner described in subclause 6.3.1.3.
2. Append to 6.5.3.4#4:
   > If the size is too large to fit in an object of type `size_t`, it is replaced by
   > an implementation-defined value.
3. Add a new constraint paragraph after 6.5.3.4#1:
   > \[#1a\] The `sizeof` operator shall not be applied to an operand whose size, in
   > bytes, is larger than the maximum value of the type `size_t`.
4. Append to 6.5.3.4#4:
   > The implementation shall ensure that the type `size_t` is large enough to hold
   > the result of all uses of the `sizeof` operator.

\[Some of these are less than wonderful, and consideration should also be given
to the interaction with VLAs.\]

---

Comment from WG14 on 2004-03-06:

### Committee Discussion

The committee has deliberated and decided that more than one interpretation is
reasonable. Translation limits do not apply to objects whose size is determined
at runtime.

> ```c
> sizeof(a[SIZE_MAX/2][SIZE_MAX/2]);
> ```

The program is not strictly conforming because it exceeds an environmental
limit.   
If the implementation generates code, there is no requirement for a diagnostic.
In the event that `sizeof` is called on the object, a diagnostic should be
issued, but not required.   
VLAs are a special case.

### Committee Response

The program is not strictly conforming because it exceeds an environmental
limit. If the implementation generates code, there is no requirement for a
diagnostic. In the event that `sizeof` is called on the object, a diagnostic can
be issued, but is not required.
