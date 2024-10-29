### Summary

What is a **directive name**? What are the semantics of a **\# non-directive**?

In particular, what should happen for a translation unit with these four lines:

> ```c
> # non-directive
> # "Long string"
> # 'Many characters are implementation defined'
> # 1234
> ```

The syntax in **6.10 Preprocessing directives** has in group-part:

> \# non-directive

The C standard section 6.10, paragraph 3 has:

> A non-directive shall not begin with any of the directive names appearing in the
> syntax.

I find that confusing as **directive name** is only used in the C standard in
6.10 paragraphs 3 and 4 (without any definition). So, what is a **directive
name**?

Assuming **directive name** is one of:

* if
* ifdef
* ifndef
* elif
* else
* endif
* include
* define
* undef
* line
* error
* pragma

then my four line program contains lines that are

> \# non-directive

so should be valid. However, almost every C compiler I have tried considers them
errors that end translation. I did find at least one C compiler that ignored
them (treated them as comments). I did find at least one C compiler that
considered them errors even inside of:

> ```c
> #if 0
> #endif
> ```

where they should have been ignored.

I believe that gcc treats

> ```c
> # 1234
> ```

the same as:

> ```c
> # line 1234
> ```

I see no semantics for non-directive. So, what is supposed to happen with them?
Is it implicitly undefined?

Since preprocessing directives (which includes non-directive) are deleted at the
end of translation phase 4, these non-directives could act as comments.

DRs 231 and 250 appear to contradict each other on what happens with a
non-directive and neither refers to the other.

[DR 231](issue:0231) Says that text-line and non-directive are not
implementation defined. They are placeholders in the phases of translation and
are subject to normal processing in subsequent phases of translation. And that
words were supposed to be added to the Rationale.

[DR 250](issue:0250) Says that non-directive is a preprocessing directive. And,
it added that as a footnote in 6.10.3#11

Neither DR added normative words.

In answering this, we should consider what happens with mis-spellings, such as:

* #endf
* #deifine

Should **\# non-directive** be a comment (and ignored)? Implementation defined?
An error that ends translation (like #error)? Undefined behaviour?

### Suggested Technical Corrigendum

Since I do not know what should happen, I have none. But, if we decide on
undefined behaviour, I would like that as explicit words.