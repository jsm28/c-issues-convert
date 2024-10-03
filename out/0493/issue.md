### Summary

The C11 threads library defines a mutex type, `mtx_t`, and a number of functions
that operate objects of the type. The `mtx_t` is fully described in **§7.26.1,
Introduction** (to the **Threads** section) as follows:

> a complete object type that holds an identifier for a mutex;

No other description of the type appears elsewhere in the text.

Among the functions provided by the C11 threads library that operate on objects
of the `mtx_t` type are `mtx_init()` and `mtx_destroy()`.

The `mtx_init(mtx_t *mtx, int type)` function is described in **§7.26.4.2** as
follows:

> -2- The `mtx_init` function creates a mutex object with properties indicated by
> `type`, which must have one of the six values:
> 
> * `mtx_plain` for a simple non-recursive mutex,
> * `mtx_timed` for a non-recursive mutex that supports timeout,
> * `mtx_plain | mtx_recursive` for a simple recursive mutex, or
> * `mtx_timed | mtx_recursive` for a recursive mutex that supports timeout.
> 
> -3- If the `mtx_init` function succeeds, it sets the mutex pointed to by `mtx`
> to a value that uniquely identifies the newly created mutex.
> 
> **Returns**  
> -4- The mtx\_init function returns `thrd_success` on success, or `thrd_error` if
> the request could not be honored.

The `mtx_destroy(mtx_t *mtx)` function is then described in **§7.26.4.1** like
so:

> The `mtx_destroy` function releases any resources used by the mutex pointed to
> by `mtx`. No threads can be blocked waiting for the mutex pointed to by `mtx`.

#### Problems With `mtx_t`

Since `mtx_t` is a complete object type, what are the semantics of copying
objects of the type (either by assignment or by passing them by value between
functions) and passing pointers to distinct copies of the same mutex object as
arguments to the C11 threads functions?

#### Problems With `mtx_init()`

The specification of `mtx_init()` raises the following questions to which the
standard doesn't provide clear answers.

1. What is the behavior of `mtx_init()` when called with a pointer to an object initialized to all zeros (such as a mutex object with static storage duration)? Are such calls valid, or if not, must the function fail by returning `thrd_error`, or is its behavior unspecified, or perhaps undefined? (If it is the same as calling it on an uninitialized object then how does one statically initialize a mutex?)
2. Similarly, what is the function's behavior when called with a pointer to an uninitialized mutex object (one whose value is indeterminate)? (Presumably, it should be to initialize the object to a valid state and not require the object to have been initialized to all zeros, but this is not specified.)
3. What is the function's behavior when called with the same pointer more than once (without a call to `mtx_destroy()` in between)?
4. What is the function's behavior when called with a pointer to a locked mutex object?
5. The function description specifies that the `type` argument must have one of six values but lists only four. What are the remaining two values of the `type` argument? (Note: this problem is the subject of DR [479](issue:0479).)
6. What is the function's behavior when `type` argument does not have one of the listed values? (Note that since the argument is a plain `int`, choosing not to define the behavior will make the function more dangerous to use than alternatives such as POSIX threads. Choosing to require the function to detect invalid arguments and reject them with an error exposes a problem due to its binary return value's inability to indicate different kinds of errors.)
7. If the function is required to fail when the `type` argument isn't valid, what is its required behavior in this case when the `mtx` argument is null?

#### Problems With `mtx_destroy()`

The specification of `mtx_destroy()` raises the following questions:

1. What is the behavior of `mtx_destroy()` when called with a pointer to an object initialized to all zeros (such as a mutex object with static storage duration) that has not been passed to `mtx_init()`? (This is important because it might mean that programs need to associate an external flag with each mutex object indicating whether or not it has been initialized in a way that requires `mtx_destroy()` to be called on it.)
2. What is the behavior of the function when called with the same pointer more than once? Is it required to have no effect or is it undefined?
3. What is the behavior of the function when threads are blocked waiting for the mutex it's called on? (The text is lax with the wording here, and assuming the function's behavior is undefined in this case, the text should phrase the requirement using the word "*shall*" rather than "*can*" and preferably make the undefined behavior explicit, for example similarly to how POSIX specifies the similar requirement in its API.)
4. What state is a mutex object in after `mtx_destroy()` has been called with it as an argument? Can such an object be subsequently passed as argument to any of the other mutex functions? For example, can such a mutex object be safely passed to `mtx_init()`? To any of the other mutex functions such as `mtx_lock()` and, if so, with what effects? (Undefined or error?)

#### Other Problems Due to the Underspecification Of Mutex Initialization

Neither `mtx_init()` nor `mtx_destroy()` discussed above, nor any of the other
functions that operate on `mtx_t` objects specifies what state the object is
required to be in when the function is called. In particular, none of the
functions specfies whether the object is required to be initialized or how.

That gives rise to the following general questions to which the standard fails
to provide clear answers:

1. Is an uninitialized mutex object (i.e., one with an indeterminate value) a valid argument to any of the other mutex functions besides those discussed above? If it isn't a valid argument (as is the most likely answer), are the mutex functions expected to detect the condition and fail by returning `thrd_error` or is the behavior unspecified, or perhaps undefined?
2. Similarly, is a statically initialized mutex object (one declared with static storage duration and initialized to all zeros) a valid argument to any of the the other mutex functions? For instance, is such a mutex a valid argument to `mtx_lock()` and if so, what is the "type" of such a mutex (is it plain, recurisive, or timed), and what state is it in? (Put another way, what are the effects of calling `mtx_lock()` on such a mutex?)
3. Assuming a statically initialized mutex object is a valid argument to only `mtx_init()` but not any of the mutex functions, what mechanism are C11 programs expected to use to statically initialize mutex objects to make them valid arguments to functions such as `mtx_lock()` (the equivalent of the POSIX threads `PTHREAD_MUTEX_INITIALIZER`)? Note that while some systems do not provide an API to statically initialize a native mutex object the functionality can be emulated by storing a flag in the C11 `mtx_t` object and checking that flag in every mutex function, lazily initializing the object as necessary. It is unclear whether C11 intends to require implementations to provide this functionality.
4. Is there any limit on the the number of times `mtx_init()` cam be called with a distinct object as an argument without an intervening call to `mtx_destroy()`? (In other words, must calls to `mtx_init()` and `mtx_destroy()` with the same mutex object be paired?) If it is intended to allow implementations to impose such a limit (as some do) how do programs distinguish the usually transient nature of exceeding such a limit from permanent mutex initialization errorss (such as invalid type arguments)?

One might be able to guess what some of the answers to the questions above might
be intended to be if one assumes that the library is meant to be implemented on
top of an existing threads library such as POSIX threads, but that is not
reflected in the specification in any way. Other reasonable guesses include that
C11 threads library is intended to provide a simpler though no less safe
interface to the underlying threads library on the system (i.e., with no
instances of undefined behavior the underlying threads library isn't already
subject to), but the lack of even the most basic requirements raises doubt about
this intent. Another possible guess is that the C11 threads library is intended
to be (or should be possible to be) independent of the underlying threads
implementation and provide its own distinct guarantees and impose its own
requirements (even though it in many cases fails to articulate them). In the
absence of answers to these questions the C11 threads library is essentially
unusable as a specification either for the development of implementations
facilitating portable code, or for writing portable code.

### Suggested Technical Corrigendum

The C11 threads specification should be amended to clearly answer the questions
above. Any new requirements should consider the goal of implementing the
specification in terms of an existings threads implementation such as the POSIX
threads library.
