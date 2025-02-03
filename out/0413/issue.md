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
