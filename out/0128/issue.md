ANSI/ISO C Defect Report #rfg35:

Subject: Editorial issue relating to tag declarations in type specifiers.

Given the code:

```c
void example ()
        {
              {
              struct TAG {int i};
              }
              {
 		struct TAG object;	/* line 7 */
              }
        }
```

Does line 7 violate the semantic rule given at the very end of the semantics
sub-part of subclause 6.5, i.e., “If an identifier for an object is declared
with no linkage, the type for the object shall be complete by the end of its
declarator, ...”?

In other words, does `struct TAG` represent an incomplete type on line 7? (I
believe that the answer is “yes,” but the C Standard fails to make that entirely
clear.)

Background:

Subclause 6.5.2.3 says:

> If a type specifier of the form
> 
> > *struct-or-union identifier*
> 
> occurs prior to the declaration that defines the content, the structure or union
> is an incomplete type. It declares a tag that specifies a type that may be used
> only when the size of an object of the specified type is not needed.

These statements fail to take full account of scoping issues. The statements
quoted above should be rephrased to take scope issues into account, perhaps as
follows:

> If a type specifier of the form
> 
> > *struct-or-union identifier*
> 
> occurs within a given scope prior to another declaration (in the same scope) of
> the same identifier (which also declares the identifier to be a struct or union
> tag) or if such a type specifier occurs at some point within a given scope where
> no prior declaration of the same tag identifier is visible, then the type
> specifier declares the identifier to be a structure or union tag for an
> incomplete structure or union type (respectively). The type so declared may only
> be used when the size of an object of the specified type is not needed.
