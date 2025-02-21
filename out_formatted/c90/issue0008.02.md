## Issue 0008.02: Should volatile functions be added?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Otto R. Newman, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-021  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_008.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_008.html)

What is happening is that, since the standard has not provided a mechanism to
describe a very recognizable and very important property of a function, such
mechanisms are by necessity being provided in non-standard ways. My
understanding is that a pragma should never be required for a program to execute
correctly as defined by the standard.

The existing situation serves to reduce portability of C programs. We believe
the Committee should address this problem and would like to offer a suggestion
which seems rather attractive.

Currently, defining an object as `volatile` indicates to the compiler that its
contents may be altered in ways not under control of the implementation. This is
meaningless with function declarations since a function doesn't have alterable
contents (i.e., is not an lvalue). Instead, it may be possible to utilize this
otherwise syntactic no-op by defining a “volatile function” to be one whose
return may not necessarily occur sequentially at the point of the invocation,
but possibly at some other point where the state of the calling program is
unknown. In other words, invocation of such a function results in the state of
the program becoming volatile.

Now, I admit that this is not a perfectly “clean” extrapolation of the use of
the type qualifier `volatile`, but it is rather compelling, having the following
advantages:

1. It solves the described problem in a general way that can be used with functions not necessarily named “`setjmp`.” Implementations defining `setjmp` as a function in `setjmp.h` would simply declare

   ```c
   int volatile setjmp(jmp_buf env);
   ```
2. It utilizes an existing keyword and gives meaning to its use in a context which would be otherwise meaningless.
3. It is consistent with the type specifier syntax to distinguish between volatile pointers and pointers to volatile objects. For example,

   ```c
   int volatile setjmp();
   ```

   defines `setjmp` to be a volatile function (i.e., a function whose invocation
   must inhibit certain optimizations).

   ```c
   int volatile (*maybe_setjmp_ptr)();
   ```

   defines a pointer to such a function, while

   ```c
   int (*mustnotbe_setjmp_ptr)();
   ```

   defines a pointer to a normal function.

   ```c
   int (* volatile vol_mustnotbe_setjmp_ptr)();
   ```

   defines a volatile pointer to a normal function.

   ```c
   int volatile (* volatile vol_maybe_setjmp_ptr)();
   ```

   defines a volatile pointer to a volatile function, and so on ...
4. Type consistency rules are already in place and make sense. For example,

   ```c
   maybe_setjmp_ptr = mustnotbe_setjmp_ptr;
   ```

   is okay with no type-checking violation, whereas

   ```c
   mustnotbe_setjmp_ptr = maybe_setjmp_ptr;
   ```

   is diagnosed. It would require casting such as

   ```c
   mustnotbe_setjmp_ptr = (int (*)())maybe_setjmp_ptr;
   ```
5. Since no new syntax or keywords are required, the impact of this change is very small to both the document defining the standard and to compilers which support it.

If there is enough Committee interest in this sort of solution, I would be glad
to draft a formal proposal.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the current semantics for type qualifiers as they
appear in the standard are as intended.
