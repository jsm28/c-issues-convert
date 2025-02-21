## Issue 0233: `%g`, `%G` precision specification

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Chris Torek, Project Editor (Larry Jones)  
Date: 2000-04-24  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_233.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_233.htm)

### Summary

7.19.6.1 (and similarly in 7.24.2.1):

> `g,G`
>
> > A `double` argument representing a floating-point number is converted in style
> > `f` or `e` (or in style `F` or `E` in the case of a `G` conversion specifier),
> > with the precision specifying the number of significant digits. If the precision
> > is zero, it is taken as 1\. The style used depends on the value converted; style
> > `e` (or `E`) is used only if the exponent resulting from such a conversion is
> > less than -4 or greater than or equal to the precision. Trailing zeros are
> > removed from the fractional portion of the result unless the `#` flag is
> > specified; a decimal-point character appears only if it is followed by a digit.
> >
> > A `double` argument representing an infinity or NaN is converted in the style of
> > an `f` or `F` conversion specifier.

Assuming "significant digits" is being used in the scientific-notation sense.
This means that, for instance, the number "12.34" has four significant digits.
So does "0.1234", and so does "0.001234". A value like "1.200" also has four
significant digits, counting trailing zeros, but not leading zeros.

Now, `%g` normally suppresses trailing zeros (as described above), so applying
`%.4g` to the value 1.2 produces not "1.200" but rather just "1.2". The `#`
modifier, however, stops the trailing-zero suppression, and:

> ```c
> printf("%#.4g\n", 1.2);
> ```

must produce "1.200", four significant digits.

The problem occurs when we go to print the value 0.0. No matter how many digits
we tack on the end, we still have no significant digits. So what should:

> ```c
> printf("%#.4g\n", 0.0);
> ```

print? "0.0000" has no significant digits. "0.0" has no significant digits.
"0.000000000000000000000000000000000000000" still has no significant digits.
Which of these, if any, is correct output? Which of these is *desirable* output?

The only way this wording makes any sense is if "significant digits" means
something else entirely, but then what does it mean?

---

Comment from WG14 on 2007-09-07:

### Committee Discussion (for history only)

There seemed to be some uncertainty about whether (for the `%.4g` example) the
exponent would be `0` or `1`. This could yield different results.

Some Committee members wondered whether the exponent would be `1` or `0` for
ZERO. The bullet describing `e, E` is clear on this though "If the value is
zero, the exponent is zero".

If there is no implementation representation of ZERO, but rather a very small
number. In this case, we generally thought that this was a user problem, that
they could not rely on a true ZERO having a representation, in which case, they
would need to place their own checks for what approximations were acceptable as
ZERO and print a literal instead.

Some pathological cases were checked, and appeared to work correctly.

NOTE: In discussion, the original bullets were:

* if X \< -4 or X \>\= P, the conversion is with style e (or E) and precision P \- 1
* otherwise the conversion is with style f (or F) and precision P \- ( X \+ 1 )

But these were changed to:

* if P \> X \>\= -4, the conversion is with style f (or F) and precision P \- ( X \+ 1 )
* otherwise the conversion is with style e (or E) and precision P \- 1

During discussion, as it was considered to be the more pure form.

---

Comment from WG14 on 2007-09-07:

### Technical Corrigendum

Change 7.19.6.1 paragraph 8 and 7.24.2.1 paragraph 8 to:

> `g,G`
>
> > A `double` argument representing a floating-point number is converted in style
> > `f` or `e` (or in style `F` or `E` in the case of a `G` conversion specifier),
> > depending on the value converted and the precision. Let `P` equal the precision
> > if non-zero, 6 if the precision is omitted, or 1 if the precision is zero. Then,
> > if a conversion with style `E` would have an exponent of `X`:
> >
> > * if `P > X >= -4`, the conversion is with style `f` (or `F`) and precision `P - (X + 1)`.
> > * otherwise the conversion is with style `e` (or `E`) and precision `P - 1`.
>
> Finally, unless the `#` flag is used, any trailing zeroes are removed from the
> fractional portion of the result and the decimal-point character is removed if
> there is no fractional portion remaining.
