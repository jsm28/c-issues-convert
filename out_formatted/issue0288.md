## Issue 0288: deficiency on multibyte conversions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: BSI, Clive Feather  
Date: 2003-10-21  
Reference document: [N1012](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1012.txt)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_288.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_288.htm)

### Summary

Consider a typical use of the multibyte conversion function `mbrtowc`:

```c
    enum { FINISHED, ERROR } convert (void)
    {
        mbstate_t s = { 0 };
        char c;
        wchar_t wc;

        for (;;)
        {
            c = get_a_byte ();
            switch (mbrtowc (&wc, &c, 1, &s))
            {
            case 1:          put_wide_char (wc);    break;
            case (size_t)-2: break;
            case 0:          put_wide_char (L'\0'); return FINISHED;
            case (size_t)-1: return ERROR;
            }
        }
    }
```

The multibyte conversion functions were originally written on the assumption
that wide characters are singletons. That is, while several multibyte characters
may map to one wide character, and may map to different wide characters
depending on the current state, each sequence maps to only one wide character.
As a result, functions such as `mbrtowc` do not have the concept of returning
more than one wide character; only a single one can be returned per call.

This is fine for mappings like:

```c
    ISO 8859-1   ->  UTF-16 or UTF-32 in Normalization Form C
    UTF-8        ->  UTF-32 without change of normalization
```

but not for others. It is possible to play fast and loose with the meaning of
*state* to relax the requirement a little bit \- if a sequence of three bytes
maps to two wide characters, the first call to `mbrtowc` can return `2` and the
second call `1`, with the state object holding any necessary information. The
requirement then becomes: N bytes can result in M wide characters, where N \>\=
M and where the first K wide characters depend only on the first N-M\+K bytes.
An example of such a mapping is UTF-8 -\> UTF-16 (shown in binary):

```c
  0AAAAAAA                            -> 000000000AAAAAAA
  110AAAAA 10BBBBBB                   -> 00000AAAAABBBBBB
  1110AAAA 10BBBBBB 10CCCCCC          -> AAAABBBBBBCCCCCC
  11110AAA 10BBCCCC 10DDEEEE 10FFFFFF -> 110110XXXXCCCCDD
110111EEEEFFFFFF
```

In the last case the `mbrtowc` function can return `-2`, `-2`, `1`, and `1` in
that order. However, consider a very similar encoding to UTF-16 where the two
wide characters are in the opposite order. The first wide character (the one
beginning 110111\) cannot be output until all 4 bytes have been seen, so the
first three calls to mbrtowc must return `-2`. The fourth call can return the
first wide character, but there is now no way to return the second one. If the
next UTF-8 sequence is 2 or 3 bytes long, it would provide an opportunity, but
if it is only 1 byte long or, even worse, was the zero character, it wouldn't.
While the above is a hypothetical situation, a real conversion that has this
problem is converting ISO 8859-1 (or many similar encodings) to Unicode in
Normalization Form D. In NFD all accented characters are broken down into their
components. So some example conversions are:

```c
    0x20 -> 0x0020
    0x61 -> 0x0061
    0xBF -> 0x00BF
    0xC0 -> 0x0041 0x0300
    0xC1 -> 0x0041 0x0301
    0xC4 -> 0x0041 0x0308
    0xC8 -> 0x0045 0x0300
    0xE6 -> 0x00E6
    0xE7 -> 0x0063 0x0327
```

What is needed is for mbrtowc to have a way to say "I have an unfinished wide
character sequence, I do not need any more bytes for now". The obvious way to
represent this would be a returned value of `0`. Unfortunately this has already
been given a different meaning ("end of string reached") and changing it would
be impractical. Therefore the following text proposes the return value `-3` for
this case. This value would only be generated for locales where this was an
issue, so it will not affect existing uses of the code. And applications that
are not modified to handle this code but are presented with it are likely to
treat it as an error.

Of the other functions in 7.24.6, `mbrlen` has the same problem. The `wcrtomb`
function also has to deal with this issue, but the wording already allows it to
be state-ful and return `0` to indicate that nothing has been output at this
stage. Neither the `mbsrtowcs` nor `wcsrtombs` functions have an issue (though
with the former it is possible that the limit of len wide characters is reached
in the middle of a multi-wide-character sequence; the rest of the sequence will
be retained in the `mbstate_t` object until the next call).

### Suggested Technical Corrigendum

Append to 7.24.6.3.2#4:

> `(size_t)(-3)` if the multibyte sequence converted by the previous call with the
> same `mbstate_t` object generated more than one wide character and not all these
> characters have yet been stored; the next wide character in the sequence has now
> been stored and no bytes from the input have been consumed by this call.

In 7.24.6.3.1#3, add `(size_t)(-3)` to the possible returned values.

Optional extra change for clarity:

In 7.24.6.3.3#4, EITHER add to the end of the first sentence:

> ; this may be 0

OR add a footnote reference to that sentence:

> 291A If the wide character encoding requires two or more wide characters to be
> considered together when doing the conversion, the value returned can be 0\.

The Rationale could also be amended to address these issues.

---

Comment from WG14 on 2004-09-28:

### Committee Discussion

* More time is needed to assess the impact on the char32 work!
* Not really a *defect*, but a *deficiency*.

### Committee Response

This is not really a *defect*, but a *deficiency* which could be addressed in a
future release of the C Standard.
