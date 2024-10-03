ANSI/ISO C Defect report #rfg8:

Subclause 6.3.2.2 **Function calls** says:

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters.

The problem with this statement is the phrase “as if by assignment.” The above
rule fails to yield an unambiguous meaning in cases where an assignment of the
actual to the formal would be prohibited by other rules of the language, as in:

```c
void callee (const int formal);
 int actual;
 void caller () { callee(actual); }
```

(Here, the name of the formal parameter `formal` may be initialized but not
assigned to, because it is a non-modifiable lvalue.)

A similar problem exists within subclause 6.6.6.4 **The `return` statement**. It
says:

If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.

This statement leaves the validity of the following code open to question:

```c
 const int returner () { return 99; }
```

Last but not least, subclause 6.5.7 **Initialization** says:

The initializer for a scalar shall be a single expression, optionally enclosed
in braces. The initial value of the object is that of the expression; the same
type constraints and conversions as for simple assignment apply, ...

This statement leaves the validity of the following code open to question:

```c
const int i = 99;
```

(Note that *assignment* to the data object `i` is not normally permitted, as its
name does not represent a modifiable lvalue.)
