### Summary

If an incomplete array type has elements of unknown size, should the incomplete
array type be a VLA type? The definition of VLA types in 6.7.5.2#4 only seems to
make complete types into VLA types. In particular, does the following, at block
scope, violate any constraint?

```c
    int i;
    // ...
    int c[][i] = { 0 };
```

If it is not a VLA \- and nothing in the standard seems to make it a VLA \- then
the initializer would seem to be valid, and to determine the size of the array.
This seems rather against the spirit of prohibiting initializing VLAs in
6.5.2.5#1 (compound literals) and 6.7.8#3 (initializers).

Those appear to be the only places where it particularly matters whether such
types are VLA types. In other cases, use of such types does not depend on
whether they are VLA types, or yields a constraint violation whether or not they
are VLA types, or in the case of

```c
    static int c[][i];
```

at block scope violates the requirement of 6.7#7 for the type to be complete, so
causing undefined behavior, though if the type were a VLA type then there would
be a violation of the constraint in 6.7.5.2#2, so requiring a diagnostic.

Defining such types to be VLA types would ensure constraint violations in
6.5.2.5#1 and 6.7.5.2#2. 6.7.8#3 would need rewording to avoid "that is not a
variable length array type" applying to "object type" only.

### Suggested Technical Corrigendum
