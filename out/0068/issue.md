Item 5 \- handling of `char` values

Values of the type `char` must be treated as either “signed” or “nonnegative”
integers (subclause 6.1.2.5).

a. Is the treatment determined strictly by the value of the expression `CHAR_MAX
== SCHAR_MAX`?

b. If the treatment is as “signed” integers, does the type `char` behave in
every instance as the type `signed char` (though of course being a different
type)? If not, what are the differences?

c. If the treatment is as “nonnegative” integers, does the type `char` behave in
every instance as the type `unsigned char` (though of course being a different
type)? If not, what are the differences? In particular, do the "no overflow,
reduce modulo" semantics apply?
