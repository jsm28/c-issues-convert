## Issue 0498: `mblen`, `mbtowc`, and `wctomb` thread-safety

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Philipp Klaus Krause  
Date: 2016-04-11  
Reference document: [N2037](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2037.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

This corresponds to Austin Group Defect #708 by Rich Felker. The following four
paragraphs are copies of that Defect Report and the three responses, all from
2013\.

dalias (Rich Felker, musl libc): Per C11 7.1.4 paragraph 5, "Unless explicitly
stated otherwise in the detailed descriptions that follow, library functions
shall prevent data races as follows: A library function shall not directly or
indirectly access objects accessible by threads other than the current thread
unless the objects are accessed directly or indirectly via the function's
arguments. A library function shall not directly or indirectly modify objects
accessible by threads other than the current thread unless the objects are
accessed directly or indirectly via the function's non-const arguments.
Implementations may share their own internal objects between threads if the
objects are not visible to users and are protected against data races." 7.22.7
(Multibyte/wide character conversion functions) does not specify that these
functions are not required to avoid data races with other calls. The only time
they would even potentially be subject to data races is for state-dependent
encodings, which are all but obsolete; for single-byte or modern multi-byte
(i.e. UTF-8) encodings, these functions are pure. Note that 7.29.6.3
(Restartable multibyte/wide character conversion functions) does make exceptions
that the "r" versions of these functions are not required to avoid data races
when the state argument is NULL.

geoffclare: It seems odd that C11 would have different thread-safety
requirements for mbrlen, mbrtowc, and wcrtomb with a null state argument than
for mblen, mbtowc, and wctomb. We should query this with the C committee, as it
may well be unintentional.

dalias: I think there's a very good reason for the discrepancy: the restartable
versions can store a partially-decoded character in the mbstate\_t object, so
even for state-independent encodings, there is state which would need to be
protected against data races. The non-restartable versions, on the other hand,
are pure except in the case of state-dependent encodings, which are mostly a
relic of the past and which were never supported on most POSIX systems, since
these encodings are mostly incompatible with POSIX filesystem semantics. Only
implementations supporting such encodings (which might not even exist \- can
anyone confirm?) would incur the burden of avoiding data races. Note that these
functions give applications access to information on whether the locale's
encoding is state-dependent, so a portable application could use the restartable
interfaces when the locale is state-dependent, and the non-restartable ones
otherwise. As to the motivation behind my request for this change, I have spent
a good deal of time investigating the performance bottlenecks in
character-at-a-time multibyte processing, and it turns out that there is a
fundamental bottleneck in the restartable interfaces due to their interface
requirements for handling the ps argument and partially-decoded characters. For
applications which don't need partial-character processing capability, I believe
it would make sense to encourage a transition to the non-restartable interfaces,
but of course this is problematic if the non-restartable interfaces are not
thread-safe. In my experiments, I found the non-restartable interfaces capable
of reaching roughly a 50% performance advantage over the restartable ones; this
difference would of course become even more extreme if the core decoding
algorithms were further optimized.

nick: This will be raised as a potential defect with the C committee, and any
decision on how to proceed should be made there first.

It seems however that this was so far not brought to the attention of WG 14\.
There seems to be confusion about the thread-safety of mblen(), mbtowc() and
wctomb() when the encoding is not state-dependent. While the C standard seems to
imply that the functions are thread-safe when the encoding is not
state-dependent, apparently some think otherwise. The GNU/Linux manpage for
these functions states "MT-Unsafe race", and recommends to use mbrlen() instead.
Thus clarification is needed.

**Possible Change**

A footnote could be added to 7.22.7 clarifying that the functions mblen(),
mbtowc() and wctomb() do not keep internal state if the encoding is not
state-dependent.

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The text in §7.1.4 paragraph 5 requires implementations to avoid data races in
> library functions that maintain their internal state. The `mblen`, `mbtowc`, and
> `wctomb` functions are among those that maintain such state. Although the state
> is typically needed only for state-dependent, multibyte encodings, the standard
> doesn't intend to prevent implementations from accessing it for other encodings
> as well. And indeed implementations are known to exist that access the state for
> other encodings as well. Multi-threaded programs that need the functionality
> provided by these functions are intended to make use of the corresponding
> restartable forms of these functions instead (i.e., `mbrlen`, `mbrtowc`, and
> `wcrtomb`, respectively) with a non-null state pointer.

In §7.22.7 paragraph 1 , change:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate.

to:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate. A call to any one of these functions may introduce a data
> race with a call to any other function in this section.

In §7.29.6.3 paragraph 1 , change:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`.

to:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`. A call to one of these functions with a null `ps`
> pointer may introduce a data race with another call to the same function.

Apr 2017 meeting

### Committee Discussion

> The committee adopted the words discussed in the previous meeting, with a small
> refinement as suggested in [(SC22WG14.14652) editorial tweak for DR 498
> PTC](https://www.open-std.org/jtc1/sc22/wg14/14652).

Apr 2017 meeting

### Committee Discussion

> A new paper [N2246](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2246.htm)
> was not discussed at WG14 and has been postponed until the next meeting.

### Proposed Change

In §7.22.7 paragraph 1 , change:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate.

to:

> Changing the `LC_CTYPE` category causes the conversion state of these functions
> to be indeterminate. A call to any one of these functions may introduce a data
> race with a call to any other function in this subclause.

In §7.29.6.3 paragraph 1 , change:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`.

to:

> The implementation behaves as if no library function calls these functions with
> a null pointer for `ps`. A call to one of these functions with a null `ps`
> pointer may introduce a data race with another call to the same function.

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> A new paper [N2281](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2281.htm)
> was discussed at some length for possible inclusion in a new edition of the
> standard.
>
> The committee believes that the goal of these papers is to establish a normative
> requirement that calls to `mblen`, `mbtowc`, and `wctomb` be data-race free when
> operating upon state-independent encodings. The committee notes that interleaved
> calls to `setlocale` that change even among non-state-dependent encodings must
> necessarily atomically change a reference to the encoding tables used by these
> functions, and that such change would impede the desired speed advantage sought
> by this change. Any assertion of data-race free must also disallow interleaved
> calls to `setlocale` to maintain the speed advantage.
>
> It was also noted in earlier discussions that some implementations are known to
> use shared state even for non-state dependent encodings.
>
> A new paper is solicited from the author for inclusion in a new edition of the
> standard. An affirmative statement is requested, perhaps along the lines of: The
> total order of `mblen`, `mbtowc`, and `wctomb` shall be data-race free when
> there are no calls to `setlocale` in that order and, proabably, that a
> state-indepenent encoding has been determined by a call to `mblen` in the
> normative manner.
