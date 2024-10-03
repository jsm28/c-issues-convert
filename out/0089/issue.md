Item 26 \- multiple definitions of macros

Consider the following code:

```c
#define macro   object_like
 #define macro(argument)        function_like
```

Does this code require a diagnostic?

The wording of subclause 6.8.3 specifies that a macro may be redefined under
certain circumstances (basically identical definitions), but does not actually
forbid any other redefinition. Thus it can be argued that the constraint in
subclause 6.8.3 is not violated, and a diagnostic is not required.
