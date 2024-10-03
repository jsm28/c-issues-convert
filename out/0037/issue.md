Subclause 5.2.1.2 **Multibyte characters** states:

> The source character set may contain multibyte characters, used to represent
> members of the extended character set. The execution character set may also
> contain multibyte characters, which need not have the same encoding as for the
> source character set. For both character sets, the following shall hold:
> 
> \- The single-byte characters defined in 5.2.1 shall be present.

and, a bit later on:

> \- A byte with all bits zero shall not occur in the second or subsequent bytes
> of a multibyte character.

My interpretation (and all of the experts that I consulted with) of the first
rule, is that the basic character set (A-z, 0-9, etc.) shall be coded in
one-byte code. All multibyte locales that I know (EUC variants, SJIS) follow
this rule. But I may still be wrong.

If the above is true, then both 10646 (other than CM 5\) and UNICODE fail this
rule and cannot be used as multibyte characters. UNICODE also fails the second
rule.
