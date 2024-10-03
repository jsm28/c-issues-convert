Does the description in subclause 7.3.1 imply that the characters defined in
subclause 5.2.1 are always classified as implied by subclause 5.2.1 regardless
of the locale specified?

In particular, do the characters `'a'` through `'z'` and `'A'` through `'Z'`
have to be classified as “lower case and “upper case,” respectively, in every
locale?

The specific lines needing interpretation are lines 20-21 in subclause 7.3.1.6,
page 103, and lines 16-17 in subclause 7.3.1.10, page 104\. The word “or” can be
interpreted to require a superset of the characters specified as lower/upper
case in subclause 5.2.1 or to allow an implementation-defined set of characters
(which might contain none of the subclause 5.2.1 designated lower/upper case
characters).
