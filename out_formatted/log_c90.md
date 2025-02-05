# C90: issue log

**This issue log has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|0001|[Do functions return values by copying?](log_c90.md#issue0001)|Fixed in C90 TC1|
|0002|[Should `\` be escaped within macro actual parameters?](log_c90.md#issue0002)|Closed|
|0003.01|[Are preprocessing numbers too inclusive?](log_c90.md#issue0003.01)|Closed|
|0003.02|[Should white space surround macro substitutions?](log_c90.md#issue0003.02)|Closed|
|0003.03|[Is an empty macro argument a constraint violation?](log_c90.md#issue0003.03)|Closed|
|0003.04|[Should preprocessing directives be permitted within macro invokations?](log_c90.md#issue0003.04)|Closed|
|0004|[Are multiple definitions of unused identifiers with external linkage permitted?](log_c90.md#issue0004)|Fixed in C90|
|0005|[May a conforming implementation define and recognize a pragma which would change the semantics of the language?](log_c90.md#issue0005)|Closed|
|0006|[How does `strtoul` behave when presented with a subject sequence that begins with a minus sign?](log_c90.md#issue0006)|Closed|
|0007|[Are declarations of the form `struct` *`tag`* permitted after *`tag`* has already been declared?](log_c90.md#issue0007)|Closed|
|0008.01|[Is dead-store elimination permitted near `setjmp`?](log_c90.md#issue0008.01)|Closed|
|0008.02|[Should volatile functions be added?](log_c90.md#issue0008.02)|Closed|
|0009|[Are typedef names sometimes ambiguous in parameter declarations?](log_c90.md#issue0009)|Fixed in C90 TC1|
|0010|[Is the typedef to an incomplete type valid?](log_c90.md#issue0010)|Closed|
|0011.01|[When do the types of multiple external declarations get formed into a composite type?](log_c90.md#issue0011.01)|Fixed in C90 TC1|
|0011.02|[Does `extern` link to a static declaration that is not visible?](log_c90.md#issue0011.02)|Fixed in C90 TC1|
|0011.03|[Are implicit initializers for tentative array definitions syntactically valid?](log_c90.md#issue0011.03)|Closed|
|0011.04|[Does an incomplete array get completed as a tentative definition?](log_c90.md#issue0011.04)|Fixed in C90 TC1|
|0012|[Can one take the address of a void expression?](log_c90.md#issue0012)|Closed|
|0013.01|[How does one form the composite type of mixed array and pointer parameter types?](log_c90.md#issue0013.01)|Fixed in C90 TC1|
|0013.02|[Is compatible properly defined for recursive types?](log_c90.md#issue0013.02)|Closed|
|0013.03|[What is the composite type of an enumeration and an integer?](log_c90.md#issue0013.03)|Closed|
|0013.04|[When is a struct type complete?](log_c90.md#issue0013.04)|Fixed in C90 TC1|
|0013.05|[When is the `sizeof` an enumeration type known?](log_c90.md#issue0013.05)|Fixed in C90 TC1|
|0014.01|[Is `setjmp` a macro or a function?](log_c90.md#issue0014.01)|Closed|
|0014.02|[How does `fscanf("%n")` behave on end-of-file?](log_c90.md#issue0014.02)|Fixed in C90 TC1|
|0015|[How does an unsigned plain bitfield promote?](log_c90.md#issue0015)|Closed|
|0016.01|[Can a tentative definition have an incomplete type initially?](log_c90.md#issue0016.01)|Closed|
|0016.02|[Can you implicitly initialize a union when null pointers have nonzero bit patterns?](log_c90.md#issue0016.02)|Fixed in C90 TC1|
|0017.01|[Are newlines permitted within macro invocations in preprocessing directives?](log_c90.md#issue0017.01)|Fixed in C90 TC1|
|0017.02|[Should the absence of function `main` be explicitly undefined?](log_c90.md#issue0017.02)|Fixed in C90 TC1|
|0017.03|[Does a constraint violation win over undefined behavior?](log_c90.md#issue0017.03)|Fixed in C90 TC1|
|0017.04|[Do numeric escape sequences map from source to execution character sets?](log_c90.md#issue0017.04)|Closed|
|0017.05|[When are character constants implementation defined?](log_c90.md#issue0017.05)|Closed|
|0017.06|[Are register aggregates permitted?](log_c90.md#issue0017.06)|Fixed in C90 TC1|
|0017.07|[What is the scope and uniqueness of `size_t`?](log_c90.md#issue0017.07)|Closed|
|0017.08|[What types are compatible with pointer to `void`?](log_c90.md#issue0017.08)|Closed|
|0017.09|[What is the type of an assignment expression?](log_c90.md#issue0017.09)|Fixed in C90 TC1|
|0017.10|[When is the `sizeof` an object needed?](log_c90.md#issue0017.10)|Closed|
|0017.11|[Is `struct t; struct t;` valid?](log_c90.md#issue0017.11)|Closed|
|0017.12|[How do typedefs parse in function prototypes?](log_c90.md#issue0017.12)|Fixed in C90 TC1|
|0017.13|[How does `register` affect compatibility of function parameters?](log_c90.md#issue0017.13)|Closed|
|0017.14|[`const void` type as a parameter](log_c90.md#issue0017.14)|Fixed in C90 TC1|
|0017.15|[When do array parameters get converted to pointers?](log_c90.md#issue0017.15)|Fixed in C90 TC1|
|0017.16|[Are subarrays of arrays distinct objects?](log_c90.md#issue0017.16)|Fixed in C90 TC1|
|0017.17|[How do you initialize the first member of a union if it has no name?](log_c90.md#issue0017.17)|Fixed in C90 TC1|
|0017.18|[Are `f()` and `f(void)` compatible?](log_c90.md#issue0017.18)|Closed|
|0017.19|[Are macro expansions ambiguous?](log_c90.md#issue0017.19)|Fixed in C90 TC1|
|0017.20|[Is the scope of macro parameters defined in the right place?](log_c90.md#issue0017.20)|Closed|
|0017.21|[Is translation phase 4 defined unambiguously?](log_c90.md#issue0017.21)|Closed|
|0017.22|[Does the rescan of a macro invocation also perform token pasting?](log_c90.md#issue0017.22)|Fixed in C90 TC1|
|0017.23|[How long does `blue paint` persist on macro names?](log_c90.md#issue0017.23)|Closed|
|0017.24|[Can subclause 7.1.2 be better expressed?](log_c90.md#issue0017.24)|Fixed in C90 TC1|
|0017.25|[Should *must* appear in footnotes?](log_c90.md#issue0017.25)|Closed|
|0017.26|[Are unnamed union members required to be initialized?](log_c90.md#issue0017.26)|Fixed in C90 TC1|
|0017.27|[Does the `#` flag alter zero stripping of `%g` in `fprintf`?](log_c90.md#issue0017.27)|Closed|
|0017.28|[Does `errno` get stored before library functions return?](log_c90.md#issue0017.28)|Closed|
|0017.29|[When does conversion failure occur in floating-point `fscanf` input?](log_c90.md#issue0017.29)|Fixed in C90 TC1|
|0017.30|[Do `fseek/fsetpos` require values from successful calls to `ftell/fgetpos`?](log_c90.md#issue0017.30)|Fixed in C90 TC1|
|0017.31|[Are object sizes always in bytes?](log_c90.md#issue0017.31)|Closed|
|0017.32|[Are `strcmp/strncmp` defined when `char` is signed?](log_c90.md#issue0017.32)|Closed|
|0017.33|[Are `strcmp/strncmp` defined for strings of differing length](log_c90.md#issue0017.33)|Closed|
|0017.34|[Is `strtok` described properly?](log_c90.md#issue0017.34)|Closed|
|0017.35|[When is a physical source line created?](log_c90.md#issue0017.35)|Closed|
|0017.36|[Is a function returning `const void` defined?](log_c90.md#issue0017.36)|Closed|
|0017.37|[What is the type of a function call?](log_c90.md#issue0017.37)|Fixed in C90 TC1|
|0017.38|[What is an iteration control structure or selection control structure?](log_c90.md#issue0017.38)|Fixed in C90 TC1|
|0017.39|[Are header names tokens outside include directives?](log_c90.md#issue0017.39)|Fixed in C90 TC1|
|0018|[Does `fscanf` recognize literal multibyte characters properly?](log_c90.md#issue0018)|Closed|
|0019|[Are printing characters implementation defined?](log_c90.md#issue0019)|Closed|
|0020|[Is the relaxed Ref/Def linkage model conforming?](log_c90.md#issue0020)|Closed|
|0021|[What is the result of `printf("%#.4o", 345)`?](log_c90.md#issue0021)|Fixed in C90 TC1|
|0022|[What is the result of `strtod("100ergs", &ptr)`?](log_c90.md#issue0022)|Fixed in C90 TC1|
|0023|[If 99,999 is larger than `DBL_MAX_10_EXP`, what is the result of `strtod("0.0e99999", &ptr)`?](log_c90.md#issue0023)|Closed|
|0024|[For `strtod`, what does `"C"` locale mean?](log_c90.md#issue0024)|Closed|
|0025|[What is meant by *representable floating-point value?*](log_c90.md#issue0025)|Closed|
|0026|[Can one use other than the basic C character set in a strictly conforming program?](log_c90.md#issue0026)|Closed|
|0027|[May a standard conforming implementation add identifier characters?](log_c90.md#issue0027)|Fixed in C90 TC1|
|0028|[What are the aliasing rules for dynamically allocated objects?](log_c90.md#issue0028)|Closed|
|0029|[Must compatible structs/unions have the same tag in different translation units?](log_c90.md#issue0029)|Closed|
|0030|[May `sin(DBL_MAX)` set `errno` to `EDOM`?](log_c90.md#issue0030)|Closed|
|0031|[How are exceptions handled in constant expressions?](log_c90.md#issue0031)|Closed|
|0032|[Can an implementation permit a comma operator in a constant expression?](log_c90.md#issue0032)|Closed|
|0033|[Must a conforming implementation diagnose *shall* violations outside **Constraints**?](log_c90.md#issue0033)|Closed|
|0034.01|[Does size information evaporate when a declaration goes out of scope, even for objects with external linkage?](log_c90.md#issue0034.01)|Fixed in C90 TC1|
|0034.02|[If so, can one then write conflicting declarations in disjoint scopes?](log_c90.md#issue0034.02)|Closed|
|0035.01|[Can one declare an enumeration or struct tag as part of an old-style parameter declaration?](log_c90.md#issue0035.01)|Closed|
|0035.02|[If so, what is the scope of enumeration tags and constants declared in old-style parameter declarations?](log_c90.md#issue0035.02)|Closed|
|0036|[May a floating-point constant be represented with more precision than implied by its type?](log_c90.md#issue0036)|Closed|
|0037|[Can UNICODE or ISO 10646 be used as a multibyte code?](log_c90.md#issue0037)|Closed|
|0038|[What happens when macro replacement creates adjacent tokens that can be taken as a single token?](log_c90.md#issue0038)|Closed|
|0039.01|[Must `MB_CUR_MAX` be one in the `"C"` locale?](log_c90.md#issue0039.01)|Closed|
|0039.02|[Should `setlocale(LC_ALL, NULL)` return `"C"` in the `"C"` locale?](log_c90.md#issue0039.02)|Closed|
|0040.01|[What is the composite type of `f(int)` and `f(const int)`?](log_c90.md#issue0040.01)|Fixed in C90 TC1|
|0040.02|[Is an implementation that fails to equal the value of an environmental limit conforming?](log_c90.md#issue0040.02)|Fixed in C90 TC1|
|0040.03|[Is an **Environmental Constraint** a constraint?](log_c90.md#issue0040.03)|Closed|
|0040.04|[Should the response to [Defect Report #017, Q39](log_c90.md#issue0017.39) be reconsidered?](log_c90.md#issue0040.04)|Closed|
|0040.05|[Can a conforming implementation accept `long long`?](log_c90.md#issue0040.05)|Closed|
|0040.06|[Can one use `offsetof(struct t1, mbr)` before `struct t1` is completely defined?](log_c90.md#issue0040.06)|Closed|
|0040.07|[Can `sizeof` be applied to earlier parameter names in a prototype, or to earlier fields in a struct?](log_c90.md#issue0040.07)|Closed|
|0040.08|[What arithmetic can be performed on a `char` holding a defined character literal value?](log_c90.md#issue0040.08)|Closed|
|0040.09|[Should the response to [Defect Report #017, Q27](log_c90.md#issue0017.27) be reconsidered?](log_c90.md#issue0040.09)|Closed|
|0041|[Are `'A'` through `'Z'` always `isupper` in all locales?](log_c90.md#issue0041)|Closed|
|0042.01|[Does `memcpy` define a (sub)object?](log_c90.md#issue0042.01)|Closed|
|0042.02|[If so, how big is the object defined by `memcpy`?](log_c90.md#issue0042.02)|Closed|
|0042.03|[How big is a string object defined by the `str*` functions?](log_c90.md#issue0042.03)|Closed|
|0043.01|[Can `NULL` be defined as `4-4`?](log_c90.md#issue0043.01)|Fixed in C90 TC1|
|0043.02|[Can an identifier that starts with an underscore be defined as a macro in a source file that includes at least one standard header?](log_c90.md#issue0043.02)|Closed|
|0044.01|[What does it mean to say that the type of `offsetof` is `size_t`?](log_c90.md#issue0044.01)|Closed|
|0044.02|[Must the expansion of a standard header be a strictly conforming program?](log_c90.md#issue0044.02)|Closed|
|0044.03|[Does expanding `offsetof` result in a non-strictly conforming program?](log_c90.md#issue0044.03)|Closed|
|0044.04|[Can one use `offsetof` in a strictly conforming program?](log_c90.md#issue0044.04)|Closed|
|0044.05|[Is `offsetof` the only standard macro that renders a program not strictly conforming?](log_c90.md#issue0044.05)|Closed|
|0045|[Can one `freopen` an already closed file?](log_c90.md#issue0045)|Closed|
|0046|[May a typedef be redeclared as a parameter outside an old-style function parameter list?](log_c90.md#issue0046)|Closed|
|0047|[Can an array parameter have elements of incomplete type?](log_c90.md#issue0047)|Closed|
|0048|[Is `abort` compatible with POSIX?](log_c90.md#issue0048)|Closed|
|0049|[Can `strxfrm` produce a longer translation string?](log_c90.md#issue0049)|Closed|
|0050|[Does a proper definition of `wchar_t` need to be in scope to write a wide-character literal?](log_c90.md#issue0050)|Closed|
|0051|[Can one index beyond the declared end of an array if space is allocated for the extra elements?](log_c90.md#issue0051)|Closed|
|0052.01|[Should the `mktime` example use `(time_t)-1` instead of `-1`?](log_c90.md#issue0052.01)|Fixed in C90 TC1|
|0052.02|[Is the index entry for static correct?](log_c90.md#issue0052.02)|Fixed in C90 TC1|
|0052.03|[Does the C Standard come with a Rationale, as indicated in Footnote 1?](log_c90.md#issue0052.03)|Closed|
|0053|[Do the aliasing rules cover accesses to different function pointers properly?](log_c90.md#issue0053)|Fixed in C90 TC1|
|0054|[What is the behavior of various string functions with a specified length of zero?](log_c90.md#issue0054)|Fixed in C90 TC1|
|0055|[Must the `SIG*` macros have distinct values?](log_c90.md#issue0055)|Fixed in C90 TC1|
|0056|[How accurate must floating-point arithmetic be?](log_c90.md#issue0056)|Closed|
|0057|[Must there exist a user-accessible integral type for every pointer?](log_c90.md#issue0057)|Closed|
|0058|[What is the number of digits in a number that can be processed by the `scanf` family and the `strtod` family?](log_c90.md#issue0058)|Closed|
|0059|[Must an incomplete type be completed by the end of a translation unit?](log_c90.md#issue0059)|Closed|
|0060|[When an array of `char` (or `wchar_t`) is initialized with a string literal that contains fewer characters than the array, are the remaining elements of the array initialized?](log_c90.md#issue0060)|Fixed in C90 TC2|
|0061|[Interpretation of white space in the format string of a scan statement](log_c90.md#issue0061)|Closed|
|0062|[Can the `rename` function alway return a failure?](log_c90.md#issue0062)|Closed|
|0063|[This is [Defect Report 056](log_c90.md#issue0056)](log_c90.md#issue0063)|Closed|
|0064|[What is a null pointer constant?](log_c90.md#issue0064)|Closed|
|0065|[Can strictly conforming programs contain locales other that the 'C' locale?](log_c90.md#issue0065)|Fixed in C90 TC2|
|0066|[A set of locale questions](log_c90.md#issue0066)|Closed|
|0067|[Are the definitions of types clear?](log_c90.md#issue0067)|Closed|
|0068|[When are values of the type `char` treated as `signed`or `nonnegative` integers](log_c90.md#issue0068)|Closed|
|0069|[What is the meaning of *pure binary numeration system*?](log_c90.md#issue0069)|Closed|
|0070|[Can non-compatible types be used interchangeabily for function arguments?](log_c90.md#issue0070)|Closed|
|0071|[Are all enumerated types compatible with a single type?](log_c90.md#issue0071)|Fixed in C90 TC2|
|0072|[What is the definition of an object?](log_c90.md#issue0072)|Closed|
|0073|[Another definition of an object question](log_c90.md#issue0073)|Closed|
|0074|[Can the alignment of an object that is a member of a structure be different from the alignment of an object of the same type that is not a member of a structure?](log_c90.md#issue0074)|Closed|
|0075|[What is the alignment of allocated memory?](log_c90.md#issue0075)|Closed|
|0076|[A set of pointers to the end of arrays questions](log_c90.md#issue0076)|Closed|
|0077|[Is the address of an object constant throughout its lifetime?](log_c90.md#issue0077)|Closed|
|0078|[May optimizer invoke the as-if rule to rearrange code?](log_c90.md#issue0078)|Closed|
|0079|[Is the address of a standard library function the same in different translation units?](log_c90.md#issue0079)|Closed|
|0080|[Questions on merging of string constants](log_c90.md#issue0080)|Fixed in C90 TC2|
|0081|[What is the result of the left shift operator `E1 < E2`, when `E1` is signed?](log_c90.md#issue0081)|Closed|
|0082|[Many varargs questions](log_c90.md#issue0082)|Fixed in C90 TC2|
|0083|[A use of library functions question](log_c90.md#issue0083)|Fixed in C90 TC2|
|0084|[When is an incomplete type in function declaration a parameter?](log_c90.md#issue0084)|Closed|
|0085|[Is the return from `main` equivalent to calling `exit`?](log_c90.md#issue0085)|Fixed in C90 TC2|
|0086|[At object-like macros in system headers conforming?](log_c90.md#issue0086)|Closed|
|0087|[Is the order of evaluation when there are no sequence points well defined?](log_c90.md#issue0087)|Closed|
|0088|[Are two incomplete structure types with a (lexically) identical tag always compatible?](log_c90.md#issue0088)|Closed|
|0089|[When does multiple definitions of a macro require a diagnositc message?](log_c90.md#issue0089)|Fixed in C90 TC2|
|0090|[Multibyte characters in formats question](log_c90.md#issue0090)|Closed|
|0091|[Does a locale with multibye characters conform?](log_c90.md#issue0091)|Closed|
|0092|[Are the remaining elements in a partially initalized string guaranteed to be zero?](log_c90.md#issue0092)|Closed|
|0093|[Can a conforming freestanding implementation reserve identifiers?](log_c90.md#issue0093)|Fixed in C90 TC2|
|0094|[Is there an inconsistency between the constraints on passing values versus returning values?](log_c90.md#issue0094)|Closed|
|0095|[Are the initialization constraints clear?](log_c90.md#issue0095)|Closed|
|0096|[Can the element type in an array declarator be a non-object type?](log_c90.md#issue0096)|Closed|
|0097|[Can the `type` argument of the `offsetof` macro be an incomplete type?](log_c90.md#issue0097)|Closed|
|0098|[Do function types and incomplete type have size?](log_c90.md#issue0098)|Closed|
|0099|[What does the term *assignment operator* mean?](log_c90.md#issue0099)|Closed|
|0100|[Do functions return values by copying?](log_c90.md#issue0100)|Fixed in C90 TC1|
|0101|[Are mismatched qualifiers allowed?](log_c90.md#issue0101)|Fixed in C90 TC2|
|0102|[Does a constraint violation win over undefined behavior?](log_c90.md#issue0102)|Closed|
|0103|[Is a diagnostic required when formal parameters for functions are incomplete types?](log_c90.md#issue0103)|Closed|
|0104|[When is an incomplete type in function declaration a parameter?](log_c90.md#issue0104)|Closed|
|0105|[Does a constraint violation win over undefined behavior?](log_c90.md#issue0105)|Fixed in C90 TC1|
|0106|[Can one take the address of a void expression?](log_c90.md#issue0106)|Closed|
|0107|[Several `assert` questions](log_c90.md#issue0107)|Closed|
|0108|[Is it conforming to allow macros to make keywords?](log_c90.md#issue0108)|Closed|
|0109|[Does the C Standard draw any significant distinction between *undefined values* and *undefined behavior*?](log_c90.md#issue0109)|Closed|
|0110|[When is a formal parameter having array-of-non-object type not conforming?](log_c90.md#issue0110)|Closed|
|0111|[A question on conversion of *pointer-to-qualified* type values to type `(void*)` values](log_c90.md#issue0111)|Closed|
|0112|[A Null pointer constants and relational comparison question](log_c90.md#issue0112)|Closed|
|0113|[Return expressions in functions declared to return qualified `void` questions](log_c90.md#issue0113)|Closed|
|0114|[Initialization of multi-dimensional `char` array object questions](log_c90.md#issue0114)|Closed|
|0115|[What it means to *declare* a declarator?](log_c90.md#issue0115)|Closed|
|0116|[Is a diagnostic required when the address of a `reigister` arry is implicitly taken?](log_c90.md#issue0116)|Closed|
|0117|[Abstract semantics, sequence points, and expression evaluation question](log_c90.md#issue0117)|Closed|
|0118|[When is the `sizeof` an enumeration type known?](log_c90.md#issue0118)|Fixed in C90 TC2|
|0119|[Is a diagnostic required on an example of an initialization of multi-dimensional array objects](log_c90.md#issue0119)|Closed|
|0120|[Semantics of assignment to (and initialization of) bit-fields question](log_c90.md#issue0120)|Closed|
|0121|[What is ment by *size required* when convering a ponter value to an integral type?](log_c90.md#issue0121)|Closed|
|0122|[Is the *type* of a bit-field totally independent from its *width*?](log_c90.md#issue0122)|Closed|
|0123|[“*Type categories*” and qualified types question](log_c90.md#issue0123)|Closed|
|0124|[What is the difference between casts to *a void type* versus casts to the `void` type?](log_c90.md#issue0124)|Fixed in C90 TC2|
|0125|[When are declarations useing `extern` *(qualified)* `void` not conforming?](log_c90.md#issue0125)|Closed|
|0126|[What does *synonym* mean with respect to typedef names?](log_c90.md#issue0126)|Closed|
|0127|[What is the composite type of an enumeration and an integer?](log_c90.md#issue0127)|Closed|
|0128|[Editorial issue relating to tag declarations in type specifiers](log_c90.md#issue0128)|Closed|
|0129|[When is name spaces of tags are shared?](log_c90.md#issue0129)|Closed|
|0130|[When is data read from a text stream guaranteed to match what was written to the stream?](log_c90.md#issue0130)|Closed|
|0131|[What is the meaning of *const-qualification*?](log_c90.md#issue0131)|Fixed in C90 TC2|
|0132|[Can undefined behavior occur at translation time, or only at run time?](log_c90.md#issue0132)|Closed|
|0133|[Undefined behavior not previously listed in subclause G2](log_c90.md#issue0133)|Closed|
|0134|[Is *error number* an undefined term?](log_c90.md#issue0134)|Closed|
|0135|[Is the `SVR4 fwrite` different?](log_c90.md#issue0135)|Closed|
|0136|[Does `mktime` yield a -1 in the *spring-forward* gap when `tm_isdst` is -1?](log_c90.md#issue0136)|Closed|
|0137|[Is `printf("%.1f", -0.01)` required to produce `0.0` , `-0.0`, or are both acceptable?](log_c90.md#issue0137)|Closed|
|0138|[What are the storage durations?](log_c90.md#issue0138)|Fixed in C90 TC2|
|0139|[Is an incomplete type compatible with the completed type?](log_c90.md#issue0139)|Fixed in C90 TC2|
|0140|[What does *performed* and *other operation* mean?](log_c90.md#issue0140)|Closed|
|0141|[What does `EOF` mean in `<stdio.h>`?](log_c90.md#issue0141)|Closed|
|0142|[Is it permitted to `#undef` a reserved macro name?](log_c90.md#issue0142)|Fixed in C99|
|0143|[What are the definitions of file opening modes?](log_c90.md#issue0143)|Fixed in C99|
|0144|[Can the white space preceeding the initial `#` of a preprocessing directive be derived from macro expansion?](log_c90.md#issue0144)|Fixed in C99|
|0145|[The four possible forms for a constant expression are not consistent](log_c90.md#issue0145)|Fixed in C99|
|0146|[Does the constraint of 6.1.2 serve a purpose?](log_c90.md#issue0146)|Fixed in C99|
|0147|[Is there a requirement for a sequence point to occur within a library function?](log_c90.md#issue0147)|Fixed in C99|
|0148|[Is it clear when it is permitted to declare a library function?](log_c90.md#issue0148)|Closed|
|0149|[Is the term *variable* defiend?](log_c90.md#issue0149)|Fixed in C99|
|0150|[Are programs containing `char array[] = "Hello, World";` strictly conforming?](log_c90.md#issue0150)|Fixed in C99|
|0151|[Is the out from `printf("%#.0o", 0);` ambiguous?](log_c90.md#issue0151)|Closed|
|0152|[Can `longjmp` be used to return from a signal handler invoked other than through `abort` or `raise`?](log_c90.md#issue0152)|Closed|
|0153|[Is there a problem with empty arguments in macro calls?](log_c90.md#issue0153)|Closed|
|0154|[What restrictions apply to implementation-defined entities?](log_c90.md#issue0154)|Closed|
|0155|[Is the word *unique* in subclause 7.10.3 ambiguous?](log_c90.md#issue0155)|Fixed in C99|
|0156|[Should calls to `fsetpos` with positions in closed and reopened streams be undefined?](log_c90.md#issue0156)|Fixed in C99|
|0157|[Is it clearly indicated when the spelling of a type name is or is not significant?](log_c90.md#issue0157)|Fixed in C99|
|0158|[Are the semantics for the explicit conversion of null pointer constants defined?](log_c90.md#issue0158)|Fixed in C99|
|0159|[Is the introduction to the C Standard confusing?](log_c90.md#issue0159)|Fixed in C99|
|0160|[It is unclear what applications can and cannot do with identifiers that are reserved?](log_c90.md#issue0160)|Fixed in C99|
|0161|[Is the wording of subclause 7.13 unclear?](log_c90.md#issue0161)|Closed|
|0162|[Is the description of the static objects used by `time.h` functions misleading?](log_c90.md#issue0162)|Fixed in C99|
|0163|[Is it clear whether the use of an undeclared identifier as a primary expression requires a diagnostic message to be issued?](log_c90.md#issue0163)|Closed|
|0164|[Is there a constraint to prevent declarations involving types not defined by subclause 6.1.2.5?](log_c90.md#issue0164)|Closed|
|0165|[Is the wording of subclause 6.5.2.3 concerning tags defective?](log_c90.md#issue0165)|Fixed in C99|
|0166|[Do constraints that require something to be an lvalue place an unacceptable burden on the implementation?](log_c90.md#issue0166)|Fixed in C99|
|0167|[The `n` conversion specifier in subclause 7.9.6.2 made by TC1, [Defect Report #014, Question 2](log_c90.md#issue0014.02), should be applied to subclause 7.9.6.1](log_c90.md#issue0167)|Fixed in C99|
|0168|[The change to subclause 6.3 made by TC1, [Defect Report #053, Question 1](log_c90.md#issue0053), should also be applied in Annex .2 (page 200\)](log_c90.md#issue0168)|Fixed in C99|
|0169|[Is the description of the replacement of trigraphs contradictory?](log_c90.md#issue0169)|Closed|
|0170|[Are the description of operators and punctuators is confusing, and are the constraints contradictory?](log_c90.md#issue0170)|Fixed in C99|
|0171|[Is it possible to create implementations with unreasonable arrangements of integral types?](log_c90.md#issue0171)|Fixed in C99|
|0172|[Does the description for the relational and equality operators contain defects?](log_c90.md#issue0172)|Fixed in C99|
|0173|[What is the meaning of *line number* when a token is split over more than one physical source line?](log_c90.md#issue0173)|Closed|
|0174|[Is there a number of errors in the usual arithmetic conversions section?](log_c90.md#issue0174)|Fixed in C99|
|0175|[Is the `sscanf` example added by TC1 wrong?](log_c90.md#issue0175)|Fixed in C99|
|0176|[Are rules concerning whether `#error` generates a diagnostic contradictory?](log_c90.md#issue0176)|Closed|
|0177|[A Preprocessing directives question](log_c90.md#issue0177)|Fixed in C99|
|0178|[Why does [Defect Report #051](log_c90.md#issue0051) and [Defect Report #073](log_c90.md#issue0073) answer the same question differently?](log_c90.md#issue0178)|Closed|

---

<div id="issue0001">

## Issue 0001: Do functions return values by copying?

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-009  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0100](log_c90.md#issue0100)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_001.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_001.html)

Do functions return values by copying?

The C Standard is clear (in subclause 6.3.2.2) that function arguments are
copied, but is not clear (in subclause 6.6.6.4) whether a function's returned
value is also copied. This question becomes an issue in the assignment statement
`s=f();` where `f` yields a structure: is the result defined when the structure
`s` overlaps the structure that `f` obtained the returned value from?

I ask this question because the GNU C compiler does not copy the structure in
this case. When I filed the enclosed bug report \[omitted from this document],
Richard Stallman, the author of GNU C, replied that he didn't think that
Standard C required the extra copy. I sympathize with Stallman's desire for
efficient code, and I also would prefer that the C Standard did not require the
extra copy here, but the point should be made clear in the C Standard.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.6.6.4, page 80, lines 30-32, replace:***

If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.

***with:***

If the expression has a type different from the return type of the function in
which it appears, the value is converted as if by assignment to an object having
the return type of the function.**\***

\[Footnote \*: The `return` statement is not an assignment. The overlap
restriction in subclause 6.3.16.1 does not apply to the case of function
return.]

***Add to subclause 6.6.6.4, page 80:***

**Example**

In:

```c
struct s {double i;} f(void);
 union {struct {int f1;
                struct s f2;} u1;
        struct {struct s f3;
                int f4;} u2;
       } g;
 struct s f(void)
         {
         return g.u1.f2;
         }
 /* ... */
 g.u2.f3 = f();
```

the behavior is defined.


</div>


---

---

<div id="issue0002">

## Issue 0002: Should `\` be escaped within macro actual parameters?

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-010  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_002.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_002.html)

Subclause 6.8.3.2: Semantics of `#`

A minor detail in the semantics is that it does not explicitly state that a `\`
character will be inserted before a `\` character that occurs within a macro
actual parameter, only when the `\` character occurs within a string literal or
character constant within the actual parameter.

I can see that there is an argument concerning the systems where `\` is a valid
part of a path name and where `#include` path names are desired to be built
dynamically and then `#`ed.

Would it not be better, however, to escape all `\` within actual parameters and
require either

a. that systems using `\` in path names escape them within`#include` strings, or
perhaps

b. that during macro processing of `#include` parameters the `#` operator will
not cause `\` characters to be escaped at all or will be implementation defined?

This second case (b) is better, as strings for `#include` directives are already
a special case (no escape processing, etc.), so should not the `#` operator also
be special for `#include` directives?

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous response to this item from David F. Prosser (Editor of the standard).
The Committee endorses the substance of this response, which follows: The rules
in subclause 6.8.3.2 regarding `\` were discussed in the Committee and the
result is as intended. The Committee's charter was to standardize prior art
where such was clear, and the behavior of those C preprocessing phases that
allowed tokens such as `\` left them alone, even when inserting them into
strings. However, the Committee also had license to fix or add to the language
where it was judged to be deficient. Since none of the existing stringizing
preprocessing phases correctly handled string literals and certain character
constants, the special rules for these were chosen. Subclause 6.8.3's examples
(page 92, lines 4-33) include a `\` that is outside of a string literal or
character constant. If the rules were to be modified along the lines of your
proposal, the intended effect would not happen. One of the main points in your
argument is that uncontained `\`s are only critical in path names that use `\`
as a special character, and that this is only needed when `#include` filenames
are constructed via macro replacement. I agree that the current rules do allow
this sort of use without too much trouble, but I don't see this as being a main
motivation for this feature. By default, the rules for stringizing were that the
original spelling of the invocation argument is placed into a string literal.
The only exceptions made to this were those that were valid C tokens that could
not be simply inserted between a pair of `"`s. The rules for `\` and `"` within
string literals and character constants were derived from that need only.
Furthermore, a lone `\` is a preprocessing token due to the “some other
character” rule of the syntax from subclause 6.1. This would be the only place
where special constraints were placed on one of this type of preprocessing
token.

Finally, solution b) of your discussion involves context-dependent rules for the
stringizing operation. While there is a minor context dependency regarding macro
replacement and the `defined` unary operator on `#if` and `#elif` directive
lines, this is the only context dependency in the whole set of macro replacement
rules. Moreover, this dependency is at the topmost level only. Solution b) would
require a flag noting whether the result of the replacement was to be used
within a `#include` directive. Therefore, the same macro invocation would
produce different results at different invocations. (At the least, debugging
and/or testing of a tricky macroized `#include` directive would be more
difficult.)

In conclusion, to the best of my knowledge, the Committee wants to keep the
behavior here as currently described, and made this choice intentionally.


</div>


---

---

<div id="issue0003.01">

## Issue 0003.01: Are preprocessing numbers too inclusive?

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.1.8: Preprocessing numbers I note from the rationale document of
November 1988, X3J11 Document Number 88-151, that the following problem has been
observed. I am surprised at the Committee's decision to allow such a loose
description. Under the grammar given for a `pp-number`

```c
0xEE+23     0x7E+macro      0x100E+value-macro
```

are preprocessing numbers and as such a conforming C compiler would be required
to generate an error when it failed to successfully convert them to actual C
language number tokens. The solution is simply to restrict the inclusion of
\[`eE`]\[`+-`] within a *`pp-number`* to situations where the `e` or `E` is the
first *`non-digit`* in the character sequence composing the preprocessing
number. This can be easily implemented in a variety of methods; the informal
description above gives perhaps a better guide to efficient implementation than
the following revised grammar:

```c
pp-number:
         pp-float
         pp-number digit
          pp-number .
         pp-number non-digit  /* A non-digit is a letter or underscore */

 pp-float:
         pp-real
         pp-real E sign         pp-real e sign

 pp-real:
         digit
         .
         pp-real digit
         pp-real .
```

It is unbelievable that a standards committee could so lose sight of its
objective that it would, in full awareness, make simple expressions illegal.

To illustrate the absurdity of the rationale document's claim that the faulty
grammar was felt to be easier to implement, why not adopt the following grammar
for a *`pp-number`* and really make life simple; after all, who wants to have
their preprocessor slowed down by checking whether the `+` or `-` was preceded
by a n `e`or an `E`?

```c
pp-number:
         digit
         .
         pp-number digit
         pp-number .
         pp-number non-digit
         pp-number sign
```

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous responses to this item from David F. Prosser. The Committee endorses
the substance of these responses, which follow: In response to your first
suggested grammar: This grammar doesn't include all valid numeric constants and
exclude other important tokens. For example, `.` is derivable. But let's assume
that you intended something like

```c
pp-number:
         pp-float
         digit
         pp-number digit
         pp-number non-digit

 pp-float:
         pp-real
         pp-float E sign
         pp-float e sign
         pp-float digit
         pp-float .
         pp-float non-digit

 pp-real:
         digit
         . digit
         pp-real digit
         pp-real .
```

This grammar is certainly more complicated than the one-level construction in
the C Standard, and consequently harder to understand. That's a strike against
it. Another strike is that, while it does mimic the two major numeric
categories, it still doesn't include all sequences covered by the existing
grammar, save those that would otherwise be valid by the stricter tokenization
rules. For example, `0b0101e+17` might be someone's future notion of a binary
floating constant. Finally, it suffers from a great deal of reduce/reduce
conflicts, making the implementation and specification less likely to be
understood and implemented as intended. In response to your second suggested
grammar: This could have been done. But the Committee chose a compromise at a
different point \- one that restricts the inappropriate gobbling of characters
to `+` and `-` immediately after `E` or `e`. This was all that was necessary to
cover all valid numeric constants in as simple a grammar as was possible. For
more background, you'd need to know the state of the proposed standard a few
years before this grammar was voted in. The Committee had stated its intent that
“garbage” character sequences that began like a numeric constant were to be
tokenized as a single sequence. This was to prevent situations in which this
“garbage” would be turned into valid C code through obscure macro replacements,
among more minor reasons. This was, unfortunately, very poorly stated in the
draft. As I recall, it was placed in the constraints for subclause 6.1. It was
something like “Each pair of adjacent tokens that are both keywords,
identifiers, and/or constants must be separated by white space.” \[As “improved”
for the May 1, 1986 draft proposed standard, subclause 6.1 **Constraints**
consisted of the single sentence: “Each keyword, identifier, or constant shall
be separated by some white space from any otherwise adjacent keyword,
identifier, or constant.”] As you can see, this constraint neither presented the
intent of the Committee nor caused implementations to behave in any sort of
consistent manner with respect to tokenization. Finally a letter writer
understood the issue well enough to suggest a grammar along the lines of the
current subclause 6.1.8. It, contrary to your opening remarks on this topic, is
*not* a “loose description,” and it finally stated in a precise way the intent
of the tokenization rules. The benefits of this construction were that all
tokenization for all implementations would now be the same, no “garbage”
character sequences would be able to be converted to valid C code, skipped
blocks of code could silently be scanned without generating needless and
unnecessary tokenization errors, the preprocessing tokenization of numeric
tokens would be greatly simplified, and room for future expansion of C's numeric
tokens was reserved. That's a lot of good. The down side was that certain
sequences now would require some white space to cause them to be tokenized as
the programmer intended. As noted in the rationale document, there are other
parts in C that require white space for tokenization to be controlled, and this
was found to be one more. Since the “mistokenization” of such sequences must
result in some diagnostic noise from the compiler, and since the fix is so mild,
the Committee agreed that the proposed standard is still much better with this
grammar than with any of the other suggestions. Personally, I think that the
biggest surprise “win” was the reservation of future numeric token “name space.”
I would not be at all surprised to find binary constants (that begin with `0b`)
in newer C implementations.


</div>


---

---

<div id="issue0003.02">

## Issue 0003.02: Should white space surround macro substitutions?

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Macro substitutions, tokenization, and white space In general I
think it is a good guiding principle that a C implementation should be able to
be based around completely disjoint preprocessing and lexical scanning parses of
the compiler. As such the rules on tokenizing need to be emphasized with the
following paragraphs (possibly placed after paragraph 1 of subclause 6.8.3.1):

> All macro substitutions and expanded macro argument substitutions will result in
> an additional space token being inserted before and after the replacement token
> sequence where such a space token is not already present and there is a
> corresponding preceding or subsequent token in the target token sequence.
>
> The last token of every macro argument has no subsequent token at the time of
> its initial macro argument expansion, and similarly a macro parameter that is
> the last token of a replacement token list has no subsequent token at the time
> of that parameter's substitution. Similarly for first tokens and preceding
> tokens.

Naturally such a step can be treated as purely conceptual by a tokenized
implementation with combined preprocessing and lexical analysis, except for the
purposes of argument stringizing where the added spacing may be essential for
unambiguous identification of the preprocessing tokens involved. Such a
statement is not a substantive change, as it is merely clarifying the
tokenization rules, and given that Standard C has changed the definition of the
preprocessor substantially from K\&R already (re macro argument expansion before
substitution) such an additional explicit change from K\&R C should cause
comparatively little difficulty except to those who had not appreciated just how
different the preprocessing rules are already. Examples which are clarified by
this change are:

```c
#define    macro    +
            +macro
            macro+
  #define    mac()    +
 #define    ro       +
            mac()ro
```

all of which unambiguously result in lines with two `+` operator tokens, in
strict accordance with the draft standard's tokenization rules, and not, as was
formerly the case with traditional text oriented preprocessors, in single `++`
operators.

Examples which are changed by this statement are:

```c
#define    mac()         +
 #define    ro            +
 #define    str(s)        # s
 #define    eval(m,e)     m(e)
            eval( str, mac()ro )
```

which produces the string `"+N+"` and not the string `"++"` as it would do with
the draft's current wording.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous responses to this item from David F. Prosser. The Committee endorses
the substance of these responses, which follow: KR never specified the macro
replacement algorithm to the extent that any such conclusion is possible. The
widest range of implementation choices were present in this area of the
language. The eventual choice of a macro replacement algorithm was one that did
not match any existing implementation, but one that tried to include the
behavior of all major variants. You agree that the C Standard is clear that once
a token is recognized, it is never retokenized unless subjected to a `#` or `##`
operation. The behavior described is that which was chosen by the Committee.
Your proposal would cause, as you note, certain created string literals to
include white space not present in the original text. This runs counter to the
`#` operator's goal of producing a string version of the spelling of the
invocation arguments. The C Standard allows an implementation that uses a
text-to-text separate preprocessing stage the option to use white space as
necessary to separate tokens when it produces its output. However, this
insertion of white space must not be visible to the program. The proposed extra
white space would probably be a surprise to the programmer as well. Finally,
this proposal would require those implementations that have a built-in
preprocessing stage to add extra code to insert white space in special
circumstances. This is counter to the goal of having both built-in and separate
implementations be purely an implementation choice.


</div>


---

---

<div id="issue0003.03">

## Issue 0003.03: Is an empty macro argument a constraint violation?

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Status: Closed  
Cross-references: [0153](log_c90.md#issue0153)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Empty arguments to function-like macros I would like to make a
request for clarification and a request for a stronger statement of
standardization. Given

```c
#define macro( xx ) xx
         macro()
```

is this a constraint violation of subclause 6.8.3 **Constraints** paragraph 4:

> The number of arguments in an invocation of a function-like macro shall agree
> with the number of parameters in the macro definition, ...

or is this an undefined, implementation-dependent program \- subclause 6.8.3,
**Semantics** paragraph 5:

> If (before argument substitution) any argument consists of no preprocessing
> tokens, the behavior is undefined.

In connection with the above I would request that the Committee make a much
stronger statement as to whether empty arguments are to be treated as valid
arguments or are to be treated as errors. They can have their uses, but if that
is recognized then it should be standardized; if not, it should not be allowed.

---

Comment from WG14 on 1997-09-23:

### Response

If one takes the general case, empty arguments in invocations of function-like
macros are easy to recognize:

```c
#define f(a,b,c) whatever

         f(,,)
```

These empty arguments all have “shadows” that cause the sentence you reference
in subclause 6.8.3 (page 90, lines 4-5) to be clearly in effect.

The only uncertain case is one in which an empty argument in an invocation of a
one-parameter function-like macro mimics a “no arguments” invocation. (It should
also be noted that the definition of a macro argument from clause 3 does not
preclude an empty sequence.) Thus the standard is clear that the behavior is
undefined in the example from your request. If an implementation does not choose
to allow empty arguments, a diagnostic will probably be emitted; otherwise, the
invocation will most likely be replaced by a preprocessing token sequence in
which the parameter is replaced with no tokens. But because the standard does
not define this, other than as a common extension, there are no guarantees.


</div>


---

---

<div id="issue0003.04">

## Issue 0003.04: Should preprocessing directives be permitted within macro invokations?

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Preprocessor directives within actual macro arguments It is a
guiding principle that a macro function and an actual function should be
invokable in as similar fashion as possible. In the latter case, it is not
uncommon to find code with variations of arguments subject to conditional
compilation. This should also compile correctly if an appropriate macro
definition is made for the function.

While conditional compilations within function arguments is not necessarily a
programming style that I would condone, I feel that it is in the interests of
the C programming community at large for such constructs to be well formed, even
if forbidden, and as such make the following requests:

> I would like the Committee to change subclause 6.8.3 to state that `#if`,
> `#ifdef`, `#ifndef`, `#else`, `#elif`, and `#endif` preprocessing directives are
> allowed within actual macro arguments (not necessarily cleanly nested).
> Conversely, I would like `#define` and `#undef` to be formally forbidden within
> macro invocations, as these can result in effects that are dependent on the
> particular implementation of the macro expansions.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous response to this item from David F. Prosser. The Committee endorses the
substance of this response, which follows: The equivalent of your proposal was
rejected a couple of years ago. Certain Committee members felt that requiring
all preprocessors to recognize these lines as directives was too much. Those
that felt that these lines must be recognized were finally convinced that it was
enough to allow implementations the right to behave in the more orthogonal
manner. (Maybe they figure that the next version of the standard will have to
require this sort of behavior, as all “reasonable” implementations already will
have it by then.)


</div>


---

---

<div id="issue0004">

## Issue 0004: Are multiple definitions of unused identifiers with external linkage permitted?

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-012  
Status: Fixed  
Fixed in: C90  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_004.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_004.html)

Are multiple definitions of unused identifiers with external linkage permitted?

The wording in subclause 6.7 permits multiple definitions of identifiers with
external linkage, so long as the identifiers are never used. For example, the
following program is “strictly conforming” if you read the wording in subclause
6.7 literally:

```c
int F() {return 0;}
 int F() {return 1;}
 int V = 0;
 int V = 1;
 int main() {return 0;}
```

This must be a bug in the wording of subclause 6.7. It cannot have been the
Committee's intent, since it prohibits the most commonly encountered linker
model. For example, most linkers will flatly refuse to link the following
“strictly conforming” program

```c
x.c:
```

> ```c
> int F() {return 0;}
>      int G(int i) {return i;}
> ```

y.c:

> ```c
>     int F() {return 1;}
>      int G(int);
>      int main() {return G(0);}
> ```

because `F` is defined twice.

---

Comment from WG14 on 1997-09-23:

### Response

This Defect Report referred to an earlier draft of the C Standard, and was
corrected prior to the publication of the C Standard.


</div>


---

---

<div id="issue0005">

## Issue 0005: May a conforming implementation define and recognize a pragma which would change the semantics of the language?

Authors: Walter J. Murray, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-020  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_005.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_005.html)

According to subclause 6.8.6, a pragma directive “causes the implementation to
behave in an implementation-defined manner.” May a conforming implementation
define and recognize a pragma which would change the semantics of the language?
For example, might a conforming implementation recognize and honor the directive

```c
#pragma UNSIGNED_PRESERVING
```

as a way for a program to request non-standard integral promotions?

I also pose the corollary question. May a strictly conforming program contain a
pragma directive? According to subclause 4, a strictly conforming program “shall
use only those features of the language ... specified in this standard. It shall
not produce output dependent on any unspecified, undefined, or
implementation-defined behavior...”

If there is no constraint on how a conforming implementation may behave when
encountering a pragma directive, would it not follow that a strictly conforming
program may not contain a pragma directive?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 6.8.6:

> A ... `pragma` ... causes the implementation to behave in an
> implementation-defined manner.

and clause 4:

> A strictly conforming program ... shall not produce output dependent on any ...
> implementation-defined behavior ...

In response to each question:

1. Yes, a conforming implementation may define and recognize a pragma which would change the semantics of the language.
2. Yes, for example, it might honor `UNSIGNED_PRESERVING`.
3. No, a strictly conforming program may not contain a pragma directive.
4. We agree with your conclusion, reasserting answer number 3\.


</div>


---

---

<div id="issue0006">

## Issue 0006: How does `strtoul` behave when presented with a subject sequence that begins with a minus sign?

Authors: Walter J. Murray, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-020  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_006.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_006.html)

It is unclear how the `strtoul` function behaves when presented with a subject
sequence that begins with a minus sign. The `strtoul` function is described in
subclause 7.10.1.6, which contains the following statements.

> If the subject sequence begins with a minus sign, the value resulting from the
> conversion is negated.
>
> If the correct value is outside the range of representable values, `ULONG_MAX`
> is returned, and the value of the macro `ERANGE` is stored in `errno`.

Assume a typical 32-bit, two's-complement machine with the following limits.

```c
LONG_MIN    -2147483648
 LONG_MAX         2147483647
 ULONG_MAX        4294967295
```

Assuming that the value of `base` is zero, how should `strto ul` behave (return
value and possible setting of `errno`) when present ed with the following
sequences? Case 1: `"-2147483647"` Case 2: `"-2147483648"` Case 3:
`"-2147483649"`

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are the ones supplied by you from subclause 7.10.1.6: If
the subject sequence begins with a minus sign, the value resulting from the
conversion is negated. If the correct value is outside the range of
representable values, `ULONG_MAX` is returned, and the value of the macro
`ERANGE` is stored in `errno`. The Committee believes that there is only one
sensible interpretation of a subject sequence with a minus sign: If the subject
sequence (neglecting the possible minus sign) is outside the range \[0,
`ULONG_MAX`], then the range error is reported. Otherwise, the value is
negated(as an `unsigned long int`). The answers to your numeric questions are:

Case 1: 2,147,483,649

Case 2: 2,147,483,648

Case 3: 2,147,483,647


</div>


---

---

<div id="issue0007">

## Issue 0007: Are declarations of the form `struct` *`tag`* permitted after *`tag`* has already been declared?

Authors: Paul Eggert, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-043  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_007.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_007.html)

Are declarations of the form `struct-or-union identifier ;` permitted after the
`identifier` tag has already been declared? Here are some examples of the
problem:

```c
/*1*/ struct s;
 /*2*/ struct s;
 /*3*/ struct s {int a;};
 /*4*/ struct s;
 /*5*/ struct t {int a;};
/*6*/ struct t;
```

Subclause 6.5 says “A declaration shall declare at least a declarator, a tag, or
the members of an enumeration.” In this sense, does `/*`*`2`*`*/` also declare
the tag `s`? If so, then surely all of the above lines are conforming. But if
not, then in what sense does `/*`*`3`*`*/` declare a tag and thus satisfy
subclause 6.5's constraint?

The example at the end of subclause 6.5.2.3 says “To eliminate this context
sensitivity, the otherwise vacuous declaration `struct s2;` may be inserted ...”
This seems to imply that `/*`*`2`*`*/`, `/*`*`4`*`*/`, and `/*`*`6`*`*/` are not
conforming, because the y are vacuous. But how can this be reconciled with the
above argument?

---

Comment from WG14 on 1997-09-23:

### Response

The declaration

```c
struct s;
```

declares the tag `s`. It need not be the first or only declaration of the tag
`s` within a given scope to qualify as a declaration of `s`, just as

```c
int i;
```

declares `i` however often it is repeated. The applicable constraint is in
subclause 6.5: “A declaration shall declare at least a declarator, a tag, or the
members of an enumeration.” Clearly,

```c
struct s;
```

declares the tag `s`.

Subclause 6.5.2.3, in the examples, characterizes a declaration of this form as
“otherwise vacuous” in the draft you read. The words “otherwise vacuous” were an
editorial comment that was omitted from the International Standard. These words
were intended to mean “other than declaring `s2` to be an (incomplete) struct
type,” and should not be read as saying that the declaration fails to declare
the tag.

We believe that this interpretation is consistent with the intent of the
Committee, and that a reasonable reading of the standard supports this
interpretation.


</div>


---

---

<div id="issue0008.01">

## Issue 0008.01: Is dead-store elimination permitted near `setjmp`?

Authors: Otto R. Newman, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-021  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_008.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_008.html)

Could you tell me if it is legitimate for a conforming C compiler to perform
what's commonly referred to as dead-store elimination for the first assignment
in the following code fragment:

```c
auto int flag;      /* non-volatile */
 ...
 flag = 1;
 flag = f();
```

If it is valid to do so, then consider

```c
auto int flag;      /* non-volatile */
 if (setjmp(buf))
    {
     if (flag == 1) ...
    }
 flag = 1;
 flag = f();
```

where function `f` invokes `longjmp`. Is the result of the relational expression
defined? A solution might be to define `flag` as `volatile`, but `flag` is *not*
really volatile, and the programmer may not wish to degrade all references to
`flag` nor to locate all such possible `flag`s and lie about their volatility. A
related issue is that in many existing applications, users have coded
`setjmp`-like mechanisms based on a particular operational environment. The
functions do not have the name “`setjmp`,” but essentially establish an
externally accessible entry point within the containing function. Sometimes,
pointers are set to reference such functions, even though the standard precludes
this from being done with `setjmp` itself since it is allowable that it only be
provided as a macro.

There are a number of additional optimizations which must be inhibited across
the actual invocation of `setjmp`, or a `setjmp`-like function. Always avoiding
these optimizations as well as the dead-store elimination shown in the example
may make the program safe for non-local jumps, but unnecessarily penalizes
programs that don't use `setjmp`. To circumvent this problem, some implementors
have defined a pragma which is included in `setjmp.h` to identify “`setjmp`” as
having the property of establishing an externally accessible entry, i.e.,
defining an otherwise non-obvious point of control flow. Other implementations
have hard-coded tests for the name “`setjmp`.”

... would you please respond to the question regarding the legitimacy of the
optimization in the first example?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citation is subclause 7.6.2.1:

> All accessible objects have values as of the time `longjmp` was called, except
> that the values of objects of automatic storage duration that are local to the
> function containing the invocation of the corresponding `setjmp` macro that do
> not have volatile-qualified type and have been changed between the `setjmp`
> invocation and `longjmp` call are indeterminate.

In response to your question about the effect on optimizations of `setjmp`: Yes,
it is legitimate for a compiler to perform optimizations that eliminate dead
stores to local, non-volatile, automatic variables when `setjmp` is used.
Subclause 7.6.2.1 makes the values of all such variables indeterminate after the
`longjmp` is called. This grants a compiler the liberty to perform dead-store
elimination as well as several other optimizations.


</div>


---

---

<div id="issue0008.02">

## Issue 0008.02: Should volatile functions be added?

Authors: Otto R. Newman, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-021  
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


</div>


---

---

<div id="issue0009">

## Issue 0009: Are typedef names sometimes ambiguous in parameter declarations?

Authors: Bruce Blodgett, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-023  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.12](log_c90.md#issue0017.12)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_009.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_009.html)

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
more, but this will suffice.]

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.4.3, page 68, lines 2-4, replace:***

In a parameter declaration, a single typedef name in parentheses is taken to be
an abstract declarator that specifies a function with a single parameter, not as
redundant parentheses around the identifier for a declarator.

***with:***

If, in a parameter declaration, an identifier can be treated as a typedef name
or as a parameter name, it shall be taken as a typedef name.


</div>


---

---

<div id="issue0010">

## Issue 0010: Is the typedef to an incomplete type valid?

Authors: Michael S. Ball, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-044  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_010.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_010.html)

Consider:

```c
typedef int table[];        /* line 1 */

 table one = {1};        /* line 2 */

 table two = {1, 2};     /* line 3 */
```

First, is the typedef to an incomplete type legal? I can't find a prohibition in
the standard. But an incomplete type is completed by a later definition, such as
line 2, so what is the status of line 3?

The type, of which `table` is only a synonym, can't be completed by line 2 if it
is to be used in line 3\. And what is `sizeof(table)`? What old C compilers seem
to do is treat the typedef as some sort of textual equivalent, which is clearly
wrong.

---

Comment from WG14 on 1997-09-23:

### Response

A typedef of an incomplete type is permitted.

Regarding objects `one` and `two`, refer to the standard subclause 6.1.2.5, page
24, lines 8-9: “An array of unknown size is an incomplete type. It is completed,
*for an identifier of that type,* by specifying the size in a later declaration
...” \[emphasis added]. The types of objects `one` and `two` are completed but
the type `table` itself is *never* completed. Hence, `sizeof(table)` is not
permitted.

An example very similar to that submitted is shown in example 6, subclause 6.5.7
on page 74, lines 16-23.


</div>


---

---

<div id="issue0011.01">

## Issue 0011.01: When do the types of multiple external declarations get formed into a composite type?

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0034.01](log_c90.md#issue0034.01)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Merging of declarations for linked identifier

When more than one declaration is present in a program for an externally-linked
identifier, exactly when do the declared types get formed into a composite type?

Certainly, if two declarations have file scope, then after the second, the
effective type for semantic analysis is the composite type of the two
declarations (subclause 6.1.2.6, page 25, lines 19-20). However, if one
declaration is in an inner scope and one is in an outer scope, are their types
formed into a composite type?

In particular, consider the code:

```c
{
 extern int i[];
 {
     /* a different declaration of the same object */
     extern int i[10];
 }
 /* Is the following legal?
    That is, does the outer declaration
    inherit any information from the inner one?  */
 sizeof (i);
 }
```

Similar situations can be constructed with internally linked identifiers. For
instance:

```c
/* File scope */
 static int i[];

 main()
 {
 /* a different declaration of the same object */
 extern int i[10];
 }

 /* Is the following legal?
    That is, does the outer declaration
    inherit any information from the inner one?*/
 int j = sizeof (i);
```

Further variants of this question can be asked:

```c
{
 extern int i[10];
 {
     /* a different declaration of the same object */
     extern int i[];

     /* Is the following legal?
        That is, does the inner declaration
        inherit any information from the outer one? */
      sizeof (i);
 }
 }
```

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.6, page 25, lines 19-20, change:***

For an identifier with external or internal linkage declared in the same scope
as another declaration for that identifier, the type of the identifier becomes
the composite type.

***to:***

For an identifier with internal or external linkage declared in a scope in which
a prior declaration of that identifier is visible**\***, if the prior
declaration specifies internal or external linkage, the type of the identifier
at the latter declaration becomes the composite type.

\[Footnote \*: As specified in 6.1.2.1, the latter declaration might hide the
prior declaration.]


</div>


---

---

<div id="issue0011.02">

## Issue 0011.02: Does `extern` link to a static declaration that is not visible?

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Interpretation of `extern`

Consider the code:

```c
/* File scope */
 static int i;           /* declaration 1 */

 main()
 {
 extern int i;           /* declaration 2 */
 {
     extern int i;       /* declaration 3 */
 }
 }
```

A literal reading of subclause 6.1.2.2 says that declarations 1 and 2 have
internal linkage, but that declaration 3 has external linkage (since declaration
1 is not visible, being hidden by declaration 2). (This combination of internal
and external linkage is undefined by subclause 6.1.2.2, page 21, lines 27-28.)

Is this what is intended?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.2, page 21, change:***

If the declaration of an identifier for an object or a function contains the
storage-class specifier `extern`, the identifier has the same linkage as any
visible declaration of the identifier with file scope. If there is no visible
declaration with file scope, the identifier has external linkage.

***to:***

For an identifier declared with the storage-class specifier `extern` in a scope
in which a prior declaration of that identifier is visible**\***, if the prior
declaration specifies internal or external linkage, the linkage of the
identifier at the latter declaration becomes the linkage specified at the prior
declaration. If no prior declaration is visible, or if the prior declaration
specifies no linkage, then the identifier has external linkage. \[Footnote \*:
As specified in 6.1.2.1, the latter declaration might hide the prior
declaration.]


</div>


---

---

<div id="issue0011.03">

## Issue 0011.03: Are implicit initializers for tentative array definitions syntactically valid?

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Initialization of tentative definitions

If the file scope declaration

```c
int i[10];
```

appears in a translation unit, subclause 6.7.2 suggests that it is implicitly
initialized as if

```c
int i[10] = 0;
```

appears at the end of the translation unit. However, this initializer is
invalid, since subclause 6.5.7 prescribes that the initializer for any object of
array type must be brace-enclosed. We believe that the intention of subclause
6.7.2 is that this declaration has an implicit initializer of

```c
int i[10] = {0};
```

Is this true?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.7.2 **External object definitions** contains the following excerpt:

> If a translation unit contains one or more tentative definitions for an
> identifier, and the translation unit contains no external definition for that
> identifier, then the behavior is exactly as if the translation unit contains a
> file scope declaration of that identifier, with the composite type as of the end
> of the translation unit, with an initializer equal to 0\.

This statement describes an effect and not a literal token sequence. Therefore,
this example does not contain an error.


</div>


---

---

<div id="issue0011.04">

## Issue 0011.04: Does an incomplete array get completed as a tentative definition?

Authors: Rich Peterson, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-008  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_011.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_011.html)

Tentative definition of externally-linked object with incomplete type

If one writes the file-scope declaration

```c
int i[];
```

then subclause 6.7.2 suggests that at the end of the translation unit the
implicit declaration

```c
int i[] = {0};
```

or equivalently

```c
int i[1] = {0};
```

appears. This seems peculiar, since subclause 6.7.2, (page 83, lines 35-36)
specifically forbids this case for internally linked identifiers.

Is this what is intended?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.7.2, page 84, a second Example:***

If at the end of the translation unit containing

```c
int i[];
```

the array `i` still has incomplete type, the array is assumed to have one
element. This element is initialized to zero on program startup.


</div>


---

---

<div id="issue0012">

## Issue 0012: Can one take the address of a void expression?

Authors: David F. Prosser, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-046  
Status: Closed  
Cross-references: [0076](log_c90.md#issue0076), [0106](log_c90.md#issue0106), [0125](log_c90.md#issue0125)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_012.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_012.html)

Bug in Standard C

I was asked a question about the validity of various expressions. Among the list
there was the following:

```c
void *p; &*p;
```

After doing a quick pass through the standard, I found nothing that disallowed
such. Moreover, back in September 1987's meeting (I didn't just recall the date
... it took a while to find when it occurred), I distinctly remember a Committee
discussion that involved the validity of the expression above. It was as a
result of this discussion and vote that the draft was changed to allow the
above.

Anyway, I wrote back that the expression was valid. This was eventually followed
by a letter from Dennis \[Ritchie] pointing out the mistake I made. As it turns
out, the definition of lvalue makes at least the unary `&` part of the above a
constraint violation. (As Bill \[Plauger] would say, “I know what the standard
was *supposed* to specify.”)

This would be just another, “Oops, well I guess I can live with it” surprise in
the standard, except that it turns out that unary `&` of a `void` type is
useful! What it provides is a construction that gives C a notion of an address
symbol. You are familiar with the symbols that are created by the UNIX linker:
`etext`, `e data`, and `end`, which designate special addresses within the `a.o
ut`'s address space. Of these, the last is most useful (it gives the beginning
of the dynamically allocated data space). However, the *type* for these symbols
was always pretty fuzzy. But, consider a declaration of `end` as

```c
extern void end;
```

What this gives is a name that only has an address \- exactly what these symbols
do, and nothing more. They can only be used in C as the operand of unary `&`,
and the address must be converted to something else (say, `char *`) even to do
address calculation, making the special nature of the symbol clearly evident.

What I'd like is a vote of the interpretations group that notes that the intent
of the Committee was that “`void *p; &*p;`” was supposed to be valid, even
though a conforming implementation must diagnose the expression. This means that
I can continue to suggest the “`extern void`” approach to address symbols in C.

P.S.: The following is my reply to Dennis's mail that pointed out the error with
my original interpretation. The indented parts are from Dennis's mail.

> I don't agree with Dave P's answer about “`void *vp; &*vp;`.” There is not a
> constraint on `*`, but the subclause 6.3.3.2 semantics say, “... if it \[the
> operand of `*`] points to an object, the result is an lvalue designating the
> object.” Does `vp` point to an object? An object is “a region of data storage
> ... the contents of which can represent values” (clause 3). Dicey at best.

I took some time looking into my records of the Committee's thoughts on this
very issue. Back in '87, based on a proposal by Plauger, the Committee voted 27
to 3 that “`*(void *)`” was not to be an error. This was when the unary `*`
constraint was simplified to the current form. Since `void` is a special
instance of an incomplete object type, it can be thought of as pointing at an
object whose size we do not know, but I agree that the argument is strained. I
would still recommend that the compiler not produce a hard error in this
situation.

> Moreover, the operand of `&` must be an lvalue, and `*vp` is certainly not an
> lvalue (subclause 6.2.2.1): “An *lvalue* is an expression (with an object type
> or an incomplete type other than `void`) ...”

Oops. In this case, I completely agree with Dennis: the standard does say that
unary `&` should not be applied to an expression with type `void` since such
cannot be an lvalue. Unfortunately, this means that the standard is “broken,” at
least according to the Committee's decisions. One of the major arguments
presented as part of the September 1987 meeting for allowing “`*(void *)`” was
that it could then be immediately used as the operand of unary `&`!

Therefore, I can state that back in 1987, the Committee's intent was that the
examples you gave were valid Standard C, but that the standard as written does
not allow the second half of the construction for `void`! Nevertheless, I'd
still suggest allowing the code to successfully compile, with at most a warning.

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 6.3.3.2 (page 43, lines 36-38):

> The operand of the unary `&` operator shall be either a function designator or
> an lvalue that designates an object that is not a bit-field and is not declared
> with the `register` storage-class specifier.

and the one supplied by you from subclause 6.2.2.1 (page 36, lines 3-4):

> An *lvalue* is an expression (with an object type or an incomplete type other
> than `void`) that designates an object.

Given the following declaration:

```c
void *p;
```

the expression `&*p` is invalid. This is because `*p` is of type `void` and so
is not an lvalue, as discussed in the quote from subclause 6.2.2.1 above.
Therefore, as discussed in the quote from subclause 6.3.3.2 above, the operand
of the `&` operator in the expression `&*p` is invalid because it is neither a
function designator nor an lvalue.

This is a constraint violation and the translator must issue a diagnostic
message.

The desired effect can be obtained by using the declaration

```c
extern const void end;
```

(where `end` denotes an object of unknown size) since `const void` type is not
`void` type and thus `&end` does not violate the constraint in subclause
6.3.3.2.

Footnote 6 (page 6), which is not part of the standard, provides a suggestion
for implementors who may wish to assign a meaning to the above expression. It
says “(An implementation) may also successfully translate an invalid program.”
Therefore, as long as a diagnostic message is issued, a translator may assign a
meaning to the expression `&*p` discussed above. Conforming programs shall not
use this expression, however.


</div>


---

---

<div id="issue0013.01">

## Issue 0013.01: How does one form the composite type of mixed array and pointer parameter types?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.15](log_c90.md#issue0017.15), [0040.01](log_c90.md#issue0040.01), [0110](log_c90.md#issue0110)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Compatible and composite function types

A fix to both problems Mr. Jones raises in X3J11 Document Number 90-006 is: In
subclause 6.5.4.3 on page 68, lines 23-25, change the two occurrences of “its
type for these comparisons” to “its type for compatibility comparisons, and for
determining a composite type.” This change makes the sentences pretty awkward,
but I think they remain readable.

This change makes all three of Mr. Jones's declarations compatible:

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

This should be the case; it is consistent with the base document's idea of
“rewriting” the parameter type from array to pointer.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.4.3, page 68, lines 22-25, change:***

(For each parameter declared with function or array type, its type for these
comparisons is the one that results from conversion to a pointer type, as in
6.7.1. For each parameter declared with qualified type, its type for these
comparisons is the unqualified version of its declared type.)

***to:***

(In the determination of type compatibility and of a composite type, each
parameter declared with function or array type is taken as having the type that
results from conversion to a pointer type, as in 6.7.1, and each parameter
declared with qualified type is taken as having the unqualified version of its
declared type.)


</div>


---

---

<div id="issue0013.02">

## Issue 0013.02: Is compatible properly defined for recursive types?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

“Compatible” not defined for recursive types

The term “compatible” is not completely defined. Consider the following two
file-scope declarations in *separate* translation units:

```c
extern struct a { struct a *p; } x;
 struct a { struct a *p; } x;
```

Are these two declarations of `x` compatible? Obviously they should be, but
subclause 6.1.2.6 does not say so.

Because subclause 6.1.2.6 does not say how to terminate the recursion in testing
for compatibility of two recursive types, either interpretation is possible. In
other words, it is consistent with the rules in subclause 6.1.2.6 to decide that
the two declarations are compatible; but it is also consistent to decide that
they are incompatible.

We can solve the problem roughly as follows: append the following draft sentence
to the first paragraph of subclause 6.1.2.6 (page 25, line 8):

> If two types declared in separate translation units admit the possibility of
> being either compatible or incompatible, the two types shall be
> compatible.**\*** \[Footnote \*: This case occurs with recursive types.]

This sentence is not satisfactory; perhaps another Committee member can state
this rule better.

---

Comment from WG14 on 1997-09-23:

### Response

We agree that the C Standard can be read in a way that it “loops.” Our intent,
and we feel the only reasonable solution, is that the recursion stops and the
two types are regarded as compatible.


</div>


---

---

<div id="issue0013.03">

## Issue 0013.03: What is the composite type of an enumeration and an integer?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Status: Closed  
Cross-references: [0127](log_c90.md#issue0127)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Composite type of `enum` vs. integer not defined

There is one case where two types are compatible, but their composite type is
not defined. To fix this problem, in subclause 6.1.2.6 insert after page 25,
line 17:

> \- If one type is an enumeration and the other is an integer type, the composite
> type is the enumeration.

There may be other cases where “compatible” is not defined. I made a cursory
search and did not find any.

---

Comment from WG14 on 1997-09-23:

### Response

The issue is that in

```c
enum {r,w,b} x;
```

and

```c
some-int-type x;
```

where `some-int-type` happens to be the type that by subclause 6.5.2.2, page 61,
line 40 is compatible with the type of the `enum`, what is the resultant
composite type?

Subclause 6.1.2.6 on page 25, lines 11-12 says “*a* type that ... satisfies the
following conditions” (added emphasis on “*a*”). The composite type of two
compatible types is not necessarily unique. In this case both the `enum` type
and the `some-int-type` satisfy the definition of “composite” type. This refutes
the claim that the “composite type is not defined;” the point is that the
standard does not guarantee a *unique* composite type.

As an example, in the following declarations:

```c
enum {r, w, b} x;
 some_int_type x;
```

provided the enumeration type is compatible with the type of `some_int_typ e`,
it is unspecified whether the composite type of `x` is the enumeration type or
`some_int_type`.


</div>


---

---

<div id="issue0013.04">

## Issue 0013.04: When is a struct type complete?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

When a structure is incomplete

Reference subclause 6.5.2.3, page 62, lines 25-28:

> If a type specifier of the form
>
> ```c
> struct-or-union  identifier
> ```
>
> occurs prior to the declaration that defines the content, the structure or union
> is an incomplete type.

In the following example, neither the second nor the third occurrence of `struct
foo` seem adequately covered by this sentence:

```c
struct foo {
         struct foo *p;
 } a[sizeof(struct foo)];
```

In the second occurrence `foo` is incomplete, but since the occurrence is within
“the declaration that defines the content,” it cannot be said to be “prior” that
declaration. In the third occurrence `foo` is complete, but again, the
occurrence is within the declaration.

To fix the problem, change the phrase “prior to the declaration” to “prior to
the end of the `struct-declaration-list` or `enumerator-list`.”

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.2.3, page 62, line 27, change:***

occurs prior to the declaration that defines the content

***to:***

occurs prior to the `}` following the `struct-declaration-li st` that defines
the content


</div>


---

---

<div id="issue0013.05">

## Issue 0013.05: When is the `sizeof` an enumeration type known?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-047  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0118](log_c90.md#issue0118), [0165](log_c90.md#issue0165)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_013.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_013.html)

Enumeration tag anomaly

Consider the following (bizarre) example:

```c
enum strange1 {
         a = sizeof (enum strange1)      /* line [2] */
 };
 enum strange2 {
         b = sizeof (enum strange2 *)    /* line [5] */
 };
```

The respective tags are visible on lines \[2] and \[5] (according to subclause
6.1.2.1, page 20, lines 39-40, but there is no rule in subclause 6.5.2.3,
**Semantics** (page 62\) that governs their meaning on lines \[2] and \[5].
Footnote 62 on page 62 seems to be written without taking this case into
account.

The first declaration must be illegal. The second declaration should be illegal
for simplicity.

Perhaps these declarations are already illegal, since no rule gives them a
meaning. To clarify matters, I suggest in subclause 6.5.2.3 appending to page
62, line 35:

> A type specifier of the form
>
> ```c
> enum identifier
> ```
>
> shall not occur prior to the end of the `enumerator-list` that defines the
> content.

If this sentence is not appended, something like it should appear as a footnote.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.5.2.3, page 63, another Example:***

An enumeration type is compatible with some integral type. An implementation may
delay the choice of which integral type until all enumeration constants have
been seen. Thus in:

```c
enum f { c = sizeof(enum f) };
```

the behavior is undefined since the size of the respective enumeration type is
not necessarily known when `sizeof`


</div>


---

---

<div id="issue0014.01">

## Issue 0014.01: Is `setjmp` a macro or a function?

Authors: Max K. Goff, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-049  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_014.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_014.html)

X/Open Reference Number KRT3.159.1

There are conflicting descriptions of the `setjmp()` interface in ISO 9899:1990.
In subclause 7.6 on page 118, line 8, it is stated that “It is unspecified
whether `setjmp` is a macro or an identifier declared with external linkage.”
Throughout the rest of the standard, however, it is referred to as “the `setjmp`
macro”; in addition, the rationale document states that `setjmp` must be
implemented as a macro. Please clarify whether `setjmp` must be implemented as a
macro, or may be a function as well as a macro, or may just be a function.

---

Comment from WG14 on 1997-09-23:

### Response

The standard states that `setjmp` can be either a macro or a function. It is
referred to as “the `setjmp` macro” just to avoid longwindedness. The rationale
document is incorrect in saying that it must be a macro.


</div>


---

---

<div id="issue0014.02">

## Issue 0014.02: How does `fscanf("%n")` behave on end-of-file?

Authors: Max K. Goff, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-049  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0167](log_c90.md#issue0167)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_014.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_014.html)

X/Open Reference Number KRT3.159.2

Subclause 7.9.6.2 **The `fscanf` function** states:

> If end-of-file is encountered during input, conversion is terminated. If
> end-of-file occurs before any characters matching the current input directive
> have been read (other than leading white space, where permitted), execution of
> the current directive terminates with input failure; otherwise, unless execution
> of the current directive is terminated with a matching failure, execution of the
> following directive (if any) is terminated with an input failure.

How should an implementation behave when end-of-file terminates an input stream
that satisfies all conversion specifications that consume input but there is a
remaining specification request that consumes no input (e.g. `%n`)? Should the
non-input-consuming directive be evaluated or terminated with an input failure
as described above?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.9.6.2, page 137, line 4 (the*** `n` ***conversion
specifier):***

No argument is converted, but one is consumed. If the conversion specification
with this conversion specifier is not one of `%n`, `%ln`, or `%hn`, the behavior
is undefined.

***Add to subclause 7.9.6.2, page 138, another Example:***

In:

```c
#include <stdio.h>
 /* ... */
 int d1, d2, n1, n2, i;
 i = sscanf("123", "%d%n%n%d",&d1, &n1, &n2, &d2);
```

the value 123 is assigned to `d1` and the value 3 to `n1` . Because `%n` can
never get an input failure the value of 3 is also assigned to `n2`. The value of
`d2` is not affected. The value 3 is assigned to `i`.


</div>


---

---

<div id="issue0015">

## Issue 0015: How does an unsigned plain bitfield promote?

Authors: Craig Blitz, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-051  
Status: Closed  
Cross-references: [0122](log_c90.md#issue0122)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_015.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_015.html)

This question concerns the promoted type of plain `int` bit-fields with length
equal to the size of an object of type `int`. I am interested in implementations
that have chosen not to regard the high-order bit as a sign bit.

The question is: What is the promoted type of such an object?

Subclause 6.5.2.1 states:

> A bit-field shall have a type that is ... `int`, `unsigned int`, or `signed
> int`.

The intent of this, I believe, is that the type of a plain `int` bit-field is
`int`.

Subclause 6.2.1.1 states:

> A `char`, a `short int`, or an `int` b it-field, or their signed or unsigned
> varieties, ... may be used in an expression wherever an `int` or `unsigned int`
> may be used. If an `int` can represent all values of the original type, the
> value is converted to an `int`; otherwise it is converted to an `unsigned
> int`...
>
> The integral promotions preserve value including sign.

Tracing this through, then, the type of any promoted plain `int` bit-field is
`int`, since `int` can hold all the values of the original type, which is `int`.
However, not all values of the bit-field, which may be regarded as non-negative,
can be represented by an `int`. By value-preserving promotion rules, I would
expect the type of the promoted bit-field to be `unsigned int`.

Can you clarify this?

---

Comment from WG14 on 1997-09-23:

### Response

As described in subclause 6.2.1.1, bit-fields that are being treated as unsigned
will promote according to the same rules as other unsigned types: if the width
is less than `int`, and `int` can hold all the values, then the promotion is to
`int`. Otherwise, promotion is to `unsigned int`.


</div>


---

---

<div id="issue0016.01">

## Issue 0016.01: Can a tentative definition have an incomplete type initially?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-052  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_016.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_016.html)

I can find no prohibition of the following translation unit:

```c
struct foo x;
 struct foo { int i; };
```

What I was looking for, but didn't find, was a statement that an implicitly
initialized declaration of an object with static storage duration must have
object type. Is this translation unit legal?

---

Comment from WG14 on 1997-09-23:

### Response

The translation unit cited is valid. It falls into the same category of
construct as

```c
int array[];
 int array[17];
```

Objects may be declared without knowing their size. However, the standard is
clear in what cases such an object may or may not be used, prior to the actual
definition of the object.


</div>


---

---

<div id="issue0016.02">

## Issue 0016.02: Can you implicitly initialize a union when null pointers have nonzero bit patterns?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-052  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_016.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_016.html)

This one is relevant only for hardware on which either null pointer or floating
point zero is *not* represented as all zero bits.

Consider this sentence in subclause 6.5.7 (starting on page 71, line 41):

> If an object that has static storage duration is not initialized explicitly, it
> is initialized implicitly as if every member that has arithmetic type were
> assigned 0 and every member that has pointer type were assigned a null pointer
> constant.

This implies that you cannot implicitly initialize a union object that could
contain overlapping members with different representations for zero/null
pointer. For example, given this translation unit:

```c
union { char *p; int i; } x;
```

If the null pointer is represented as, say, `0x80000000`, then there is no way
to implicitly initialize this object. Either the `p` member contains the null
pointer, or the `i` member contains 0, but not both. So the behavior of this
translation unit is undefined.

This is a bad state of affairs. I assume it was not the Committee's intention to
prohibit a large class of implicitly initialized unions; this would render a
great deal of existing code nonconforming.

The right thing \- although I can find no support for this idea in the draft \-
is to implicitly initialize only the first member of a union, by analogy with
explicit initialization. Here is a proposed new sentence; perhaps it can be
saved for the next time we make a C standard. (This sentence also tries to get
around the difficulty of the old “as if ... assigned” language in dealing with
`const` items; Dave Prosser tipped me off there.)

1. If an object that has static storage duration is not initialized explicitly, it is initialized implicitly according to these rules:
2. if it is a scalar with pointer type, it is initialized implicitly to a null pointer constant;
3. if it is a scalar with non-pointer type, it is initialized implicitly to zero;
4. if it is an aggregate, every member is initialized (recursively) according to these rules;
5. if it is a union, the first member is initialized (recursively) according to these rules.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 71, line 41 through page 72, line 2, change:***

If an object that has static storage duration is not initialized explicitly, it
is initialized implicitly as if every member that has arithmetic type were
assigned 0 and every member that has pointer type were assigned a null pointer
constant.

***to:***

1. If an object that has static storage duration is not initialized explicitly, then:
2. if it has pointer type, it is initialized to a null pointer;
3. if it has arithmetic type, it is initialized to zero;
4. if it is an aggregate, every member is initialized (recursively) according to these rules;
5. if it is a union, the first named member is initialized (recursively) according to these rules.


</div>


---

---

<div id="issue0017.01">

## Issue 0017.01: Are newlines permitted within macro invocations in preprocessing directives?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

New-line in preprocessor directives

Subclause 5.1.1.2, page 5, line 37 says: “Preprocessing directives are executed
and macro invocations are expanded.”

Subclause 6.8, page 86, lines 2-5 say: “A preprocessing directive ... and is
ended by the next new-line character.”

Subclause 6.8.3, page 89, lines 38-39 say: “Within the sequence of preprocessing
tokens ... new-line is considered a normal white-space character.”

These three statements are not sufficient to categorize the following:

```c
#define f(a,b) a+b
 #if f(1,
      2)
 ...
```

It should be defined whether the preprocessing directive rule or macro expansion
wins, i.e. is this code fragment legal or illegal?

In translation phase 4 “preprocessing directives are executed and macro
invocations expanded.”

Now do macro invocations get done first, followed by preprocessor directives?
Does the macro expander need to know that what it is expanding forms a
preprocessing directive?

Subclause 6.8, page 86, lines 2-5 suggest that the preprocessor directive is
examined to look for the new-line character. But how is it examined? Obviously
phases 1-3 happen during this examination. So why shouldn't part of phase 4?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.8, page 86, line 5, (Description):***

A new-line character ends the preprocessing directive even if it occurs within
what would otherwise be an invocation of a function-like macro.


</div>


---

---

<div id="issue0017.02">

## Issue 0017.02: Should the absence of function `main` be explicitly undefined?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Behavior if no function called `main` exists

According to subclause 5.1.2.2.1, page 6, it is implicitly undefined behavior if
the executable does not contain a function called `main`.

It ought to be explicitly undefined if no function called `main` exists in the
executable.

---

Comment from WG14 on 1997-09-23:

### Response

You are correct that it is implicitly undefined behavior if the executable does
not contain a function called `main`. This was a conscious decision of the
Committee.

There are many places in the C Standard that leave behavior implicitly
undefined. The Committee chose as a style for the C Standard not to enumerate
these places as explicitly undefined behavior. Rather, subclause 3.16, page 3,
lines 12-16 explicitly allow for implicitly undefined behavior and explicitly
give implicitly undefined behavior equal status with other forms of undefined
behavior.

### Correction

***Add to subclause G.2, page 200:***

\- A program contains no function called `main` (5.1.2.2.1).


</div>


---

---

<div id="issue0017.03">

## Issue 0017.03: Does a constraint violation win over undefined behavior?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0102](log_c90.md#issue0102), [0105](log_c90.md#issue0105)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Precedence of behaviors

Refer to subclause 6.1.2.6, page 25, lines 9-10 and subclause 6.5, page 57,
lines 20-21. The constructs covered by these sentences overlap. The latter is a
constraint while the former is undefined behavior. In the overlapping case who
wins?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.1.1.3, page 6, lines 15-17, change:***

A conforming implementation shall produce at least one diagnostic message
(identified in an implementation-defined manner) for every translation unit that
contains a violation of any syntax rule or constraint.

***to:***

A conforming implementation shall produce at least one diagnostic message
(identified in an implementation-defined manner) for every translation unit that
contains a violation of any syntax rule or constraint, even if the behavior is
also explicitly specified as undefined or implementation-defined.

***Add to subclause 5.1.1.3, page 6:***

**Example**

An implementation shall issue a diagnostic for the translation unit:

```c
char i;
 int i;
```

because in those cases where wording in this International Standard describes
the behavior for a construct as being both a constraint error and resulting in
undefined behavior, the constraint error shall be diagnosed.


</div>


---

---

<div id="issue0017.04">

## Issue 0017.04: Do numeric escape sequences map from source to execution character sets?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Mapping of escape sequences

Refer to subclause 6.1.3.4, page 29, line 12 and line 16\. Are these values the
values in the source or execution character set?

When subclause 6.1.3.4, page 29, line 24 says: “The value of an ...,” is this
“value” the value in the source character set of the escape sequence or the
value of the mapped escape sequence? I would have said that the “value” is the
value in the execution environment since in the source environment `\x123` is
part of a token.

It might be argued that characters in the source character set do not have
values and thus no misinterpretation of “value” can occur. Subclause 5.2.1, page
10, lines 25-26 refer to the value of a character in the source basic character
set.

---

Comment from WG14 on 1997-09-23:

### Response

The values of octal or hexadecimal escape sequences are well defined and not
mapped. For instance, the value of the constant `'\x12'` is always 18, while the
value of the constant `'\34'` is always 28\.

The mapping described in subclause 6.1.3.4 on page 28, lines 35-39 only applies
to members of the source character set, of which octal and hexadecimal escape
sequences clearly are not members.


</div>


---

---

<div id="issue0017.05">

## Issue 0017.05: When are character constants implementation defined?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Example of value of character constants

Refer to subclause 6.1.3.4, page 29, lines 24-25 and page 30, lines 9-10. Both
of these statements cannot be true.

1. If the constraint is violated, end of story. There is no implementation-defined value.
2. The implementation-defined behavior may be referring to the mapping of the escape sequence to the basic character set, in which case subclause 6.1.3.4, page 29, lines 24-25 should be changed to mention that it will violate a constraint if the mapped value is outside the range of representable values for the type `unsigned char`.

---

Comment from WG14 on 1997-09-23:

### Response

The values of octal or hexadecimal escape sequences are well defined and not
mapped. For instance, the value of the constant `'\x123'` has the value 291\.

The mapping described in subclause 6.1.3.4 on page 28, lines 35-39 applies only
to members of the source character set, of which octal and hexadecimal escape
sequences clearly are not members.

The constraint in subclause 6.1.3.4 on page 29, lines 24-25 will be violated
only if the implementation uses characters of eight bits.

The text of the example in subclause 6.1.3.4 on page 30, lines 8-10 is slightly
opaque, but the parenthesized comment is meant to be subject to the words “Even
if eight bits are used ...” The value is implementation-defined only in that the
implementation specifies how many bits are used for characters and whether type
`char` is signed or not.

This example could be worded a little more clearly to indicate what is
implementation-defined about the constant, and that it “violates the above
constraint” only if eight bits are used for objects that have type `char`, but
we believe that this interpretation is consistent with the intent of the
Committee, and that a reasonable reading of the standard supports this
interpretation.


</div>


---

---

<div id="issue0017.06">

## Issue 0017.06: Are register aggregates permitted?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0116](log_c90.md#issue0116)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`register` on aggregates

```c
void f(void)
 {
 register union{int i;} v;
 &v      /* Constraint error */
 &(v.i);  /*  Constraint error or undefined? */
 }
```

In subclause 6.3.3.2 on page 43, lines 37-38 in a constraint clause, it says
“... and is not declared with the `register` storage-class specifier.” But in
the above, the field `i` is not declared with the `register` storage-class
specifier.

Footnote 58, on page 58, states that “... the address of any part of an object
declared with storage-class specifier `register` may not be computed ...”
Although the reference to this footnote is in a constraints clause I think that
it is still classed as undefined behavior.

Various people have tried to find clauses in the standard that tie the storage
class of an aggregate to its members. I would not use the standard to show this
point. Rather I would use simple logic to show that if an object has a given
storage class then any of its constituent parts must have the same storage
class. Also the use of storage classes on members is syntactically illegal.

The question is not whether such a construction is legal but the status of its
illegality. Is it a constraint error or undefined behavior?

It might be argued that although `register` does not appear on the field `i`,
its presence is still felt. I would point out that the standard does go to some
pains to state that in the case of `const union{...}` the `const` does apply to
the fields. The fact that there is no such wording for `register` implies that
`register` does not follow the `const` rule.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.5.1, page 58 (Semantics):***

If an aggregate or union object is declared with a storage-class specifier other
than `typedef`, the properties resulting from the storage-class specifier,
except with respect to linkage, also apply to the members of the object, and so
on recursively for any aggregate or union member objects.


</div>


---

---

<div id="issue0017.07">

## Issue 0017.07: What is the scope and uniqueness of `size_t`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Cross-references: [0047](log_c90.md#issue0047), [0050](log_c90.md#issue0050)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Scope and uniqueness of `size_t`

Subclause 6.3.3.4 on page 45, lines 1-2 says: “... and its type (...) is
`size_t` defined in the `<stddef.h>` header.” This line could be read as either
of the following:

1. “... and its type is `size_t` which happens to be defined in `stddef.h`.”
2. “... and its type is the `size_t` defined in `stddef.h`.”

(It was probably intended as a helpful piece of information only.) So what does
the compiler do?

In (1) the compiler has to define a `size_t` in some outer scope. This
definition does not make `size_t` visible, but gives a type to the return value
of `sizeof`. Now if the programmer defines a typedef making `size_t` synonymous
with `float` (say) then the compiler now has to use this new type. This
interpretation does not require the programmer to include `<stddef.h>` in order
to use `sizeof`.

In (2) the compiler picks up the type `size_t` from `<stddef.h>` (assuming that
the user included this header). Should the compiler give a diagnostic if this
header was not included and `sizeof` was used? A subsequent typedef for `size_t`
does not affect the type of the result of `sizeof`.

These problems do not arise with `int`, et al. because they are keywords. Thus
“`typedef float int`” would give a syntax error and need not be considered
semantically.

According to subclause 6.3.3.4, page 45, `sizeof` has type `size_t`. What
happens if the type of `size_t` does not match what the compiler thinks is the
type of `sizeof`?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 6.3.3.4

> The value of the result is implementation-defined, and its type (an unsigned
> integral type) is `size_t` defined in the `<stddef.h>` header.

and subclause 7.1.6

> The types are ...
>
> ```c
> size_t
> ```
>
> which is the unsigned integral type of the result of the `sizeof` operator; ...

These sections, both separately and together, define the relationship between
the result type of `sizeof` and the type `size_t` defined in `stddef.h`. The
result type of `sizeof` and the type `size_t` defined in `stddef.h` are an
unsigned integral type, and `size_t` defined in `<stddef.h>` is identical to the
result type of `sizeof`. To restate, in a conforming implementation, the result
type of `sizeof` will be the same as the type of `size_t` defined in
`<stddef.h>`.

Since these two types are the same, there need be no mechanism for a compiler to
discover the type of `size_t` defined in `<stddef.h>`. A compiler's private
knowledge of the result type of `sizeof` is as good as `stddef.h`'s private
knowledge of the type of `size_t`.

Note that the result of `sizeof` has the same type as not just any `size_t,` but
the `size_t` defined in `<stddef.h>`.


</div>


---

---

<div id="issue0017.08">

## Issue 0017.08: What types are compatible with pointer to `void`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of pointer to `void` with storage class

Refer to subclause 6.3.9, page 49, lines 24-25. Do these lines make the
following legal?

```c
register void *p;
 char *q;
 if (p==q)  /* legal */
 ...
```

The wording on line 25, “... version of `void`; or” does not talk about the
“`void` type.” This sentence could be taken as simply referring to the
occurrence of a qualified or unqualified occurrence of `void`.

Should the wording on line 25 be changed to “... version of the type `void`; or”
and thus cause the storage class to be ignored, or does the above example fall
outside the scope of the constraint?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citation is subclause 6.3.9:

> one operand is a pointer to an object or incomplete type and the other is a
> pointer to a qualified or unqualified version of `void`; or

The Committee believes that the current wording of the standard is clear, and it
is not changed in meaning by changing “version of `void`” in the quoted section
to “version of the `void` type.”

The standard uses the word “`void`” in two contexts: the keyword itself and the
type that the keyword names. The context that the word is used in adequately
distinguishes between the two. In the section quoted, which discusses type
compatibility, a misreading of “`void`” as meaning the keyword quickly results
in nonsense.

As to the qualification discussed in the quoted passage, it is type
qualification, defined in subclause 6.5.3. The standard only uses the words
“qualified” and “unqualified” when discussing type qualification and never uses
them when discussing storage classes. Thus, storage classes have no place in the
discussion of the quoted passage.


</div>


---

---

<div id="issue0017.09">

## Issue 0017.09: What is the type of an assignment expression?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Syntax of assignment expression

In subclause 6.3.16.1 on page 53, lines 31-32 there is a typo: “... of the
assignment expression ...” should be “... of the unary expression ...”

In subclause 6.3.16 on page 53, lines 3-5 we have

```c
assignment-expression:
    ...
         unary-expression  assignment-operator  assignment-expression
```

Now the string “*`assignment-expression`*” occurs twice.

The use of “assignment expression” in subclause 6.3.16 on page 53, line 12
refers to the first occurrence (the one to the left of the colon).

We suggest changing the use of “assignment expression” in subclause 6.3.16.1 on
page 53, line 32 in order to prevent confusion. The fact that any qualifier is
kept actually makes more sense, since this qualifier has to take part in any
constraint checking.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.3.16.1, page 54, another Example:***

In the fragment:

```c
   char c;
    int i;
    long l;

    l = ( c = i );
```

the value of `i` is converted to the type of the assignment-expression `c = i`,
that is, `char` type. The value of the expression enclosed in parenthesis is
then converted to the type of the outer assignment-expression, that is, `long`
type.


</div>


---

---

<div id="issue0017.10">

## Issue 0017.10: When is the `sizeof` an object needed?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

When is `sizeof` needed?

Refer to subclause 6.5.2.3, page 62, lines 28-29. When is the size of an
incomplete structure needed? An interpreter may not need the size until run
time, while some strictly typed memory architecture may not even allow pointers
to structures of unknown size.

In subclause 6.5.2.3, Footnote 63 starts off as an example. The last sentence
contains a “shall.” Does a violation of this “shall” constitute undefined
behavior?

Even though an interpreter may not need the size of a structure until run time
its compiler still has to do some checking, i.e. an unexecuted statement may
contain `sizeof` an incomplete type; even though the statement is unexecuted the
constraint still has to be detected.

---

Comment from WG14 on 1997-09-23:

### Response

Whether the language processor is an interpreter or a true compiler does not
affect the language rules about when the size of an object is needed. Both a
compiler and an interpreter must act as if the translation phases in subclause
5.1.1.2 were followed. This is a requirement that an implementation act as if
the entire program is translated before the program's execution.

The “shall” in Footnote 63 in subclause 6.5.2.3 carries no special meaning: this
footnote, like all other footnotes in the standard, is provided to emphasize the
consequences of the rules in the standard. The footnote is not part of the
standard.

The Committee believes that a careful reading of the standard shows all of the
places that the size of an object is needed, and that the translation phases
prevent those requirements from being relaxed by an implementation.


</div>


---

---

<div id="issue0017.11">

## Issue 0017.11: Is `struct t; struct t;` valid?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Clarification of incomplete `struct` declaration

Referring to subclause 6.5.2.3, page 62:

```c
struct t;
 struct t; /* Is this undefined? */
```

People seem to think that the above is undefined.

The problem arises because no rules exist for compatibility of incomplete
structures or unions.

---

Comment from WG14 on 1997-09-23:

### Response

The proposed example is valid. Nothing in the standard prohibits it.

The relevant citation is subclause 6.5.2.3 Semantics, paragraph 2:

> A declaration of the form
>
> ```c
>     struct-or-union  identifier ;
> ```
>
> specifies a structure or union type and declares a tag, both visible only within
> the scope in which the declaration occurs. It specifies a new type distinct from
> any type with the same tag in an enclosing scope (if any).


</div>


---

---

<div id="issue0017.12">

## Issue 0017.12: How do typedefs parse in function prototypes?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0009](log_c90.md#issue0009)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Ambiguous parsing of typedefs in prototypes

On page 67 in subclause 6.5.4.3, an ambiguity needs resolving in the parsing of
the following:

a. `int x(T (U));`

b. `int x(T (U (int a, char b)));`

In (a) `U` is the type of the parameter to a function returning type `T`. From
subclause 6.5.4.3, page 68, line 2:

> In a parameter declaration, a single typedef name in parentheses is taken to be
> an abstract declarator that specifies a function with a single parameter, not as
> redundant parentheses around the identifier for a declarator.

Thus in the case of (b):

1. `U` could be a redundantly parenthesized name of a function which takes a *`parameter-type-list`* and returns type `T`, or
2. `U` could be the type returned by a function which takes a *`parameter-type-list`*, which in turn is the single parameter of a function returning type `T`.

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #009](log_c90.md#issue0009), Question 1 for a clarifying correction in
this area.


</div>


---

---

<div id="issue0017.13">

## Issue 0017.13: How does `register` affect compatibility of function parameters?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of functions with `register` on parameters

Reference subclause 6.5.4.3, page 67\.

```c
f1(int);
 f1(register int a) /* Is this function compatible with the above?  */
 {
 }
```

Subclause 6.5.4.3, page 68, lines 5-7 were presumably intended to make sure that
the `register` storage class got kept in the case of a definition so that the
appropriate constraints applied, i.e., it is not allowed to take its address,
etc. But the further implication of the wording is that the occurrence of
`register` lingers on for other uses \- but there are no other uses.

Suggest a clarification on this point.

---

Comment from WG14 on 1997-09-23:

### Response

The function is compatible. Storage class is not part of the type.

The relevant citation, as given, is subclause 6.5.4.3, page 68, lines 5-7, but
it does not imply any “other uses.”


</div>


---

---

<div id="issue0017.14">

## Issue 0017.14: `const void` type as a parameter

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0110](log_c90.md#issue0110)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`const void` type as a parameter

Refer to subclause 6.5.4.3, page 67, line 37\. `f(const void)` should be
explicitly undefined; also `f(register void)`, `f(volatile void)`, and
combinations thereof.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause G.2, page 201:***

\- A storage-class specifier or type qualifier modifies the keyword `void` as a
function parameter type list (6.5.4.3).


</div>


---

---

<div id="issue0017.15">

## Issue 0017.15: When do array parameters get converted to pointers?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0013.01](log_c90.md#issue0013.01), [0110](log_c90.md#issue0110)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Ordering of conversion of arrays to pointers

In subclause 6.5.4.3 on page 68, line 22 there is a sentence in parentheses.
Does the sentence refer to the whole paragraph or just the preceding sentence?

```c
int f(int a[4]);
 int f(int a[5]);
 int f(int *a);
```

1. It refers to the whole paragraph. This makes all of the above three declarations compatible.
2. It does not refer to the whole paragraph. This makes all three declarations incompatible.

---

Comment from WG14 on 1997-09-23:

### Response

Regarding page 68, line 22: There are *two* sentences in parentheses. They apply
to the entire paragraph. The declarations are all compatible. (See [Defect
Report #013, Question 1](log_c90.md#issue0013.01) for a clarifying correction in this
area.)


</div>


---

---

<div id="issue0017.16">

## Issue 0017.16: Are subarrays of arrays distinct objects?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Pointer to multidimensional array

Given the declaration:

```c
char a[3][4], (*p)[4]=a[1];
```

Does the behavior become undefined when:

1. `p` no longer points within the slice of the array, or
2. `p` no longer points within the object `a`?

This case should be explicitly stated.

Arguments for/against:

The standard refers to a pointed-to object. There does not appear to be any
concept of a slice of an array being an independent object.

---

Comment from WG14 on 1997-09-23:

### Response

For an array of arrays, the permitted pointer arithmetic in subclause 6.3.6,
page 47, lines 12-40 is to be understood by interpreting the use of the word
“object” as denoting the specific object determined directly by the pointer's
type and value, *not* other objects related to that one by contiguity.
Therefore, if an expression exceeds these permissions, the behavior is
undefined. For example, the following code has undefined behavior:

```c
int a[4][5];

 a[1][7] = 0;    /* undefined */
```

Some conforming implementations may choose to diagnose an “array bounds
violation,” while others may choose to interpret such attempted accesses
successfully with the “obvious” extended semantics.

### Correction

***Add to subclause G.2, page 201:***

\- An array subscript is out of range, even if an object is apparently
accessible with the given subscript (as in the lvalue expression `a[1][7]` given
the declaration `int a[4][5]`) (6.3.6).


</div>


---

---

<div id="issue0017.17">

## Issue 0017.17: How do you initialize the first member of a union if it has no name?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.26](log_c90.md#issue0017.26)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Initialization of unions with unnamed members

Subclause 6.5.7 on page 71, line 39 says: “All unnamed structure or union
members are ignored ...” On page 72, lines 22-23, it says: “... for the first
member of the union.” Subclause 6.5.2.1, page 60, line 40 and Footnote 60 say
that a field with no declarator is a member.

```c
union {
        int  :3;
        float f;} u = {3.4};
```

Should page 72 be changed to refer to the first named member or is the
initialization of a union whose first member is unnamed illegal?

It has been suggested that the situation described above is implicitly
undefined.

I think that it is a straightforward ambiguity that needs resolution one way or
the other.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 71, line 39, change:***

All unnamed structure or union members are ignored during initialization.

***to:***

Except where explicitly stated otherwise, for the purposes of this subclause
unnamed members of objects of structure and union type do not participate in
initialization. Unnamed members of structure objects have indeterminate value
even after initialization. A union object containing only unnamed members has
indeterminate value even after initialization.

***In subclause 6.5.7, page 72, line 11, change:***

The initial value of the object is that of the expression.

***to:***

The initial value of the object, including unnamed members, is that of the
expression.


</div>


---

---

<div id="issue0017.18">

## Issue 0017.18: Are `f()` and `f(void)` compatible?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of functions with `void` and no prototype

```c
f2(void);
 f2(); /* Is this function compatible with the one above? */
```

Now subclause 6.5.4.3, page 68, line 1 says that the first declaration of `f2`
specifies that the function has no parameters.

No rules are given in the subsequent paragraphs to say that a function
declaration with a parameter type list, with no parameters, is compatible with a
function declaration with an empty parameter list.

If we treat the `void` as a single parameter then page 68, lines 14-18 would
make the above two functions incompatible. `void` is not compatible with any
default promotions. subclause 6.5.4.3, page 68, lines 18-22 cover the case for
declaration and definition.

Thus I think that in the above example the behavior is implicitly undefined.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.5.4.3, page 67, line 37 and page 68, line 1 state, “The special case
of `void` as the only item in the list specifies that the function has no
parameters.” Therefore, in the case of `f2(void);` there are *no* parameters
just as there are none for `f2();`. Since both functions have the same return
type, these declarations *are* compatible.


</div>


---

---

<div id="issue0017.19">

## Issue 0017.19: Are macro expansions ambiguous?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Order of evaluation of macros

Refer to subclause 6.8.3, page 89\. In:

```c
#define f(a) a*g
 #define g(a) f(a)
 f(2)(9)
```

it should be defined whether this results in:

1. ```c
   2*f(9)
   ```

   or
2. `2*9*g`

X3J11 previously said, “The behavior in this case could have been specified, but
the Committee has decided more than once not to do so. \[They] do not wish to
promote this sort of macro replacement usage.”

I interpret this as saying, in other words, “If we don't define the behavior
nobody will use it.” Does anybody think this position is unusual?

People seem to agree that the behavior is ambiguous in this case. Should we
specify this case as undefined behavior?

---

Comment from WG14 on 1997-09-23:

### Response

If a fully expanded macro replacement list contains a function-like macro name
as its last preprocessing token, it is unspecified whether this macro name may
be subsequently replaced. If the behavior of the program depends upon this
unspecified behavior, then the behavior is undefined.

For example, given the definitions:

```c
#define f(a) a*g
 #define g(a) f(a)
```

the invocation:

```c
f(2)(9)
```

results in undefined behavior. Among the possible behaviors are the generation
of the preprocessing tokens:

```c
2*f(9)
```

and

```c
2*9*g
```

### Correction

***Add to subclause G.2, page 202:***

\- A fully expanded macro replacement list contains a function-like macro name
as its last preprocessing token (6.8.3).


</div>


---

---

<div id="issue0017.20">

## Issue 0017.20: Is the scope of macro parameters defined in the right place?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Scope of macro parameters

Refer to subclause 6.8.3 on page 89, line 16; the scope of macro parameters
should be defined in the section on scope.

The idea is to enable all references to the scope of names to be under one
heading. This is not really a significant issue.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2 on page 20, line 5, states “Macro names and macro parameters are
not considered further here.” This approach was intentionally adopted to avoid
explicitly having to mention exceptions of using identifiers, for example in the
sections on scope, linkage, name spaces, and storage durations, none of which
applies to macros. The proposed change does *not* clarify the standard and may
even obscure it.


</div>


---

---

<div id="issue0017.21">

## Issue 0017.21: Is translation phase 4 defined unambiguously?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Self references in translation phase 4

The following queries arise because of the imprecise way in which phase 4
interacts with itself. While processing a token within phase 4 it is sometime
necessary to get the following tokens from the input, i.e. reading the arguments
to a function-like macro. But when getting these tokens it is not clear how many
phases operate on them:

1. Do the following tokens only get processed by phases 1-3?
2. Do the following tokens get processed by phases 1-4?

When an identifier declared as a function-like macro is encountered, how hard
should an implementation try to locate the opening/closing parentheses?

In:

```c
#define lparen (
 #define f_m(a) a
 f_m lparen "abc" )
```

should the object-like macro be expanded while searching for an opening
parenthesis? Or does the lack of a readily available left parenthesis indicate
that the macro should not be expanded?

Subclause 6.8.3, on page 89, lines 34-35 says “... followed by a `(` as the next
preprocessing token ...” This sentence does not help because in translation
phase 4 all tokens are preprocessing tokens. They don't get converted to “real”
tokens until phase 7\. Thus it cannot be argued that `lparen` is not correct in
this situation, because its result is a preprocessing token.

In:

```c
#define i(x) 3
 #define a i(yz
 #define b )
 a b )   /* goes to 3) or 3 */
```

does `b` get expanded to complete the call `i(yz,` or does the parenthesis to
its right get used?

---

Comment from WG14 on 1997-09-23:

### Response

Concerning the first example:

```c
#define lparen (
 #define f_m(a) a
 f_m lparen "abc" )
```

According to subclause 5.1.1.2 **Translation phases**, page 5, lines 25-39, the
translation phases 1-3 do not cause macros to be expanded. Phase 4 does expand.
To apply subclause 6.8.3 **Macro replacement** page 89, lines 34-35 to the
example: Since `lparen` is not `(` in “`f_m lparen "abc" )`,” this construct is
not recognized as a function-like macro invocation. Therefore the example
expands to

```c
f_m("abc")
```

The same principle applies to the second example:

```c
#define i(x) 3
 #define a i(yz
 #define b )
 a b )       /* expands via the following stages: */

 i(yz b )    /* ) delimits the argument list before b is expanded  */
 i([yz ) ])
 3
```

This is how we interpret subclause 6.8.3, page 89, lines 36-38: The sequence of
preprocessing tokens is terminated by the right-parenthesis preprocessing token.


</div>


---

---

<div id="issue0017.22">

## Issue 0017.22: Does the rescan of a macro invocation also perform token pasting?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Gluing during rescan

Reference: subclause 6.8.3.3, page 90\. Does the rescan of a macro invocation
also perform gluing?

```c
#define hash_hash # ## #
 #define mkstr(a) # a
 #define in_between(a) mkstr(a)
 #define join(c, d) in_between(c hash_hash d)

 char p[2] = join(x, y);
```

Is the above legal? Does `join` expand to `"xy"` or `"x ## y"`?

It all depends on the wording in subclause 6.8.3.3 on page 90, lines 39-40. Does
the wording “... before the replacement list is reexamined ...” mean before
being reexamined for the first time only, or before being reexamined on every
rescan?

This rather perverse macro expansion is only made possible because the
constraints on the use of `#` refer to function-like macros only. If this
constraint were extended to cover object-like macros the whole question goes
away.

Dave Prosser says that the intent was to produce `"x ## y"`. My reading is that
the result should be `"xy"`. I cannot see any rule that says a created `##`
should not be processed appropriately. The standard does say in subclause
6.8.3.3, page 90, line 40 “... each instance of a `##` ...”

The reason I ask if the above is legal is that the order of evaluation of `#`
and `##` is not defined. Thus if `#` is performed first the result is very
different than if `##` goes first.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.8.3.3, page 90:***

**Example**

```c
#define hash_hash # ## #
 #define mkstr(a) # a
 #define in_between(a) mkstr(a)
 #define join(c, d) in_between(c hash_hash d)
 char p[] = join(x, y); /* equivalent to char p[] = "x ## y";*/
```

The expansion produces, at various stages:

```c
join(x, y)
 in_between(x hash_hash y)
 in_between(x ## y)
 mkstr(x ## y)
 "x ## y"
```

In other words, expanding `hash_hash` produces a new token, consisting of two
adjacent sharp signs, but this new token is not the catenation operator.


</div>


---

---

<div id="issue0017.23">

## Issue 0017.23: How long does `blue paint` persist on macro names?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

How long does blue paint persist?

Consider the following code:

```c
#define a(x) b
 #define b(x) x
 a(a)(a)(a)
```

The macro replacement for `a(a)` results in `b`.

First replacement buffer: `b`

Remaining tokens: `(a)(a)`

Inside the first replacement buffer, no further nested replacements will
recognize the macro name “`a`.” The name “`a`” is painted blue.

The first replacement buffer is rescanned not by itself, but along with the rest
of the source program's tokens. “`b(a)`” also causes macro replacement and
becomes “`a`.”

Second replacement buffer: `a`

Remaining tokens: `(a)`

The second replacement buffer is rescanned not by itself, but along with the
rest of the source program's tokens.

The “`a`” in the second replacement buffer did not come from the first
replacement buffer. It came from three of the remaining tokens which were in the
source file following the first replacement buffer. Is this “`a`” part of a
nested replacement? Is it still painted blue?

Note that there are many “paths” that can be taken for a possible macro name to
travel from a preprocessing token (outside the replacement buffer) to one that
is inside the replacement buffer. When do they stop getting painted blue? If
either too early or too late, they cause very surprising results.

Given the amount of discussion involving macro expansion that uses the concept
of “blue paint,” why doesn't the standard tell the reader about this idea?

Everybody seems to agree that the above is undefined. Does anybody have a set of
words to make this and other cases explicitly undefined?

---

Comment from WG14 on 1997-09-23:

### Response

The reference is to subclause 6.8.3.4, page 91\.

```c
#define a(x) b
 #define b(x) x
 a(a)(a)(a)      /*  may expand as follows: */
 b(a)(a)
 a'(a)   or       a(a)
 a(a)            or       b
 /* a' indicates the symbol a marked for non-replacement */
```

The Committee addressed this issue explicitly in previous deliberations and
decided to say nothing about the situation, understanding that behavior in such
cases would be undefined.

The result, as with other examples, is intentionally left undefined.


</div>


---

---

<div id="issue0017.24">

## Issue 0017.24: Can subclause 7.1.2 be better expressed?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Improve English

Just a tidy up. Change subclause 7.1.2, page 96, line 33 from “if the
identifier” to “if an identifier.”

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.1.2, page 96, lines 32-33, change:***

However, if the identifier is declared or defined in more than one header,

***to:***

However, if an identifier is declared or defined in more than one header,


</div>


---

---

<div id="issue0017.25">

## Issue 0017.25: Should *must* appear in footnotes?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

“Must” in footnotes

This change is not essential since footnotes have no status. But this change
would cut down the number of occurrences of “shall” synonyms used where “shall”
itself could have be used.

---

Comment from WG14 on 1997-09-23:

### Response

The standard is clear enough as is.


</div>


---

---

<div id="issue0017.26">

## Issue 0017.26: Are unnamed union members required to be initialized?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.17](log_c90.md#issue0017.17)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Implicit initialization of unions with unnamed members

Are unnamed union members required to be initialized?

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #017, Question 17](log_c90.md#issue0017.17) for a clarifying correction
in this area.


</div>


---

---

<div id="issue0017.27">

## Issue 0017.27: Does the `#` flag alter zero stripping of `%g` in `fprintf`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Cross-references: [0040.09](log_c90.md#issue0040.09)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`g` conversions

Subclause 7.9.6.1 says on page 132, lines 42: “For `g` and `G` conversions,
trailing zeros will *not* be removed ...,” whereas on page 133, lines 37-38 it
says: “Trailing zeros are removed ...”

It has been suggested that the italics on page 132, lines 42 gives this rule
precedence. I don't mind which rule wins as long as the text says so. Do we add
text to describe the italics rule or change the conflicting lines?

---

Comment from WG14 on 1997-09-23:

### Response

In the collision between the description of the `#` flag and the `g` and `G`
conversion specifiers to `fprintf,` which takes precedence?

The `#` flag takes precedence. Subclause 7.9.6.1, page 132, line 1 says, “Zero
or more *flags* (in any order) ... modify the meaning of the conversion
specification.”


</div>


---

---

<div id="issue0017.28">

## Issue 0017.28: Does `errno` get stored before library functions return?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Ordering of conditions on return

In subclause 7.9.9.1, subclause 7.9.9.3, and subclause 7.9.9.4, the words are
“returns ... and stores an implementation-defined positive value in `errno`.”
This is a strange order of operations \- shouldn't the wording be reversed?

---

Comment from WG14 on 1997-09-23:

### Response

No. In subclause 7.9.9.1, subclause 7.9.9.3, and subclause 7.9.9.4, the words
“returns ... and stores an implementation-defined positive value in `errno`” do
not imply any temporal ordering. There are implementations that may perform
these operations in either order and they still meet the standard.


</div>


---

---

<div id="issue0017.29">

## Issue 0017.29: When does conversion failure occur in floating-point `fscanf` input?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Conversion failure and longest matches

Consider `1.2e+4` with field width of 5\. Is it input item `1.2e+` that gives a
conversion failure? What is the ordering between building input items and
converting them? Do they run in parallel, or sequential?

Refer to subclause 7.9.6.2 **The `fscanf` function**, page 135, lines 31-33
concerning the longest matching sequence, and subclause 7.9.6.2, page 137, lines
15-16 concerning a conflicting input character.

For `1.2e-x,` is `1.2` or `1.2e-` read?

The above questions all come about because of page 137, line 15: “If conversion
terminates ...” In this context the use of the word “conversion” could be
referring to the process of turning a sequence of characters into numeric form.
I believe what was intended was “If a conversion specifier terminates ...”

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citations are subclause 7.9.6.2, page 137, lines 15-16:

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.

and subclause 7.9.6.2, page 135, lines 31-33:

An input item is defined as the longest matching sequence of input characters,
unless that exceeds a specified field width, in which case it is the initial
subsequence of that length in the sequence.

and subclause 7.9.6.2, page 135, lines 38-40:

If the input item is not a matching sequence, the execution of the directive
fails: this condition is a matching failure.

The “conversion” in the first quoted passage is the process of both forming an
input item and converting it as specified by the conversion specifier.

About your example: If the characters available for input are “ `1.2e+4`” and
input is performed using a “`%5e`,” then the input item is “`1.2e+`” as defined
by the second passage quoted above. That input item is not a matching sequence,
but only an initial subsequence that fails to be a matching sequence in its own
right. Under the rules of the third quoted passage, this is a matching failure.

Note that in this case, no characters were pushed back onto the input stream.
There was no “conflicting input character” that terminated the field, and so the
first quoted passage does not apply.

See the Correction made in response to Defect Report #022, Question 1, for
additional clarification.


</div>


---

---

<div id="issue0017.30">

## Issue 0017.30: Do `fseek/fsetpos` require values from successful calls to `ftell/fgetpos`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Successful call to `ftell` or `fgetpos`

In subclause 7.9.9.2 on page 145, lines 39-40, “... a value returned by an
earlier call to the `ftell` function ...” should actually read “... a value
returned by an earlier successful call ...” Similarly for subclause 7.9.9.3.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.9.2, page 145, lines 39-40, change:***

a value returned by an earlier call to the `ftell` function

***to:***

a value returned by an earlier successful call to the `ftell` function

***In subclause 7.9.9.3, page 146, lines 10-11, change:***

a value obtained from an earlier call to the `fgetpos` function

***to:***

a value obtained from an earlier successful call to the `fgetpos` function


</div>


---

---

<div id="issue0017.31">

## Issue 0017.31: Are object sizes always in bytes?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Size in bytes

References to the size of an object in other parts of the standard specify that
size is measured in bytes. The following lines do not follow this convention:
subclause 7.10.3.1 on page 154, lines 26-27 and subclause 7.10.3.3 on page 155,
line 8\.

---

Comment from WG14 on 1997-09-23:

### Response

There are numerous places in the standard where “size in bytes” is used, and
numerous places where “size” alone is used. The Committee does not feel that any
of these places need fixing \- the meaning is everywhere clear, especially since
for `sizeof` in subclause 6.3.3.4 size is specifically mentioned in terms of
bytes.


</div>


---

---

<div id="issue0017.32">

## Issue 0017.32: Are `strcmp/strncmp` defined when `char` is signed?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

`char` parameters to `strcmp` and `strncmp`

Refer to subclause 7.11.4, page 164\. If `char` is signed then `char *` cannot
be interpreted as pointing to `unsigned char`. The required cast may give
undefined results. This applies to `strcmp` and `strncmp`.

---

Comment from WG14 on 1997-09-23:

### Response

`strcmp` can compare two `char` strings, even though the representation of
`char` may be signed, because subclause 7.11.4, page 164, line 7 says that the
interpretation of bytes is done as if each byte were accessed as an `unsigned
char`. We believe the standard is clear.


</div>


---

---

<div id="issue0017.33">

## Issue 0017.33: Are `strcmp/strncmp` defined for strings of differing length

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Different length strings

Refer to subclause 7.11.4, page 164, lines 5-7. What about strings of different
length?

Perhaps the fact that the terminating null character takes part in the
comparison ought to be mentioned.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.1.1 on page 96, lines 4-5 says that a string includes the
terminating null character. Therefore this character takes part in the
comparison. The standard is clear.


</div>


---

---

<div id="issue0017.34">

## Issue 0017.34: Is `strtok` described properly?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Calls to `strtok`

In subclause 7.11.5.8 on page 167, line 36, “... first call ...” should read
“... all calls ...”

I think that the current wording causes confusion. The first call is the one
that takes a non-`NULL` “`s1`” parameter. However, the discussion from line 36
onwards is describing the behavior for all calls.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee felt that the suggested wording for the `strtok` function
description is not an improvement. The existing wording is clear as written.


</div>


---

---

<div id="issue0017.35">

## Issue 0017.35: When is a physical source line created?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

When is a physical source line created?

Is the output or input to translation phase 1 a physical source line?

---

Comment from WG14 on 1997-09-23:

### Response

The use of the term “physical source line” occurs only in the description of the
phases of translation (subclause 5.1.1.2) and the question of whether the input
or output of phase 1 consists of physical source lines does not matter.


</div>


---

---

<div id="issue0017.36">

## Issue 0017.36: Is a function returning `const void` defined?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Qualifiers on function return type

Refer to subclause 6.6.6.4, page 80, line 24-25: “... whose return type is
`void`.”

The behavior of a type qualifier on a function return is explicitly undefined,
according to subclause 6.5.3, page 64, lines 24-25.

This creates a loophole.

An implementation that supports type qualifiers on function return types is not
required to flag the constraint given on page 80\.

---

Comment from WG14 on 1997-09-23:

### Response

A Constraint on subclause 6.7.1 says “The return type of a function shall be
`void` or an object type other than array.”


</div>


---

---

<div id="issue0017.37">

## Issue 0017.37: What is the type of a function call?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Function result type

Refer to subclause 6.3.2.2, page 40, line 35\. The result type of a function
call is not defined.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3.2.2, page 40, line 35, change:***

The value of the function call expression is specified in 6.6.6.4.

***to:***

If the expression that denotes the called function has type pointer to function
returning an object type, the function call expression has the same type as that
object type, and has the value determined as specified in 6.6.6.4. Otherwise,
the function call has type `void`.


</div>


---

---

<div id="issue0017.38">

## Issue 0017.38: What is an iteration control structure or selection control structure?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

What is an iteration control structure or selection control structure?

An “iteration control structure,” a term used in subclause 5.2.4.1 **Translation
limits** on page 13, line 1, is not defined by the standard.

Is it:

1. A `for` loop header excluding its body, e.g. `for (;;)`,

   or
2. A `for` loop header plus its body, e.g. `for (;;) {}`?

Does it make a difference if the compound statement is a simple statement
without the braces?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.2.4.1, page 13, lines 1-2, change:***

\- 15 nested levels of compound statements, iteration control structures, and
selection control structures

***to:***

\- 15 nested levels of compound statements, iteration statements, and selection
statements


</div>


---

---

<div id="issue0017.39">

## Issue 0017.39: Are header names tokens outside include directives?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0040.04](log_c90.md#issue0040.04), [0146](log_c90.md#issue0146)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Header name tokenization

There is an inconsistency between subclause 6.1.7, page 33, line 8 and the
description of the creation of header name preprocessing tokens.

The “shall” on page 32, line 33 does not limit the creation of header name
preprocessing tokens to within `#include` directives. It simply states that they
would cause a constraint error in this context.

Subclause 6.1.7, page 33, line 8 should read {`0x3`}{`<1/a.h>`}{`1e2`}, or extra
text needs to be added to subclause 6.1.7.

I have not met anybody who expects `if (a<b || c>d)` to parse as {`if`} {`(`}
{`a`} {`<b || c>`} {`d`} {`)`}.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 6.1, page 18 (Semantics):***

A header name preprocessing token is only recognized within a `#include`
preprocessing directive, and within such a directive, a sequence of characters
that could be either a header name or a string literal is recognized as the
former.

***Add to subclause 6.1.2, page 20 (Semantics):***

When preprocessing tokens are converted to tokens during translation phase 7, if
a preprocessing token could be converted to either a keyword or an identifier,
it is converted to a keyword.

***In subclause 6.1.7, page 32, lines 32-34, delete:***

**Constraint**

Header name preprocessing tokens shall only appear within a `#include`
preprocessing directive.

***Add to subclause 6.1.7, page 32 (Semantics):***

A header name preprocessing token is recognized only within a `#include`
preprocessing directive.


</div>


---

---

<div id="issue0018">

## Issue 0018: Does `fscanf` recognize literal multibyte characters properly?

Authors: Yasushi Nakahara, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-066  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_018.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_018.html)

It is unclear how the `fscanf` function shall behave when executing directives
that include “ordinary multibyte characters,” especially in the case of
shift-encoded ordinary multibyte characters.

The following statements are described in subclause 7.9.6.2 **The `fscanf`
function** of the current standard:

A directive that is an ordinary multibyte character is executed by reading the
next characters of the stream. If one of the characters differs from one
comprising the directive, the directive fails, and the differing and subsequent
characters remain unread.

Assume a typical shift-encoded directive: `A\*` in 7-bit representation. And
consider two different encoding systems, Latin Alphabet No.1 \- 8859/1 and
German Standard DIN 66 003\. The codes are, for example,

```c
A; in 8859/1: SO 4/4 SI
 A; in DIN 66 003: ESC 2/8 4/11 5/11 ESC 2/8 4/2
```

`where SO` is a Shift-Out code (0/15 \= 0x0F) and **SI** corresponds to a
Shift-In code (0/14). “`ESC 2/8 4/11`” is an escape sequence for the German
Standard DIN 66 003, and “`ESC 2/8 4/2`” is for ISO 646 USA Version (ASCII).

Assuming that a subject sequence includes `A;`, `O;`, and `U;` with the
following 7-bit representations,

```c
in 8859/1: SO 4/4 5/6 5/12 SI
 in DIN 66 003: ESC 2/8 4/11 5/11 5/12 5/13 ESC 2/8 4/2
```

does the “`A;`” directive in the `fscanf` format string match the beginning part
of the“`A;O;U;`” sequence?

At what position of the target sequence shall the “`A;`” directive fail?

One interpretation of this is that because the current standard defined the
behavior of the directive in the `fscanf` format based on the word “character”
(byte), not using the term “multibyte character,” the comparison shall be done
on a byte-by-byte basis. One may conclude that the “`A;`” directive never
matches the “`;”;O;U` sequence in this case.

Another interpretation may lead to an opposite conclusion, saying that the
current standard's statements quoted above do not necessarily mean that such
comparison shall be done on a byte-by-byte basis. Instead, it is read that the
matching shall be done on a “multibyte character by multibyte character basis”
or rather “wide character by wide character basis.” Especially, a “ghost”
sequence like “`ESC ...`” and `SI`*`/`*`SO` characters should not be regarded as
independent ordinary multibyte characters in this case.

Which is a correct interpretation of the current standard?

These different interpretations are caused by the ambiguity of the descriptions
in the current standard. Also, it should be pointed out that the major problem
here is usage of the word “character.” The generic word “character” and the
specific word “character(\=byte)” should be properly discriminated in the
standard.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.9.6.2 says, “A directive that is an ordinary multibyte character is
executed by reading the next *characters* ...” \[emphasis added]. Consistently
throughout the standard, plain “characters” refers to one-byte characters. (See
subclause 3.5 for the definition of “character.”)


</div>


---

---

<div id="issue0019">

## Issue 0019: Are printing characters implementation defined?

Authors: Richard Wiersma, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-014  
Status: Closed  
Cross-references: [0132](log_c90.md#issue0132)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_019.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_019.html)

Background:

Subclause 7.3.1.5 states that “the `isgraph` function tests for any printing
character except space.” Subclause 7.3.1.7 states that “the `isprint` function
tests for any printing character including space.”

The third paragraph of subclause 7.3 defines the term *printing character* as “a
member of an implementation-defined set of characters, each of which occupies
one printing position on a display device.”

Subclause 5.2.1 defines the source and execution character sets and provides a
list of characters which must be contained in both sets.

Question for interpretation: Are the `isprint` and `isgraph` functions required
to return a non-zero value for all of the characters defined in subclause 5.2.1?

A scenario for use of `isprint`/`isgraph` that depends on the interpretation is:
A developer may wish to use these functions to determine whether a particular
character can be displayed as itself (e.g., whether a square bracket is actually
displayed as a square bracket). This could be useful for formatting output in a
device-independent manner, since the application could substitute some other
character for ones that do not print “correctly.”

If `isprint` and `isgraph` are required to return non-zero for all characters in
subclause 5.2.1, developers cannot use them for this purpose.

This problem has occurred in a real implementation. The most commonly used
terminals and printers for IBM System/370 computers do not support all of the
characters listed in subclause 5.2.1. For example, most IBM printers and
terminals do not print the square brackets.

The SAS/C implementation of `isprint` and `isgraph` assumes that subclause 7.3
controls the behavior of these functions, and returns non-zero only for those
characters that print “correctly.” The Plum Hall test suite, however, assumes
that `isprint` and `isgraph` return non-zero for all characters listed in
subclause 5.2.1.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.3, page 102, line 8 says that *printing character* is
implementation-defined. In particular, the value (zero or non-zero) of
`isprint('[')` is implementation-defined, *even in the* `"C"` *`locale.`*


</div>


---

---

<div id="issue0020">

## Issue 0020: Is the relaxed Ref/Def linkage model conforming?

Authors: Bruce Lambert, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-006  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_020.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_020.html)

Is a compiler which allows the Relaxed Ref/Def linkage model to be considered a
conforming compiler? That is, can a compiler that compiles the following code
with no errors or warnings

```c
filea.c:
 #include stdio.h>
 void foo(void);
 int age;
 int main()
 {
 age = 24;
 printf("my age is %d.\n", age);
 foo();
 printf("my age is %d.\n", age);
 return 0;
 }

 fileb.c:
 #include <stdio.h>
 int age;
 void foo()
 {
 age = 25;
 printf("your age is %d.\n", age);
 }
```

and which produces the following output

```c
my age is 24
 your age is 25
 my age is 25
```

be called a standard-compliant compiler?

---

Comment from WG14 on 1997-09-23:

### Response

Yes, a compiler that allows the Relaxed Ref/Def model can be standard
conforming. (In this case, the model permits two tentative definitions for `age`
in two translation units to resolve to a single definition at link time.) See
subclause 6.7, page 81, lines 23-25. The code is conforming but not strictly
conforming. The behavior is undefined.


</div>


---

---

<div id="issue0021">

## Issue 0021: What is the result of `printf("%#.4o", 345)`?

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-001  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_021.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_021.html)

What is the result of: `printf("%#.4o", 345);`? Is it `0531` or is it `00531`?

Subclause 7.9.6.1, on page 132, lines 37-38 says: “For `o` conversion, it
increases the precision to force the first digit of the result to be a zero.”

Is this a conditional or an unconditional increase in the precision if the most
significant digit is not already a `0`? Which is the correct interpretation?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.6.1, page 132, lines 37-38, change:***

For `o` conversion, it increases the precision to force the first digit of the
result to be a zero.

***to:***

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of the result to be a zero.


</div>


---

---

<div id="issue0022">

## Issue 0022: What is the result of `strtod("100ergs", &ptr)`?

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-002  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_022.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_022.html)

What is the result of: `strtod("100ergs", &ptr);`? Is it 100.0 or is it 0.0?

Subclause 7.10.1.4 **The `strtod` function** on page 150, lines 36-38 says: “The
subject sequence is defined as the longest initial subsequence of the input
string, starting with the first non-white-space character, that is of the
expected form.” In this case, the longest initial subsequence of the expected
form is `100`, so `100.0` should be the return value. Also, since the entire
string is in memory, `strtod` can scan it as many times as need be to find the
longest valid initial subsequence.

Subclause 7.9.6.2 **The `fscanf` function** on page 136, lines 17-18 says:
“`e`,`f`,`g` Matches an optionally signed floating-point number, whose format is
the same as expected for the subject string of the `strtod` function.” Later,
page 138, lines 6, 16, and 25 show that `100ergs` fails to match `%f`. Those two
show that `100ergs` is invalid to `fscanf` and therefore, invalid to `strtod`.
Then, subclause 7.10.1.4, page 151, lines 11-12, “If no conversion could be
performed, zero is returned” indicates for an error input, 0.0 should be
returned. The reason this is invalid is spelled out in the rationale document,
subclause 7.9.6.2 **The `fscanf` function**, page 85: “One-character pushback is
sufficient for the implementation of `fscanf`. Given the invalid field `-.x`,
the characters `-.` are not pushed back.” And later, “The conversions performed
by `fscanf` are compatible with those performed by `strtod` and `strtol`.”

So, do `strtod` and `fscanf` act alike and both accept and fail on the same
inputs, by the one-character pushback scanning strategy, or do they use
different scanning strategies and `strtod` accept more than `fscanf`?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.9.6.2, page 135, lines 31-33, change:***

An input item is defined as the longest matching sequence of input characters,
unless that exceeds a specified field width, in which case it is the initial
subsequence of that length in the sequence.

***to:***

An input item is defined as the longest sequence of input characters which does
not exceed any specified field width and which is, or is a prefix of, a matching
input sequence.

***In subclause 7.9.6.2, page 137, delete:***

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.

***Add to subclause 7.9.6.2, page 137:***

If conversion terminates on a conflicting input character, the offending input
character is left unread in the input stream.\* \[Footnote \*: `fscanf` pushes
back at most one input character onto the input stream. Therefore, some
sequences that are acceptable to `strtod`, `strtol`, or `strtoul` are
unacceptable to `fscanf`.]


</div>


---

---

<div id="issue0023">

## Issue 0023: If 99,999 is larger than `DBL_MAX_10_EXP`, what is the result of `strtod("0.0e99999", &ptr)`?

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-003  
Status: Closed  
Cross-references: [0025](log_c90.md#issue0025)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_023.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_023.html)

Assuming that 99999 is larger than `DBL_MAX_10_EXP`, what is the result of:

```c
strtod("0.0e99999", &ptr);
```

Is it 0.0, `HUGE_VAL`, or undefined?

Subclause 6.1.3.1 **Floating constants** on page 26, lines 30-32 says: “The
significand part is interpreted as a decimal rational number; the digit sequence
in the exponent part is interpreted as a decimal integer. The exponent indicates
the power of 10 by which the significand part is to be scaled.” In this case
`0.0e99999` means 0.0 times 10 to the power 99999, or 0.0x10<sup>99999</sup>,
which has a scaled value of 0.0; therefore, return 0.0.

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 12-14 says: “If
the correct value is outside the range of representable values, plus or minus
`HUGE_VAL` is returned (according to the sign of the value), and the value of
the macro `ERANGE` is stored in `errno`.” Since the exponent (99999 in this
case) is larger than `DBL_MAX_10_EXP`, the value is outside the range of
representable values (overflow). Therefore, return `HUGE_VAL`.

Subclause 5.2.4.2.2 **Characteristics of floating types \<`float.h>`**, pages
14-16, describes the model that defines the floating-point types. The number
`0.0e99999`, as written, is not part of that model (it cannot be represented
since the exponent is larger than *e<sub>max</sub>*). From subclause 6.2.1.4
**Floating types** page 35, lines 11-13, “... if the value being converted is
outside the range of values that can be represented, the behavior is undefined.”
Therefore, since this number, as written, has no representation, the behavior is
undefined.

---

Comment from WG14 on 1997-09-23:

### Response

According to our response to [Defect Report #025, Question 1](log_c90.md#issue0025), the
result of `strtod("0.0e99999", &ptr)` is exactly representable, i.e., it lies
within the range of representable values. Therefore, by subclause 7.10.1.4,
**Returns**, the value zero shall be returned in this case, and `errno` shall
not be set. (This means that implementations have to test for the special case
of zero when creating floating-point representations from characters.)

Note also that `strtod("0.0e-99999", &ptr)` is not a case of underflow, so
`errno` shall not be set to `ERANGE` in this case either.


</div>


---

---

<div id="issue0024">

## Issue 0024: For `strtod`, what does `"C"` locale mean?

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-004  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_024.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_024.html)

In subclause 7.10.1.4 **The `strtod` function** page 151, line 5: What does
“`"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) == "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) == "C"
```

c. `&&`

d.

```c
||
```

e. something else.

What does “other than the `"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) != "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) != "Ct
```

c.

```c
&&
```

d.

```c
||
```

e. something else.

Subclause 7.4.1 **Locale control**, page 107 may help answer the questions.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.4.1.1, page 107, lines 11-17 describe what is affected by each
locale portion.

Is it the `LC_NUMERIC` locale category which affects the implementation-defined
behavior of `strtod`, etc.?

Answer: Yes.

How can one guarantee that `strtod` functions are in the `"C"` locale?

Answer: Execute `setlocale(LC_NUMERIC, "C")` or execute `setlocale(LC_ALL, "C")`
.

What is meant by “other than the `"C"` locale?” That is, how can one ensure that
`strtod` is not in the `"C"` locale?

Answer: Successfully execute `setlocale(LC_NUMERIC, str)` or `setlocale(LC_ALL,
str)` to some implementation-defined string `str` which specifies a locale that
is different from the `"C"` locale. No universally portable method can be
provided, because the functionality is implementation-defined.


</div>


---

---

<div id="issue0025">

## Issue 0025: What is meant by *representable floating-point value?*

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-005  
Status: Closed  
Cross-references: [0023](log_c90.md#issue0023)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_025.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_025.html)

What is meant by “representable floating-point value?” Assume double precision,
unless stated otherwise.

First, some definitions based partially upon the floating-point model in
subclause 5.2.4.2.2, on pages 14-16 of the C Standard:

1. \+Normal Numbers: `DBL_MIN` to `DBL_MAX`, inclusive; normalized (first significand digit is non-zero), sign is \+1.
2. -Normal Numbers: `-DBL_MAX` to `-DBL_MIN`, inclusive; normalized.
3. \+Zero: All digits zero, sign is \+1; (true zero).
4. -Zero: All digits zero, sign is -1.
5. Zero: Union of \+zero and -zero.
6. \+Denormals: Exponent is “minimum” (biased exponent is zero); first significand digit is zero; sign is \+1. These are in range `+DBL_DeN` (inclusive) to `+DBL_MIN` (exclusive). (Let `DBL_DeN` be the symbol for the minimum positive denormal, so we can talk about it by name.)
7. -Denormals: same as \+denormals, except sign, and range is `-DBL_MIN` (exclusive) to `-DBL_DeN` (inclusive).
8. \+Unnormals: Biased exponent is non-zero; first significand digit is zero; sign is \+1. These overlap the range of \+normals and \+denormals.
9. -Unnormals: Same as \+unnormals, except sign; range is over -normals and -denormals.
10. \+infinity: From IEEE-754.
11. -infinity: From IEEE-754.
12. Quiet NaN (Not a Number); sign does not matter; from IEEE-754.
13. Signaling NaN; sign does not matter; from IEEE-754.
14. NaN: Union of Quiet NaN and Signaling NaN.
15. Others: Reserved (VAX?) and Indefinite (CDC/Cray?) act like NaN.

On the real number line, these symbols order as:

```c
[   1   )[   2   ](   3   ](  4 )[5](  6 )[   7   )[   8   ](   9   ]
+--------+-------+--------+------+-+------+--------+-------+--------+
-INF -DBL_MAX -DBL_MIN -DBL_Den -0 +0 +DBL_Den +DBL_MIN +DBL_MAX +INF
```

Non-real numbers are: SNaN, QNaN, and NaN; call this region 10\.

Regions 1 and 9 are overflow, 2 and 8 are normal numbers, 3 and 7 are denormal
numbers (pseudo underflow), 4 and 6 are true underflow, and 5 is zero.

So, the question is: What does “representable (double-precision) floating-point
value” mean:

a. Regions 2, 5 and 8 (\+/- normals and zero)

b. Regions 2, 3, 5, 7, and 8 (\+/- normals, denormals, and zero)

c. Regions 2 through 8 \[`-DBL_MAX` ... `+DBL_MAX`]

d. Regions 1 through 9 \[-INF ... \+INF]

e. Regions 1 through 10 (reals and non-reals)

f. What the hardware can represent

g. Something else? What?

Some things to consider in your answer follow. The questions that follow are
rhetorical and do not need answers.

Subclause 5.2.4.2.2 **Characteristics of floating types `<float.h>`**, page 14,
lines 32-34:

> The characteristics of floating types are defined in terms of a model that
> describes a representation of floating-point numbers and values that provide
> information about an implementation's floating-point arithmetic.

Same section, page 15, line 6:

> A normalized floating-point number *x* ... is defined by the following model:
> ...

That model is just normalized numbers and zero (appears to include signed
zeros). It excludes denormal and unnormal numbers, infinities, and NaNs. Are
signed zeros required, or just allowed?

Subclause 6.1.3.1 **Floating constants**, page 26, lines 32-35: “If the scaled
value is in the range of representable values (for its type) the result is
either the nearest representable value, or the larger or smaller representable
value immediately adjacent to the nearest value, chosen in an
implementation-defined manner.”

```c
A B y C x D E z F
 -DBL_Den 0.0 +DBL_Den +DBL_MIN +DBL_MAX +INF
```

The representable numbers are A, B, C, D, E, and F. The number x can be
converted to B, C, or D! But what if B is zero, C is `DBL_DeN` (denormal), and D
is `DBL_MIN` (normalized). Is x representable? It is not in the range `DBL_MIN
... DBL_MAX` and its inverse causes overflow; so those say not valid. On the
other hand, it is in the range `DBL_DeN ... DBL_MAX` and it does not cause
underflow; so those say it is valid.

What if B is zero, A is `-DBL_DeN` (denormal), and C is `+DBL_DeN` (denormal);
is y representable? If so, its nearest value is zero, and the immediately
adjacent values include a positive and a negative number. So a user-written
positive number is allowed to end up with a negative value!

What if E is `DBL_MAX` and F is infinity (on a machine that uses infinities,
IEEE-754)? Does z have a representation? If z came from 1.0/x, then z caused
overflow which says invalid. But on IEEE-754 machines, it would either be
`DBL_MAX` or infinity depending upon the rounding control, so it has a
representation and is valid.

What is “nearest?” In linear or logarithmic sense? If the number is between 0
and `DBL_DeN`, e.g.,

10<sup>-99999</sup>, it is linear-nearest to zero, but log-nearest to `DBL_DeN`.
If the number is between `DBL_MAX` and INF, e.g., 10<sup>\+99999</sup>, it is
linear- and log-nearest to `DBL_MAX`. Or is everything bigger than `DBL_MAX`
nearest to INF?

Subclause 6.2.1.3 **Floating and integral**, page 35, Footnote 29: “Thus, the
range of portable floating values is (-1,`Utype_MAX`\+1).”

Subclause 6.2.1.4 **Floating types**, page 35, lines 11-15: “When a `double` is
demoted to `float` or a `long double` to `double` or `float`, if the value being
converted is outside the range of values that can be represented, the behavior
is undefined. If the value being converted is in the range of values that can be
represented but cannot be represented exactly, the result is either the nearest
higher or nearest lower value, chosen in an implementation-defined manner.”

Subclause 6.3 **Expressions**, page 38, lines 15-17: “If an *exception* occurs
during the evaluation of an expression (that is, if the result is not
mathematically defined or not in the range of representable values for its
type), the behavior is undefined.”

```c
w = 1.0 / 0.0 ; /* infinity in IEEE-754 */
 x = 0.0 / 0.0 ; /* NaN in IEEE-754 */
 y = +0.0 ; /* plus zero */
 z = - y ; /* minus zero: Must this be -0.0? May it be +0.0? */
```

Are the above representable?

Subclause 7.5.1 **Treatment of error conditions**, page 111, lines 11-12: “The
behavior of each of these functions is defined for all representable values of
its input arguments.”

What about non-numbers? Are they representable? What is `sin(`*`NaN`*`)`? If you
got a NaN as input, then you can return NaN as output. But, is it a domain
error? Must `errno` be set to `EDOM`? The NaN already indicates an error, so
setting `errno` adds no more information. Assuming NaN is not part of Standard C
“representable,” but the hardware supports it, then using NaNs is an extension
of Standard C and setting `errno` need not be required, but is allowed. Correct?

Subclause 7.5.1 **Treatment of error conditions**, on page 111, lines 20-27
says: “Similarly, a *range error* occurs if the result of the function cannot be
represented as a `double` value. If the result overflows (the magnitude of the
result is so large that it cannot be represented in an object of the specified
type), the function returns the value of the macro `HUGE_VAL`, with the same
sign (except for the `tan` function) as the correct value of the function; the
value of the macro `ERANGE` is stored in `errno`. If the result underflows (the
magnitude of the result is so small that it cannot be represented in an object
of the specified type), the function returns zero; whether the integer
expression `errno` acquires the value of the macro `ERANGE` is
implementation-defined.”

What about denormal numbers? What is `sin(DBL_MIN/3.0L)`? Must this be
considered underflow and therefore return zero, and maybe set `errno` to
`ERANGE`? Or may it return `DBL_MIN/3.0`, a denormal number? Assuming denormals
are not part of Standard C “representable,” but the hardware supports it, then
using them is an extension of Standard C and setting `errno` need not be
required, but is allowed. Correct?

What about infinity? What is `exp(`*`INF`*`)`? If you got an INF as input, then
you can return INF as output. But, is it a range error? The output value is
representable, so that says: no error. The output value is bigger than
`DBL_MAX`, so that says: an error and set `errno` to `ERANGE`. Assuming infinity
is not part of Standard C “representable,” but the hardware supports it, then
using INFs is an extension of Standard C and setting `errno` need not be
required, but is allowed. Correct?

What about signed zeros? What is `sin(-0.0)`? Must this return -0.0? May it
return -0.0? May it return \+0.0? Signed zeros appear to be required in the
model in subclause 5.2.4.2.2 on page 15\.

What is `sqrt(-0.0)`? IEEE-754 and IEEE-854 (floating-point standards) say this
must be -0. Is -0.0 negative? Is this a domain error?

Subclause 7.9.6.1 **The `fprintf` function** on page 132, lines 32-33 says: “(It
will begin with a sign only when a negative value is converted if this flag is
not specified.)”

What is `fprintf(stdout, "%+.1f", -0.0);`? Must it be -0.0? May it be \+0.0? Is
-0.0 a negative value? The model on page 15 appears to require support for
signed zeros.

What is `fprintf(stdout, "%f %f", 1.0/0.0, 0.0/0.0);`? May it be the IEEE-854
strings of `inf` or `infinity` for the infinity and `NaN` for the quiet NaN?
Would `NaNQ` also be allowed for a quiet NaN? Would `NaNS` be allowed for a
signaling NaN? Must the sign be printed? Signs are optional in IEEE-754 and
IEEE-854. Or, must it be some decimal notation as specified by subclause
7.9.6.1, page 133, line 19? Does the locale matter?

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 2-3 says: “If
the subject sequence begins with a minus sign, the value resulting from the
conversion is negated.”

What is `strtod("-0.0", &ptr)`? Must it be -0.0? May it be \+0.0? The model on
page 15 appears to require support for signed zeros. All floating-point hardware
I know about support signed zeros at least at the load, store, and
negate/complement instruction level.

Subclause 7.10.1.4 **The `strtod` function** on page 151, lines 12-15 say: “If
the correct value is outside the range of representable values, plus or minus
`HUGE_VAL` is returned (according to the sign of the value), and the value of
the macro `ERANGE` is stored in `errno`. If the correct value would cause
underflow, zero is returned and the value of the macro `ERANGE` is stored in
`errno`.”

If `HUGE_VAL` is \+infinity, then is `strtod("1e99999", &ptr)` outside the range
of representable values, and a range error? Or is it the “nearest” of `DBL_MAX`
and INF?

---

Comment from WG14 on 1997-09-23:

### Response

Principles for C floating-point representation:

(These principles are intended to clarify the use of some terms in the standard;
they are not meant to impose additional constraints on conforming
implementations.)

1. “Value” refers to the abstract (mathematical) meaning; “representation” refers to the implementation data pattern.
2. Some (not all) values have exact representations.
3. There may be multiple exact representations for the same value; all such representations shall compare equal.
4. Exact representations of different values shall compare unequal.
5. There shall be at least one exact representation for the value zero.
6. Implementations are allowed considerable latitude in the way they represent floating-point quantities; in particular, as noted in Footnote 10 on page 14, the implementation need not exactly conform to the model given in subclause 5.2.4.2.2 for “normalized floating-point numbers.”
7. There may be minimum and/or maximum exactly-representable values; all values between and including such extrema are considered to “lie within the range of representable values.”
8. Implementations may elect to represent “infinite” values, in which case all real numbers would lie within the range of representable values.
9. For a given value, the “nearest representable value” is that exactly-representable value within the range of representable values that is closest (mathematically, using the usual Euclidean norm) to the given value.

(Points 3 and 4 are meant to apply to representations of the same floating type,
not meant for comparison between different types.)

This implies that a conforming implementation is allowed to accept a
floating-point constant of any arbitrarily large or small value.


</div>


---

---

<div id="issue0026">

## Issue 0026: Can one use other than the basic C character set in a strictly conforming program?

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-007  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_026.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_026.html)

Example:

```c
#include stdio.h>
 int main()
 {
 puts("@$(etc.)");
 return 0;
 }
```

Is this a strictly conforming program?

---

Comment from WG14 on 1997-09-23:

### Response

Strictly conforming programs cannot depend on unspecified or
implementation-defined behavior (cf. clause 4, page 3, lines 31-32). Note that
`@` and `$` are extended source characters. Source characters are translated to
execution characters in an unspecified manner (cf. subclause 5.2.1). This is in
the `"C"` locale. The `@` character is either a printing character or a control
character, either of which is implementation-defined (subclause 7.3, page 102,
lines 8-11). Therefore, the program is *not* strictly conforming.


</div>


---

---

<div id="issue0027">

## Issue 0027: May a standard conforming implementation add identifier characters?

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-008  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_027.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_027.html)

May a standard conforming implementation make characters in its character set
that are not in the required source character set identifier characters? Can
these additional identifier characters be used in preprocessor identifier tokens
as well as post-processor identifier tokens?

Subclause G.5.2 states:

> Characters other than the underscore `_`, letters, and digits, that are not
> defined in the required source character set (such as the dollar sign `$`, or
> characters in national character sets) may appear in an identifier (subclause
> 6.1.2).

---

Comment from WG14 on 1997-09-23:

### Response

May a standard conforming implementation make characters in its character set
that are not in the required source character set identifier characters?

Answer: Yes.

Can these additional identifier characters be used in preprocessor identifier
tokens as well as post-processor identifier tokens?

Answer: Yes, but the C Standard is currently ambiguous about the parsing of a
definition such as:

```c
#define abc$ x
```

This could either define `abc$` as `x` or `abc` as `$x`. The Correction that
follows resolves the ambiguity.

### Correction

***Add to subclause 6.8, page 86 (Constraints):***

In the definition of an object-like macro, if the first character of a
replacement list is not a character required by subclause 5.2.1, then there
shall be white-space separation between the identifier and the replacement
list.**\***

\[Footnote \*: This allows an implementation to choose to interpret the
directive:

```c
#define THIS$AND$THAT(a, b) ((a) + (b))
```

as defining a function-like macro `THIS$AND$THAT`, rather than an object-like
macro `THIS`. Whichever choice it makes, it must also issue a diagnostic.]


</div>


---

---

<div id="issue0028">

## Issue 0028: What are the aliasing rules for dynamically allocated objects?

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-009  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_028.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_028.html)

Subclause 6.3, page 38, lines 18-27 state some very important rules governing
how a strictly conforming program can access the value of an object. The basic
theme of the rules is that an object's value may only be accessed through an
lvalue of the appropriate type. These rules are required to permit C programs to
be optimized.

The rules depend on the “declared type of the object.” This seems to make the
rules not apply if the object was not declared, which is the case for an object
allocated using `malloc()`.

Do the rules somehow apply to dynamically allocated objects? Is a compiler free
to optimize the following function:

```c
void f(int *x, double *y)
 {
 *x = 0;
 *y = 3.14;
 *x = *x + 2;
 }
```

into the equivalent function:

```c
void f(int *x, double *y)
 {
 *x = 0;
 *y = 3.14;
 *x = 2; /* *x known to be zero */
 }
```

Or must an optimizer prove that pointers are not pointing at dynamically
allocated storage before performing such optimizations?

---

Comment from WG14 on 1997-09-23:

### Response

Case 1: unions `f(&u.i, &u.d)`

Subclause 6.3.2.3, page 42, lines 5-6:

> ... if a member of a union object is accessed after a value has been stored in a
> different member of the object, the behavior is implementation-defined.

Therefore, an alias is not permitted and the optimization is allowed.

Case 2: declared objects `f((int *)&d, &d)`

Subclause 6.3, page 38, lines 18-27 list specific ways in which declared objects
can be accessed. Therefore, an alias is not permitted and the optimization is
allowed.

Case 3: any other, including `malloc`ed objects `f((int *)dp, dp)`

We must take recourse to intent. The intent is clear from the above two
citations and from Footnote 36 on page 38:

The intent of this list is to specify those circumstances in which an object may
or may not be aliased.

Therefore, this alias is not permitted and the optimization is allowed.

In summary, yes, the rules do apply to dynamically allocated objects.


</div>


---

---

<div id="issue0029">

## Issue 0029: Must compatible structs/unions have the same tag in different translation units?

Authors: Sam Kendall, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-016  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_029.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_029.html)

Subclause 6.1.2.6 says:

> ... two structure, union, or enumeration types declared in separate translation
> units are compatible if they have the same number of members, the same member
> names, and compatible member types; for two structures, the members shall be in
> the same order; for two structures or unions, the bit-fields shall have the same
> widths; for two enumerations, the members shall have the same values.

I have one question and one clarification, both about compatibility between two
`struct`/`union`/`enum` types declared in separate translation units.

(1) Was it the Committee's intent that the two types must have the same tag (or
both lack tags) to be compatible? As the standard is written, the following is
legal:

```c
One Translation Unit:
 struct foo { int i; } x;
 Another Translation Unit:
 extern struct bar { int i; } x;
```

Recommendation: This seems like an accidental omission. To be compatible, the
two types should have the same tag, or both lack tags. I would guess that such
was the Committee's intent.

(2) Clarification: The phrase “two structure, union, or enumeration types”
should be written “two structure types, two union types, or two enumeration
types.” The current standard, interpreted literally, allows a structure and a
union with identical member lists to be compatible, even though this is clearly
not the intent of the Committee.

```c
One Translation Unit:
 union foo { int i; } x;
 union bar { int i, j; } y;
 Another Translation Unit:
 extern struct foo { int i; } x;
 extern struct bar { int i, j; } y;
```

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2.6 says (by omission) that tags do not have to be the same for
structure, union, or enumeration types to be compatible in separate translation
units. Tags are used in succeeding declarations to ensure that they are of the
same type. They are not used for type compatibility.

Does “two structure, union, and enumeration types” mean “two structure types,
two union types, or two enumeration types?”

Answer: Yes.


</div>


---

---

<div id="issue0030">

## Issue 0030: May `sin(DBL_MAX)` set `errno` to `EDOM`?

Authors: Pawel Molenda, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-017  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_030.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_030.html)

Reference: subclause 7.5.1 **Treatment of error conditions**, page 111, lines
14-17:

> For all functions, a *domain error* occurs if an input argument is outside the
> domain over which the mathematical function is defined. ... an implementation
> may define additional domain errors, provided that such errors are consistent
> with the mathematical definition of the function.

If `sin(DBL_MAX)` results in `errno` being set to `EDOM`, is this a violation of
the standard? If yes, what should be the result of this call?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.5.1 does not give license for an implementation to set `errno` to
`EDOM` for `sin(DBL_MAX)`. The mathematical function is defined for that
argument value. While a conforming hosted implementation must not set `errno` to
`EDOM` for this case, the standard imposes no constraint on the accuracy of the
result value.


</div>


---

---

<div id="issue0031">

## Issue 0031: How are exceptions handled in constant expressions?

Authors: Pawel Molenda, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-018  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_031.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_031.html)

Referring to subclause 6.3, page 38, lines 15-17:

> If an *exception* occurs during the evaluation of an expression (that is, if the
> result is not mathematically defined or not in the range of representable values
> for its type), the behavior is undefined.

and subclause 6.4, page 55, lines 11-12:

> Each constant expression shall evaluate to a constant that is in the range of
> representable values for its type.

What should be the result of the constant expression:

```c
INT_MAX + 2
```

Is this a constraint violation, or it should be mapped onto the set of
representable values?

What should be the result of:

```c
INT_MAX + 2ul
```

How should compilers that do not evaluate the constant expressions at compile
time behave?

What is the result of:

```c
(INT_MAX*4)/4
```

Referring to subclause 6.5.2.2, page 61, lines 29-30:

> The expression that defines the value of an enumeration constant shall be an
> integral constant expression that has a value representable as an `int.`

What is the result of:

```c
enum { a=INT_MAX, b };
```

Does this violate the C Standard?

---

Comment from WG14 on 1997-09-23:

### Response

`case INT_MAX + 2:` is a constraint violation.

`case INT_MAX + 2ul:` is okay, representable.

`case (INT_MAX*4)/4:` is a constraint violation.

When subclause 6.4 says on page 55, lines 11-12:

> Each constant expression shall evaluate to a constant that is in the range of
> representable values for its type.

the Committee's judgement of the intent is that the “representable” requirement
applies to each subexpression of a constant expression, as shown in the third
example. A constant expression is meant as defined by the syntax rules.

`enum {a=INT_MAX, b};` is a constraint violation.


</div>


---

---

<div id="issue0032">

## Issue 0032: Can an implementation permit a comma operator in a constant expression?

Authors: Stephen D. Clamage, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-036  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_032.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_032.html)

In subclause 6.4, page 55, line 10, a constraint specifies that a comma operator
may not appear in a constant expression (except within the operand of a `sizeof`
operator).

At the end of the same section, page 56, line 1, it says, “An implementation may
accept other forms of constant expressions.”

Does the later statement give a license to relax the earlier constraint? For
example, may a conforming implementation accept

```c
int i = (1, 2);
```

without issuing a diagnostic?

---

Comment from WG14 on 1997-09-23:

### Response

No, a conforming implementation may not accept this example without issuing a
diagnostic. Constraint violations always require a diagnostic (subclause
5.1.1.3). The intent of the statement “An implementation may accept other forms
of constant expressions” (subclause 6.4) is to allow an implementation to accept
syntactic forms, such as might be generated by the `offsetof` macro, that may
not otherwise be semantically allowed.


</div>


---

---

<div id="issue0033">

## Issue 0033: Must a conforming implementation diagnose *shall* violations outside **Constraints**?

Authors: Mike Vermeulen, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-037  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_033.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_033.html)

Is a conforming implementation required to diagnose all violations of “shall”
and “shall not” statements in the standard, even if those statements occur
outside of a section labeled **Constraints**?

An example that illustrates this question is:

```c
struct s { char field:1; };
```

This fragment violates a statement in subclause 6.5.2.1 on page 60, line 30: “A
bit-field shall have a type that is a qualified or unqualified version of one of
`int`, `unsigned int`, or `signed int`.” Must a conforming implementation issue
a diagnostic for this violation of “shall?”

Following are two different ways in which the C Standard has been interpreted.
These interpretations came up during discussions over NIST conformance tests for
an ANSI-C FIPS. I would like to ask the Committee for an interpretation of this
issue, perhaps based on one or both of the interpretations given.

**Suggested Interpretation #1**:

Clause 3 **Definitions and conventions** states in the very beginning: “In this
International Standard, ‘shall' is to be interpreted as a requirement on an
implementation or on a program; conversely, ‘shall not' is to be interpreted as
a prohibition.”

Therefore *every* “shall” is viewed as testable. The question is what happens if
a “shall” is violated.

Subclause 5.1.1.3 **Diagnostics** provides the answer: “A conforming
implementation shall produce at least one diagnostic message (identified in an
implementation-defined manner) for every translation unit that contains a
violation of *any syntax rule* or *constraint.* Diagnostic messages *need not
be* produced in other circumstances.” (emphasis added)

Therefore every violation of a “shall” should be treated as a failure to meet
the requirements of the C Standard (first definition). Any violation of syntax
rules, semantic rules, or sections labeled as **Constraints** should therefore
generate a diagnostic.

According to this interpretation, a diagnostic should be produced for the
example given above.

**Suggested Interpretation #2**:

Subclause 5.1.1.3 states that diagnostics must be produced “for every
translation unit that contains a violation of any syntax rule or constraint.
Diagnostic messages need not be produced in other circumstances.”

*Syntax rules* are those items listed in the **Syntax** sections of the
standard. *Constraints* are those items listed in the **Constraints** sections
of the standard.

The C Standard specifies in clause 3, page 3, lines 12-13 that when the words
“shall” or “shall not” appearing outside of a constraint are violated, the
behavior is undefined.

For undefined behavior, the C Standard specifies in clause 3, page 3, lines 6-7
that the standard “imposes no requirements.” Thus a conformance suite should not
test for the words “shall” or “shall not” outside of a **Constraints** section,
since the standard imposes no requirements.

According to this interpretation, the C Standard imposes no requirements on a
conforming implementation for the program fragment above. A conforming
implementation could choose to accept this program (see also Footnote 6 to
subclause 5.1.1.3 on page 6), it could issue a diagnostic, or have any other
behavior.

---

Comment from WG14 on 1997-09-23:

### Response

Concerning a violation of subclause 6.5.2.1, **Semantics**, page 60, line 30: No
diagnostic is required; this is undefined behavior. It is not a violation of a
constraint or syntax.

Concerning a violation of clause 3, page 2, lines 2-3, No diagnostic is
required.

Suggested Interpretation #2 is the correct one.

Conformance to FIPS is beyond the scope of WG14. We can't comment on this.


</div>


---

---

<div id="issue0034.01">

## Issue 0034.01: Does size information evaporate when a declaration goes out of scope, even for objects with external linkage?

Authors: Stephen D. Clamage, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-038  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0011.01](log_c90.md#issue0011.01)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_034.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_034.html)

In *The C Users Journal,* Vol. 8 No. 7, July 1990, P.J. Plauger gives the
following example on page 10:

```c
extern int a[];
 int f() {
 extern int a[10];
 ...
 }
 int sizea = sizeof a; /* error */
```

Mr. Plauger claims that the size information from the inner scope “evaporates”
when its scope ends, and the operand to the `sizeof` operator has an incomplete
type. We cannot find unequivocal support for this claim in the standard.

Subclause 6.1.2.2 says on page 21, lines 10-11:

> ... each instance of a particular identifier with *external linkage* denotes the
> same object or function.

Combining subclause 6.1.2.6 and subclause 6.5.4.2, we find that the two
declarations for `a` are compatible and we may construct a composite type. The
composite type is array of 10 `int`.

Subclause 6.1.2.6 on page 25, lines 19-20, discusses the case of two
declarations in the same scope, but does not discuss the case of two
declarations for the same object in different scopes.

But subclause 6.1.2.5 says on page 24, lines 8-9:

> An array type of unknown size is an incomplete type. It is completed, for an
> identifier of that type, by specifying the size in a later declaration (with
> internal or external linkage).

The identifier `a` appears in two declarations, and denotes the same object. The
second declaration completes the type for the identifier in the inner scope. The
two identifiers denote the same object, so it would seem reasonable to say the
type of that object is completed.

Is the size information in the inner scope lost upon leaving the scope?

---

Comment from WG14 on 1997-09-23:

### Response

Is the size information in the inner scope lost upon leaving the scope?

Answer: Yes.

See the correction in response to [Defect Report #011](log_c90.md#issue0011.01).


</div>


---

---

<div id="issue0034.02">

## Issue 0034.02: If so, can one then write conflicting declarations in disjoint scopes?

Authors: Stephen D. Clamage, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-038  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_034.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_034.html)

If no size information is known in the outer scope, then consider the following
example:

```c
extern int a[];
 int f() {
 extern int a[10];
 ...
 }
 int g() {
 extern int a[20]; /* error? */
 ...
 }
```

Is this legal? If not, does it violate a constraint?

---

Comment from WG14 on 1997-09-23:

### Response

The example exhibits undefined behavior. It does not violate a constraint.
Subclause 6.1.2.2, page 21, lines 10-13 describe “same object;” subclause
6.1.2.6, page 25, lines 9-10 require that “All declarations that refer to the
same object or function shall have compatible type; otherwise, the behavior is
undefined.”


</div>


---

---

<div id="issue0035.01">

## Issue 0035.01: Can one declare an enumeration or struct tag as part of an old-style parameter declaration?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-039  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_035.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_035.html)

```c
void f(a, b)
 int a(enum b {x, y});
 int b;
 {
 }
```

Now this example is perverse because a prototype declaration is used to declare
the parameter of an old-style function declaration. But anyway ...

Is the declaration of the parameter `a` legal or a constraint error?

Now `a(...)` is a declarator.

Subclause 6.7.1 says on page 82, lines 7-8:

> ... each declaration in the declaration list shall have at least one declarator,
> and those declarators shall declare only identifiers from the identifier list.

The identifier list contains `a` and `b`.

The declarator for parameter `a` declares the identifiers `a`, `b`, `x`, and
`y`.

`b` is in the identifier list, so that is okay. But `x` and `y` are not.
Constraint error (methinks so)?

See subclause 6.1.2, page 19 for a definition of an identifier.

---

Comment from WG14 on 1997-09-23:

### Response

There is no constraint violation. The scopes of `b`, `x`, and `y` end at the
right-parenthesis at the end of the `enum`, so there is no violation. It is
difficult to *call* the function `f`, but there is no constraint violation. The
phrase “each declarator declares one identifier” in subclause 6.5.4 refers to
`a`, not to `b`, `x`, or `y`.

As an example, in the conforming definition:

```c
void f(a, b)
 int a(enum b{x, y});
 int b;
 {
 }
```

the scope of `b` (the enum tag), `x`, and `y` ends at the right-parenthesis at
the end of the enum (prototype scope).


</div>


---

---

<div id="issue0035.02">

## Issue 0035.02: If so, what is the scope of enumeration tags and constants declared in old-style parameter declarations?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-039  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_035.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_035.html)

Also consider:

```c
void g(c)
 enum m{q, r} c;
 {
 }
```

What is the scope of `m`, `q`, and `r`?

Subclause 6.1.2.1 says on page 20, lines 28-29 “... appears outside of any block
or list of parameters, the identifier has *file scope,* ...”

It says on page 20, lines 30-31 “... appears inside a block or within the list
of parameter declarations in a function definition, the identifier has *block
scope,* ...”

Now the above three identifiers appear outside of any block or list of
parameters but they are within the list of parameter declarations.

Who wins?

---

Comment from WG14 on 1997-09-23:

### Response

The scope of `m`, `q`, and `r` ends at the close-brace (block scope). The
operative wording is the more specific statement on page 20, lines 30-31 “...
appears inside a block or within the list of parameter declarations in a
function definition, the identifier has *block scope,* ...”

As an example, in the code fragment:

```c
void g(c)
 enum m{q, r} c;
 {
 }
```

the scope of `m`, `q`, and `r` ends at the closing brace of the function
definition (block scope).


</div>


---

---

<div id="issue0036">

## Issue 0036: May a floating-point constant be represented with more precision than implied by its type?

Authors: Fred Tydeman, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-040  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_036.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_036.html)

May floating-point constants be represented with more precision than implied by
its type? Consider the following code fragment:

```c
float f;
 double d;
 long double ld;
 ld = ld + 0.1; /* add a long double and a double */
 ld = ld + 1.0 / 10.0; /* expression with "same" value */
 d = f + 0.1f; /* "+" is allowed to be double precision */
```

In the above example, the decimal number `0.1`, when converted to binary, is a
non-terminating repeating binary number; so the more bits used to represent the
number, the closer it will be to its true value. Hence, if `double`s are 64 bits
and `long double`s are 80 bits, the `long double` will be more accurate. So in
essence, may `0.1` (a `double`) be represented with more precision, e.g. as
`0.1L` (a `long double`)?

Parts of the C Standard that may help answer the question follow.

Subclause 5.1.2.3 **Program execution**, page 7, line 36:

> In the abstract machine, all expressions are evaluated as specified by the
> semantics.

I believe that this is the “as if” rule that applies to this case.

Subclause 5.1.2.3 **Program execution**, page 8, lines 44-45:

> Alternatively, an operation involving only `int`s or `float`s may be executed
> using double-precision operations if neither range nor precision is lost
> thereby.

Clearly, `d = f + 0.1F` may be done using a double-precision add. But may `0.1f`
be represented as the `double 0.1`?

Subclause 6.1.3.1 **Floating constants**, page 26, lines 32-35:

> If the scaled value is in the range of representable values (for its type) the
> result is either the nearest representable value, or the larger or smaller
> representable value immediately adjacent to the nearest representable value,
> chosen in an implementation-defined manner.

I believe that the above does not require that the result be the nearest
representable value (for its type).

Subclause 6.2.1.5 **Usual arithmetic conversions**, page 35, lines 38-39:

> The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby.

I believe that a floating constant is a floating operand, so is allowed greater
precision. Clearly, the expression `1.0 / 10.0` is allowed greater precision
than just `double`, so it would make sense to allow an equivalent constant
(`0.1`) to have greater precision.

Subclause 6.4 **Constant expressions**, page 55, lines 14-16:

> If a floating expression is evaluated in the translation environment, the
> arithmetic precision and range shall be at least as great as if the expression
> were being evaluated in the execution environment.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee concurs with all the arguments presented \- a floating constant
may be represented in more precision than implied by its type.


</div>


---

---

<div id="issue0037">

## Issue 0037: Can UNICODE or ISO 10646 be used as a multibyte code?

Authors: Isai Scheinberg, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-043  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_037.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_037.html)

Subclause 5.2.1.2 **Multibyte characters** states:

> The source character set may contain multibyte characters, used to represent
> members of the extended character set. The execution character set may also
> contain multibyte characters, which need not have the same encoding as for the
> source character set. For both character sets, the following shall hold:
>
> \- The single-byte characters defined in 5.2.1 shall be present.

and, a bit later on:

> \- A byte with all bits zero shall not occur in the second or subsequent bytes
> of a multibyte character.

My interpretation (and all of the experts that I consulted with) of the first
rule, is that the basic character set (A-z, 0-9, etc.) shall be coded in
one-byte code. All multibyte locales that I know (EUC variants, SJIS) follow
this rule. But I may still be wrong.

If the above is true, then both 10646 (other than CM 5\) and UNICODE fail this
rule and cannot be used as multibyte characters. UNICODE also fails the second
rule.

---

Comment from WG14 on 1997-09-23:

### Response

The following answers apply (almost) equally to ISO 10646-1 and UNICODE. They
are expressed in terms of ISO 10646-1.

Clause 3, page 2, lines 18-24 and 40-42 define “byte,” “character,” and
“multibyte character” as follows:

**byte**: The unit of data storage large enough to hold any member of the basic
character set of the execution environment.

**character**: A bit representation that fits in a byte. The representation of
each member of the basic character set in both the source and execution
environments shall fit in a byte.

**multibyte character**: A sequence of one or more bytes representing a member
of the extended character set of either the source or the execution environment.
The extended character set is a superset of the basic character set.”

Therefore, if ISO 10646-1 were used as a basic character set, then by definition
a byte would have to be large enough to hold each member of the ISO 10646-1
character set. Also by definition this would make ISO 10646-1 a valid multibyte
character set.

If a byte were only eight bits long, the following answer would hold. ISO
10646-1 represents, in a particular byte order, the character `'a'` for example
as follows.

```c
0 0 0 97
 ---- 16-bit version
 -------- 32-bit version
```

This fails subclause 5.2.1.2, page 11, lines 30-32:

\- A byte with all bits zero shall be interpreted as a null character
independent of shift state.

\- A byte with all bits zero shall not occur in the second or subsequent bytes
of a multibyte character.

Therefore, 8-bit bytes preclude the use of ISO 10646-1 as a multibyte character
set.


</div>


---

---

<div id="issue0038">

## Issue 0038: What happens when macro replacement creates adjacent tokens that can be taken as a single token?

Authors: Kuo-Wei Lee, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-046  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_038.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_038.html)

Under subclause 6.8.3.1 **Argument substitution**, the C Standard states on page
90, lines 12-14:

> Before being substituted, each argument's preprocessing tokens are completely
> macro replaced as if they form the rest of the translation unit; no other
> preprocessing tokens are available.

It is not clear to us what should happen if, after the first replacement, the
argument is a valid preprocessing number. Consider the following example:

```c
#define X 0x000E
 #define Y 0x0100
 #define FOO(a) a
 FOO(X+Y)
```

After `X` is replaced, `FOO(X+Y)` becomes `FOO(0x000E+Y)`. At this point, should
the macro replacement continue and expand `Y` to be 0x0100 with the final result
being `FOO(0x000E+0x0100)`; or should the expansion stop since `0x000E+Y` is a
syntactically valid preprocessing number?

In other words, should `FOO(X+Y)` be expanded into `FOO(0x000E+0x0100)`, or
should it be `FOO(0x000E+Y)`?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 5.1.1.2, page 5, lines 32-39 indicate that translation must proceed as
if all creation of preprocessing tokens completes before any macro expansion
begins. These are translation phases 3 and 4:

> 3\. The source file is decomposed into preprocessing tokens and sequences of
> white-space characters (including comments)...
>
> 4\. Preprocessing directives are executed and macro invocations are expanded.

Therefore, if `X+Y` were expanded to `0x000E+Y`, a new preprocessing number
would not be created. The macro expansion proceeds as follows.

```c
FOO(X+Y) (6 tokens) --
 FOO(0x000E+0x0100) (6 tokens) --
 0x000E+0x0100 (3 tokens)
```

This sequence is required by subclause 6.8.3.1, page 90, lines 10-14:

> A parameter in the replacement list ... is replaced by the corresponding
> argument after all macros contained therein have been expanded. Before being
> substituted, each argument's preprocessing tokens are completely macro replaced
> as if they formed the rest of the translation unit...


</div>


---

---

<div id="issue0039.01">

## Issue 0039.01: Must `MB_CUR_MAX` be one in the `"C"` locale?

Authors: Vania Joloboff, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-061  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_039.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_039.html)

My interpretation of the Standard is that the value of `MB_CUR_MAX` must be one
in the `"C"` locale. I infer that from the fact that:

1. The characters in the `"C"` locale must be alphanumeric \+ space.
2. The `is`*`XXX`* functions specify character constant values for the `"C"` locale.
3. A character constant consists of one or more characters that are enclosed within apostrophes. A character is regarded as having type `char`.
4. The data type `char` consists of one byte of storage.

However this clarification should be made explicit.

---

Comment from WG14 on 1997-09-23:

### Response

In fact 3, we presume the second sentence was intended to be: “A character
*constant* is regarded as having type `char`,” in order to be applicable to this
request. That is not true; a character constant is of type `int`. Also facts 1-4
deal with the single-byte chars and not the extended character set.

In any case, the facts as listed do not logically lead to the conclusion that
`MB_CUR_MAX` must be one (1) in the `"C"` locale. In fact, this conclusion is
not true. It is possible for `MB_CUR_MAX` to be greater than one in the `"C"`
locale. In subclause 7.10, page 149, `MB_CUR_MAX` is “the maximum number of
bytes in a multibyte character for the extended character set specified by the
current locale.” In subclause 7.4.1.1, page 107, the `"C"` locale is “the
minimal environment for C translation.” The minimal environment may still
require more than one byte for multibyte characters.


</div>


---

---

<div id="issue0039.02">

## Issue 0039.02: Should `setlocale(LC_ALL, NULL)` return `"C"` in the `"C"` locale?

Authors: Vania Joloboff, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-061  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_039.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_039.html)

I also would like to make a requirement that if the current locale is the `"C"`
locale, the value returned by `setlocale(LC_ALL, NULL)` be a string of length
one, consisting of the single character `C`.

Currently the value of `setlocale(LC_ALL, NULL)` is unspecified for the `"C"`
locale.

This makes it difficult to build libraries where you want to maintain the
behavior pre-existing to internationalization for backward compatibility.

Typically you want to say in these programs:

```c
if (*setlocale(LC_ALL, NULL) == 'C')
 do the old thing
 else
 do the new thing
```

---

Comment from WG14 on 1997-09-23:

### Response

The reference is to subclause 7.4.1.1, page 107\.

The Committee acknowledges that there exists no strictly portable method for
determining whether the current locale is the `"C"` locale. The request for this
feature is neither an erratum nor a request for interpretation; it is a request
for an amendment. The Committee will consider this request for a future revision
of the C Standard.


</div>


---

---

<div id="issue0040.01">

## Issue 0040.01: What is the composite type of `f(int)` and `f(const int)`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0013.01](log_c90.md#issue0013.01)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Composite type

Rule for function parameter compatibility, subclause 6.7,1, page 82, lines
24-25:

```c
void f(const int);
 void f(int a)
 {
 a = 4;
 }
```

In the above case what is the composite type of `f`? The legality of the
assignment to `a` depends on the answer.

```c
int f(int a[4]);
 int f(int a[5]);
```

The parameters are compatible because they are converted to *pointer to* ...,
but what is the composite type?

---

Comment from WG14 on 1997-09-23:

### Response

```c
void f(const int);
 void f(int a)
 {
 a = 4;
 }
```

What is the composite type of `f`?

Answer: `void f(int)`. [Defect Report #013, Question 1](log_c90.md#issue0013.01) describes
the correct manner for constructing the composite type.

Is the assignment valid?

Answer: Yes. The type of a parameter is independent of the composite type of the
function, so the assignment is valid (cf. subclause 6.7.1).

Another example:

```c
int f(int a[4]);
 int f(int a[5]);
```

The parameters are compatible because they are converted to *pointer to ...*,
but what is the composite type?

Answer: The response to the Defect Report mentioned above answers this question
as well.


</div>


---

---

<div id="issue0040.02">

## Issue 0040.02: Is an implementation that fails to equal the value of an environmental limit conforming?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Is an implementation that fails to equal (or exceed) the value of an
environmental limit conforming? Subclause 5.2.4 says that those in that
subclause must be equalled in a conforming implementation. There is no such
wording for the environmental limits in the Library (subclauses 7.9.2, 7.9.3,
7.9.4.4, 7.9.6.1, 7.10.2.1).

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause G.2, page 203:***

\- A call to a library function exceeds an **environmental limit** (7.9.2,
7.9.3, 7.9.4.4, 7.9.6.1, 7.10.2.1).


</div>


---

---

<div id="issue0040.03">

## Issue 0040.03: Is an **Environmental Constraint** a constraint?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Is an “environmental constraint” a constraint?

In subclause 7.6.1.1, page 118, lines 22-30, we have a set of environmental
constraints on where `setjmp` may occur.

Does violating these rules require a constraint error to be flagged, or is it
undefined behavior?

Some examples:

```c
i = setjmp(a);
 if (setjmp(a) == i)
 ...
```

---

Comment from WG14 on 1997-09-23:

### Response

Must an implementation diagnose violations of environmental constraints?

Answer: Diagnostics are not required for constraint violations in clause 7,
since subclause 5.1.1.3 refers to a constraint as defined in clause 3, which
applies to language elements only.


</div>


---

---

<div id="issue0040.04">

## Issue 0040.04: Should the response to [Defect Report #017, Q39](log_c90.md#issue0017.39) be reconsidered?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Cross-references: [0017.39](log_c90.md#issue0017.39)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

For the fragment

```c
if (a**b||c++d)
 ;
```

[Defect Report #017 Question 39](log_c90.md#issue0017.39) states that this is lexed as:

a. {`if`} {`(`} {`a`} {`<<`} {`b`} {`||`} {`c`} {`>>`} {`d`} {`)`}

not as:

b. {`if`} {`(`} {`a`} {`**b||c++`} {`d`} {`)`}

The rationale for this interpretation was that the constraint in subclause
6.1.7, page 32, lines 33-34 disallowed a header name preprocessing token
anywhere except within a `#include`. Since the header name preprocessing token
could not exist it was not lexed as such.

It was pointed out that the “longest possible token” rule was not influenced by
rules elsewhere in the C Standard, i.e. `i+++++j` is lexed as:

c. {`i`} {`++`} {`++`} {`+`} {`j`}

not as:

d. {`i`} {`++`} {`+`} {`++`} {`j`}

Now (c) is a constraint violation by subclause 6.3.2.4, page 42, lines 38-39,
the operand of the second `++` is not a modifiable lvalue. But this constraint
does not require that the input be re-lexed to form the preprocessing tokens
given in (d), which is conforming code.

As the UK C Panel saw it, the first example should be lexed as given in (b) and
a diagnostic issued. Having violated a constraint, we are now into undefined
behavior. An implementation could define the behavior in this circumstance to be
a re-lex of the input to produce the preprocessing tokens given in (a).

As far as the user was concerned, they would get the expected behavior with the
added value of a diagnostic being issued.

All those present felt that the interpretation was incorrect and recommended
that the UK ask the Committee to reconsider its decision.

To summarize, there is no ambiguity in the C Standard and the original X3J11
interpretation is incorrect.

---

Comment from WG14 on 1997-09-23:

### Response

Is a diagnostic required for an input such as

```c
if (a**b||c++d)
```

because of a violation of the constraint specified in subclause 6.1.7, page 32,
lines 33-34?

Answer: No. Our response to [Defect Report #017 Question 39](log_c90.md#issue0017.39)
addresses this issue.


</div>


---

---

<div id="issue0040.05">

## Issue 0040.05: Can a conforming implementation accept `long long`?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

In the constraint for subclause 6.5.2, page 59, lines 2-4: What does the C
Standard mean when it says “set?”

Does it mean that the construct:

```c
int int i;
```

violates a constraint?

It has been suggested that this wording was left vague to allow such constructs
as `long long` (which is supported by some compilers) to fall into the undefined
behavior category.

Would the Committee clarify the situation with regard to duplicate type
specifiers? Do such constructs result in a constraint error or undefined
behavior?

The related case `static static` is explicitly ruled out by the constraints in
the previous subclause.

Additionally, `volatile volatile` is ruled out by the constraint in subclause
6.5.3.

---

Comment from WG14 on 1997-09-23:

### Response

Example:

```c
int int i;
```

Must this be diagnosed?

Answer: Yes. It is allowed to rearrange the order of type specifiers within a
set, but not to duplicate them (cf. subclause 6.5.2). Thus `int int` is a
constraint violation.


</div>


---

---

<div id="issue0040.06">

## Issue 0040.06: Can one use `offsetof(struct t1, mbr)` before `struct t1` is completely defined?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Cross-references: [0097](log_c90.md#issue0097)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

The definition of the `offsetof` macro in subclause 7.1.6 does not cover all its
possible occurrences:

a. There are no restrictions on the structure being a completed type.

```c
struct t1 {
 char c;
 short s;
 int i[offsetof(struct t1, s)];
 }
```

When discussing the use of incomplete types, recourse usually has to be made to
the rules relating to where an object of unknown size may appear.

Would the Committee agree that there are not any rules prohibiting the above
construction?

b. In this structure we are asked to find the offset of a field that has not yet
been encountered:

```c
struct t2 {
 char c;
 union {
 int i[offsetof(struct t2, s)];
 short s;
 } u;
 };
```

Would the Committee agree that there do not appear to be any rules that make
this construct illegal?

c. The following structure has infinitely many “solutions:”

```c
struct t3 {
 char a[offsetof(struct t3, i)];
 int i;
 }
```

since `char` has size 1, any size of array will be the same as the `offsetof`
the field `i`.

d. The following structure has no “solutions:”

```c
struct t4 {
 int a[offsetof(struct t3, i)];
 int i;
 }
```

`int` is always larger than 1\.

---

Comment from WG14 on 1997-09-23:

### Response

a. Example:

> ```c
> struct t1 {
>  char c;
>  short s;
>  int i[offsetof(struct t1, s)];
>  };
> ```

This is *not* a valid use of the `offsetof` macro. The hypothetical `static`
*`type`* `t;` declaration required for `offsetof` (cf. subclause 7.1.6) could
not have validly appeared prior to the invocation of `offsetof` because the type
`struct t1` is incomplete (cf. subclause 6.7.2); therefore the `offsetof`
invocation is not strictly conforming.

b. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.

c. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.

d. The answer is the same as (a) above. In addition, the members mentioned in
these invocations are not in scope.


</div>


---

---

<div id="issue0040.07">

## Issue 0040.07: Can `sizeof` be applied to earlier parameter names in a prototype, or to earlier fields in a struct?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

`sizeof` various identifiers (subclause 7.1.6)

a)

```c
void f(int c, char a[sizeof(c)]);
```

b)

```c
int i;
 struct {
 int i;
 char a[sizeof(i)];
 };
```

Now the argument to `sizeof` must be an expression or a type.

In (a) is `c` an expression? I think not because:

expression -\> object -\> has storage in execution environment

and `c` does not have storage allocated to it. So (a) violates a semantic
“shall” and is undefined behavior.

Now in (b) the field `i` is obviously not an expression. But is it visible? Like
the outer `i`, it has file scope. However, it is in a different namespace. There
are no rules for namespace resolution in the `sizeof` subclause.

So is (b) legal or undefined behavior?

---

Comment from WG14 on 1997-09-23:

### Response

a. Example:

```c
void f(int c, char a[sizeof(c)]);
```

The reference to `c` is an expression because the previously declared identifier
designates a function parameter (cf. subclause 6.5.4.3), which is an object
(subclause 3.15), thus meeting the requirement in subclause 6.3.1.

b. Another example:

```c
int i;
 struct {
 int i;
 char a[sizeof(i)];
 };
```

In C, this is okay. Subclause 6.1.2.3, **Name spaces of identifiers**, requires
that `i` in the `sizeof` expression refers to the external `i`, not the member.


</div>


---

---

<div id="issue0040.08">

## Issue 0040.08: What arithmetic can be performed on a `char` holding a defined character literal value?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

Refer to subclause 6.1.2.5, page 22, lines 32-36:

a.

```c
char c = 7; /* implementation defined behavior, since 7 need not
 be a member of the basic execution character set */
```

b.

```c
c = 'a'; /* ok */
 c++; /* implementation defined */
```

c.

```c
c = '1'; /* ok */
 c++; /* ok? */
```

It has been suggested that the above constructs are not implementation defined.

Subclause 6.1.3.4, page 29, lines 30-33:

d.

```c
c = '\07'; /* what is in the source/execution character set is
 given in subclause 5.2.1. Anything else is an extension. */
```

e.

```c
c = '$';
```

It has been suggested that characters may be added to the basic source/execution
character set without implementation defined behavior being invoked. (I guess my
position on this item can be deduced from the text.)

---

Comment from WG14 on 1997-09-23:

### Response

a. Subclause 6.1.2.5 says “An object declared as type `char` is large enough to
store any member of the basic execution character set... If other quantities are
stored in a `char` object, the behavior is implementation-defined: the values
are treated as either signed or nonnegative integers.” Consider this example:

```c
char c = 7;
```

The assignment `c = 7` is not implementation-defined because, from a reasonable
reading of subclause 6.1.2.5, it is clear that the only implementation-defined
behavior here is the signedness of the value of the `char` object.

b. Another example:

```c
c = 'a';
 c++;
```

The increment of `c` after assigning an `'a'` to it is defined by the
implementation because the numeric encoding of `'a'` is defined by the
implementation. If `'a'` were equal to `CHAR_MAX`, the increment could even
cause an overflow (cf. subclause 5.2.1).

c. Another example:

```c
c = '1';
 c++;
```

The increment of `c` after assigning a `'1'` to it is not implementation-defined
because the characters `'0'` through `'9'` are required to be a contiguous range
(cf. subclause 5.2.1). Thus, the result is `'2'`.

d. Another example:

```c
c = '\07';
```

The value of the character constant `'\07'` is defined by the C Standard (cf.
subclause 6.1.3.4, page 29, line 10-13). The implementation-defined behavior of
some escape sequences, described on page 29, lines 30-33, is clarified in the
example on page 30, lines 8-14.

e. Another example:

```c
c = '$';
```

If `$` is in the execution character set, the value of `'$'` is locale-specific
and so must be defined by the implementation (cf. subclause 5.2.1).


</div>


---

---

<div id="issue0040.09">

## Issue 0040.09: Should the response to [Defect Report #017, Q27](log_c90.md#issue0017.27) be reconsidered?

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-062  
Status: Closed  
Cross-references: [0017.27](log_c90.md#issue0017.27)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_040.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_040.html)

re: UK request for interpretation cai027 ( [Defect Report #017 Question
27](log_c90.md#issue0017.27))

X3J11 refs: 90-056, 90-083

It has been pointed out, and the UK C panel agreed at its last meeting, that the
request for interpretation was unnecessary. The C Standard was clear and
unambiguous as is.

To make matters worse, X3J11 appears to have given an interpretation that is the
opposite of what the C Standard says.

The UK would like to withdraw this request for interpretation and ask the
Committee to reconsider its position.

---

Comment from WG14 on 1997-09-23:

### Response

We reaffirm the previous interpretation.


</div>


---

---

<div id="issue0041">

## Issue 0041: Are `'A'` through `'Z'` always `isupper` in all locales?

Authors: Andrew Josey, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-076  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_041.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_041.html)

Does the description in subclause 7.3.1 imply that the characters defined in
subclause 5.2.1 are always classified as implied by subclause 5.2.1 regardless
of the locale specified?

In particular, do the characters `'a'` through `'z'` and `'A'` through `'Z'`
have to be classified as “lower case and “upper case,” respectively, in every
locale?

The specific lines needing interpretation are lines 20-21 in subclause 7.3.1.6,
page 103, and lines 16-17 in subclause 7.3.1.10, page 104\. The word “or” can be
interpreted to require a superset of the characters specified as lower/upper
case in subclause 5.2.1 or to allow an implementation-defined set of characters
(which might contain none of the subclause 5.2.1 designated lower/upper case
characters).

---

Comment from WG14 on 1997-09-23:

### Response

Does the description in subclause 7.3.1 imply that the characters defined in
subclause 5.2.1 are always classified as implied by subclause 5.2.1 regardless
of the locale specified?

Answer: By subclause 7.3.1.6 **The `islower` function** and subclause 7.3.1.10
**The `isupper` function** which refer to lower- and upper-case letters,
respectively, and by subclause 5.2.1: “basic source and basic execution
character sets shall have at least ... upper-case letters of the English
alphabet” (with example) ... “lower-case letters of the English alphabet” (with
example), and by subclause 5.2.1.2 “The single-byte characters defined in
subclause 5.2.1 shall be present,” which refers to multibyte characters,
therefore, yes, the characters defined in subclause 5.2.1 are always classified
as implied by subclause 5.2.1 regardless of the locale specified.

Do the characters `'a'` through `'z'`, and `'A'` through `'Z'`, have to be
classified as “lower case” and “upper case,” respectively, in every locale?

Answer: Yes, the characters `'a'` through `'z'`, and `'A'` through `'Z'`, have
to be classified as “lower case” and “upper case,” respectively, in every locale
(following the citations above).


</div>


---

---

<div id="issue0042.01">

## Issue 0042.01: Does `memcpy` define a (sub)object?

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Status: Closed  
Cross-references: [0054](log_c90.md#issue0054)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

The description of `memcpy` in subclause 7.11.2.1 says:

> ```c
> void *memcpy(void *s1, const void *s2, size_t n);
> ```
>
> The `memcpy` function copies `n` characters from the object pointed to by `s2`
> to the object pointed to by `s1`. If copying takes place between objects that
> overlap, the behavior is undefined.

The definition of the term *object* in subclause 3.14 is:

> **object** \- A region of data storage in the execution environment, the
> contents of which can represent values. Except for bit-fields, objects are
> composed of contiguous sequences of one or more bytes, the number, order, and
> encoding of which are either explicitly specified or implementation-defined.
> When referenced, an object may be interpreted as having a particular type...

Are the objects in the description of `memcpy` the largest objects into which
the arguments can be construed as pointing?

In particular, is the behavior of the call of `memcpy` in Example 1 defined:

```c
void f1(void) {
        extern char a[2][N];
        memcpy(a[1], a[0], N);
        }
```

because the arguments point into the disjoint array objects, `a[1]` and `a[0]`?
Or is the behavior undefined because the arguments both point into the same
array object, `a`?

---

Comment from WG14 on 1997-09-23:

### Response

From subclause 3.14, an object is “a region of data storage ... Except for
bit-fields, objects are composed of contiguous sequences of one or more bytes,
the number, order, and encoding of which are either explicitly specified or
implementation-defined ...” From subclause 7.11.1, “the header `<string.h>`
declares one type and several functions, and defines one macro useful for
manipulating arrays of character type and other objects treated as arrays of
character type.” “Various methods are used for determining the lengths of the
arrays...” From subclause 7.11.2.1, description of `memcpy`, “if copying takes
place between objects that overlap, the behavior is undefined.” Therefore, the
“objects” referred to by subclause 7.11.2.1 are exactly the regions of data
storage pointed to by the pointers and dynamically determined to be of `N` bytes
in length (i.e. treated as an array of `N` elements of character type).

a. So, no, the objects are not “the largest objects into which the arguments can
be construed as pointing.”

b. In Example 1, the call to `memcpy` has defined behavior.

c. The behavior is defined because the pointers point into different
(non-overlapping) objects.


</div>


---

---

<div id="issue0042.02">

## Issue 0042.02: If so, how big is the object defined by `memcpy`?

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

For the purposes of the description of `memcpy`, can a contiguous sequence of
elements within an array be regarded as an object in its own right? If so, are
the objects in the description of `memcpy` the smallest contiguous sequences of
bytes that can be construed as the objects into which the arguments point?

In Example 2:

```c
void f2(void) {
        extern char b[2*N];
        memcpy(b+N, b, N);
        }
```

can each of the first and last half of array `b` be regarded as an object in its
own right, so that the behavior of the call of `memcpy` is defined? (Although
they are not declared as separate objects, each half does seem to satisfy the
definition of object quoted above.) Or is the behavior undefined, since both
arguments point into the same array object `b`?

In Example 3:

```c
void f3(void) {
 	void *p = malloc(2*N);	/* Allocate an object. */
        {
 	char (*q)[N] = p;	/* The object pointed to by p may
 					   be interpreted as having type
 					   (char [2][N]) when referenced
 							through q. */
 	/* ... */
        memcpy(q[1], q[0], N);
        /* ... */
        }
        {
 	char *r = p;		/* The object pointed to by p may
 					   be interpreted as having type
 					   (char [2*N]) when referenced
 							through r. */
 	/* ... */
        memcpy(r+N, r, N);
 	/* ... */
        }
 }
```

the types of the objects are inferred from the pointers, and the underlying
storage is dynamically allocated. Is the behavior of each call of `memcpy`
defined?

Since the relationship between the values of the arguments presented to `memcpy`
is the same in all the above calls, it seems reasonable to expect that either
all these calls of `memcpy` give defined behavior, or none do. But which is it?

---

Comment from WG14 on 1997-09-23:

### Response

a. Yes, for `memcpy`, a contiguous sequence of elements within an array can be
regarded as an object in its own right.

b. The objects are not the smallest contiguous sequence of bytes that can be
construed; they are exactly the regions of data storage starting at the pointer
and of `N` bytes in length.

c. Yes, the non-overlapping halves of array `b` can be regarded as objects in
their own rights.

d. The behavior (in Example 2\) is defined.

e. The definition of object is independent of the *method* of storage
allocation. The array length is determined by “various methods.” So, yes, the
behavior of each call of `memcpy` is well-defined.

f. All of the calls of `memcpy` (in Example 3\) give defined behavior.


</div>


---

---

<div id="issue0042.03">

## Issue 0042.03: How big is a string object defined by the `str*` functions?

Authors: Tom MacDonald, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-001  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_042.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_042.html)

Similar questions arise for the other library string handling functions that
have undefined behavior when copying between overlapping objects. These include
`strcpy`, `strncpy`, `strcat`, `strncat`, `strxfrm`, `mbstowcs`, `wcstombs`,
`strftime`, `vsprintf`, `sscanf`, and `sprintf`. For these functions, however,
the number of bytes referenced through each pointer depends, at least in part,
upon the values stored in the bytes.

Consider a library function for which the number of bytes accessed or modified
is affected by the values of the bytes. Is the object associated with each of
its pointer arguments the smallest contiguous sequence of bytes actually
accessed or modified through that pointer?

In Example 4:

```c
void f4(void) {
        extern char b[2*N];
        strcpy(b+N, b);
        }
```

is the behavior defined if `N >> strlen(b)`?

In Example 5:

```c
void f5(void) {
        extern char c[2*N];
        strcat(c+N, c);
        }
```

is the behavior defined if both `N >> strlen(c)` and `N >> strlen(c) +
strlen(c+N)`?

---

Comment from WG14 on 1997-09-23:

### Response

Length is determined by “various methods.” For strings in which all elements are
accessed, length is inferred by null-byte termination. For `mbstowcs`,
`wcstombs`, `strftime`, `vsprintf`, `sscanf`, `sprintf` and all other similar
functions, it was the intent of the C Standard that the rules in subclause
7.11.1 be applicable by extension (i.e., the objects and lengths are similarly
dynamically determined). The behavior (in Examples 4 and 5\) is defined.


</div>


---

---

<div id="issue0043.01">

## Issue 0043.01: Can `NULL` be defined as `4-4`?

Authors: Robert Paul Corbett, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-004  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_043.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_043.html)

Defining `NULL`

Subclause 7.1.6 defines `NULL` to be a macro “which expands to an
implementation-defined null pointer constant.” Subclause 6.2.2.3 defines a null
pointer constant to be “an integral constant expression with the value 0, or
such an expression cast to type `void *`.” The expression `4-4` is an integral
constant expression with the value 0\. Therefore, Standard C appears to permit

`#define NULL 4 - 4` as one of the ways `NULL` can be defined in the standard
headers. By allowing such a definition, Standard C forces programmers to
parenthesize `NULL` in several contexts if they wish to ensure portability. For
example, when `NULL` is cast to a pointer type, `NULL` must be parenthesized in
the cast expression.

At least one book about Standard C suggests defining `NULL` as

`#define NULL (void *) 0` That definition leads to a subtler version of the
problem described above. Consider the expression `NULL[p]`, where `p` is an
array of pointers. The expression expands to `(void *)0[p]` which is equivalent
to `(void *)(p[0])`. I doubt many users would expect such a result.

Have I correctly understood Standard C's requirements regarding `NULL`? If not,
what are those requirements?

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.1.2, page 96 (before Forward references):***

Any definition of an object-like macro described in this clause shall expand to
code that is fully protected by parentheses where necessary, so that it groups
in an arbitrary expression as if it were a single identifier.


</div>


---

---

<div id="issue0043.02">

## Issue 0043.02: Can an identifier that starts with an underscore be defined as a macro in a source file that includes at least one standard header?

Authors: Robert Paul Corbett, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-004  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_043.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_043.html)

Subclause 7.1.3 implies that an identifier that begins with an underscore cannot
be defined as a macro name in any source file that includes at least one
standard header. Footnote 91 emphasizes this restriction. Nonetheless, there are
texts on Standard C that imply that such macro definitions are allowed.

The first paragraph of subclause 7.1.3 states that each header optionally
declares or defines identifiers which are always reserved either for any use or
for use as file scope identifiers. The second bullet item states, “All
identifiers that begin with an underscore are always reserved for use as
identifiers with file scope in both the ordinary identifier and tag name
spaces.” The final sentence states, “If the program declares or defines an
identifier with the same name as an identifier reserved in that context (other
than as allowed by 7.1.7), the behavior is undefined.” Taken together, these
statements imply that an identifier that starts with an underscore cannot be
defined as a macro in a source file that includes at least one of the standard
headers.

Can an identifier that starts with an underscore be defined as a macro in a
source file that includes at least one standard header?

---

Comment from WG14 on 1997-09-23:

### Response

No. See subclause 7.1.3 and Footnote 91\.


</div>


---

---

<div id="issue0044.01">

## Issue 0044.01: What does it mean to say that the type of `offsetof` is `size_t`?

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Status: Closed  
Cross-references: [0072](log_c90.md#issue0072)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Subclause 7.1.6, page 98, lines 24-30 describe the macro

```c
offsetof(type, member_designator)
```

“which expands to an integral constant expression that has type `size_t`, ...”

How is this statement to be interpreted? The expansion of the macro `offsetof`
is

a. an expression which can be evaluated during translation, the value of which
is in the range representable by a `size_t` type.

Or

b. an expression as (a) above, but further constrained to be an “integral
constant expression” as defined in subclause 6.4, page 55, lines 17-21.

---

Comment from WG14 on 1997-09-23:

### Response

Neither alternative (a) nor (b) in Question 1 fully captures the intent. What is
intended is exactly what is specified in the C Standard. A strictly conforming
program shall not produce output that varies depending upon details of
implementation of facilities defined by the standard headers. Hence, use of the
`offsetof` macro, in a context requiring an integer constant expression, per se
does not render a program not strictly conforming.

Further clarification provided by David Prosser:

Although the replacement for the `offsetof` macro must be an integral constant
expression, and must follow all the constraints appropriate to expressions, an
implementation is permitted to make use of its extensions to constant
expressions that behave like integral constant expressions. This is why the
sample replacement expressions for the `offsetof` macro in the Rationale are
valid candidates (for many implementations) but do not come under the strict
definition of integral constant expression that strictly conforming code must
follow. In particular, this is why the `offsetof` macro exists: there was
otherwise no portable means to compute such translation-time constants.
Therefore, of the two choices, (b) is the closest, but it is not the whole
story.


</div>


---

---

<div id="issue0044.02">

## Issue 0044.02: Must the expansion of a standard header be a strictly conforming program?

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Subclause 5.1.1.1, page 5, lines 11-20 define a “translation unit” to be
equivalent to the sequence of preprocessing tokens and white-space characters
which exists at the end of translation phase 4 (subclause 5.1.1.2). Later in
translation phases 5, 6, 7, these preprocessing tokens are converted to tokens
and syntactically and semantically analyzed and translated.

Therefore, must a conforming implementation provide strictly conforming
expansions of macros defined by the standard headers, such that any use of the
resulting preprocessing token sequence, and ultimately the token sequence,
beyond phase 4 does not alter the behavior of an otherwise strictly conforming
program? See also clause 4 **Compliance**, page 4, lines 24-26.

---

Comment from WG14 on 1997-09-23:

### Response

A conforming implementation need not provide strictly conforming expansion of
macros defined by the standard headers.


</div>


---

---

<div id="issue0044.03">

## Issue 0044.03: Does expanding `offsetof` result in a non-strictly conforming program?

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Assuming (b) is the correct interpretation of Question 1, if a particular
implementation expands `offsetof` into an expression which contains operands
and/or operators which result in a violation of the definition of “integral
constant expression” from subclause 6.4, page 55, lines 17-21, does this
situation constitute:

a. a constraint violation since the expansion presented for further translation
is not an “integer constant expression?”

or

b. undefined behavior since the definition of “integral constant expression”
appears in a “shall” requirement in the semantic description of subclause 6.4
**Constant expressions**?

---

Comment from WG14 on 1997-09-23:

### Response

The response to Question 1 makes this a moot question.


</div>


---

---

<div id="issue0044.04">

## Issue 0044.04: Can one use `offsetof` in a strictly conforming program?

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Assuming (b) is the correct interpretation of Question 3, if within a
translation unit at a point where an “integer constant expression” is required
to satisfy a language constraint \- such as to specify the size of a bit-field
member of a structure, the value of an enumeration constant, the size of an
array, or the value of a case constant \- does the use of the macro `offsetof`
constitute:

a. a constraint violation?

or

b. the use of undefined behavior, which renders the translation unit to be not
strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

The response to Question 1 makes this a moot question.


</div>


---

---

<div id="issue0044.05">

## Issue 0044.05: Is `offsetof` the only standard macro that renders a program not strictly conforming?

Authors: Steve M. Hoxey, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-010  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_044.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_044.html)

Revisiting (b) as the correct interpretation of Question 1, it seems the only
possibility for a definition of the macro `offsetof` constitutes use of an
identifier from the reserved name space to define a builtin which interrogates
the translator's symbol table in a fashion analogous to the `sizeof` operator.
Further, this builtin must appear syntactically as a keyword rather than an
identifier to avoid the constraint violation of subclause 6.4, page 55, line 9,
which invalidates the use of what appears to be a function call within that
which is otherwise required to be a constant expression.

Further, implementing an expansion for `offsetof` as described in the previous
paragraph would violate the implementation constraint outlined in Question 2
above, since the expansion would inject preprocessing tokens requiring
recognition of a keyword outside the scope of a strictly conforming program.

In any case, the implication is that the fragment:

```c
#include <stddef.h>
 static struct x {int field1, field2; } s;
 enum fields {F0, F1, F2 = offsetof(struct x,field2), F3 };
```

is either rendered not strictly conforming or the implementation is rendered a
nonconforming implementation.

Alternatively, if the answer to Question 2 above is no, then the following
questions are raised:

Since translation phases 1 through 4 may introduce into the translation unit
token sequences which are not strictly conforming, what mechanism exists, if
any, to determine whether such sequences originated from the program source?

How is one to interpret the meaning of “strictly conforming program” from clause
4, page 3, lines 38-40, given that subclause 5.1.1.1, page 5, lines 12-15 define
the translation unit to be “a source file together with all the headers and
source files included via the preprocessing directive `#include`, less any
source lines skipped by any of the conditional inclusion preprocessing
directives?”

It seems that any program which makes use of the macro `offsetof` in the context
of a constraint requirement mandating an “integer constant expression” will
require use of unspecified, undefined, or implementation-defined behavior.

As near as I can tell, `offsetof` is the only macro defined by the C Standard
which can alter the behavior of a strictly conforming program as a consequence
of its own definition.

---

Comment from WG14 on 1997-09-23:

### Response

The response to Question 1 addresses this issue.


</div>


---

---

<div id="issue0045">

## Issue 0045: Can one `freopen` an already closed file?

Authors: David J. Hendricksen, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-036  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_045.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_045.html)

Under subclause 7.9.5.4 **The `freopen` function**, the C Standard states on
page 130, lines 24-29:

> The `freopen` function opens the file whose name is the string pointed to by
> `filename` and associates the stream pointed to by `stream` with it. The `mode`
> argument is used just as in the `fopen` function.
>
> The `freopen` function first attempts to close any file that is associated with
> the specified stream. Failure to close the file successfully is ignored. The
> error and end-of-file indicators for the stream are cleared.

It is not clear whether the following situations have defined behavior:

1. Calling `freopen` where `stream` points to uninitialized storage. For example:

   ```c
           { FILE a, *b;
           b = freopen("c.d", "r", &a);
           }
   ```

   (It may not be possible to detect that the information contained within `a` is
   not valid when the close for `freopen` is attempted.)
2. Calling `freopen` where `stream` is associated with a previously closed file. (The storage pointed to by `stream` may have been deallocated.)

---

Comment from WG14 on 1997-09-23:

### Response

The behavior is undefined in both cases; case (2) is clear from subclause 7.9.3
**Files**, page 126, lines 24-27, “A file may be disassociated from a
controlling stream by *closing* the file... The value of a pointer to a `FILE`
object is indeterminate after the associated file is closed (including the
standard text streams).” Also subclause 7.9.3 **Files**, page 126, lines 2-3 and
lines 37-39, “A stream is associated with an external file... by *opening* a
file, ... At program startup, three text streams are predefined and need not be
opened explicitly...” Also subclause 7.9.5.3 **The `fopen` function**, and,
similarly, subclause 7.9.5.4 **The `freopen` function**: “The ... function opens
the file ... and associates a stream with it...” Thus when subclause 7.9.5.4
says “The `freopen` function ... associates the stream pointed to by `stream`
with it,” the intention is certainly that `stream` already points to a valid
stream. Extending this to case (1), we observe that `a` (or `&a`) might not
refer to a stream, since none has been “associated” by any means specified in
the C Standard.


</div>


---

---

<div id="issue0046">

## Issue 0046: May a typedef be redeclared as a parameter outside an old-style function parameter list?

Authors: Neal Weidenhofer, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-041  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_046.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_046.html)

In subclause 6.7.1, page 82, line 9, it says, “An identifier declared as a
typedef name shall not be redeclared as a parameter.”

The question I have is: Does that sentence stand by itself absolutely or is it
intended to be read in the context of the paragraph in which it appears?

The beginning of the paragraph says, “If the declarator includes an identifier
list, ...” Function declarators including a parameter type list are dealt with
in the preceding paragraph which says nothing about typedef names.

In other words, is the following valid Standard C?

```c
typedef int foo;
 int bar(int foo) {return foo; }
```

---

Comment from WG14 on 1997-09-23:

### Response

The sentence is a part of the paragraph in which it appears. An identifier
declared as a typedef name may be redeclared as a parameter in a parameter type
list. The example is strictly conforming.


</div>


---

---

<div id="issue0047">

## Issue 0047: Can an array parameter have elements of incomplete type?

Authors: Randall Meyers, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-040  
Status: Closed  
Cross-references: [0017.07](log_c90.md#issue0017.07), [0110](log_c90.md#issue0110)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_047.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_047.html)

Are the following declarations strictly conforming?

```c
/* 1 */  struct S;
 /* 2 */ struct S *f(struct S *p) {return p; }
 /* 3 */ struct S *g(struct S a[]) {return a; }
 /* 4 */ int *h(int a2[][]) {return *a2; }
 /* 5 */ extern struct S es1;
 /* 6 */ extern struct S es2[1];
```

The declaration of struct tag `S` introduces an incomplete type (subclause
6.5.2.3, page 62, lines 25-29) that may only be used when the size of the type
is not needed.

The function `f` therefore is a fairly common and non-controversial use of an
incomplete pointer type by a function. It is strictly conforming.

The function `g` is more interesting. A parameter of type array is adjusted to
pointer type (subclause 6.7.1, page 82, lines 23-26). (Note that is an
adjustment of the type of the parameter definition. It is not a conversion, as
is what happens when an argument of type array is passed to a function.) Thus,
the type of parameter `a` is pointer to struct `S`. This would seem to make the
function `g` the same case as function `f`. However, subclause 6.1.2.5, page 23,
lines 23-24 (also Footnote 17\) disallow array types from having an incomplete
element type (like struct `S`). This raises the question, is function `g`
strictly conforming because the type of `a` is really pointer, or is function
`g` not strictly conforming because `a` had an invalid array type before the
compiler in effect rewrote the declaration?

The function `h` is similar to function `g`. The type of `a2` after adjustment
is pointer to array of unknown size of `int`, which does not violate any rules.
However, before adjustment, the type of `a2` is illegal because it is an array
whose element type is array of unknown size, which is an incomplete type.

In previous Committee discussion that occurred concerning [Defect Report #017
Question 10](log_c90.md#issue0017.07), the Committee took the position that a declaration
like that of `es1` was strictly conforming, since the size of `es1` is not
needed for an external reference, and thus was similar to the cases described in
Footnote 63 in subclause 6.5.2.3 on page 62\.

The declaration of `es2` also does not require its size to be known. However, it
appears that the rule from subclause 6.1.2.5, page 23, lines 23-24 that
prohibits an incomplete array element type makes `es2` not strictly conforming.

---

Comment from WG14 on 1997-09-23:

### Response

First of all, no constraints are violated. Therefore, no diagnostics are
required.

Declarations 1, 2, and 5 are strictly conforming. Declarations 3, 4, and 6 are
not, and therefore cause undefined behavior.

The struct `S` is an incomplete type (subclause 6.5.2.3, page 62, lines 25-28).
Also, an array of unknown size is an incomplete type (subclause 6.5.4.2, page
67, lines 9-10). Therefore, arrays of either of the above are not strictly
conforming (subclause 6.1.2.5, page 23, lines 23-24). This makes declarations 3,
4, and 6 not strictly conforming. (But an implementation could get it right.)

As an aside, array parameters are adjusted to pointer type (subclause 6.7.1,
page 82, lines 23-24). However, there is nothing to suggest that a
not-strictly-conforming array type can magically be transformed into a strictly
conforming pointer parameter via this rule.

The types in question can be interpreted two different ways. (Array to pointer
conversion can happen as soon as possible or as late as possible.) Hence a
program that uses such a form has undefined behavior.


</div>


---

---

<div id="issue0048">

## Issue 0048: Is `abort` compatible with POSIX?

Authors: David F. Prosser, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-043  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_048.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_048.html)

This Defect Report requests a clarification regarding the valid interpretations
of the `abort` function, especially when the implementation must also match the
requirements of POSIX.1 (ISO/IEC 9945-1:1990).

The C Standard states (subclause 7.10.4.1, page 155):

> The `abort` function causes abnormal termination to occur, unless the signal
> `SIGABRT` is being caught and the signal handler does not return. Whether open
> output streams are flushed or open streams closed or temporary files removed is
> implementation-dependent. An implementation-defined form of the status
> *unsuccessful termination* is returned to the host environment by means of the
> function call `raise(SIGABRT)`.

and (subclause 7.10.4.3, page 156):

> The `exit` function causes normal program termination to occur.

and (subclause 7.10.4.1, page 101 \[Rationale]):

> The Committee vacillated over whether a call to `abort` should return if the
> signal `SIGABRT` is caught or ignored. To minimize astonishment, the final
> decision was that `abort` never returns.

The POSIX.1 Standard states (subclause 3.2, page 46):

> There are two kinds of process termination:
>
> (1) Normal termination occurs by a return from `main()` or when requested with
> the `exit()` or `_exit()` functions.
>
> (2) Abnormal termination occurs when requested by the `abort()` function or when
> some signals are received (see 3.3.1).
>
> The `exit()` and `abort()` functions shall be as described in the C Standard
> {2}. Both `exit()` and `abort()` shall terminate a process with the consequences
> specified in 3.2.2, except that the status made available to `wait()` or
> `waitpid()` by `abort()` shall be that of a process terminated by the `SIGABRT`
> signal.

and (subclause 8.2.3.12, page 161):

> The `exit()` function shall have the effect of `fclose()` ... as described
> above. The `abort()` function shall also have these effects if the call to
> `abort()` causes process termination, but shall have no effect on streams
> otherwise. The C Standard {2} specifies the conditions where `abort()` does or
> does not cause process termination. For the purposes of that specification, a
> signal that is blocked shall not be considered caught.

and (subclause B.8.2.3.12, page 291 \[Rationale]):

> POSIX.1 intends that processing related to the `abort()` function will occur
> unless “the signal `SIGABRT` is being caught, and the signal handler does not
> return,” as defined by the C Standard {2}. This processing includes at least the
> effect of `fclose()` on all open streams, and the default actions defined for
> `SIGABRT`.
>
> The `abort()` function will override blocking or ignoring the `SIGABRT` signal.
> Catching the signal is intended to provide the application writer with a
> portable means to abort processing, free from possible interference from any
> implementation-provided library functions.
>
> Note that the term “program termination” in the C Standard {2} is equivalent to
> “process termination” in POSIX.1.

The above quotes make it clear that the POSIX.1 Standard intends to have the
abort function implementation be roughly the following:

1. Inquire about `SIGABRT` handling.
2. If currently blocked, unblock `SIGABRT`.
3. If currently `SIG_IGN`, reset `SIGABRT` to `SIG_DFL`.
4. If currently `SIG_DFL`, flush all open output streams.
5. `raise(SIGABRT)`.
6. Reset `SIGABRT` to `SIG_DFL` (handler must have returned).
7. Go to step 5\.

As far as the C Standard is concerned, step 2 is outside its scope, so it can be
part of a valid implementation. (The effects cannot be noticed by a strictly
conforming program.) Step 4 is clearly permitted as well. It is step 3 and the
loop that are the key of this Defect Report. (Note that step 3 could have been
skipped above as it would be handled by the 5-6-7 loop, but I've left it
explicit for clarity.)

The special case in the C Standard regarding `SIGABRT` handlers that don't
return is intended to keep the implementation straightforward. (It is, in
general, difficult to determine whether a handler will return without calling
it!) The POSIX.1 Standard has understood the C Standard to require, in effect,
an implementation to force an uncaught `SIGABRT` to terminate the program. But,
is this actually the C Standard's intent? The Rationale quote can certainly be
taken to indicate that catching and ignoring `SIGABRT` are in the same category.

Does the C Standard either permit or require an implementation to reset an
ignored `SIGABRT` to `SIG_DFL`? Or, does the C Standard permit or require a call
similar to `exit(EXIT_FAILURE)`? Is the distinction between abnormal termination
and unsuccessful normal termination beyond the scope of the C Standard? (After
all, how can it be tested?) And, finally, can a portable application find any
utility in setting `SIGABRT` to `SIG_IGN`?

---

Comment from WG14 on 1997-09-23:

### Response

Does the C Standard either permit or require an implementation to reset an
ignored `SIGABRT` to `SIG_DFL`?

Answer: Yes, it permits it. There is no way to detect such a change in a
strictly conforming program.

Or, does the C Standard permit or require a call similar to
`exit(EXIT_FAILURE)`?

Answer: No. Abnormal termination does not allow calls to the `atexit`-registered
functions.

Does the C Standard? (After all, how can it be tested?)

Answer: No. See above.

And, finally, can a portable application find any utility in setting `SIGABRT`
to `SIG_IGN`?

Answer: Not within the context of `abort`.

We note that therefore there is no clash between Standard C and POSIX.1.


</div>


---

---

<div id="issue0049">

## Issue 0049: Can `strxfrm` produce a longer translation string?

Authors: David Metsky, Project Editor (P.J. Plauger)  
Date: 1993-01-10  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_049.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_049.html)

It has been suggested that, at least in the `"C"` locale, the transformed string
output from `strxfrm` will not contain more characters than the original string.
I believe that this suggestion is overly restrictive, and that the standard does
not impose such a restriction on implementations. I am requesting a
clarification from the appropriate standards committee(s). I hope that you will
agree with the following resolution:

> The C Standard does not impose a requirement upon the length of the transformed
> string output from `strxfrm`. (The returned value does indicate the necessary
> length.)

Here are some citations from the C Standard:

Subclause 7.4.1.1 **The `setlocale` function**:

> `LC_COLLATE` affects the behavior of the `strcoll` and `strxfrm` functions... A
> value of `"C"` for `locale` specifies the minimal environment for C
> translation... At program startup, the equivalent of

```c
setlocale(LC_ALL, "C");
```

> is executed.

Subclause 7.11.4.3 **The `strcoll` function**:

> The `strcoll` function compares the string pointed to by `s1` to the string
> pointed to by `s2`, both interpreted as appropriate to the `LC_COLLATE` category
> of the current locale.

Subclause 7.11.4.5 **The `strxfrm` function**:

> The transformation is such that if the `strcmp` function is applied to two
> transformed strings, it returns a value greater than, equal to, or less than
> zero, corresponding to the result of the `strcoll` function applied to the same
> two original strings... The `strxfrm` function returns the length of the
> transformed string (not including the terminating null character). If the value
> returned is `n` or more, the contents of the array pointed to by `s1` are
> indeterminate.

I haven't located any requirement that the `"C"` locale behavior of `strcoll`
must be identical to `strcmp`. Even if there were such a requirement, I haven't
located any requirement that the transformed string must not be longer than the
original string.

---

Comment from WG14 on 1997-09-23:

### Response

We support your resolution:

The C Standard does not impose a requirement upon the length of the transformed
string output from `strxfrm`, other than a limitation on the size of objects.
(The returned value does indicate the necessary length.)


</div>


---

---

<div id="issue0050">

## Issue 0050: Does a proper definition of `wchar_t` need to be in scope to write a wide-character literal?

Authors: C. Breeus, Project Editor (P.J. Plauger)  
Date: 1993-02-24  
Status: Closed  
Cross-references: [0017.07](log_c90.md#issue0017.07)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_050.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_050.html)

Subclause 6.1.3.4 says that the type of a wide character constant is `wchar_t`,
and subclause 6.1.4 says the type of a wide character string is array of
`wchar_t`.

Subclause 7.1.6 says the typedef name `wchar_t` must be defined in `<stddef.h>`.

Question: When a compiler sees a literal of the form `L'...'` or `L"..."` must
it not check that

1. The name `wchar_t` is visible at that place.
2. The name is a typedef name. It could be redefined in an inner scope.
3. It is a typedef for an integral type. Again, it could be redefined.

And then, take that integral type as the meaning of `wchar_t`. I suppose it
cannot just hope for the best and take a type that makes it feel good.

---

Comment from WG14 on 1997-09-23:

### Response

A similar issue was explained in response to [Defect Report #017
Question](log_c90.md#issue0017.07) 7, regarding `size_t`. The relevant citation here is
from subclause 6.1.3.4, page 29, lines 36-37:

> A wide character constant has type `wchar_t`, an integral type defined in the
> `<stddef.h>` header.

The intent of this sentence is to note that a wide character constant has an
integral type. That integral type is the same integral type used to define
`wchar_t` in the header `<stddef.h>`. The sentence imposes no requirement that
this particular definition of `wchar_t` be in scope wherever you write a wide
character constant. It certainly does not suggest that the translator should
honor any other definition of `wchar_t` that may be in scope, as the type for a
wide character constant.

Rather, the sentence suggests that the translator knows what integral type to
assign to a wide character constant. The implementation further knows to define
`wchar_t` within the header `<stddef.h>` as having that same integral type.
Thus, the program has a way of obtaining a name for this type, if it chooses \-
by including the header `<stddef.h>`. But it need not invoke that mechanism just
to assist the translator.

It is an unfortunate, but widespread, practice within the C Standard to use
abbreviated language for describing some types. Thus, subclause 6.1.4, page 31,
lines 5-6 say:

> for wide string literals, the array elements have type `wchar_t`, ...

instead of the more long winded (but clearer):

> for wide string literals, the array elements have the same type used to define
> `wchar_t` in the header `<stddef.h>`, ...

We feel the usage is sufficiently uniform that the meaning intended by the
Committee is sufficiently clear, even as we acknowledge that the words can be
(and have been) misread.

So to put the matter crassly, the translator *does* “just hope for the best and
take a type that makes it feel good,” as you conjectured.


</div>


---

---

<div id="issue0051">

## Issue 0051: Can one index beyond the declared end of an array if space is allocated for the extra elements?

Authors: Andrew R. Koenig, Project Editor (P.J. Plauger)  
Date: 1993-03-08  
Status: Closed  
Cross-references: [0072](log_c90.md#issue0072), [0178](log_c90.md#issue0178)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_051.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_051.html)

I'll give you the short form first. I can haul out lots of related material if
it becomes necessary, but perhaps the bare question is enough. Is the following
program strictly conforming?

```c
#include <stdlib.h>

 struct A {
        char x[1];
        };

 main()
        {
        struct A *p = (struct A *) malloc(sizeof(struct A) + 100);
 	p->x[5] = '?';		/* This is the key line */
        return 0;
        }
```

If I remember correctly from reading the C Standard, pointer arithmetic is
illegal if it results in an address outside the object to which the original
pointer refers. The question here is essentially whether the “object” is all the
memory returned by `malloc` or the single `char` denoted by `p->x[0]`.

I do not believe there is any language in the C Standard that clearly answers
this question. I understand that this particular programming technique is quite
common, but that is more likely to affect whether a program is “conforming” than
whether it is “strictly conforming.”

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.3.2.1 describes limitations on pointer arithmetic, in connection
with array subscripting. (See also subclause 6.3.6.) Basically, it permits an
implementation to tailor how it *represents pointers* to the size of the objects
they point at. Thus, the expression `p->x[5]` may fail to designate the expected
byte, even though the `malloc` call ensures that the byte is present. The idiom,
while common, is *not* strictly conforming.

A safer idiom is:

```c
#include <stdlib.h>
 #define HUGE_ARR	10000	/* largest desired array */

 struct A {
        char x[HUGE_ARR];
        };

 main()
        {
        struct A *p = (struct A *) malloc(sizeof(struct A)
 		- HUGE_ARR + 100);	/* want x[100] this time */
 	p->x[5] = '?';		/* now strictly conforming */
        return 0;
        }
```


</div>


---

---

<div id="issue0052.01">

## Issue 0052.01: Should the `mktime` example use `(time_t)-1` instead of `-1`?

Authors: Paul Edwards, Project Editor (P.J. Plauger)  
Date: 1993-03-21  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_052.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_052.html)

In subclause 7.12.2.3, page 172, the example is not strictly conforming. The
`mktime` return is compared against `-1` instead of `(time_t)-1`, which could
cause a problem with a strictly conforming implementation.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.12.2.3, page 172, line 16, change:***

> ```c
> if (mktime(&time_str) == -1)
> ```

***to:***

> ```c
> if (mktime(&time_str) == (time_t)-1)
> ```


</div>


---

---

<div id="issue0052.02">

## Issue 0052.02: Is the index entry for static correct?

Authors: Paul Edwards, Project Editor (P.J. Plauger)  
Date: 1993-03-21  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_052.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_052.html)

Index entry for `static` lists subclause 3.1.2.2 instead of subclause 6.1.2.2.

---

Comment from WG14 on 1997-09-23:

### Correction

***In the index, page 217, change:***

`static` storage-class specifier, 3.1.2.2, 6.1.2.4, **6.5.1**, 6.7

***to:***

`static` storage-class specifier, 6.1.2.2, 6.1.2.4, **6.5.1**, 6.7


</div>


---

---

<div id="issue0052.03">

## Issue 0052.03: Does the C Standard come with a Rationale, as indicated in Footnote 1?

Authors: Paul Edwards, Project Editor (P.J. Plauger)  
Date: 1993-03-21  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_052.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_052.html)

Footnote 1, page 1, says that the C Standard comes with a Rationale; it doesn't.

---

Comment from WG14 on 1997-09-23:

### Response

The footnote actually states, in part, “It is accompanied by a Rationale
document that explains ...” And indeed, the C Standard was accompanied by such a
document throughout its approval process. ISO, unfortunately, has elected not to
distribute the Rationale with the C Standard. “Accompanied by” does not promise
“comes with” when you buy the C Standard.


</div>


---

---

<div id="issue0053">

## Issue 0053: Do the aliasing rules cover accesses to different function pointers properly?

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-03-25  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0168](log_c90.md#issue0168)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_053.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_053.html)

There's been a discussion on `comp.std.c` recently about accessing a pointer to
a function with parameter type information through a pointer to a pointer to a
function without parameter type information. For example:

```c
int f(int);
        int (*fp1)(int);
        int (*fp2)();
        int (**fpp)();

        fp1 = f;
 	fp2 = fp1;	/* pointers to compatible types, assignment ok */
 	(*fp2)(3);	/* function types are compatible, call is ok */
 	fpp = &fp1;	/* pointer to compatible types, assignment ok */
 	(**fpp)(3);	/* valid? */
```

The final call itself should be valid since the resulting function type is
compatible with the type of the function being called, but there's still a
problem: Subclause 6.3 **Expressions**, page 38, says:

> An object shall have its stored value accessed only by an lvalue expression that
> has one of the following types:**36**
>
> \- the declared type of the object,
>
> \- a qualified version of the declared type of the object,
>
> \- a type that is the signed or unsigned type corresponding to the declared type
> of the object,
>
> \- a type that is the signed or unsigned type corresponding to a qualified
> version of the declared type of the object,
>
> \- an aggregate or union type that includes one of the aforementioned types
> among its members (including, recursively, a member of a subaggregate or
> contained union), or
>
> \- a character type.
>
> \[Footnote 36: The intent of this list is to specify those circumstances in
> which an object may or may not be aliased.]

This would appear to render the final call undefined since the stored value of
`fp1` is being accessed by an lvalue that does not match its declared type:
`(int (*)())` vs. `(int (*)(int))`.

I think that this example should be valid and that the above limitation is too
strict. I think what we meant to say was “*a type compatible with* the declared
type of the object,” which would allow “reasonable” type mismatches without
allowing aliasing between wildly different types.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3, page 38, lines 18-21, change:***

An object shall have its stored value accessed only by an lvalue expression that
has one of the following types:**36**

\- the declared type of the object,

\- a qualified version of the declared type of the object,

***to:***

An object shall have its stored value accessed only by an lvalue expression that
has one of the following types:**36**

\- a type compatible with the declared type of the object,

\- a qualified version of a type compatible with the declared type of the
object,


</div>


---

---

<div id="issue0054">

## Issue 0054: What is the behavior of various string functions with a specified length of zero?

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-04-01  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0042.01](log_c90.md#issue0042.01)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_054.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_054.html)

Are the string handling functions defined in subclause 7.11 that have an
explicit length specification (`memcpy`, `memmove`, `strncpy`, `strncat`,
`memcmp`, `strncmp`, `strxfrm`, `memchr`, and `memset`) well-defined when the
length is specified as zero?

Taking `memcpy` as an example, the description in subclause 7.11.2.1 states:

> The `memcpy` function copies `n` characters from the object pointed to by `s2`
> into the object pointed to by `s1`. If copying takes place between objects that
> overlap, the behavior is undefined.

The response to [Defect Report #042 Question 1](log_c90.md#issue0042.01) indicates that:

> ... the “objects” referred to by subclause 7.11.2.1 are exactly the regions of
> data storage pointed to by the pointers and dynamically determined to be of `N`
> bytes in length (i.e. treated as an array of `N` elements of character type).

Since, by definition, objects consist of at least one byte, this would imply
that `s1` and `s2` are not pointing to objects when `N` is zero and thus are
outside the domain of the function leading to undefined behavior.

I do not recall whether this was the Committee's intent or not, but it would
seem that some clarification is in order.

---

Comment from WG14 on 1997-09-23:

### Correction

***Add to subclause 7.11.1, page 162:***

Where an argument declared as `size_t n` specifies the length of the array for a
function, `n` can have the value zero on a call to that function. Unless
explicitly stated otherwise in the description of a particular function in this
subclause, pointer arguments on such a call must still have valid values, as
described in subclause 7.1.7. On such a call, a function that locates a
character finds no occurrence, a function that compares two character sequences
returns zero, and a function that copies characters copies zero characters.


</div>


---

---

<div id="issue0055">

## Issue 0055: Must the `SIG*` macros have distinct values?

Authors: Loren Schall, Project Editor (P.J. Plauger)  
Date: 1993-04-14  
Status: Fixed  
Fixed in: C90 TC1  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_055.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_055.html)

It has been suggested that the six macros `SIGABRT`, `SIGFPE`, `SIGILL`,
`SIGINT`, `SIGSEGV`, and `SIGTERM` must have distinct values. Here is the
relevant portion of subclause 7.7:

> “The macros defined are
>
> ```c
> SIG_DFL
>               SIG_ERR
>               SIG_IGN
> ```
>
> which expand to constant expressions with distinct values that have type
> compatible with the second argument to and the return value of the `signal`
> function, and whose value compares unequal to the address of any declarable
> function; and the following, each of which expands to a positive integral
> constant expression that is the signal number corresponding to the specified
> condition:
>
> ...
>
> An implementation need not generate any of these signals, except as a result of
> explicit calls to the `raise` function.”

On the one hand, the reference to “the signal number corresponding to the
specified condition” might be assumed to imply different numbers for each
signal. On the other hand, the words “distinct values” were explicitly used for
the three `SIG_*` macros and are conspicuously missing for the others.

Also, I think it's worth noting that the standard expects `raise` to work
meaningfully (i.e. to be able to tell them apart).

Summary: must `SIGABRT`, `SIGFPE`, `SIGILL`, `SIGINT`, `SIGSEGV`, and `SIGTERM`
have distinct values?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.7, page 120, lines 14-16, change:***

and the following, each of which expands to a positive integral constant
expression that is the signal number corresponding to the specified condition:

***to:***

and the following, which expand to positive integral constant expressions with
distinct values that are the signal numbers, each corresponding to the specified
condition:


</div>


---

---

<div id="issue0056">

## Issue 0056: How accurate must floating-point arithmetic be?

Authors: Thomas Plum, Project Editor (P.J. Plauger)  
Date: 1993-04-15  
Status: Closed  
Cross-references: [0063](log_c90.md#issue0063)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_056.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_056.html)

The following requirement is implied in several places, but not explicitly
stated. It should be explicitly affirmed, or alternative wording adopted.

The representation of floating-point values (such as floating-point constants,
the results of floating-point expressions, and floating-point values returned by
library functions) shall be accurate to one unit in the last position, as
defined in the implementation's `<float.h>` header.

Discussion: The values in `<float.h>` aren't required to document the underlying
bitwise representations. If you want to know how many bits, or bytes, a
floating-point values occupies, use `sizeof`. The `<float.h>` values document
the mathematical properties of the representation, the behaviors that the
programmer can count upon in analyzing algorithms.

It is a quality-of-implementation question as to whether the implementation
delivers accurate bits throughout the bitwise representation, or alternatively,
delivers considerably less accuracy. The point being clarified is that
`<float.h>` documents the delivered precision, not the theoretically possible
precision.

---

Comment from WG14 on 1997-09-23:

**Open Issue**


</div>


---

---

<div id="issue0057">

## Issue 0057: Must there exist a user-accessible integral type for every pointer?

Authors: Fred Tydeman, Project Editor (P.J. Plauger)  
Date: 1993-06-07  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_057.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_057.html)

Must there exist a user-accessible integral type for every pointer? If an
implementation provides 48-bit pointers, must there be an integral type, such as
`long` or `int`, that is at least 48 bits? Parts of the C Standard that may help
answer the question follow:

Subclause 6.3.4, **Cast operators**, page 45, lines 30-34 and Footnote 45:

> A pointer may be converted to an integral type. The size of integer required and
> the result are implementation-defined. If the space provided is not long enough,
> the behavior is undefined.
>
> An arbitrary integer may be converted to a pointer. The result is
> implementation-defined.**45** \[Footnote 45: The mapping functions for
> converting a pointer to an integer or an integer to a pointer are intended to be
> consistent with the addressing structure of the execution environment.]

---

Comment from WG14 on 1997-09-23:

### Response

Integral types and pointer types are incommensurate. An implementation need not
provide an integral type that can accept the conversion from a pointer type
without loss of information.


</div>


---

---

<div id="issue0058">

## Issue 0058: What is the number of digits in a number that can be processed by the `scanf` family and the `strtod` family?

Authors: Fred Tydeman, Project Editor (P.J. Plauger)  
Date: 1993-06-07  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_058.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_058.html)

What is the minimum value for the maximum number of digits in a number that can
be processed by the `scanf` family and the `strtod` family?

1. 509
2. 32767
3. something else

Parts of the the C Standard that may help answer the question follow. Subclause
7.9.6.1**The `fprintf` function**, page 134, lines 16-18:

> **Environmental limit**. The minimum value for the maximum number of characters
> produced by any single conversion shall be 509\.

But, note, there is no such environmental limit for `fscanf`.

Subclause 5.2.4.1 **Translation limits**, page 13, line 17:

> \- 509 characters in a logical source line

But, note, there is no execution limit. Subclause 5.2.4.1 **Translation
Limits**, page 13, line 19:

> \- 32767 bytes in an object (in a hosted environment only)

Consider the number 1.0 written as `.00000...00001e32759` that is 32767
characters long (including terminator). There is only one significant digit, the
`1`. It can be stored in an array of 32767 characters, so it should be possible
to pass this string to `atof`, `strtod`, or `sscanf` and get the value 1.0.
Correct?

---

Comment from WG14 on 1997-09-23:

### Response

You are correct; the C Standard imposes no execution limit on the maximum number
of digits in the subject sequence of `fscanf` conversion specifiers and the
`strto*` functions, other than on the size of objects.


</div>


---

---

<div id="issue0059">

## Issue 0059: Must an incomplete type be completed by the end of a translation unit?

Authors: Martin Ruckert, Project Editor (P.J. Plauger)  
Date: 1993-06-15  
Status: Closed  
Cross-references: [0139](log_c90.md#issue0139)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_059.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_059.html)

The ISO Standard for the programming language C explains the notion of
*incomplete type* in subclause 6.1.2.5 and subclause 6.5.2.3 (for structures).
Both sections do not explicitly require that an incomplete type eventually must
be completed, nor do they explicitly allow incomplete types to remain incomplete
for the whole compilation unit.

Since this feature is of importance for the declaration of true opaque data
types, it deserves clarification. I propose to add to the fourth paragraph on
page 24 (subclause 6.1.2.5) the sentence: “It is admissable that an incomplete
type remain incomplete in the whole compilation unit.”

The type `void` is already an incomplete type which is never completed.

The examples given in the standard document explain that incomplete types are
exclusively needed to define mutual referential structures. Opaque data types,
however, constitute a second use for this feature. Considering mutual
referential structures defined and implemented in different compilation units
makes the idea of an opaque data type a natural extension of an incomplete data
type.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard intentionally contains no prohibition against leaving a type
incomplete. (As you so aptly observe, `void` is an incomplete type that is never
completed.) There is no need to make a positive statement about the absence of a
prohibition.

Moreover, the examples were not intended to represent that mutual referencing
was the only reason for permitting incomplete structure types. Opaque data types
were considered, and endorsed, by the Committee when drafting the C Standard.


</div>


---

---

<div id="issue0060">

## Issue 0060: When an array of `char` (or `wchar_t`) is initialized with a string literal that contains fewer characters than the array, are the remaining elements of the array initialized?

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1993-07-19  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0092](log_c90.md#issue0092)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_060.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_060.html)

When an array of `char` (or `wchar_t`) is initialized with a string literal that
contains fewer characters than the array, are the remaining elements of the
array initialized?

Subclause 6.5.7 **Initialization**, page 72, only says (emphasis mine):

> If there are fewer initializers in a *brace-enclosed list* than there are
> members of an aggregate, the remainder of the aggregate shall be initialized
> implicitly the same as objects that have static storage duration.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.5.7, page 72, the penultimate paragraph of Semantics (before
Examples), add after the comma:***

or fewer characters in a string literal or wide string literal used to
initialize an array of known size, and elements of character or `wchar_t` type


</div>


---

---

<div id="issue0061">

## Issue 0061: Interpretation of white space in the format string of a scan statement

Authors: Ed Bendickson, X3 Secretariat (USA)  
Date: 1993-08-19  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_061.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_061.html)

I am requesting an interpretation of white space in the format string of a scan
statement. One of our customers is concerned about this as it appears to
conflict with some books on C. I am referring to subclause 7.9.6.2, page 135,
paragraph 3:

> A directive composed of white space character(s) is executed by reading input up
> to the first non-white-space character (which remains unread), or until no more
> characters can be read.

Page 135, paragraph 7 says:

> If the length of the input item is zero, the execution of the directive fails:
> this condition is a matching failure, unless an error prevented input from the
> stream, in which case it is an input failure.

My questions are:

1. Is white space in the format string a directive which must be satisfied by white space in the input string?
2. What are the correct answers to the following examples? Note the white space in the format string.

Example 1:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu %ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 1?

Example 2:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu%ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 2?

---

Comment from WG14 on 1997-09-23:

### Response

A directive composed of one or more white-space characters can successfully
match zero white-space characters in the input stream. The paragraphs that
intervene between your two quotations make clear that the second paragraph
applies only to a directive that is a conversion specification.

Thus, both examples should assign 2 to `numAssigned`.


</div>


---

---

<div id="issue0062">

## Issue 0062: Can the `rename` function alway return a failure?

Authors: David J. Hendricksen, X3 Secretariat (USA)  
Date: 1993-08-19  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_062.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_062.html)

If the only way to effectuate the renaming of a file on a given system is to
copy the contents of the file, does an implementation conform to the C Standard
by always returning a failure from the `rename` function? Footnote 113 would
seem to imply this.

---

Comment from WG14 on 1997-09-23:

### Response

Yes, subclause 7.9.4.2 permits the `rename` function to fail if it must copy the
file contents, among other reasons.


</div>


---

---

<div id="issue0063">

## Issue 0063: This is [Defect Report 056](log_c90.md#issue0056)

Authors: Thomas Plum, Project Editor (P.J. Plauger)  
Date: 1993-12-01  
Status: Closed  
Cross-references: [0056](log_c90.md#issue0056)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_063.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_063.html)

\[This is Defect Report #056, resubmitted for administrative reasons.]

The following requirement is implied in several places, but not explicitly
stated. It should be explicitly affirmed, or alternative wording adopted.

The representation of floating-point values (such as floating-point constants,
the results of floating-point expressions, and floating-point values returned by
library functions) shall be accurate to one unit in the last position, as
defined in the implementation's `<float.h>` header.

Discussion: The values in `<float.h>` aren't required to document the underlying
bitwise representations. If you want to know how many bits, or bytes, a
floating-point values occupies, use `sizeof`. The `<float.h>` values document
the mathematical properties of the representation, the behaviors that the
programmer can count upon in analyzing algorithms.

It is a quality-of-implementation question as to whether the implementation
delivers accurate bits throughout the bitwise representation, or alternatively,
delivers considerably less accuracy. The point being clarified is that
`<float.h>` documents the delivered precision, not the theoretically possible
precision.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard imposes no requirement on the accuracy of floating-point
arithmetic.

Further discussion:

The C Standard speaks directly to the matter of floating-point accuracy only in
one or two areas. Subclause 6.2.1.4 **Floating types**, page 35, says of
conversions from one floating type to one with less range and/or precision:

> If the value being converted is in the range of values that can be represented
> but cannot be represented exactly, the result is either the nearest higher or
> nearest lower value, chosen in an implementation-defined manner.

And in subclause 6.2.1.5 **Usual arithmetic conversions**, page 35:

> The values of floating operands and of the results of floating expressions may
> be represented in greater precision and range than that required by the type;
> the types are not changed thereby.

Otherwise, arithmetic for both integer and floating types is defined in terms of
the usual terminology of mathematics. Nothing in the C Standard suggests that
floating arithmetic is excused from the conventional rules of arithmetic.

Nevertheless, it is commonplace for the functions declared in `<math.h>` to
deliver results less accurate than the underlying representation can support. It
is not uncommon even for simple arithmetic expressions to do the same. And
still, implementations document in `<float.h>` properties of the underlying
*representation,* not the effective range and precision reliably delivered. The
C community has typically tolerated a certain laxity in this area.

Probably the most useful response would be to amend the C Standard by adding two
requirements on implementations:

Require that an implementation document the maximum errors it permits in
arithmetic operations and in evaluating math functions. These should be
expressed in terms of “units in the least-significant position” (ULP) or “lost
bits of precision.”

Establish an upper bound for these errors that all implementations must adhere
to.

The state of the art, as the Committee understands it, is:

correctly rounded results for arithmetic operations (no loss of precision)

1 ULP for functions such as `sqrt`, `sin`, and `cos` (loss of 1 bit of
precision)

4-6 ULP (loss of 2-3 bits of precision) for other math functions.

Since not all commercially viable machines and implementations meet these
exacting requirements, the C Standard should be somewhat more liberal.

The Committee would, however, suggest a requirement no more liberal than a loss
of 3 bits of precision, out of kindness to users. An implementation with worse
performance can always conform by providing a more conservative version of
`<float.h>`, even if that is not a desirable approach in the general case.

The Committee should revisit this issue during the revision of the C Standard.


</div>


---

---

<div id="issue0064">

## Issue 0064: What is a null pointer constant?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_064.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_064.html)

Item 1 \- Null pointer constants

Consider the following translation unit:

```c
char *f1 (int i, int *pi)
        {
        *pi = i;
        return 0;
        }

 char *f2 (int i, int *pi)
        {
        return (*pi = i, 0);
        }
```

In `f1`, the `0` is a null pointer constant (subclause 6.2.2.3). Since `return`
acts as if by assignment (subclause 6.6.6.4) the function is strictly
conforming.

In `f2`, the `0` is a null pointer constant. However, a constant expression
cannot contain a comma operator (subclause 6.4), and so the expression being
returned is not a null pointer constant per se. Which of the following is the
case?

1. The property of being a null pointer constant percolates upwards through an expression, and the function `f2` is strictly conforming.
2. The property of being a null pointer constant does not percolate upwards, and the expression being notionally assigned in the `return` statement, though of value zero, is not a null pointer constant but only of type `int`, thus violating a constraint (subclause 6.3.16.1).

---

Comment from WG14 on 1997-09-23:

### Response

Function `f2` is not strictly conforming, because it violates a constraint for
simple assignment (which applies to converting the type of the `return`
expression), because the `return` expression is not a null pointer constant.


</div>


---

---

<div id="issue0065">

## Issue 0065: Can strictly conforming programs contain locales other that the 'C' locale?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_065.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_065.html)

Item 2 \- locales

Consider the program:

```c
#include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 int main (void)
        {
        int i;
        char *loc [] = { "English", "En_UK", "Loglan", "" };

        for (i = 0; ; i++)
              if (setlocale (LC_ALL, loc [i]) != NULL)
 	           {
 	           /*
 			 *  We must eventually get here,
 			 *  because setlocale("") can't yield NULL.
 	            /*
 	           printf ("Decimal point = '%s'\n",
 	           localeconv ()->decimal_point);
 	           exit (0);
 	           }
        }
```

The valid locales are implementation-defined (subclause 7.4.1.1). Nevertheless,
the output produced depends only on the locale, not any other
implementation-defined behavior. Is the program strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

The Committee affirms that the intent of this wording is that a program such as
that above, whose output varies only according to the locale selected and does
not rely on the presence of a specific locale other than the `"C"` locale or
that selected by `""`, was always intended to be strictly conforming.
Nevertheless, it is agreed that the cited extract from subclause 7.4.1.1 could
be read strictly as making such programs depend on implementation-defined
behavior.

The Committee reaffirms that programs that depend on the identity of the
available locales, as opposed to their contents, are not strictly conforming.

The Committee believes that the first occurrence of the term “implementation
defined” in subclause 7.4.1.1 was intended in the sense of
“implementation-documented.” However, the Committee is reluctant to introduce a
new term, with possibly new conformance requirements, in a Technical
Corrigendum. The Committee notes that the term “locale-specific,” while making
the sentence read somewhat awkwardly, carries the necessary requirements (the
implementation must document the relevant details).

The Committee decided that, though the question only addresses one issue to do
with locales, the above discussion applies to all instances where the behavior
of an implementation depends on the locale. For this reason, the Committee
decided to address all such issues at this time.

The Committee should revisit this issue during the revision of the C Standard.

### Correction

***In subclause 5.2.1.2, page 11, change the third bullet item:***

wherein each sequence of multibyte characters begins in an *initial shift state*
and enters other implementation-defined *shift states*

***to:***

wherein each sequence of multibyte characters begins in an *initial shift state*
and enters other locale-specific *shift states*

***In subclause 7.3, page 102, second paragraph, change:***

Those functions that have implementation-defined aspects only when not in the
`"C"` locale are noted below.

The term *printing character* refers to a member of an implementation-defined
set of characters, each of which occupies one printing position on a display
device; the term *control character* refers to a member of an
implementation-defined set of characters that are not printing characters.

***to:***

Those functions that have locale-specific aspects only when not in the `"C"`
locale are noted below.

The term *printing character* refers to a member of a locale-specific set of
characters, each of which occupies one printing position on a display device;
the term *control character* refers to a member of a locale-specific set of
characters that are not printing characters.

***In subclause 7.3.1.2, page 102, subclause 7.3.1.6, page 103, subclause
7.3.1.9, page 104, and subclause 7.3.1.10, page 104, change:***

is one of an implementation-defined set of characters

***to:***

is one of a locale-specific set of characters

***In subclause 7.4.1.1, page 107, second paragraph of Description, change:***

a value of `""` for `locale` specifies the implementation-defined native
environment.

***to:***

a value of `""` for `locale` specifies the locale-specific native environment.

***In subclause 7.10.1.4, page 151, subclause 7.10.1.5, page 152, and 7.10.1.6,
page 152, change:***

In other than the `"C"` locale, additional implementation-defined subject
sequence forms may be accepted.

***to:***

In other than the `"C"` locale, additional locale-specific subject sequence
forms may be accepted.

***Change Footnote 131, page 159, from:***

If the implementation employs special bytes to change the shift state, these
bytes do not produce separate wide character codes, but are grouped with an
adjacent multibyte character.

***to:***

If the locale employs special bytes to change the shift state, these bytes do
not produce separate wide character codes, but are grouped with an adjacent
multibyte character.

***In subclause 7.11.6.2, page 168, change:***

The `strerror` function returns a pointer to the string, the contents of which
are implementation-defined.

***to:***

The `strerror` function returns a pointer to the string, the contents of which
are locale-specific.

***In Annex G, pages 204-207, move the following bullet items under subclause
G.3 to subclause G.4:***

> G.3.4, page 204, item 2 (“The shift states used for the encoding ...”)
>
> G.3.14, page 206, item 3 (“The sets of characters tested for ...”)
>
> G.3.14, page 207, item 33 (“The contents of the error message strings ...”)

***In Annex G.4 page 207, Locale-specific behavior, change:***

The following characteristics of a hosted environment are locale-specific:

***to:***

The following characteristics of a hosted environment are locale-specific and
must be documented by the implementation:


</div>


---

---

<div id="issue0066">

## Issue 0066: A set of locale questions

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_066.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_066.html)

Item 3 \- locales

In a conforming implementation, can the value of any of the following
expressions (subclause 7.4.2.1) be a value other than 0 or 1? Can the value of
the first expression be 0?

> ```c
> strlen(localeconv()->decimal_point)
>         strlen(localeconv()->thousands_sep)
>         strlen(localeconv()->mon_decimal_point)
>         strlen(localeconv()->mon_thousands_sep)
> ```

If the value can be greater than 1, can the string contain more than one
multibyte character? If so, can the string contain shift sequences? If so, can
the string end other than in the initial shift state?

---

Comment from WG14 on 1997-09-23:

### Response

Of the four `strlen` calls, the first must return 1, the second must return 0 or
1, and the other two must return 0 or more, in a conforming implementation.
There is a specific requirement for `decimal_point` in the second paragraph of
subclause 7.4.2.1 **Description**, and in the individual descriptions
“character” is intended to imply 0 or 1 while “string” is meant to imply 0 or
more.


</div>


---

---

<div id="issue0067">

## Issue 0067: Are the definitions of types clear?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0071](log_c90.md#issue0071)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_067.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_067.html)

Item 4 \- definitions of types

The terms “signed integer type,” “unsigned integer type,” and “integral type”
are defined in subclause 6.1.2.5. The C Standard also uses the terms “integer
type,” “signed integral type,” and “unsigned integral type” without defining
them. Integer-valued bitfields are also introduced in subclause 6.5.2.

a. For each of the following types, which if any of the six categories above do
they belong to?

```c
char
        signed char
        unsigned char
        signed short
        unsigned short
        signed int
        unsigned int
        signed long
        unsigned long
 	int : N	 /* i.e. bitfield of size N /*
        signed int : N
        unsigned int : N
        enumerated type
```

b. For each of these categories, do the `const` and/or `volatile` qualified
versions of the types belonging to the category also belong to the category?

c. Can an implementation extension add other types defined by the C Standard to
any of these six categories?

d. Can an implementation define other types (e.g. `__very long`) which belong to
any of these six categories?

e. If the answer to (c) or (d), or both, is yes, can `size_t` and `ptrdiff_t` be
one of these other types, or must it be a type in the above list?

---

Comment from WG14 on 1997-09-23:

### Response

a) “Signed integer type”, “unsigned integer type”, and plain “integer type” are
used interchangeably with “signed integral type”, “unsigned integral type”, and
“integral type” in the C Standard. This observation makes it easy to categorize
the types in your list.

b) Yes, see subclause 6.1.2.5.

c) No, the list in the C Standard is meant to be exhaustive. For example,
`float` cannot be defined as an integer type.

d) No strictly conforming program could contain an instance of such a type. The
treatment of such types is beyond the scope of the C Standard.

e) No, it must be a type in the list. For example, `size_t` cannot be defined as
`unsigned __int24`.


</div>


---

---

<div id="issue0068">

## Issue 0068: When are values of the type `char` treated as `signed`or `nonnegative` integers

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_068.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_068.html)

Item 5 \- handling of `char` values

Values of the type `char` must be treated as either “signed” or “nonnegative”
integers (subclause 6.1.2.5).

a. Is the treatment determined strictly by the value of the expression `CHAR_MAX
== SCHAR_MAX`?

b. If the treatment is as “signed” integers, does the type `char` behave in
every instance as the type `signed char` (though of course being a different
type)? If not, what are the differences?

c. If the treatment is as “nonnegative” integers, does the type `char` behave in
every instance as the type `unsigned char` (though of course being a different
type)? If not, what are the differences? In particular, do the "no overflow,
reduce modulo" semantics apply?

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes.

b) and c) Yes. Subclause 6.2.1.1, “As discussed earlier, ...” indicates that
this is the intent.


</div>


---

---

<div id="issue0069">

## Issue 0069: What is the meaning of *pure binary numeration system*?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0171](log_c90.md#issue0171)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_069.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_069.html)

Item 6 \- representation of integral types

Subclause 6.1.2.5 refers to the representation of a value in an integral type
being in a “pure binary numeration system,” and defines this further in Footnote
18\. On the other hand, the wording of ISO 2382 is:

> 05.03.15
>
> **binary (numeration) system**
>
> The *fixed radix numeration system* that uses the *bits* 0 and 1 and the *radix*
> two.
>
> Example: In this *numeration system,* the numeral 110,01 represents the number
> "6,25"; that is 1 x 2-2 \+ 1 x 2-1 \+ 1 x 2-2.
>
> 05.03.11
>
> **fixed radix (numeration) system**
>
> **fixed radix notation**
>
> A *radix numeration system* in which all the *digit places,* except perhaps the
> one with the highest *weight,* have the same *radix.*
>
> NOTES
>
> 1\. The weights of successive digit places are successive integral powers of a
> single radix, each multiplied by the same factor. Negative integral powers of
> the radix are used in the representation of factors.
>
> 2\. A fixed radix numeration system is a particular case of a *mixed radix
> numeration system*; see also Note 2 to 05.03.19.
>
> 05.03.08
>
> **radix**
>
> **base (deprecated in this sense)**
>
> In a *radix numeration system,* the positive *integer* by which the *weight* of
> any *digit place* is multiplied to obtain the weight of the digit place with the
> next higher weight.
>
> Example: In the *decimal numeration system* the radix of each digit place is
> 10\.
>
> NOTE \- The term base is deprecated in this sense because of its mathematical
> use (see definition in 05.02.01).
>
> 05.03.07
>
> **radix (numeration) system**
>
> A *positional representation system* in which the ratio of the *weight* of any
> one *digit place* to the weight of the digit place with the next lower weight is
> a positive *integer.*
>
> NOTE \- The permissible values of the *character* in any digit place range from
> zero to one less than the *radix* of that digit place.
>
> 05.03.04
>
> **weight**
>
> In a *positional representation system,* the factor by which the value
> represented by a *character* in a *digit place* is multiplied to obtain its
> additive contribution in the representation of a number.
>
> 05.03.03
>
> **digit place**
>
> **digit position**
>
> In a *positional representation system,* each site that may be occupied by a
> *character* and that may be identified by an ordinal number or by an equivalent
> identifier.
>
> 05.03.01
>
> **positional (representation) system**
>
> **positional notation**
>
> Any *numeration system* in which a number is represented by an *ordered* set of
> *characters* in such a way that the value contributed by a character depends
> upon its position as well as upon its value.

a. What is the legal force of the footnote, given that it quotes a definition
from a document other than ISO 2382 (see 3)?

b. Is the footnote wording correct, seeing that the ISO 2382 definition does not
appear to allow any of the common representations (note the word “positive” in
05.03.07)?

c. Does the C Standard require that an implementation appear to use only one
representation for each value of a given type?

d. Does the C Standard require that all the bits of the value be significant?

e. Does the C Standard require that all possible bit patterns represent numbers?

f. Do the answers to questions (c), (d), and (e) depend on whether the type is
signed or unsigned, and in the former case, on the sign of the value?

g. If it is permitted for certain bit patterns not to represent values, is
generation of such a value by an application (using bit operators) undefined
behavior, or is use of such a value strictly conforming provided that it is not
used with arithmetic operators?

In particular, are the following five implementations allowed?

h. Unsigned values are pure binary. Signed values are represented using
ones-complement (in other words, positive and negative values with the same
absolute value differ in all bits, and zero has two representations). Positive
numbers have a sign bit of 0, and negative numbers a sign bit of 1\. In both
cases, all bits are significant.

i. Unsigned values are pure binary. Signed values are represented using
sign-and-magnitude with a pure binary magnitude (note that the top bit is not
“additive”). Positive numbers have a sign bit of 0, and negative numbers a sign
bit of 1\. In both cases, all bits are significant.

j. Unsigned values are pure binary, with all bits significant. Signed values
with an MSB (sign bit) of 0 are positive, and the remainder of the bits are
evaluated in pure binary. Signed values with an MSB of 1 are negative, and the
remainder of the bits are evaluated in BCD. If ints are 20 bits, then `INT_MAX`
is 524,287 and `INT_MIN` is -79,999.

k. Signed values are twos-complement using all bits. Unsigned values are pure
binary, but ignoring the MSB (so each number has two representations). In this
implementation, `SCHAR_MAX == UCHAR_MAX`, `SHRT_MAX == USHRT_MAX`, `INT_MAX ==
UINT_MAX`, and `LONG_MAX == ULONG_MAX`.

l. Signed values are twos-complement. Unsigned values are pure binary. In both
cases, the top three bits of the value are ignored (and each number has eight
representations). For signed values, the sign bit is the fourth bit from the
top.

Furthermore:

m. Does the C Standard require that the values of `SCHAR_MAX`, `SHRT_MAX`,
`INT_MAX`, and `LONG_MAX`, defined in `<limits.h>` (subclause 5.2.4.2.1) all be
exactly one less than a power of 2?

n. If the answer to (m) is “yes,” then must the exponent of 2 be exactly one
less than `CHAR_BIT * sizeof (T)`, where `T` is `signed char`, `short`, `int`,
or `long`, respectively?

o. Does the C Standard require that the values of `UCHAR_MAX`, `USHRT_MAX`,
`UINT_MAX`, and `ULONG_MAX`, defined in `<limits.h>` (subclause 5.2.4.2.1) all
be exactly one less than a power of 2?

p. If the answer to (p) is “yes,” then must the exponent of 2 be exactly
`CHAR_BIT * sizeof (T)`, where `T` is `unsigned char`, `unsigned short`,
`unsigned int`, or `unsigned long` respectively?

q. Does the C Standard require that the absolute values of `SCHAR_MIN`,
`SHRT_MIN`, `INT_MIN`, and `LONG_MIN`, defined in `<limits.h>` (subclause
5.2.4.2.1) all be exactly a power of 2 or exactly one less than a power of 2?

r. If the answer to (r) is “yes,” then must the exponent of 2 be exactly one
less than `CHAR_BIT * sizeof (T)`, where `T` is `signed char`, `short`, `int`,
or `long` respectively?

s. If any of the answers to (m), (p), or (r) is “no,” are there any values for
each of these expressions that are permitted by subclause 5.2.4.2 but prohibited
by the C Standard for other reasons, and if so, what are they?

t. Does the C Standard require that the expressions `(SCHAR_MIN + SCHAR_MAX)`,
`(SHRT_MIN + SHRT_MAX)`, `(INT_MIN + INT_MAX)`, and `(LONG_MIN + LONG_MAX)` be
exactly 0 or -1? If not, does it put any restrictions on these expressions?

---

Comment from WG14 on 1997-09-23:

### Response

Before providing detailed answers, we want to provide some clarified
terminology. For any object type `T`, the underlying bytes of the object can be
copied into an array of `unsigned char`:

```c
#define N sizeof(T)
 union aligned_buf {
         T t;
         unsigned char s[N];
         } buf;
 T object;
 .....
         memcpy(buf.s, (const void *)&object, N);
```

The *object representation* of an object consists of the resulting sequence of
`N` objects of type `unsigned char` in the buffer. The object representation
depends upon several features of the implementation such as byte-ordering
(“big-endian,” “little-endian,” etc.), “holes” (i.e., bits within a scalar
object which do not participate in forming the value of the object), and
“padding” (i.e., bits in a non-scalar object which lie between the component
scalar objects or after the last scalar object).

The *value representation* of an object is a sequence of bits structured in a
specific conventional way. The scalar components are listed in their declaration
sequence. Each scalar component is a sequence of bits (the “participating bits”)
arranged in a conventional ordering. The value representation of floating-point
and pointer types is implementation-defined. The value representation of an
integer type is defined as follows: The least-significant bit (the bit which
represents the integer value 1\) is also called the low-order bit or rightmost
bit; the most-significant bit is also called the high-order bit or leftmost bit.
The sign bit (if any) is the leftmost bit.

If all the bits in a scalar object representation participate in the value
representation (i.e. no holes or padding), then the value representation can be
referred to simply as the *representation.* The bits of the value representation
determine a *value,* which is one discrete element of an implementation-defined
set of values. The conventional depiction of an integer value is as a decimal
integer, optionally signed, such as 128 or -1.

Here is an example. Consider a (possibly hypothetical) ones-complement
implementation whose `int` value representation provides one sign bit and 40
integer bits.

```c
    +-+---------------------+
    | |                     |
    +-+---------------------+
     1         40
```

Its object representation provides one sign bit, a hole containing seven
non-participating bits, and 40 integer bits (issues of byte ordering are
irrelevant here):

```c
    +-+------+---------------------+
    | |      |                     |
    +-+------+---------------------+
     1   7        40
```

The value representation containing 41 zero bits designates the value 0:

```c
    +-+---------------------+
    |0|000     ...       000|
    +-+---------------------+
     1         40
```

Depending upon the implementation, the value representation containing 41 one
bits may designate the same value 0, in which case it is indistinguishable from
the other value representation; or it may designate a distinguishable value,
conventionally depicted as -0, which is arithmetically equal to 0 but
distinguishable by bitwise operations.

```c
    +-+---------------------+
    |1|111     ...       111|
    +-+---------------------+
     1         40
```

Now for detailed replies:

a) Footnotes are not normative. The *legality* of a footnote is beyond the scope
of WG14/X3J11.

b) Yes, the footnote is correct.

c) No, there is no such requirement.

d) In view of the discussion above, we assume you mean the following question:
Does the C Standard require that all bits of the object representation
participate in the value representation? For character types, all bits of the
object representation do contribute. See subclauses 7.9.2 (re binary streams)
and 7.11.1 (re string functions) for (indirect) justification. More precisely,
any bits that do not contribute to the value of a character type must not
contribute to the value of any other object type. (Parity bits are an obvious
example.) For other types, the answer is no.

e) In view of the discussion above, we assume you mean the following question:
Does the C Standard require that all possible bit patterns of the object
representation represent numbers? For the type `unsigned char`, the answer is
yes. (And if all values of the type `char` are non-negative, then the answer is
yes.) Otherwise, the answer is no.

f) No, except for the character types as mentioned above.

g) Not applicable, since it is unclear what are the meanings of “bit pattern”
and “value” in the question; see the answer to part (e).

h) Yes, provided there is no other violation of the C Standard.

i) Yes, provided there is no other violation of the C Standard.

j) No. It is not a pure binary system.

k) Yes, except for `SCHAR_MAX == UCHAR_MAX` (which is specifically disallowed),
provided there is no other violation of the C Standard.

l) Yes, provided there is no other violation of the C Standard.

m) Yes, because subclause 6.1.2.5 states that the positive signed integers have
the same representation as the corresponding unsigned integers, and because
signed integers use a pure binary numeration system. The Committee intended to
permit ones complement, twos complement, and signed magnitude implementation.

n) No. There are architectures on which not all bits can be used.

p) Yes, because subclause 6.1.2.5 requires unsigned integers to behave as if a
result “is reduced modulo the number that is one greater than the largest value
that can represented,” and unsigned integers use a pure binary numeration
system.

q) No. The memory occupied by a value of an integer is allowed to exceed the
number of binary digits used to represent the actual value.

r) Yes. See the answer to part (m).

s) No. See the answer to part (q).

t) Not applicable.

u) Yes, the expression must evaluate to 0 or -1.


</div>


---

---

<div id="issue0070">

## Issue 0070: Can non-compatible types be used interchangeabily for function arguments?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_070.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_070.html)

Item 7 \- interchangeability of function arguments

Consider the following program:

```c
#include <stdio.h>

 void output (c)
        int c;
        {
        printf("C == %d\n", c);
        }
 int main (void)
        {
        output(6);
        output(6U);
        return 0;
        }
```

The constant `6` has type `int`, and `6U` has type `unsigned int` (subclause
6.1.3.2), and they have the same representation (subclause 6.1.2.5). Footnote
16, which is not a part of the C Standard, states that this implies that they
are interchangable as arguments. However, `int` and `unsigned int` are not
compatible types, and so subclause 6.3.2.2 makes the second call undefined.

Is the program strictly conforming?

Note that similar issues arise in connection with the other cases mentioned in
Footnote 16 (function return values and union members).

---

Comment from WG14 on 1997-09-23:

### Response

The program is not strictly conforming. Since many pre-existing programs assume
that objects with the same representation are interchangeable in these contexts,
the C Standard encourages implementors to allow such code to work, but does not
require it.


</div>


---

---

<div id="issue0071">

## Issue 0071: Are all enumerated types compatible with a single type?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0067](log_c90.md#issue0067)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_071.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_071.html)

Item 8 \- enumerated types

The C Standard states (in effect) that an enumerated type is a set of integer
constant values (subclause 6.1.2.5). It also states that an enumerated type must
be compatible with an implementation-defined integer type (subclause 6.5.2.2).
Finally, the integral promotions (subclause 6.2.1.1) convert an enumerated type
to `signed` or `unsigned int`. Consider:

```c
enum foo { foo_A = 0, foo_B = 1, foo_C = 8 };
 enum bar { bar_A = -10, bar_B = 10 };
 enum qux { qux_A = UCHAR_MAX * 4, qux_B };
```

a. If any value between zero and `SCHAR_MAX` (inclusive) is assigned to a
variable of type `enum foo`, and the value of the variable is then converted to
type `int` or `unsigned int`, does the C Standard require the original value to
result; or is the implementation permitted or required to convert it to one of
the three values 0, 1, and 8; or is the result of the assignment undefined?

b. Can a conforming implementation require all enumerated types to be compatible
with a single type?

c. If the answer to (b) is “yes,” and assuming that the value `UCHAR_MAX * 4` is
less than `SHRT_MAX` is the declaration of the type `enum qux` strictly
conforming, or can a conforming implementation require all enumerated types to
be compatible with a single type which is a character type?

d. Can an implementation make the type that `enum bar` is compatible with be an
unsigned type, even though it uses an enumeration constant not representable in
that type?

e. Can an implementation make the type that `enum qux` is compatible with be
either of `signed char` or `unsigned char`, even though it uses an enumeration
constant not representable in that type?

f. If the answer to (d) or (e) is “yes,” what is the effect of making one of the
enumeration constants of an enumerated type outside the range of the compatible
type? What is the effect of assigning the value of that constant to an object of
the enumerated type?

g. Can the type that an enumerated type is compatible with be `signed` or
`unsigned long`? If so, what are the effects of the integral promotions on a
value of that type?

h. If an implementation is allowed to add other types to the list of integer
types (see items 4(b) and (c)), then can the type that an enumerated type is
compatible with be such a type?

---

Comment from WG14 on 1997-09-23:

### Response

a) Every enumerated type is compatible with some integer type (subclause
6.5.2.2). When conversion takes place between compatible types, values are not
altered (subclause 6.2). So for values between 0 and `SCHAR_MAX`, the original
value must result, because no matter what type is chosen, the value can be
expressed in that type.

b) Yes it can.

c-g) It is the intention of the C Standard that all the members of the
enumeration be representable in the enumerated type, and that the compatible
integer type be one which promotes to `int` or `unsigned int`.

h) An implementation is not allowed to add other types to the list. (See reply
to [Defect Report #067](log_c90.md#issue0067).)

### Correction

***In subclause 6.5.2.2, page 61, second paragraph of Semantics, change:***

Each enumerated type shall be compatible with an integer type; the choice of
type is implementation-defined.

***to:***

Each enumerated type shall be compatible with an integer type. The choice of
type is implementation-defined, but shall be capable of representing the values
of all the members of the enumeration.


</div>


---

---

<div id="issue0072">

## Issue 0072: What is the definition of an object?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0044.01](log_c90.md#issue0044.01), [0051](log_c90.md#issue0051), [0073](log_c90.md#issue0073)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_072.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_072.html)

Item 9 \- definition of object

Consider the following translation unit:

```c
#include <stdlib.h>

 typedef double T;
 struct hacked
        {
        int size;
        T data [1];
        };

 struct hacked *f (void);
        {
        T *pt;
        struct hacked *a;
        char *pc;

        a = malloc (sizeof (struct hacked) + 20 * sizeof (T));
        if (a == NULL)
              return NULL;
        a->size = 20;

 	/* Method 1 /*
 	a->data [8] = 42;					/* Line A /*

 	/* Method 2 /*
        pt = a->data;
 	pt += 8;							/* Line B /*
        *pt = 42;

 	/* Method 3 /*
        pc = (char *) a;
        pc += offsetof (struct hacked, data);
 	pt = (T *) pc;						/* Line C /*
 	pt += 8;							/* Line D /*
        *pt = 6 * 9;
        return a;
        }
```

Now, [Defect Report #051](log_c90.md#issue0051) has established that the assignment on
line A involves undefined behavior.

a. Is the addition on line B strictly conforming?

If the answer to (a) is “yes,” are the three statements forming “method 2” a
valid way of implementing the `struct hacked`?

b. Is the cast of line C strictly conforming?

c. Is the addition on line D strictly conforming?

d. If the answer to (c) and (d) are “yes,” are the five statements forming
“method 3” a valid way of implementing the `struct hacked`?

Now suppose that the definition of type `T` is changed to `char`. This means
that the last bullet in subclause 6.3 (“an object shall have its stored value
accessed only by ... a character type”) now applies, and furthermore it means
that the location accessed is an integral multiple of `sizeof(T)` bytes from the
start of the `malloc`ed object, and so constitutes an element of that object
when viewed as an array of `T`.

e. Is the assignment on line A now strictly conforming?

f. What are the answers to questions (a) to (e) with this change?

---

Comment from WG14 on 1997-09-23:

### Response

a) [Defect Report #051](log_c90.md#issue0051) provides the rationale for why Line A
results in undefined behavior. The same rules also apply to the assignment to
`pt`; thus Line B results in undefined behavior

b) Not applicable given the answer to question (a).

c) Assignment causes the base address of the structure to be assigned to `pc`.
The response to [Defect Report #044, question 1](log_c90.md#issue0044.01), states that use
of the `offsetof` macro does not result in undefined behavior. The second line
causes `pc` to point to member `data`. Line C does not contain any construct
that would result in the program not being strictly conforming.

d) Line D results in undefined behavior. See answer (a) for rationale.

e) Not applicable given answers (c) and (d).

f) Subclause 6.3 contains additional restrictions, not permissions.

g) The answers to questions (a)-(e) are not affected if `T` has `char` type.


</div>


---

---

<div id="issue0073">

## Issue 0073: Another definition of an object question

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0072](log_c90.md#issue0072), [0178](log_c90.md#issue0178)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_073.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_073.html)

Item 10 \- definition of object

Consider the following translation unit:

```c
#include <stdlib.h>
 struct complex
        {
        double real [2];
        double imag;
        }
 #define D_PER_C (sizeof (struct complex) / sizeof (double))
 struct complex *f (double x)
        {
        struct complex *array = malloc(sizeof (struct complex) +
              sizeof (double));
        struct complex *pc;
        double *pd;

        if (array == NULL)
              return NULL;
 	array [1].real [0] = x;				/* Line A /*
 	array [1].real [1] = x;				/* Line B /*
 	array [1].imag = x;					/* Line C /*
 	pc = array + 1;					/* Line D /*
 	pc = array + 2;					/* Line E /*
 	pd = &(array [1].real [0]);			/* Line F /*
 	pd = &(array [1].real [1]);			/* Line G /*
 	pd = &(array [1].imag);				/* Line H /*
 	pd = &(array [0].real [0]) + D_PER_C;		/* Line I /*
 	pd = &(array [0].real [1]) + D_PER_C;		/* Line J /*
 	pd = &(array [0].imag) + D_PER_C;		/* Line K /*
 	pd = &(array [0].real [0]) + D_PER_C * 2; 		/* Line L /*
 	pd = &(array [0].real [0]) + D_PER_C + 1; 		/* Line M /*
 	pd = &(array [0].real [0]) + D_PER_C + 2; 		/* Line N /*
        return array;
        }
```

Subscripting is strictly conforming if the array is “large enough” (subclause
6.3.6). For each of the marked lines, is the assignment strictly conforming?

---

Comment from WG14 on 1997-09-23:

### Response

Lines A, B, C. The identifier `array` points to an object that is not large
enough to hold two `struct complex` objects. The dot selection operator is at
liberty to require the complete structure denoted by its left hand side to be
accessed. Such an access would result in undefined behavior.

Line D. If `array` is regarded as pointing to a single structure then creating a
pointer to one past the end of that object is permitted.

Line E. If `array` is regarded as pointing to a single structure then creating a
pointer two past the end of that object is not permitted. Since there is
insufficient storage allocated to create a second `struct complex` object, it is
not permitted to point one past this partial `struct complex` object.

Lines F, G, H. Same analysis as Lines A, B, C.

Lines I, J, K, L, M, N. All of these calculations will result in pointers that
point outside the original object (arrays or structures) and result in undefined
behavior.


</div>


---

---

<div id="issue0074">

## Issue 0074: Can the alignment of an object that is a member of a structure be different from the alignment of an object of the same type that is not a member of a structure?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_074.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_074.html)

Item 11 \- alignment and structure padding

The existence of structure padding (subclause 6.5.2.1) can be detected by a
strictly conforming program by use of the `sizeof` operator and the `offsetof`
macro.

a. If a structure has a field of type `t`, can the alignment requirements of the
field be different from the alignment requirements of objects of the same type
that are not members of structures?

If the answer to (a) is “yes,” then where applicable the remaining questions
should be assumed to have been asked for both objects within structures and
objects outside structures.

b. If an array has a component type of `t`, can the alignment requirements of
the elements of the array be different from those of independent variables of
type `t`?

The alignment requirement of a type is that addresses of objects of that type
must be multiples of some constant (subclause 3.1); for some type `t`, this is
written `A(t)` in this Defect Report.

c. For any type `t`, can the expression `sizeof (t) % A(t)` be non-zero (in
other words, can `A(t)` be a value other than 1, `sizeof (t)`, or a factor of
`sizeof (t)`)? It would appear not, because otherwise adjacent elements of an
array of objects of type `t` would either not be correctly aligned, or else
would not be contiguously allocated.

d. Can `A(struct foo)` be greater than the least common multiple of `A(type_1)`,
`A(type_2)`, ..., `A(type_n)`, where `type_1` to `type_n` are the types of the
elements of `struct foo`? In particular, if a structure holds exactly one
element, can `A(structure type)` be different from `A(element type)`? (In each
case, if the answer to (a) is “yes,” `A(type)` should be interpreted
appropriately.)

e. If, at any point in a structure or union (obviously excluding the start),
there is more than one size of padding that can satisfy all alignment
requirements, can any size be used, or must the smallest (possibly zero) padding
be used because that is all that is “necessary to achieve the appropriate
alignment?”

f. If a structure type has trailing padding to ensure that its use as an array
element would be correctly aligned, must objects of that type which are not
array elements also have the padding? If not, what is the effect of using
`memcpy` to copy the value of one such object to another thus?

```c
struct fred a, b;
 	/* ... /*
        memcpy(&a, &b, sizeof (struct fred));
```

It appears from subclause 6.3.3.4 (“the size is determined from the type of the
operand”) that `sizeof a` must equal `sizeof (struct fred)`. Is this correct?

g. When an element of a structure is in turn a structure, can trailing padding
of the inner structure be reused to hold other elements of the enclosing
structure? For example, in:

```c
struct outer
        {
        struct inner { long a; char b; } inner;
        char c;
        };
```

is it permitted for `offsetof (struct outer, c)` to be less than `sizeof (struct
inner)`?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2.5 says, “... pointers to qualified or unqualified versions of
compatible types shall have the same representation and alignment requirements.”

Subclause 6.5.2.1 says, “Each non-bit-field member of a structure or union
object is aligned in an implementation-defined manner appropriate to its type.”
And later, “There may therefore be unnamed padding within a structure object,
... as necessary to achieve the appropriate alignment.”

a) It is possible for an implementation to state generalized requirements to
satisfy subclause 6.1.2.5. These requirements may be further strengthened using
the implementation-defined behavior made available in subclause 6.5.2.1. Yes,
the alignment requirements can be different.

b) In several places the C Standard states that a single object may be treated
as an array of one element. Nowhere does it give permission for array element
types to have different alignment requirements from isolated object types.

c) `sizeof (t)` must indeed be a multiple of `A(t)`.

d) Yes. A structure object can have an alignment that is greater than the least
common multiple of the alignments of its members.

e) The phrase “necessary to achieve the appropriate alignment” is not considered
to mean the use of the minimum padding possible. The Committee does not see any
advantage to changing this phrase.

f) Yes. See answer to question (b). `sizeof (struct fred)` must equal `sizeof
a`.

g) Such sharing of storage by objects would cause the requirements of subclause
6.3 to be violated and is not allowed.


</div>


---

---

<div id="issue0075">

## Issue 0075: What is the alignment of allocated memory?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_075.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_075.html)

Item 12 \- alignment of allocated memory

Is a piece of memory allocated by `malloc` required to be aligned suitably for
any type, or only for those types that will fit into the space? For example,
following the assignment:

```c
void *vp = malloc (1);
```

is it required that `(void *)(int *)vp` compare equal to `vp` (assuming that
`sizeof(int) > 1`), or is it permissible for `vp` to be a value not suitably
aligned to point to an `int`?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 7.10.3 requires allocated memory to be suitably aligned for *any*
type, so they must compare equal.


</div>


---

---

<div id="issue0076">

## Issue 0076: A set of pointers to the end of arrays questions

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0012](log_c90.md#issue0012), [0166](log_c90.md#issue0166)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_076.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_076.html)

Item 13 \- pointers to the end of arrays

Consider the following code extracts:

```c
int a [10];
        int *p;
 	/* ... */
        p = &a[10];
```

and

```c
int *n = NULL;
        int *p
 	/* ... */
        p = &*n;
```

In the first extract, is the assignment strictly conforming (with `p` being set
to the expression `a + 10`), or is the constraint in subclause 6.3.3.2 violated
because `a[10]` is not an object? Note that this expression is often seen in the
idiom:

> ```c
> for (p = &a[0]; p &lt; &a[10]; p++)
>  		/* ... */
> ```

In the second extract, is the assignment strictly conforming (with `p` being set
to a null pointer), or is the constraint in subclause 6.3.3.2 violated because
`*n` is not an object?

If only one assignment is strictly conforming, what distinguishes the two cases?
If either assignment is strictly conforming, what distinguishes it from the
situation described in the following extract from the response to [Defect Report
#012](log_c90.md#issue0012)?

> Given the following declaration:
>
> ```c
> void *p;
> ```
>
> the expression `&*p` is invalid. This is because `*p` is of type `void` and so
> is not an lvalue, as discussed in the quote from subclause 6.2.2.1 above.
> Therefore, as discussed in the quote from subclause 6.3.3.2 above, the operand
> of the `&` operator in the expression `&*p` is invalid because it is neither a
> function designator nor an lvalue.
>
> This is a constraint violation and the translator must issue a diagnostic
> message.

---

Comment from WG14 on 1997-09-23:

### Response

This issue remains open. The C Standard as currently worded has the following
consequences:

1\) Subclause 6.3.3.2 requires the operand of `&` to be an lvalue designating an
object; `a[10]` is not an object.

2\) Subclause 6.3.3.2 requires the operand of `&` to be an lvalue; `NULL` is not
an lvalue.

Since the use of either construct prevents a program from being strictly
conforming, the remaining portion of the question is not applicable.

However, the Committee is not entirely comfortable with these restrictions and
may decide to relax them in resolving this issue.


</div>


---

---

<div id="issue0077">

## Issue 0077: Is the address of an object constant throughout its lifetime?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_077.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_077.html)

Item 14 \- stability of addresses

Is the address of an object constant throughout its lifetime? For example, if a
pointer to an object is written to a binary file using `fwrite`, and then read
back later during the same run of the program using `fread`, is it guaranteed to
compare equal to the address of the original object taken again?

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard does not explicitly state that the address of an object remains
constant throughout the life of the object. That this is the intent of the
Committee can be inferred from the fact that an address constant is considered
to be a constant expression. The framers of the C Standard considered that it
was so obvious that addresses should remain constant that they neglected to
craft words to that effect.

The Committee should revisit this issue during the revision of the C Standard.


</div>


---

---

<div id="issue0078">

## Issue 0078: May optimizer invoke the as-if rule to rearrange code?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_078.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_078.html)

Item 15 \- uniqueness of addresses

Consider the following translation unit:

```c
#include <string.h>

 unsigned int f (unsigned int a)
        {
        unsigned int x, y;

        x = a;
        x = x * x + a;
        if (x > 100)
 		return x;	/* Returned value must be > 100 */
        if (&x == &y)
              return 0;
        y = a + 1;
        y = y * y + 17;
 	return y;		/* Returned value must be > 0 */
        }

 unsigned int g1 (void) { return 0; };
 unsigned int g2 (void) { return 0; };

 unsigned int g (void)
        {
        return g1 != g2;
        }

 unsigned int h (void)
        {
        return memcpy != memmove;
        }

 const int j1 = 1;
 const int j2 = 1;

 unsigned int j (void)
        {
        return &j1 != &j2;
        }
```

a. Can `f` ever return zero? An aggressive optimizer could notice that `x` and
`y` are never used at the same time, and assign them the same memory location.
(The optimizer could be designed to conceal the fact that `x` and `y` are
sharing storage, for example by forcing the comparison to be unequal. Such an
application of the “as if” rule (subclause 5.1.2.3) would become increasingly
difficult to implement in the presence of operations such as writing out `&x` to
a file (using `fwrite` or the `fprintf %p` conversion specification) and then
reading it back in later in the same run of the program. However, this is
irrelevant; the issue is whether or not the implementation is required to
conceal it in the first place.)

b. Can `g` ever return zero? A optimizer using an intermediate form can easily
determine that the two functions have identical effects.

c. Can `h` ever return zero? The library function `memmove` (subclause 7.11.2.2)
completely meets the requirements for `memcpy` (subclause 7.11.2.1) and so they
could be implemented using the same code (even if the answer to (b) is no, this
could happen if the system library is not implemented in C).

d. Can `j` ever return zero? Since the two variables are constants, code which
uses `j1` instead of `j2` anywhere except in an address comparison cannot
distinguish them.

---

Comment from WG14 on 1997-09-23:

### Response

a) `f` can never return zero. There are three `return` statements:

i) Will always return a value greater than 100\.

ii) `x` and `y` exist at different addresses. An optimizer may invoke the as-if
rule to rearrange code provided it always achieves the required effect.
(Subclause 6.1.2.2: “Identifiers with *no linkage* denote unique entities.”)

iii) Modulo arithmetic may wrap to produce zero. However, it is not possible to
square any number, add 17 and get zero as the result.

b) No, `g` cannot return zero.

c) Yes, `h` can return zero.

d) `j` can never return zero. Subclause 6.7.2 says, “If the declaration of an
identifier for an object has file scope and an initializer, the declaration is
an external definition for the identifier.” Subclause 6.5 says, “A declaration
that also causes storage to be reserved for an object or function named by an
identifier is a *definition.*” Taken together these two statements can be taken
to imply that two file-scope definitions must refer to different objects.


</div>


---

---

<div id="issue0079">

## Issue 0079: Is the address of a standard library function the same in different translation units?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_079.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_079.html)

Item 16 \- constancy of system library function addresses

(These questions approach the same problem from three slightly different
directions.)

a. If a pointer to a given standard library function (say `strlen`) is evaluated
in two different translation units, and the pointers compared, must they compare
equal?

b. Can a conforming implementation declare a standard library function as having
internal linkage, or must the identifiers with file scope declared in standard
headers have external linkage?

c. If the contents of the header `<string.h>` include the following definition
of `strlen`, is the implementation conforming?

```c
static size_t strlen (const char *__s)
        {
        size_t __len = 0;

        while (*__s++)
              __len++;
        return __len;
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

Since the answer to question (b) is needed for question (a) it is given first.

b) Since, according to the fourth item in subclause 7.1.3, the library function
prototypes are implicitly `extern`, the standard library functions have external
linkage.

a) If the usage of `strlen` is such that standard library functions are referred
to, the pointers must compare equal by the requirements of subclauses 5.1.1.2
and 6.1.2.2.

c) The contents of standard headers are implementation-defined. For instance,
they may contain code written in other languages. It is not the job of this
Committee to mandate implementation. Whatever their contents, including a
standard header must achieve the effects required by the C Standard.


</div>


---

---

<div id="issue0080">

## Issue 0080: Questions on merging of string constants

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_080.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_080.html)

Item 17 \- merging of string constants

Consider the following code:

```c
char *s1 = "abcde" + 2;
 char *s2 = "cde";
```

Can the expression `(s1 == s2)` be non-zero? Is the answer different if the
first string literal is replaced by the two literals `"ab" "cde"` (because then
there are identical string literals)?

---

Comment from WG14 on 1997-09-23:

### Response

When the last paragraph of subclause 6.1.4 refers to “string literals” it is
referring to the static arrays created in translation phase 7 as specified in
the previous paragraph. Although the current wording of the C Standard may imply
that only completely identical arrays need not be distinct, this was not the
Committee's intent.

### Correction

***In subclause 6.1.4, page 31, change the last paragraph of Semantics (before
the Example) from:***

Identical string literals of either form need not be distinct. If the program
attempts to modify a string literal of either form, the behavior is undefined.

***to:***

These arrays need not be distinct provided their elements have the appropriate
values. If the program attempts to modify such an array, the behavior is
undefined.


</div>


---

---

<div id="issue0081">

## Issue 0081: What is the result of the left shift operator `E1 < E2`, when `E1` is signed?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_081.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_081.html)

Item 18 \- left shift operator

The result of the left shift operator `E1 < E2`, when `E1` is signed, is defined
(subclause 6.3.7) as `E1` left-shifted by `E2` bits, with vacated bits filled
with zeros. But what exactly does this mean?

The C Standard defines a bit (subclause 3.3) only as a unit of data storage.
Bits are related to the value of an object only in subclause 6.1.2.5, which
specifies the representation of certain types. It may therefore be claimed that
the left shift operator must act on representations, which are of fixed length.
In this interpretation, the left `E2` bits (including the sign bit) are lost, as
they would be if `E1` was unsigned; the sign bit of the result is taken from a
bit in `E1`, `E2` places to the right of the sign bit and, provided that the
resultant bit pattern actually represents a value of the result type, an
exception is impossible.

On the other hand, it may also be claimed that the whole of subclause 6.3
specifies the meaning of operations in abstract mathematical terms, subject to
the general note about exceptions. In this view, the bit sequence representing
the non-sign part of a signed integer is converted by the shift operation to a
bit sequence of indefinite length, and, to avoid an exception due to overflow,
this bit sequence must fit back in the non-sign part without the loss at the
left of anything but copies of the sign bit.

a. Which of these two views is correct?

b. If the answer to (a) is the first view, does undefined behavior occur if the
resulting bit pattern is not the representation of an integer?

The following questions apply only if the answer to (a) is that the second view
is correct.

c. If `E1` is positive, and `E1` times 2 to the power `E2` is less than or equal
to `INT_MAX` (or `LONG_MAX`), is the result always `E1` times 2 to the power
`E2`?

d. Under what circumstances is the result undefined?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.3 states that the binary operator `<` , among others, has
implementation-defined aspects for signed types. Therefore, the answer to “What
does it mean to left shift a signed value?” is that it is
implementation-defined.


</div>


---

---

<div id="issue0082">

## Issue 0082: Many varargs questions

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_082.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_082.html)

Item 19 \- multiple varargs

Consider the following translation unit:

```c
#include <stdarg.h>
 #include <stdio.h>

 extern int is_final_arg (int);

 void f1 (int n, ...)
        {
        va_list ap1, ap2;

        va_start (ap1, n);
        va_start (ap2, n);
        while (va_arg (ap1, int) != 0)
              printf ("Value is %d\n", va_arg (ap2, int));
        va_end (ap1);
        va_end (ap2);
        }

 void f2 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        for (;;)
              {
              n = va_arg (ap, int);
              if (is_final_arg (n))
 	           {
 	           va_end (ap);
 	           return;
 	           }
              printf ("Value is %d\n", n);
              }
        }

 void f3 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        while (n = va_arg (ap, int), n != 0)
              printf ("Value is %d\n", n);
        va_start (ap, n);
        while (n = va_arg (ap, int), n != 0)
              printf ("Value is still %d\n", n);
        va_end (ap);
        }

 void f4a (va_list *pap)
        {
        int n;

        while (n = va_arg (*pap, int), n != 0)
              printf ("Value is %d\n", n);
        }

 void f4 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        f4a (&ap);
        va_end (ap);
        }

 void f5a (va_list apc)
        {
        int n;

        while (n = va_arg (apc, int), n != 0)
              printf ("Value is %d\n", n);
        }

 void f5 (int n, ...)
        {
        va_list ap;

        va_start (ap, n);
        f5a (ap);
        va_end (ap);
        }
```

a. Is each function in this translation unit strictly conforming? Note in
particular:

in `f1`, the use of simultaneous `va_lists` in `f1`;

in `f2`, `va_start` and `va_end` are in different scopes;

in `f3`, there are two `va_start`s and one `va_end`;

in `f4`, the address of an object of type `va_list` is taken;

in `f4a` and `f5a`, `va_arg` is called with a first parameter which is not “the
same as the `va_list ap` initialized by `va_start`” (subclause 7.8.1.2).

b. Is the following implementation conforming?

`va_start` allocates a block of memory with `malloc`;

a `va_list` is a pointer to the block;

`va_end` frees the same block;

c. Is there any portable method to copy the current state of a `va_list`, for
example in order that the remaining arguments can be scanned twice without
knowledge of the `va_arg` calls made previous to that point? If the answer to
(b) is “yes,” I believe the answer to (c) must be “no.”

---

Comment from WG14 on 1997-09-23:

### Response

a) All functions listed except for `f3` contain strictly conforming code. The
function `f3` violates the intended requirement for `va_start` and `va_end` to
be invoked in matching pairs, as reflected in the following Correction.

b) There is nothing described in this section that would make such an
implementation non-conforming.

c) No.

### Correction

***In subclause 7.8.1, page 122, change the last sentence from:***

The `va_start` and `va_end` macros shall be invoked in the function accepting a
varying number of arguments, if access to the varying arguments is desired.

***to:***

The `va_start` and `va_end` macros shall be invoked in corresponding pairs in
the function accepting a varying number of arguments, if access to the varying
arguments is desired.

***In subclause 7.8.1.1, page 122, add at the end of the second paragraph of the
Description:***

`va_start` shall not be invoked again for the same `ap` without an intervening
invocation of `va_end` for the same `ap`.


</div>


---

---

<div id="issue0083">

## Issue 0083: A use of library functions question

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_083.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_083.html)

Item 20 \- use of library functions

Consider the following program:

```c
#include <stdio.h>

 int main (void)
        {
        printf ("%d\n", 42.0);
        return 0;
        }
```

This program clearly should have undefined behavior, but I can find no wording
which states so.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 7.1.7, page 99, insert after the words in parentheses in the
second sentence of the first paragraph:***

or a type (after promotion) not expected by a function with variable number of
arguments


</div>


---

---

<div id="issue0084">

## Issue 0084: When is an incomplete type in function declaration a parameter?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0104](log_c90.md#issue0104)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_084.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_084.html)

Item 21 \- incomplete type in function declaration

Consider the following declarations:

```c
struct tag;
 extern void (*f) (struct tag);
```

At the point of the declaration of `f`, the type of the parameter is incomplete.
Now a parameter is an object (subclause 3.15) with no linkage (subclause
6.1.2.2), but it is unclear whether this is a declaration of the parameter. If
it is, then the declaration of `f` is forbidden by subclause 6.5. If it is not,
then the declaration is strictly conforming. Which is the case?

If the type `struct tag` is completed before a call to `f`, is the call strictly
conforming? Alternatively, since the declaration of `f` includes an incomplete
type, is it possible to make a call to it at all?

---

Comment from WG14 on 1997-09-23:

### Response

From subclause 6.5.2.3, the incomplete type specified by the tag may be used,
unless the size of the corresponding object is needed.

In responding to Defect Reports, the Committee has discussed at length when the
size of an object is actually required. The C Standard is inconclusive with
regard to whether or not the size of the structure is needed in the example
given, leaving the behavior undefined.

The Committee should revisit this issue during the revision of the C Standard.


</div>


---

---

<div id="issue0085">

## Issue 0085: Is the return from `main` equivalent to calling `exit`?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_085.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_085.html)

Item 22 \- returning from `main`

Consider the following program:

```c
#include <stdlib.h>
 #include <stdio.h>

 int *pi;

 void handler (void)
        {
        printf ("Value is %d\n", *pi);
        }

 int main (void)
        {
        int i;

        atexit (handler);
        i = 42;
        pi = &i;
        return 0;
        }
```

Return from `main` is defined to be equivalent to calling `exit` (subclause
5.1.2.2.3). If the `return` statement was replaced by the equivalent call, the
program would be strictly conforming. Is it strictly conforming without this
replacement?

Note that if the answer is “yes,” special processing will be required for return
from `main,` which will depend on whether the call being returned from is the
initial call or a recursive one.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 5.1.2.2.3, page 7, add at the end of the first sentence the
footnote:***

In accordance with subclause 6.1.2.4, objects with automatic storage duration
declared in `main` will no longer have storage guaranteed to be reserved in the
former case even where they would in the latter.


</div>


---

---

<div id="issue0086">

## Issue 0086: At object-like macros in system headers conforming?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_086.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_086.html)

Item 23 \- object-like macros in system headers

Consider an implementation where `<string.h>` defines the macro `strlen` thus:

```c
#define strlen  __internal_fast_strlen
```

and declares functions (defined elsewhere) called `__internal_fast_strlen` and
`strlen`, both with the functionality of `strlen` in subclause 7.11.6.3. Is such
an implementation conforming with respect to the rules of subclause 7.1.7?

Note that a strictly conforming application can detect this situation by
comparing the value of the expression `strlen` taken before and after a
`#undef`.

---

Comment from WG14 on 1997-09-23:

### Response

The question asks whether a system header can define the name of a library
function as an object-like macro, and cites subclause 7.1.7 as not using the
term “function-like.”

The Committee notes the absence of this term, but also notes that subclause
7.1.7 requires that the macro definition always be suppressed when not followed
by an open parenthesis. Therefore such macros must either be function-like, or
the implementation must cause them to act as function-like macros.


</div>


---

---

<div id="issue0087">

## Issue 0087: Is the order of evaluation when there are no sequence points well defined?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0287](log_c99.md#issue0287)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_087.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_087.html)

Item 24 \- order of evaluation

Consider the following program:

```c
int g;

 int main (void)
        {
        int x;

 	x = (10, g = 1, 20) + (30, g = 2, 40);	 /* Line A */
 	x = (10, f (1), 20) + (30, f (2), 40);	 /* Line B */
 	x = (g = 1) + (g = 2);			 /* Line C */
        return 0;
        }

 int f (int i)
        {
        g = i;
        return 0;
        }
```

Subclause 6.3 makes the statement:

> Between the previous and the next sequence point an object shall have its stored
> value modified at most once by the evaluation of an expression.

Consider line A. The full expression (the assignment to `x`) assigns two values
(1 and 2\) to `g`. Each such assignment is surrounded by sequence points.
However, there is no sequence point between the two operands of the addition,
and therefore no defined order of evaluation of the two inner assignments. There
are a number of possible interpretations of the C Standard that can be made.

1. Multiple threads of evaluation may take place at one time (or equivalently, the evaluation of various parts of the expression may be interleaved to any level of detail), provided that anything specified to occur before a given sequence point actually takes place before anything specified to occur after the same sequence point. (This is equivalent to the “collateral evaluation” of Algol 68.)

   In this interpretation, the expression is clearly undefined, because the two
   assignments to `g` may take place simultaneously and interfere destructively
   with one another. However, if this model is applied to line B, it yields the
   same result (since the sequence points occur at the same places). This means
   that, in effect, two function calls can be taking place simultaneously, and, if
   they modify the same object, the effect is undefined. This would surprise many
   users of the C Standard.
2. As (1), but assignments are atomic. This means that `g` has the value 1 or 2, though it is unspecified which. When applied to line C, this would also mean that `x` is specified to be assigned the value 3\. This seems counter to the quoted provision of subclause 6.3.
3. Any expression which completely fills the interval between two sequence points, and does not contain any embedded sequence points, is an “atomic sequence.” The operations of any one atomic sequence are carried out together, and cannot be interleaved with any other atomic sequence. The order of the atomic sequences is unspecified, except that if the ending sequence point of one atomic sequence is the same as the starting point of another atomic sequence, they must be executed in that order.

   In line A, there are five atomic sequences:

   (i) evaluate 10

   (ii) assign 1 to `g`

   (iii) evaluate 30

   (iv) assign 2 to `g`

   (v) evaluate 20 and 40, add, and assign to `x`

   (i) must come before (ii), (iii) must come before (iv), (v) must come after (ii)
   and (iv).

   In line A this model has the same effect as (2), but it could differ in more
   complex expressions.
4. Multiple threads of execution can occur within an expression, but all except one are suspended while a function is being executed (this may, of course, spawn off new threads). This interpretation could be viewed as supported by the wording in subclause 6.6: “Except as indicated, statements are executed in sequence.” It would have the effect of leaving line A undefined while line B is conforming (with it being unspecified whether the latter assigns 1 or 2 to `g`).

Which, if any, of these interpretations is correct? If none of them, what is the
correct interpretation to make?

---

Comment from WG14 on 1997-09-23:

### Response

In line B, the expression does not exhibit undefined behavior, but because the
order of evaluation of the operands of the addition operator is not specified
and function calls do not overlap, it is unspecified whether `g` will attain the
value 1 or 2\. Lines C and A violate the quoted restriction from subclause 6.3,
so the behavior is undefined.


</div>


---

---

<div id="issue0088">

## Issue 0088: Are two incomplete structure types with a (lexically) identical tag always compatible?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0139](log_c90.md#issue0139)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_088.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_088.html)

*\[Question was revised in Dec 94]*

Item 25 \- compatibility of incomplete types

According to subclause 6.1.2.6 **Compatible type and composite type**, an
incomplete structure type is incompatible with everything except “the same
type:”

> Two types *have compatible type* if their types are the same.

The C Standard fails to define when exactly two types are “the same.” It is
intuitively clear in context of basic types and array or pointer derivation, but
becomes vague when genuinely new structure or union types are involved,
especially when they are created as incomplete types first and completed later.

a) Are two incomplete structure types with a (lexically) identical tag always
“the same” in the sense of subclause 6.1.2.6? It would appear not, unless they
are declared in the same scope of the same translation unit.

b) Can two different incomplete structure types be compatible in other ways? If
so, how?

c) Is a structure type before and after completion “the same type” in the sense
of subclause 6.1.2.6? If the answer to (c) is no, then questions (d) to (g)
apply.

d) Are the types before completion and after completion compatible?

Consider the following translation unit (the file `a.c`):

```c
 struct tag;

 int a1 (struct tag * p)
 	{ a2 (p); }		/* Line A */

 struct tag { int i; } s;

 int main ()
        {
        a1 (&s);
        return 0;
        }

 int a2 (struct tag * p)
 	{ /* ... */ }
```

e) Is the call to `a2` in line A valid? The parameter and argument types appear
to be incompatible.

f) Suppose that the definition of `a2` were moved to a separate translation
unit, preceded by a definition of `struct tag` which was compatible with the one
in the above translation unit. Would the call in line A then be valid?

g) A constraint in subclause 6.5 demands that:

> All declarations in the same scope that refer to the same object or function
> shall specify compatible types.

Does this mean that:

```c
struct tag;
 extern struct tag* p;		/* Line B */

 struct tag { int x; }
 extern struct tag* p;
```

requires a diagnostic since the two declarations of `p` specify incompatible
types? If not, what is the type `p` is declared as in Line B ?

If the answer to (c) is yes, then question (h) applies.

h) If two types `A` and `B` are compatible, is `A` compatible with all types
that are the same as `B`? For example, is the call in line D below valid? If the
redeclaration in line C is omitted, does undefined behavior result?

```c
 /* First translation unit */

 struct tag;
 int c1 (struct tag * p)
 	{ /* ... */ }

 struct tag { int i; };		/* Line C */

 /* Second translation unit */

 struct tag { int i; } s;
 int main()
        {
 	c1 (&s);		/* Line D */
        return 0;
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

a) No.

b) Yes, see the Response to [Defect Report #139](log_c90.md#issue0139).

c) Yes. The C Standard failed to make clear that the type remains the same, but
that is the obvious intent.

d) through (g) not applicable, because of the response to (c).

h) Yes, yes, and no.


</div>


---

---

<div id="issue0089">

## Issue 0089: When does multiple definitions of a macro require a diagnositc message?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_089.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_089.html)

Item 26 \- multiple definitions of macros

Consider the following code:

```c
#define macro   object_like
 #define macro(argument)        function_like
```

Does this code require a diagnostic?

The wording of subclause 6.8.3 specifies that a macro may be redefined under
certain circumstances (basically identical definitions), but does not actually
forbid any other redefinition. Thus it can be argued that the constraint in
subclause 6.8.3 is not violated, and a diagnostic is not required.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.8.3, page 89, change, in both paragraphs 2 and 3:***

may be redefined by another `#define` preprocessing directive provided that

***to:***

shall not be redefined by another `#define` preprocessing directive unless


</div>


---

---

<div id="issue0090">

## Issue 0090: Multibyte characters in formats question

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_090.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_090.html)

Item 27 \- multibyte characters in formats

Consider a locale where the characters `'\xE'` and `'\xF'` start and end an
alternate shift state (i.e., the latter reverts to the initial shift state), and
where multibyte characters whose first byte is greater than or equal to 0x80 are
two bytes long. The multibyte characters and the alternate shift state
characters are all distinct from the basic execution character set (subclause
5.2.1). What is the output generated by the following `fprintf` calls?

> ```c
>         fprintf (stdout, "Test A: (%d)\n", 42);
>         fprintf (stdout, "Test B: (\xE%d\xF)\n", 42);
>         fprintf (stdout, "Test C: (\xE%\xF" "d)\n", 42);
>         fprintf (stdout, "Test D: (\xCC%d)\n", 42);
>         fprintf (stdout, "Test E: (\xE\xCC%d\xF)\n", 42);
>         fprintf (stdout, "Test F: (\xE\xCC%\xF" "d)\n", 42);
> ```

---

Comment from WG14 on 1997-09-23:

### Response

The first call contains no locale-specific characters and must produce the
obvious output. The remainder of this response addresses the subsequent calls.

The hypothetical locale is defined such that “the multibyte characters and the
alternate shift state characters are all distinct from the basic execution
character set.” Thus the `%` character in the string literal is not the same
character as the `%` that introduces a conversion specification (subclauses
7.9.6.1 and 7.9.6.2) because it is distinct.

The C Standard says, “The format is composed of zero or more directives:
ordinary multibyte characters (not `%`), which are copied unchanged to the
output stream, ...” Therefore, the output generated by the example `fprintf`
calls is the format argument copied unchanged to the output stream. Note that
the third argument in each call to `fprintf` is not needed.


</div>


---

---

<div id="issue0091">

## Issue 0091: Does a locale with multibye characters conform?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_091.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_091.html)

Item 28 \- multibyte encodings

Does a locale with the following encoding of multibyte characters conform to the
C Standard?

The 99 characters of the basic execution character set have codes 1 to 99, in
the order mentioned in subclause 5.2.1.1 (so `'A' == 1`, `'a' == 27`, `'0' ==
53`, `'!' == 63`, `'\n' == 99`).

The extended execution character set consists of 16,256 (127 `*` 128\) two-byte
characters. For each two-byte character, the first byte is between 1 and 127
inclusive, and the second byte is between 128 and 255 inclusive.

Note that any sequence of bytes can unambiguously be broken into multibyte
characters, but the basic characters are prefixes of other characters.

---

Comment from WG14 on 1997-09-23:

### Response

The hypothetical locale described does conform to the C Standard because the
specified encoding does not violate the requirements imposed on multibyte
characters by subclause 5.2.1.2. No additional requirements are needed.


</div>


---

---

<div id="issue0092">

## Issue 0092: Are the remaining elements in a partially initalized string guaranteed to be zero?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0060](log_c90.md#issue0060)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_092.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_092.html)

Item 29 \- partial initialization of strings

Consider the following program:

```c
#include <stdio.h>

 int main (void)
        {
        char s [10] = "Hello";

        printf ("s [9] is %d\n", s [9]);
        return 0;
        }
```

Is this program strictly conforming? If so, is the value of `s[9]` guaranteed to
be zero? Subclause 6.5.7 states:

> If there are fewer initializers in a brace-enclosed list than there are members
> of an aggregate, the remainder of the aggregate shall be initialized the same as
> objects that have static storage duration.

However, the initializer is not brace-enclosed, so this clause does not apply.

---

Comment from WG14 on 1997-09-23:

### Response

See the response to [Defect Report #060](log_c90.md#issue0060).


</div>


---

---

<div id="issue0093">

## Issue 0093: Can a conforming freestanding implementation reserve identifiers?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_093.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_093.html)

Item 30 \- reservation of identifiers

Can a conforming freestanding implementation reserve identifiers? Subclause
5.1.2.1 states that only one identifier (the equivalent of `main`) is reserved
in a freestanding implementation. Subclause 7.1.3 states that certain
identifiers are reserved, even when the corresponding headers are not included.
This is a direct contradiction.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee observes that conforming freestanding implementations tend to vary
widely in the library facilities provided, and that the simple binary choice
implied by the above text is really a continuum. It also notes that it is
difficult to provide a C implementation with no reserved names (not even those
beginning with two underscores). It is therefore felt to be unreasonable to
restrict the names available to implementors of freestanding implementations
compared with hosted implementations.

The Committee notes that certain freestanding programs (such as UNIX kernels)
have tended to use names such as `exit`, but agrees that existing practice
dictates that the authors of such programs must already be prepared to change
such names when using certain compilers.

### Correction

***In subclause 5.1.2.1, page 6, delete:***

There are otherwise no reserved external identifiers.


</div>


---

---

<div id="issue0094">

## Issue 0094: Is there an inconsistency between the constraints on passing values versus returning values?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_094.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_094.html)

ANSI/ISO C Defect report #rfg1:

There appears to be an inconsistency between the constraints on “passing” values
versus “returning” values. The constraints for function calls clearly indicate
that a diagnostic is required if any given actual argument is passed (to a
prototyped function) into a corresponding formal parameter whose type is not
assignment compatible with respect to the type of the passed value. In the case
of values returned by a return statement however, there seems to be no such
compatibility constraint imposed upon the expression given in the `return`
statement and the corresponding (declared) function return type.

A new constraint should be added to the C Standard like:

> If present, the expression given in a `return` statement shall have a type such
> that its value may be assigned to an object with the unqualified version of the
> return type of the containing function.

(This exactly mirrors the existing constraint on parameter matching imposed upon
calls to prototyped functions.)

---

Comment from WG14 on 1997-09-23:

### Response

The constraint in the description of the `return` statement is unneeded. Early
on, the Committee decided that if a behavior was described as being equivalent
to another construct, all of the constraints of that construct would apply. This
“chaining” process means that any violation of a constraint in any section
referred to explicitly or by the phrases “equivalent behavior” or “as if” will
generate a diagnostic.

The **Semantics** section of the `return` statement (subclause 6.6.6.4) states:
“If the expression has a type different from that of the function in which it
appears, it is converted as if it were assigned to an object of that type.” The
constraints in the section on simple assignment (subclause 6.3.16.1) are
sufficient to assure assignment compatibility of the two types.


</div>


---

---

<div id="issue0095">

## Issue 0095: Are the initialization constraints clear?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_095.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_095.html)

ANSI/ISO C Defect report #rfg2:

There is an ambiguity with respect to the constraints which may (or may not)
apply to initializations.

Subclause 6.5.7 says:

> ... the same type constraints and conversions as for simple assignment apply,
> ...

Note however that this rule itself appears within a **Semantics** section, thus
leading some implementors to feel that no diagnostics are required in cases
where an attempt is made to provide an initializer for a given scalar and where
the type of the initializer is *not* assignment compatible with the type of the
scalar object being initialized. This ambiguity should be removed by adding an
explicit constraint to the section covering initializations, such as:

> Each scalar initializer expression given in an initializer shall have a type
> such that its value may be assigned to an object with the unqualified version of
> the corresponding scalar object to be initialized by the given scalar
> initializer expression.

(This roughly mirrors the existing constraint on parameter matching imposed upon
calls to prototyped functions.)

---

Comment from WG14 on 1997-09-23:

### Response

An explicit constraint is not required in the initializer section. Early on, the
Committee decided that if a behavior was described as being equivalent to
another construct, all of the constraints of that construct would apply. This
“chaining” process means that any violation of a constraint in any section
referred to explicitly or by the phrases “equivalent behavior” or “as if” will
generate a diagnostic.

The constraints in the section on simple assignment (subclause 6.3.16.1) are
sufficient to assure type compatibility of the object and the initializer.


</div>


---

---

<div id="issue0096">

## Issue 0096: Can the element type in an array declarator be a non-object type?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_096.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_096.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.1.2.5 does clearly state, “An *array type* describes a contiguously
allocated nonempty set of objects with a particular member object type, called
the *element type.***17**” Footnote 17 and the first paragraph of subclause
6.1.2.5 both state that object types do not include incomplete types. Nor do
object types include function types. Thus, the array element type must not be
any of the items you have listed. A diagnostic is not required. The Committee
believes that whether or not a diagnostic is produced is an issue of quality of
implementation.


</div>


---

---

<div id="issue0097">

## Issue 0097: Can the `type` argument of the `offsetof` macro be an incomplete type?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0040.06](log_c90.md#issue0040.06)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_097.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_097.html)

ANSI/ISO C Defect report #rfg4:

Subclause 7.1.6 fails to contain any constraint which would prohibit the type
argument given in an invocation of the `offsetof` macro from being an incomplete
type. This situation can arise in examples such as the following:

```c
#include <stddef.h>

 struct S
        {
        int member1;
        int member2[1+offsetof(struct S, member1)];
        };
```

I believe that a constraint prohibiting the type argument to `offsetof` from
being an incomplete type is clearly needed.

This problem could be solved by adding an explicit constraint to subclause
7.1.6, such as:

> The type argument given in an invocation of the `offsetof` macro shall be the
> name of a complete structure type or a complete union type. (Note that this way
> of expressing the constraint also makes it completely clear that diagnostics are
> required for cases where the type given in the invocation is, for instance, a
> function type, an array type, an enumerated type, a pointer type, or a built-in
> arithmetic type.)

---

Comment from WG14 on 1997-09-23:

### Response

See the response to [Defect Report #040](log_c90.md#issue0040.06), question 6\. This code
is not strictly conforming.


</div>


---

---

<div id="issue0098">

## Issue 0098: Do function types and incomplete type have size?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_098.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_098.html)

ANSI/ISO C Defect report #rfg5:

Subclause 6.3.3.4 provides the following constraint:

> The `sizeof` operator shall not be applied to an expression that has function
> type or an incomplete type...

The logical implication of this constraint is that neither function types nor
incomplete types have “sizes” per se, at least not as far as the C Standard is
concerned.

I have noted however that neither subclause 6.3.2.4 **Postfix increment and
decrement operators** nor subclause 6.3.3.1 **Prefix increment and decrement
operators** contain any constraints which would prohibit the incrementing or
decrementing of pointers to function types or pointers to incomplete types.

I believe that this logical inconsistency needs to be addressed (and rectified)
in the C Standard. It seems that the most appropriate way to do this is to add
the following additional constraint to subclause 6.3.2.4:

> The operand of the postfix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.

Likewise, the following new constraint should be added to subclause 6.3.3.1:

> The operand of the prefix increment or decrement operator shall not have a type
> which is a pointer to incomplete type or a pointer to function type.

---

Comment from WG14 on 1997-09-23:

### Response

The explicit constraint on pre/post increment/decrement operators (subclauses
6.3.2.4 and 6.3.3.1) is not required. Early on, the Committee decided that if a
behavior was described as being equivalent to another construct, all of the
constraints of that construct would apply. This “chaining” process means that
any violation of a constraint in any section referred to explicitly or by the
phrases “equivalent behavior” or “as if” will generate a diagnostic.

Both subclauses 6.3.2.4 and 6.3.3.1 state in their respective **Semantics**
sections, “See the discussions of additive operators and compound assignment for
information on constraints, types, \[side effects,] and conversions and the
effects of operations on pointers.”

The **Semantics** section of subclause 6.3.16.2 states, “A *compound assignment*
of the form `E1` *`op`*`= E2` differs from the simple assignment expression `E1
= E1` *`op`* `(E2)` only in that the lvalue `E1` is evaluated only once.”

This makes the pre/post increment/decrement equivalent to adding or subtracting
1 to/from an object. Looking at subclause 6.3.6 for the constraints on additive
operators, in each case which refers to pointer operands, the C Standard uses
the phrase “pointer to an object type.” Since incomplete types and function
types are not object types, their use as operands of these operators is
precluded.


</div>


---

---

<div id="issue0099">

## Issue 0099: What does the term *assignment operator* mean?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_099.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_099.html)

ANSI/ISO C Defect report #rfg6:

Subclause 6.2.1.5 explicitly allows an implementation to evaluate a
floating-point expression using some type which has *more* precision than the
apparent type of the expression itself:

> The values of floating operands and the results of floating expressions may be
> represented in greater precision and range than that required by the type, ...

A footnote on this rule also says explicitly that:

> The cast and assignment operators still must perform their specified
> conversions, as described in 6.2.1.3 and 6.2.1.4.

As noted in the first of these two quotes (above) some compilers (most notably
for x86 and mc680x0 target systems) may perform floating-point expression
evaluation using a type which has more precision and/or range than that of the
“apparent type” of the expression being evaluated.

The clear implication of the above rules is that compilers must sometimes
generate code to implement narrowing of floating-point expression results, when
(a) those results were generated using a format with more precision and/or range
than the “apparent type” of the expression would seem to call for, and where (b)
the expression result is the operand of a cast or is used as an operand of an
“assignment operator.”

My question is simply this: For the purposes of the above rules, does the term
“assignment operator” mean exactly (and only) those operators listed in
subclause 6.3.3.16, or should implementors and users expect that other
operations described within the C Standard as being similar to “assignment” will
also produce floating-point narrowing effects (under the right conditions)?

Specifically, may (or must) implicit floating-point narrowing occur as a result
of parameter passing if the actual argument expression is evaluated in a format
which is wider than its “apparent type?” May (or must) implicit floating-point
narrowing occur as a result of a `return` statement if the `return` statement
contains a floating-point expression which is evaluated in some format which is
wider than its “apparent type?”

Here are two examples illustrating these two questions. Imagine that these
examples will be compiled for a type of target system which is capable of
performing floating-point addition *only* on floating-point operands which are
represented in the same floating-point format normally used to hold type `long
double` operands in C:

Example 1:

```c
extern void callee ();	/* non-prototyped */
 double a, b;

 void caller ()
        {
 	callee(a+b);  /* evaluated in long double then narrowed? */
        }
```

Example 2:

```c
double a, b;

 double returner ()
        {
 	return a+b;  /* evaluated in long double then narrowed? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

A careful reading of the C Standard indicates that everything that is done “as
if by assignment” must pass through a knot-hole (be narrowed). See the following
references: subclause 6.3.16 for assignment, 6.3.2.2 for parameters, and 6.6.6.4
for return types.


</div>


---

---

<div id="issue0100">

## Issue 0100: Do functions return values by copying?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0001](log_c90.md#issue0001)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_100.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_100.html)

ANSI/ISO C Defect report #rfg7:

Subclause 6.6.6.4 **The `return`** statement says:

> If the expression has a type different from that of the function in which it
> appears, it is converted as if it were assigned to an object of that type.

This is nonsensical. The type of the containing function is a function type, and
that's different from an object type. I believe that should be changed to read:

> If the expression has a type different from that of the return type of the
> function in which it appears, it is converted as if it were assigned to an
> object having the same type as the return type of the containing function.

---

Comment from WG14 on 1997-09-23:

### Response

This error was corrected in response to [Defect Report #001](log_c90.md#issue0001).


</div>


---

---

<div id="issue0101">

## Issue 0101: Are mismatched qualifiers allowed?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_101.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_101.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

There are three questions about mismatched type qualifiers in places where
conversions “as if by assignment” takes place. Two of these are in
initialization and in function returns. A careful reading of the C Standard
shows that mismatched qualifiers are allowed in these two cases; see subclauses
6.5.7 and 6.5.3 **Semantics**.

The other issue deals with a qualifier mismatch between arguments and the
parameters of a called function. The C Standard should be modified to clarify
that such a mismatch is allowed.

### Correction

***In subclause 6.3.2.2, page 41, second paragraph, change:***

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters.

***to:***

If the expression that denotes the called function has a type that includes a
prototype, the arguments are implicitly converted, as if by assignment, to the
types of the corresponding parameters, taking the type of each parameter to be
the unqualified version of its declared type.


</div>


---

---

<div id="issue0102">

## Issue 0102: Does a constraint violation win over undefined behavior?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0017.03](log_c90.md#issue0017.03)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_102.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_102.html)

ANSI/ISO C Defect report #rfg9:

Subclause 6.5 **Constraints** says:

If an identifier has no linkage, there shall be no more than one declaration of
the identifier (in a declarator or type specifier) with the same scope and in
the same name space, except for tags as specified in 6.5.2.3.

Subclause 6.5.2.3, **Semantics** section says:

Subsequent declarations \[of a tag] in the same scope shall omit the bracketed
list.

Given that one of the above two rules appears in a **Constraints** section,
while the other appears in a **Semantics** section, it is ambiguous whether or
not diagnostics are strictly required in the following cases (in which more than
one defining declaration of each tag appears within a single scope):

```c
void example ()
        {
        struct S { int member; };
 	struct S { int member; };  /* diagnostic required? */

        union U { int member; };
 	union U { int member; };   /* diagnostic required? */

        enum E { member };
 	enum E { member };         /* diagnostic required? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

A diagnostic is required for the `struct`, `union`, and `enum` redeclarations
indicated in the question. Subclause 6.5 indicates that there must be a
diagnostic “except for tags as specified in 6.5.2.3.” In subclause 6.5.2.3, the
specified exception is for subsequent declarations that omit the bracketed list.

See also the response to [Defect Report #017, Question 3](log_c90.md#issue0017.03).


</div>


---

---

<div id="issue0103">

## Issue 0103: Is a diagnostic required when formal parameters for functions are incomplete types?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_103.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_103.html)

ANSI/ISO C Defect report #rfg10:

According to subclause 6.5:

> If an identifier for an object is declared with no linkage, the type for the
> object shall be complete by the end of its declarator, or by the end of its
> init-declarator if it has an initializer.

Note that this rule appears in a **Semantics** section, so it would seem that
comforming implementations are permitted but not strictly required to produce
diagnostics for violations of this rule.

Anyway, my interpretation of the above rule is that conforming implementations
are permitted (and even encouraged it would seem) to issue diagnostics for code
such as the following, in which formal parameters for functions (which, by
definition, have no linkage) are declared to have incomplete types:

```c
typedef int AT[];

 void example1 (int arg[]);	/* diagnostic permitted/encouraged? */
 void example2 (AT arg);		/* diagnostic permitted/encouraged? */
```

I believe that subclause 6.5 needs to be reworded so as to clarify that code
such as that shown above is perfectly valid, and that conforming implementations
should not reject such code out of hand.

---

Comment from WG14 on 1997-09-23:

### Response

The types of the parameters are rewritten, as in subclause 6.7.1 via subclause
6.5.4.3. No incomplete object types are involved.


</div>


---

---

<div id="issue0104">

## Issue 0104: When is an incomplete type in function declaration a parameter?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0084](log_c90.md#issue0084)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_104.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_104.html)

ANSI/ISO C Defect report #rfg11:

According to subclause 6.5:

> If an identifier for an object is declared with no linkage, the type for the
> object shall be complete by the end of its declarator, or by the end of its
> init-declarator if it has an initializer.

It would appear that the above rule effectly renders the following code not
strictly conforming (because this code violates the above rule):

```c
typedef struct incomplete_S ST;
 typedef union  incomplete_U UT;

 void example1(ST arg);	/* diagnostic permitted/encouraged? */
 void example2(UT arg);	/* diagnostic permitted/encouraged? */
```

I have noted however that many/most/all “conforming” implementations do in fact
accept code such as that shown above (without producing any diagnostics).

Is it the intention of the Committee that code such as that shown above should
be considered to be strictly conforming? If so, then some change to the wording
now present in subclause 6.5 is in order (to allow for such cases).

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #084](log_c90.md#issue0084).


</div>


---

---

<div id="issue0105">

## Issue 0105: Does a constraint violation win over undefined behavior?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC1  
Cross-references: [0017.03](log_c90.md#issue0017.03)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_105.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_105.html)

ANSI/ISO C Defect report #rfg12:

Subclause 6.5 says (in its **Constraints** section):

> All declarations in the same scope that refer to the same object or function
> shall specify compatible types.

However in subclause 6.1.2.6 we have the following rule:

> All declarations that refer to the same object or function shall have compatible
> type; otherwise the behavior is undefined.

There is a conflict between the meaning of these two rules. The former rule
indicates declaring something in two or more incompatible ways (in a given
scope) *must* cause a diagnostic, while the latter rule indicates that doing the
exact same thing may result in undefined behavior (i.e. possibly silent
acceptance of the code by the implementation). (Note that this same issue was
raised previously in the C Information Bulletin #1, [RFI #17, question
#3](log_c90.md#issue0017.03). While the response to that question indicated that no change
was needed, a change *is* clearly need in order to resolve this ambiguity.)

Furthermore, the use of the term “refer to” in both of these rules seems both
unnecessary and potentially confusing. Why not just talk instead about
declarations “declaring” things, rather than “referring to” those things?

To eliminate the first problem I would suggest that the rules quoted above from
subclause 6.1.2.6 should be clarified as follows:

> If any pair of declarations of the same object or function which appear in
> different scopes declare the object or function in question to have two
> different incompatible types, the behavior is undefined.

(Actually the rule regarding declaration compatibility which now appears in
subclause 6.1.2.6 seems entirely misplaced anyway. Shouldn't it just be taken
out of subclause 6.1.2.6 and moved to the subclause on declarations, i.e.
subclause 6.5?)

---

Comment from WG14 on 1997-09-23:

### Response

This error was corrected in response to [Defect Report #017, Question
3](log_c90.md#issue0017.03).


</div>


---

---

<div id="issue0106">

## Issue 0106: Can one take the address of a void expression?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0012](log_c90.md#issue0012)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_106.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_106.html)

ANSI/ISO C Defect report #rfg13:

Subclause 6.2.2.2 says:

> The (nonexistent) value of a *void expression* (an expression that has type
> `void`) shall not be used in any way, ...

There are two separate (but related) problems with this rule.

First, it is not entirely clear what constitutes a “use” of a value (or of an
expression). In which lines of the following code is a type `void` value
actually “used?”

```c
void example(void *pv, int i)
        {
 	&*pv;            /* ? */
 	*pv;             /* ? */
 	i ? *pv : *pv;   /* ? */
 	*pv, *pv;        /* ? */
        }
```

(The answer to this question will determine which of the above lines cause
undefined behavior, and which cause well defined behavior.)

If one or more of the (questionable) lines from the above example are judged by
the Committee to result in well defined behavior, then a second (separate) issue
arises. This second issue requires some explaining.

Subclause 6.2.2.1 contains the following rules:

> An *lvalue* is an expression (with an object type or an incomplete type other
> than `void`) ...
>
> Except when it is the operand of the `sizeof` operator, the unary `&` operator,
> the `++` operator, the `--` operator, or the left operand of the `.` operator or
> an assignment operator, an lvalue that does not have array type is converted to
> the value stored in the designated object (and is no longer an lvalue)... If the
> lvalue has an incomplete type and does not have array type, the behavior is
> undefined.

Note that the final rule (specifying a condition under which undefined behavior
arises) seems, based upon the context, to only apply to those cases in which
“...an lvalue that does not have an array type is converted to the value...”
More specifically, it appears that undefined behavior is *not* necessarily
produced for non-lvalue expressions (appearing in the indicated contexts).

Furthermore, it should be noted that the definition of an lvalue (quoted above)
*does not include* all void types. Rather, it only includes *the* `void` type.

The result is that the indicated lines in following example would seem to yield
well defined behavior (or at least they *will* yield well defined behavior if
the Committee decides that their unqualified counterparts do), however I suspect
that this may not have been what the Committee intended.

```c
void example(const void *pcv, volatile void *pvv, int i)
        {
 	&*pcv;              /* ? */
 	*pcv;               /* ? */
 	i ? *pcv : *pcv;    /* ? */
 	*pcv, *pcv;         /* ? */

 	&*pvv;              /* ? */
 	*pvv;               /* ? */
 	i ? *pvv : *pvv;    /* ? */
 	*pvv, *pvv;         /* ? */
        }
```

In summary, I would ask that the Committee comment upon and/or clarify the
behavior produced by each of the examples shown herein. Separately, I would
request that the Committee make changes in the existing C Standard in order to
make the rules applicable to such cases more readily apparent.

---

Comment from WG14 on 1997-09-23:

### Response

In the first function called `example`, the expression statement `&*pv` is dealt
with in [Defect Report #012](log_c90.md#issue0012). The remaining three statements are
well formed. See the last sentence of the cited reference and also subclause
6.6.3.

In the second function called `example`, the expression statements `&*pcv` and
`&*pvv` are dealt with in [Defect Report #012](log_c90.md#issue0012). The remaining six
statements are well formed. The restrictions given in subclause 6.5.3 apply to
object types, not incomplete types.


</div>


---

---

<div id="issue0107">

## Issue 0107: Several `assert` questions

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_107.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_107.html)

ANSI/ISO C Defect report #rfg14:

Subclause 7.2.1.1 (**Synopsis**) says:

> ```c
>  #include <assert.h>
>  void assert(int expression);
> ```

This synopsis raises several related questions.

a) May a strictly conforming program contain code which includes an invocation
of the `assert` macro for an expression whose type is not directly convertible
to type `int`? (See examples below.)

b) Must a conforming implementation issue diagnostics for any and all attempts
to invoke the `assert` macro for an expression having some type which is not
directly convertible to type `int`?

Examples:

```c
 #include <assert.h>

 char *cp;
 void (*fp) ();
 struct S { int member; } obj;

 void example ()
        {
 	assert (cp);	/* conforming code?  diagnostic required? */
 	assert (fp);	/* conforming code?  diagnostic required? */
 	assert (obj);	/* conforming code?  diagnostic required? */
        }
```

c) Must a conforming implementation convert the value yielded by the expression
given in an invocation of the assert macro to type `int` before checking to see
if it compares equal to zero?

Example:

```c
#include <assert.h>

 void example ()
        {
 	assert (0.1);	/* must this casue an abort?  must it NOT? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

a) The definition of `assert` depends on the `NDEBUG` macro. The **Synopsis**
provides information on how an implementation may use the parameter. If `NDEBUG`
is defined as a macro, the parameter is not used and hence cannot cause
undefined behavior. If `NDEBUG` is not defined as a macro, the implementation
may rely on the parameter having type `int`. Passing a non-`int` argument in
such a context will render the translation unit not strictly conforming.

b) If `NDEBUG` is defined as a macro, the parameter is not used and no
diagnostic should occur. Otherwise, a violation of this requirement results in
undefined behavior, which does not require a diagnostic.

c) No.


</div>


---

---

<div id="issue0108">

## Issue 0108: Is it conforming to allow macros to make keywords?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_108.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_108.html)

ANSI/ISO C Defect Report #rfg15:

Subclause 7.1.3 lists the set of reserved identifiers, but this list does not
include keywords (subclause 6.1.1).

Subclause 6.1.1 says (in a **Semantics** section):

> The above tokens (entirely in lower-case) are reserved (in translation phases 7
> and 8\) for use as keywords, and shall not be used otherwise.

Based upon the above named sections of the C Standard, I am forced to conclude
that the following code is strictly conforming. Is this a correct conclusion?

```c
#define double void
 #include <math.h>
 #undef double

 void example (double d1, double d2)
        {
        d1 = acos (d2);
        }
```

My impression is that few (if any) existing implementations now accept such
code. I am therefore inclined to believe that the Committee's true intentions
were that *all* keywords (as listed in subclause 6.1.1) should be considered to
be reserved identifiers, at least during translation phase 4, and at least while
processing `#include` directives which name standard include files provided by
the implementation (as listed in subclause 7.1.2).

I believe that the proper way to address this problem would be to add another
stipulation (regarding reserved identifiers) to subclause 7.1.2.1. This
additional stipulation might read as follows:

> If, during inclusion of any one of the standard headers listed in the preceding
> section (during translation phase 4\) any one of the keywords listed in
> subclause 6.1.1 is defined as a preprocessor macro, the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Response

This program's behavior is undefined because of the restriction on inclusion of
standard headers in subclause 7.1.2:

The program shall not have any macros with names lexically identical to keywords
currently defined prior to the inclusion.

The Committee's intention was indeed to otherwise allow macros to mask keywords.


</div>


---

---

<div id="issue0109">

## Issue 0109: Does the C Standard draw any significant distinction between *undefined values* and *undefined behavior*?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_109.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_109.html)

\[Question was revised in Jun 94.]

ANSI/ISO C Defect Report #rfg16:

Does the C Standard draw any significant distinction between “undefined values”
and “undefined behavior?” (It appears that it does, but if it does, that fact is
not always apparent.)

Just to give two examples which, it would appear, involve the generation (in a
running program) of undefined values (as opposed to totally undefined behavior
at either compile-time or link-time or run-time) I provide the following two
citations.

Subclause 6.3.8 **Relational operators**:

> If the objects pointed to are not members of the same aggregate or union object,
> the *result* is undefined,...

(Emphasis added.)

Subclause 7.5.2.1 **The `acos` function**:

> A domain error occurs for arguments not in the range \[-1,\+1].

The issue of “undefined values” versus “undefined behavior” has great
significance and importance to people doing compiler testing. It is generally
accepted that the C Standard's use of the term “undefined behavior” is meant to
imply that absolutely *anything* can happen at any time, e.g. at compile-time,
at link-time, or at run-time. Thus, people testing compilers must either totally
avoid writing test cases which involve any kind of “undefined behavior” or else
they must treat any such test cases which they *do* write as strictly “quality
of implementation” tests which may validly cause errors at compile-time, at
link-time, or at run-time.

If however the C Standard recognizes the separate existence of “undefined
values” (whose mere creation *does not* involve wholly “undefined behavior”)
then a person doing compiler testing could write a test case such as the
following, and he/she could also expect (or possibly demand) that a conforming
implementation should, at the very least, compile this code (and possibly also
allow it to execute) without “failure.”

```c
 int array1[5];
 int array2[5];
 int *p1 = &array1[0];
 int *p2 = &array2[0];

 int foo()
        {
        int i;
 	i = (p1 > p2);  /* Must this be "successfully translated"? */
 	1/0;             /* Must this be "successfully translated"? */
        return 0;
        }
```

So the bottom line question is this: Must the above code be “successfully
translated” (whatever that means)? (See the footnote attached to subclause
5.1.1.3.)

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard uses the term “indeterminately valued” not “undefined value.” Use
of an indeterminate valued object results in undefined behavior.

The footnote to subclause 5.1.1.3 points out that an implementation is free to
produce any number of diagnostics as long as a valid program is still correctly
translated.

If an expression whose evaluation would result in undefined behavior appears in
a context where a constant expression is required, the containing program is not
strictly conforming. Furthermore, if *every* possible execution of a given
program would result in undefined behavior, the given program is not strictly
conforming.

A conforming implementation must not fail to translate a strictly conforming
program simply because *some* possible execution of that program would result in
undefined behavior. Because `foo` might never be called, the example given must
be successfully translated by a conforming implementation.


</div>


---

---

<div id="issue0110">

## Issue 0110: When is a formal parameter having array-of-non-object type not conforming?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0013.01](log_c90.md#issue0013.01), [0017.14](log_c90.md#issue0017.14), [0017.15](log_c90.md#issue0017.15), [0047](log_c90.md#issue0047)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_110.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_110.html)

ANSI/ISO C Defect report #rfg17:

Subject: Formal parameters having array-of-non-object types.

a) For which (if any) of the following function declarations and definitions is
a diagnostic required?

b) Which (if any) of the following function declarations and definitions would,
if present in a translation unit, render the translation unit not strictly
conforming?

```c
typedef void VT;
 typedef struct incomplete_S ST;
 typedef union  incomplete_U UT;
 typedef int AT[];
 typedef void (FT) ();

 void declaration1 (VT arg[]);		/* ? */
 void declaration2 (ST arg[]);		/* ? */
 void declaration3 (UT arg[]);		/* ? */
 void declaration4 (AT arg[]);		/* ? */
 void declaration5 (FT arg[]);		/* ? */

 void definition1 (VT arg[]) { }	/* ? */
 void definition2 (ST arg[]) { }	/* ? */
 void definition3 (UT arg[]) { }	/* ? */
 void definition4 (AT arg[]) { }	/* ? */
 void definition5 (FT arg[]) { }	/* ? */
```

Footnote: I have heard rumors that the issue of the exact timing of the decay of
a formal parameter's array type into a pointer type (relative to the timing of
the necessary check that the type of the formal parameter is in fact a valid
type) was determined *explicitly* to be undefined by the Committee, but there is
no record of this in the CIB #1 document I have. \[CIB #1 is X3J11's earlier
attempt to respond to Defect Reports #001-#035, then called Requests for
Interpretation #001-#035.]

References: CIB #1, [RFI #13, question #1](log_c90.md#issue0013.01); CIB #1, [RFI #17,
question #14](log_c90.md#issue0017.14); CIB #1, [RFI #17, question #15](log_c90.md#issue0017.15)

---

Comment from WG14 on 1997-09-23:

### Response

No diagnostics are required for any of the above declarations. Each of the
function declarations and definitions would render the translation unit not
strictly conforming. See also [Defect Report #047](log_c90.md#issue0047).


</div>


---

---

<div id="issue0111">

## Issue 0111: A question on conversion of *pointer-to-qualified* type values to type `(void*)` values

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_111.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_111.html)

ANSI/ISO C Defect report #rfg18:

Subject: Conversion of pointer-to-qualified type values to type `(void*)`
values.

Does the following code involve usage which requires a diagnostic from a
standard conforming implementation?

```c
const char *ccp;
 void *vp;

 void test ()
        {
 	vp = ccp;	/* diagnostic required? */
        }
```

With respect to this example, the following quotations are relevant.

Subclause 6.2.2.3:

> A pointer to `void` may be converted to or from a pointer to any incomplete or
> object type.

Subclause 6.3.16.1 (**Constraints**):

> One of the following shall hold:
>
> ...
>
> \- both operands are pointers to qualified or unqualified versions of compatible
> types, and the type pointed to by the left has all the qualifiers of the type
> pointed to by the right;
>
> \- one operand is a pointer to an object or incomplete type and the other is a
> pointer to a qualified or unqualified version of `void`, and the type pointed to
> by the left has all the qualifiers of the type pointed to by the right; ...

The rule specified in subclause 6.2.2.3 (and quoted above) makes it unclear
whether a value of some pointer-to-qualified-object type may be *first*
implicitly converted to type `(void*)` and then assigned to a type `(void*)`
variable, or whether such implicit conversion only takes place as an integral
part of an otherwise valid assignment operation.

If the former interpretation of subclause 6.2.2.3 is correct, then the above
code example is valid, and no diagnostic is required. If, however, the latter
interpretation is the correct one, then the code example shown above fails to
meet the constraints of subclause 6.3.16.1, and (thus) a diagnostic is required.

---

Comment from WG14 on 1997-09-23:

### Response

The constraint in subclause 6.3.16.1 takes precedence over subclause 6.2.2.3;
therefore a diagnostic is required. Note that the above quote from subclause
6.2.2.3 is incomplete and taken out of context.


</div>


---

---

<div id="issue0112">

## Issue 0112: A Null pointer constants and relational comparison question

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_112.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_112.html)

ANSI/ISO C Defect report #rfg19:

Subject: Null pointer constants and relational comparisons.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
void test (void *vp)
        {
 	(vp > (void*)0);	/* ? */
        }
```

Background:

Subclause 6.2.2.3:

> An integral constant expression with the value 0, or such an expression cast to
> type `void *`, is called a *null pointer constant.* If a null pointer constant
> is assigned to or compared for equality to a pointer, the constant is converted
> to a pointer of that type.

This last paragraph of subclause 6.2.2.3 seems to suggest that zero-valued
integral constant expressions which are cast to `void *` (and then called null
pointer constants) can *only* be used in assignments and/or equality
comparisons, but not in relational comparisons.

(It was probably the Committee's intent to permit such expression to be used in
all ways, and in all contexts where any other kind of `void *` non-lvalued
expressions can be used, but the current wording of subclause 6.2.2.3 does not
make that fact altogether apparent and unambiguous.)

---

Comment from WG14 on 1997-09-23:

### Response

The code does not require a diagnostic but has undefined behavior, so it renders
the translation unit not strictly conforming. Subclause 6.3.8 makes clear that
this behavior is undefined.


</div>


---

---

<div id="issue0113">

## Issue 0113: Return expressions in functions declared to return qualified `void` questions

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_113.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_113.html)

ANSI/ISO C Defect report #rfg20:

Subject: Return expressions in functions declared to return qualified `void`.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
volatile void func0 (volatile void *vvp)
        {
 	return *vvp;	/* ? */
        }

 const void func1 (const void *cvp)
        {
 	return *cvp;	/* ? */
        }
```

Background:

Subclause 6.6.6.4 (**Constraints**):

> A `return` statement with an expression shall not appear in a function whose
> return type is `void`.

Note that this constraint doesn't say anything about functions declared to
return some qualified version of the `void` type.

I believe that it was probably the Committee's true intent to require a
diagnostic for any attempt to specify an expression in a return statement within
any function declared to return *any* qualified or unqualified version of the
`void` type (and indeed, many existing implementations do already issue
diagnostics for usage such as that shown in the example above). Thus, it would
seem appropriate for the Committee to amend the above quoted constraint (from
subclause 6.6.6.4) to read:

> A `return` statement with an expression shall not appear in a function whose
> return type is a void type.

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes, a diagnostic is required.

b) Yes, this renders the program not strictly conforming code.

A qualified `void` function return type is disallowed by the constraints of
subclause 6.7.1:

> The return type from a function shall be `void` or an object type other than
> array.

The constraint does not say “a void type” and thus `void` must not be qualified
when used as a function return type. Since a qualified `void` return type is
already invalid, there is no need for the additional constraint on the `return`
statement (subclause 6.6.6.4).


</div>


---

---

<div id="issue0114">

## Issue 0114: Initialization of multi-dimensional `char` array object questions

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_114.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_114.html)

ANSI/ISO C Defect Report #rfg21:

Subject: Initialization of multi-dimensional `char` array objects.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
char array2[2][5] = { "defghi" };	/* ? */
```

Background:

Subclause 6.5.7 (**Constraints**):

> There shall be no more initializers in an initializer list than there are
> objects to be initialized.

Subclause 6.5.7:

> An array of character type may be initialized by a character string literal,
> optionally enclosed in braces.

Subclause 6.5.7 (examples):

> ... It defines a three-dimensional array object; ...

It appears that many existing compilers seem to feel the the code example shown
above violates the “no more initializers” constraint (quoted above) which is
given in subclause 6.5.7.

Note however that the *entire* two-dimensional array object being initialized
consists of exactly 2\*5 \= 10 individual `char` objects, whereas the
initializer itself only consists of 7 individual `char` values (if one counts
the terminating null byte). Thus, it would appear that these existing
implementations are in fact *wrong* in rejecting the above code, and that such
usage is in fact strictly conforming.

I ask the Committee to unambiguously either confirm or refute that position.

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes, a diagnostic is required.

b) Yes, this renders the program not strictly conforming.

Note that initialization of an array of character type by a string literal is a
special case, described in subclause 6.5.7.

The phrases “two-dimensional array” and “three-dimensional array” are merely
used for convenience. The **Semantics** section on array declarators (subclause
6.5.4.2) and the syntax specification in the section on declarations (subclause
6.5.4) clearly show that array types must be declared with one index. Thus, an
array which has two indices must be considered an “array of array of type.”

Since this is the case, the **Semantics** description for initializing
aggregates and subaggregates in subclause 6.5.7 applies. This description states

> If the initializer of a subaggregate or the first member of the contained union
> begins with a left brace, the initializers enclosed by that brace and its
> matching right brace initialize the members of the subaggregate or the first
> member of the contained union.

Thus, in the example, the string must be applied only to the first element of
the two-element array (which is an array of 5 characters). Since the initializer
contains 6 characters, it violates the constraint of the same section which
states:

> There shall be no more initializers in an initializer list than there are
> objects to be initialized.


</div>


---

---

<div id="issue0115">

## Issue 0115: What it means to *declare* a declarator?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_115.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_115.html)

ANSI/ISO C Defect Report #rfg22:

Subject: Member declarators as declarators.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
 struct { int mbr; };   /* ? */
 union  { int mbr; };   /* ? */
```

Background:

Subclause 6.5 (**Constraints**):

> A declaration shall declare at least a declarator, a tag, or the members of an
> enumeration.

It is not entirely clear what it means to “declare” a declarator. Neither is it
clear whether or not a declarator for a member should be considered to satisfy
the constraint quoted above. (Many existing implementations behave as if member
declarators *do not* satisfy the constraint.)

---

Comment from WG14 on 1997-09-23:

### Response

The Committee agrees that the quoted constraint can be read either way. Hence, a
diagnostic is not required, but a program that uses such a form has undefined
behavior. In the case of an aggregate, the intent was to require a tag or
declarator for the aggregate itself. Thus, it is not unreasonable to issue a
diagnostic for the given example. However, since the constraint can be read
either way, an implementation could actually compile such a case though it is
marginally useful at best.


</div>


---

---

<div id="issue0116">

## Issue 0116: Is a diagnostic required when the address of a `reigister` arry is implicitly taken?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0017.06](log_c90.md#issue0017.06)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_116.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_116.html)

ANSI/ISO C Defect Report #rfg23:

Subject: Implicit unary `&` applied to register arrays.

a) Does the following code involve usage which requires a diagnostic from a
conforming implementation?

b) Does the following code involve usage which renders the code itself not
strictly conforming?

```c
void example ()
        {
        register int array[5] = 0;

 	array;     /* ? */
 	array[3];  /* ? */
 	array+3;   /* ? */
        }
```

Background:

Subclause 6.5.1 (footnotes):

> The implementation may treat any `register` declaration simply as an `auto`
> declaration. However whether or not addressable storage is actually used, the
> address of any part of an object declared with storage-class specifier
> `register` may not be computed, either explicitly (by use of the unary `&`
> operator as discussed in 6.3.3.2) or implicitly (by converting an array name to
> a pointer as discussed in 6.2.2.1). Thus the only operator that can be applied
> to an array declared with storage-class specifier `register` is `sizeof`.

This footnote, while offering guidance, doesn't really answer the question of
whether or not an implementation is required to issue a diagnostic for the case
where the address of a register array is implicitly taken (as discussed in
subclause 6.2.2.1). Nor does it definitively answer the question of whether such
code should be considered to be strictly conforming or not.

(Reference: CIB #1, [RFI #17, question #6](log_c90.md#issue0017.06).)

---

Comment from WG14 on 1997-09-23:

### Response

a) No, a diagnostic is not required.

b) Yes, this renders the program not strictly conforming.


</div>


---

---

<div id="issue0117">

## Issue 0117: Abstract semantics, sequence points, and expression evaluation question

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_117.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_117.html)

ANSI/ISO C Defect Report #rfg24:

Subject: Abstract semantics, sequence points, and expression evaluation.

Does the following code involve usage which renders the code itself not strictly
conforming?

```c
int example ()
        {
        int x1 = 2, x2 = 1, x_temp;

        return (x_temp = x1, x_temp) + (x_temp = x2, x_temp);
        }
```

Background:

Subclause 5.1.2.3:

> The semantic descriptions in this International Standard describe the behavior
> of an abstract machine in which issues of optimization are irrelevant.

Subclause 6.3:

> Between the previous and next sequence point an object shall have its stored
> value modified at most once by the evaluation of an expression.

Although it is quite clear that the above quoted “modified at most once” rule
was intended to render certain programs “not strictly conforming,” there is an
unfortunate amount of ambiguity built into the current wording of that rule.

Quite simply, while the “modified at most once” rule is obviously telling us
what a “strictly conforming program” must not do between two particular points
*in time,* it is altogether less than clear what events and/or actions (exactly)
are associated with these two points in time. Additionally, it is also less than
clear (from reading the remainder of the C Standard) what actions and/or events
are allowed (or required) to take place between some pair of sequence points in
cases where both members of the pair are part of some large single expression
whose evaluation order is not completely dictated by the C Standard.

Note that despite the assertion given in subclause 5.1.2.3 (and quoted above)
the C Standard does not *fully* specify the behavior of the “abstract machine,”
especially when it comes to the issue of the ordering of sub-expression
evaluation used by the “abstract machine” model.

This fact makes it inherently impossible to precisely determine even just the
*relative* timings of various events (including the “occurrence” of or the
“execution” of or the “evaluation” of sequence points) which may (or must) occur
sometime during the evaluation of a larger containing expression (except in a
few cases involving `||` or `&&` or `?:` or `,` operators).

To put it more plainly, if some pair of sequence points will be “reached” (or
“evaluated” or “executed”) during the evaluation of any pair of subexpressions
which are themselves operands for some binary operator (other than the operators
`||` or `&&` or `?:` or `,`) then the C Standard's description of the “abstract
machine” semantics are inadequate to enable us to know either which *order*
these two sequence points will occur in, or even which other aspects of the
evaluation of the overall expression may (or must) occur “between” the two
sequence points.

Thus, it seems that it may also be inherently impossible to know whether or not
the prohibition against multiple modifications of a given variable “between” two
consecutive sequence points is (or may be) violated in such contexts.

Here is a simple example of an expression which illustrates these points:

> ```c
>         (x = i, x) + (x = j, x)
> ```

In this expression there are two “comma” sequence points; however, nothing in
the C Standard gives any indication as to which of these two may be (or must be)
“evaluated” or “reached” first. (Indeed, it would seem that on a parallel
machine of some sort, *both* points could perhaps be reached simultaneously.) It
is fairly clear however that each of the references to the stored values of `x`
must not be evaluated until their respective preceding “comma sequence points”
have been “reached” or “evaluated.” Thus, a partial (but very incomplete)
ordering is imposed upon the sequence of events which must occur during the
evaluation of this expression.

For the sake of this example, let us call the leftmost comma in the above
expression “lcomma” and call the rightmost comma “rcomma.” Given this
terminology, it would appear that the C Standard permits the following sequence
of events during evaluation of the above expression:

> ```c
>         eval(i)
>         x=          (leftmost assignment to x)
>         lcomma      <==== sequence point
>         eval(x)     (leftmost reference to stored value of x)
>         eval(j)
>         x=          (rightmost assignment to x)
>         rcomma      <==== sequence point
>         eval(x)     (rightmost reference to stored value of x)
>         +
> ```

Note that in this (very realistic) example, the stored value of `x` is *never*
modified more than once between any pair of sequence points. Given that the
ordering described above is both a perfectly *plausible* and also a perfectly
*permissible* ordering for the evaluation of the expression in question, and
given that this particular permissible ordering of events does not violate the
“modified at most once” rule (quoted earlier) it therefore appears that the
expression in question may in fact be interpreted as being “strictly
conforming,” and that such expressions may appear within “strictly conforming”
programs.

I would like the Committee to either confirm or reject this view, and to provide
some commentary explaining that confirmation or rejection.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard does not forbid an implementation from interleaving the
subexpressions in the given example as specified above. Similarly, there is no
requirement that an implementation use this particular interleaving. It is
irrelevant that one particular interleaving yields code that properly delimits
multiple modifications of the same object with sequence points. Any program that
depends on this particular interleaving is depending on unspecified behavior,
and is therefore not strictly conforming.


</div>


---

---

<div id="issue0118">

## Issue 0118: When is the `sizeof` an enumeration type known?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0013.05](log_c90.md#issue0013.05)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_118.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_118.html)

ANSI/ISO C Defect Report #rfg25:

Subject: Completion point for enumerated types.

Are diagnostics required for the following code examples?

```c
enum E1 { enumerator1 = sizeof (enum E1) };
 enum E2 { enumerator2 = sizeof (enum E2 *) };
```

(Just read on! This *isn't* just the same old question again!)

Background:

Subclause 6.3.3.4 (**Constraints**):

> The `sizeof` operator shall not be applied to an expression that has function
> type or an incomplete type, to the parenthesized name of such a type, ...

Subclause 6.5.2.1 (**Semantics**):

> The \[structure or union] type is incomplete until after the `}` that terminates
> the list \[of member declarations].”

(Bracketed portions added for clarity.)

CIB #1, RFI #13, response to question #5:

> For the example:
>
> > ```c
> > enum e { a = sizeof(enum e) };
> > ```
>
> the relevant citations are subclause 6.1.2.1 starting on page 21, line 39,
> indicating that the scope of the first `e` begins at the `{`, and subclause
> 6.5.2.2, page 62, line 20, which attributes meaning to a later `enum e` *only
> if* this use appears in a *subsequent* declaration. By subsequent, we mean
> “after the `}`.” Because in this case, the second `enum e` is not in a
> subsequent declaration, and no other wording in the C Standard addresses the
> meaning, the C Standard has left this example in the category of undefined
> behavior.

Please note that the above response to RFI #13, question #5 has totally failed
to solve the *real* problem with the current wording of the C Standard.

The *real* problem is that (unlike the case for structure and union type
definitions) nothing in the C Standard presently indicates where (or whether) an
enumerated type becomes “completed.”

This is a very serious flaw in the current C Standard. Given that the C Standard
currently contains no statement(s) which specify where (or whether) an
enumerated type becomes a “completed” type, any and all programs which use *any*
enumerated type in *any* context requiring a completed type are, by definition,
*not* strictly conforming. (This will come as quite a shock to a number of C
programmers!)

I feel that the Committee must resolve this serious problem as soon as possible.
The only plausible way to do that is to add a statement to subclause 6.5.2.2
which will specify the point at which an enum type become a “completed” type.

Using the statement currently given in subclause 6.5.2.1 (relating to struct and
union types) as a guide, it would appear that subclause 6.5.2.2 should be
amended to include the following new semantic rule:

> The enum type is incomplete until after the `}` that terminates the list of
> enumerators.

Some such addition is obviously necessary in order to render enum types usable
as complete types within strictly conforming programs.

Note however that such a clarification would have the additional (beneficial?)
side effect of rendering the following declaration subject to a mandatory
diagnostic (due to the violation of the constraints for the operand of the
`sizeof` operator):

```c
enum E1 { enumerator1 = sizeof (enum E1) };
```

Even after such a clarification however, the status of:

```c
enum E2 { enumerator2 = sizeof (enum E2 *) };
```

is still questionable at best, and the proper interpretation for such a case
should, I believe, still be drawn from the response given to [RFI #13, question
#5](log_c90.md#issue0013.05); i.e., such examples should be viewed as involving undefined
behavior.

---

Comment from WG14 on 1997-09-23:

### Response

No, diagnostics are not required. The following Correction clarifies the intent.
Note than an implementation *may* complete the type *before* the `}`.

### Correction

***In subclause 6.5.2.2, page 61, append to Semantics:***

The enumerated type is complete at the `}` that terminates the list of
enumerator declarations.


</div>


---

---

<div id="issue0119">

## Issue 0119: Is a diagnostic required on an example of an initialization of multi-dimensional array objects

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_119.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_119.html)

ANSI/ISO C Defect Report #rfg26:

Subject: Initialization of multi-dimensional array objects.

a) Is a diagnostic required for the following declaration?

b) Is the following declaration strictly conforming or not?

```c
static int array[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9  } };
```

Background:

Subclause 6.5.7 (**Semantics**):

> If an array of unknown size is initialized, its size is determined by the number
> of initializers provided for its elements.

Subclause 6.5.7 (**Semantics**):

> If the aggregate contains members that are aggregates or unions, or if the first
> member of a union is an aggregate or union, the rules apply recursively to the
> subaggregates or contained unions.

On the basis of the above quoted rules, one might conclude that the code example
given above is strictly conforming. (Many existing implementations seem to
disagree, however.)

---

Comment from WG14 on 1997-09-23:

### Response

a) No, a diagnostic is not required. It is a semantic requirement that array
elements must be objects, not a constraint.

b) No, this is undefined behavior. Note that `array` does not have an array type
because its element type is not an object type; hence subclause 6.5.7 does not
apply. See subclause 6.1.2.5.


</div>


---

---

<div id="issue0120">

## Issue 0120: Semantics of assignment to (and initialization of) bit-fields question

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_120.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_120.html)

ANSI/ISO C Defect Report #rfg27:

Subject: Semantics of assignment to (and initialization of) bit-fields.

a) Is the following program strictly conforming?

b) Must a conforming implementation translate this code into an executable
program which prints `3 3`?

```c
#include <stdio.h>

 struct S { unsigned bit:1; };
 struct S object1 = { 3 };	/* ? */
 struct S object2;

 int main ()
        {
 	object2.bit = 3;	/* ? */
        printf ("%d %d\n", object1.bit, object2.bit);
        return 0;
        }
```

Background:

Subclause 6.3.16.1 (**Semantics**):

> In *simple assignment* (`=`), the value of the right operand is converted to the
> type of the assignment expression and replaces the value stored in the object
> designated by the left operand.

Subclause 6.2.1.2 (**Semantics**):

> When a value with integral type is converted to another integral type, if the
> value can be represented by the new type, its value is unchanged.

Unless I'm mistaken, the type of the assignment expression:

> ```c
>         object2.bit = 3;
> ```

in the above example is type `unsigned int`. Thus, according to the rules quoted
here, the value of `3` is converted to an `unsigned int` type value (during this
assignment statement) and it is otherwise unchanged. Then, *that value* of 3
replaces the previous value of `object2.bit`.

I believe that the above examples illustrate the point that the C Standard
currently fails to adequately describe the semantics of assignments to (and/or
initializations of) bit-fields in cases where the value being assigned will not
actually fit into the bit-field object.

In lieu of any description of the special semantics of assignments to bitfields,
it appears to be currently *necessary* for both implementors and users to assume
that the “normal” assignment semantics apply, but as you can see from the above
examples, such assumptions lead to highly counterintuitive expectations (and to
expectations which fly in the face of actual current common practice).

I believe that the Committee should rectify the current unfortunate situation by
adding to subclause 6.3.16.1 (or maybe to subclause 6.2.1.2) some additional new
verbage explicitly describing the special semantics of assignments to
bit-fields.

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 6.5.2.1 states “A bit-field is interpreted as an integral type
consisting of the specified number of bits.” Thus the type of `object1.bit` and
`object2.bit` can be informally described as `unsigned int : 1`. A larger
integer is converted to this type according to the rules in subclause 6.2.1.2.
Thus the value 3 is converted to the value 1\.

The program is strictly conforming. It prints `1 1`.


</div>


---

---

<div id="issue0121">

## Issue 0121: What is ment by *size required* when convering a ponter value to an integral type?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_121.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_121.html)

ANSI/ISO C Defect Report #rfg28:

Subject: Conversions of pointer values to integral types.

Subclause 6.3.4 (**Semantics**):

> A pointer may be converted to an integral type. The size of integer required and
> the result are implementation-defined. If the space provided is not long enough,
> the behavior is undefined.

This passage is worded rather ambiguously.

In the first place, it talks about “The size of the integer required....”
Required by whom? Required by what? I can't tell.

Also, I get the feeling that the way this passage reads, an implementation might
permit conversions of pointers to types `char`, `short`, and `int` (with
implementation defined semantics) while *disallowing* conversions of pointers to
type `long`! (Of course that would be highly counterintuitive.)

Here is a suggested replacement for the above passage:

The value of any pointer expression whose `sizeof`, if computed, would be *N,*
may be converted (via a cast) to any integral type whose `sizeof` is *N* or
greater. The values resulting from such conversions are implementation-defined.

If an attempt is made to convert (via a cast) the value of a pointer expression
whose `sizeof`, if computed, would be *N,* to some integral type whose `sizeof`
is less than *N,* the behavior is undefined.

This is simply a more precise (and accurate) way of saying exactly what was
(obviously) intended.

---

Comment from WG14 on 1997-09-23:

### Response

The “size required” is that required by the implementation. The words “If the
space provided is not long enough” make it clear that it is the size of the type
that is relevant, and means that any type that is at least as long as the type
of the “size required” is also acceptable. The size required need not be related
to the result of `sizeof` applied to the expression.


</div>


---

---

<div id="issue0122">

## Issue 0122: Is the *type* of a bit-field totally independent from its *width*?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0015](log_c90.md#issue0015)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_122.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_122.html)

ANSI/ISO C Defect Report #rfg29:

Subject: Conversion/widening of bit-fields.

Must the following program print `1` or `0`?

```c
#include <stdio.h>

 struct S { unsigned bit:1; } object = { 1 };

 int main ()
        {
        printf ("%d\n", ((object.bit - 2) < 0));
        return 0;
        }
```

(At least one existing implementations prints `1` while another prints `0`.)

Background:

Subclause 6.2.1.1:

> A `char`, a `short int`, or an `int` bit-field, or their signed or unsigned
> varieties, or an enumeration type, may be used in an expression wherever an
> `int` or `unsigned int` may be used. If an `int` can represent all values of the
> original type, the value is converted to an `int`; otherwise it is converted to
> an `unsigned int`.

The key phrase here is “the original type.”

In effect, I am asking if the *type* of a bit-field is totally independent from
its *width* for the purposes of the above rule.

If the answer to that question is “yes,” then the value of `object.bit` must be
considered to be an `unsigned int` (with a value of `1U`). In that case, the
value `2` used in the above example must also be converted to type `unsigned
int` and then the subtraction should be carried out on the two `unsigned int`
values. The subtraction should then itself yield a value of type `unsigned int`
which is itself (by definition) \>\= 0, so it would seem that the C Standard
requires the above program to print `0`.

Is that correct? If so, perhaps the wording of the above paragraph needs to be
improved so as to make the correct interpretation of these rules more apparent
to implementors.

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #015](log_c90.md#issue0015). “The original type” applies to both width
and signedness. `object.bit` promotes to `int`, and the program prints `1`.


</div>


---

---

<div id="issue0123">

## Issue 0123: “*Type categories*” and qualified types question

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_123.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_123.html)

ANSI/ISO C Defect Report #rfg30:

Subject: “Type categories” and qualified types.

a) Is the following code strictly conforming?

b) Must a conforming implementation correctly translate the following code?

```c
enum E1 { enumerator1 = (const int) 9 };	/* ? */
 enum E2 { enumerator2 = (volatile int) 9 };	/* ? */
```

Background:

Subclause 6.5.2.2 (**Constraints**):

> The expression that defines the value of an enumeration constant shall be an
> integral constant expression that has a value representable as an `int`.

Subclause 6.4 (**Semantics**):

> Cast operators in an integral constant expression shall only convert arithmetic
> types to integral types, ...

Subclause 6.1.2.5:

> The type `char`, the signed and unsigned integer types, and the enumerated types
> are collectively called *integral types.*

Subclause 6.1.2.5:

> Any type so far mentioned mentioned is an unqualified type. Each *unqualified
> type* has three corresponding *qualified versions* of its type: ... The
> qualified or unqualified versions of a type are distinct types that belong to
> the same type category ...

The problem is with the term “type category.” I have been unable to find any
actual definition of this term in the C Standard. My assumption is that
*integral types* constitute one such “type category,” but it would be nice to
have the Committee's assurances about this. More specifically, I think that it
would be advisable to add a statement somewhat like the following one just after
the first paragraph in subclause 6.1.2.5:

> In addition to the partitioning of types into *object types, function types,*
> and *incomplete types,* each type is also said to belong to some *type
> category.* The *type categories* are *integral types, floating types, pointer
> types, structure types, union types, array types, void types,* and *function
> types.*

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes.

b) Yes.

As stated in subclause 6.5.3, “The properties associated with qualified types
are meaningful only for expressions that are lvalues.” The definition of “type
category” is given in subclause 6.1.2.5, in the paragraph preceding your last
citation.


</div>


---

---

<div id="issue0124">

## Issue 0124: What is the difference between casts to *a void type* versus casts to the `void` type?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_124.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_124.html)

ANSI/ISO C Defect Report #rfg31:

Subject: Casts to “a void type” versus casts to “the `void` type.”

Must a conforming implementation issue a diagnostic for the following code?

```c
void example ()
        {
 	(const volatile void) 0;	/* diagnostic required? */
        }
```

Background:

Subclause 6.3.4 (**Constraints**):

> Unless the type name specifies void type, the type name shall specify qualified
> or unqualified scalar type and the operand shall have scalar type.

Note that this constraint is *not* specific about whether a qualified void type
is permitted in a cast or not; i.e. it should say either “a void type” or else
say “the `void` type.”

A quick check of several existing implementations seems to indicate that a
majority of implementors have assumed that any void type (however qualified) is
acceptable in a cast. Therefore it would seem prudent for the Committee to
clarify the above quoted rule by changing “void type” to “a `void` type.”

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.3.4, page 45, change the paragraph under Constraints:***

Unless the type name specifies void type, the type name shall specify qualified
or unqualified scalar type and the operand shall have scalar type.

***to:***

Unless the type name specifies a void type, the type name shall specify
qualified or unqualified scalar type and the operand shall have scalar type.


</div>


---

---

<div id="issue0125">

## Issue 0125: When are declarations useing `extern` *(qualified)* `void` not conforming?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0012](log_c90.md#issue0012)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_125.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_125.html)

ANSI/ISO C Defect Report #rfg32:

Subject: Using things declared as “`extern` (qualified) `void`.”

May a conforming implementation fail to correctly translate a translation unit
containing the following declarations?

```c
extern const void etext;
 const void *vp = &etext;
```

Background:

[Defect Report #012](log_c90.md#issue0012) discusses at length the issue of applying unary
`&` to an expression whose type is some void type. The conclusion of that
discussion seem to be that although unary `&` *may not* be applied to an
expression having *the* `void` type (because such expressions are not lvalues)
it *is* permissible to apply unary `&` to an expression whose type is some
qualified version of `void`. The text of the interpretation for [Defect Report
#012](log_c90.md#issue0012) even goes so far as to actively recommend the practice of
declaring things to be `extern` and to have some qualified void type (so that
the address may then be taken).

The question raised herein is a different one. Tom Pennello has pointed out the
following rule from the second **Semantics** paragraph of subclause 6.7:

> If an identifier declared with external linkage is used in an expression (other
> than as part of the operand of a `sizeof` operator), somewhere in the entire
> program there shall be exactly one external definition for the identifier; ...

Thus, as Tom has noted, applying unary `&` to an entity declared to be both
`extern` and of some qualified void type is a “use” of that entity which would
necessarily force you to supply a definition of that entity, somewhere in the
program. But as Tom has further noted, there is simply no way to accomplish that
(in a strictly conforming program) because of the following rule (given in
subclause 6.5):

> All declarations ... that refer to the same object or function shall specify
> compatible types.

Thus, if you either define or fail to define `etext`, it would appear that the
behavior is undefined. Is this a correct interpretation?

(Footnote: It would appear that a strictly conforming program may contain a mere
declaration of an `extern` entity whose type is any qualified or unqualified
void type, but that any use of such an entity within an expression, other than
within a `sizeof` expression, renders the program not strictly conforming.)

---

Comment from WG14 on 1997-09-23:

### Response

Applying `&` to an identifier of type `const void` has undefined behavior. Thus
an implementation can define any semantics it wishes. A strictly conforming
program cannot contain such a construct.


</div>


---

---

<div id="issue0126">

## Issue 0126: What does *synonym* mean with respect to typedef names?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_126.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_126.html)

ANSI/ISO C Defect Report #rfg33:

Subject: What does “synonym” mean with respect to typedef names?

Given the declarations:

```c
typedef int *IP;
 const IP object;
```

what is the type of `object`?

Background:

Subclause 6.5.6 says:

> A `typedef` declaration does not introduce a new type, only a synonym for the
> type so specified.

At least one person has wondered aloud about the true meaning of this rule.

Note that if the name `IP` in the above example is expanded as if it were a mere
macro, then the type of `object` would be `(const int *)`. But essentially all
existing implementations act as if there were some sort of magical parsing
precedence (or extra parenthesization) which causes the `IP` (when used in the
second line of the example above) to be treated as a single type, to which the
`const` qualifier is applied (after the fact) thus resulting in `object` having
type `(int * const)` rather than `(const int *)`.

While this treatment is well known to experienced implementors and users, it
appears that the C Standard doesn't really explain it very well (or very
precisely). I consider this to be a defect in the C Standard, worthy of the
Committee's attention.

---

Comment from WG14 on 1997-09-23:

### Response

A `typedef` introduces a name for a type. This is not a macro, and the type must
indeed be “magically parenthesized.” In

```c
 typedef int *ip;
 ip x;
 const ip y;
```

the type of `x` is *pointer to* `int`, and the type of `y` is `const` *pointer
to* `int`. This is exactly analogous to the fact that

```c
 ip x1, x2;
```

declares both `x1` and `x2` as having the type *pointer to* `int`, and is not to
be read as

```c
 int *x1, x2;
```


</div>


---

---

<div id="issue0127">

## Issue 0127: What is the composite type of an enumeration and an integer?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0013.03](log_c90.md#issue0013.03)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_127.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_127.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

See [Defect Report #013, Question 3](log_c90.md#issue0013.03). There is no requirement
that the composite type be unique, and either of the types could be chosen as
the composite type.


</div>


---

---

<div id="issue0128">

## Issue 0128: Editorial issue relating to tag declarations in type specifiers

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_128.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_128.html)

ANSI/ISO C Defect Report #rfg35:

Subject: Editorial issue relating to tag declarations in type specifiers.

Given the code:

```c
void example ()
        {
              {
              struct TAG {int i};
              }
              {
 		struct TAG object;	/* line 7 */
              }
        }
```

Does line 7 violate the semantic rule given at the very end of the semantics
sub-part of subclause 6.5, i.e., “If an identifier for an object is declared
with no linkage, the type for the object shall be complete by the end of its
declarator, ...”?

In other words, does `struct TAG` represent an incomplete type on line 7? (I
believe that the answer is “yes,” but the C Standard fails to make that entirely
clear.)

Background:

Subclause 6.5.2.3 says:

> If a type specifier of the form
>
> > *struct-or-union identifier*
>
> occurs prior to the declaration that defines the content, the structure or union
> is an incomplete type. It declares a tag that specifies a type that may be used
> only when the size of an object of the specified type is not needed.

These statements fail to take full account of scoping issues. The statements
quoted above should be rephrased to take scope issues into account, perhaps as
follows:

> If a type specifier of the form
>
> > *struct-or-union identifier*
>
> occurs within a given scope prior to another declaration (in the same scope) of
> the same identifier (which also declares the identifier to be a struct or union
> tag) or if such a type specifier occurs at some point within a given scope where
> no prior declaration of the same tag identifier is visible, then the type
> specifier declares the identifier to be a structure or union tag for an
> incomplete structure or union type (respectively). The type so declared may only
> be used when the size of an object of the specified type is not needed.

---

Comment from WG14 on 1997-09-23:

### Response

Yes, line 7 violates the semantic rule cited. Yes, `struct TAG` represents an
incomplete type. The application of rules such as scope rules need not be
restated at each relevant point in the C Standard.


</div>


---

---

<div id="issue0129">

## Issue 0129: When is name spaces of tags are shared?

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_129.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_129.html)

ANSI/ISO C Defect Report #rfg36:

Subject: Tags and name spaces.

Should (or must) a conforming implementation correctly translate the following
code?

```c
void *vp;
 struct TAG { int i; };

 void f ()
        {
        enum TAG { enumerator };
        (struct TAG *) vp;
        }
```

Background:

Subclause 6.1.2.3 says:

> Thus, there are separate *name spaces* for various categories of identifiers, as
> follows:
>
> ...
>
> \- the *tags* of structures, unions, and enumerations (disambiguated by
> following any of the keywords `struct`, `union`, or `enum`);...

A footnote for this subclause states that “There is only one name space for tags
even though three are possible.”

Given that this statement is only a footnote, and given that there are neither
any specific constraints nor any specific semantic rules violated by the code
shown above, it appears that a conforming implementation is actually *required*
(by the C Standard, as now written) to accept the code shown above (even though
this was probably not the intent of the Committee). It also seems that the code
shown above is strictly conforming.

If the Committee actually intended that such code should be considered to be
invalid, then it seems necessary to amend the C Standard to make it say that.
(Actually, I think that a new constraint is in order here.)

---

Comment from WG14 on 1997-09-23:

### Response

No change is necessary, because subclause 6.1.2.3 (second item) states that name
spaces of tags are shared. Therefore the inner `enum TAG` hides the outer
`struct TAG`, and therefore the cast `(struct TAG *)` attempts to declare a new
`struct TAG`, thus violating a constraint in subclause 6.5.

A conforming implementation need not translate the given code.


</div>


---

---

<div id="issue0130">

## Issue 0130: When is data read from a text stream guaranteed to match what was written to the stream?

Authors: Sheng Yu, WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_130.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_130.html)

Under subclause 7.9.2 **Streams**, page 125, lines 26-28:

> Data read in from a text stream will necessarily compare equal to the data that
> were earlier written out to the stream only if: the data consist only of
> printable characters and the control characters horizontal tab and new-line; ...

Writing on a text stream might not cause characters to be overwritten exactly
one for one, especially on fixed-length record based file systems. If the file
is not truncated beyond the point where the data is written, there is no sure
way to predict what will be read in after writing in the middle of a text stream
because the data might just replace a character, a line, etc. Consider the
following example:

```c
#include <stdio.h>
 #include <string.h>
 int buf[99];
 unsigned int len;
 int main()
        {
        FILE *f = fopen("test data", "w");
        fwrite("abc\ndef\n", 8, 1, f);
        fseek(f, 0, SEEK_SET);
        fwrite("UWXYZ", 5, 1, f);
        fseek(f, 0, SEEK_SET);
        len = fread(buf, 1, 10, f);
        if (len == 8 && !memcmp(buf, "UWXYZef\n"))
 		;	/* Case 1: OK, acts like binary */
        else if (len == 5 && !memcmp(buf, "UWXYZ", 5))
 		;	/* Case 2: OK to truncate after write */
        else if (len > 5 && !memcmp(buf, "UWXYZ", 5))
              printf("len = %u, buf = %s\n", len, buf);
 			/* Case 3: Is this nonstandard? */
        else
              printf("This is obviously nonstandard.\n");
        }
```

Can a conforming implementation translate the above program and produce the
following output (Case 3)?

```c
len = 9, buf = UWXYZdef
```

---

Comment from WG14 on 1997-09-23:

### Response

Yes, a conforming implementation may produce the “Case 3” output. However, there
may be cases in some conforming implementations in addition to those shown in
your example, so the printout “obviously nonstandard” may be inappropriate.


</div>


---

---

<div id="issue0131">

## Issue 0131: What is the meaning of *const-qualification*?

Authors: Douglas Gwyn, WG14  
Date: 1993-12-03  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_131.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_131.html)

I've discovered an apparent bug in the C Standard. The code snippet:

```c
struct {const int a[5]; } s1, s2;
 void f(void) {s1 = s2; }
```

can be contained in a strictly conforming program, which runs counter to my
understanding of the meaning of “const-qualification.” That occurs because,
according to subclause 6.5.3, the member `s1.a` is *not* const-qualified and
thus slips past the modifiable-lvalue definition in subclause 6.2.2.1. Subclause
6.5.3 says that the *elements* of the array `s1.a` are const-qualified, not the
array itself, and I can find no reasonable way to construe `s1.a[3]`, for
example, as a “member” of `s1`; its only member is `s1.a`, as I see it.
Apparently, the C Standard does not define the term “member,” except implicitly
through its use in subclause 6.3.2.3 **Semantics**, which says that `s1.a` is
the member (on which the subscripting operator can operate to extract an
element, but the element is not a member of the structure.)

What I think is desirable would be a required diagnostic for this example, as it
*should* be considered to violate the constraint in subclause 6.3.16 that
requires the left operand of an assignment operator to be a modifiable lvalue.

Relevant citations:

Subclause 6.2.2.1 **Lvalues and function designators**:

> A *modifiable lvalue* is an lvalue that does not have array type, does not have
> an incomplete type, does not have a const-qualified type, and if it is a
> structure or union, does not have any member (including, recursively, any member
> of all contained structures or unions) with a const-qualified type.

Subclause 6.3.16 **Assignment operators**:

> **Constraints**:
>
> An assignment operator shall have a modifiable lvalue as its left operand.

Subclause 6.5.3 **Type qualifiers**:

> If the specification of an array type includes any type qualifiers, the element
> type is so-qualified, not the array type. If the specification of a function
> type includes any type qualifiers, the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Response

The example code is *not* strictly conforming, because some objects (the
elements of the array `s1.a`) are being modified through use of an lvalue (`s1`)
with non-const-qualified type, which according to subclause 6.5.3 results in
undefined behavior.

However, a diagnostic is indeed desired here.

### Correction

***In subclause 6.2.2.1, page 36, change the parenthetic remark in the final
sentence of the first paragraph:***

(including, recursively, any member of all contained structures or unions)

***to:***

(including, recursively, any member or element of all contained aggregates or
unions)


</div>


---

---

<div id="issue0132">

## Issue 0132: Can undefined behavior occur at translation time, or only at run time?

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Status: Closed  
Cross-references: [0019](log_c90.md#issue0019)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_132.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_132.html)

Can undefined behavior occur at translation time, or only at run time? If the
former, then how does one distinguish the two cases in the C Standard?

Consider the translation unit:

```c
/* No headers included */
 int checkup()
        {
 	/* Case 1 */
        if (0)
              printf("Printing.\n");
 	/* Case 2 */
        return 2 || 1 / 0;
        }
```

Case 1 calls a function with a variable number of arguments without a prototype
in scope. But the call is never actually executed. Now, subclause 6.3.2.2, in
the first paragraph of page 41, states that this is undefined. Is it undefined
to *translate* the code, or to *execute* it? The definition of undefined
behavior (subclause 3.16) clearly allows the former, and subclause 5.3.2.2 does
*not* say that the undefined behavior occurs only if the call is actually
executed.

On the other hand, while subclause 6.3.5 uses similar wording about division by
zero, “we all know” that my Case 2 is strictly conforming.

So what is the answer? If undefined behavior cannot occur at translation time,
why the wording in subclause 3.16? If it can, how do I distinguish the
possibilities? And, by the way, what is the answer for my Case 1?

---

Comment from WG14 on 1997-09-23:

### Response

The Response to [Defect Report #109](log_c90.md#issue0019) addresses this issue. The
translation unit must be successfully translated.


</div>


---

---

<div id="issue0133">

## Issue 0133: Undefined behavior not previously listed in subclause G2

Authors: Project Editor (P.J. Plauger), WG14  
Date: 1993-12-03  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_133.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_133.html)

Undefined behavior not previously listed in subclause G2:

1\. Applying `sizeof` to an enumerate type, as in

```c
enum f {c = sizeof (enum f)}
```

has undefined behavior.

2\. A program containing no function called `main` has undefined behavior.

3\. A storage class specifier or type-qualifier modifying the keyword `void` as
a function parameter-type-list has undefined behavior.

4\. Indexing an array beyond its specified size, as in:

```c
int a[4][5];
 a[1][7] = 0;
```

has undefined behavior.

5\. If a “shall” or “shall not” requirement that appears outside of a constraint
is violated, the behavior is undefined.

6\. In pointer-integer conversion, the size of integer required and the result
are implementation-defined. If the space provided is not long enough, the
behavior is undefined.

7\. The result of the `%` operator is the remainder. In both this and the divide
operations, if the value of the second operand is zero, the behavior is
undefined.

8\. As with any other arithmetic overflow, if the result does not fit in the
space provided, the behavior is undefined.

9\. If a file with the same name as a standard header, not provided as part of
the implementation, is placed in any of the standard places for a source file to
be included, the behavior is undefined.

10\. If the signal handler `func(int sig)` executes a `return` statement and the
value of `sig` was `SIGFPE` or any other implementation-defined value
corresponding to a computational exception, the behavior is undefined.

11\. If any signal is generated by an asynchronous signal handler, the behavior
is undefined.

12\. If copying takes place between objects that overlap, the behavior is
undefined.

13\. If a fully expanded macro replacement list contains a function-like macro
name as its last preprocessing token, it is unspecified whether this macro name
may be subsequently replaced. If the behavior of the program depends upon this
unspecified behavior, then the behavior is undefined. For example:

```c
#define f(a)    a*g
 #define g(a)   f(a)
```

the invocation `f(2) (9)` results in undefined behavior.

14\. A call to a library function that exceeds an **Environmental limit** has
undefined behavior.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard makes it sufficiently clear that the described behaviors are
undefined. The next revision of the C Standard can include a more comprehensive
list.


</div>


---

---

<div id="issue0134">

## Issue 0134: Is *error number* an undefined term?

Authors: Clive Feather, Project Editor (P.J. Plauger)  
Date: 1994-01-31  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_134.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_134.html)

Subclause 7.11.6.2 **The `strerror` function**, page 168, reads:

> The `strerror` function maps the error number in `errnum` to an error message
> string.

However, “error number” is an undefined term. Must `strerror` provide a valid
message for every value of type `int`, or can some values be a domain error,
allowing it to return garbage or a null pointer? If the latter, then what are
the values that must generate a valid string? Must the following generate a
valid string:

zero

`EDOM` and `ERANGE`

the value of any other symbol defined in `<errno.h>`

any value that a library routine might set `errno` to

---

Comment from WG14 on 1997-09-23:

### Response

The `strerror` function must provide a valid message for the error numbers
`EDOM`, `ERANGE`, and any other value a library function might store in `errno`.
For all other values, the behavior is undefined.


</div>


---

---

<div id="issue0135">

## Issue 0135: Is the `SVR4 fwrite` different?

Authors: Per Bothner, Project Editor (P.J. Plauger)  
Date: 1994-01-31  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_135.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_135.html)

H.J. Lu points out that the SVR4 manual explicitly says that `fwrite(ptr, 0, 1,
stream)` returns 0, not 1\. I don't know what the SVID states.

I think it is more mathematically consistent to return 1 in this case. But in
that case `fread(ptr, 0, 1, stream)` should also return 1, but ANSI explicitly
states that it should return 0\. I don't see any reason why these should be
different, so I think it is best to follow existing practice. I think the ANSI
specification for `fwrite` is a mistake; perhaps it should be fixed in the
revision.

---

Comment from WG14 on 1997-09-23:

### Response

There are no zero-length objects in C. Therefore, if the size argument to
`fwrite` is zero, it is outside the domain of the function and (by subclause
7.1.7), the result is undefined. The C Standard is not in conflict with the
cited behavior of SVR4.


</div>


---

---

<div id="issue0136">

## Issue 0136: Does `mktime` yield a -1 in the *spring-forward* gap when `tm_isdst` is -1?

Authors: Paul Eggert, Project Editor (P.J. Plauger)  
Date: 1994-03-31  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_136.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_136.html)

Suppose I run the following program in a US environment, where the clocks will
jump forward from 01:59:59 to 03:00:00 on April 3, 1994\. This program attempts
to invoke `mktime` on a `struct tm` that represents 02:30:00 on that date. Does
the C Standard let `mktime` return -1 in this case?

```c
#include <stdio.h>
 #include <time.h>
 int main()
        {
        struct tm t;
        time_t r;

 	/* 1994-04-03 02:30:00 */
        t.tm_year = 1994 - 1900; t.tm_mon = 3; t.tm_mday = 3;
        t.tm_hour = 2; t.tm_min = 30; t.tm_sec = 0;

 	t.tm_isdst = -1; /* i.e. unknown */

        r = mktime(&t);
        if (r == -1)
              printf("mktime failed\n");
        else
              printf("%s", ctime(&r));
        return 0;
        }
```

The ANSI C Rationale (corresponding to subclause 7.12.2.3) clearly lets `mktime`
yield -1 in the “fall-backward fold” that will occur when the clock is turned
back from 01:59:59 to 01:00:00 on October 30, 1994\. The question is whether
`mktime` is also allowed to yield -1 in the “spring-forward gap” when the clock
is advanced from 01:59:59 to 03:00:00.

This question arose when Arthur David Olson's popular “tz” time zone software
was tested using NIST-PCTS:151-2, Version 1.4, (1993-12-03) a test suite put out
by the National Institute of Standards and Technology that attempts to test C
and Posix conformance. The PCTS package insists that in the above case, `mktime`
must yield a `time_t` corresponding to either 01:30:00 or 03:30:00; i.e. PCTS
rejects Olson's `mktime`, which yields -1.

This test case differs in an important way from the common practical use of
`mktime` to “add 1” to the output of `localtime` or `gmtime`, since those
functions normally set `tm_isdst` to a nonnegative value, whereas `tm_isdst` is
-1 in the case under question.

I suggest that the Committee issue a clarification which makes it clear that
`mktime` can yield -1 in the spring-forward gap when `tm_isdst` is -1.

---

Comment from WG14 on 1997-09-23:

### Response

The Standard does not specify the behavior precisely enough to preclude `mktime`
from returning a value of `(time_t)-1` and leaving the `tm_isdst` member set to
-1 in such situations.


</div>


---

---

<div id="issue0137">

## Issue 0137: Is `printf("%.1f", -0.01)` required to produce `0.0` , `-0.0`, or are both acceptable?

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1994-04-30  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_137.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_137.html)

Is `printf("%.1f", -0.01)` required to produce `0.0`, `-0.0`, or are both
acceptable?

Subclause 7.9.6.1 says that when the `+` flag is not specified, the result
begins with a sign only when a negative value is converted. The description of
the `f` conversion (also `e` and `E`) says that the value is rounded to the
appropriate number of digits. Is the value used to determine the sign of the
result the value before or after rounding?

---

Comment from WG14 on 1997-09-23:

### Response

As specified in subclause 7.9.6.1 for the `+` flag, a negative value is being
converted, so a minus sign is required. The intent is that the sign is
determined prior to conversion.


</div>


---

---

<div id="issue0138">

## Issue 0138: What are the storage durations?

Authors: John Max Skaller, Project Editor (P.J. Plauger)  
Date: 1994-06-02  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_138.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_138.html)

Subclause 6.1.2.4 says:

> An object has a *storage duration* that determines its lifetime. There are two
> storage durations: static and automatic.

To me that clearly excludes heap objects. Is there a Defect Report on that? If
so which one? (I have responses to Defect Report #001 through Defect Report
#059.) If not and something else in the Standard fixes it, can you point out
where?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.4, page 22, first paragraph, change:***

There are two storage durations: static and automatic.

***to:***

There are three storage durations: static, automatic, and allocated. Allocated
storage is described in 7.10.3.


</div>


---

---

<div id="issue0139">

## Issue 0139: Is an incomplete type compatible with the completed type?

Authors: Larry Jones, Project Editor (P.J. Plauger)  
Date: 1994-06-13  
Status: Fixed  
Fixed in: C90 TC2  
Cross-references: [0059](log_c90.md#issue0059), [0088](log_c90.md#issue0088)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_139.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_139.html)

Subject: Compatibility of complete and incomplete types.

The Committee has already endorsed the concept of using incomplete types which
are completed in some translation units and left incomplete in others for
encapsulation and data hiding (cf. [Defect Report #059](log_c90.md#issue0059)). However, I
can find nothing in the Standard which allows the incomplete type to be
compatible with the completed type, which causes such usage to be not strictly
conforming. I believe this to be an oversight.

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.6, page 25, first paragraph, change:***

Moreover, two structure, union, or enumerated types declared in separate
translation units are compatible if they have the same number of members, the
same member names, and compatible member types; for two structures, the members
shall be in the same order; for two structures or unions, the bit-fields shall
have the same widths; for two enumerated types, the members shall have the same
values.

***to:***

Moreover, two structure, union, or enumerated types declared in separate
translation units are compatible if at least one is an incomplete type or if
they have the same number of members, the same member names, and compatible
member types; for two complete structure types, the members shall be in the same
order; for two complete structure or union types, the bit-fields shall have the
same widths; for two enumerated types, the members shall have the same values.


</div>


---

---

<div id="issue0140">

## Issue 0140: What does *performed* and *other operation* mean?

Authors: Andy Pepperdine, BSI  
Date: 1994-07-27  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_140.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_140.html)

Subclause 7.9.5.6 says:

> The `setvbuf` function may be used only after the stream ... has been associated
> with an open file and before any other operation is performed on the stream.

There are two related questions associated with this statement.

1\. What does “performed” mean?

a. Does it include attempts that failed (such as `fread` on output file, etc.)?

b. In particular, does it include a failed attempt to `setvbuf`?

c. What about `fprintf(f, "")`?

2\. What does “other operation” mean?

a. Does it include `setvbuf` itself?

b. Are `ferror` and `feof` operations?

c. What about `clearerr`?

Reasons for asking:

It would seem reasonable to try to get a very large buffer in some applications
by attempting to do a `setvbuf` with, say, 1 MB of buffer space. If that fails,
try again with 0.5 MB, etc. Is this allowed?

My *guess* as to the interpretation is as follows:

1\. An operation is “performed” even if it fails for whatever reason.

2\. All functions defined in subclause 7.9 are to be treated as “operations.”

This is unsatisfactory, as the above approach of attempting to find a good
buffer size would fail.

In the Rationale, it states “The general principle is to provide portable code
with a means of requesting the most appropriate popular buffering style, but not
to *require* an implementation to support these styles.” \[Emphasis added.]

I interpret this as saying that `setvbuf` is an advisory call and need not be
acted on. However, my questions above still stand as there seems to be no way of
negotiating an agreement on good acceptable buffer sizes.

I believe that a clarification is required.

---

Comment from WG14 on 1997-09-23:

### Response

As you say, “`setvbuf` is an advisory call and need not be acted on.” That is to
say, the C Standard allows it to fail. Therefore, discussions of detailed
constraints such as you describe could only constitute non-normative advice to
programmers or implementers. The Committee does not have any specific advice to
give in this regard.


</div>


---

---

<div id="issue0141">

## Issue 0141: What does `EOF` mean in `<stdio.h>`?

Authors: Doug McIlroy, Project Editor (P.J. Plauger)  
Date: 1994-09-10  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_141.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_141.html)

What does `EOF` mean in `<stdio.h>`? Subclause 7.9.1 says that it “is returned
by several functions to indicate *end-of-file,* that is, no more input from a
stream.”

Taken at face value, the statement that there is no more input implies that
further reads from the stream will yield `EOF`. In many implementations this is
not true. It may be possible to read data from a stream on which the end-of-file
indicator is set. Just whether that happens usually depends on what kind of file
the stream is associated with. In System V, for example, one will almost always
get more data on reading past `EOF` on a terminal, and almost never on a plain
file. This violates the principle of device-independent behavior.

I believe the System V behavior is wrong. Whenever `feof` would return nonzero,
`getc` should return `EOF`.

Some old code will break if `EOF` is made sticky as I suggest, but surprisingly
little. When we made it sticky in v10 UNIX, we had to change exactly one
dishonest program (sdb), which used ctl-D as if it were a character without
putting the terminal in raw mode. Not one complaint arose from the change.

On the other hand, almost every UNIX user has at one time or another been
surprised by a nonsticky `EOF`, manifested as a program needing more than one
`EOT` to stop it when `stdin` comes from a terminal. That breeds the habit of
typing extra `EOT` at balky programs. The habit causes yet more trouble (hangup,
for example), when things are merely slow and not really balky. This
indefinite-`EOF` problem is not the fault of the programs, which should be able
to count on a uniform behavior of `EOF` across all files. It is a fundamental
mistake in the implementation of `<stdio.h>`.

I urge the Committee to clarify `EOF`, and clarify it in the direction of
predictability.

---

Comment from WG14 on 1997-09-23:

### Response

It was certainly the intent of the Committee that end-of-file should indicate
“no more input from a stream,” at least when returned by functions such as
`fgetc`. In particular, subclause 7.9.7.1 **The `fgetc` function** says, in
part:

If the stream is at end-of-file, the end-of-file indicator for the stream is set
and `fgetc` returns `EOF`. “Setting the end-of-file indicator” implies that
*that stream* is now considered to be “at end-of-file.”

For input from a stream to return other than `EOF` after once returning `EOF`
(with no intervening file-positioning operations or calls to `clearerr`) is
non-conforming behavior, however widespread.


</div>


---

---

<div id="issue0142">

## Issue 0142: Is it permitted to `#undef` a reserved macro name?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_142.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_142.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 026: Reservation of macro names

Is it permitted to `#undef` a reserved macro name? Consider the translation
unit:

```c
#include <errno.h>
 #undef EASTER
 #undef EDOM
 #undef __ERRNO_BASE
 int error (void) { return errno == ERANGE; }
```

Considering each of the three `#undef` directives independently, is each
directive permitted in a strictly conforming program? Is the translation unit
strictly conforming?

Subclause 7.1.3 describes various classes of reserved identifiers, and then
states:

> If the program declares or defines an identifier with the same name as an
> identifier reserved in that context (other than as allowed by 7.1.7), the
> behavior is undefined.

However, this does mention the use of `#undef`. Subclause 7.1.7 does so, for
certain identifiers, but in rather ambiguous words:

> The use of `#undef` to remove any macro definition will also ensure ...

It has been suggested that this wording merely describes a strictly conforming
coding technique, rather than establishing a special case (rather like the
wording about placing the name in parentheses does).

Therefore, can a strictly conforming program `#undef` a name which is reserved
for any use at that point?

There is a good reason to allow such an `#undef`. A program can make use of a
identifier which is convenient but would otherwise be reserved (for example, the
identifier `EASTER`). There is also a good reason to forbid it: the macro
`ERANGE` might actually be defined as (`__ERRNO_BASE + 42`). This leads to the
conclusion that it might be best to permit it for some names but not others.

A further example \[inserted at the request of BSI] is the translation unit:

```c
#include <stdlib.h>
 #undef __INCLUDED_STDLIB_H
 #include <stdlib.h>
```

### Suggested Technical Corrigendum:

Add to the end of subclause 7.1.3:

If the program removes (with `#undef`) the macro definition of an identifier in
the first group listed above, the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Technical Corrigendum

Replace the third bullet in subclause 7.1.3 with the following:

Each macro name in any of the following subclauses (including **Future library
directions**) is reserved for use as specified if any of its associated headers
is included, unless explicitly stated otherwise.

Forward reference: 7.1.7.


</div>


---

---

<div id="issue0143">

## Issue 0143: What are the definitions of file opening modes?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_143.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_143.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 027: fopen modes

*\[BSI characterize this issue as minor.]*

The definition of file opening modes is self-contradictory.

Subclause 7.9.5.3 reads in part:

> The argument mode points to a string beginning with one of the following
> sequences:

and then lists all of `r`, `r+`, `rb`, and `rb+` or `r+b`, with different
meanings. Obviously, it is possible for a string to begin with up to three of
these simultaneously, and thus the quoted text is contradictory.

Also, the wording is confusing since it can easily be misread as "beginning with
exactly one of the following sequences," which would prohibit those of the
specified modes that are longer than one character.

### Suggested Technical Corrigendum:

Change the quoted text to:

> The mode is determined by the longest match of the following sequences to the
> initial characters of the string pointed to by the argument `mode`; at least the
> initial character shall match.

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

The current C Standard has correct meaning, but the wording could be clearer. We
suggest the following change for the revised C Standard:

> The argument `mode` points to a string. The mode is determined by the string's
> longest initial match to the following sequences; at least the initial character
> shall match:


</div>


---

---

<div id="issue0144">

## Issue 0144: Can the white space preceeding the initial `#` of a preprocessing directive be derived from macro expansion?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_144.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_144.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 028: Preprocessing of preprocessing directives

Can the white space preceding the initial `#` of a preprocessing directive be
derived from macro expansion? Consider the following code extract:

```c
#define EMPTY
 # EMPTY include <file.h>  /* Line A */
 EMPTY # include <file.h>  /* Line B */
```

Line A is clearly forbidden by subclause 6.8:

> The preprocessing tokens within a preprocessing directive are not subject to
> macro expansion unless otherwise stated.

However, this text does not appear to forbid line B. Nor does subclause 6.8.3.4:

> The resulting completely macro-replaced preprocessing token sequence is not
> processed as a preprocessing directive even if it resembles one. If that
> subclause applies only to the expansion of `EMPTY`, it is not relevant. If it
> applies to both the expansion and the following preprocessing token sequence,
> then no subsequent preprocessing directive could ever be processed.

Is line B strictly conforming, or does it violate a constraint (and if so,
which), or does it cause undefined behavior?

### Suggested Technical Corrigendum:

In subclause 6.8 Description, change:

> A preprocessing directive consists of a sequence of preprocessing tokens that
> begins with a \# preprocessing token that is either ...

to:

> A preprocessing directive consists of a sequence of preprocessing tokens that
> begins with a \# preprocessing token that (at the start of translation phase 4,
> before any preprocessing takes place) is either ...

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

The current C Standard has correct meaning, but the wording could be clearer. We
suggest the following change for the revised C Standard:

> A preprocessing directive consists of a directive consists of a sequence of
> preprocessing tokens that begins with a `#` preprocessing token that (at the
> start of translation phase 4\) is either ...


</div>


---

---

<div id="issue0145">

## Issue 0145: The four possible forms for a constant expression are not consistent

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_145.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_145.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 029: Constant expressions

There is a confusion of contextual levels in subclause 6.4. Subclause 6.4 lists
four possible forms for a constant expression in an initializer:

> Such a constant expression shall evaluate to one of the following:
>
> an arithmetic constant expression,
>
> a null pointer constant,
>
> an address constant, or
>
> an address constant for an object type plus or minus an integral constant
> expression.

The first two of these are syntactic forms, not something that a syntactic form
would evaluate to. The third is the result of an evaluation, and the fourth is a
compound of the two types of entity.

This confusion makes it unclear whether expressions like:

```c
(int *)0
```

which is not a null pointer constant, or

```c
x[5] - x[2]
```

which is clearly a constant, are permitted in initializers.

### Suggested Technical Corrigendum:

Replace the quoted text with:

> Such a constant expression shall be either an arithmetic constant expression, a
> null pointer constant, or an address constant expression.

In the second subsequent paragraph, change:

> An address constant is a pointer to an lvalue designating an object of static
> storage duration, or to a function designator; it shall be created explicitly,
> using the unary \& operator, or implicitly ...

to:

> An address constant expression shall have pointer type, and shall evaluate to:
>
> a null pointer,
>
> the address of a function, or
>
> the address of an object of static storage duration plus or minus some integer.
>
> The address may be created explicitly, using the unary `&` operator, or
> implicitly ...

---

Comment from WG14 on 1997-09-23:

### Future Change

In subclause 6.4 Semantics, change:

> More latitude is permitted for constant expressions in initializers. Such an
> expression shall evaluate to one of the following:

to:

> More latitude is permitted for constant expressions in initializers. Such an
> expression shall be, or evaluate to, one of the following:

and change:

> An *address constant* is a pointer to an lvalue designating an object of static
> storage duration, or to a function designator; it shall be created explicitly,
> using the unary \& operator, or implicitly, by the use of an expression of array
> or function type.

to:

> An *address constant* is a null pointer, a pointer to an lvalue designating an
> object of static storage duration, or a pointer to a function designator. It
> shall be created explicitly using the unary \& operator or an integral constant
> expression cast to pointer type, or implicitly by the use of an expression of
> array or function type.


</div>


---

---

<div id="issue0146">

## Issue 0146: Does the constraint of 6.1.2 serve a purpose?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Cross-references: [0017.39](log_c90.md#issue0017.39)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_146.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_146.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 030: Nugatory constraint

*\[BSI characterize this issue as minor.]*

The constraint of 6.1.2 serves no purpose. Subclause 6.1.2 states in part:

**Constraints**

In translation phases 7 and 8, an identifier shall not consist of the same
sequence of characters as a keyword.

**Semantics**

... When preprocessing tokens are converted to tokens during translation phase
7, if a preprocessing token could be converted to either a keyword or an
identifier, it is converted to a keyword.

Given the latter text \[added in Technical Corrigendum 1, reference [DR 017
Q39](log_c90.md#issue0017.39)], the constraint can never be violated.

### Suggested Technical Corrigendum:

Delete the constraint in subclause 6.1.2.

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

Delete the constraint in subclause 6.1.2.


</div>


---

---

<div id="issue0147">

## Issue 0147: Is there a requirement for a sequence point to occur within a library function?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_147.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_147.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 031: Sequence points in library functions

There is no requirement for a sequence point to occur within a library function,
since it might not be written in C. Consider the following code:

```c
#include <string.h>
 char s[10];
 /* ... */
 (strcpy)(s, "Testing") [0] = 'X';
```

Any function written in C must have a sequence point after the last full
expression evaluated (which will be the returned value if there is one), so if
`strcpy` were a C function, the assigning of `'T'` to `s[0]` would be completed
before the call returned.

However, since library functions might not be written in C, they might not have
such a sequence point. If not, then the above statement is in breach of the
requirements of the second paragraph of subclause 6.3.

### Suggested Technical Corrigendum:

Add to the end of subclause 7.1.7:

There is a sequence point immediately before a library function returns.

Add to the end of annex C:

Immediately before a library function returns (7.1.7).

Add a reference to 7.1.7 in the **Forward References** of 5.1.2.3, and in the
relevant **Index** entry.

---

Comment from WG14 on 1997-09-23:

### Response

We agree that the current wording does not make this clear. The next revision of
the C Standard will clarify that every function return is a sequence point. The
suggested changes will be used.


</div>


---

---

<div id="issue0148">

## Issue 0148: Is it clear when it is permitted to declare a library function?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_148.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_148.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 032: Defining library functions

Subclause 7.1.7 is unclear about when it is permitted to declare a library
function. Consider the following translation unit:

```c
#include <math.h>
 double (sin)(double);
```

Subclause 7.1.7 states in part:

Any function declared in a header may be additionally implemented as a macro
defined in the header, so a library function should not be declared explicitly
if its header is included.

Since the wording uses the term "should", this does not appear to actually be a
requirement on programs, and the code appears to be strictly conforming; in
other words, the C Standard here simply uses overly restrictive wording while
trying to assist readers, and does not actually forbid the above code.

Is this interpretation correct?

Note that code such as the above is useful if the `#include` is conditionally
compiled or is within a header not under the control of the code's author.

### Suggested Technical Corrigendum:

If the intent was to forbid such a declaration, then change the quoted text to:

A library function shall not be declared explicitly if its header is included.

If the intent was to allow the macros described in subclause 7.1.7 to be
object-like macros (though other wording in 7.1.7 appears to forbid this), then
change the quoted text to:

A library function must not be declared explicitly if its header is included,
unless any macro definition of the name has been removed with `#undef`.

If the intent was to allow the example declaration, then change the quoted text
to:

Any function declared in a header may be additionally implemented as a macro
defined in the header, so one of the techniques below should be used to ensure
that any explicit declaration of a library function is not affected by any such
macro.

---

Comment from WG14 on 1997-09-23:

### Response

The wording of the C Standard is as intended. The term "should" is intended as
guidance to the programmer as is the sentence following the one cited in the C
Standard.


</div>


---

---

<div id="issue0149">

## Issue 0149: Is the term *variable* defiend?

Authors: Clive D.W. Feather, BSI  
Date: 1995-02-23  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_149.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_149.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 033: The term "variable"

*\[BSI characterize this issue as minor.]*

The term "variable" is used in subclause 7.7.1.1, but is never defined in the C
Standard.

### Suggested Technical Corrigendum:

In subclause 7.7.1.1, change:

... or refers to any object with static storage duration other than by assigning
a value to a static storage duration variable of type `volatile sig_atomic_t`.

to:

... or refers to any object with static storage duration other than by assigning
a value to an object declared as `volatile sig_atomic_t`.

---

Comment from WG14 on 1997-09-23:

### Response

The next revision of the C Standard will use the term "object" instead of
"variable" uniformly.


</div>


---

---

<div id="issue0150">

## Issue 0150: Are programs containing `char array[] = "Hello, World";` strictly conforming?

Authors: Jutta Degener, DIN  
Date: 1995-06-11  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_150.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_150.html)

*This Defect Report was prepared with considerable help from Mark Brader, Clive
Feather, Ronald Guilmette, and a person whose employment conditions require
anonymity.*

DIN-001:

According to the current C Standard, programs containing

```c
char array[] = "Hello, World";
```

are not strictly conforming.

A **Constraint** in subclause 6.5.7 **Initialization**, demands that:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions.

Subclause 6.4 **Constant expressions**, defines various kinds of constant
expression. In its **Semantics** it states that a constant expression in an
initializer evaluates to one of the following:

\- an arithmetic constant expression

\- a null pointer constant,

\- an address constant, or

\- an address constant for an object type plus or minus an integral constant
expression.

String literals are neither. A string literal used to initialize a character
array does not decay to a pointer to its first element, according to Subclause
6.2.2.1:

Except when it is the operand of the `sizeof` operator or the unary `&`
operator, or is a character string literal used to initialize an array of
character type, or is a wide string literal used to initialize an array with
element type compatible with `wchar_t`, an lvalue that has type "array of
*type*" is converted to an expression that has type "pointer to *type*" that
points to the initial element of the array object and is not an lvalue.

and hence is not an address constant.

### Suggested Technical Corrigendum:

In subclause 6.5.7, change:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions.

to:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions or string literals.

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

In subclause 6.5.7, change:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions.

to:

All the expressions in an initializer for an object that has static storage
duration or in an initializer list for an object that has aggregate or union
type shall be constant expressions or string literals.


</div>


---

---

<div id="issue0151">

## Issue 0151: Is the out from `printf("%#.0o", 0);` ambiguous?

Authors: Jutta Degener, DIN  
Date: 1995-06-11  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_151.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_151.html)

*This Defect Report was prompted by articles posted to comp.std.c by Bakul Shah,
Rex Jaeschke, and Soenke Behrens.*

DIN-002:

The C Standard's specification of what

```c
printf("%#.0o", 0);
```

outputs is ambiguous, and compiler vendors have indeed interpreted it
differently.

For a zero integer value, the descriptions of the `#` flag and the 0 precision
in subclause 7.9.6.1 contradict each other.

The `#` demands that the first digit be zero;

`#` The result is to be converted to an "alternate form." For `o` conversion, it
increases the precision, if and only if necessary, to force the first digit of
the result to be a zero.

But a precision of 0 demands that nothing at all be printed.

`o,u,x,X [...]` The result of converting a zero value with a precision of zero
is no characters.

In the hexadecimal case, the description of the `#` flag's effects has been
worded such that the conflict is avoided:

`# [...]` For `x` (or `X`) conversion, a nonzero result will have `0x` (or `0X`)
prefixed to it.

If it was intended that the octal case, too, should print nothing, this crucial
"nonzero" should be introduced into its description as well.

### Suggested Technical Corrigendum:

In subclause 7.9.6.1, replace:

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of the result to be a zero.

by:

For `o` conversion, it increases the precision, if and only if necessary, to
force the first digit of a nonzero result to be a zero.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard is clear enough as is. The call

```c
printf("%#.0o", 0)
```

should print `0`.


</div>


---

---

<div id="issue0152">

## Issue 0152: Can `longjmp` be used to return from a signal handler invoked other than through `abort` or `raise`?

Authors: Jutta Degener, DIN  
Date: 1995-06-11  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_152.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_152.html)

*This Defect Report was prepared with considerable help from Mark Brader, Clive
Feather, Ronald Guilmette, and a person whose employment conditions require
anonymity.*

DIN-003:

Can `longjmp` be used to return from a signal handler invoked other than through
`abort` or `raise`? The descriptions of `signal` and `longjmp` contradict each
other.

According to subclause 7.7.1.1 **The `signal` function**:

If the signal occurs other than as the result of calling the `abort` or `raise`
function, the behavior is undefined if the signal handler calls any function in
the standard library other than the `signal` function itself (with a first
argument of the signal number corresponding to the signal that caused the
invocation of the handler) or refers to any object with static storage duration
other than by assigning a value to a static storage duration variable of type
`volatile sig_atomic_t`.

Since `longjmp` is a function, it cannot be called.

But subclause 7.6.2.1 **The `longjmp` function**, broadly guarantees the
opposite:

As it bypasses the usual function call and return mechanisms, the `longjmp`
function shall execute correctly in contexts of interrupts, signals and any of
their associated functions.

### Suggested Technical Corrigendum:

If the intent is to allow calls to `exit` and `longjmp` from signal handlers not
invoked through calls to `raise` or `abort`, replace in subclause 7.6.2.1:

... other than the `signal` function itself ...

by:

... other than `longjmp`, `exit`, or the `signal` function itself ...

Alternatively, if the intent is to disallow calls to `longjmp` from signal
handlers not invoked through calls to `raise` or `abort`, replace in subclause
7.7.1.1:

As it bypasses the usual function call and return mechanisms, the `longjmp`
function shall execute correctly in contexts of interrupts, signals and any of
their associated functions. However, if the `longjmp` function is invoked from a
nested signal handler (that is, from a function invoked as a result of a signal
raised during the handling of another signal), the behavior is undefined.

by:

If the `longjmp` function is invoked from a nested signal handler (that is, from
a function invoked as a result of a signal raised during the handling of another
signal), the behavior is undefined.

---

Comment from WG14 on 1997-09-23:

### Response

The C Standard is clear enough as is. The `longjmp` function shall execute
correctly when called from a non-nested signal handler invoked through calls to
the `raise` or `abort` functions; if `longjmp` is called from a signal handler
invoked by other means, or from a nested signal handler, the behavior is
undefined.


</div>


---

---

<div id="issue0153">

## Issue 0153: Is there a problem with empty arguments in macro calls?

Authors: Ed Keizer, NNI  
Date: 1995-08-21  
Status: Closed  
Cross-references: [0003.03](log_c90.md#issue0003.03)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_153.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_153.html)

**Short description of problem**

The C Standard contains conflicting words on whether `f()` can be considered a
call to a function-like macro with one empty argument.

**Problem description**

There seems to be a problem with empty arguments in macro calls in the current C
Standard. An example:

```c
#define foo()     A
 #define bar(B)  B

 foo()           // no arguments
  bar()           // one empty argument?
```

There seem to be two choices when there are no preprocessing tokens between the
parentheses in a macro call: a single empty argument or no arguments. The call
to `bar` is different. According to some the call violates a constraint. Others
are of the opinion that the call to `bar` is undefined behavior and that it can
be seen as a call with a single, empty argument.

Quotes from subclause 6.8.3 of the C Standard: fourth paragraph of

**Constraints:**

The number of arguments in an invocation of a function-like macro shall agree
with the number of parameters in the macro definition, and there shall exist a
`)` preprocessing token that terminates the invocation.

Last paragraph of semantics:

If (before argument substitution) any argument consists of no preprocessing
tokens, the behavior is undefined.

Is the call to `bar` in the example a constraint violation or undefined
behavior? The question seems to show an ambiguity in the C Standard.

The X3J11 archives contain several requests to allow empty macro arguments and
refusals to do so. The refusals stated that the reasons would be included in the
rationale, but the rationale is silent on this matter. Hearsay indicates that
X3J11 decided to leave the issue of empty macro arguments open.

**Solutions:**

There seem to be four ways to change the C Standard:

(1) Resolve the ambiguity by considering `bar()` and `foo()` calls with no
parameters.

(2) Resolve the ambiguity by considering `bar()` and `foo()` calls with one
empty parameter.

(3) Resolve the ambiguity by making the interpretation of the empty
preprocessing token sequence context dependent and consider `bar()` a call with
one empty parameter and `foo()` a call without parameters.

(4) Leave the issue open by making clear that empty arguments are undefined
behavior and that a call without preprocessing tokens between the parentheses to
a function-like macro defined with one parameter does not violate a constraint.

**Arguments for a choice:**

Solution 2 causes a constraint violation in `foo()` and thus forbids calls to
macros defined without parameters. Argument-less macros are often used in
current C programs. Thus making this change would violate the first part of
guiding principle 1 of the C9X charter: Existing code is important.

Solution 4 allows compiler writers to choose between solution 1 and solution 3\.

Solutions 1 and 2 are in conflict with WG14/N418, the proposal to allow empty
arguments in macro replacements.

Solution 3 conflicts with our rule to "keep it simple" and will create
confusion. The following example serves as an illustration. A user had a program
in which he used a function-like macro without arguments. While doing an
overhaul of the program he decided that he needed one argument and changed the
function definition accordingly. When he edited his program to change the calls,
he forgot one call. His program compiled, but showed strange behavior. After
several hours of debugging he found the one call with the missing arguments and
was very surprised that the compiler had not complained.

**Proposal**

The arguments above led us to believe that to allow empty arguments to
function-like macros would be bad from a software engineering viewpoint and
cause confusion. Thus we propose to use solution 1\. This can be done by
inserting the following sentence from the semantics section of subclause 6.8.3
quoted above:

A call to a function-like macro without preprocessing tokens between the opening
and closing parentheses is taken to be a call without arguments, not a call with
a single empty argument.

---

Comment from WG14 on 1997-09-23:

### Response

This was addressed in the response to [Defect Report #003, question
3](log_c90.md#issue0003.03), which asked essentially the same question. A diagnostic is
not required.


</div>


---

---

<div id="issue0154">

## Issue 0154: What restrictions apply to implementation-defined entities?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_154.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_154.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 002: Consistency of implementation-defined values

The restrictions that apply to "implementation-defined" entities are not clear.

What restrictions apply to implementation-defined entities? If the value of an
expression is implementation-defined, need the implementation always produce the
same result?

For example, the value of the expressions `7/-3` and `8/-3` must each be either
`3` or `2`. Can an implementation make them different (that is, use a different
implementation-defined choice for each), or must it make the same choice for all
integral divisions involving a negative quantity?

As another example, can the number of significant characters and the
significance of case in an identifier with external linkage depend on the
identifier itself, or must it be the same for all possible identifiers?

---

Comment from WG14 on 1997-09-23:

### Response

"Implementation defined" means just that: an implementation can define any
behavior even though it may not be constant.


</div>


---

---

<div id="issue0155">

## Issue 0155: Is the word *unique* in subclause 7.10.3 ambiguous?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0158](log_c90.md#issue0158)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_155.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_155.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 003: Zero-sized allocations

The use of the word "unique" in subclause 7.10.3 is ambiguous, and the handling
of zero size allocations is incomplete.

**Part 1**

Subclause 7.10.3 reads

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer.

Does the term "unique" mean "different every time," or does it mean "there is a
single pointer returned by all calls with size zero" (as might be presumed from
the ordinary dictionary definition of "unique") ?

In other words, if `malloc(0)` does not return a null pointer, is the following
expression:

```c
malloc(0) == malloc(0)
```

always zero, always non-zero, or implementation-defined ?

**Part 2**

If unique means "there is a single pointer," what is the result of attempting to
free that pointer? How does the wording of 7.10.3 apply:

The value of a pointer that refers to freed space is indeterminate.

Possibly nothing happens, because the pointer does not really point to a block
of memory. In that case, is the following code strictly conforming?

```c
#include <stdlib.h>
 /* ..... */
 void *p = malloc(0);
 if (p != NULL)
 {
 free (p); /* Line A */
free (p); /* Line B */
}
```

What is the behavior if each of lines A and B are reached?

**Part 3**

If "unique" means "different every time," then each such call still consumes
address space, even though no storage actually needs to be allocated, and
therefore the call can fail due to exhaustion of memory. Thus `malloc(0)` can
return a null pointer, while the C Standard seems to suggest that an
implementation can return either null pointers or unique pointers, but not both.
This is a defect in the existing wording.

### Suggested Technical Corrigendum:

If "unique" means "there is a single pointer," then change the penultimate
sentence of 7.10.3 from:

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer.

to:

If the size of the space requested is zero, the behavior is
implementation-defined; the value returned shall be either a null pointer or a
unique pointer. The values returned by two zero-length allocations shall compare
equal. Freeing the value returned by a zero-length allocation shall have no
effect. If that value is used as an operand of the unary `*` operator, or of a
`+` or `-` operator except one whose other operand has integral type and value
zero, the behavior is undefined.

If "unique" means "different every time," then change it to:

If the size of the space requested is zero, the behavior is
implementation-defined; either a null pointer is always returned, or the
behavior is as if the size were some unspecified non-zero value. In the latter
case, if the returned pointer is not a null pointer and is used as an operand of
the unary `*` operator, or of a `+` or `-` operator except one whose other
operand has integral type and value zero, the behavior is undefined.

\[See also [Defect Report #158](log_c90.md#issue0158).]

---

Comment from WG14 on 1997-09-23:

Technical Corrigendum

In subclause 7.10.3, change the next to last sentence to read:

If the size of the space requested is zero, the behavior is implementation
defined: either a null pointer is returned, or the behavior is as if the size
were some unspecified nonzero value, except that the returned pointer shall not
be used to access an object.


</div>


---

---

<div id="issue0156">

## Issue 0156: Should calls to `fsetpos` with positions in closed and reopened streams be undefined?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_156.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_156.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned. This Defect Report has been
prepared with considerable help from Mark Brader, Jutta Degener, Ronald
Guilmette, and a person whose employment conditions require anonymity. However,
except where stated, opinions expressed or implied should not be assumed to be
those of any person other than myself.*

Defect Report UK 004: Closed streams

Calls to `fsetpos` with positions in closed and reopened streams are permitted,
but should be undefined.

The definition of `fsetpos` (subclause 7.9.9.3) requires the `fpos_t` argument
to have a value generated by a successful call to `fgetpos` on the same stream.
However, it does not require the stream to refer to the same file. If the stream
does not so refer, the effect should be explicitly undefined.

### Suggested Technical Corrigendum:

In subclause 7.9.9.3, change:

... an earlier call to the `fgetpos` function on the same stream.

to:

... an earlier call to the `fgetpos` function on the same stream; there shall
not have been an intervening call to the `fclose` or `freopen` function with
that stream.

---

Comment from WG14 on 1997-09-23:

Technical Corrigendum

In subclause 7.9.9.2, page 145, change:

... an earlier successful call to the `ftell` function on the same stream ...

to:

... an earlier successful call to the `ftell` function on a stream associated
with the same file ...

In subclause 7.9.9.3, page 146, change:

... an earlier successful call to the `fgetpos` function on the same stream.

to:

... an earlier successful call to the `fgetpos` function on a stream associated
with the same file.


</div>


---

---

<div id="issue0157">

## Issue 0157: Is it clearly indicated when the spelling of a type name is or is not significant?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_157.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_157.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 005: Legitimacy of type synonyms

The C Standard does not clearly indicate when the spelling of a type name is or
is not significant; in other words, when a type name may be replaced by another
type name representing the same type.

**Part 1**

Subclause 6.5.4.3 reads in part:

The special case of `void` as the only item in the list specifies that the
function has no parameters.

Subclause 6.7.1 reads in part:

(except in the special case of a parameter list consisting of a single parameter
of type `void`, in which there shall not be an identifier).

In both cases, the word `void` is set in the typeface used to indicate C code.

In the code:

```c
typedef void Void;
 extern int f (Void);
 int f (Void) { return 0; }
```

is the declaration on line 2 strictly conforming, and is the external definition
on line 3 strictly conforming?

**Part 2**

Subclause 5.1.2.2.1 reads in part: It can be defined with no parameters:

```c
                int main (void) { /* ... */ }
```

Is the following definition of `main` strictly conforming?

```c
typedef int word;
 word main (void) { /* ... */ }
```

**Part 3**

Are there any circumstances in which a typedef name is not permitted instead of
the type it is a synonym for? If so, what are they?

---

Comment from WG14 on 1997-09-23:

Proposed Response

A synonym is always acceptable, except that a function definition may not use a
typedef for the function type.

### Response

**Part 1**

Both function declarations are strictly conforming.

Subclause 6.7.1 makes clear that it is a single parameter having the type `void`
(as opposed to use of the `void` keyword) that indicates that a function takes
no parameters.

For clarity, Subclause 6.5.4.3 should be rephrased to emphasize that it is the
type `void`, not the keyword `void`that matters.

### Future Change

In Subclause 6.5.4.3,

Change

> "The special case of `void` as the only item in the list specifies that the
> function has no parameters."

To

> "The special case of an unnamed parameter of type `void` as the only item in the
> list specifies that the function has no parameters."

**Part 2**

Yes, the definition of `main` is strictly conforming.

**Part 3**

A synonym is not acceptable in these cases:

1. A function definition may not use a typedef for the function type:
   > ```c
   > typedef void F(void);
   > extern F g { } /* Invalid */
   > ```
2. A typedef may not be combined with another type specifier:
   > ```c
   > typedef int I;
   >  short I x;     /* Invalid */
   > ```


</div>


---

---

<div id="issue0158">

## Issue 0158: Are the semantics for the explicit conversion of null pointer constants defined?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0155](log_c90.md#issue0155)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_158.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_158.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 006: Null pointer conversions

The C Standard does not define semantics for the explicit conversion of null
pointer constants and for the implicit conversion of null pointers.

Subclause 6.2.2.3 reads in part:

If a null pointer constant is assigned to or compared for equality to a pointer,
the constant is converted to a pointer of that type. Such a pointer, called a
null pointer, is guaranteed to compare unequal to a pointer to any object or
function.

Two null pointers, converted through possibly different sequences of casts to
pointer types, shall compare equal.

Given the definitions:

```c
void * p = 0;
 int  * i = 0;
```

does the standard guarantee that the expression `p == i` always evaluates to 1?
The last quoted sentence only covers casts, and not the implicit conversions of
that comparison. Conversely, do the expressions `(int *)0` or `1 ? 0 : (int *)0`
yield null pointers of type `(int *)`? The quoted text does not cover the case
of a null pointer constant being converted other than by assignment or in a test
for equality, yet expressions such as these are widely used.

### Suggested Technical Corrigendum:

In subclause 6.2.2.3, change:

> Two null pointers, converted through possibly different sequences of casts to
> pointer types, shall compare equal.

to:

> Conversion of a null pointer to another pointer type yields a null pointer of
> that type. Any two null pointers shall compare equal.

Alternatively, a common term could be introduced to more conveniently describe
the various forms of pointer that cannot be dereferenced. In this case, replace
the last two paragraphs of subclause 6.2.2.3 with:

> For each pointer type, there exist values which can participate in assignment
> and equality operations, but which cause undefined behavior if dereferenced.
> These are referred to as *undereferenceable.* An undereferenceable pointer
> compares unequal to any other value of the same pointer type. For each pointer
> type, one particular undereferenceable pointer value is called the *null
> pointer.* \[Footnote: Since there is only one such value, all null pointers of
> the same type compare equal.]
>
> An integral constant expression with the value 0, or such an expression cast to
> type `void *`, is called a *null pointer constant.* If a null pointer constant
> is assigned to or compared for equality with an object of pointer type, or cast
> to pointer type, then it is converted to the null pointer of that type.
> Conversion of a null pointer to another pointer type produces the null pointer
> of that type.

If the answer to [Defect Report #155](log_c90.md#issue0155) is that *unique* means
*different each time,* then replace the last two sentences of subclause 7.10.3
with:

> If the size of the space requested is zero, an undereferenceable pointer is
> returned. It is implementation-defined whether this is always a null pointer or
> whether the implementation attempts to produce a value distinct from any other
> undereferenceable pointer. Any pointer value returned by an allocation can be
> passed to the free function; if the value is not a null pointer, it becomes
> indeterminate. \[Footnote: A subsequent allocation may return a pointer value
> with the same bit pattern, but a strictly conforming program can't detect this.]
> The value of a pointer that refers to any part of a freed object is also
> indeterminate.

---

Comment from WG14 on 1997-09-23:

### Response

Does the Standard guarantee that `p == i`? Yes.

Does `(int *) 0` yield a null pointer of type `int *`? Yes.

Does `1 ? 0 : (int *) 0` yield a null pointer of type `int *`? Yes.

The intent of the part of Subclause 6.2.2.3 that you quote is to state that a
null pointer results when a null pointer constant is converted to a pointer. By
singling out assignment and comparison, the Standard is misleadingly specific.
This should be clarified in the Standard.

### Future Change

In Subclause 6.2.2.3

Change

> "If a null pointer constant is assigned to or compared for equality to a
> pointer, the constant is converted to a pointer of that type. Such a pointer,
> called a null pointer, is guaranteed to compare unequal to a pointer to any
> object or function.
>
> Two null pointers, converted through possibly different sequences of casts to
> pointer types, shall compare equal."

To

> "The result of converting a null pointer constant to a pointer type is called a
> null pointer. A null pointer is guaranteed to compare unequal to a pointer to
> any object or function.
>
> Conversion of a null pointer to another pointer type yields a null pointer of
> that type. Any two null pointers shall compare equal."

In Subclause 6.3.9

Add a new paragraph after the first paragraph in Semantics

> "If a null pointer constant is compared for equality to a pointer, the constant
> is converted to the type of the pointer."


</div>


---

---

<div id="issue0159">

## Issue 0159: Is the introduction to the C Standard confusing?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_159.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_159.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.* Defect
Report UK 007: Consistency of the C Standard Defects exist in the way the
Standard refers to itself.

**Part 1**

The introduction to the C Standard reads in part:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.

While it is not, strictly speaking, an inconsistency for text that is not part
of the C Standard to specify which text is part of the C Standard, it is
confusing for this to be the case when other text that *looks* like part of the
C Standard isn't \- the examples and footnotes.

In particular, placing this information \- necessary for interpreting the text
of the C Standard itself \- outside that text causes a danger that, when some
other document is produced that purports to contain the full text of the C
Standard, the Introduction will be omitted while the footnotes and examples are
retained. A reader of such a document who is not aware of the text of the
introduction will then be misled as to the C Standard's contents. Whilst this is
not the responsibility of ISO, it is another reason for regularizing the
situation.

Note that this has definitely happened in the case of *The Annotated ANSI C
Standard* by Herbert Schildt, and I have been informed (but have not confirmed)
that it has also happened with the version of the C Standard distributed by the
Australian National Body.

**Part 2**

The introduction to the C Standard reads in part:

The language clause (clause 7\) ... The library clause (clause 8\) ...

These references are wrong.

### Suggested Technical Corrigendum:

In the Introduction, change:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.

The language clause (clause 7\) ...

The library clause (clause 8\) ...

to:

As specified in the definitions and conventions clause (clause 3), this
introduction, the examples, the footnotes, the references, and the annexes are
not part of this International Standard.

The language clause (clause 6\) ...

The library clause (clause 7\) ...

Insert at the start of clause 3:

The introduction, the examples, the footnotes, the references, and the annexes
are not part of this International Standard.


</div>


---

---

<div id="issue0160">

## Issue 0160: It is unclear what applications can and cannot do with identifiers that are reserved?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_160.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_160.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 008: Reservation of identifiers

The C Standard is unclear in its description of what applications can and cannot
do with identifiers that are reserved to the implementation for certain uses.

Subclause 7.1.3 reads in part:

Each identifier with file scope listed in any of the following subclauses
(including the future library directions) is reserved for use as an identifier
with file scope in the same name space if any of its associated headers is
included.

Does this include reservation as macros? In particular, is the following code:

```c
#include  <stddef.h>
 #define size_t 42
```

strictly conforming, or could it cause a redefinition of the macro `size_t`?
Similarly, can another macro legitimately defined by `stddef.h` (such as
`offsetof`) include `size_t` in its replacement list, so that:

```c
#include  <stddef.h>
 #undef size_t
 #define size_t 42
  /* ... */
 offsetof (struct_type, field)
```

fails to expand correctly? It is not clear how the wording of Footnote 91
applies, and this is in any case not part of the C Standard (except in Australia
:-).

---

Comment from WG14 on 1997-09-23:

### Suggested Future Change

In subclause 7.1.3, Reserved Identifiers, change bullet 2 to:

> All identifiers that begin with an underscore are always reserved for use as
> macros and as identifiers with file scope in both the ordinary and tag name
> spaces.

Change bullet 5 to:

> Each identifier with file scope listed in any of the following subclauses
> (including the Future library directions) is reserved for use as a macro and as
> an identifier with file scope in the same name space if any of its associated
> headers is included.


</div>


---

---

<div id="issue0161">

## Issue 0161: Is the wording of subclause 7.13 unclear?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_161.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_161.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 009: Details of reserved symbols

The wording of subclause 7.13 is unclear.

Does the term *any combination* in subclause 7.13 include the empty combination?
In other words, are names like `E2`, `tom`, `LC_X`, and `memo` reserved?

---

Comment from WG14 on 1997-09-23:

### Response

Yes, the term "any combination" does include the empty combination so names such
as those cited are reserved. We believe that having the "any combination"
language in parenthetical remarks rather than as part of the main text makes is
sufficiently clear that it is just the prefix that is important in determining
whether a name is reserved or not.


</div>


---

---

<div id="issue0162">

## Issue 0162: Is the description of the static objects used by `time.h` functions misleading?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_162.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_162.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 010: `gmtime` and `localtime`

The C Standard's description of the static objects used by `time.h` functions is
misleading.

Subclause 7.12.3 reads in part:

these functions return values in one of two static objects: a broken-down time
structure and an array of `char`. Execution of any of the functions may
overwrite the information returned in either of these objects by any of the
other functions.

Does this mean that, for example, `localtime` and `gmtime` must share a single
broken-down time structure, and so the value returned from `gmtime`, if not a
null pointer, must equal the value returned from `localtime` (and this value
cannot change during execution of the program)?

The wording *the other functions* also implies that a call to `gmtime` can
overwrite a previous call to `localtime`, but not a previous call to `gmtime`.
This is clearly ridiculous.

### Suggested Technical Corrigendum

In subclause 7.12.3, change:

these functions return values in one of two static objects: a broken-down time
structure and an array of `char`. Execution of any of the functions may
overwrite the information returned in either of these objects by any of the
other functions.

to:

these functions each return a pointer to an object of static storage duration
after assigning a value to it. Execution of any of these functions may overwrite
the information returned in any of these objects by a previous call to any of
these functions.

---

Comment from WG14 on 1997-09-23:

### Future Change

In subclause 7.12.3, change:

> Except for the `strftime` function, these functions return values in one of two
> static objects: a broken-down time structure and an array of `char`. Execution
> of any of the functions may overwrite the information returned in either of
> these objects by any of the other functions.

to:

> Except for the `strftime` function, these functions each return a pointer to one
> of two types of static objects: a broken-down time structure or an array of
> `char`. Execution of any of the functions that return a pointer to one of these
> object types may overwrite the information in any object of the same type
> pointed to by the value returned from any previous call to any of them.


</div>


---

---

<div id="issue0163">

## Issue 0163: Is it clear whether the use of an undeclared identifier as a primary expression requires a diagnostic message to be issued?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_163.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_163.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 011: Undeclared identifiers

The C Standard is not clear on whether the use of an undeclared identifier as a
primary expression requires a diagnostic message.

Subclause 6.3.1 states that:

An identifier is a primary expression, provided it has been declared as
designating an object (in which case it is an lvalue) or a function (in which
case it is a function designator).

It has been suggested that if no declaration of some identifier is visible in
the current scope when that identifier appears in an expression, the identifier
is not a primary expression, and therefore the syntax of subclause 6.3.1 is
violated (in other words, there is no valid parse for the expression). This
would thus require a diagnostic for an undeclared identifier.

Is this interpretation correct? If yes, then it needs to be made clear that this
does not prevent a previously undeclared function from being called by a
strictly conforming program (see 6.3.2.2).

If not, does an undeclared identifier require a diagnostic, and if so, why? If
not, is this a deliberate policy, or is it a defect that needs correction?

---

Comment from WG14 on 1997-09-23:

### Response

Identifiers that designate objects must be declared and be visible before they
can be primary expressions (subclause 6.1.2.1, *An identifier is visible (i.e.,
can be used) ...*). A reasonable person could interpret that if no declaration
of some identifier is visible, the identifier cannot be a primary expression.
This affects undeclared identifiers that are intended to be used as implicitly
declared functions. The Committee's intent is that the C Standard be read in the
following order:

1\. **6.3.1 Primary expressions**

**Syntax**

```c
          primary-expression:
                         identifier
```

2\. **6.3.2.2 Function calls**

**Semantics**

If the expression that precedes the parenthesized argument list in a function
call consists solely of an identifier, and if no declaration is visible for this
identifier, the identifier is implicitly declared exactly as if, in the
innermost block containing the function call, the declaration

```c
extern int identifier();
```

appeared.

3\. 6.3.1 **Primary expressions**

**Semantics**

An identifier is a primary expression, provided it has been declared as
designating ... a function (...).

However, a reasonable person may not interpret the current wording as having
that meaning (i.e., it might not be read in that order). This needs to be
clarified in the next revision of the C Standard.

### Response

Identifiers must be declared and visible before they can be primary expressions
(Subclause 6.1.2.1, "An identifier is visible (i.e., can be used) ..."). If no
declaration of some identifier is visible, the identifier cannot be a primary
expression, and a diagnostic is required for a violation of the syntax rule.

Note that a declaration of an identifier might be visible due to the identifier
being implicitly declared (Subclause 6.3.2.2). This should be clarified in the
Standard.

### Future Change

In Subclause 6.3.1, first paragraph in "Semantics"

Change

> "An identifier is a primary expression, provided is has been declared as
> designating an object (in which case it is an lvalue) or a function (in which
> case it is a function designator)."

To

> "An identifier is a primary expression, provided is has been declared as
> designating an object (in which case it is an lvalue) or implicitly**\*** or
> explicitly declared as designating a function (in which case it is a function
> designator)."
>
> The **\*** above references the new footnote:

"See 6.3.2.2."


</div>


---

---

<div id="issue0164">

## Issue 0164: Is there a constraint to prevent declarations involving types not defined by subclause 6.1.2.5?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_164.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_164.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 012: Bad declarations

The C Standard contains no constraint to prevent declarations involving types
not defined by subclause 6.1.2.5.

Subclause 6.5 states that:

A declaration shall declare at least a declarator, a tag, or the members of an
enumeration. There seems to be no constraint that a declarator generate a
well-formed type. Consider the following code:

```c
  {
         int a [][5];            /* Line A */
         int x, b [][5];         /* Line B */
         }
```

Neither `a` nor `b` has a well formed type. Does line A nevertheless *declare a
declarator,* or does it violate the quoted constraint? If it violates the
constraint, does line B?

Is it the intent of the C Standard that an ill-formed (but syntactically
correct) type generate a diagnostic? If so, then is there one, or does one need
to be added?

---

Comment from WG14 on 1997-09-23:

### Response

Line A declares a declarator. It violates the semantics described in subclause
6.5:

If an identifier for an object is declared with no linkage, the type for the
object shall be complete by the end of its declarator, ...

But no diagnostic is required.


</div>


---

---

<div id="issue0165">

## Issue 0165: Is the wording of subclause 6.5.2.3 concerning tags defective?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0013.05](log_c90.md#issue0013.05)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_165.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_165.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 013: Tags and incomplete types

The wording of subclause 6.5.2.3 concerning tags is defective in a number of
ways.

**Part 1**

The first paragraph states that:

If this declaration of the tag is visible, a subsequent declaration that uses
the tag and that omits the bracketed list specifies the declared structure,
union, or enumerated type.

This neither handles the case of a type name (for example, in the operand of the
`sizeof` operator), nor does it make it clear whether or not the rule applies
within the braces of the first declaration (the tag is in scope from the open
brace).

In other words, it fails to address either occurrence of `struct tag *` in the
following code:

```c
  {
         struct tag { int i [sizeof (struct tag *)]; };
         int j [sizeof (struct tag *)];
 /* ... */
        }
```

**Part 2**

The second paragraph does not adequately distinguish between type specifiers
which refer to an incomplete type and those which refer to a type in an outer
scope. For example, in the following code, it fails to indicate whether or not
all the uses of the tag refer to the same type:

```c
struct tag;
 struct tag *p;
         {
         struct tag *q;
         /* ... */
         }
        struct tag { int member; };
```

**Part 3**

The handling of enumerated types before their content is defined is also
unclear; this was covered to some extent in [DR013Q5](log_c90.md#issue0013.05) and
subsequent discussion on the WG14 mailing list.

For example, what is the status of the following code:

```c
enum tag { e = sizeof (enum tag ******) };
```

or of:

```c
enum tag { e0, e1, e2, e3 };
         {
         enum tag2 { e4 = sizeof (enum tag); };
         enum tag  { e5 = sizeof (enum tag); };
        }
```

If an enumeration tag cannot be used before the end of the list defining its
contents, a diagnostic ought to be required.

**Part 4**

If the same tag is used in a type specifier with a contents list twice in the
same scope, it is unclear whether or not a diagnostic is required. It could be
argued that, since this is forbidden by the semantics in subclause 6.5.2.3, it
is not excluded from the second constraint of subclause 6.5, and so a diagnostic
is required by that constraint. However, this may be viewed as clutching at
straws. An explicit constraint should be added.

### Suggested Technical Corrigendum

Rather than making piecemeal changes to address each issue separately, the whole
subclause should be rewritten. Footnote numbers have been chosen to match the
present footnotes.

**Constraints**

A specific type shall have its content defined at most once.

A type specifier of the form

```c
          enum identifier
```

without an enumerator list shall only appear when the type it specifies is
complete.

**Semantics**

All declarations of structure, union, or enumerated types that have the same
scope and use the same tag declare the same type. The type is incomplete \[63]
until the closing brace of the list defining the content, and complete
thereafter. \[Footnote 63: An incomplete type may only be used when the size of
an object of that type is not needed.]

\[Append the present wording, or see Defect Report CA-2-09 \- submitted
independently \- for alternative wording.]

Two declarations of structure, union, or enumerated types which are in different
scopes or use different tags declare distinct types. Each declaration of a
structure, union, or enumerated type which does not include a tag declares a
distinct type.

A type specifier of the form

```c
          struct-or-union identifier    { struct-declaration-list }
                                  opt or
            enum identifier    { enumerator-list }
                                 opt
```

declares a structure, union, or enumerated type. The list defines the *structure
content, union content,* or *enumeration content.* If an identifier is provided
\[64], the type specifier also declares the identifier to be the tag of that
type. \[Footnote 64: If there is no identifier, the type can, within the
translation unit, only be referred to by the declaration of which it is a part.
Of course, when the declaration is of a typedef name, subsequent declarations
can make use of that typedef name to declare objects having the specified
structure, union, or enumerated type.]

A declaration of the form

```c
          struct-or-union identifier ;
```

specifies a structure or union type and declares the identifier as the tag of
that type \[62]. \[Footnote 62: A similar construction with `enum` does not
exist.]

If a type specifier of the form

```c
          struct-or-union identifier
```

occurs other than as part of one of the above constructions, and no other
declaration of the identifier as a tag is visible, then it declares a structure
or union type which is incomplete at this point, and declares the identifier as
the tag of that type \[62].

If a type specifier of the form

```c
          struct-or-union identifier
```

or

```c
          enum identifier
```

occurs other than as part of one of the above constructions, and a declaration
of the identifier as a tag is visible, then it specifies the same type as that
other declaration, and does not redeclare the tag.


</div>


---

---

<div id="issue0166">

## Issue 0166: Do constraints that require something to be an lvalue place an unacceptable burden on the implementation?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0076](log_c90.md#issue0076)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_166.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_166.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 014: Meaning of lvalue

Constraints that require something to be an lvalue place an unacceptable burden
on the implementation.

Subclause 6.2.2.1 states in part:

An lvalue is an expression (with an object type or an incomplete type other than
`void`) that designates an object.

Given the declaration

```c
int a[10], i;
```

the expression `a[i]` designates an object, and is thus an lvalue, if and only
if `i` has a value between 0 and 9 inclusive (see [Defect Report
#076](log_c90.md#issue0076) for further details). Now consider the Constraint in subclause
6.3.3.2:

The operand of the unary `&` operator shall be either a function designator or
an lvalue that designates an object ...

This means that the expression `&a[i]` is a constraint violation whenever `i`
has a value outside the range 0 to 9 inclusive, and that therefore a diagnostic
is required, at run-time!

The defect is that the operand of the unary `&` operator does not need to be an
lvalue that designates an object, but rather an lvalue which, if evaluated with
its operands having suitable values, could designate an object.

There are probably other parts of the C Standard with the same problem, such as
subclauses 6.3.2.4, 6.3.3.1, and 6.3.16.


</div>


---

---

<div id="issue0167">

## Issue 0167: The `n` conversion specifier in subclause 7.9.6.2 made by TC1, [Defect Report #014, Question 2](log_c90.md#issue0014.02), should be applied to subclause 7.9.6.1

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0014.02](log_c90.md#issue0014.02)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_167.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_167.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 015: Consistency of the C Standard

The change to the `n` conversion specifier in subclause 7.9.6.2 made by TC1,
[Defect Report #014, Question 2](log_c90.md#issue0014.02), should also be applied to
subclause 7.9.6.1. Change:

No argument is converted.

to:

No argument is converted, but one is consumed.

If the conversion specification with this conversion specifier is not one of
`%n`, `%ln`, or `%hn`, the behavior is undefined.

In addition, an entry something like:

A `%n` conversion specification for the `fprintf` or `fscanf` functions is not
one of `%n`, `%ln`, or `%hn` (7.9.6.1, 7.9.6.2).

should be added to Annex G.2.


</div>


---

---

<div id="issue0168">

## Issue 0168: The change to subclause 6.3 made by TC1, [Defect Report #053, Question 1](log_c90.md#issue0053), should also be applied in Annex .2 (page 200\)

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0053](log_c90.md#issue0053)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_168.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_168.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 016: Consistency of the C Standard

The change to subclause 6.3 made by TC1, [Defect Report #053, Question
1](log_c90.md#issue0053), should also be applied in Annex G.2 (page 200).


</div>


---

---

<div id="issue0169">

## Issue 0169: Is the description of the replacement of trigraphs contradictory?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_169.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_169.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 017: Trigraphs

The C Standard's description of the replacement of trigraphs is contradictory.

Subclause 5.2.1.1 reads in part:

All occurrences in a source file of the following sequences of three characters
(called trigraph sequences \[7]) are replaced with the corresponding single
character... Each `?` that does not begin one of the trigraphs listed above is
not changed.

Since the second character in each trigraph is a `?` that does not begin the
trigraph, this is a direct contradiction.

### Suggested Technical Corrigendum

Change the last sentence of the cited text to:

Each `?` that is not part of one of the trigraphs listed above is not changed.

---

Comment from WG14 on 1997-09-23:

Proposed Response

The C Standard is clear enough as is. A trigraph begins with two question marks,
so it is reasonable to refer to both of them as beginning the trigraph.


</div>


---

---

<div id="issue0170">

## Issue 0170: Are the description of operators and punctuators is confusing, and are the constraints contradictory?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_170.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_170.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 018: Operators and punctuators

The description of operators and punctuators is confusing, and the constraints
are contradictory.

Subclause 6.1.5 Constraints reads:

The operators `[ ]`, `( )`, and `? :` shall occur in pairs, possibly separated
by expressions. The operators `#` and `##` shall occur in macro-defining
preprocessing directives only.

Subclause 6.1.6 Constraints reads:

The punctuators `[ ]`, `( )`, and `{ }` shall occur (after translation phase 4\)
in pairs, possibly separated by expressions, declarations, or statements. The
punctuator `#` shall occur in preprocessing directives only.

Consider the code:

```c
#define STR(x)  #x
 STR ({)    /* Line A */
 STR (:)    /* Line B */
 STR ([)    /* Line C */
 STR (#)    /* Line D */
```

Line A appears to be strictly conforming, since the first sentence of the
constraint of subclause 6.1.6 does not apply during translation phase 4\. Line B
violates the constraint of subclause 6.1.5. The interpretation of line C depends
on whether the `[` is an operator or a punctuator!

Line D violates both constraints, but again which one depends on whether it is
an operator or a punctuator, something which is not made clear in the C
Standard.

Assuming that the intent was for line B to be strictly conforming, and that
*(after translation phase 4\)* was inadvertently omitted from subclause 6.1.5,
the first sentence of each of these Constraints is nugatory, as any program that
violates these constraints also violates a syntax rule elsewhere in clause 6\.
The remaining sentences would be better expressed as part of subclause 6.8. It
is also arguable that the concepts of operator and punctuator are better merged
at the syntactic level, and separated out only at the semantic level.

### Suggested Technical Corrigendum

Delete the Constraints of subclauses 6.1.5 and 6.1.6. Add the following
constraint to 6.8:

A `#` preprocessing token shall only occur within a replacement-list or when
permitted by the syntax rules of this subclause. A `##` preprocessing token
shall only occur within a replacement-list.

Add to the end of the Constraints of subclause 6.1, just before the full stop:

, and shall not be `#` or `##`

**Alternative Suggested Technical Corrigendum**

In subclause 6.1 syntax, delete both occurrences of *operator* and replace the
second occurrence of *punctuator* by *pp-punctuator.*

Delete subclauses 6.1.5 and 6.1.6, and replace them by the following:

**6.1.5 Punctuators**

**Syntax:**

```c
  pp-punctuator:
                 punctuator
                 pp-only-punctuator
         pp-only-punctuator: one of
                 # ## defined
         punctuator:
                 [ ] ( ) { } . -
                 ++ -- & * + - ~ ! sizeof
                 / %            =  = == != ^ | && ||
                 ? : , : ; ...
                 = *= /= %= += -=   =   = &= ^= |=
```

**Semantics:**

A punctuator is a symbol that has independent syntactic and semantic
significance. Depending on context, some punctuators may specify an operation to
be performed (an *evaluation*) that yields a value, or yields a designator, or
produces a side-effect, or a combination thereof; in that context, the
punctuator is known as an *operator.* An *operand* is an entity on which an
operator acts.

Add the following constraint to 6.8:

A `#` preprocessing token shall only occur within a replacement-list or when
permitted by the syntax rules of this subclause. A `##` preprocessing token
shall only occur within a replacement-list.

---

Comment from WG14 on 1997-09-23:

### Response

This is a work in progress item.

General feeling is that this should be cleaned up for C9X along the lines of
C\+\+ pp-punctuator grammar.

Suggested response is to add words to subclause 6.1.5 along the lines, *shall
occur in pairs within expressions...*


</div>


---

---

<div id="issue0171">

## Issue 0171: Is it possible to create implementations with unreasonable arrangements of integral types?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Cross-references: [0069](log_c90.md#issue0069)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_171.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_171.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 019: Ranges of integral types

It appears to be possible to create implementations with unreasonable
arrangements of integral types.

Subclause 6.1.2.5 states various rules which allow the following deductions to
be made:

> ```c
> SCHAR_MAX  = SHRT_MAX
>  SHRT_MAX   = INT_MAX
>  INT_MAX    = LONG_MAX
>  SCHAR_MIN  = SHRT_MIN
>  SHRT_MIN   = INT_MIN
>  INT_MIN    = LONG_MIN
>  SCHAR_MAX  = UCHAR_MAX
>  SHRT_MAX   = USHRT_MAX
>  INT_MAX    = UINT_MAX
>  LONG_MAX   = ULONG_MAX
> ```

and, depending on the interpretation of the term *the same amount of storage:*

> ```c
> sizeof (unsigned short) == sizeof (short)
>  sizeof (unsigned int)   == sizeof (int)
>  sizeof (unsigned long)  == sizeof (long)
> ```

However, (based on the preliminary discussions of [Defect Report
#069](log_c90.md#issue0069), which allow padding bits in integral types) there does not
appear to be any requirement for the following:

> ```c
> UCHAR_MAX  = USHRT_MAX
>  USHRT_MAX  = UINT_MAX
>  UINT_MAX   = ULONG_MAX
>  sizeof (short)  = sizeof (int)
>  sizeof (int)    = sizeof (long)
>  UCHAR_MAX  = INT_MAX
> ```

The first five of these are necessary to allow reasonable deductions to be made
about the behavior of types in the presence of padding bits (for example, that
unsigned long can hold any value representable in any integral type). The sixth
is necessary to allow the `<ctype.h>` functions to behave sensibly (it is also
assumed by example 2 of subclause 5.1.2.3).

### Suggested Technical Corrigendum

In subclause 6.1.2.5, change in the fourth paragraph:

> In the list of signed integer types above, the range of values of each type is a
> subrange of the values of the next type in the list

. to:

> In the list of signed integer types above, the range of values of each type is a
> subrange of the values of the next type in the list, and the size of an object
> of each type is not greater than the size of an object of the next type in the
> list.

Add to the fifth paragraph:

> The range of values of each unsigned integer type is a subrange of the next type
> (in the list `unsigned char`, `unsigned short`, `unsigned int`, `unsigned
> long`).

Add to the fifth or eighth paragraph:

> The range of values of the type `unsigned char` is a subrange of the values of
> the type `int`.

---

Comment from WG14 on 1997-09-23:

### Response

This is a work in progress item.

Summary: Explicit statements are not made about ranges for all types. It can be
argued that you can derive this information from the C Standard.

Does the Committee want to make explicit statements about all relationships,
specifically the unsigned types?


</div>


---

---

<div id="issue0172">

## Issue 0172: Does the description for the relational and equality operators contain defects?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_172.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_172.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 020: Relational and equality operators

The descriptions of these operators with pointer operands contain several
defects.

**Part 1**

Consider the following code:

```c
char *s = "a string";
 if (s  = NULL)
 	/* ... */
```

Subclause 6.3.8, Semantics reads in part:

If the objects pointed to are not members of the same aggregate or union object,
the result is undefined

This implies that the comparison causes undefined behavior.

Subclause 6.2.2.1 reads in part:

Such a pointer, called a null pointer, is guaranteed to compare unequal to a
pointer to any object or function.

This implies that the comparison is guaranteed to yield *false.*

This is a direct contradiction.

**Part 2**

Subclause 6.3.9, Semantics reads in part:

Where the operands have types and values suitable for the relational operators,
the semantics detailed in subclause 6.3.8 apply.

This can reasonably be read as meaning that, whenever the constraints of
subclause 6.3.8 apply, its definitions should be used, even if that would result
in undefined behavior. (The phrase *and values* can reasonably be read as
requiring only that the pointers both be to objects; it does not necessarily
mean that the result of the comparison must be defined.)

It further reads:

If two pointers to object or incomplete types are both null pointers, they
compare equal. If two pointers to object or incomplete types compare equal, they
both are null pointers, or both point to the same object, or both point one past
the last element of the same array object.

This says nothing about the comparison of any other pointers. Now, subclause
3.16 reads in part:

Undefined behavior is otherwise indicated ... by the omission of any explicit
definition of behavior.

Thus, in:

```c
int a, b;
 &a == &b
```

the comparison causes undefined behavior!

**Part 3**

The above citation does not allow for the case where one pointer is to an
object, and the other is one past the last element of an array object. If an
implementation places two independent objects in adjacent memory locations, a
pointer to one would equal a pointer to just past the other on many common
implementations.

If these pointers are not to be viewed as identical, then the wording is
defective.

### Suggested Technical Corrigendum

In subclause 6.2.2.1, replace the cited text by:

Such a pointer is called a null pointer.

In subclause 6.3.9, replace the first paragraph of the semantics by:

The operators `==` (equal to) and `!=` (not equal to) shall yield 1 if the
specified relation is true and 0 if it is false. If the operands have types
suitable for those of a relational operator and values that would not cause
undefined behavior if used with a relational operator, then the result of the
comparison, either greater than or less than (both implying not equal to) or
equal to, is the same as with a relational operator.

Insert at the start of the second paragraph:

Otherwise the operands are pointers, and they shall compare either equal or not
equal.

If part 3 is viewed as an issue, then in the same paragraph change:

or both point one past the last element of the same array object.

to:

both point one past the last element of the same array object, or one points one
past the last element of some array object and the other points to the first
element of a different array object.

---

Comment from WG14 on 1997-09-23:

### Response

This is a work in progress item.

Summary of Part 1:

The standard does not currently state what happens with relational operators
when you compare the address of an object with a null pointer.

We know from the citation from subclause 6.2.2.3 that a null pointer is
guaranteed to yield false when compared with a pointer to an object.

It is explicitly undefined behaviour to use relational operators on two pointer
that are not members of the same aggregate or union object. However it is
unstated whether a null pointer compares greater or less than the address of an
object and hence is implicitly undefined behaviour.

Is this the desired behaviour?

Note: the current C\+\+ clause has the following wording:

> If two pointers of the same type point to different objects or functions, or
> only one of them is null, they compare unequal.

This wording gives the possibility for C and C\+\+ to give different results.

Summary of Part 2:

Discussion from Nashua is as follows:

The intent is that pointers to distinct object will compare unequal, The C
Standard will be fixed in a future revision.


</div>


---

---

<div id="issue0173">

## Issue 0173: What is the meaning of *line number* when a token is split over more than one physical source line?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_173.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_173.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 021: Line numbers

The concept of *line number* is not clearly defined when a token is split over
more than one physical source line.

Subclause 6.8.4 reads in part:

The line number of the current source line is one greater than the number of
new-line characters read or introduced in translation phase 1 (5.1.1.2) while
processing the source file to the current token.

Subclause 6.8.8 reads in part:

`__LINE__` \- The line number of the current source line (a decimal constant).

Consider the program:

```c
#include  stdio.h
 #define LNER __LINE__

 /* The next statement is on physical source lines 6 to 8 */
 int east_coast = __\
 LINE\
 __;
 /* The next statement is on physical source lines 10 to 13 */
 int main_line = L\
 N\
 E\
 R;

 int main (void)
 {
         printf ("%d %d\n", east_coast, main_line);
         return 0;
 }
```

In each of the two substitutions, it is unclear whether the line number is the
number of new-lines read to the *start of* the current token, or to the *end of*
the current token, or to a specified point within the current token.

What is the output of this program?


</div>


---

---

<div id="issue0174">

## Issue 0174: Is there a number of errors in the usual arithmetic conversions section?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_174.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_174.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 022: Implicit conversions

The wording dealing with the usual arithmetic conversions contains a number of
errors; while the correct meaning is usually clear, a strict reading of the C
Standard shows some contradictions and/or unwanted side-effects.

Subclause 6.2.1.5 reads in part:

Many binary operators that expect operands of arithmetic type cause conversions
and yield result types in a similar way. The purpose is to yield a common type,
which is also the type of the result.

Subclause 6.3.15 reads in part:

The second operand is evaluated only if the first compares unequal to 0; the
third operand is evaluated only if the first compares equal to 0; the value of
the second or third operand (whichever is evaluated) is the result.

If both the second and third operands have arithmetic type, the usual arithmetic
conversions are performed to bring them to a common type and the result has that
type ... in which case the other operand is converted to type pointer to void,
and the result has that type.

These citations have several defects:

The relational and equality operators apply the usual arithmetic conversions,
but not to yield the type of result.

The conditional operator `?:` is not a binary operator, but is specified as
performing the usual arithmetic conversions.

The concept of conversions applies only to a value; subclause 6.3.15 is
therefore contradicting itself when it calls for both the second and third
operands to be subject to conversion when only one of them is evaluated.

The value of the result of the `?:` operator is not necessarily that of the
second or third operand, as the value may have been converted (possibly yielding
a different value).

### Suggested Technical Corrigendum

In subclause 6.2.1.5, change the cited sentences to:

Many operators cause the same pattern of conversions to be applied to two
operands of arithmetic type. The purpose is to yield a common type, which,
unless explicitly stated otherwise, is also the type of the operator's result.

In 6.3.15, change the cited wording to:

The second operand is evaluated only if the first compares unequal to 0; the
third operand is evaluated only if the first compares equal to 0; the result of
the operator is the value of the second or third operand (whichever is
evaluated), converted to the type described below.

If both the second and third operands have arithmetic type, the type that the
usual arithmetic conversions would yield if applied to those two operands is the
type of the result ... in which case the type of the result is pointer to
`void`.


</div>


---

---

<div id="issue0175">

## Issue 0175: Is the `sscanf` example added by TC1 wrong?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_175.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_175.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 023: Correction to Technical Corrigendum 1

An example added by TC1 is wrong.

TC1 added the following example to subclause 7.9.6.2:

In:

```c
  #include  stdio.h
         /* ..... */
         int d1, d2, n1, n2, i;
        i = sscanf("123", "%d%n%n%d", &d1, &n1, &n2, &d2);
```

the value 123 is assigned to `d1` and the value 3 to `n1`. Because `%n` can
never get an input failure the value of 3 is also assigned to `n2`. The value of
`d2` is not affected. The value 3 is assigned to `i`.

This should set `i` to 1, not 3, as `%n` does not affect the returned assignment
count.

### Suggested Technical Corrigendum

In the example, change:

The value 3 is assigned to `i`.

to:

The value 1 is assigned to `i`.


</div>


---

---

<div id="issue0176">

## Issue 0176: Are rules concerning whether `#error` generates a diagnostic contradictory?

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_176.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_176.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 024: Diagnostics for `#error`

The rules concerning whether `#error` generates a diagnostic are contradictory.

Subclause 5.1.1.3 reads:

> A conforming implementation shall produce at least one diagnostic message
> (identified in an implementation-defined manner) for every translation unit that
> contains a violation of any syntax rule or constraint. Diagnostic messages need
> not be produced in other circumstances.

Subclause 6.8.5 reads:

> **Semantics**
>
> A preprocessing directive of the form
>
> ```c
>           # error pp-tokens    new-line                   opt
> ```

causes the implementation to produce a diagnostic message that includes the
specified sequence of preprocessing tokens.

Since this is not in a Constraints section, these two statements directly
contradict one another. Furthermore, the second statement can be read as
applying to a `#error` directive that is excluded by a false `#if` condition.

### Suggested Technical Corrigendum

In subclause 6.8.5, replace the entire subclause with:

**Constraints**

A `#error` preprocessing directive shall not occur in a translation unit. Any
diagnostic message generated because of the violation of this constraint
\[Footnote: The intent of this subclause is that `#error` indicates that
translation should fail. As stated in subclause 5.1.1.3, a translation unit
excludes lines within the *false* side of `#if` ... `#else` ... `#endif`
groups.] shall include the sequence of preprocessing tokens in the directive.


</div>


---

---

<div id="issue0177">

## Issue 0177: A Preprocessing directives question

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_177.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_177.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 025: Preprocessing directives

Preprocessing directives are not removed from the translation unit at any point
during or after translation phase 4, and thus wreck the syntax analysis in
translation phase 7\.

Subclause 5.1.1.1 reads in part:

A source file together with all the headers and source files included via the
preprocessing directive `#include`, less any source lines skipped by any of the
conditional inclusion preprocessing directives, is called a *translation unit.*

Nothing here, in the description of translation phase 4, or in subclause 6.8,
states that any preprocessing directive is removed (except for `#include`, which
is *replaced*).

Consider the source file:

```c
#define QUIT return 0
 #if 0
 This is some junk
 #else
  int main (void)
 {
         puts ("Hello world\n");
 #endif
          QUIT;
 }
```

The translation unit resulting at the end of translation phase 4 is thus:

```c
#define QUIT return 0
 #if 0
 #else
 int main (void)
  {
         puts ("Hello world\n");
 #endif
         return 0;
 }
```

and this clearly does not match the syntax of *translation-unit* in subclause
6.7.

### Suggested Technical Corrigendum

In subclause 5.1.1.2, add at the end of the description of translation phase 4:
All preprocessing directives are then removed from the translation unit.


</div>


---

---

<div id="issue0178">

## Issue 0178: Why does [Defect Report #051](log_c90.md#issue0051) and [Defect Report #073](log_c90.md#issue0073) answer the same question differently?

Authors: Frank Farance, WG14  
Date: 1996-02-06  
Status: Closed  
Cross-references: [0051](log_c90.md#issue0051), [0073](log_c90.md#issue0073)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_178.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_178.html)

Is the following conforming?

```c
  struct x
                 {
                 char y[1];
                  };
         struct x *z;

         z = (struct x *) malloc(sizeof (*z) + 100);
         z- y[5] = '?';
```

[Defect Report #051](log_c90.md#issue0051) states that this isn't conforming behavior
because the pointer arithmetic for the larger structure might not be compatible
with a smaller structure. Thus, it recommends the *safer* idiom:

```c
#define HUGE_ARR  1000    /* or bigger than ever needed */
         struct x
                 {
                 char y[HUGE_ARR];
                 };
         struct x *z;

         z = (struct x *) malloc(sizeof (*z) + 100);
         z- y[5] = '?';
```

However, [Defect Report #073](log_c90.md#issue0073) states that the *safer* idiom is
undefined behavior because it is possible to implement the operator `-` as first
fetching all of `*z`, then selecting `y[5]` from it. This approach would cause
access to unallocated memory. Thus, the operation produces undefined behavior.

These responses are inconsistent. At the Oct 95 meeting in Nashua NH, WG14
indicated that it wanted to designate this as undefined behavior.


</div>


---

