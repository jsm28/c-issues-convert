## Issue 0159: Is the introduction to the C Standard confusing?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_159.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_159.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.* Defect
Report UK 007: Consistency of the C Standard Defects exist in the way the
Standard refers to itself.

**Part 1**

The introduction to the C Standard reads in part:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.

While it is not, strictly speaking, an inconsistency for text that is not part
of the C Standard to specify which text is part of the C Standard, it is
confusing for this to be the case when other text that *looks* like part of the
C Standard isn't \- the examples and footnotes.

In particular, placing this information \- necessary for interpreting the text
of the C Standard itself \- outside that text causes a danger that, when some
other document is produced that purports to contain the full text of the C
Standard, the Introduction will be omitted while the footnotes and examples are
retained. A reader of such a document who is not aware of the text of the
introduction will then be misled as to the C Standard's contents. Whilst this is
not the responsibility of ISO, it is another reason for regularizing the
situation.

Note that this has definitely happened in the case of *The Annotated ANSI C
Standard* by Herbert Schildt, and I have been informed (but have not confirmed)
that it has also happened with the version of the C Standard distributed by the
Australian National Body.

**Part 2**

The introduction to the C Standard reads in part:

The language clause (clause 7\) ... The library clause (clause 8\) ...

These references are wrong.

### Suggested Technical Corrigendum:

In the Introduction, change:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.

The language clause (clause 7\) ...

The library clause (clause 8\) ...

to:

As specified in the definitions and conventions clause (clause 3), this
introduction, the examples, the footnotes, the references, and the annexes are
not part of this International Standard.

The language clause (clause 6\) ...

The library clause (clause 7\) ...

Insert at the start of clause 3:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.
