### Summary

The rules for compatibility of function types in 6.7.5.3#15 do not define when a
function type is "specified by a function definition that contains a (possibly
empty) identifier list", and do not address compatibility between two types with
that property or what the composite type is in such cases.

As a first example, consider:

```c
        void f(a)int a;{}
        void g(a,b)int a,b;{}
        void (*h)(int, int, int) = (0 ? f : g);
```

What is the type of `(0 ? f : g)`? The types of `f` and `g` are compatible. Does
`(0 ? f : g)` have a type specified by a function definition? Does `(0 ? f :
f)`?

Question 1: Is the above translation unit valid?

Another example is:

```c
        void f(a)int a;{}
        void (*h)(int, int, int) = f;
```

I believe the intent of the standard is that a type is specified by a function
definition *only* for the purposes of checking compatibility of multiple
declarations of the same function; when as here the name of the function appears
in an expression, its type is determined by its return type and contains no
trace of the parameter types. However, implementation interpretations vary.

Question 2: Is the above translation unit valid?

It may still be necessary for compatibility of multiple unprototyped function
types determined by function definitions to be considered, if those definitions
are in different translation units and all but one are inline. (As an aside,
while the text of 6.7.4#6 assumes that there is only one definition of a
function in a translation unit, I can find nothing prohibiting more if `inline`
is used, though the presumption would probably mean compile-time undefined
behavior if there were more than one in a translation unit, with compatible
types.) By way of example, consider the following three translation units:

```c
        // TU 1:
        inline void f(a)int a;{}

        // TU 2:
        inline void f(a,b)int a,b;{}

        // TU 3:
        void f(a,b,c)int a,b,c;{}
```

The function types seem to be compatible, so 6.2.7#2 does not apply.

Question 3: Must a program containing these three translation units, which never
calls the function `f`, be accepted?

The function `f` cannot be called above from TU 1 or TU 2 without undefined
behavior, but could be called from TU 3, where the inline definitions in TU 1
and TU 2 cannot be used for a call. (Though a program containing calls in TU 1
and TU 2 which are conditioned by `if (0)` would also seem to be valid.) In the
following case, the types are similar enough that it would seem possible for
calls to occur in all three translation units without undefined behavior (by
virtue of the exceptions in 6.5.2.2#6):

```c
        // TU 1:
        inline void f(a,b)int a;unsigned b;{}
        void g(void){f(0,0);}

        // TU 2:
        inline void f(a,b)unsigned a;int b;{}
        void h(void){f(0,0);}

        // TU 3:
        void f(a,b)int a,b;{}
        void i(void){f(0,0);}
```

Question 4: Must a program containing these three translation units be accepted?

It seems undesirable for such variation among the types of functions with inline
definitions to be permitted. This could be fixed by defining compatibility of
multiple unprototyped function definitions to require compatibility of the
parameter types.

### Suggested Technical Corrigendum
