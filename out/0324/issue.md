**Summary #1**

5.1.1.2 #2 ("Translation phases") says:

> \[#2] ...2. Each instance of a backslash character (`\`) immediately followed by
> a new-line character is deleted, splicing physical source lines to form logical
> source lines. Only the last backslash on any physical source line shall be
> eligible for being part of such a splice. A source file that is not empty shall
> end in a new-line character, which shall not be immediately preceded by a
> backslash character before any such splicing takes place.
>
> 3\. The source file is decomposed into preprocessing tokens<sup>6\)</sup> and
> sequences of white-space characters (including comments). A source file shall
> not end in a partial preprocessing token or in a partial comment. Each comment
> is replaced by one space character. New-line characters are retained. Whether
> each nonempty sequence of white-space characters other than new-line is retained
> or replaced by one space character is implementation-defined.

Assuming there is a non-empty source file legally ending with a new-line
character, what are examples of such partial preprocessing tokens that could end
the file? And, generally, what the partial preprocessing tokens are?

**Summary #2**

6.4.4.4 ("Character constants") says:

> \[#3] The single-quote `'`, the double-quote `"`, the question-mark `?`, the
> backslash `\`, and arbitrary integer values are representable according to the
> following table of escape sequences...
>
> \[#5] The octal digits that follow the backslash in an octal escape sequence are
> taken to be part of the construction of a single character for an integer
> character constant or of a single wide character for a wide character
> constant...
>
> \[#6] The hexadecimal digits that follow the backslash and the letter `x` in a
> hexadecimal escape sequence are taken to be part of the construction of a single
> character for an integer character constant or of a single wide character for a
> wide character constant...
>
> \[#8] In addition, characters not in the basic character set are representable
> by universal character names and certain nongraphic characters are representable
> by escape sequences consisting of the backslash `\` followed by a lowercase
> letter: `\a`, `\b`, `\f`, `\n`, `\r`, `\t`, and `\v`.<sup>64\)</sup>
>
> <sup>64\)</sup> The semantics of these characters were discussed in 5.2.2. If
> any other character follows a backslash, the result is not a token and a
> diagnostic is required. See “future language directions” (6.11.4).

6.4 #3 ("Lexical elements") says:

> \[#3] ...The categories of preprocessing tokens are: header names, identifiers,
> preprocessing numbers, character constants, string literals, punctuators, and
> single non-white-space characters that do not lexically match the other
> preprocessing token categories.<sup>58\)</sup> If a `'` or a `"` character
> matches the last category, the behavior is undefined.

What in the formal content of the standard says that if any other character
follows a backslash, there should be a diagnostic? Does such a case causes
undefined behaviour? Furthermore, if a character sequence that is coming just
after a double quote `"` (that is not terminating a string literal) begins with,
say, `\l` and the result of the tokenization is not a token, then what the
result is?

**Summary #3**

6.10.9 #2 ("Pragma operator") gives the following example:

> \[#2] EXAMPLE A directive of the form:
>
> ```c
> #pragma listing on "..\listing.dir"
> ```
>
> can also be expressed as:
>
> ```c
> _Pragma ( "listing on \"..\\listing.dir\"" )
> ```

The previous summary says that if there an unknown escape sequence encountered
during tokenization of a character constant or string literal, then the result
is not token. The question is whether the example above is well-defined.

### Suggested Technical Corrigendum
