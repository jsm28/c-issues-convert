## Issue 0105: Does a constraint violation win over undefined behavior?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.03](issue0017.03.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_105.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_105.html)

ANSI/ISO C Defect report #rfg12:

Subclause 6.5 says (in its **Constraints** section):

> All declarations in the same scope that refer to the same object or function
> shall specify compatible types.

However in subclause 6.1.2.6 we have the following rule:

> All declarations that refer to the same object or function shall have compatible
> type; otherwise the behavior is undefined.

There is a conflict between the meaning of these two rules. The former rule
indicates declaring something in two or more incompatible ways (in a given
scope) *must* cause a diagnostic, while the latter rule indicates that doing the
exact same thing may result in undefined behavior (i.e. possibly silent
acceptance of the code by the implementation). (Note that this same issue was
raised previously in the C Information Bulletin #1, [RFI #17, question
#3](issue0017.03.md). While the response to that question indicated that no change
was needed, a change *is* clearly need in order to resolve this ambiguity.)

Furthermore, the use of the term “refer to” in both of these rules seems both
unnecessary and potentially confusing. Why not just talk instead about
declarations “declaring” things, rather than “referring to” those things?

To eliminate the first problem I would suggest that the rules quoted above from
subclause 6.1.2.6 should be clarified as follows:

> If any pair of declarations of the same object or function which appear in
> different scopes declare the object or function in question to have two
> different incompatible types, the behavior is undefined.

(Actually the rule regarding declaration compatibility which now appears in
subclause 6.1.2.6 seems entirely misplaced anyway. Shouldn't it just be taken
out of subclause 6.1.2.6 and moved to the subclause on declarations, i.e.
subclause 6.5?)

---

Comment from WG14 on 1997-09-23:

### Response

This error was corrected in response to [Defect Report #017, Question
3](issue0017.03.md).
