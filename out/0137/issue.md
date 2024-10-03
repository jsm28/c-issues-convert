Is `printf("%.1f", -0.01)` required to produce `0.0`, `-0.0`, or are both
acceptable?

Subclause 7.9.6.1 says that when the `+` flag is not specified, the result
begins with a sign only when a negative value is converted. The description of
the `f` conversion (also `e` and `E`) says that the value is rounded to the
appropriate number of digits. Is the value used to determine the sign of the
result the value before or after rounding?
