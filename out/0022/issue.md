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
