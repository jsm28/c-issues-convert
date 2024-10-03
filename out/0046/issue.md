In subclause 6.7.1, page 82, line 9, it says, “An identifier declared as a
typedef name shall not be redeclared as a parameter.”

The question I have is: Does that sentence stand by itself absolutely or is it
intended to be read in the context of the paragraph in which it appears?

The beginning of the paragraph says, “If the declarator includes an identifier
list, ...” Function declarators including a parameter type list are dealt with
in the preceding paragraph which says nothing about typedef names.

In other words, is the following valid Standard C?

```c
typedef int foo;
 int bar(int foo) {return foo; }
```
