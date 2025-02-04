## Issue 0003.02: Should white space surround macro substitutions?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Macro substitutions, tokenization, and white space In general I
think it is a good guiding principle that a C implementation should be able to
be based around completely disjoint preprocessing and lexical scanning parses of
the compiler. As such the rules on tokenizing need to be emphasized with the
following paragraphs (possibly placed after paragraph 1 of subclause 6.8.3.1):

> All macro substitutions and expanded macro argument substitutions will result in
> an additional space token being inserted before and after the replacement token
> sequence where such a space token is not already present and there is a
> corresponding preceding or subsequent token in the target token sequence.
>
> The last token of every macro argument has no subsequent token at the time of
> its initial macro argument expansion, and similarly a macro parameter that is
> the last token of a replacement token list has no subsequent token at the time
> of that parameter's substitution. Similarly for first tokens and preceding
> tokens.

Naturally such a step can be treated as purely conceptual by a tokenized
implementation with combined preprocessing and lexical analysis, except for the
purposes of argument stringizing where the added spacing may be essential for
unambiguous identification of the preprocessing tokens involved. Such a
statement is not a substantive change, as it is merely clarifying the
tokenization rules, and given that Standard C has changed the definition of the
preprocessor substantially from K\&R already (re macro argument expansion before
substitution) such an additional explicit change from K\&R C should cause
comparatively little difficulty except to those who had not appreciated just how
different the preprocessing rules are already. Examples which are clarified by
this change are:

```c
#define    macro    +
            +macro
            macro+
  #define    mac()    +
 #define    ro       +
            mac()ro
```

all of which unambiguously result in lines with two `+` operator tokens, in
strict accordance with the draft standard's tokenization rules, and not, as was
formerly the case with traditional text oriented preprocessors, in single `++`
operators.

Examples which are changed by this statement are:

```c
#define    mac()         +
 #define    ro            +
 #define    str(s)        # s
 #define    eval(m,e)     m(e)
            eval( str, mac()ro )
```

which produces the string `"+N+"` and not the string `"++"` as it would do with
the draft's current wording.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous responses to this item from David F. Prosser. The Committee endorses
the substance of these responses, which follow: KR never specified the macro
replacement algorithm to the extent that any such conclusion is possible. The
widest range of implementation choices were present in this area of the
language. The eventual choice of a macro replacement algorithm was one that did
not match any existing implementation, but one that tried to include the
behavior of all major variants. You agree that the C Standard is clear that once
a token is recognized, it is never retokenized unless subjected to a `#` or `##`
operation. The behavior described is that which was chosen by the Committee.
Your proposal would cause, as you note, certain created string literals to
include white space not present in the original text. This runs counter to the
`#` operator's goal of producing a string version of the spelling of the
invocation arguments. The C Standard allows an implementation that uses a
text-to-text separate preprocessing stage the option to use white space as
necessary to separate tokens when it produces its output. However, this
insertion of white space must not be visible to the program. The proposed extra
white space would probably be a surprise to the programmer as well. Finally,
this proposal would require those implementations that have a built-in
preprocessing stage to add extra code to insert white space in special
circumstances. This is counter to the goal of having both built-in and separate
implementations be purely an implementation choice.
