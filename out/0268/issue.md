### Problem

Consider the code:

```c
int x = 0;
    goto centre;
    while (++x < 10)
    {
        // Some code centre:
        // More code }
```

"Everyone knows" that, when the end of the block is reached, the loop test is
evaluated in the normal way. Nevertheless, I can find nothing in the Standard
that says so (it is implied by the example in 6.8.6.1#3, but that is all). Note
that in:

```c
int x;
    // ... if (condition) { x = -1; goto true_case; }
    // ... if (x > 0)
      true_case:
        do_something ();
    else
        do_something_else ();
```

the `else` case is not executed after a jump to `true_case`, even though the
condition `x > 0` is false. Therefore it is not possible to argue from analogy;
note also that this latter case is spelled out in the Standard. Since this
technique is well-known, it ought to be well-defined.

### Suggested Technical Corrigendum

Add a new paragraph after 6.8.5#4:

> \[#4a] If the loop body is reached by a jump from outside the iteration
> statement, the behavior is as if the body were entered in the normal way. That
> is, when the end of the body is reached the controlling expression is evaluated
> (and, in the case of a `for` statement, *expr-3* is evaluated first) and the
> body re-executed if it is not 0\. Similarly, a `break` or `continue` statement
> has the appropriate effect. However, the code jumped over \- including the
> controlling expressions in the case of a `while` or `for` statement \- is not
> evaluated when the jump happens.

Possibly also add an example either as 6.8.5#6 or 6.8.6.1#5 (with appropriate
editorial changes):

> \[#6] EXAMPLE: A jump into a `for` statement does not execute *clause-1* at all
> or *expr-2* during the jump:
>
> ```c
>   int i = 5;
>         if (condition) goto body;
>         for (i = 0; i < 10; i++)
>         {
>             if (i > 2) i++;
>         body:
>             printf (" %d", i);
>         }
>         printf ("\n");
> ```
>
> If `condition` is true, this prints:
>
> ```c
>   5 7 9
> ```
>
> while if it is false it prints:
>
> ```c
>   0 1 2 4 6 8 10
> ```
