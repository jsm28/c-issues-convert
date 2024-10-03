`char` parameters to `strcmp` and `strncmp`

Refer to subclause 7.11.4, page 164\. If `char` is signed then `char *` cannot
be interpreted as pointing to `unsigned char`. The required cast may give
undefined results. This applies to `strcmp` and `strncmp`.
