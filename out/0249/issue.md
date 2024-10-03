### Problem

Defect Report 009 made a change to the text concerning function declarators.
This text seems not have made it into C99, even though the issue remains valid.
The change should be reinstated.

### Suggested Technical Corrigendum

Change 6.7.5.3#11 to:

> \[#11] If, in a parameter declaration, an identifier can be treated as a typedef
> name or as a parameter name, it shall be taken as a typedef name.
