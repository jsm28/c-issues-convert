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
