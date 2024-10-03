Do functions return values by copying?

The C Standard is clear (in subclause 6.3.2.2) that function arguments are
copied, but is not clear (in subclause 6.6.6.4) whether a function's returned
value is also copied. This question becomes an issue in the assignment statement
`s=f();` where `f` yields a structure: is the result defined when the structure
`s` overlaps the structure that `f` obtained the returned value from?

I ask this question because the GNU C compiler does not copy the structure in
this case. When I filed the enclosed bug report \[omitted from this document],
Richard Stallman, the author of GNU C, replied that he didn't think that
Standard C required the extra copy. I sympathize with Stallman's desire for
efficient code, and I also would prefer that the C Standard did not require the
extra copy here, but the point should be made clear in the C Standard.
