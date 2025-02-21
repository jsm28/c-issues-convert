# C standard issues lists

**Issue tracking for C is not currently in operation.  The
following is a proposed process for issue submission, to be
considered at the Graz meeting of the C standards committee.**

The C standards committee considers issues reported against the
C standard and other associated documents it has released.  Please
send reports of issues to the issues list maintainer (*details to
be inserted here*).  The data for the issues lists is maintained
in JSON and Markdown format in a public git repository (*details to
be inserted here*); issues may be submitted in Markdown format
if you wish, but that is not required.  Note that the following
principles apply to issue handling.

* Submitted issues will be handled along the lines described in
  [N3002](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3002.pdf).
  As the C standards committee returns to issue tracking after a
  hiatus from 2019 to 2025, the details of the process may evolve.
* The issue tracking process is only suitable for problems in the
  standard (and associated documents) that can be addressed with a
  reasonably small, local fix.  Feature or enhancement requests
  need to be submitted as papers through the standards development
  process, not as issues for issue tracking.
* The C standards committee does not maintain old versions of
  standards or other superseded documents.  Thus, issues can only
  be considered if they are present in the most recent version
  of the relevant document to be officially published (or pending
  publication) and that has not been superseded by another
  document.  For example, issues with the C standard can only be
  considered if they are present in C23; issues can no longer be
  reported against C17.  However, if an issue is present in both
  C17 and C23, it is likely many implementations will find it
  useful to apply a resolution for C23 also in C17 mode.  If some
  issues reported against C23 (and present in C2Y) remain open after
  C2Y has been published, those will continue to be processed
  alongside issues newly reported against the released version of
  C2Y.
* If an issue is not present in the most recent officially
  published version of the relevant document, only in a subsequent
  working draft, then it should be raised through the standards
  development process, not through issue tracking.  For example,
  issues present in a C2Y working draft but not in C23 should not
  be raised here.  Instead, such an issue can be raised through a
  paper proposing a fix, or a direct email to the author of the
  paper that introduced the issue to start joint work with them on
  a fix.  Depending on the stage of standard development, issues
  may also be raised through NB comments on ballot drafts.
* Fixes for typos, formatting and similar very straightforward
  editorial issues (present in the latest working draft, whether or
  not present in an officially published document) may be sent
  direct to the editor (for the C standard or other documents with
  an active editor) rather than needing to go through issue
  tracking; see the [contact
  list](https://www.open-std.org/jtc1/sc22/wg14/www/contacts.html).
  This also includes cases where a mistake was made in
  applying changes approved by the committee to the working draft.
  (If such a mistake has technical impact and is present in an
  officially published document rather than just a working draft,
  then an actual issue report is a good idea, however.)
* If an issue has already been fixed in the latest working draft
  (for example, an issue present in C23 but fixed in C2Y), there
  is limited value in also submitting it through issue tracking,
  but if such an issue is submitted it may result in an opinion
  from the committee on what fix would be appropriate for
  implementations of the current release.

## C90

* [Summary (one page per issue)](c90/summary.md)
* [Full issue log (all issues on one page)](c90/log.md)

## C99

* [Summary (one page per issue)](c99/summary.md)
* [Full issue log (all issues on one page)](c99/log.md)

## C11 / C17

* [Summary (one page per issue)](c11c17/summary.md)
* [Full issue log (all issues on one page)](c11c17/log.md)

## C23

No issues recorded.

## Floating-point TS 18661 (C11 version, 2014-2016)

* [Summary (one page per issue)](cfp-c11/summary.md)
* [Full issue log (all issues on one page)](cfp-c11/log.md)

## Floating-point TS 18661 (C23 version, 2025)

No issues recorded.

## C Secure Coding Rules TS 17961:2013

* [Summary (one page per issue)](cscr2013/summary.md)
* [Full issue log (all issues on one page)](cscr2013/log.md)

## Embedded C TR 18037:2004

* [Summary (one page per issue)](embc2004/summary.md)
* [Full issue log (all issues on one page)](embc2004/log.md)

## Embedded C TR 18037:2008

No issues recorded.

## Mathematical special functions ISO/IEC 24747:2009

No issues recorded.

## Dynamic allocation functions TR 24731-2:2010

No issues recorded.

## Provenance TS 6010:2025

No issues recorded.

## Bounds-checking interfaces TR 24731-1:2007 (superseded)

No issues recorded.

## New character data types TR 19769:2004 (superseded)

No issues recorded.

## Decimal floating-point TR 24732:2009 (superseded)

No issues recorded.

