### Summary

There is an implication at various points in the standard, notably the copysign
function, that infinities and NaNs have signs. This is not the case in all
implementations, and this needs to be allowed for.

### Suggested Technical Corrigendum

Add a new paragraph to 5.2.4.2.2, preferably after \[#3]:

> \[#3a] An implementation may give zero and non-numeric values (such as
> infinities and `NaNs`) a sign or may leave them unsigned. Wherever such values
> are unsigned, any requirement in this International Standard to retrieve the
> sign shall act as if the value were positive, and any requirement to set the
> sign shall be ignored.

or:

> \[...]  
> to retrieve the sign shall produce an unspecified sign, and any requirement to
> set the sign shall be ignored.
