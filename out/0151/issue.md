*This Defect Report was prompted by articles posted to comp.std.c by Bakul Shah,
Rex Jaeschke, and Soenke Behrens.*

DIN-002:

The C Standard's specification of what

```c
printf("%#.0o", 0);
```

outputs is ambiguous, and compiler vendors have indeed interpreted it
differently.

For a zero integer value, the descriptions of the `#` flag and the 0 precision
in subclause 7.9.6.1 contradict each other.

The `#` demands that the first digit be zero;

`#` The result is to be converted to an "alternate form." For `o` conversion, it
increases the precision, if and only if necessary, to force the first digit of
the result to be a zero.

But a precision of 0 demands that nothing at all be printed.

`o,u,x,X [...]` The result of converting a zero value with a precision of zero
is no characters.

In the hexadecimal case, the description of the `#` flag's effects has been
worded such that the conflict is avoided:

`# [...]` For `x` (or `X`) conversion, a nonzero result will have `0x` (or `0X`)
prefixed to it.

If it was intended that the octal case, too, should print nothing, this crucial
"nonzero" should be introduced into its description as well.

### Suggested Technical Corrigendum:

In subclause 7.9.6.1, replace:

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of the result to be a zero.

by:

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of a nonzero result to be a zero.
