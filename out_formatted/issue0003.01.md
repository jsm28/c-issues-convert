## Issue 0003.01: Are preprocessing numbers too inclusive?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.1.8: Preprocessing numbers I note from the rationale document of
November 1988, X3J11 Document Number 88-151, that the following problem has been
observed. I am surprised at the Committee's decision to allow such a loose
description. Under the grammar given for a `pp-number`

```c
0xEE+23     0x7E+macro      0x100E+value-macro
```

are preprocessing numbers and as such a conforming C compiler would be required
to generate an error when it failed to successfully convert them to actual C
language number tokens. The solution is simply to restrict the inclusion of
\[`eE`]\[`+-`] within a *`pp-number`* to situations where the `e` or `E` is the
first *`non-digit`* in the character sequence composing the preprocessing
number. This can be easily implemented in a variety of methods; the informal
description above gives perhaps a better guide to efficient implementation than
the following revised grammar:

```c
pp-number:
         pp-float
         pp-number digit
          pp-number .
         pp-number non-digit  /* A non-digit is a letter or underscore */

 pp-float:
         pp-real
         pp-real E sign         pp-real e sign

 pp-real:
         digit
         .
         pp-real digit
         pp-real .
```

It is unbelievable that a standards committee could so lose sight of its
objective that it would, in full awareness, make simple expressions illegal.

To illustrate the absurdity of the rationale document's claim that the faulty
grammar was felt to be easier to implement, why not adopt the following grammar
for a *`pp-number`* and really make life simple; after all, who wants to have
their preprocessor slowed down by checking whether the `+` or `-` was preceded
by a n `e`or an `E`?

```c
pp-number:
         digit
         .
         pp-number digit
         pp-number .
         pp-number non-digit
         pp-number sign
```

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous responses to this item from David F. Prosser. The Committee endorses
the substance of these responses, which follow: In response to your first
suggested grammar: This grammar doesn't include all valid numeric constants and
exclude other important tokens. For example, `.` is derivable. But let's assume
that you intended something like

```c
pp-number:
         pp-float
         digit
         pp-number digit
         pp-number non-digit

 pp-float:
         pp-real
         pp-float E sign
         pp-float e sign
         pp-float digit
         pp-float .
         pp-float non-digit

 pp-real:
         digit
         . digit
         pp-real digit
         pp-real .
```

This grammar is certainly more complicated than the one-level construction in
the C Standard, and consequently harder to understand. That's a strike against
it. Another strike is that, while it does mimic the two major numeric
categories, it still doesn't include all sequences covered by the existing
grammar, save those that would otherwise be valid by the stricter tokenization
rules. For example, `0b0101e+17` might be someone's future notion of a binary
floating constant. Finally, it suffers from a great deal of reduce/reduce
conflicts, making the implementation and specification less likely to be
understood and implemented as intended. In response to your second suggested
grammar: This could have been done. But the Committee chose a compromise at a
different point \- one that restricts the inappropriate gobbling of characters
to `+` and `-` immediately after `E` or `e`. This was all that was necessary to
cover all valid numeric constants in as simple a grammar as was possible. For
more background, you'd need to know the state of the proposed standard a few
years before this grammar was voted in. The Committee had stated its intent that
“garbage” character sequences that began like a numeric constant were to be
tokenized as a single sequence. This was to prevent situations in which this
“garbage” would be turned into valid C code through obscure macro replacements,
among more minor reasons. This was, unfortunately, very poorly stated in the
draft. As I recall, it was placed in the constraints for subclause 6.1. It was
something like “Each pair of adjacent tokens that are both keywords,
identifiers, and/or constants must be separated by white space.” \[As “improved”
for the May 1, 1986 draft proposed standard, subclause 6.1 **Constraints**
consisted of the single sentence: “Each keyword, identifier, or constant shall
be separated by some white space from any otherwise adjacent keyword,
identifier, or constant.”] As you can see, this constraint neither presented the
intent of the Committee nor caused implementations to behave in any sort of
consistent manner with respect to tokenization. Finally a letter writer
understood the issue well enough to suggest a grammar along the lines of the
current subclause 6.1.8. It, contrary to your opening remarks on this topic, is
*not* a “loose description,” and it finally stated in a precise way the intent
of the tokenization rules. The benefits of this construction were that all
tokenization for all implementations would now be the same, no “garbage”
character sequences would be able to be converted to valid C code, skipped
blocks of code could silently be scanned without generating needless and
unnecessary tokenization errors, the preprocessing tokenization of numeric
tokens would be greatly simplified, and room for future expansion of C's numeric
tokens was reserved. That's a lot of good. The down side was that certain
sequences now would require some white space to cause them to be tokenized as
the programmer intended. As noted in the rationale document, there are other
parts in C that require white space for tokenization to be controlled, and this
was found to be one more. Since the “mistokenization” of such sequences must
result in some diagnostic noise from the compiler, and since the fix is so mild,
the Committee agreed that the proposed standard is still much better with this
grammar than with any of the other suggestions. Personally, I think that the
biggest surprise “win” was the reservation of future numeric token “name space.”
I would not be at all surprised to find binary constants (that begin with `0b`)
in newer C implementations.
