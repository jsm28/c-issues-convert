New-line in preprocessor directives

Subclause 5.1.1.2, page 5, line 37 says: “Preprocessing directives are executed
and macro invocations are expanded.”

Subclause 6.8, page 86, lines 2-5 say: “A preprocessing directive ... and is
ended by the next new-line character.”

Subclause 6.8.3, page 89, lines 38-39 say: “Within the sequence of preprocessing
tokens ... new-line is considered a normal white-space character.”

These three statements are not sufficient to categorize the following:

```c
#define f(a,b) a+b
 #if f(1,
      2)
 ...
```

It should be defined whether the preprocessing directive rule or macro expansion
wins, i.e. is this code fragment legal or illegal?

In translation phase 4 “preprocessing directives are executed and macro
invocations expanded.”

Now do macro invocations get done first, followed by preprocessor directives?
Does the macro expander need to know that what it is expanding forms a
preprocessing directive?

Subclause 6.8, page 86, lines 2-5 suggest that the preprocessor directive is
examined to look for the new-line character. But how is it examined? Obviously
phases 1-3 happen during this examination. So why shouldn't part of phase 4?
