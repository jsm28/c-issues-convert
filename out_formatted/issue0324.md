## Issue 0324: Tokenization obscurities

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ivan A. Kosarev (Unicals Group, RU)  
Date: 2005-04-19  
Reference document: [N1123](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1123.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_324.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_324.htm)

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

---

Comment from WG14 on 2006-10-25:

### Proposed Committee Response

**Answers to Summary #1**

"Partial preprocessing token" is not itself a technical term; it is merely the
English Language word "partial" modifying the technical term "preprocessing
token". A preprocessing token is defined by the grammar non-terminal
*preprocessing-token* in Subclause 6.4. A partial preprocessing token is
therefore just part of a preprocessing token that is not the entire
preprocessing token.

The statement that "source files shall not end in a partial preprocessing token
or in a partial comment" has two implications. First, a preprocessing token may
not begin in one file and end in another file. Second, the last preprocessing
token in a source file must be well-formed and complete. For example, the last
token may not be a string literal missing the close quote.

**Answers to Summary #2**

Subclause 5.1.1.3 requires a diagnostic to be produced if there is a violation
of any syntax rule or constraint. The syntax for character constants (Subclause
6.4.4.4) and string literals (Subclause 6.4.5) both require that any escape
sequence be well formed according the nonterminal *escape-sequence* (Subclause
6.4.4.4). Thus a diagnostic is required if a character constant or string
literal contains a `\` not followed by the remainder of a valid escape sequence.

Note that a preprocessor token may be a *header-name* in addition to a
*string-literal*. Although a *header-name* has the appearance of a string
literal, it is parsed by a different grammar (Subclause 6.4.7). The syntax for
*header-name* is not violated if a `\` is not followed by the remainder of a
valid escape sequence. Thus, no diagnostic is required. However, if a header
name contains a `\`, the behavior is undefined (Subclause 6.4.7, paragraph 3).

Since the behavior is undefined, the implementation is free to do anything it
wishes. Some possible examples:

* Fail
* Issue a diagnostic
* Treat the `\` as the start of an escape sequence
* Treat the `\` as a literal character

The last alternative is useful if your operating system normally uses `\` in the
names of files.

**Answers to Summary #3**

Before your question can be answered, it is necessary to understand the precise
steps taken in translating a `_Pragma` operator as controlled by the phases of
translation (Subclause 5.1.1.2).

The `_Pragma` operator (Subclause 6.10.9) has an argument that is a string
literal. If any escape sequence in that string literal is not grammatically
well-formed, a diagnostic is required. In the example, the string literal is
syntactically correct, so no diagnostic is required so far.

The `_Pragma` operator is executed during translation phase 4\. Note that escape
sequences in a string are not replaced by the characters that they represent
until translation phase 5\. However, the `_Pragma` operator itself does limited
processing to handle `\\` and `\"` escape sequences (Subclause 6.10.9 paragraph
1), and so when the value of the string literal is retokenized to produce
preprocessor tokens, the result for the example matches the `#pragma` directive
given.

The final answer to your question rests with whether the preprocessor tokens in
the `#pragma` directive require a diagnostic. Subclause 6.10.6 states that a
`#pragma` directive ends in just a list of preprocessor tokens without placing
any requirements on which preprocessor tokens.

Your question then becomes whether the preprocessor token that looks like a
string in the `#pragma` in the example is a *string-literal* or a *header-name*.
If it is a *string-literal*, a diagnostic is required. If it is a *header-name*,
no diagnostic is required, but there is undefined behavior. The choice of which
preprocessor tokens are allowed in a `#pragma` directive is implementation
defined.

Subclause 6.10.9 paragraph 1 states that a `#pragma` causes the implementation
to behave in an implementation-defined manner including the possibility that the
implementation might fail or otherwise behave in a non-conforming manner. The
intent of the committee was that implementations could recognize *header-name*
preprocessor tokens in `#pragma` directives, if the implementation chooses, but
this seems to be contradicted by the two places requiring Technical Corrigenda
below.

### Technical Corrigendum

Change Subclause 6.4.7, paragraph 3, last sentence to:

Header name preprocessing tokens are recognized only within `#include`
preprocessing directives or in implementation-defined locations within `#pragma`
directives<sup>\*)</sup>.

(\* New Footnote): For an example of a header name preprocessing token used in a
`#pragma` directive, see Subclause 6.10.9.

Change Subclause 6.4, paragraph 4, last sentence to:

There is one exception to this rule: Header name preprocessing tokens are
recognized only within `#include` preprocessing directives or in
implementation-defined locations within `#pragma` directives. In such contexts,
a sequence of characters that could be either a header name or a string literal
is recognized as the former.
