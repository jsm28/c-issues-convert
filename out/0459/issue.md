### Summary

The synopsis of the `atomic_load` pair of generic functions specified in
7.17.7.2 shows that they accept pointers to a `volatile`\- (bot not `const`-)
qualified type:

> ```c
>           #include <stdatomic.h>
>
>           C atomic_load(volatile A *object);
>           C atomic_load_explicit(volatile A *object,
>                                  memory_order order);
> ```

The absence of the `const` qualifier implies that the functions cannot be called
with an argument of type `const` *`A`*`*` since there is no such conversion.

However, since neither function modifies its argument, there is no need to
prevent it from being called with an argument of type `const` *`A`*`*`. And, in
fact, the latest draft C\+\+ standard as of this writing,
[N3936](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3936.pdf
"Working Draft, Standard for Programming Language C++"), does provide an
overload of each function that takes a `const volatile` pointer.

### Suggested Technical Corrigendum

In section 7.17.7.2, paragraph 1, **Synopsis**, modify the declarations of the
`atomic_load` pair of generic functions as indicated below:

> `#include <stdatomic.h>`  
>     
>           *`C`* `atomic_load(`<ins>`const`</ins> `volatile` *`A`* `*object);`  
>           *`C`* `atomic_load_explicit(`<ins>`const`</ins> `volatile` *`A`* `*object,`  
>                                  `memory_order order);`
