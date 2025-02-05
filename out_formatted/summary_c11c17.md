# C11 / C17: issue summary

**This issue summary has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|0400|[`realloc` with size zero problems](issue0400.md)|Fixed in C17|
|0401|["happens before" cannot be cyclic](issue0401.md)|Fixed in C17|
|0402|[memory model coherence is not aligned with C\+\+11](issue0402.md)|Fixed in C17|
|0403|[`malloc()` and `free()` in the memory model](issue0403.md)|Fixed in C17|
|0404|[joke fragment remains in a footnote](issue0404.md)|Fixed in C17|
|0405|[mutex specification not aligned with C\+\+11 on total order](issue0405.md)|Fixed in C17|
|0406|[Visible sequences of side effects are redundant](issue0406.md)|Fixed in C17|
|0407|[SC fences do not restrict modification order enough](issue0407.md)|Fixed in C17|
|0408|[Should locks provide intra-thread synchronization](issue0408.md)|Closed|
|0409|[`f(inf)` is `inf` being a range error](issue0409.md)|Closed|
|0410|[`ilogb` inconsistent with `lrint`, `lround`](issue0410.md)|Fixed in C17|
|0411|[Predefined macro values](issue0411.md)|Fixed in C11 TC1|
|0412|[`#elif`](issue0412.md)|Fixed in C17|
|0413|[initialization](issue0413.md)|Fixed in C17|
|0414|[Typos in 6.27 Threads `<threads.h>`](issue0414.md)|Fixed in C17|
|0415|[Missing divide by zero entry in Annex J.2](issue0415.md)|Fixed in C17|
|0416|[`tss_t` destruction unspecified](issue0416.md)|Fixed in C17|
|0417|[Annex J not updated with necessary `aligned_alloc` entries](issue0417.md)|Fixed in C17|
|0418|[`fmod(0.,Nan)` and `fmod(Nan, infinity)`](issue0418.md)|Closed|
|0419|[What the heck is a "generic function"?](issue0419.md)|Fixed in C17|
|0420|[syntax error in specification of for-statement](issue0420.md)|Closed|
|0421|[initialization of `atomic_flag`](issue0421.md)|Closed|
|0422|[initialization of atomic types](issue0422.md)|Closed|
|0423|[Defect Report relative to n1570: underspecification for qualified rvalues](issue0423.md)|Fixed in C17|
|0424|[underspecification of `tss_t`](issue0424.md)|Fixed in C17|
|0425|[no specification for the access to variables with temporary lifetime](issue0425.md)|Closed|
|0426|[G.5.1: `-yv` and `-x/v` are ambiguous](issue0426.md)|Fixed in C17|
|0427|[Function Parameter and Return Value Assignments](issue0427.md)|Closed|
|0428|[runtime-constraint issue with sprintf family of routines in Annex K](issue0428.md)|Fixed in C17|
|0429|[Should `gets_s` discard next input line when `(s == NULL)` ?](issue0429.md)|Fixed in C17|
|0430|[`getenv_s`, `maxsize` should be allowed to be zero](issue0430.md)|Fixed in C17|
|0431|[`atomic_compare_exchange`: What does it mean to say two structs compare equal?](issue0431.md)|Fixed in C17|
|0432|[Is `0.0` required to be a representable value?](issue0432.md)|Closed|
|0433|[Issue with constraints for wide character function arguments involving **RSIZE\_MAX**](issue0433.md)|Fixed in C17|
|0434|[Missing constraint w.r.t. Atomic](issue0434.md)|Fixed in C17|
|0435|[Missing constraint w.r.t. Imaginary](issue0435.md)|Closed|
|0436|[Request for interpretation of C11 6.8.5#6](issue0436.md)|Fixed in C17|
|0437|[`clock` overflow problems](issue0437.md)|Fixed in C17|
|0438|[`ungetc / ungetwc` and file position after discarding push back problems](issue0438.md)|Fixed in C17|
|0439|[Issues with the definition of “full expression”](issue0439.md)|Fixed in C17|
|0440|[Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 1](issue0440.md)|Closed|
|0441|[Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 2](issue0441.md)|Fixed in C17|
|0442|[Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 3](issue0442.md)|Closed|
|0443|[Floating-point issues in C11 from PDTS 18661-1 UK review, Issue 4](issue0443.md)|Closed|
|0444|[Issues with alignment in C11, part 1](issue0444.md)|Fixed in C17|
|0445|[Issues with alignment in C11, part 2](issue0445.md)|Fixed in C17|
|0446|[Use byte instead of character for memcmp, memcpy](issue0446.md)|Closed|
|0447|[Boolean from complex](issue0447.md)|Fixed in C17|
|0448|[What are the semantics of a **\# non-directive**?](issue0448.md)|Fixed in C17|
|0449|[What is the value of TSS\_DTOR\_ITERATIONS for implementations with no maximum?](issue0449.md)|Closed|
|0450|[`tmpnam_s` clears `s[0]` when `maxsize > RSIZE_MAX`](issue0450.md)|Fixed in C17|
|0451|[Instability of uninitialized automatic variables](issue0451.md)|Closed|
|0452|[Effective Type in Loop Invariant](issue0452.md)|Fixed in C17|
|0453|[Atomic flag type and operations](issue0453.md)|Fixed in C17|
|0454|[ATOMIC\_VAR\_INIT (issues 3 and 4\)](issue0454.md)|Closed|
|0455|[ATOMIC\_VAR\_INIT issue 5](issue0455.md)|Closed|
|0456|[Compile time definition of `UINT`*`N`*`_C(`*`value`*`)`](issue0456.md)|Closed|
|0457|[The `ctime_s` function in Annex K defined incorrectly](issue0457.md)|Fixed in C17|
|0458|[ATOMIC\_XXX\_LOCK\_FREE macros not constant expressions](issue0458.md)|Fixed in C17|
|0459|[atomic\_load missing const qualifier](issue0459.md)|Fixed in C17|
|0460|[`aligned_alloc` underspecified](issue0460.md)|Fixed in C17|
|0461|[problems with references to objects in signal handlers](issue0461.md)|Closed|
|0462|[Clarifying objects accessed in signal handlers](issue0462.md)|Fixed in C17|
|0463|[Left-shifting into the sign bit](issue0463.md)|Closed|
|0464|[Clarifying the Behavior of the `#line` Directive](issue0464.md)|Fixed in C17|
|0465|[Fixing an inconsistency in `atomic_is_lock_free`](issue0465.md)|Fixed in C17|
|0466|[scope of a `for` loop control declaration](issue0466.md)|Closed|
|0467|[maximum representable finite description vs math](issue0467.md)|Closed|
|0468|[`strncpy_s` clobbers buffer past `null`](issue0468.md)|Fixed in C17|
|0469|[lock ownership vs. thread termination](issue0469.md)|Closed|
|0470|[mtx\_trylock should be allowed to fail spuriously](issue0470.md)|Fixed in C17|
|0471|[Complex math functions cacosh and ctanh](issue0471.md)|Fixed in C17|
|0472|[Introduction to complex arithmetic in 7.3.1p3 wrong due to CMPLX](issue0472.md)|Fixed in C17|
|0473|["A range error occurs if x is too large." is misleading](issue0473.md)|Fixed in C17|
|0474|[NOTE 1 Clarification for `atomic_compare_exchange`](issue0474.md)|Closed|
|0475|[Misleading Atomic library references to atomic types](issue0475.md)|Fixed in C17|
|0476|[volatile semantics for lvalues](issue0476.md)|Fixed in C23|
|0477|[`nan` should take a string argument](issue0477.md)|Fixed in C17|
|0478|[valid uses of the `main` function](issue0478.md)|Closed|
|0479|[unclear specification of `mtx_trylock` on non-recursive muteness](issue0479.md)|Closed|
|0480|[`cnd_wait` and `cnd_timewait` should allow spurious wake-ups](issue0480.md)|Fixed in C17|
|0481|[Controlling expression of `_Generic` primary expression](issue0481.md)|Fixed in C17|
|0482|[Macro invocation split over many files](issue0482.md)|Closed|
|0483|[`__LINE__` and `__FILE__` in macro replacement list](issue0483.md)|Closed|
|0484|[invalid characters in `strcoll()`](issue0484.md)|Closed|
|0485|[Problem with the specification of `ATOMIC_VAR_INIT`](issue0485.md)|Fixed in C17|
|0486|[Inconsistent specification for arithmetic on atomic objects](issue0486.md)|Closed|
|0487|[`timespec` vs. `tm`](issue0487.md)|Fixed in C17|
|0488|[`c16rtomb()` on wide characters encoded as multiple `char16_t`](issue0488.md)|Fixed in C23|
|0489|[Integer Constant Expression](issue0489.md)|Closed|
|0490|[Unwritten Assumptions About if-then](issue0490.md)|Closed|
|0491|[Concern with Keywords that Match Reserved Identifiers](issue0491.md)|Fixed in C17|
|0492|[Named Child struct-union with no Member](issue0492.md)|Closed|
|0493|[Mutex Initialization Underspecified](issue0493.md)|Closed|
|0494|[Part 1: Alignment specifier expression evaluation](issue0494.md)|Fixed in C23|
|0495|[Part 2: Atomic specifier expression evaluation](issue0495.md)|Closed|
|0496|[`offsetof` questions](issue0496.md)|Fixed in C23|
|0497|["white-space character" defined in two places](issue0497.md)|Fixed in C23|
|0498|[`mblen`, `mbtowc`, and `wctomb` thread-safety](issue0498.md)|Closed|
|0499|[Anonymous structure in union behavior](issue0499.md)|Fixed in C23|
|0500|[Ambiguous specification for **FLT\_EVAL\_METHOD**](issue0500.md)|Fixed in C23|
|0501|[Can **DECIMAL\_DIG** be larger than necessary?](issue0501.md)|Fixed in C23|
|0502|[Flexible array member in an anonymous struct](issue0502.md)|Closed|
|0503|[Hexadecimal floating-point and `strtod`](issue0503.md)|Closed|

