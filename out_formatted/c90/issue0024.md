## Issue 0024: For `strtod`, what does `"C"` locale mean?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-004  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_024.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_024.html)

In subclause 7.10.1.4 **The `strtod` function** page 151, line 5: What does
“`"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) == "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) == "C"
```

c. `&&`

d.

```c
||
```

e. something else.

What does “other than the `"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) != "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) != "Ct
```

c.

```c
&&
```

d.

```c
||
```

e. something else.

Subclause 7.4.1 **Locale control**, page 107 may help answer the questions.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.4.1.1, page 107, lines 11-17 describe what is affected by each
locale portion.

Is it the `LC_NUMERIC` locale category which affects the implementation-defined
behavior of `strtod`, etc.?

Answer: Yes.

How can one guarantee that `strtod` functions are in the `"C"` locale?

Answer: Execute `setlocale(LC_NUMERIC, "C")` or execute `setlocale(LC_ALL, "C")`
.

What is meant by “other than the `"C"` locale?” That is, how can one ensure that
`strtod` is not in the `"C"` locale?

Answer: Successfully execute `setlocale(LC_NUMERIC, str)` or `setlocale(LC_ALL,
str)` to some implementation-defined string `str` which specifies a locale that
is different from the `"C"` locale. No universally portable method can be
provided, because the functionality is implementation-defined.
