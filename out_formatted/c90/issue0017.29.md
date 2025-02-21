## Issue 0017.29: When does conversion failure occur in floating-point `fscanf` input?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Conversion failure and longest matches

Consider `1.2e+4` with field width of 5\. Is it input item `1.2e+` that gives a
conversion failure? What is the ordering between building input items and
converting them? Do they run in parallel, or sequential?

Refer to subclause 7.9.6.2 **The `fscanf` function**, page 135, lines 31-33
concerning the longest matching sequence, and subclause 7.9.6.2, page 137, lines
15-16 concerning a conflicting input character.

For `1.2e-x,` is `1.2` or `1.2e-` read?

The above questions all come about because of page 137, line 15: “If conversion
terminates ...” In this context the use of the word “conversion” could be
referring to the process of turning a sequence of characters into numeric form.
I believe what was intended was “If a conversion specifier terminates ...”

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 7.9.6.2, page 137, lines 15-16:

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.

and subclause 7.9.6.2, page 135, lines 31-33:

An input item is defined as the longest matching sequence of input characters,
unless that exceeds a specified field width, in which case it is the initial
subsequence of that length in the sequence.

and subclause 7.9.6.2, page 135, lines 38-40:

If the input item is not a matching sequence, the execution of the directive
fails: this condition is a matching failure.

The “conversion” in the first quoted passage is the process of both forming an
input item and converting it as specified by the conversion specifier.

About your example: If the characters available for input are “ `1.2e+4`” and
input is performed using a “`%5e`,” then the input item is “`1.2e+`” as defined
by the second passage quoted above. That input item is not a matching sequence,
but only an initial subsequence that fails to be a matching sequence in its own
right. Under the rules of the third quoted passage, this is a matching failure.

Note that in this case, no characters were pushed back onto the input stream.
There was no “conflicting input character” that terminated the field, and so the
first quoted passage does not apply.

See the Correction made in response to Defect Report #022, Question 1, for
additional clarification.
