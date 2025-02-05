# C90: issue summary

**This issue summary has been automatically converted from the original issue lists and some formatting may not have been preserved.**

|Issue|Summary|Status|
|-|-|-|
|[0001](issue0001.md)|Do functions return values by copying?|Fixed in C90 TC1|
|[0002](issue0002.md)|Should `\` be escaped within macro actual parameters?|Closed|
|[0003.01](issue0003.01.md)|Are preprocessing numbers too inclusive?|Closed|
|[0003.02](issue0003.02.md)|Should white space surround macro substitutions?|Closed|
|[0003.03](issue0003.03.md)|Is an empty macro argument a constraint violation?|Closed|
|[0003.04](issue0003.04.md)|Should preprocessing directives be permitted within macro invokations?|Closed|
|[0004](issue0004.md)|Are multiple definitions of unused identifiers with external linkage permitted?|Fixed in C90|
|[0005](issue0005.md)|May a conforming implementation define and recognize a pragma which would change the semantics of the language?|Closed|
|[0006](issue0006.md)|How does `strtoul` behave when presented with a subject sequence that begins with a minus sign?|Closed|
|[0007](issue0007.md)|Are declarations of the form `struct` *`tag`* permitted after *`tag`* has already been declared?|Closed|
|[0008.01](issue0008.01.md)|Is dead-store elimination permitted near `setjmp`?|Closed|
|[0008.02](issue0008.02.md)|Should volatile functions be added?|Closed|
|[0009](issue0009.md)|Are typedef names sometimes ambiguous in parameter declarations?|Fixed in C90 TC1|
|[0010](issue0010.md)|Is the typedef to an incomplete type valid?|Closed|
|[0011.01](issue0011.01.md)|When do the types of multiple external declarations get formed into a composite type?|Fixed in C90 TC1|
|[0011.02](issue0011.02.md)|Does `extern` link to a static declaration that is not visible?|Fixed in C90 TC1|
|[0011.03](issue0011.03.md)|Are implicit initializers for tentative array definitions syntactically valid?|Closed|
|[0011.04](issue0011.04.md)|Does an incomplete array get completed as a tentative definition?|Fixed in C90 TC1|
|[0012](issue0012.md)|Can one take the address of a void expression?|Closed|
|[0013.01](issue0013.01.md)|How does one form the composite type of mixed array and pointer parameter types?|Fixed in C90 TC1|
|[0013.02](issue0013.02.md)|Is compatible properly defined for recursive types?|Closed|
|[0013.03](issue0013.03.md)|What is the composite type of an enumeration and an integer?|Closed|
|[0013.04](issue0013.04.md)|When is a struct type complete?|Fixed in C90 TC1|
|[0013.05](issue0013.05.md)|When is the `sizeof` an enumeration type known?|Fixed in C90 TC1|
|[0014.01](issue0014.01.md)|Is `setjmp` a macro or a function?|Closed|
|[0014.02](issue0014.02.md)|How does `fscanf("%n")` behave on end-of-file?|Fixed in C90 TC1|
|[0015](issue0015.md)|How does an unsigned plain bitfield promote?|Closed|
|[0016.01](issue0016.01.md)|Can a tentative definition have an incomplete type initially?|Closed|
|[0016.02](issue0016.02.md)|Can you implicitly initialize a union when null pointers have nonzero bit patterns?|Fixed in C90 TC1|
|[0017.01](issue0017.01.md)|Are newlines permitted within macro invocations in preprocessing directives?|Fixed in C90 TC1|
|[0017.02](issue0017.02.md)|Should the absence of function `main` be explicitly undefined?|Fixed in C90 TC1|
|[0017.03](issue0017.03.md)|Does a constraint violation win over undefined behavior?|Fixed in C90 TC1|
|[0017.04](issue0017.04.md)|Do numeric escape sequences map from source to execution character sets?|Closed|
|[0017.05](issue0017.05.md)|When are character constants implementation defined?|Closed|
|[0017.06](issue0017.06.md)|Are register aggregates permitted?|Fixed in C90 TC1|
|[0017.07](issue0017.07.md)|What is the scope and uniqueness of `size_t`?|Closed|
|[0017.08](issue0017.08.md)|What types are compatible with pointer to `void`?|Closed|
|[0017.09](issue0017.09.md)|What is the type of an assignment expression?|Fixed in C90 TC1|
|[0017.10](issue0017.10.md)|When is the `sizeof` an object needed?|Closed|
|[0017.11](issue0017.11.md)|Is `struct t; struct t;` valid?|Closed|
|[0017.12](issue0017.12.md)|How do typedefs parse in function prototypes?|Fixed in C90 TC1|
|[0017.13](issue0017.13.md)|How does `register` affect compatibility of function parameters?|Closed|
|[0017.14](issue0017.14.md)|`const void` type as a parameter|Fixed in C90 TC1|
|[0017.15](issue0017.15.md)|When do array parameters get converted to pointers?|Fixed in C90 TC1|
|[0017.16](issue0017.16.md)|Are subarrays of arrays distinct objects?|Fixed in C90 TC1|
|[0017.17](issue0017.17.md)|How do you initialize the first member of a union if it has no name?|Fixed in C90 TC1|
|[0017.18](issue0017.18.md)|Are `f()` and `f(void)` compatible?|Closed|
|[0017.19](issue0017.19.md)|Are macro expansions ambiguous?|Fixed in C90 TC1|
|[0017.20](issue0017.20.md)|Is the scope of macro parameters defined in the right place?|Closed|
|[0017.21](issue0017.21.md)|Is translation phase 4 defined unambiguously?|Closed|
|[0017.22](issue0017.22.md)|Does the rescan of a macro invocation also perform token pasting?|Fixed in C90 TC1|
|[0017.23](issue0017.23.md)|How long does `blue paint` persist on macro names?|Closed|
|[0017.24](issue0017.24.md)|Can subclause 7.1.2 be better expressed?|Fixed in C90 TC1|
|[0017.25](issue0017.25.md)|Should *must* appear in footnotes?|Closed|
|[0017.26](issue0017.26.md)|Are unnamed union members required to be initialized?|Fixed in C90 TC1|
|[0017.27](issue0017.27.md)|Does the `#` flag alter zero stripping of `%g` in `fprintf`?|Closed|
|[0017.28](issue0017.28.md)|Does `errno` get stored before library functions return?|Closed|
|[0017.29](issue0017.29.md)|When does conversion failure occur in floating-point `fscanf` input?|Fixed in C90 TC1|
|[0017.30](issue0017.30.md)|Do `fseek/fsetpos` require values from successful calls to `ftell/fgetpos`?|Fixed in C90 TC1|
|[0017.31](issue0017.31.md)|Are object sizes always in bytes?|Closed|
|[0017.32](issue0017.32.md)|Are `strcmp/strncmp` defined when `char` is signed?|Closed|
|[0017.33](issue0017.33.md)|Are `strcmp/strncmp` defined for strings of differing length|Closed|
|[0017.34](issue0017.34.md)|Is `strtok` described properly?|Closed|
|[0017.35](issue0017.35.md)|When is a physical source line created?|Closed|
|[0017.36](issue0017.36.md)|Is a function returning `const void` defined?|Closed|
|[0017.37](issue0017.37.md)|What is the type of a function call?|Fixed in C90 TC1|
|[0017.38](issue0017.38.md)|What is an iteration control structure or selection control structure?|Fixed in C90 TC1|
|[0017.39](issue0017.39.md)|Are header names tokens outside include directives?|Fixed in C90 TC1|
|[0018](issue0018.md)|Does `fscanf` recognize literal multibyte characters properly?|Closed|
|[0019](issue0019.md)|Are printing characters implementation defined?|Closed|
|[0020](issue0020.md)|Is the relaxed Ref/Def linkage model conforming?|Closed|
|[0021](issue0021.md)|What is the result of `printf("%#.4o", 345)`?|Fixed in C90 TC1|
|[0022](issue0022.md)|What is the result of `strtod("100ergs", &ptr)`?|Fixed in C90 TC1|
|[0023](issue0023.md)|If 99,999 is larger than `DBL_MAX_10_EXP`, what is the result of `strtod("0.0e99999", &ptr)`?|Closed|
|[0024](issue0024.md)|For `strtod`, what does `"C"` locale mean?|Closed|
|[0025](issue0025.md)|What is meant by *representable floating-point value?*|Closed|
|[0026](issue0026.md)|Can one use other than the basic C character set in a strictly conforming program?|Closed|
|[0027](issue0027.md)|May a standard conforming implementation add identifier characters?|Fixed in C90 TC1|
|[0028](issue0028.md)|What are the aliasing rules for dynamically allocated objects?|Closed|
|[0029](issue0029.md)|Must compatible structs/unions have the same tag in different translation units?|Closed|
|[0030](issue0030.md)|May `sin(DBL_MAX)` set `errno` to `EDOM`?|Closed|
|[0031](issue0031.md)|How are exceptions handled in constant expressions?|Closed|
|[0032](issue0032.md)|Can an implementation permit a comma operator in a constant expression?|Closed|
|[0033](issue0033.md)|Must a conforming implementation diagnose *shall* violations outside **Constraints**?|Closed|
|[0034.01](issue0034.01.md)|Does size information evaporate when a declaration goes out of scope, even for objects with external linkage?|Fixed in C90 TC1|
|[0034.02](issue0034.02.md)|If so, can one then write conflicting declarations in disjoint scopes?|Closed|
|[0035.01](issue0035.01.md)|Can one declare an enumeration or struct tag as part of an old-style parameter declaration?|Closed|
|[0035.02](issue0035.02.md)|If so, what is the scope of enumeration tags and constants declared in old-style parameter declarations?|Closed|
|[0036](issue0036.md)|May a floating-point constant be represented with more precision than implied by its type?|Closed|
|[0037](issue0037.md)|Can UNICODE or ISO 10646 be used as a multibyte code?|Closed|
|[0038](issue0038.md)|What happens when macro replacement creates adjacent tokens that can be taken as a single token?|Closed|
|[0039.01](issue0039.01.md)|Must `MB_CUR_MAX` be one in the `"C"` locale?|Closed|
|[0039.02](issue0039.02.md)|Should `setlocale(LC_ALL, NULL)` return `"C"` in the `"C"` locale?|Closed|
|[0040.01](issue0040.01.md)|What is the composite type of `f(int)` and `f(const int)`?|Fixed in C90 TC1|
|[0040.02](issue0040.02.md)|Is an implementation that fails to equal the value of an environmental limit conforming?|Fixed in C90 TC1|
|[0040.03](issue0040.03.md)|Is an **Environmental Constraint** a constraint?|Closed|
|[0040.04](issue0040.04.md)|Should the response to [Defect Report #017, Q39](issue0017.39.md) be reconsidered?|Closed|
|[0040.05](issue0040.05.md)|Can a conforming implementation accept `long long`?|Closed|
|[0040.06](issue0040.06.md)|Can one use `offsetof(struct t1, mbr)` before `struct t1` is completely defined?|Closed|
|[0040.07](issue0040.07.md)|Can `sizeof` be applied to earlier parameter names in a prototype, or to earlier fields in a struct?|Closed|
|[0040.08](issue0040.08.md)|What arithmetic can be performed on a `char` holding a defined character literal value?|Closed|
|[0040.09](issue0040.09.md)|Should the response to [Defect Report #017, Q27](issue0017.27.md) be reconsidered?|Closed|
|[0041](issue0041.md)|Are `'A'` through `'Z'` always `isupper` in all locales?|Closed|
|[0042.01](issue0042.01.md)|Does `memcpy` define a (sub)object?|Closed|
|[0042.02](issue0042.02.md)|If so, how big is the object defined by `memcpy`?|Closed|
|[0042.03](issue0042.03.md)|How big is a string object defined by the `str*` functions?|Closed|
|[0043.01](issue0043.01.md)|Can `NULL` be defined as `4-4`?|Fixed in C90 TC1|
|[0043.02](issue0043.02.md)|Can an identifier that starts with an underscore be defined as a macro in a source file that includes at least one standard header?|Closed|
|[0044.01](issue0044.01.md)|What does it mean to say that the type of `offsetof` is `size_t`?|Closed|
|[0044.02](issue0044.02.md)|Must the expansion of a standard header be a strictly conforming program?|Closed|
|[0044.03](issue0044.03.md)|Does expanding `offsetof` result in a non-strictly conforming program?|Closed|
|[0044.04](issue0044.04.md)|Can one use `offsetof` in a strictly conforming program?|Closed|
|[0044.05](issue0044.05.md)|Is `offsetof` the only standard macro that renders a program not strictly conforming?|Closed|
|[0045](issue0045.md)|Can one `freopen` an already closed file?|Closed|
|[0046](issue0046.md)|May a typedef be redeclared as a parameter outside an old-style function parameter list?|Closed|
|[0047](issue0047.md)|Can an array parameter have elements of incomplete type?|Closed|
|[0048](issue0048.md)|Is `abort` compatible with POSIX?|Closed|
|[0049](issue0049.md)|Can `strxfrm` produce a longer translation string?|Closed|
|[0050](issue0050.md)|Does a proper definition of `wchar_t` need to be in scope to write a wide-character literal?|Closed|
|[0051](issue0051.md)|Can one index beyond the declared end of an array if space is allocated for the extra elements?|Closed|
|[0052.01](issue0052.01.md)|Should the `mktime` example use `(time_t)-1` instead of `-1`?|Fixed in C90 TC1|
|[0052.02](issue0052.02.md)|Is the index entry for static correct?|Fixed in C90 TC1|
|[0052.03](issue0052.03.md)|Does the C Standard come with a Rationale, as indicated in Footnote 1?|Closed|
|[0053](issue0053.md)|Do the aliasing rules cover accesses to different function pointers properly?|Fixed in C90 TC1|
|[0054](issue0054.md)|What is the behavior of various string functions with a specified length of zero?|Fixed in C90 TC1|
|[0055](issue0055.md)|Must the `SIG*` macros have distinct values?|Fixed in C90 TC1|
|[0056](issue0056.md)|How accurate must floating-point arithmetic be?|Closed|
|[0057](issue0057.md)|Must there exist a user-accessible integral type for every pointer?|Closed|
|[0058](issue0058.md)|What is the number of digits in a number that can be processed by the `scanf` family and the `strtod` family?|Closed|
|[0059](issue0059.md)|Must an incomplete type be completed by the end of a translation unit?|Closed|
|[0060](issue0060.md)|When an array of `char` (or `wchar_t`) is initialized with a string literal that contains fewer characters than the array, are the remaining elements of the array initialized?|Fixed in C90 TC2|
|[0061](issue0061.md)|Interpretation of white space in the format string of a scan statement|Closed|
|[0062](issue0062.md)|Can the `rename` function alway return a failure?|Closed|
|[0063](issue0063.md)|This is [Defect Report 056](issue0056.md)|Closed|
|[0064](issue0064.md)|What is a null pointer constant?|Closed|
|[0065](issue0065.md)|Can strictly conforming programs contain locales other that the 'C' locale?|Fixed in C90 TC2|
|[0066](issue0066.md)|A set of locale questions|Closed|
|[0067](issue0067.md)|Are the definitions of types clear?|Closed|
|[0068](issue0068.md)|When are values of the type `char` treated as `signed`or `nonnegative` integers|Closed|
|[0069](issue0069.md)|What is the meaning of *pure binary numeration system*?|Closed|
|[0070](issue0070.md)|Can non-compatible types be used interchangeabily for function arguments?|Closed|
|[0071](issue0071.md)|Are all enumerated types compatible with a single type?|Fixed in C90 TC2|
|[0072](issue0072.md)|What is the definition of an object?|Closed|
|[0073](issue0073.md)|Another definition of an object question|Closed|
|[0074](issue0074.md)|Can the alignment of an object that is a member of a structure be different from the alignment of an object of the same type that is not a member of a structure?|Closed|
|[0075](issue0075.md)|What is the alignment of allocated memory?|Closed|
|[0076](issue0076.md)|A set of pointers to the end of arrays questions|Closed|
|[0077](issue0077.md)|Is the address of an object constant throughout its lifetime?|Closed|
|[0078](issue0078.md)|May optimizer invoke the as-if rule to rearrange code?|Closed|
|[0079](issue0079.md)|Is the address of a standard library function the same in different translation units?|Closed|
|[0080](issue0080.md)|Questions on merging of string constants|Fixed in C90 TC2|
|[0081](issue0081.md)|What is the result of the left shift operator `E1 < E2`, when `E1` is signed?|Closed|
|[0082](issue0082.md)|Many varargs questions|Fixed in C90 TC2|
|[0083](issue0083.md)|A use of library functions question|Fixed in C90 TC2|
|[0084](issue0084.md)|When is an incomplete type in function declaration a parameter?|Closed|
|[0085](issue0085.md)|Is the return from `main` equivalent to calling `exit`?|Fixed in C90 TC2|
|[0086](issue0086.md)|At object-like macros in system headers conforming?|Closed|
|[0087](issue0087.md)|Is the order of evaluation when there are no sequence points well defined?|Closed|
|[0088](issue0088.md)|Are two incomplete structure types with a (lexically) identical tag always compatible?|Closed|
|[0089](issue0089.md)|When does multiple definitions of a macro require a diagnositc message?|Fixed in C90 TC2|
|[0090](issue0090.md)|Multibyte characters in formats question|Closed|
|[0091](issue0091.md)|Does a locale with multibye characters conform?|Closed|
|[0092](issue0092.md)|Are the remaining elements in a partially initalized string guaranteed to be zero?|Closed|
|[0093](issue0093.md)|Can a conforming freestanding implementation reserve identifiers?|Fixed in C90 TC2|
|[0094](issue0094.md)|Is there an inconsistency between the constraints on passing values versus returning values?|Closed|
|[0095](issue0095.md)|Are the initialization constraints clear?|Closed|
|[0096](issue0096.md)|Can the element type in an array declarator be a non-object type?|Closed|
|[0097](issue0097.md)|Can the `type` argument of the `offsetof` macro be an incomplete type?|Closed|
|[0098](issue0098.md)|Do function types and incomplete type have size?|Closed|
|[0099](issue0099.md)|What does the term *assignment operator* mean?|Closed|
|[0100](issue0100.md)|Do functions return values by copying?|Fixed in C90 TC1|
|[0101](issue0101.md)|Are mismatched qualifiers allowed?|Fixed in C90 TC2|
|[0102](issue0102.md)|Does a constraint violation win over undefined behavior?|Closed|
|[0103](issue0103.md)|Is a diagnostic required when formal parameters for functions are incomplete types?|Closed|
|[0104](issue0104.md)|When is an incomplete type in function declaration a parameter?|Closed|
|[0105](issue0105.md)|Does a constraint violation win over undefined behavior?|Fixed in C90 TC1|
|[0106](issue0106.md)|Can one take the address of a void expression?|Closed|
|[0107](issue0107.md)|Several `assert` questions|Closed|
|[0108](issue0108.md)|Is it conforming to allow macros to make keywords?|Closed|
|[0109](issue0109.md)|Does the C Standard draw any significant distinction between *undefined values* and *undefined behavior*?|Closed|
|[0110](issue0110.md)|When is a formal parameter having array-of-non-object type not conforming?|Closed|
|[0111](issue0111.md)|A question on conversion of *pointer-to-qualified* type values to type `(void*)` values|Closed|
|[0112](issue0112.md)|A Null pointer constants and relational comparison question|Closed|
|[0113](issue0113.md)|Return expressions in functions declared to return qualified `void` questions|Closed|
|[0114](issue0114.md)|Initialization of multi-dimensional `char` array object questions|Closed|
|[0115](issue0115.md)|What it means to *declare* a declarator?|Closed|
|[0116](issue0116.md)|Is a diagnostic required when the address of a `reigister` arry is implicitly taken?|Closed|
|[0117](issue0117.md)|Abstract semantics, sequence points, and expression evaluation question|Closed|
|[0118](issue0118.md)|When is the `sizeof` an enumeration type known?|Fixed in C90 TC2|
|[0119](issue0119.md)|Is a diagnostic required on an example of an initialization of multi-dimensional array objects|Closed|
|[0120](issue0120.md)|Semantics of assignment to (and initialization of) bit-fields question|Closed|
|[0121](issue0121.md)|What is ment by *size required* when convering a ponter value to an integral type?|Closed|
|[0122](issue0122.md)|Is the *type* of a bit-field totally independent from its *width*?|Closed|
|[0123](issue0123.md)|“*Type categories*” and qualified types question|Closed|
|[0124](issue0124.md)|What is the difference between casts to *a void type* versus casts to the `void` type?|Fixed in C90 TC2|
|[0125](issue0125.md)|When are declarations useing `extern` *(qualified)* `void` not conforming?|Closed|
|[0126](issue0126.md)|What does *synonym* mean with respect to typedef names?|Closed|
|[0127](issue0127.md)|What is the composite type of an enumeration and an integer?|Closed|
|[0128](issue0128.md)|Editorial issue relating to tag declarations in type specifiers|Closed|
|[0129](issue0129.md)|When is name spaces of tags are shared?|Closed|
|[0130](issue0130.md)|When is data read from a text stream guaranteed to match what was written to the stream?|Closed|
|[0131](issue0131.md)|What is the meaning of *const-qualification*?|Fixed in C90 TC2|
|[0132](issue0132.md)|Can undefined behavior occur at translation time, or only at run time?|Closed|
|[0133](issue0133.md)|Undefined behavior not previously listed in subclause G2|Closed|
|[0134](issue0134.md)|Is *error number* an undefined term?|Closed|
|[0135](issue0135.md)|Is the `SVR4 fwrite` different?|Closed|
|[0136](issue0136.md)|Does `mktime` yield a -1 in the *spring-forward* gap when `tm_isdst` is -1?|Closed|
|[0137](issue0137.md)|Is `printf("%.1f", -0.01)` required to produce `0.0` , `-0.0`, or are both acceptable?|Closed|
|[0138](issue0138.md)|What are the storage durations?|Fixed in C90 TC2|
|[0139](issue0139.md)|Is an incomplete type compatible with the completed type?|Fixed in C90 TC2|
|[0140](issue0140.md)|What does *performed* and *other operation* mean?|Closed|
|[0141](issue0141.md)|What does `EOF` mean in `<stdio.h>`?|Closed|
|[0142](issue0142.md)|Is it permitted to `#undef` a reserved macro name?|Fixed in C99|
|[0143](issue0143.md)|What are the definitions of file opening modes?|Fixed in C99|
|[0144](issue0144.md)|Can the white space preceeding the initial `#` of a preprocessing directive be derived from macro expansion?|Fixed in C99|
|[0145](issue0145.md)|The four possible forms for a constant expression are not consistent|Fixed in C99|
|[0146](issue0146.md)|Does the constraint of 6.1.2 serve a purpose?|Fixed in C99|
|[0147](issue0147.md)|Is there a requirement for a sequence point to occur within a library function?|Fixed in C99|
|[0148](issue0148.md)|Is it clear when it is permitted to declare a library function?|Closed|
|[0149](issue0149.md)|Is the term *variable* defiend?|Fixed in C99|
|[0150](issue0150.md)|Are programs containing `char array[] = "Hello, World";` strictly conforming?|Fixed in C99|
|[0151](issue0151.md)|Is the out from `printf("%#.0o", 0);` ambiguous?|Closed|
|[0152](issue0152.md)|Can `longjmp` be used to return from a signal handler invoked other than through `abort` or `raise`?|Closed|
|[0153](issue0153.md)|Is there a problem with empty arguments in macro calls?|Closed|
|[0154](issue0154.md)|What restrictions apply to implementation-defined entities?|Closed|
|[0155](issue0155.md)|Is the word *unique* in subclause 7.10.3 ambiguous?|Fixed in C99|
|[0156](issue0156.md)|Should calls to `fsetpos` with positions in closed and reopened streams be undefined?|Fixed in C99|
|[0157](issue0157.md)|Is it clearly indicated when the spelling of a type name is or is not significant?|Fixed in C99|
|[0158](issue0158.md)|Are the semantics for the explicit conversion of null pointer constants defined?|Fixed in C99|
|[0159](issue0159.md)|Is the introduction to the C Standard confusing?|Fixed in C99|
|[0160](issue0160.md)|It is unclear what applications can and cannot do with identifiers that are reserved?|Fixed in C99|
|[0161](issue0161.md)|Is the wording of subclause 7.13 unclear?|Closed|
|[0162](issue0162.md)|Is the description of the static objects used by `time.h` functions misleading?|Fixed in C99|
|[0163](issue0163.md)|Is it clear whether the use of an undeclared identifier as a primary expression requires a diagnostic message to be issued?|Closed|
|[0164](issue0164.md)|Is there a constraint to prevent declarations involving types not defined by subclause 6.1.2.5?|Closed|
|[0165](issue0165.md)|Is the wording of subclause 6.5.2.3 concerning tags defective?|Fixed in C99|
|[0166](issue0166.md)|Do constraints that require something to be an lvalue place an unacceptable burden on the implementation?|Fixed in C99|
|[0167](issue0167.md)|The `n` conversion specifier in subclause 7.9.6.2 made by TC1, [Defect Report #014, Question 2](issue0014.02.md), should be applied to subclause 7.9.6.1|Fixed in C99|
|[0168](issue0168.md)|The change to subclause 6.3 made by TC1, [Defect Report #053, Question 1](issue0053.md), should also be applied in Annex .2 (page 200\)|Fixed in C99|
|[0169](issue0169.md)|Is the description of the replacement of trigraphs contradictory?|Closed|
|[0170](issue0170.md)|Are the description of operators and punctuators is confusing, and are the constraints contradictory?|Fixed in C99|
|[0171](issue0171.md)|Is it possible to create implementations with unreasonable arrangements of integral types?|Fixed in C99|
|[0172](issue0172.md)|Does the description for the relational and equality operators contain defects?|Fixed in C99|
|[0173](issue0173.md)|What is the meaning of *line number* when a token is split over more than one physical source line?|Closed|
|[0174](issue0174.md)|Is there a number of errors in the usual arithmetic conversions section?|Fixed in C99|
|[0175](issue0175.md)|Is the `sscanf` example added by TC1 wrong?|Fixed in C99|
|[0176](issue0176.md)|Are rules concerning whether `#error` generates a diagnostic contradictory?|Closed|
|[0177](issue0177.md)|A Preprocessing directives question|Fixed in C99|
|[0178](issue0178.md)|Why does [Defect Report #051](issue0051.md) and [Defect Report #073](issue0073.md) answer the same question differently?|Closed|

