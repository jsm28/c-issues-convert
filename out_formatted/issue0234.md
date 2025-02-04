## Issue 0234: Miscellaneous Typos

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14 Convener (John Benito)  
Date: 2000-09-26  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_234.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_234.htm)

**Summary #1**

In 6.10.3 Macro Replacement the text:

> \[#5] The identifier `__VA_ARGS__` shall occur only in the replacement-list of a
> function-like macro that uses the ellipsis notation in the arguments.

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

---

Comment from WG14 on 2001-01-22:

### Technical Corrigendum

In the cited text in 6.10.3, change "arguments" to "parameters"

In the Foreword, change `VA_COPY` to `va_copy`.

In 7.11.2.1, change all occurrences of `int_currency_symbol` to
`int_curr_symbol`. Also, append to paragraph 5:

> For `int_p_sep_by_space` and `int_n_sep_by_space`, the fourth character of
> `int_curr_symbol` is used instead of a space.

In 7.19.6.14, change the reference from `vscanf` to `vsscanf`.

In 7.19.6.12, change `vsprintf` to `vsnprintf` in the synopsis.

In 7.4.1.12, change "(as defined in 6.4.4.2)" to "(as defined in 6.4.4.1)".
