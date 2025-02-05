## Issue 0254: `mbtowc` and partial characters

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_254.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_254.htm)

### Problem

If `mbtowc()` is given a partial character (or an escape sequence that isn't a
complete character), it returns -1. However, is it supposed to remember the
relevant state information or should it ignore it ?

Consider an implementation where the character `'\xE'` starts an alternate shift
state and `'\xF'` returns to the initial shift state. The wide character
encodings are:

|  |  |  |
| --- | --- | --- |
|  | initial shift state: | 'x' maps to ASCII codes |
|  | alternate shift state: | 'x' maps to ASCII codes \+ 0x100 |

Starting in the initial shift state,

```c
   mbtowc (&wc, "\xEZ", 2);
```

should return 2 and set `wc` to 0x15A. However, starting in the initial shift
state, consider:

```c
   mbtowc (&wc1, "\xE", 1);
    mbtowc (&wc2, "Z",   1);
```

I would expect that the first call returns -1, leaving `wc1` unaltered, while
the second returns 1 and sets `wc2` to 0x5A. However, is it permitted for the
second to set `wc2` to 0x15A ? If so, how is an application meant to use
`mbtowc` ?

\[The newer function `mbrtowc` does not have this problem.\]

### Suggested Technical Corrigendum

The UK C Panel prefers to add a new return value for this case. To do so, change
the main part (see *the previous DR*) of 7.20.7.2#3 to read:

> If `s` is a null pointer, the mbtowc function returns a nonzero or zero value,
> if multibyte character encodings, respectively, do or do not have
> state-dependent encodings. If `s` is not a null pointer, the `mbtowc` function
> returns the first of the following that applies (given the current conversion
> state):
>
> |  |  |
> | --- | --- |
> | 0 | if `s` points to the null character |
> | between 1 and `n` inclusive | if the next `n` or fewer bytes complete a valid multibyte character (which is the value stored); the value returned is the number of bytes that complete the multibyte character. The value returned will not be greater than that of the `MB_CUR_MAX` macro. |
> | `(size_t)(-2)` | if the next `n` bytes contribute to an incomplete (but potentially valid) multibyte character, and all `n` bytes have been processed (no value is stored). |
> | `(size_t)(-1)` | if an encoding error occurs, in which case the next `n` or fewer bytes do not contribute to a complete and valid multibyte character (no value is stored); the value of the macro `EILSEQ` is stored in `errno`, and the conversion state is unspecified. |

(note that most of this wording comes from `mbrtowc`) and delete #4.

If this option is unacceptable, then append to 7.20.7.2#2:

> If the next multibyte character is incomplete or invalid, the shift state is
> unaffected and nothing is stored.

---

Comment from WG14 on 2002-03-06:

### Committee Response

The Committee believe the behavior of this example is unspecified. The
`mbrtowc()` function provides a superior migration path, so we are leaving this
alone.
