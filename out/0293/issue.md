### Summary

> 6.7.8, paragraph 24, example 1\.
>
> > ```c
> > complex c = 5 + 3 * I
> > ```
>
> should changed to
>
> > ```c
> > double complex c = 5 + 3 * I
> > ```

### Suggested Technical Corrigendum

Change `complex` to `double complex` in the example.
