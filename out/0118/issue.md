ANSI/ISO C Defect Report #rfg25:

Subject: Completion point for enumerated types.

Are diagnostics required for the following code examples?

```c
enum E1 { enumerator1 = sizeof (enum E1) };
 enum E2 { enumerator2 = sizeof (enum E2 *) };
```

(Just read on! This *isn't* just the same old question again!)

Background:

Subclause 6.3.3.4 (**Constraints**):

> The `sizeof` operator shall not be applied to an expression that has function
> type or an incomplete type, to the parenthesized name of such a type, ...

Subclause 6.5.2.1 (**Semantics**):

> The \[structure or union] type is incomplete until after the `}` that terminates
> the list \[of member declarations].”

(Bracketed portions added for clarity.)

CIB #1, RFI #13, response to question #5:

> For the example:
> 
> > ```c
> > enum e { a = sizeof(enum e) };
> > ```
> 
> the relevant citations are subclause 6.1.2.1 starting on page 21, line 39,
> indicating that the scope of the first `e` begins at the `{`, and subclause
> 6.5.2.2, page 62, line 20, which attributes meaning to a later `enum e` *only
> if* this use appears in a *subsequent* declaration. By subsequent, we mean
> “after the `}`.” Because in this case, the second `enum e` is not in a
> subsequent declaration, and no other wording in the C Standard addresses the
> meaning, the C Standard has left this example in the category of undefined
> behavior.

Please note that the above response to RFI #13, question #5 has totally failed
to solve the *real* problem with the current wording of the C Standard.

The *real* problem is that (unlike the case for structure and union type
definitions) nothing in the C Standard presently indicates where (or whether) an
enumerated type becomes “completed.”

This is a very serious flaw in the current C Standard. Given that the C Standard
currently contains no statement(s) which specify where (or whether) an
enumerated type becomes a “completed” type, any and all programs which use *any*
enumerated type in *any* context requiring a completed type are, by definition,
*not* strictly conforming. (This will come as quite a shock to a number of C
programmers!)

I feel that the Committee must resolve this serious problem as soon as possible.
The only plausible way to do that is to add a statement to subclause 6.5.2.2
which will specify the point at which an enum type become a “completed” type.

Using the statement currently given in subclause 6.5.2.1 (relating to struct and
union types) as a guide, it would appear that subclause 6.5.2.2 should be
amended to include the following new semantic rule:

> The enum type is incomplete until after the `}` that terminates the list of
> enumerators.

Some such addition is obviously necessary in order to render enum types usable
as complete types within strictly conforming programs.

Note however that such a clarification would have the additional (beneficial?)
side effect of rendering the following declaration subject to a mandatory
diagnostic (due to the violation of the constraints for the operand of the
`sizeof` operator):

```c
enum E1 { enumerator1 = sizeof (enum E1) };
```

Even after such a clarification however, the status of:

```c
enum E2 { enumerator2 = sizeof (enum E2 *) };
```

is still questionable at best, and the proper interpretation for such a case
should, I believe, still be drawn from the response given to [RFI #13, question
#5](issue:0013.05); i.e., such examples should be viewed as involving undefined
behavior.
