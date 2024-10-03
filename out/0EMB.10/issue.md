Description: the relationship beween named-registers and 6.9.2 (external object
definitions) need to specified: when there is no initializer in the
named-register declaration, the declaration is not an external definition for
the identifier. The declaration is however also not a tentative definition,
because it has a storage-class specifier. Then, what is it?

Proposed solution: That's one problem with using existing syntactic categories
for new facilities. A workaround would be to change storage-class-specifier to
storage-class- specifier\|whatever in the grammar, where "whatever" is some new
category, and then adjust the text that constrains storage-class-specifier to
say the right thing (just storage-class-specifier or
storage-class-specifier\|whatever, depending). Then the construct would not have
a storage-class-specifier and thus would be a tentative definition.
