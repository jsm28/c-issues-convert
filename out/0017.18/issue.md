Compatibility of functions with `void` and no prototype

```c
f2(void);
 f2(); /* Is this function compatible with the one above? */
```

Now subclause 6.5.4.3, page 68, line 1 says that the first declaration of `f2`
specifies that the function has no parameters.

No rules are given in the subsequent paragraphs to say that a function
declaration with a parameter type list, with no parameters, is compatible with a
function declaration with an empty parameter list.

If we treat the `void` as a single parameter then page 68, lines 14-18 would
make the above two functions incompatible. `void` is not compatible with any
default promotions. subclause 6.5.4.3, page 68, lines 18-22 cover the case for
declaration and definition.

Thus I think that in the above example the behavior is implicitly undefined.
