Use of typedef names in parameter declarations

A syntactic ambiguity exists in the draft proposed C standard for which there
appears to be no semantic disambiguation. A sequence of examples should explain
the ambiguity. This matter needs interpretation by the Committee.

For these examples, let `T` be declaration specifiers which contain at least one
type specifier, to satisfy the semantics from subclause 6.5.6:

> If the identifier is redeclared in an inner scope ..., the type specifiers shall
> not be omitted in the inner declaration.

Let `U` be an identifier which is a typedef name at outer scope and which has
not (yet) been redeclared at current scope. A caret indicates the position of
each abstract declarator. Consider this declaration:

```c
declaration-specifiers direct-declarator (T^(U));
```

Here `U` is the type of the single parameter to a function returning type `T`,
due to a requirement from subclause 6.5.4.3:

> In a parameter declaration, a single typedef name in parentheses is taken to be
> an abstract declarator that specifies a function with a single parameter, not as
> redundant parentheses around the identifier for a declarator.

Consider this declaration:

```c
declaration-specifiers direct-declarator
         (T^(U^(parameter-type-list)));
```

In this example, `U` could be the type returned by a function which takes
`parameter-type-list`. This in turn would be the single parameter to a function
returning type `T`.

Alternatively, `U` could be a redundantly parenthesized name of a function which
takes `parameter-type-list` and returns type `T`.

Given the spirit of the requirement from subclause 6.5.4.3, the former
interpretation seems to be that intended by the Committee. If so, the
requirement may be changed to something similar to:

> In a parameter declaration, a direct declarator which redeclares a typedef name
> shall not be redundantly parenthesized.

Of course, parentheses must not be disallowed entirely... \[The original had
more, but this will suffice.\]
