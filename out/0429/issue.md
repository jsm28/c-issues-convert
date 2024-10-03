### Summary

gets\_s Annex K.3.5.4.1p2 says:  

"If there is a runtime-constraint violation, s\[0] is set to the null  
character, and characters are read and discarded from stdin until a  
new-line character is read, or end-of-file or a read error occurs."  

The runtime-constraint violation here can be caused by a null "s"  
pointer.  Should we discard the next input line even if `(s == NULL)` ?  

The way it is written, it looks like the answer is yes.  However it is  
not clear to us that that was the intent.  Note also that s\[0] cannot be  
set to the null character when `s==NULL`.

### Suggested Technical Corrigendum
