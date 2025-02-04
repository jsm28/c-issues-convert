## Issue 0098: Do function types and incomplete type have size?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_098.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_098.html)

ANSI/ISO C Defect report #rfg5:

Subclause 6.3.3.4 provides the following constraint:

> The `sizeof` operator shall not be applied to an expression that has function
> type or an incomplete type...

The logical implication of this constraint is that neither function types nor
incomplete types have “sizes” per se, at least not as far as the C Standard is
concerned.

I have noted however that neither subclause 6.3.2.4 **Postfix increment and
decrement operators** nor subclause 6.3.3.1 **Prefix increment and decrement
operators** contain any constraints which would prohibit the incrementing or
decrementing of pointers to function types or pointers to incomplete types.

I believe that this logical inconsistency needs to be addressed (and rectified)
in the C Standard. It seems that the most appropriate way to do this is to add
the following additional constraint to subclause 6.3.2.4:

> The operand of the postfix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.

Likewise, the following new constraint should be added to subclause 6.3.3.1:

> The operand of the prefix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.

---

Comment from WG14 on 1997-09-23:

### Response

The explicit constraint on pre/post increment/decrement operators (subclauses
6.3.2.4 and 6.3.3.1) is not required. Early on, the Committee decided that if a
behavior was described as being equivalent to another construct, all of the
constraints of that construct would apply. This “chaining” process means that
any violation of a constraint in any section referred to explicitly or by the
phrases “equivalent behavior” or “as if” will generate a diagnostic.

Both subclauses 6.3.2.4 and 6.3.3.1 state in their respective **Semantics**
sections, “See the discussions of additive operators and compound assignment for
information on constraints, types, \[side effects,] and conversions and the
effects of operations on pointers.”

The **Semantics** section of subclause 6.3.16.2 states, “A *compound assignment*
of the form `E1` *`op`*`= E2` differs from the simple assignment expression `E1
= E1` *`op`* `(E2)` only in that the lvalue `E1` is evaluated only once.”

This makes the pre/post increment/decrement equivalent to adding or subtracting
1 to/from an object. Looking at subclause 6.3.6 for the constraints on additive
operators, in each case which refers to pointer operands, the C Standard uses
the phrase “pointer to an object type.” Since incomplete types and function
types are not object types, their use as operands of these operators is
precluded.
