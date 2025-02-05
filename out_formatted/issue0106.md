## Issue 0106: Can one take the address of a void expression?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0012](issue0012.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_106.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_106.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

In the first function called `example`, the expression statement `&*pv` is dealt
with in [Defect Report #012](issue0012.md). The remaining three statements are
well formed. See the last sentence of the cited reference and also subclause
6.6.3.

In the second function called `example`, the expression statements `&*pcv` and
`&*pvv` are dealt with in [Defect Report #012](issue0012.md). The remaining six
statements are well formed. The restrictions given in subclause 6.5.3 apply to
object types, not incomplete types.
