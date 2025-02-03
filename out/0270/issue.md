### Problem

In the `fprintf` conversion specifier `"%lc"`, the corresponding argument is of
type `wint_t`, but is then treated as if it contained a `wchar_t` value. In
7.19.6.1#18, the last call is:

```c
  fprintf(stdout, "|%13lc|\n", wstr[5]);
```

This argument has the type `wchar_t`.

There is no requirement in the Standard that the default argument promotions
convert `wchar_t` to `wint_t`. Therefore this example exhibits undefined
behaviour on some implementations. Nonetheless, the code looks like it ought to
work, and WG14 should consider changing the definition of `wint_t` to force it.

The current definition of `wint_t` is in 7.24.1#2:

> ```c
> wint_t
> ```
>
> which is an integer type unchanged by default argument promotions that can hold
> any value corresponding to members of the extended character set, as well as at
> least one value that does not correspond to any member of the extended character
> set (see `WEOF` below);<sup>269\)</sup> and
>
> <sup>269</sup>`wchar_t` and `wint_t` can be the same integer type.

Three possible solutions are:

1. Fix the example.
2. Change the definition of `wint_t` to be the promoted version of `wchar_t`.
3. Change the definition of `%lc` to take promoted `wchar_t` rather than `wint_t`.

### Suggested Technical Corrigendum 1

Change the quoted line of 7.19.6.1#18 to:

> ```c
>   fprintf(stdout, "|%13lc|\n", (wint_t) wstr[5]);
> ```

### Suggested Technical Corrigendum 2

Change the cited portion of 7.24.1#2 to:

> `wint_t` which is the integer type resulting when the default argument
> promotions are applied to the type `wchar_t`;269) and

### Suggested Technical Corrigendum 3

*\[Italics are used to show the changed text.]*

Change 7.19.6.1#7 and 7.24.2.1#7, l modifier, to:

> |  |  |
> | --- | --- |
> | `l` (ell) | Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `long int` or `unsigned long int` argument; that a following `n` conversion specifier applies to a pointer to a `long int` argument; that a following `c` conversion specifier applies to *an argument whose type is that resulting when the default argument conversions are applied to the type `wchar_t`*; that a following `s` conversion specifier applies to a pointer to a `wchar_t` argument; or has no effect on a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier. |

Change 7.19.6.1#8, `c` specifier, second paragraph, to:

> If an `l` length modifier is present*, the argument \- whose type is that
> resulting when the default argument conversions are applied to the type
> `wchar_t`* \- is converted as if by an `ls` conversion specification with no
> precision and an argument that points to the initial element of a two-element
> array of `wchar_t`, the first element containing *the argument* to the `lc`
> conversion specification and the second a null wide character.

Change 7.24.2.1#8, `c` specifier, second paragraph, to:

> If an `l` length modifier is present, *the argument* is converted to `wchar_t`
> and written.
