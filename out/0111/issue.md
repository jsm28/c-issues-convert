ANSI/ISO C Defect report #rfg18:

Subject: Conversion of pointer-to-qualified type values to type `(void*)`
values.

Does the following code involve usage which requires a diagnostic from a
standard conforming implementation?

```c
const char *ccp;
 void *vp;

 void test ()
        {
 	vp = ccp;	/* diagnostic required? */
        }
```

With respect to this example, the following quotations are relevant.

Subclause 6.2.2.3:

> A pointer to `void` may be converted to or from a pointer to any incomplete or
> object type.

Subclause 6.3.16.1 (**Constraints**):

> One of the following shall hold:
>
> ...
>
> \- both operands are pointers to qualified or unqualified versions of compatible
> types, and the type pointed to by the left has all the qualifiers of the type
> pointed to by the right;
>
> \- one operand is a pointer to an object or incomplete type and the other is a
> pointer to a qualified or unqualified version of `void`, and the type pointed to
> by the left has all the qualifiers of the type pointed to by the right; ...

The rule specified in subclause 6.2.2.3 (and quoted above) makes it unclear
whether a value of some pointer-to-qualified-object type may be *first*
implicitly converted to type `(void*)` and then assigned to a type `(void*)`
variable, or whether such implicit conversion only takes place as an integral
part of an otherwise valid assignment operation.

If the former interpretation of subclause 6.2.2.3 is correct, then the above
code example is valid, and no diagnostic is required. If, however, the latter
interpretation is the correct one, then the code example shown above fails to
meet the constraints of subclause 6.3.16.1, and (thus) a diagnostic is required.
