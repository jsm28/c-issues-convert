## Issue 0065: Can strictly conforming programs contain locales other that the 'C' locale?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_065.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_065.html)

Item 2 \- locales

Consider the program:

```c
#include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 int main (void)
        {
        int i;
        char *loc [] = { "English", "En_UK", "Loglan", "" };

        for (i = 0; ; i++)
              if (setlocale (LC_ALL, loc [i]) != NULL)
 	           {
 	           /*
 			 *  We must eventually get here,
 			 *  because setlocale("") can't yield NULL.
 	            /*
 	           printf ("Decimal point = '%s'\n",
 	           localeconv ()->decimal_point);
 	           exit (0);
 	           }
        }
```

The valid locales are implementation-defined (subclause 7.4.1.1). Nevertheless,
the output produced depends only on the locale, not any other
implementation-defined behavior. Is the program strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

The Committee affirms that the intent of this wording is that a program such as
that above, whose output varies only according to the locale selected and does
not rely on the presence of a specific locale other than the `"C"` locale or
that selected by `""`, was always intended to be strictly conforming.
Nevertheless, it is agreed that the cited extract from subclause 7.4.1.1 could
be read strictly as making such programs depend on implementation-defined
behavior.

The Committee reaffirms that programs that depend on the identity of the
available locales, as opposed to their contents, are not strictly conforming.

The Committee believes that the first occurrence of the term “implementation
defined” in subclause 7.4.1.1 was intended in the sense of
“implementation-documented.” However, the Committee is reluctant to introduce a
new term, with possibly new conformance requirements, in a Technical
Corrigendum. The Committee notes that the term “locale-specific,” while making
the sentence read somewhat awkwardly, carries the necessary requirements (the
implementation must document the relevant details).

The Committee decided that, though the question only addresses one issue to do
with locales, the above discussion applies to all instances where the behavior
of an implementation depends on the locale. For this reason, the Committee
decided to address all such issues at this time.

The Committee should revisit this issue during the revision of the C Standard.

### Correction

***In subclause 5.2.1.2, page 11, change the third bullet item:***

wherein each sequence of multibyte characters begins in an *initial shift state*
and enters other implementation-defined *shift states*

***to:***

wherein each sequence of multibyte characters begins in an *initial shift state*
and enters other locale-specific *shift states*

***In subclause 7.3, page 102, second paragraph, change:***

Those functions that have implementation-defined aspects only when not in the
`"C"` locale are noted below.

The term *printing character* refers to a member of an implementation-defined
set of characters, each of which occupies one printing position on a display
device; the term *control character* refers to a member of an
implementation-defined set of characters that are not printing characters.

***to:***

Those functions that have locale-specific aspects only when not in the `"C"`
locale are noted below.

The term *printing character* refers to a member of a locale-specific set of
characters, each of which occupies one printing position on a display device;
the term *control character* refers to a member of a locale-specific set of
characters that are not printing characters.

***In subclause 7.3.1.2, page 102, subclause 7.3.1.6, page 103, subclause
7.3.1.9, page 104, and subclause 7.3.1.10, page 104, change:***

is one of an implementation-defined set of characters

***to:***

is one of a locale-specific set of characters

***In subclause 7.4.1.1, page 107, second paragraph of Description, change:***

a value of `""` for `locale` specifies the implementation-defined native
environment.

***to:***

a value of `""` for `locale` specifies the locale-specific native environment.

***In subclause 7.10.1.4, page 151, subclause 7.10.1.5, page 152, and 7.10.1.6,
page 152, change:***

In other than the `"C"` locale, additional implementation-defined subject
sequence forms may be accepted.

***to:***

In other than the `"C"` locale, additional locale-specific subject sequence
forms may be accepted.

***Change Footnote 131, page 159, from:***

If the implementation employs special bytes to change the shift state, these
bytes do not produce separate wide character codes, but are grouped with an
adjacent multibyte character.

***to:***

If the locale employs special bytes to change the shift state, these bytes do
not produce separate wide character codes, but are grouped with an adjacent
multibyte character.

***In subclause 7.11.6.2, page 168, change:***

The `strerror` function returns a pointer to the string, the contents of which
are implementation-defined.

***to:***

The `strerror` function returns a pointer to the string, the contents of which
are locale-specific.

***In Annex G, pages 204-207, move the following bullet items under subclause
G.3 to subclause G.4:***

> G.3.4, page 204, item 2 (“The shift states used for the encoding ...”)
>
> G.3.14, page 206, item 3 (“The sets of characters tested for ...”)
>
> G.3.14, page 207, item 33 (“The contents of the error message strings ...”)

***In Annex G.4 page 207, Locale-specific behavior, change:***

The following characteristics of a hosted environment are locale-specific:

***to:***

The following characteristics of a hosted environment are locale-specific and
must be documented by the implementation:
