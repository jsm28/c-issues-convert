## Issue 0061: Interpretation of white space in the format string of a scan statement

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ed Bendickson, X3 Secretariat (USA)  
Date: 1993-08-19  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_061.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_061.html)

I am requesting an interpretation of white space in the format string of a scan
statement. One of our customers is concerned about this as it appears to
conflict with some books on C. I am referring to subclause 7.9.6.2, page 135,
paragraph 3:

> A directive composed of white space character(s) is executed by reading input up
> to the first non-white-space character (which remains unread), or until no more
> characters can be read.

Page 135, paragraph 7 says:

> If the length of the input item is zero, the execution of the directive fails:
> this condition is a matching failure, unless an error prevented input from the
> stream, in which case it is an input failure.

My questions are:

1. Is white space in the format string a directive which must be satisfied by white space in the input string?
2. What are the correct answers to the following examples? Note the white space in the format string.

Example 1:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu %ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 1?

Example 2:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu%ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 2?

---

Comment from WG14 on 1997-09-23:

### Response

A directive composed of one or more white-space characters can successfully
match zero white-space characters in the input stream. The paragraphs that
intervene between your two quotations make clear that the second paragraph
applies only to a directive that is a conversion specification.

Thus, both examples should assign 2 to `numAssigned`.
