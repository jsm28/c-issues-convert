### Summary

I believe the intent of C is that old-style function definitions with empty
parentheses do not give the function a type including a prototype for the rest
of the translation unit. For example,

```c
void f(){}
void g(){if(0)f(1);}
```

is valid.

6.9.1#7 specifies that if the declarator in the function definition includes a
parameter type list, it also serves as a prototype for the rest of the
translation unit. It does not specify that nothing else serves as a prototype.
Some readers of the standard interpret 6.7.5.3#14, "An empty list in a function
declarator that is part of a definition of that function specifies that the
function has no parameters.", as specifying that it provides a prototype.

Question 1: Does such a function definition give the function a type including a
prototype for the rest of the translation unit?

Question 2: Is the above translation unit valid?

### Suggested Technical Corrigendum
