This repository contains code and data for conversion of lists of
issues filed against revisions of the C standard and related documents
into JSON + Markdown for use in a new issue tracker.

`in/` - the issue lists used as input for the conversion

`issues.py` - the conversion script.  This depends on a [forked
version of
python-markdownify](https://github.com/jsm28/python-markdownify/tree/c-issues-convert).

`out/` - a copy of the output data from the script, committed for user
convenience in viewing that data (and in comparing the result of
changes to the conversion process).

`format.py` - a script to produce formatted Markdown files of the
issues combining both data and metadata for convenient viewing

`out_formatted/` - a copy of that formatted output, committed for user
convenience in viewing that data

The layout and JSON schema of the output are subject to change to
match whatever ends up being used by the new issue tracker, and may
not currently have any resemblance to what is used there.  The JSON
schema used here is not currently documented, but note that `-md`
fields are intended to be interpreted as Markdown, while `x-` fields
have extra metadata from the source documents unlikely to be of direct
use in the new issue tracker.  The metadata here has details of what
standard had fixes for each issue, including when that was not found
in the source issue lists but had to be entered manually (e.g. for C90
issues fixed in associated Technical Corrigenda).

Certain extensions to CommonMark (all found in GFM) are used in the
output: tables and strikethrough.  Raw HTML output is used for `<u>`,
`<sub>` and `<sup>` as those are not supported in Markdown.  In
addition, links between issues use `issue:` pseudo-URIs.  (If
formatted output is generated from the data here, the appropriate
handling of such links might depend on whether separate pages are
generated for each issue, or a single long page with all issues
against a given standard version.)  Soft line breaks in paragraphs are
intended to be interpreted as spaces, not as line endings; the
Markdown is wrapped purely for convenience in reading / editing it
directly, not for any semantic significance.
