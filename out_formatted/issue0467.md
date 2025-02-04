## Issue 0467: maximum representable finite description vs math

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2014-09-26  
Reference document: [N1870,](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1870.htm) [N1871](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1871.htm)  
Submitted against: C11 / C17  
Status: Closed  
Cross-references: [0432](issue0432.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

formula for maximum representable finite (normalized) floating-point numbers in
5.2.4.2.2#12, and epsilon floating-point numbers in 5.2.4.2.2#13.

### Details

The math formula is for a normalized number, while the words are missing
'normalized'. Now, in the floating-point model in paragraph 2, the maximum
finite number is the same as the maximum finite normalized number, so it did not
matter.

However, if long double is a pair of doubles (not matching the model in
paragraph 2), then there can be finite numbers larger than the largest
normalized finite number. The largest normalized finite number is
DBL\_MAX\*(1.\+DBL\_EPSILON/2.), while the largest finite number can be
DBL\_MAX\*2.

Also, if long double is a pair of doubles (not matching the model in paragraph
2), then 'least value greater than 1 that is representable in the given floating
point type' is (for double) 1.0\+DBL\_TRUE\_MIN. That makes the difference
DBL\_TRUE\_MIN, which is not the same at the math formula (b to the power
(1-p)).

### Suggested Technical Corrigendum

In 5.2.4.2.2#13, add 'normalized' between 'least' and 'value'.

In 5.2.4.2.2#12, add 'normalized' between 'finite' and 'floating-point'.

Add a new paragraph:

12b The values given in the following list shall be replaced by constant
expressions with implementation-defined values that are greater than or equal to
those shown:

\-- maximum representable finite floating-point number (footnote),

* **FLT\_TRUE\_MAX 1E\+37**
* **DBL\_TRUE\_MAX 1E\+37**
* **LDBL\_TRUE\_MAX 1E\+37**

(footnote): Need not be normalized.

---

Comment from WG14 on 2018-10-18:

Oct 2014 meeting

### Committee Discussion

> The committee accepts the correction of "normalized" but concludes that adding
> the suggested macros is a feature and out of scope for a DR.

Oct 2015 meeting

### Committee Discussion

> There has been discussion of this Proposed Technical Corrigendum on the WG 14
> email reflector starting with [(SC22WG14.13764)
> LDBL\_MAX](https://www.open-std.org/jtc1/sc22/wg14/13764) suggesting that since
> `double double` implementations do not follow (nor are provided by) the IEEE
> model that the implementation is free to define additional macros to describe
> the behavior as they see fit. To some degree a consensus on LDBL\_MAX was
> formed, and the following words are provided as food for further committee
> thought.
>
> > In 5.2.4.2.2#12, first item change the phrase
> >
> > maximum representable finite floating-point number, \[math formula]
> >
> > to
> >
> > maximum representable finite floating-point number; if that value is normalized,
> > its value is \[math formula]

Apr 2016 meeting

### Committee Discussion

> The committee agrees with the reflector discussion.

Apr 2017 meeting

### Committee Discussion

> Additional input to the Proposed Technical Corrigendum was suggested and adopted
> by the committee from [DR 467
> PTC](https://www.open-std.org/jtc1/sc22/wg14/14655).
>
> Further, after discussion, the change from [DR 432](issue0432.md) is now viewed as
> necessary but not sufficient, and so it will be further reviewed before being
> incorporated into a future version of the standard along with these changes.

### Proposed Change

In §5.2.4.2.2#1 after the definition of the floating point model parameters,
add:

> For each floating-point type: *b*, *e<sub>min</sub>*, *e<sub>max</sub>*, *p* are
> fixed constants.

In §5.2.4.2.2#3 change:

> In addition to normalized floating-point numbers ( *f<sub>1</sub>* \> 0 if *x* ≠
> 0),

to:

> In addition to *normalized floating-point numbers* ( *f<sub>1</sub>* \> 0 if *x*
> ≠ 0), all possible *f<sub>k</sub>* digits result in values representable in the
> type<sup>footnote</sup>.
>
> <sup>footnote</sup>: Some implementations may have types with numeric values
> which are not covered by this model.

In 5.2.4.2.2#12, first item change the phrase

> maximum representable finite floating-point number, \[ math formula ]

to

> maximum representable finite floating-point number; if that value is normalized,
> its value is \[ math formula ],

In 5.2.4.2.2#13, first item change the phrase

> the difference between 1 and the least value greater than 1

to

> the difference between 1 and the least normalized value greater than 1

Oct 2018 meeting

### Committee Response

> The "C17" edition of the standard has been published as IS 9899:2018.
>
> This issue was not resolved in that publication.
>
> The committee is now considering changes for the next revision of the standard,
> and asks that this proposed change and that from [CR 432](issue0432.md) be
> combined in a new paper to completely resolve this issue.
