My interpretation of the Standard is that the value of `MB_CUR_MAX` must be one
in the `"C"` locale. I infer that from the fact that:

1. The characters in the `"C"` locale must be alphanumeric \+ space.
2. The `is`*`XXX`* functions specify character constant values for the `"C"` locale.
3. A character constant consists of one or more characters that are enclosed within apostrophes. A character is regarded as having type `char`.
4. The data type `char` consists of one byte of storage.

However this clarification should be made explicit.
