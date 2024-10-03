ANSI/ISO C Defect report #rfg20:

Subject: Return expressions in functions declared to return qualified `void`.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
volatile void func0 (volatile void *vvp)
        {
 	return *vvp;	/* ? */
        }

 const void func1 (const void *cvp)
        {
 	return *cvp;	/* ? */
        }
```

Background:

Subclause 6.6.6.4 (**Constraints**):

> A `return` statement with an expression shall not appear in a function whose
> return type is `void`.

Note that this constraint doesn't say anything about functions declared to
return some qualified version of the `void` type.

I believe that it was probably the Committee's true intent to require a
diagnostic for any attempt to specify an expression in a return statement within
any function declared to return *any* qualified or unqualified version of the
`void` type (and indeed, many existing implementations do already issue
diagnostics for usage such as that shown in the example above). Thus, it would
seem appropriate for the Committee to amend the above quoted constraint (from
subclause 6.6.6.4) to read:

> A `return` statement with an expression shall not appear in a function whose
> return type is a void type.
