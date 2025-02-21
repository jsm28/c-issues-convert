## Issue 0017.10: When is the `sizeof` an object needed?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

When is `sizeof` needed?

Refer to subclause 6.5.2.3, page 62, lines 28-29. When is the size of an
incomplete structure needed? An interpreter may not need the size until run
time, while some strictly typed memory architecture may not even allow pointers
to structures of unknown size.

In subclause 6.5.2.3, Footnote 63 starts off as an example. The last sentence
contains a “shall.” Does a violation of this “shall” constitute undefined
behavior?

Even though an interpreter may not need the size of a structure until run time
its compiler still has to do some checking, i.e. an unexecuted statement may
contain `sizeof` an incomplete type; even though the statement is unexecuted the
constraint still has to be detected.

---

Comment from WG14 on 1997-09-23:

### Response

Whether the language processor is an interpreter or a true compiler does not
affect the language rules about when the size of an object is needed. Both a
compiler and an interpreter must act as if the translation phases in subclause
5.1.1.2 were followed. This is a requirement that an implementation act as if
the entire program is translated before the program's execution.

The “shall” in Footnote 63 in subclause 6.5.2.3 carries no special meaning: this
footnote, like all other footnotes in the standard, is provided to emphasize the
consequences of the rules in the standard. The footnote is not part of the
standard.

The Committee believes that a careful reading of the standard shows all of the
places that the size of an object is needed, and that the translation phases
prevent those requirements from being relaxed by an implementation.
