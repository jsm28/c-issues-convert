### Summary

The `offsetof` macro is specified in the normative text of the C11 standard in
**§7.19 Common Definitions `<stddef.h>`** as follows:

> The macros \[defined in the header `<stddef.h>`] are...
>
> > `offsetof(`*type*`,` *member-designator*`)`
>
> which expands to an integer constant expression that has type `size_t`, the
> value of which is the offset in bytes, to the structure member (designated by
> *member-designator*), from the beginning of its structure (designated by
> *type*). The type and member designator shall be such that given
>
> > ```c
> > static type t;
> > ```
>
> then the expression `&(t.`*member-designator*`)` evaluates to an address
> constant. (If the specified member is a bit-field, the behavior is undefined.)

In addition, undefined uses of the macro are mentioned in the informative **§J.2
Undefined Behavior** using the following words:

> — The member designator parameter of an `offsetof` macro is an invalid right
> operand of the `.` operator for the type parameter, or designates a bit-field
> (7.19).

A number of questions have been independently raised about this specification
over the years, both by C (and C\+\+) committee members and by implementers of
both languages (the C\+\+ defintion of the macro is largely equivalent to C's),
pointing out gaps or aspects lacking in clarity. Most recently some of the
questions were raised in the thread [(SC22WG14.13852) what's a
member-designator?](https://www.open-std.org/jtc1/sc22/wg14/13852) As a result
of the lack of clarity, implementations diverge in what `offsetof` expressions
they accept. In one case, an implementer of a compiler known for its conformance
and high quality of diagnostics interpreted the specification as restricting the
`member-designator` operand of the macro to ordinary identifiers and to the
exclusion of references to subobjects.

For example, given the following code:

> ```c
> struct A { int n, a [2]; };
> struct B { struct A a; };
>
> int noff = offsetof (struct B, a.n);
> int aoff = offsetof (struct B, a.a [1]);
> ```

this implemenation issues the diagnostics below.

> ```c
> warning: using extended field designator is an extension [-Wextended-offsetof]
> int noff = offsetof (struct B, a.n);
>            ^                    ~~
> warning: using extended field designator is an extension [-Wextended-offsetof]
> int aoff = offsetof (struct B, a.a [1]);
>            ^                    ~~~~~~
> ```

In other instances, some implementations reject the following example with an
error, indicating that they are not prepared to handle the `->` operator in this
context.

> ```c
> struct A { int i; };
> struct B { struct A a [1]; };
>
> int ioff = offsetof (struct B, a->i);
> ```

Some of the questions that have been identified are outlined in the following
list.

* In the specification, the *member-designator* operand is referred to as a
  *structure member*. Is this intended to include members of subobjects (members
  of structures other thant *type*, subobjects of which are members of *type*), or
  of and array elements as in the code examples above, or are the diagnostics
  required?
* The *type* operand is described as designating a structure. Is a *type* that
  that refers to a union not a valid operand? (No implementation has been observed
  to reject union operands.)
* Does C intend to permit defining a new type as the *type* operand? For example,
  is the following a well-formed expression? (No implementation has been observed
  to reject such operands.)

  > ```c
  > offsetof (struct A { int i; }, i)
  > ```
* If C does intend to permit defining a new type in `offsetof` expressions, does
  it intend to permit defining arbitrarily complex types such as the one below?
  (No implementation is known to accept the definition of a type containing commas
  since they are interpreted by the preprocessor as separating macro arguments.
  But since implementations often define the `offsetof` macro in terms of a
  built-in function, it would be possible to implement each as a variadic macro
  and function, respectively, and handle this corner case. This isn't a question
  about whether it would be worthwhile to do so but rather about whether the
  standard text can be interpreted so as to require implementers to accept this
  admittedly unusual case.)

  > ```c
  > offsetof (struct A { struct B { int i, j; } b [1]; }, b->j)
  > ```

Some of the same questions and others were summarized a number of years ago by
Joseph Myers in his paper on
[`offsetof`](https://www.polyomino.org.uk/computer/c/pre-dr-3.txt). Althugh
Joseph chose not to submit the paper to WG14 we believe many are still relevant
and should be dealt with by clarifying the text of the standard.
