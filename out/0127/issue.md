ANSI/ISO C Defect Report #rfg34:

Subject: Composite type of an enumerated type and an integral type.

Given the declarations:

```c
enum E { red, green, blue } object;
 int object;
```

and given an implementation for which the type `int` is considered to be
compatible with the type `enum E`, what is the composite type of `object` at the
end of the translation unit which contains the above declarations?

Background:

Subclause 6.5.2.2 says:

> Each enumerated type shall be compatible with an integer type; the choice of
> type implementation-defined.

Subclause 6.1.2.6 says:

> A *composite type* can be constructed from two types that are compatible; ...
> 
> For an identifier with external or internal linkage declared in the same scope
> as another declaration for that identifier, the type of the identifier becomes
> the composite type.
