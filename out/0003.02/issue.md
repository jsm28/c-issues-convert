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
