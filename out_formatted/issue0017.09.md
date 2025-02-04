## Issue 0017.09: What is the type of an assignment expression?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Syntax of assignment expression

In subclause 6.3.16.1 on page 53, lines 31-32 there is a typo: “... of the
assignment expression ...” should be “... of the unary expression ...”

In subclause 6.3.16 on page 53, lines 3-5 we have

```c
assignment-expression:
    ...
         unary-expression  assignment-operator  assignment-expression
```

Now the string “*`assignment-expression`*” occurs twice.

The use of “assignment expression” in subclause 6.3.16 on page 53, line 12
refers to the first occurrence (the one to the left of the colon).

We suggest changing the use of “assignment expression” in subclause 6.3.16.1 on
page 53, line 32 in order to prevent confusion. The fact that any qualifier is
kept actually makes more sense, since this qualifier has to take part in any
constraint checking.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.3.16.1, page 54, another Example:***

In the fragment:

```c
   char c;
    int i;
    long l;

    l = ( c = i );
```

the value of `i` is converted to the type of the assignment-expression `c = i`,
that is, `char` type. The value of the expression enclosed in parenthesis is
then converted to the type of the outer assignment-expression, that is, `long`
type.
