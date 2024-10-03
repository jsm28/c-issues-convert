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
