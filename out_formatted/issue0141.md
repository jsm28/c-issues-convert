## Issue 0141: What does `EOF` mean in `<stdio.h>`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Doug McIlroy, Project Editor (P.J. Plauger)  
Date: 1994-09-10  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_141.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_141.html)

What does `EOF` mean in `<stdio.h>`? Subclause 7.9.1 says that it “is returned
by several functions to indicate *end-of-file,* that is, no more input from a
stream.”

Taken at face value, the statement that there is no more input implies that
further reads from the stream will yield `EOF`. In many implementations this is
not true. It may be possible to read data from a stream on which the end-of-file
indicator is set. Just whether that happens usually depends on what kind of file
the stream is associated with. In System V, for example, one will almost always
get more data on reading past `EOF` on a terminal, and almost never on a plain
file. This violates the principle of device-independent behavior.

I believe the System V behavior is wrong. Whenever `feof` would return nonzero,
`getc` should return `EOF`.

Some old code will break if `EOF` is made sticky as I suggest, but surprisingly
little. When we made it sticky in v10 UNIX, we had to change exactly one
dishonest program (sdb), which used ctl-D as if it were a character without
putting the terminal in raw mode. Not one complaint arose from the change.

On the other hand, almost every UNIX user has at one time or another been
surprised by a nonsticky `EOF`, manifested as a program needing more than one
`EOT` to stop it when `stdin` comes from a terminal. That breeds the habit of
typing extra `EOT` at balky programs. The habit causes yet more trouble (hangup,
for example), when things are merely slow and not really balky. This
indefinite-`EOF` problem is not the fault of the programs, which should be able
to count on a uniform behavior of `EOF` across all files. It is a fundamental
mistake in the implementation of `<stdio.h>`.

I urge the Committee to clarify `EOF`, and clarify it in the direction of
predictability.

---

Comment from WG14 on 1997-09-23:

### Response

It was certainly the intent of the Committee that end-of-file should indicate
“no more input from a stream,” at least when returned by functions such as
`fgetc`. In particular, subclause 7.9.7.1 **The `fgetc` function** says, in
part:

If the stream is at end-of-file, the end-of-file indicator for the stream is set
and `fgetc` returns `EOF`. “Setting the end-of-file indicator” implies that
*that stream* is now considered to be “at end-of-file.”

For input from a stream to return other than `EOF` after once returning `EOF`
(with no intervening file-positioning operations or calls to `clearerr`) is
non-conforming behavior, however widespread.
