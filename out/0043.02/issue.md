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
