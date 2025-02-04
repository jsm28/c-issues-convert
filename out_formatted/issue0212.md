## Issue 0212: Binding of multibyte conversion state objects

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 1999-10-20  
Reference document: [ISO/IEC WG14 N898](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n898.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_212.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_212.htm)

### Summary

At present an `mbstate_t` object can only ever be used to make one conversion.
This is not desirable, and changes are proposed in this area.

**Discussion**  
Clause 7.24.6 paragraph 3 reads, in part:

> If an `mbstate_t` object has been altered by any of the functions described in
> this subclause, and is then used with a different multibyte character sequence,
> or in the other conversion direction, or with a different `LC_CTYPE` category
> setting than on earlier function calls, the behavior is undefined.

Put another way, each `mbstate_t` object is initially "unbound" (if it is
initialized to zero) and then becomes "bound" by any call to a function such as
`mbrtowc` or `wcrtomb`. When "bound" it can only be used in the same direction
with the same string as originally bound, and only when the `LC_CTYPE` category
is that in effect when it was bound. With ordinary `mbstate_t` objects this is a
annoyance; one implication is that a new object must be created every single
time a new string is to be converted (the Standard does not provide any way to
"unbind" the object). With the `mbstate_t` object inside a `FILE` structure it
is even worse, because it makes it impossible to (for example) write to a file,
rewind it, and then read the same file. Similarly, the internal `mbstate_t`
objects used when the `mbstate_t` pointer argument is set to `NULL` can be used
for only one string in the entire program !

Users of `mbstate_t` objects (including those in `FILE` structures) expect to be
able to use them for more than a single purpose.

**Proposed solution**  
The changes introduce the concept that an `mbstate_t` object is either "unbound"
or "bound". When set to an all-zero value (which can be at initialization or
explicitly later on) it is unbound. As soon as the object is used for a
conversion it becomes bound to that string, locale, and direction. Returning to
the initial state does not unbind the object (in other words, while all unbound
objects are in the initial state the converse is not necessarily true).

The special cases of `mbrtowc` and `wcrtomb` are defined to always result in an
unbound state. This both provides more consistent behaviour (the special case
resets everything to a known state) and also allows the internal `mbstate_t`
objects associated with these functions to be unbound.

The `mbstate_t` object hidden in a file is returned to the unbound state
whenever end of file is reached on input, and by any call to `fseek` (these
choices were made to correspond with the requirements of 7.19.5.3 paragraph 6
for changing I/O direction).

The internal `mbstate_t` objects associated with the `mbrlen`, `mbrtowc`,
`wcrtomb`, `mbsrtowcs`, and `wcsrtombs` functions can only be used with the
locale they initially bind to. Other changes deal with the first three; a
previously impossible case is used for the last two to force the object to the
unbound state.

### Suggested Technical Corrigendum

(*Changes concerning explicit* `mbstate_t` *objects.*)  
Change 7.24.6 paragraph 3 to:

> \[#3] The initial conversion state corresponds, for a conversion in either
> direction, to the beginning of a new multibyte character in the initial shift
> state. An `mbstate_t` object may be "unbound" or "bound". A zero-valued
> `mbstate_t` object is (at least) one way to describe an unbound object, and if
> an mbstate\_t object is assigned such a value it it becomes unbound. All unbound
> `mbstate_t` objects are in the initial conversion state (but the converse is not
> necessarily true).
>
> \[#3a] An unbound object can be used to initiate conversion involving any
> multibyte character sequence, in any `LC_CTYPE` category setting, in either
> direction; once used for a conversion, it becomes bound to that sequence,
> category setting, and direction. If a bound `mbstate_t` object is used with a
> different multibyte character sequence, a different `LC_CTYPE` category setting,
> or in the other conversion direction to that it is bound to, the behavior is
> undefined.<sup>290</sup>)

Append to footnote 290:

> Furthermore, provided that the object is unbound, and thus in the initial
> conversion state, it can then be used in converting a new string, a new locale,
> or in the other direction.

Change 7.24.6.3 paragraph 1 and 7.24.6.4 paragraph 1 from:

> \[...] which is initialized at program startup to the initial conversion state.
> \[...]

to:

> \[...] which is initialized at program startup to the unbound state. \[...]

Change 7.24.6.3.2 paragraph 2 to:

> \[#2] If s is a null pointer, the `mbrtowc` function is equivalent to the call:
>
> > ```c
> > mbrtowc(NULL, "", 1, ps)
> > ```
>
> except that the resulting state described is unbound even if an encoding error
> occurred.
>
> In this case, the values of the parameters `pwc` and `n` are ignored.

Change 7.24.6.3.3 paragraph 2 to:

> \[#2] If s is a null pointer, the `wcrtomb` function is equivalent to the call
>
> > ```c
> > wcrtomb(buf, L'\0',ps)
> > ```
>
> where `buf` is an internal buffer except that the resulting state described is
> always unbound even if an encoding error occurred <sup>291a</sup>; the value of
> `wc` is ignored.
>
> 291a) The effect is reliably to make `*ps` unbound.

Append to 7.24.6.4 paragraph 2:

> As a special case, if `src` is a null pointer then the normal behaviour of the
> function is ignored and instead `ps` becomes unbound irrespective of its
> previous state; an unspecified value is returned.

(*Changes associated with streams.*)  
Append to 7.19.2 paragraph 6:

> If a wide character input function encounters end-of-file, or after a successful
> call to the fseek function, the`mbstate_t` object associated with the stream is
> unbound.

Append to the last sentence of 7.19.9.2 paragraph 5:

> and if the stream is wide-oriented the associated `mbstate_t` object shall be
> unbound.

In 7.24.3.1 paragraph 2, change: to:

> \[...] If the stream is at end-of-file, the end-of-file indicator for the stream
> is set, the `mbstate_t` object associated with the stream is unbound, and
> `fgetwc` returns `WEOF`. \[...]

---

Comment from WG14 on 2001-09-18:

### Committee Response

The consensus is that a programmer can put an `mbstate_t` object in the initial
conversion state *for any sequence* by the assignment:

> ```c
> static mbstate_t init_state = {0};
> ```
>
> *...*
>
> ```c
> mbstate_t mystate = init_state;
> ```

This technique is used and is believed it to be portable.

There is concern about over specifying the behavior of streams. The Committee
believes that to say that the state becomes unbound at EOF, would cause problems
with a read/write stream that later gets extended. The Committee could not find
a valid reason to hamstring the reader just because it reached an interim EOF.
Moreover, is is unlikely one can portably `fsetpos()` in a wide stream except to
the beginning or to a point that was earlier memorized with an `fgetpos()`. In
either case, there is an obvious state to restore. Old fashioned
`seek()`/`tell()` logic just doesn't full fill the requirements for a wide
stream.

The Committee believes that real implementations and real applications do in
fact support streams that do not begin in the initial state, as well as streams
that do not end in the initial state.

It was also pointed out that even with the suggested text that required a file
to begin in the initial shift state, there was no stated requirement that
`fopen` initialize the associated `mbstate_t` object to have the initial shift
state (which again, would break existing implementations that support files that
do not begin in the initial shift state).

There is no consensus to make this change or any change along this line.
