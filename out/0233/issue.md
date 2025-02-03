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
