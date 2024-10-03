What is the result of: `printf("%#.4o", 345);`? Is it `0531` or is it `00531`?

Subclause 7.9.6.1, on page 132, lines 37-38 says: “For `o` conversion, it
increases the precision to force the first digit of the result to be a zero.”

Is this a conditional or an unconditional increase in the precision if the most
significant digit is not already a `0`? Which is the correct interpretation?
