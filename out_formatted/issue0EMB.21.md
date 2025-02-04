## Issue 0EMB.21: \[Embedded C 2004 DR#21]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2005-03-03  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: the text on the countls function in 4.1.7.3 and 7.18a.6.4 reads:

> The integer return value of the above functions is defined as follows:
>
> * if the value of the fixed-point argument f is non-zero, the return value is the largest integer k for which the expression f\<\<k does not overflow;
> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N-1, where N is the total number of (nonpadding) bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N-1.

From the definition it is clear that for instance

```c
    countlsur( UFRACT_EPSILON ) == (UFRACT_FBIT - 1)
```

and

```c
    countlsk ( ACCUM_EPSILON ) == (ACCUM_IBIT + ACCUM_FBIT - 1)
```

If the text '(nonpadding) bits' is replaced by 'value bits' (see Defect 20),
then the text requires that

```c
    countlsr( 0.0r ) >= (N - 1)
```

where the latter value equals countls( FRACT\_EPSILON ). This seems
counterintuitive; one would expect the value of countlsr( 0.0r ) to be one less
than countls( FRACT\_EPSILON ).

Solution: change in 4.1.7.3 and 7.18a.6.4 the text of the 2nd bullet and the
Note as follows:

> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N, where N is the total number of value bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N.
