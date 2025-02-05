## Issue 0022: What is the result of `strtod("100ergs", &ptr)`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-002  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_022.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_022.html)

What is the result of: `strtod("100ergs", &ptr);`? Is it 100.0 or is it 0.0?

Subclause 7.10.1.4 **The `strtod` function** on page 150, lines 36-38 says: “The
subject sequence is defined as the longest initial subsequence of the input
string, starting with the first non-white-space character, that is of the
expected form.” In this case, the longest initial subsequence of the expected
form is `100`, so `100.0` should be the return value. Also, since the entire
string is in memory, `strtod` can scan it as many times as need be to find the
longest valid initial subsequence.

Subclause 7.9.6.2 **The `fscanf` function** on page 136, lines 17-18 says:
“`e`,`f`,`g` Matches an optionally signed floating-point number, whose format is
the same as expected for the subject string of the `strtod` function.” Later,
page 138, lines 6, 16, and 25 show that `100ergs` fails to match `%f`. Those two
show that `100ergs` is invalid to `fscanf` and therefore, invalid to `strtod`.
Then, subclause 7.10.1.4, page 151, lines 11-12, “If no conversion could be
performed, zero is returned” indicates for an error input, 0.0 should be
returned. The reason this is invalid is spelled out in the rationale document,
subclause 7.9.6.2 **The `fscanf` function**, page 85: “One-character pushback is
sufficient for the implementation of `fscanf`. Given the invalid field `-.x`,
the characters `-.` are not pushed back.” And later, “The conversions performed
by `fscanf` are compatible with those performed by `strtod` and `strtol`.”

So, do `strtod` and `fscanf` act alike and both accept and fail on the same
inputs, by the one-character pushback scanning strategy, or do they use
different scanning strategies and `strtod` accept more than `fscanf`?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.6.2, page 135, lines 31-33, change:***

An input item is defined as the longest matching sequence of input characters,
unless that exceeds a specified field width, in which case it is the initial
subsequence of that length in the sequence.

***to:***

An input item is defined as the longest sequence of input characters which does
not exceed any specified field width and which is, or is a prefix of, a matching
input sequence.

***In subclause 7.9.6.2, page 137, delete:***

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.

***Add to subclause 7.9.6.2, page 137:***

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.\* \[Footnote \*: `fscanf` pushes
back at most one input character onto the input stream. Therefore, some
sequences that are acceptable to `strtod`, `strtol`, or `strtoul` are
unacceptable to `fscanf`.\]
