## Issue 0040.01: What is the composite type of `f(int)` and `f(const int)`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0013.01](../c90/issue0013.01.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Composite type

Rule for function parameter compatibility, subclause 6.7,1, page 82, lines
24-25:

```c
void f(const int);
 void f(int a)
 {
 a = 4;
 }
```

In the above case what is the composite type of `f`? The legality of the
assignment to `a` depends on the answer.

```c
int f(int a[4]);
 int f(int a[5]);
```

The parameters are compatible because they are converted to *pointer to* ...,
but what is the composite type?

---

Comment from WG14 on 1997-09-23:

### Response

```c
void f(const int);
 void f(int a)
 {
 a = 4;
 }
```

What is the composite type of `f`?

Answer: `void f(int)`. [Defect Report #013, Question 1](../c90/issue0013.01.md) describes
the correct manner for constructing the composite type.

Is the assignment valid?

Answer: Yes. The type of a parameter is independent of the composite type of the
function, so the assignment is valid (cf. subclause 6.7.1).

Another example:

```c
int f(int a[4]);
 int f(int a[5]);
```

The parameters are compatible because they are converted to *pointer to ...*,
but what is the composite type?

Answer: The response to the Defect Report mentioned above answers this question
as well.
