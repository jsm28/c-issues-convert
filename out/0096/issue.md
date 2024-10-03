ANSI/ISO C Defect report #rfg3:

Subclause 6.5.4.2 **Array declarators** fails to contain any constraint which
would prohibit the element type in an array declarator from being a type which
is not an object type. (Note that subclause 6.1.2.5 seems to suggest that such
usage is prohibited by saying that “An *array type* describes a contiguously
allocated nonempty set of objects ...” But this still leaves the matter rather
unclear.)

I believe that some new constraint prohibiting the element type in an array
declarator from being a non-object type (at least in some obvious cases) is
clearly needed.

Please consider the case of an array declarator, occurring at some point within
a given translation unit, and indicating an element type `T`, where `T` is one
of the following:

1. A function type.
2. A void type.
3. An incomplete struct or union type which is *never* completed within the given translation unit.
4. An incomplete struct or union type which *is* completed later within the given translation unit.
5. An incomplete array type which is *never* completed within the given translation unit.
6. An incomplete array type which *is* completed later within the given translation unit.

I believe that it should be abundantly clear that the C Standard should contain
a constraint prohibiting array declarators where the specified element type is
either (1) or (2). Essentially all existing implementations already issue
diagnostics for such usage.

Also, in cases where an array declarator uses either a (3) or a (5) as the
element type, it seems eminently reasonable to require diagnostics \- and
indeed, many existing implementations already do issue diagnostics for such
usage \- but this is perhaps debatable.

Cases (4) and (6) from the above list are *entirely* debatable. Existing
practice among so-called “conforming” C compilers varies with respect to these
cases (in which an element type is completed at some point *after* use of the
type, as an element type, in an array declarator). Here are two examples:

```c
struct S array[10];			/* ok? */
 struct S { int member; };	/* type completed now */

 int array_of_array[][];		/* ok? */
 int array_of_array[5][5];	/* type completed now */
```

As I say, I believe that the very least the Committee should do is to add a
constraint requiring diagnostics for array declarators whose element types fall
into categories (1) or (2). The Committee may wish to provide an even more
stringent interpretation of subclause 6.1.2.5 and also require diagnostics for
element types falling into categories (3) and/or (5). The Committee may even
wish to take the simplest approach to this entire problem, and simply require
diagnostics for *any* case in which an array declarator specifies an element
type which is not (already) an object type.

Regardless of which choice is made, I feel strongly that it is important for
subclause 6.5.4.2 **Array declarators** to be revised to fully reflect both
common sense and (to the extent possible) the intent of subclause 6.1.2.5.

Footnote: Note that while is it *always* possible for a given incomplete struct
or union type to be completed somewhere later within the same scope and same
translation unit where it is used, and while it is *often* possible to complete
a given incomplete array type later within the same scope and same translation
unit where it is used (as illustrated by the above examples) it can sometimes be
*impossible* to *ever* complete a given array type later within its scope and
translation unit. This will certainly be the case whenever the array type in
question is *not* used to declare an entity having *some* linkage (either
internal or external).

Examples:

> ```c
>  void example ()
>         {
>  	void *vp = (int (*)[][]) 0;	/* abstract declarator
>  		declares no  object - type can't be completed */
>  	int array[][];	/* no linkage - type can't ever be
>  			completed */
>         }
> ```

I mention these cases only because they may potentially have some small bearing
upon the Committee's deliberations of the central issues of this Defect Report.
