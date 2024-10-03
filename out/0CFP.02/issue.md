### Summary

### Summary

Page 38: The C 7.12.13a subclause heading is “Functions that round result to
narrower type” and this is the way the functions in the subclause are referred
to throughout the TS. In some cases, the functions in the subclause round their
result to a type that isn’t really narrower than the parameter types. For
example, this is true for the functions **daddl**, **dsubl**, etc. if the **long
double** and **double** types have the same width (as is allowed). (With the
extended types introduced in TS 18661-3, the destination type might be wider, as
it might for **f32xaddf64**.)

The current way of referencing these functions reflects the usual situation, and
is perhaps a helpful way of think about them generally. With a note about the
uncharacteristic cases, it seems unlike to cause significant confusion. Also,
changing all the references to these functions would be a large editorial
undertaking, spanning multiple parts of the TS. Confusion could easily arise
from having an inconsistent set of documents.

### Suggested Technical Corrigendum

Page 38: After the C 7.12.13a subclause heading, insert the following paragraph:

> \[1] The functions in this subclause round their results to a type typically
> narrower than the parameter types.

Page 40: After the change to C ending with “7.12.13a.6 Square root rounded to
narrower type ... \[3] These functions return the square root of x, rounded to
the type of the function.”, insert the following:

> In 7.12.13a #1, attach a footnote to the wording:
> 
> > typically narrower
> 
> where the footnote is:
> 
> > \*) In some cases the destination type might not be narrower than the parameter
> > types. For example, **double** might not be narrower than **long double**.
