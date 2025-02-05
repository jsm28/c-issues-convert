### Summary

The requirements of subclause 7.18.4.1 may be impossible to satisfy (for *N* \=
8 or 16, typically) unless an implementation has special (non-standard) support
for integer constants of types `char` and `short`:

> The macro `INT`*N*`_C(`*value* `)` shall expand to a signed integer constant
> with the specified value and type `int_least`*N*`_t`.

(Similarly for `UINT`*N*`_C`.) The paragraph preceding this overly restrictive
specification reflects the actual intent:

> ... a type with at least the specified width.

**Possible Solutions**

1. Change "integer constant" to "integer constant expression". While this still does not reflect the original intent, at least it permits accurate implementation without special support from the compiler.
2. Specify that the type shall be the promoted type corresponding to `int_least`*N*`_t`.
3. Specify that the type shall be any appropriately signed integer type of sufficient width.

**Suggested Technical Correction**  
In subclause 7.18.4.1 paragraph 2, change the two occurrences of "and type" to
"and \[un\]signed integer type at least as wide as".
