## Issue 0017.18: Are `f()` and `f(void)` compatible?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of functions with `void` and no prototype

```c
f2(void);
 f2(); /* Is this function compatible with the one above? */
```

Now subclause 6.5.4.3, page 68, line 1 says that the first declaration of `f2`
specifies that the function has no parameters.

No rules are given in the subsequent paragraphs to say that a function
declaration with a parameter type list, with no parameters, is compatible with a
function declaration with an empty parameter list.

If we treat the `void` as a single parameter then page 68, lines 14-18 would
make the above two functions incompatible. `void` is not compatible with any
default promotions. subclause 6.5.4.3, page 68, lines 18-22 cover the case for
declaration and definition.

Thus I think that in the above example the behavior is implicitly undefined.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.5.4.3, page 67, line 37 and page 68, line 1 state, “The special case
of `void` as the only item in the list specifies that the function has no
parameters.” Therefore, in the case of `f2(void);` there are *no* parameters
just as there are none for `f2();`. Since both functions have the same return
type, these declarations *are* compatible.
