# C90: issue summary

**This issue summary has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|0001|[Do functions return values by copying?](issue0001.md)|Fixed in C90 TC1|
|0002|[Should `\` be escaped within macro actual parameters?](issue0002.md)|Closed|
|0003.01|[Are preprocessing numbers too inclusive?](issue0003.01.md)|Closed|
|0003.02|[Should white space surround macro substitutions?](issue0003.02.md)|Closed|
|0003.03|[Is an empty macro argument a constraint violation?](issue0003.03.md)|Closed|
|0003.04|[Should preprocessing directives be permitted within macro invokations?](issue0003.04.md)|Closed|
|0004|[Are multiple definitions of unused identifiers with external linkage permitted?](issue0004.md)|Fixed in C90|
|0005|[May a conforming implementation define and recognize a pragma which would change the semantics of the language?](issue0005.md)|Closed|
|0006|[How does `strtoul` behave when presented with a subject sequence that begins with a minus sign?](issue0006.md)|Closed|
|0007|[Are declarations of the form `struct` *`tag`* permitted after *`tag`* has already been declared?](issue0007.md)|Closed|
|0008.01|[Is dead-store elimination permitted near `setjmp`?](issue0008.01.md)|Closed|
|0008.02|[Should volatile functions be added?](issue0008.02.md)|Closed|
|0009|[Are typedef names sometimes ambiguous in parameter declarations?](issue0009.md)|Fixed in C90 TC1|
|0010|[Is the typedef to an incomplete type valid?](issue0010.md)|Closed|
|0011.01|[When do the types of multiple external declarations get formed into a composite type?](issue0011.01.md)|Fixed in C90 TC1|
|0011.02|[Does `extern` link to a static declaration that is not visible?](issue0011.02.md)|Fixed in C90 TC1|
|0011.03|[Are implicit initializers for tentative array definitions syntactically valid?](issue0011.03.md)|Closed|
|0011.04|[Does an incomplete array get completed as a tentative definition?](issue0011.04.md)|Fixed in C90 TC1|
|0012|[Can one take the address of a void expression?](issue0012.md)|Closed|
|0013.01|[How does one form the composite type of mixed array and pointer parameter types?](issue0013.01.md)|Fixed in C90 TC1|
|0013.02|[Is compatible properly defined for recursive types?](issue0013.02.md)|Closed|
|0013.03|[What is the composite type of an enumeration and an integer?](issue0013.03.md)|Closed|
|0013.04|[When is a struct type complete?](issue0013.04.md)|Fixed in C90 TC1|
|0013.05|[When is the `sizeof` an enumeration type known?](issue0013.05.md)|Fixed in C90 TC1|
|0014.01|[Is `setjmp` a macro or a function?](issue0014.01.md)|Closed|
|0014.02|[How does `fscanf("%n")` behave on end-of-file?](issue0014.02.md)|Fixed in C90 TC1|
|0015|[How does an unsigned plain bitfield promote?](issue0015.md)|Closed|
|0016.01|[Can a tentative definition have an incomplete type initially?](issue0016.01.md)|Closed|
|0016.02|[Can you implicitly initialize a union when null pointers have nonzero bit patterns?](issue0016.02.md)|Fixed in C90 TC1|
|0017.01|[Are newlines permitted within macro invocations in preprocessing directives?](issue0017.01.md)|Fixed in C90 TC1|
|0017.02|[Should the absence of function `main` be explicitly undefined?](issue0017.02.md)|Fixed in C90 TC1|
|0017.03|[Does a constraint violation win over undefined behavior?](issue0017.03.md)|Fixed in C90 TC1|
|0017.04|[Do numeric escape sequences map from source to execution character sets?](issue0017.04.md)|Closed|
|0017.05|[When are character constants implementation defined?](issue0017.05.md)|Closed|
|0017.06|[Are register aggregates permitted?](issue0017.06.md)|Fixed in C90 TC1|
|0017.07|[What is the scope and uniqueness of `size_t`?](issue0017.07.md)|Closed|
|0017.08|[What types are compatible with pointer to `void`?](issue0017.08.md)|Closed|
|0017.09|[What is the type of an assignment expression?](issue0017.09.md)|Fixed in C90 TC1|
|0017.10|[When is the `sizeof` an object needed?](issue0017.10.md)|Closed|
|0017.11|[Is `struct t; struct t;` valid?](issue0017.11.md)|Closed|
|0017.12|[How do typedefs parse in function prototypes?](issue0017.12.md)|Fixed in C90 TC1|
|0017.13|[How does `register` affect compatibility of function parameters?](issue0017.13.md)|Closed|
|0017.14|[`const void` type as a parameter](issue0017.14.md)|Fixed in C90 TC1|
|0017.15|[When do array parameters get converted to pointers?](issue0017.15.md)|Fixed in C90 TC1|
|0017.16|[Are subarrays of arrays distinct objects?](issue0017.16.md)|Fixed in C90 TC1|
|0017.17|[How do you initialize the first member of a union if it has no name?](issue0017.17.md)|Fixed in C90 TC1|
|0017.18|[Are `f()` and `f(void)` compatible?](issue0017.18.md)|Closed|
|0017.19|[Are macro expansions ambiguous?](issue0017.19.md)|Fixed in C90 TC1|
|0017.20|[Is the scope of macro parameters defined in the right place?](issue0017.20.md)|Closed|
|0017.21|[Is translation phase 4 defined unambiguously?](issue0017.21.md)|Closed|
|0017.22|[Does the rescan of a macro invocation also perform token pasting?](issue0017.22.md)|Fixed in C90 TC1|
|0017.23|[How long does `blue paint` persist on macro names?](issue0017.23.md)|Closed|
|0017.24|[Can subclause 7.1.2 be better expressed?](issue0017.24.md)|Fixed in C90 TC1|
|0017.25|[Should *must* appear in footnotes?](issue0017.25.md)|Closed|
|0017.26|[Are unnamed union members required to be initialized?](issue0017.26.md)|Fixed in C90 TC1|
|0017.27|[Does the `#` flag alter zero stripping of `%g` in `fprintf`?](issue0017.27.md)|Closed|
|0017.28|[Does `errno` get stored before library functions return?](issue0017.28.md)|Closed|
|0017.29|[When does conversion failure occur in floating-point `fscanf` input?](issue0017.29.md)|Fixed in C90 TC1|
|0017.30|[Do `fseek/fsetpos` require values from successful calls to `ftell/fgetpos`?](issue0017.30.md)|Fixed in C90 TC1|
|0017.31|[Are object sizes always in bytes?](issue0017.31.md)|Closed|
|0017.32|[Are `strcmp/strncmp` defined when `char` is signed?](issue0017.32.md)|Closed|
|0017.33|[Are `strcmp/strncmp` defined for strings of differing length](issue0017.33.md)|Closed|
|0017.34|[Is `strtok` described properly?](issue0017.34.md)|Closed|
|0017.35|[When is a physical source line created?](issue0017.35.md)|Closed|
|0017.36|[Is a function returning `const void` defined?](issue0017.36.md)|Closed|
|0017.37|[What is the type of a function call?](issue0017.37.md)|Fixed in C90 TC1|
|0017.38|[What is an iteration control structure or selection control structure?](issue0017.38.md)|Fixed in C90 TC1|
|0017.39|[Are header names tokens outside include directives?](issue0017.39.md)|Fixed in C90 TC1|
|0018|[Does `fscanf` recognize literal multibyte characters properly?](issue0018.md)|Closed|
|0019|[Are printing characters implementation defined?](issue0019.md)|Closed|
|0020|[Is the relaxed Ref/Def linkage model conforming?](issue0020.md)|Closed|
|0021|[What is the result of `printf("%#.4o", 345)`?](issue0021.md)|Fixed in C90 TC1|
|0022|[What is the result of `strtod("100ergs", &ptr)`?](issue0022.md)|Fixed in C90 TC1|
|0023|[If 99,999 is larger than `DBL_MAX_10_EXP`, what is the result of `strtod("0.0e99999", &ptr)`?](issue0023.md)|Closed|
|0024|[For `strtod`, what does `"C"` locale mean?](issue0024.md)|Closed|
|0025|[What is meant by *representable floating-point value?*](issue0025.md)|Closed|
|0026|[Can one use other than the basic C character set in a strictly conforming program?](issue0026.md)|Closed|
|0027|[May a standard conforming implementation add identifier characters?](issue0027.md)|Fixed in C90 TC1|
|0028|[What are the aliasing rules for dynamically allocated objects?](issue0028.md)|Closed|
|0029|[Must compatible structs/unions have the same tag in different translation units?](issue0029.md)|Closed|
|0030|[May `sin(DBL_MAX)` set `errno` to `EDOM`?](issue0030.md)|Closed|
|0031|[How are exceptions handled in constant expressions?](issue0031.md)|Closed|
|0032|[Can an implementation permit a comma operator in a constant expression?](issue0032.md)|Closed|
|0033|[Must a conforming implementation diagnose *shall* violations outside **Constraints**?](issue0033.md)|Closed|
|0034.01|[Does size information evaporate when a declaration goes out of scope, even for objects with external linkage?](issue0034.01.md)|Fixed in C90 TC1|
|0034.02|[If so, can one then write conflicting declarations in disjoint scopes?](issue0034.02.md)|Closed|
|0035.01|[Can one declare an enumeration or struct tag as part of an old-style parameter declaration?](issue0035.01.md)|Closed|
|0035.02|[If so, what is the scope of enumeration tags and constants declared in old-style parameter declarations?](issue0035.02.md)|Closed|
|0036|[May a floating-point constant be represented with more precision than implied by its type?](issue0036.md)|Closed|
|0037|[Can UNICODE or ISO 10646 be used as a multibyte code?](issue0037.md)|Closed|
|0038|[What happens when macro replacement creates adjacent tokens that can be taken as a single token?](issue0038.md)|Closed|
|0039.01|[Must `MB_CUR_MAX` be one in the `"C"` locale?](issue0039.01.md)|Closed|
|0039.02|[Should `setlocale(LC_ALL, NULL)` return `"C"` in the `"C"` locale?](issue0039.02.md)|Closed|
|0040.01|[What is the composite type of `f(int)` and `f(const int)`?](issue0040.01.md)|Fixed in C90 TC1|
|0040.02|[Is an implementation that fails to equal the value of an environmental limit conforming?](issue0040.02.md)|Fixed in C90 TC1|
|0040.03|[Is an **Environmental Constraint** a constraint?](issue0040.03.md)|Closed|
|0040.04|[Should the response to [Defect Report #017, Q39](issue0017.39.md) be reconsidered?](issue0040.04.md)|Closed|
|0040.05|[Can a conforming implementation accept `long long`?](issue0040.05.md)|Closed|
|0040.06|[Can one use `offsetof(struct t1, mbr)` before `struct t1` is completely defined?](issue0040.06.md)|Closed|
|0040.07|[Can `sizeof` be applied to earlier parameter names in a prototype, or to earlier fields in a struct?](issue0040.07.md)|Closed|
|0040.08|[What arithmetic can be performed on a `char` holding a defined character literal value?](issue0040.08.md)|Closed|
|0040.09|[Should the response to [Defect Report #017, Q27](issue0017.27.md) be reconsidered?](issue0040.09.md)|Closed|
|0041|[Are `'A'` through `'Z'` always `isupper` in all locales?](issue0041.md)|Closed|
|0042.01|[Does `memcpy` define a (sub)object?](issue0042.01.md)|Closed|
|0042.02|[If so, how big is the object defined by `memcpy`?](issue0042.02.md)|Closed|
|0042.03|[How big is a string object defined by the `str*` functions?](issue0042.03.md)|Closed|
|0043.01|[Can `NULL` be defined as `4-4`?](issue0043.01.md)|Fixed in C90 TC1|
|0043.02|[Can an identifier that starts with an underscore be defined as a macro in a source file that includes at least one standard header?](issue0043.02.md)|Closed|
|0044.01|[What does it mean to say that the type of `offsetof` is `size_t`?](issue0044.01.md)|Closed|
|0044.02|[Must the expansion of a standard header be a strictly conforming program?](issue0044.02.md)|Closed|
|0044.03|[Does expanding `offsetof` result in a non-strictly conforming program?](issue0044.03.md)|Closed|
|0044.04|[Can one use `offsetof` in a strictly conforming program?](issue0044.04.md)|Closed|
|0044.05|[Is `offsetof` the only standard macro that renders a program not strictly conforming?](issue0044.05.md)|Closed|
|0045|[Can one `freopen` an already closed file?](issue0045.md)|Closed|
|0046|[May a typedef be redeclared as a parameter outside an old-style function parameter list?](issue0046.md)|Closed|
|0047|[Can an array parameter have elements of incomplete type?](issue0047.md)|Closed|
|0048|[Is `abort` compatible with POSIX?](issue0048.md)|Closed|
|0049|[Can `strxfrm` produce a longer translation string?](issue0049.md)|Closed|
|0050|[Does a proper definition of `wchar_t` need to be in scope to write a wide-character literal?](issue0050.md)|Closed|
|0051|[Can one index beyond the declared end of an array if space is allocated for the extra elements?](issue0051.md)|Closed|
|0052.01|[Should the `mktime` example use `(time_t)-1` instead of `-1`?](issue0052.01.md)|Fixed in C90 TC1|
|0052.02|[Is the index entry for static correct?](issue0052.02.md)|Fixed in C90 TC1|
|0052.03|[Does the C Standard come with a Rationale, as indicated in Footnote 1?](issue0052.03.md)|Closed|
|0053|[Do the aliasing rules cover accesses to different function pointers properly?](issue0053.md)|Fixed in C90 TC1|
|0054|[What is the behavior of various string functions with a specified length of zero?](issue0054.md)|Fixed in C90 TC1|
|0055|[Must the `SIG*` macros have distinct values?](issue0055.md)|Fixed in C90 TC1|
|0056|[How accurate must floating-point arithmetic be?](issue0056.md)|Closed|
|0057|[Must there exist a user-accessible integral type for every pointer?](issue0057.md)|Closed|
|0058|[What is the number of digits in a number that can be processed by the `scanf` family and the `strtod` family?](issue0058.md)|Closed|
|0059|[Must an incomplete type be completed by the end of a translation unit?](issue0059.md)|Closed|
|0060|[When an array of `char` (or `wchar_t`) is initialized with a string literal that contains fewer characters than the array, are the remaining elements of the array initialized?](issue0060.md)|Fixed in C90 TC2|
|0061|[Interpretation of white space in the format string of a scan statement](issue0061.md)|Closed|
|0062|[Can the `rename` function alway return a failure?](issue0062.md)|Closed|
|0063|[This is [Defect Report 056](issue0056.md)](issue0063.md)|Closed|
|0064|[What is a null pointer constant?](issue0064.md)|Closed|
|0065|[Can strictly conforming programs contain locales other that the 'C' locale?](issue0065.md)|Fixed in C90 TC2|
|0066|[A set of locale questions](issue0066.md)|Closed|
|0067|[Are the definitions of types clear?](issue0067.md)|Closed|
|0068|[When are values of the type `char` treated as `signed`or `nonnegative` integers](issue0068.md)|Closed|
|0069|[What is the meaning of *pure binary numeration system*?](issue0069.md)|Closed|
|0070|[Can non-compatible types be used interchangeabily for function arguments?](issue0070.md)|Closed|
|0071|[Are all enumerated types compatible with a single type?](issue0071.md)|Fixed in C90 TC2|
|0072|[What is the definition of an object?](issue0072.md)|Closed|
|0073|[Another definition of an object question](issue0073.md)|Closed|
|0074|[Can the alignment of an object that is a member of a structure be different from the alignment of an object of the same type that is not a member of a structure?](issue0074.md)|Closed|
|0075|[What is the alignment of allocated memory?](issue0075.md)|Closed|
|0076|[A set of pointers to the end of arrays questions](issue0076.md)|Closed|
|0077|[Is the address of an object constant throughout its lifetime?](issue0077.md)|Closed|
|0078|[May optimizer invoke the as-if rule to rearrange code?](issue0078.md)|Closed|
|0079|[Is the address of a standard library function the same in different translation units?](issue0079.md)|Closed|
|0080|[Questions on merging of string constants](issue0080.md)|Fixed in C90 TC2|
|0081|[What is the result of the left shift operator `E1 < E2`, when `E1` is signed?](issue0081.md)|Closed|
|0082|[Many varargs questions](issue0082.md)|Fixed in C90 TC2|
|0083|[A use of library functions question](issue0083.md)|Fixed in C90 TC2|
|0084|[When is an incomplete type in function declaration a parameter?](issue0084.md)|Closed|
|0085|[Is the return from `main` equivalent to calling `exit`?](issue0085.md)|Fixed in C90 TC2|
|0086|[At object-like macros in system headers conforming?](issue0086.md)|Closed|
|0087|[Is the order of evaluation when there are no sequence points well defined?](issue0087.md)|Closed|
|0088|[Are two incomplete structure types with a (lexically) identical tag always compatible?](issue0088.md)|Closed|
|0089|[When does multiple definitions of a macro require a diagnositc message?](issue0089.md)|Fixed in C90 TC2|
|0090|[Multibyte characters in formats question](issue0090.md)|Closed|
|0091|[Does a locale with multibye characters conform?](issue0091.md)|Closed|
|0092|[Are the remaining elements in a partially initalized string guaranteed to be zero?](issue0092.md)|Closed|
|0093|[Can a conforming freestanding implementation reserve identifiers?](issue0093.md)|Fixed in C90 TC2|
|0094|[Is there an inconsistency between the constraints on passing values versus returning values?](issue0094.md)|Closed|
|0095|[Are the initialization constraints clear?](issue0095.md)|Closed|
|0096|[Can the element type in an array declarator be a non-object type?](issue0096.md)|Closed|
|0097|[Can the `type` argument of the `offsetof` macro be an incomplete type?](issue0097.md)|Closed|
|0098|[Do function types and incomplete type have size?](issue0098.md)|Closed|
|0099|[What does the term *assignment operator* mean?](issue0099.md)|Closed|
|0100|[Do functions return values by copying?](issue0100.md)|Fixed in C90 TC1|
|0101|[Are mismatched qualifiers allowed?](issue0101.md)|Fixed in C90 TC2|
|0102|[Does a constraint violation win over undefined behavior?](issue0102.md)|Closed|
|0103|[Is a diagnostic required when formal parameters for functions are incomplete types?](issue0103.md)|Closed|
|0104|[When is an incomplete type in function declaration a parameter?](issue0104.md)|Closed|
|0105|[Does a constraint violation win over undefined behavior?](issue0105.md)|Fixed in C90 TC1|
|0106|[Can one take the address of a void expression?](issue0106.md)|Closed|
|0107|[Several `assert` questions](issue0107.md)|Closed|
|0108|[Is it conforming to allow macros to make keywords?](issue0108.md)|Closed|
|0109|[Does the C Standard draw any significant distinction between *undefined values* and *undefined behavior*?](issue0109.md)|Closed|
|0110|[When is a formal parameter having array-of-non-object type not conforming?](issue0110.md)|Closed|
|0111|[A question on conversion of *pointer-to-qualified* type values to type `(void*)` values](issue0111.md)|Closed|
|0112|[A Null pointer constants and relational comparison question](issue0112.md)|Closed|
|0113|[Return expressions in functions declared to return qualified `void` questions](issue0113.md)|Closed|
|0114|[Initialization of multi-dimensional `char` array object questions](issue0114.md)|Closed|
|0115|[What it means to *declare* a declarator?](issue0115.md)|Closed|
|0116|[Is a diagnostic required when the address of a `reigister` arry is implicitly taken?](issue0116.md)|Closed|
|0117|[Abstract semantics, sequence points, and expression evaluation question](issue0117.md)|Closed|
|0118|[When is the `sizeof` an enumeration type known?](issue0118.md)|Fixed in C90 TC2|
|0119|[Is a diagnostic required on an example of an initialization of multi-dimensional array objects](issue0119.md)|Closed|
|0120|[Semantics of assignment to (and initialization of) bit-fields question](issue0120.md)|Closed|
|0121|[What is ment by *size required* when convering a ponter value to an integral type?](issue0121.md)|Closed|
|0122|[Is the *type* of a bit-field totally independent from its *width*?](issue0122.md)|Closed|
|0123|[“*Type categories*” and qualified types question](issue0123.md)|Closed|
|0124|[What is the difference between casts to *a void type* versus casts to the `void` type?](issue0124.md)|Fixed in C90 TC2|
|0125|[When are declarations useing `extern` *(qualified)* `void` not conforming?](issue0125.md)|Closed|
|0126|[What does *synonym* mean with respect to typedef names?](issue0126.md)|Closed|
|0127|[What is the composite type of an enumeration and an integer?](issue0127.md)|Closed|
|0128|[Editorial issue relating to tag declarations in type specifiers](issue0128.md)|Closed|
|0129|[When is name spaces of tags are shared?](issue0129.md)|Closed|
|0130|[When is data read from a text stream guaranteed to match what was written to the stream?](issue0130.md)|Closed|
|0131|[What is the meaning of *const-qualification*?](issue0131.md)|Fixed in C90 TC2|
|0132|[Can undefined behavior occur at translation time, or only at run time?](issue0132.md)|Closed|
|0133|[Undefined behavior not previously listed in subclause G2](issue0133.md)|Closed|
|0134|[Is *error number* an undefined term?](issue0134.md)|Closed|
|0135|[Is the `SVR4 fwrite` different?](issue0135.md)|Closed|
|0136|[Does `mktime` yield a -1 in the *spring-forward* gap when `tm_isdst` is -1?](issue0136.md)|Closed|
|0137|[Is `printf("%.1f", -0.01)` required to produce `0.0` , `-0.0`, or are both acceptable?](issue0137.md)|Closed|
|0138|[What are the storage durations?](issue0138.md)|Fixed in C90 TC2|
|0139|[Is an incomplete type compatible with the completed type?](issue0139.md)|Fixed in C90 TC2|
|0140|[What does *performed* and *other operation* mean?](issue0140.md)|Closed|
|0141|[What does `EOF` mean in `<stdio.h>`?](issue0141.md)|Closed|
|0142|[Is it permitted to `#undef` a reserved macro name?](issue0142.md)|Fixed in C99|
|0143|[What are the definitions of file opening modes?](issue0143.md)|Fixed in C99|
|0144|[Can the white space preceeding the initial `#` of a preprocessing directive be derived from macro expansion?](issue0144.md)|Fixed in C99|
|0145|[The four possible forms for a constant expression are not consistent](issue0145.md)|Fixed in C99|
|0146|[Does the constraint of 6.1.2 serve a purpose?](issue0146.md)|Fixed in C99|
|0147|[Is there a requirement for a sequence point to occur within a library function?](issue0147.md)|Fixed in C99|
|0148|[Is it clear when it is permitted to declare a library function?](issue0148.md)|Closed|
|0149|[Is the term *variable* defiend?](issue0149.md)|Fixed in C99|
|0150|[Are programs containing `char array[] = "Hello, World";` strictly conforming?](issue0150.md)|Fixed in C99|
|0151|[Is the out from `printf("%#.0o", 0);` ambiguous?](issue0151.md)|Closed|
|0152|[Can `longjmp` be used to return from a signal handler invoked other than through `abort` or `raise`?](issue0152.md)|Closed|
|0153|[Is there a problem with empty arguments in macro calls?](issue0153.md)|Closed|
|0154|[What restrictions apply to implementation-defined entities?](issue0154.md)|Closed|
|0155|[Is the word *unique* in subclause 7.10.3 ambiguous?](issue0155.md)|Fixed in C99|
|0156|[Should calls to `fsetpos` with positions in closed and reopened streams be undefined?](issue0156.md)|Fixed in C99|
|0157|[Is it clearly indicated when the spelling of a type name is or is not significant?](issue0157.md)|Fixed in C99|
|0158|[Are the semantics for the explicit conversion of null pointer constants defined?](issue0158.md)|Fixed in C99|
|0159|[Is the introduction to the C Standard confusing?](issue0159.md)|Fixed in C99|
|0160|[It is unclear what applications can and cannot do with identifiers that are reserved?](issue0160.md)|Fixed in C99|
|0161|[Is the wording of subclause 7.13 unclear?](issue0161.md)|Closed|
|0162|[Is the description of the static objects used by `time.h` functions misleading?](issue0162.md)|Fixed in C99|
|0163|[Is it clear whether the use of an undeclared identifier as a primary expression requires a diagnostic message to be issued?](issue0163.md)|Closed|
|0164|[Is there a constraint to prevent declarations involving types not defined by subclause 6.1.2.5?](issue0164.md)|Closed|
|0165|[Is the wording of subclause 6.5.2.3 concerning tags defective?](issue0165.md)|Fixed in C99|
|0166|[Do constraints that require something to be an lvalue place an unacceptable burden on the implementation?](issue0166.md)|Fixed in C99|
|0167|[The `n` conversion specifier in subclause 7.9.6.2 made by TC1, [Defect Report #014, Question 2](issue0014.02.md), should be applied to subclause 7.9.6.1](issue0167.md)|Fixed in C99|
|0168|[The change to subclause 6.3 made by TC1, [Defect Report #053, Question 1](issue0053.md), should also be applied in Annex .2 (page 200\)](issue0168.md)|Fixed in C99|
|0169|[Is the description of the replacement of trigraphs contradictory?](issue0169.md)|Closed|
|0170|[Are the description of operators and punctuators is confusing, and are the constraints contradictory?](issue0170.md)|Fixed in C99|
|0171|[Is it possible to create implementations with unreasonable arrangements of integral types?](issue0171.md)|Fixed in C99|
|0172|[Does the description for the relational and equality operators contain defects?](issue0172.md)|Fixed in C99|
|0173|[What is the meaning of *line number* when a token is split over more than one physical source line?](issue0173.md)|Closed|
|0174|[Is there a number of errors in the usual arithmetic conversions section?](issue0174.md)|Fixed in C99|
|0175|[Is the `sscanf` example added by TC1 wrong?](issue0175.md)|Fixed in C99|
|0176|[Are rules concerning whether `#error` generates a diagnostic contradictory?](issue0176.md)|Closed|
|0177|[A Preprocessing directives question](issue0177.md)|Fixed in C99|
|0178|[Why does [Defect Report #051](issue0051.md) and [Defect Report #073](issue0073.md) answer the same question differently?](issue0178.md)|Closed|

