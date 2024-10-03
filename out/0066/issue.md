Item 3 \- locales

In a conforming implementation, can the value of any of the following
expressions (subclause 7.4.2.1) be a value other than 0 or 1? Can the value of
the first expression be 0?

> ```c
> strlen(localeconv()->decimal_point)
>         strlen(localeconv()->thousands_sep)
>         strlen(localeconv()->mon_decimal_point)
>         strlen(localeconv()->mon_thousands_sep)
> ```

If the value can be greater than 1, can the string contain more than one
multibyte character? If so, can the string contain shift sequences? If so, can
the string end other than in the initial shift state?
