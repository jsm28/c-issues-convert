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
