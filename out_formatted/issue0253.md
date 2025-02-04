## Issue 0253: "overriding" in designated initializers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Cross-references: [0413](issue0413.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_253.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_253.htm)

### Problem

Consider the code:

```c
   struct fred
    {
        char s [6];
        int n;
    };
    struct fred x [] = { { { "abc" }, 1 }, [0].s[0] = 'q'        };
    struct fred y [] = { { { "abc" }, 1 }, [0] = { .s[0] = 'q' } };
```

Both `x` and `y` will contain one element of type `struct fred`, which will be
initialized by the initializer `{ { "abc" }, 1 }` and then modified in some way.
The question is exactly how it is modified.

6.7.8#19 reads:

> \[#19] The initialization shall occur in initializer list order, each
> initializer provided for a particular subobject overriding any previously listed
> initializer for the same subobject; all subobjects that are not initialized
> explicitly shall be initialized implicitly the same as objects that have static
> storage duration.

In the case of `x`, it is fairly clear that the first initializer sets:

```c
   x [0].s [0] = 'a'
    x [0].s [1] = 'b'
    x [0].s [2] = 'c'
    x [0].s [3] = '\0'
    x [0].n     = 1
```

and the second one sets:

```c
   x [0].s [0] = 'q'
```

Finally, the remaining subobjects are initialized implicitly:

```c
   x [0].s [4] = 0
    x [0].s [5] = 0
```

Now consider the second initializer for `y`. One point of view says that this
behaves the same as for `x`: it specifies a value for `y [0].s [0]`, after which
the two remaining elements of `y [0].s` are still uninitialized and so are set
to zero. The other point of view says that this sets:

```c
   y [0] = (struct fred) { .s[0] = 'q' }
```

and that the rule concerning "all subobjects that are not initialized
explicitly" applies recursively. If so, the effect is to set:

```c
   x [0].s [0] = 'q'
    x [0].s [1] = 0
    x [0].s [2] = 0
    x [0].s [3] = 0
    x [0].s [4] = 0
    x [0].s [5] = 0
    x [0].n     = 0
```

Which of these is correct ?

### Suggested Technical Corrigendum 1

If `x` and `y` are supposed to have the same effect, change 6.7.8#19 to:

> \[#19] The initialization shall occur in initializer list order, each
> initializer provided for a particular subobject overriding any previously listed
> initializer for the same subobject. When all initializers have been applied, any
> subobjects of the overall object being initialized that have not been
> initialized explicitly shall be initialized implicitly the same as objects that
> have static storage duration.

and add a new paragraph at the end:

> \[#39] To illustrate the rules for implicit initialization, in:
>
> ```c
>        struct fred
>         {
>             char s [6];
>             int n;
>         };
>         struct fred x [] = { { { "abc" }, 1 }, [0].s[0] = 'q'        };
>         struct fred y [] = { { { "abc" }, 1 }, [0] = { .s[0] = 'q' } };
> ```
>
> the definitions of `x` and `y` result in identical objects. Each will be an
> array with one element; within that element, the members `s[4]` and `s[5]` are
> implicitly initialized to zero.

### Suggested Technical Corrigendum 2

If `x` and `y` are supposed to be different, change 6.7.8#19 to:

> \[#19] The initialization shall occur in initializer list order, each
> initializer provided for a particular subobject overriding any previously listed
> initializer for the same subobject; for each brace-enclosed list, all subobjects
> within the object that that list initializes that are not initialized explicitly
> shall be initialized implicitly the same as objects that have static storage
> duration.

and add a new paragraph at the end:

> \[#39] To illustrate the rules for implicit initialization, in:
>
> ```c
>        struct fred
>         {
>             char s [6];
>             int n;
>         };
>         struct fred x [] = { { { "abc" }, 1 }, [0] = { .s[0] = 'q' } };
>         struct fred y [] = { { .s[0] = 'q' } };
> ```
>
> the definitions of `x` and `y` result in identical objects. Each will be an
> array with one element; within that element, all the members are implicitly
> initialized to zero except for `s[0]`. In the definition of `x` the first
> initializer has no effect, since the second one initializes the same subobject
> (`x[0]`).

---

Comment from WG14 on 2002-05-15:

### Committee Response

Given the example

```c
   struct fred
    {
        char s [6];
        int n;
    };
    struct fred y [] = { { { "abc" }, 1 }, [0] = { .s[0] = 'q' } };
```

6.7.8#21 makes it clear already that `{ .s[0] = 'q' }` initializes a whole
object of type "struct fred" whose members (other than `s[0]`) are initialized
as though they were static storage, so this initialization of `y[0]` overrides
the previous one. Thus, all subobjects of `y[0]` other than `s[0]` are zeroed.
Paragraph #21 of 6.7.8 also makes it clear that the initializations for `x` and
`y` are different.

### Committee Discussion

The tem "designated initializer" is never mentioned in the Standard though it
appears in the index and new features section (the Standard uses the term
"designation initializer" in the text).
