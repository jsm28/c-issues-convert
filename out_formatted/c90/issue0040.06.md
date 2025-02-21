## Issue 0040.06: Can one use `offsetof(struct t1, mbr)` before `struct t1` is completely defined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Submitted against: C90  
Status: Closed  
Cross-references: [0097](../c90/issue0097.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

The definition of the `offsetof` macro in subclause 7.1.6 does not cover all its
possible occurrences:

a. There are no restrictions on the structure being a completed type.

```c
struct t1 {
 char c;
 short s;
 int i[offsetof(struct t1, s)];
 }
```

When discussing the use of incomplete types, recourse usually has to be made to
the rules relating to where an object of unknown size may appear.

Would the Committee agree that there are not any rules prohibiting the above
construction?

b. In this structure we are asked to find the offset of a field that has not yet
been encountered:

```c
struct t2 {
 char c;
 union {
 int i[offsetof(struct t2, s)];
 short s;
 } u;
 };
```

Would the Committee agree that there do not appear to be any rules that make
this construct illegal?

c. The following structure has infinitely many “solutions:”

```c
struct t3 {
 char a[offsetof(struct t3, i)];
 int i;
 }
```

since `char` has size 1, any size of array will be the same as the `offsetof`
the field `i`.

d. The following structure has no “solutions:”

```c
struct t4 {
 int a[offsetof(struct t3, i)];
 int i;
 }
```

`int` is always larger than 1\.

---

Comment from WG14 on 1997-09-23:

### Response

a. Example:

> ```c
> struct t1 {
>  char c;
>  short s;
>  int i[offsetof(struct t1, s)];
>  };
> ```

This is *not* a valid use of the `offsetof` macro. The hypothetical `static`
*`type`* `t;` declaration required for `offsetof` (cf. subclause 7.1.6) could
not have validly appeared prior to the invocation of `offsetof` because the type
`struct t1` is incomplete (cf. subclause 6.7.2); therefore the `offsetof`
invocation is not strictly conforming.

b. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.

c. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.

d. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.
