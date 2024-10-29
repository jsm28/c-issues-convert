### Summary

Section 7.28.1 describes the function c16rtomb(). In particular, it states "When
c16 is not a valid wide character, an encoding error occurs". "wide character"
is defined in section 3.7.3 as "value representable by an object of type
wchar\_t, capable of representing any character in the current locale". This
wording seems to imply that, e.g. for the common cases (e.g, an implementation
that defines \_\_STDC\_UTF\_16\_\_ and a program that uses an UTF-8 locale),
c16rtomb() will return -1 when it encounters a character that is encoded as
multiple char16\_t (for UTF-16 a wide character can be encoded as a surrogate
pair consisting of two char16\_t). In particular, c16rtomb() will not be able to
process strings generated by mbrtoc16().

I would like to implement a standard-conforming c16rtomb() for SDCC, that allows
conversion from all of UTF-16 (not just the basic multilingual plane) to UTF-8.
It seems to me that this is currently not possible.

On the other hand, the description of mbrtoc16() described in section 7.28.1
states "If the function determines that the next multibyte character is complete
and valid, it determines the values of the corresponding wide characters". So it
considers it possible that a single multibyte character translates into multiple
wide characters. So maybe the meaning of "wide character" in section 7.28.1 is
different from definition of "wide character" in section 3.7.3.

In either case, the intended behaviour of c16rtomb() for characters encoded as
multiple char16\_t seems unclear. The issue has been discussed in the thread "A
function to convert char16\_t strings to char strings" in comp.std.c.

### Suggested Change

I see two possible options:

* State clearly that passing a char16\_t that is not a valid character by itself to c16rtomb() is an error. In this case, another function to convert char16\_t strings to char strings should be provided by the standard. The term "wide character" should then not be used in the description of mbrtoc16() the way it currently is.
* State clearly that c16rtomb() can handle characters consisting of multiple char16\_t. For such characters the first call would return 0, and only once all char16\_t encoding the character had been seen, c16rtomb() could write the character as multibyte character. The current wording "When c16 is not a valid wide character, an encoding error occurs" should be changed accordingly.