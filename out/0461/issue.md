### Summary

We believe there are two problems in section **7.14.1.1 The signal function**,
paragraph 5, which specifies the constraints under which signal handlers can
access objects declared in other scopes. The problems are summarized in the
following two subsections. The section titled Suggested Technical Corrigendum
then proposes a correction to both.

Section **7.14.1.1 The signal function**, paragraph 5, specifies the following
constraints. Note, in particular, to use of the word "refers," and the reference
to objects with "static or thread storage duration" underscored in the text
below.

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler <ins>refers</ins> to
> any object with <ins>static or thread storage duration</ins> that is not a
> lock-free atomic object other than by assigning a value to an object declared as
> `volatile sig_atomic_t`, or the signal handler calls any function in the
> standard library other than the abort function, the `_Exit` function, the
> `quick_exit` function, or the `signal` function with the first argument equal to
> the signal number corresponding to the signal that caused the invocation of the
> handler.

**Underspecification of referring to objects**

The standard doesn't formally define the term *refer* but its uses in the text
suggest that it denotes any use of an object, including one that doesn't involve
accessing it. The term *access* is defined in 3.1 to mean an \<execution-time
action\> *to read or modify the value of an object.*

Preventing signal handlers from accessing objects is necessary in order to avoid
data races between accesses (reads and writes) to the same object in the rest of
the program that are in progress but not completed at the time the signal is
delivered.

However, by making use of the word "refers," the sentence in 7.14.1.1 quoted
above implies that even mentioning the name of an object in an unevaluated
context such as the `sizeof` expression, or taking its address is undefined in a
signal handler. This restriction is unnecessary, since such references are safe
because they cannot introduce any sort of a data race between the signal handler
and the rest of the program. Thus, referring to such objects without accessing
them should be permitted in conforming programs.

Furthermore, accessing a `const` object to read (but not modify) its value also
cannot introduce a data race and is safe as well. Thus, the restriction can be
relaxed even further to allow signal handlers to read constant objects. Note
that `const` objects are those that are declared `const`. In particular,
accessing an object that was not declared const via a pointer to a
`const`-qualified type does not change the fact that the object itself is not
`const`. This distinction is important to understand that relaxing this
constraint cannot introduce the potential for a data race when such a
non-`const` object is modied in the program while it's accessed via a
`const`-qualified pointer in a signal handler.

The comments in the following example should make this distinction clear:

> ```c
> const int safe = (1 << SIGINT) | (1 << SIGQUIT);
>       int unsafe = (1 << SIGHUP) | (1 << SIGTERM);
>
> volatile sig_atomic_t sigcount [2];
>
> void handler (int signo) {
>
>     const int *pmask;   // pointer to const int
>
>     // taking the address of any object is safe and should be allowed
>     pmask = &safe;
>
>     // access to safe should be allowed since it's a const object
>     if ((1 << signo) & *pmask)
>         ++sigcount [0];
>
>     // safe and should be allowed
>     pmask = &unsafe;
>
>     // access to unsafe remains undefined since it's not a const object
>     if ((1 << signo) & *pmask)
>         ++sigcount [1];
> }
> ```

**Missing restriction to access other functions' local objects**

The sentence from paragraph 5 quoted above specifically singles out objects with
static or thread storage duration, but permits signal handlers to access objects
with automatic storage duration without a similar restriction. However, a signal
handler that has access to a local variable defined in another function whose
execution is interrupted by the delivery of a signal resulting in the invocation
of the signal handler contains the same potential data race as if the two
functions both accessed the same object with static storage duration.

To make clear how this condition could arise, consider the following program
which, when `atomic_intptr_t` is a lock-free type, is strictly conforming
according to the letter of the standard despite the data race.

> ```c
> atomic_intptr_t p;   // assume atomic_intptr_t is lock-free
>
> void handler (int signo) {
>     // the following write access should be undefined since it modifies
>     // an object with automatic storage duration declared in f
>     ++*(int*)p;
> }
>
> void f (void) {
>     int i = 0;
>     p = (atomic_intptr_t)&i;
>
>     signal (SIGINT, handler);
>
>     while (i < 7)
>         printf ("%i\n", i);
> }
> ```

### Suggested Technical Corrigendum

The proposed corrigendum below changes the standard to remove the unnecessary
constraints discussed above, and to add the missing restriction to prevent
accessing local variables defined elsewhere in the program. The reference to the
lifetime of auto objects makes sure that accesses to local variables defined in
signal handlers themselves as well as in functions called from them remain well
defined.

In section 7.14.1.1, modify the first sentence of paragraph 5 as indicated
below:

> If the signal occurs other than as the result of calling the `abort` or `raise`
> function, the behavior is undefined if the signal handler <del>refers
> to</del><ins>accesses</ins> any <ins>non-`const`</ins> object with static or
> thread storage duration<ins>, or any non-`const` object with automatic storage
> duration whose lifetime started before the signal handler has been
> entered,</ins> that is not a lock-free atomic object other than by...

In addition, make the corresponding change to section **J.2 Undefined
behavior**.
