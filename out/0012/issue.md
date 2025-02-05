Bug in Standard C

I was asked a question about the validity of various expressions. Among the list
there was the following:

```c
void *p; &*p;
```

After doing a quick pass through the standard, I found nothing that disallowed
such. Moreover, back in September 1987's meeting (I didn't just recall the date
... it took a while to find when it occurred), I distinctly remember a Committee
discussion that involved the validity of the expression above. It was as a
result of this discussion and vote that the draft was changed to allow the
above.

Anyway, I wrote back that the expression was valid. This was eventually followed
by a letter from Dennis \[Ritchie\] pointing out the mistake I made. As it turns
out, the definition of lvalue makes at least the unary `&` part of the above a
constraint violation. (As Bill \[Plauger\] would say, “I know what the standard
was *supposed* to specify.”)

This would be just another, “Oops, well I guess I can live with it” surprise in
the standard, except that it turns out that unary `&` of a `void` type is
useful! What it provides is a construction that gives C a notion of an address
symbol. You are familiar with the symbols that are created by the UNIX linker:
`etext`, `e data`, and `end`, which designate special addresses within the `a.o
ut`'s address space. Of these, the last is most useful (it gives the beginning
of the dynamically allocated data space). However, the *type* for these symbols
was always pretty fuzzy. But, consider a declaration of `end` as

```c
extern void end;
```

What this gives is a name that only has an address \- exactly what these symbols
do, and nothing more. They can only be used in C as the operand of unary `&`,
and the address must be converted to something else (say, `char *`) even to do
address calculation, making the special nature of the symbol clearly evident.

What I'd like is a vote of the interpretations group that notes that the intent
of the Committee was that “`void *p; &*p;`” was supposed to be valid, even
though a conforming implementation must diagnose the expression. This means that
I can continue to suggest the “`extern void`” approach to address symbols in C.

P.S.: The following is my reply to Dennis's mail that pointed out the error with
my original interpretation. The indented parts are from Dennis's mail.

> I don't agree with Dave P's answer about “`void *vp; &*vp;`.” There is not a
> constraint on `*`, but the subclause 6.3.3.2 semantics say, “... if it \[the
> operand of `*`\] points to an object, the result is an lvalue designating the
> object.” Does `vp` point to an object? An object is “a region of data storage
> ... the contents of which can represent values” (clause 3). Dicey at best.

I took some time looking into my records of the Committee's thoughts on this
very issue. Back in '87, based on a proposal by Plauger, the Committee voted 27
to 3 that “`*(void *)`” was not to be an error. This was when the unary `*`
constraint was simplified to the current form. Since `void` is a special
instance of an incomplete object type, it can be thought of as pointing at an
object whose size we do not know, but I agree that the argument is strained. I
would still recommend that the compiler not produce a hard error in this
situation.

> Moreover, the operand of `&` must be an lvalue, and `*vp` is certainly not an
> lvalue (subclause 6.2.2.1): “An *lvalue* is an expression (with an object type
> or an incomplete type other than `void`) ...”

Oops. In this case, I completely agree with Dennis: the standard does say that
unary `&` should not be applied to an expression with type `void` since such
cannot be an lvalue. Unfortunately, this means that the standard is “broken,” at
least according to the Committee's decisions. One of the major arguments
presented as part of the September 1987 meeting for allowing “`*(void *)`” was
that it could then be immediately used as the operand of unary `&`!

Therefore, I can state that back in 1987, the Committee's intent was that the
examples you gave were valid Standard C, but that the standard as written does
not allow the second half of the construction for `void`! Nevertheless, I'd
still suggest allowing the code to successfully compile, with at most a warning.
