### Summary

What is the value of: `_Bool b = 0.0 + 3.0*I;`

I believe that there is a contradiction between **6.3.1.2 Boolean type** and
**6.3.1.7 Real and complex** in that one requires that the value to be 1 and the
other requires the value to be 0\.

> **6.3.1.2 Boolean type**
>
> 1 When any scalar value is converted to **\_Bool**, the result is 0 if the value
> compares equal to 0; otherwise, the result is 1\.
>
> **6.3.1.7 Real and complex**
>
> 2 When a value of complex type is converted to a real type, the imaginary part
> of the complex value is discarded and the value of the real part is converted
> according to the conversion rules for the corresponding real type.

DR 285 against C99 had a similar issue on conversion from imaginary to boolean.
That resulted in:

> **G.4.2 Real and imaginary**
>
> 1 When a value of imaginary type is converted to a real type other than
> **\_Bool**,376) the result is a positive zero.
>
> 376\) See 6.3.1.2.

### Suggested Technical Corrigendum

I believe that **6.3.1.7 Real and complex**, paragraph 2 should be changed to:

> 2 When a value of complex type is converted to a real type other than
> **\_Bool**(footnote), the imaginary part of the complex value is discarded and
> the value of the real part is converted according to the conversion rules for
> the corresponding real type.
>
> (footnote) See 6.3.1.2.
