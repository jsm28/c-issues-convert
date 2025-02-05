ANSI/ISO C Defect report #rfg13:

Subclause 6.2.2.2 says:

> The (nonexistent) value of a *void expression* (an expression that has type
> `void`) shall not be used in any way, ...

There are two separate (but related) problems with this rule.

First, it is not entirely clear what constitutes a “use” of a value (or of an
expression). In which lines of the following code is a type `void` value
actually “used?”

```c
void example(void *pv, int i)
        {
        &*pv;            /* ? */
        *pv;             /* ? */
        i ? *pv : *pv;   /* ? */
        *pv, *pv;        /* ? */
        }
```

(The answer to this question will determine which of the above lines cause
undefined behavior, and which cause well defined behavior.)

If one or more of the (questionable) lines from the above example are judged by
the Committee to result in well defined behavior, then a second (separate) issue
arises. This second issue requires some explaining.

Subclause 6.2.2.1 contains the following rules:

> An *lvalue* is an expression (with an object type or an incomplete type other
> than `void`) ...
>
> Except when it is the operand of the `sizeof` operator, the unary `&` operator,
> the `++` operator, the `--` operator, or the left operand of the `.` operator or
> an assignment operator, an lvalue that does not have array type is converted to
> the value stored in the designated object (and is no longer an lvalue)... If the
> lvalue has an incomplete type and does not have array type, the behavior is
> undefined.

Note that the final rule (specifying a condition under which undefined behavior
arises) seems, based upon the context, to only apply to those cases in which
“...an lvalue that does not have an array type is converted to the value...”
More specifically, it appears that undefined behavior is *not* necessarily
produced for non-lvalue expressions (appearing in the indicated contexts).

Furthermore, it should be noted that the definition of an lvalue (quoted above)
*does not include* all void types. Rather, it only includes *the* `void` type.

The result is that the indicated lines in following example would seem to yield
well defined behavior (or at least they *will* yield well defined behavior if
the Committee decides that their unqualified counterparts do), however I suspect
that this may not have been what the Committee intended.

```c
void example(const void *pcv, volatile void *pvv, int i)
        {
        &*pcv;              /* ? */
        *pcv;               /* ? */
        i ? *pcv : *pcv;    /* ? */
        *pcv, *pcv;         /* ? */

        &*pvv;              /* ? */
        *pvv;               /* ? */
        i ? *pvv : *pvv;    /* ? */
        *pvv, *pvv;         /* ? */
        }
```

In summary, I would ask that the Committee comment upon and/or clarify the
behavior produced by each of the examples shown herein. Separately, I would
request that the Committee make changes in the existing C Standard in order to
make the rules applicable to such cases more readily apparent.
