### Summary

Obviously, what appear in the definition syntax of a function-like macro are not
its arguments, but its parameters. On the other hand, what is similar
syntactically to a function call is obviously the invocation of the macro, not
its definition. Clearly, there is confusion about whether this sentence is
talking about the definition or an invocation.

Perhaps it would be clearer yet to say something like, "a function-like macro
<ins>which takes</ins> arguments, similarly syntactically to a function call".

### Suggested Technical Corrigendum

Change 6.10.3p10:

> A preprocessing directive of the form
>
> > `# define` *identifier lparen identifier-list<sub>opt</sub>* `)`
> > *replacement-list new-line*  
> > `# define` *identifier lparen* `... )` *replacement-list new-line*  
> > `# define` *identifier lparen identifier-list* `, ... )` *replacement-list
> > new-line*
>
> defines a function-like macro with <del>arguments</del> <ins>parameters</ins>,
> similar syntactically to a function call.
