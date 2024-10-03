**Summary:** Is an implementation permitted to return an empty string for
`strerror()`?

This is a potential defect forwarded from the Austin Group. Is an implementation
of strerror permitted to return an empty string if there is no associated error
message for the given `errnum`?

The C Standard, although not perfectly clear, strongly implies that the string
returned by `strerror()` cannot be empty. The C Standard says

> `strerror` shall map any value of type `int` to a message.

It doesn't state that the message cannot be empty, but the fact that it uses the
word "message" means that any interpretation that allows this message to be
empty would also have to allow the diagnostic messages produced by the compiler
to be empty. Clearly such an interpretation is very much not intended. Note that
the relationship between the term "diagnostic message" and the "message"
produced by `strerror()` is clear from section 3.10:

> **diagnostic message**  
> message belonging to an implementation-defined subset of the implementation's
> message output

On the other hand, some have argued that "An implementation-defined subset" does
not preclude the empty string from being included in the set of messages,
provided the implementation has defined the error that equates to the message.

### Suggested Technical Corrigendum

Clarification Required.

Change 7.21.6.2, p2 from:

> The strerror function maps the number in `errnum` to a message string.
> Typically, the values for `errnum` come from `errno`, but `strerror()` shall map
> any value of type `int` to a message.

To:

> The strerror function maps the number in `errnum` to a message string. If the
> value of `errnum` is a valid error number, the message string shall indicate
> what error occurred; otherwise, if this functions completes successfully, the
> message string shall indicate that an unknown error occurred. Typically, the
> values for `errnum` come from `errno`, but strerror shall map any value of type
> int to a message.
