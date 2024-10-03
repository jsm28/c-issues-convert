Subclause 5.1.1.1, page 5, lines 11-20 define a “translation unit” to be
equivalent to the sequence of preprocessing tokens and white-space characters
which exists at the end of translation phase 4 (subclause 5.1.1.2). Later in
translation phases 5, 6, 7, these preprocessing tokens are converted to tokens
and syntactically and semantically analyzed and translated.

Therefore, must a conforming implementation provide strictly conforming
expansions of macros defined by the standard headers, such that any use of the
resulting preprocessing token sequence, and ultimately the token sequence,
beyond phase 4 does not alter the behavior of an otherwise strictly conforming
program? See also clause 4 **Compliance**, page 4, lines 24-26.
