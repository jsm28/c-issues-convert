## Issue 0209: Problem implementing `INT`*N*`_C` macros

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Douglas A. Gwyn (J11)  
Date: 1999-10-19  
Reference document: [ISO/IEC WG14 N896](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n896.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC1  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_209.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_209.htm)

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

---

Comment from WG14 on 2000-11-02:

### Technical Corrigendum

7.18.4 Macros for integer constants

> \[#1\] The following function-like macros<sup>220</sup> expand to integer
> constant expressions suitable for initializing objects that have integer types
> corresponding to types defined in \<`stdint.h`\>. Each macro name corresponds to
> a similar type name in 7.18.1.2 or 7.18.1.5.
>
> \[#2\] The argument in any instance of these macros shall be a decimal, octal,
> or hexadecimal constant (as defined in 6.4.4.1) with a value that does not
> exceed the limits for the corresponding type.

Add:

> \[#3\] Each invocation of one of these macros shall expand to an integer
> constant expression suitable for use in `#if` preprocessing directives. The type
> of the expression shall have the same type as would an expression that is an
> object of the corresponding type converted according to the integer promotions.
> The value of the expression shall be that of the argument.

*Most of the following wording is taken almost exactly from* `<limits.h>`

7.18.4.1 Macros for minimum-width integer constants

Remove:

> \[#1\] Each of the following macros expands to an integer constant having the
> value specified by its argument and a type with at least the specified
> width.<sup>221</sup>)
>
> <sup>221</sup> For each name described in 7.18.1.2 that the implementation
> provides, the corresponding macro in this subclause is required.

Change \[#2\] to:

> \[#2\] The macro `INT`*N*`_C(`*value* `)` shall expand to an integer constant
> expression corresponding to the type `int_least`*N*`_t`. The macro
> `UINT`*N*`_C(`*value* `)` shall expand to an integer constant expression
> corresponding to the type `uint_least`*N*`_t`. For example, if `uint_least64_t`
> is a name for the type `unsigned long long int`, then `UINT64_C(0x123)` might
> expand to the integer constant `0x123ULL`.

7.18.4.2 Macros for greatest-width integer constants

> \[#1\] The following macro expands to an integer constant expression having the
> value specified by its argument and the type `intmax_t`:
>
> > `INTMAX_C(`*value*`)`
>
> The following macro expands to an integer constant expression having the value
> specified by its argument and the type `uintmax_t`:
>
> > `UINTMAX_C(`*value*`)`
