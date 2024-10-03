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
