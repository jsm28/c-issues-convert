# Embedded C TR 18037:2004: issue log

**This issue log has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|[0EMB.01](../embc2004/log.md#issue0EMB.01)|Name conflict for strtok|Fixed in Embedded C TR 18037:2008|
|[0EMB.02](../embc2004/log.md#issue0EMB.02)|Order in which overflow handling and rounding is done|Fixed in Embedded C TR 18037:2008|
|[0EMB.03](../embc2004/log.md#issue0EMB.03)|Typo in 4.1.6.2.1 \- Binary arithmetic operations|Fixed in Embedded C TR 18037:2008|
|[0EMB.04](../embc2004/log.md#issue0EMB.04)|Type generic macro's|Fixed in Embedded C TR 18037:2008|
|[0EMB.05](../embc2004/log.md#issue0EMB.05)|Typo in new text for 6.2.6.3|Fixed in Embedded C TR 18037:2008|
|[0EMB.06](../embc2004/log.md#issue0EMB.06)|fp arithmetic support functions do not specify what happens if an integer result overflows|Fixed in Embedded C TR 18037:2008|
|[0EMB.07](../embc2004/log.md#issue0EMB.07)|Error in 7.18.a.6.3|Fixed in Embedded C TR 18037:2008|
|[0EMB.08](../embc2004/log.md#issue0EMB.08)|Diagnostic required on named-register constraint violation?|Fixed in Embedded C TR 18037:2008|
|[0EMB.09](../embc2004/log.md#issue0EMB.09)|Effective type definition (aka US-40)|Fixed in Embedded C TR 18037:2008|
|[0EMB.10](../embc2004/log.md#issue0EMB.10)|The relationship beween named-registers and external object definitions|Closed|
|[0EMB.11](../embc2004/log.md#issue0EMB.11)|Initialization of global named-registers|Fixed in Embedded C TR 18037:2008|
|[0EMB.12](../embc2004/log.md#issue0EMB.12)|Address space qualifier in specifier-qualifier-list|Fixed in Embedded C TR 18037:2008|
|[0EMB.13](../embc2004/log.md#issue0EMB.13)|\[Embedded C 2004 DR#13\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.14](../embc2004/log.md#issue0EMB.14)|\[Embedded C 2004 DR#14\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.15](../embc2004/log.md#issue0EMB.15)|\[Embedded C 2004 DR#15\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.16](../embc2004/log.md#issue0EMB.16)|\[Embedded C 2004 DR#16\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.17](../embc2004/log.md#issue0EMB.17)|\[Embedded C 2004 DR#17\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.18](../embc2004/log.md#issue0EMB.18)|\[Embedded C 2004 DR#18\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.19](../embc2004/log.md#issue0EMB.19)|\[Embedded C 2004 DR#19\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.20](../embc2004/log.md#issue0EMB.20)|\[Embedded C 2004 DR#20\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.21](../embc2004/log.md#issue0EMB.21)|\[Embedded C 2004 DR#21\]|Fixed in Embedded C TR 18037:2008|
|[0EMB.22](../embc2004/log.md#issue0EMB.22)|\[Embedded C 2004 DR#22\]|Fixed in Embedded C TR 18037:2008|

---

<div id="issue0EMB.01">

## Issue 0EMB.01: Name conflict for strtok

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [188](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/188), [189](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/189), [190](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/190), [191](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/191), [192](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/192), [194](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/194), [196](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/196), [198](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/198), [200](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/200), [201](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/201), [203](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/203), [204](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/204), [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: by selecting the letter 'k' as suffix for the accum type, the the
function to convert a string to an accum type gets the name strtok; this name is
already in use in the C standard. Possible solutions:

* use a different letter
  + 'q' as proposed originally, conflicts with quadruple precision format
  + 'y' the only reasonable choice of the 'free' letters (others are 'b', 'm', 'v' and 'w');
* change the names of all "strto" functions to "strto\_"; that is: "strtok" becomes "strto\_k", "strtoht" becomes "strto\_hr", etc. Easy to do but a little bit inconsistent with the C library;
* use the letter 'q' only for the functionnames, leave the 'k' everywhere else.

---

Comment from WG14 on 2004-11-15:

Problem: Using the suffix 'k' to stand for 'accum' with the base 'strto' for
numeric conversion functions yields a conflict with the existing C function
'strtok'.

Solution: Rename the fixed-point numeric conversion functions to have a base of
'strtofx' instead of 'strto'. The new names will be 'strtofxhr', 'strtofxr',
'strtofxlr', 'strtofxhk', 'strtofxk', 'strtofxlk', 'strtofxuhr', 'strtofxur',
'strtofxulr', 'strtofxuhk', 'strtofxuk', and 'strtofxulk'.

Affected sections in TR18037: 4.1.7 (2 times), 4.1.9, replacement text for
7.18a.6.8 (many times), replacement text for 7.19.6.2 para 12\.


</div>


---

---

<div id="issue0EMB.02">

## Issue 0EMB.02: Order in which overflow handling and rounding is done

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the current text requires that overflow handling is done before
rounding; this is counter intuitive, and not what is done for floating-point
overflow/rounding. As it happens, the order in which overflow and rounding are
done has no effect on the result when saturation is used for overflow handling.

Hence, if we change the order, the result remains the same for saturation.
However, with the current required order, mod\_wrap as overflow handling (which
is allowed but not required) cannot (reasonably) be implemented. It is therefore
proposed to change the order.

Proposed solution: change the required order of overflow handling and rounding.

---

Comment from WG14 on 2004-11-15:

Problem: TR 18037 requires that overflow handling be done before rounding, which
causes problems for alternative overflow modes such as modular wraparound. (When
the overflow mode is saturation, the order in which rounding and overflow
handling are performed has no effect on the end-result.)

Solution: Specify that rounding should be done before overflow handling.

Changes:

* Clause 4.1.3, para 3: strike '(after any overflow handling)'.
* Replacement text for 5.2.4.2.3:
  + Replace in para 6 (staring with 'If the result type of an arithmetic operation') the text 'and then overflow handling and rounding' by 'and then rounding and overflow handling'
  + Strike from para 9 (starting with 'If (after any overflow handling)') the text '(after any overflow handling)'


</div>


---

---

<div id="issue0EMB.03">

## Issue 0EMB.03: Typo in 4.1.6.2.1 \- Binary arithmetic operations

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [206](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/206)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: 4.1.6.2.1 (Binary arithmetic operations), last para, the text on
the divi fuctions has 'yielding a fixed-point type result'; this must be
'yielding an integer type result'.

Proposed solution: obvious

---

Comment from WG14 on 2004-11-15:

Problem: 4.1.6.2.1 (Binary arithmetic operations), last para, the text on the
divi functions has 'yielding a fixed-point type result' while the divi functions
have an integer result.

Solution: Change 'yielding a fixed-point type result'; this must be 'yielding an
integer type result'

Change: Modify 4.1.6.2.1 para 5 accordingly.


</div>


---

---

<div id="issue0EMB.04">

## Issue 0EMB.04: Type generic macro's

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [211](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/211)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: The type-generic macro definition sections (2.1.7.6 and 7.18a.6.7)
are incomplete and possibly wrong.

Incomplete because there are no rules on which function should be called when a
type- generic macro is called with a non fixed-point type argument. Possibly
wrong, because it is not clear what the name of the type-generic macro's should
be: 2.1.7.6 suggest to call the type-generic abs function 'absfx', in 7.18a.6.7
the 'fx' part of the name is in italic which might suggest that the name should
really be 'abs'. So, do we want to have 'abs', 'round' and 'countls', or
'absfx', 'roundfx' and 'countls'?

Proposed solution:

---

Comment from WG14 on 2004-11-15:

Problem: The type-generic macro definition sections (4.1.7.6 and 7.18a.6.7) are
incomplete and possibly wrong (see N1071 for more information)

Solution: The generic function names should be 'absfx', 'countlsfx' and
'roundfx'; 7.18a.6.7 should better explain which underlying functions are
selected.

Changes: in the replacement text for 7.18a.6.7:

* Change the type font for 'fx' from bold italic to bold (3 times)
* Add to 7.18a.6.7:
  > For each macro, use of the macro invokes the function whose corresponding real
  > type and type domain is the real type of the first generic argument. If the real
  > type of the first generic argument is not a fixed-point type, the behavior is
  > undefined.


</div>


---

---

<div id="issue0EMB.05">

## Issue 0EMB.05: Typo in new text for 6.2.6.3

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [206](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/206)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the new text for clause 6.2.6.3, 3rd para, last sentence: replace
'integer types' by 'fixed-point types' twice.

Proposed solution: obvious

---

Comment from WG14 on 2004-11-15:

Problem: The replacement text for 6.2.6.3 para 3, last sentence says 'integer
types' while it should say 'fixed-point types' (twice).

Solution: Make the change

Change: Replace the last sentence of the replacement text for 6.2.6.3 para 3
with: The width of a fixed-point type is the same but including any sign bit;
thus for unsigned fixed-point types the two values are the same, while for
signed fixed-point types the width is one greater than the precision.


</div>


---

---

<div id="issue0EMB.06">

## Issue 0EMB.06: fp arithmetic support functions do not specify what happens if an integer result overflows

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: 7.18a.6.1 (fp arithmetic support functions) does not specify what
happens if an integer result overflows.

Proposed solution: Isn't there a blanket statement to the effect that when a
specified result is not representable in the type, the behavior is undefined? If
not, there should be.

---

Comment from WG14 on 2004-11-15:

Problem: The replacement text for 7.18a.6.1 (on fixed-point arithmetic support
functions) does not specify what happens if an integer result overflows.

Solution: Undefined behavior is implied by default in the C standard. Mention in
the descriptive text that this should result in undefined behavior.

Change: In 4.1.6.2.1 para 5, add the following sentence to the end of the
paragraph: If an integer result of one of these functions overflows, the
behavior is undefined.


</div>


---

---

<div id="issue0EMB.07">

## Issue 0EMB.07: Error in 7.18.a.6.3

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the rounding functions in 7.18a.6.3 require that

> Fractional bits beyond the rounding point are set to zero in the result.

This should not apply when saturation has occurred.

Proposed solution: replace the offending text by:

> When saturation has not occurred, fractional bits beyond the rounding point are
> set to zero in the result.

---

Comment from WG14 on 2004-11-15:

Problem: The description of the fixed-point rounding functions in the
replacement text for 7.18a.6.3 require that fractional bits beyond the rounding
point are set to zero in the result. This should not apply when saturation has
occurred.

Solution: Replace the text as proposed.

Change: Modify the third sentence of the description of 7.18a.6.3 to read: 'When
saturation has not occurred, fractional bits beyond the rounding point are set
to zero in the result.'


</div>


---

---

<div id="issue0EMB.08">

## Issue 0EMB.08: Diagnostic required on named-register constraint violation?

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: consider

```c
// file 1
register REG_A int reg_a;

// file 2
extern int reg_a;

int main() { return reg_a; }
```

According to the new constraints for 6.7.1 this is not allowed:

> If an object is declared with a named-register storage-class specifier, every
> declaration of that object shall include the same named-register storage-class
> specifier.

The 'shall' implies that a diagnostic is required here. However, so far C
compilers have not been required to diagnose such issues across translation
units. Is this really the intention?

Proposed solution:

---

Comment from WG14 on 2004-11-15:

Problem: Consider

```c
// file 1
register REG_A int reg_a;

// file 2
extern int reg_a;
int main() { return reg_a; }
```

According to the second new constraints for 6.7.1 this is not allowed:

> If an object is declared with a named-register storage-class specifier, every
> declaration of that object shall include the same named-register storage-class
> specifier.

The 'shall' implies that a diagnostic is required here. However, so far C
compilers have not been required to diagnose such issues across translation
units. Is this really the intention?

Solution: The intent is to require a diagnostic for different named-register
storage-class specifier declarations within a single translation unit for the
same object.

Changes:

* Change in the second of the new constraint paragraphs for 6.7.1 the words 'every declaration of that object' to 'every declaration of that object within the same translation unit'.
* In the new text for 6.7.1.1, add at the beginning of the last paragraph (paragraph 6\) the sentence: 'If an object is declared with a named-register storage-class specifier, every declaration of that object shall include the same named-register storage-class specifier.'


</div>


---

---

<div id="issue0EMB.09">

## Issue 0EMB.09: Effective type definition (aka US-40)

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [184](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/184), [195](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/195), [199](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/199), [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: a couple of the statements concerning effective types in 6.5 of the
C Standard are not exactly correct in the presence of address-space qualifiers.
The easiest fix is probably to modify the concept of *effective type* in the C
Standard so as not to include an address-space qualifier. (The whole concept of
*effective type* is used only in 6.5 and in one footnote elsewhere in the C
Standard.)

Possible solution: add the following section to clause 5.3 of TR 18037:

> **Clause 6.5 \- Expressions**, replace the first two sentences of paragraph 6
> with: The *effective type* of an object for an access to its stored value is the
> declared type of the object, if any, without any address-space qualifier that
> the declared type may have.<sup>72\)</sup> If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue, without any address-space qualifier, becomes
> the effective type of the object for that access and for subsequent accesses
> that do not modify the stored value.

and remove the notion *additionally access-qualified version* from TR 18037
(first replacement paragraph of paragraph 26 of 6.2.5, replacement text for
paragraph 7 of 6.5).

---

Comment from WG14 on 2004-11-15:

Problem: If \_X and \_Y are address spaces with \_Y enclosing \_X, after the
declarations

```c
_X char a;


_Y char *p = &a;
```

the dereference \*p is undefined because of the way TR 18037 applies the notion
of effective type (C Standard 6.5, paragraphs 6 and 7). This makes overlapping
named address spaces unusable by strictly conforming code in most circumstances.

Solution: In the detailed changes to the C Standard, modify the definition of
*effective type* (clause 6.5, paragraph 6\) to exclude address space qualifiers,
and restore the rules in paragraph 7 to their original form. (Note that the
whole concept of *effective type* is used only in 6.5 and in one footnote
elsewhere in the C Standard.) This makes TR 18037's definition of *additionally
access-qualified version* of a type (in the new text for 6.2.5) unnecessary.

Changes: Change the replacement text for clause 6.5 of the C Standard to the
following:

> **Clause 6.5 \- Expressions**, replace the first two sentences of paragraph 6
> with:
>
> The *effective type* of an object for an access to its stored value is the
> declared type of the object, if any, without any address-space qualifier that
> the declared type may have.<sup>72\)</sup> If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue, without any address-space qualifier, becomes
> the effective type of the object for that access and for subsequent accesses
> that do not modify the stored value.

Remove the sentence defining *additionally access-qualified version* from TR
18037 (first paragraph replacing paragraph 26 of 6.2.5).


</div>


---

---

<div id="issue0EMB.10">

## Issue 0EMB.10: The relationship beween named-registers and external object definitions

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Status: Closed  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the relationship beween named-registers and 6.9.2 (external object
definitions) need to specified: when there is no initializer in the
named-register declaration, the declaration is not an external definition for
the identifier. The declaration is however also not a tentative definition,
because it has a storage-class specifier. Then, what is it?

Proposed solution: That's one problem with using existing syntactic categories
for new facilities. A workaround would be to change storage-class-specifier to
storage-class- specifier\|whatever in the grammar, where "whatever" is some new
category, and then adjust the text that constrains storage-class-specifier to
say the right thing (just storage-class-specifier or
storage-class-specifier\|whatever, depending). Then the construct would not have
a storage-class-specifier and thus would be a tentative definition.

---

Comment from WG14 on 2004-11-15:

After close reading during the meeting it appeared that Issue 10 of N1071 was
not a defect. The number is maintained for consistency with N1071.


</div>


---

---

<div id="issue0EMB.11">

## Issue 0EMB.11: Initialization of global named-registers

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [209](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/209), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: the current specification allows global named-registers to be
initialized:

```c
register REG_A int reg_a = 32;
```

It is however unclear when, and by whom this initialization should be done (one
could imagine that the register storage onto which the variable maps does not
really exist until some device is initialized by some user code).

Proposed solution: disallow initializers on named-register variables.

---

Comment from WG14 on 2004-11-15:

Problem: The current specification allows global named-registers to be
initialized. It is however unclear when, and by whom this initialization should
be done (one could imagine that the register storage onto which the variable
maps does not really exist until some device is initialized by some user code).

Solution: Disallow initializers on named-register variables.

Change: Add the following new constraint to section 6.7: 'A declaration
containing a named- register storage-class specifier shall not contain an
initializer.'


</div>


---

---

<div id="issue0EMB.12">

## Issue 0EMB.12: Address space qualifier in specifier-qualifier-list

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: in the new text for 6.7.2.1, the TR adds a constraint:

> The *specifier-qualifier-list* in the declaration of a member of a structure or
> union shall not include an address space qualifier.

This is a mistake, because it keeps us from declaring something innocuous like

```c
struct onePointer { _X int *pX; };
```

As written, the constraint would make the member declaration invalid, whereas we
only intended to prohibit declarations such as this:

```c
struct oneInteger { _X int iX; };
```

Proposed solution: change the constraint to be:

> Within a structure or union specifier, the type of a member shall not be
> qualified by an address space qualifier.

---

Comment from WG14 on 2004-11-15:

Problem: The new text for 6.7.2.1, requires that a specifier-qualifier-list in
the declaration of a member of a structure or union shall not include an address
space qualifier. This disallows for instance the type of a member of structure
to be a pointer into a named address space.

Solution: The intention was to disallow members of a single structure/union to
have different address qualifiers.

Change: Modify the constraint for 6.7.2.1 to be: 'Within a structure or union
specifier, the type of a member shall not be qualified by an address space
qualifier.'


</div>


---

---

<div id="issue0EMB.13">

## Issue 0EMB.13: \[Embedded C 2004 DR#13\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: TR 18037 does not alter the definition of integer constant expression
in para 6 of 6.6.

Solution: This is an oversight which, for consistency reasons, should be
corrected.

Change: Add new replacement text for 6.6 to change the first sentence of para 6
as follows: insert before 'and floating' the text 'fixed-point constants that
are the immediate operand of casts'


</div>


---

---

<div id="issue0EMB.14">

## Issue 0EMB.14: \[Embedded C 2004 DR#14\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: The new text for 6.5.8 (relational operators) and 6.5.9 (equality
operators) add as a constraint: 'If the two operands are pointers into different
address spaces, the address spaces must overlap.'. Such a constraint is missing
for 6.5.6 (additive operators), where it is relevant for pointer subtraction.

Solution: Add the requested constraint.

Change: Add the following constraint to 6.5.6 : 'For subtraction, if the two
operands are pointers into different address spaces, the address spaces must
overlap.'


</div>


---

---

<div id="issue0EMB.15">

## Issue 0EMB.15: \[Embedded C 2004 DR#15\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: The third sentence of para 5 of 4.1.6.2.1 start with 'The generic
function names ...'; the word 'generic' might cause confusion with
'type-generic'.

Solution: Change 'generic function names' to just 'names'.

Change: Modify 4.1.6.2.1 para 5 third sentence accordingly.


</div>


---

---

<div id="issue0EMB.16">

## Issue 0EMB.16: \[Embedded C 2004 DR#16\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: The first sentence of 4.1.6.2.1 para 5 (' According to the rules above,
the result type of an arithmetic operation where (at least) one operand has a
fixed-point type is always a fixed- point type.') is wrong as it does not take
operands with floating-point type into account.

Solution: As it is the intention to only discuss integer types and fixed-point
types in this paragraph, change the sentence accordingly.

Change: Modify the first sentence of 4.1.6.2.1 para 5 to read: 'According to the
rules above, the result type of an arithmetic operation where one operand has a
fixed-point type and the other operand has an integer or a fixed-point type is
always a fixed-point type.'


</div>


---

---

<div id="issue0EMB.17">

## Issue 0EMB.17: \[Embedded C 2004 DR#17\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: TR 18037 has in many places the text fragment 'overflow and rounding',
but has also the text 'rounding and overflow'.

Solution: Defect 2 has established that the required order is first to do
rounding and then to do overflow handling; make the text consistent by replacing
the text fragment 'overflow and rounding' by 'rounding and overflow' throughout
the document.

Change: Make the required change in many places (including the title of 4.1.3
and A.4).


</div>


---

---

<div id="issue0EMB.18">

## Issue 0EMB.18: \[Embedded C 2004 DR#18\]

Authors: WG14  
Date: 2004-11-15  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: In 6.5, the first sentence of the replacement text for the description
section of 7.8a.4.6 lists a number of functions. The second sentence of the same
paragraph has a similar list of functions that should be in the same order as in
the first sentence, but which is not.

Solution: Reorder the list in the second sentence.

Change: Change in 6.5 (detailed changes for the Basic I/O Hardware Addressing)
the second sentence of the description section in 7.8a.4.6 to start with: ' The
functions are equivalent to ioand, ioor, ioxor, ioandl, ioorl, and ioxorl,
respectively, ...'.


</div>


---

---

<div id="issue0EMB.19">

## Issue 0EMB.19: \[Embedded C 2004 DR#19\]

Authors: WG14  
Date: 2005-03-03  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: Sec 7.18a.2 introduces a set of typedefs, and describes a convention
for the return type of bits'*fx*': either int\_*fx*\_t, or uint\_*fx*\_t.

Sec 7.18a.6.5 lists the 12 functions for bits'*fx*', all of which make use of
the form 'int\_*fx*\_t'. According to 7.18a.2 the last six should be of the form
'uint\_*fx*\_t'.

Solution: change the last 6 function prototypes in the Synopsis of 7.18a.6.5 to:

```c
uint_uhr_t bitsuhr(unsigned short fract f);
uint_ur_t bitsur(unsigned fract f);
uint_ulr_t bitsulr(unsigned long fract f);
uint_uhk_t bitsuhk(unsigned short accum f);
uint_uk_t bitsuk(unsigned accum f);
uint_ulk_t bitsulk(unsigned long accum f);
```


</div>


---

---

<div id="issue0EMB.20">

## Issue 0EMB.20: \[Embedded C 2004 DR#20\]

Authors: WG14  
Date: 2005-03-03  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: the text on the countls function in 4.1.7.3 and 7.18a.6.4 reads:

> The integer return value of the above functions is defined as follows:
>
> * if the value of the fixed-point argument f is non-zero, the return value is the largest integer k for which the expression f\<\<k does not overflow;
> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N-1, where N is the total number of (nonpadding) bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N-1.

In the 'argument is zero' case, for a signed fixed-point type, the notion
'nonpadding bits' includes the sign bit (see 6.2.6.3); this implies that the N
for signed types is one larger that the N for the corresponding unsigned types;
this is wrong (it suggests that shifting into the sign bit does not generate an
overflow). In stead of '(nonpadding) bits', the notion 'value bits' should be
used.

Solution: in 4.1.7.3 and 7.18a.6.4, replace in the 2nd bullet '(nonpadding)' by
'value'.


</div>


---

---

<div id="issue0EMB.21">

## Issue 0EMB.21: \[Embedded C 2004 DR#21\]

Authors: WG14  
Date: 2005-03-03  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: the text on the countls function in 4.1.7.3 and 7.18a.6.4 reads:

> The integer return value of the above functions is defined as follows:
>
> * if the value of the fixed-point argument f is non-zero, the return value is the largest integer k for which the expression f\<\<k does not overflow;
> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N-1, where N is the total number of (nonpadding) bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N-1.

From the definition it is clear that for instance

```c
    countlsur( UFRACT_EPSILON ) == (UFRACT_FBIT - 1)
```

and

```c
    countlsk ( ACCUM_EPSILON ) == (ACCUM_IBIT + ACCUM_FBIT - 1)
```

If the text '(nonpadding) bits' is replaced by 'value bits' (see Defect 20),
then the text requires that

```c
    countlsr( 0.0r ) >= (N - 1)
```

where the latter value equals countls( FRACT\_EPSILON ). This seems
counterintuitive; one would expect the value of countlsr( 0.0r ) to be one less
than countls( FRACT\_EPSILON ).

Solution: change in 4.1.7.3 and 7.18a.6.4 the text of the 2nd bullet and the
Note as follows:

> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N, where N is the total number of value bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N.


</div>


---

---

<div id="issue0EMB.22">

## Issue 0EMB.22: \[Embedded C 2004 DR#22\]

Authors: WG14  
Date: 2005-03-03  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: the bitwise integer to fixed-point functions (in 7.18a.6.6) do not use
the int\_*fx*\_t and uint\_*fx*\_t integer types; the text in 4.1.7.5 is already
correct.

Solution:

* change the Synopsis section of 7.18a.6.6 to read:

  ```c
  #include <stdfix.h>
  short fract hrbits(int_hr_t n);
  fract rbits(int_r_t n);
  long fract lrbits(int_lr_t n);
  short accum hkbits(int_hk_t n);
  accum kbits(int_k_t n);
  long accum lkbits(int_lk_t n);
  unsigned short fract uhrbits(uint_uhr_t n);
  unsigned fract urbits(uint_ur_t n);
  unsigned long fract ulrbits(uint_ulr_t n);
  unsigned short accum uhkbits(uint_uhk_t n);
  unsigned accum ukbits(uint_uk_t n);
  unsigned long accum ulkbits(uint_ulk_t n);
  ```
* remove from the of 7.18a.2 the words 'as return types'
* change in 7.18a.2 the first sentence after the list to read:

  The integer types **int\_*fx*\_t** and **uint\_*fx*\_t** are the return types of
  the corresponding **bits*fx*** functions and are chosen so that the return value
  can hold all the necessary bits; the ***fx*****bits** functions use these
  integer types as types for their parameters.


</div>


---

