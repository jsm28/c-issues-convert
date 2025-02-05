### Summary

I suspect that this was introduced as a result of a public comment from someone
who was confused (honestly or perversely) about 6.10.3.4p1: "**After all
parameters in the replacement list have been substituted,** the resulting
preprocessing token sequence is rescanned *...*" (emphasis added). This clearly
describes the rescanning of function-like macros, but because of the reference
to parameters, may be taken as not applying to object-like macros.

### Suggested Technical Corrigendum

Add a new sentence to the end of 6.10.3p9:

> A preprocessing directive of the form
>
> > ```c
> > # define identifier replacement-list new-line
> > ```
>
> defines an object-like macro that causes each subsequent instance of the macro
> name<sup>145\)</sup> to be replaced by the replacement list of preprocessing
> tokens that constitute the remainder of the directive. <ins>The replacement list
> is then rescanned for more macro names as specified below.</ins>
