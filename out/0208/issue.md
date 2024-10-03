### Summary

When there is more than one initializer for the same object it is not clear
whether both initializers are actually evaluated. Wording changes are proposed
to clarify this.

### Details

Subclause 6.7.8 paragraph 19 reads:

> The initialization shall occur in initializer list order, each initializer
> provided for a particular subobject overriding any previously listed initializer
> for the same subobject; all subobjects that are not initialized explicitly shall
> be initialized implicitly the same as objects that have static storage duration.

Paragraph 23 reads:

> The order in which any side effects occur among the initialization list
> expressions is unspecified.

If the same object is initialized twice, as in:

> ```c
> int a [2] = { f (0), f (1), [0] = f (2) };
> ```

the term "overriding" could be taken to mean that the first initializer is
ignored completely, or it could be taken to mean that the expression is
evaluated and then discarded. The proposed wording change assumes the latter.

### Suggested Technical Corrigendum

Replace 6.7.8 paragraph 23 with:

> All the initialization list expressions are evaluated, even if the resulting
> value will be overridden, but the order in which any side effects occur is
> unspecified.
