*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 023: Correction to Technical Corrigendum 1

An example added by TC1 is wrong.

TC1 added the following example to subclause 7.9.6.2:

In:

```c
  #include  stdio.h
         /* ..... */
         int d1, d2, n1, n2, i;
        i = sscanf("123", "%d%n%n%d", &d1, &n1, &n2, &d2);
```

the value 123 is assigned to `d1` and the value 3 to `n1`. Because `%n` can
never get an input failure the value of 3 is also assigned to `n2`. The value of
`d2` is not affected. The value 3 is assigned to `i`.

This should set `i` to 1, not 3, as `%n` does not affect the returned assignment
count.

### Suggested Technical Corrigendum

In the example, change:

The value 3 is assigned to `i`.

to:

The value 1 is assigned to `i`.
