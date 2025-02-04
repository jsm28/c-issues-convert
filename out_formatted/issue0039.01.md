## Issue 0039.01: Must `MB_CUR_MAX` be one in the `"C"` locale?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Vania Joloboff, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-061  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_039.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_039.html)

My interpretation of the Standard is that the value of `MB_CUR_MAX` must be one
in the `"C"` locale. I infer that from the fact that:

1. The characters in the `"C"` locale must be alphanumeric \+ space.
2. The `is`*`XXX`* functions specify character constant values for the `"C"` locale.
3. A character constant consists of one or more characters that are enclosed within apostrophes. A character is regarded as having type `char`.
4. The data type `char` consists of one byte of storage.

However this clarification should be made explicit.

---

Comment from WG14 on 1997-09-23:

### Response

In fact 3, we presume the second sentence was intended to be: “A character
*constant* is regarded as having type `char`,” in order to be applicable to this
request. That is not true; a character constant is of type `int`. Also facts 1-4
deal with the single-byte chars and not the extended character set.

In any case, the facts as listed do not logically lead to the conclusion that
`MB_CUR_MAX` must be one (1) in the `"C"` locale. In fact, this conclusion is
not true. It is possible for `MB_CUR_MAX` to be greater than one in the `"C"`
locale. In subclause 7.10, page 149, `MB_CUR_MAX` is “the maximum number of
bytes in a multibyte character for the extended character set specified by the
current locale.” In subclause 7.4.1.1, page 107, the `"C"` locale is “the
minimal environment for C translation.” The minimal environment may still
require more than one byte for multibyte characters.
