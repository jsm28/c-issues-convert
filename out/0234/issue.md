**Summary #1**

In 6.10.3 Macro Replacement the text:

> \[#5\] The identifier `__VA_ARGS__` shall occur only in the replacement-list of
> a function-like macro that uses the ellipsis notation in the arguments.

The word "arguments" should be "parameters".

**Summary #2**  
In the Foreword under major changes, `VA_COPY` should be `va_copy` .

**Summary #3**  
In 7.11.2.1, in the description of the `lconv` members `int_p_cs_precedes`,
`int_n_cs_precedes`, `int_p_sep_by_space`, and `int_n_sep_by_space`, the
reference to `int_currency_symbol` should be `int_curr_symbol`.

**Summary #4**  
In 7.19.6.14 The `vsscanf` function:

> The `vsscanf` function returns the value of the macro `EOF` if an input failure
> occurs before any conversion. Otherwise, the `vscanf` function ...

The reference to `vscanf` should be `vsscanf`.

**Summary #5**  
In 7.19.6.12 The `vsnprintf` function is misspelled in the synopsis.

**Summary #6**  
In 7.4.1.12, paragraph #2, "as defined in 6.4.4.2" should be "as defined in
6.4.4.1".
