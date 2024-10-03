Mapping of escape sequences

Refer to subclause 6.1.3.4, page 29, line 12 and line 16\. Are these values the
values in the source or execution character set?

When subclause 6.1.3.4, page 29, line 24 says: “The value of an ...,” is this
“value” the value in the source character set of the escape sequence or the
value of the mapped escape sequence? I would have said that the “value” is the
value in the execution environment since in the source environment `\x123` is
part of a token.

It might be argued that characters in the source character set do not have
values and thus no misinterpretation of “value” can occur. Subclause 5.2.1, page
10, lines 25-26 refer to the value of a character in the source basic character
set.
