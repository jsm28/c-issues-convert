## Issue 0040.07: Can `sizeof` be applied to earlier parameter names in a prototype, or to earlier fields in a struct?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

`sizeof` various identifiers (subclause 7.1.6)

a)

```c
void f(int c, char a[sizeof(c)]);
```

b)

```c
int i;
 struct {
 int i;
 char a[sizeof(i)];
 };
```

Now the argument to `sizeof` must be an expression or a type.

In (a) is `c` an expression? I think not because:

expression -\> object -\> has storage in execution environment

and `c` does not have storage allocated to it. So (a) violates a semantic
“shall” and is undefined behavior.

Now in (b) the field `i` is obviously not an expression. But is it visible? Like
the outer `i`, it has file scope. However, it is in a different namespace. There
are no rules for namespace resolution in the `sizeof` subclause.

So is (b) legal or undefined behavior?

---

Comment from WG14 on 1997-09-23:

### Response

a. Example:

```c
void f(int c, char a[sizeof(c)]);
```

The reference to `c` is an expression because the previously declared identifier
designates a function parameter (cf. subclause 6.5.4.3), which is an object
(subclause 3.15), thus meeting the requirement in subclause 6.3.1.

b. Another example:

```c
int i;
 struct {
 int i;
 char a[sizeof(i)];
 };
```

In C, this is okay. Subclause 6.1.2.3, **Name spaces of identifiers**, requires
that `i` in the `sizeof` expression refers to the external `i`, not the member.
