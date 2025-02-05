Enumeration tag anomaly

Consider the following (bizarre) example:

```c
enum strange1 {
         a = sizeof (enum strange1)      /* line [2] */
 };
 enum strange2 {
         b = sizeof (enum strange2 *)    /* line [5] */
 };
```

The respective tags are visible on lines \[2\] and \[5\] (according to subclause
6.1.2.1, page 20, lines 39-40, but there is no rule in subclause 6.5.2.3,
**Semantics** (page 62\) that governs their meaning on lines \[2\] and \[5\].
Footnote 62 on page 62 seems to be written without taking this case into
account.

The first declaration must be illegal. The second declaration should be illegal
for simplicity.

Perhaps these declarations are already illegal, since no rule gives them a
meaning. To clarify matters, I suggest in subclause 6.5.2.3 appending to page
62, line 35:

> A type specifier of the form
>
> ```c
> enum identifier
> ```
>
> shall not occur prior to the end of the `enumerator-list` that defines the
> content.

If this sentence is not appended, something like it should appear as a footnote.
