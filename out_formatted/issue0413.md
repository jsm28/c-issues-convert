## Issue 0413: initialization

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Willem Wakker  
Date: 2012-01-27  
Reference document: [N1601](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1601.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0253](issue0253.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Consider the following code:

> ```c
> typedef struct {
> int k;
> int l;
> int a[2];
> } T;
>
> typedef struct {
> int i;
> T t;
> } S;
>
> T x = {.l = 43, .k = 42, .a[1] = 19, .a[0] = 18 };
>
> void f(void)
> {
> S l = { 1, .t = x, .t.l = 41, .t.a[1] = 17};
> }
> ```

The question is: what is now the value of `l.t.k`? Is it 42 (due to the
initialization of `.t = x`) or is it 0 (due to the fact that `.t.l` starts an
incomplete initialization of `.t`?

The relevant clause from the standard is 6.7.9 clause 19:

> 19 The initialization shall occur in initializer list order, each initializer
> provided for a particular subobject overriding any previously listed initializer
> for the same subobject;<sup>151</sup>) all subobjects that are not initialized
> explicitly shall be initialized implicitly the same as objects that have static
> storage duration.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2014-10-31:

Feb 2012 Meeting

### Committee Discussion

> * It was noted that this is basically similar to [dr\_253](issue0253.md).
> * The following was proposed, but there was no consensus for adoption.
>   > The initialization shall occur in initializer list order, each initializer
>   > provided for a particular subobject overriding any previously listed initializer
>   > for the same subobject <sup>151\)</sup>. Subsequently, all subobjects that are
>   > not initialized explicitly previously shall be initialized implicitly the same
>   > as objects that have static storage duration.

Oct 2012 meeting

### Committee Discussion

> * The original author intended the result to be 42 by the following reasoning:
> * 6.7.9 paragraphs 17-18 specify that each designator list affects only the smallest subobject to which the designator list refers. As a result, the second clause of paragraph 19 occurs once for the greater object as a whole, filling in only those parts of the whole object that were never initialized explicitly.
> * **gcc** and some IBM compilers give the result as 0, although it is not believed that there is code dependent on this interpretation.
> * David Keaton proposed [N1659](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1659.pdf).
> * This, however, does not clarify the interpreted conflict of paragraph 19 "subobjects that are not initialized explicitly \[shall be set to zero]" applied "recursively to subaggregates" (paragraph 20).
> * Adding the example is a desired outcome.

Apr 2013 meeting

### Committee Discussion

> There was no work performed on this DR.
>
> Although both GCC and six compilers from IBM provide the unintended answer, it
> is believed to be such a rarely used feature that it is not depended upon to a
> great degree, and the compiler venders are willing to change their behavior
> appropriately.

Oct 2013 meeting

### Committee Discussion

> There has been considerable discussion and several proposals ( N1659, N1749) to
> clarify the standard to no avail. Upon reflection, and consultation with the
> author, we believe that the proper course of action is twofold. First, simply
> answer the question asked as the committee believes that the standard already
> specifies correctly. To add clarification to the standard we will also add the
> examples from N1659 that leads to this answer.

### Proposed Committee Response

The proper answer to the question raised according to the standard is that the
value of l.t.k is 42, because implicit initialization does not override explicit
initialization. We will also provide a non-normative example to further clarify
the intent.

### Proposed Technical Corrigendum

Add the following example to 6.7.9:

```c
    typedef struct {
        int k;
        int l;
        int a[2];
    } T;

    typedef struct {
        int i;
        T t;
    } S;

    T x = {.l = 43, .k = 42, .a[1] = 19, .a[0] = 18 };

    void f(void)
    {
        S l = { 1, .t = x, .t.l = 41, .t.a[1] = 17};
    }
```

The value of l.t.k is 42, because implicit initialization does not override
explicit initialization.
