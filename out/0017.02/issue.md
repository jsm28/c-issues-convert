Behavior if no function called `main` exists

According to subclause 5.1.2.2.1, page 6, it is implicitly undefined behavior if
the executable does not contain a function called `main`.

It ought to be explicitly undefined if no function called `main` exists in the
executable.
