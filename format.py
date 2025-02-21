#! /usr/bin/env python3

import argparse
import collections
import json
import os
import os.path
import re
from mistletoe import Document
from mistletoe.contrib.pygments_renderer import PygmentsRenderer
from mistletoe.html_renderer import HtmlRenderer


# The location of the WG14 documents site.
WG14_DOCS = 'https://www.open-std.org/jtc1/sc22/wg14/www/docs/'


# The location of issue data and metadata.
ISSUES_DIR = 'out'


# The location of formatted (Markdown) output.
OUT_MD_DIR = 'out_formatted'


# The location of formatted (HTML) output.
OUT_HTML_DIR = 'out_html'


# Valid submitted-against values and human descriptions (including
# documents with no issues reported).  These do not correspond
# one-to-one with published standards, since a single issue list was
# used for both C11 and C17, and a single list for all parts of TS
# 18661.
SUBMITTED_AGAINST = {
    'c90': 'C90',
    'c99': 'C99',
    'c11c17': 'C11 / C17',
    'c23': 'C23',
    'cfp-c11': 'Floating-point TS 18661 (C11 version, 2014-2016)',
    'cfp-c23': 'Floating-point TS 18661 (C23 version, 2025)',
    'cscr2013': 'C Secure Coding Rules TS 17961:2013',
    'embc2004': 'Embedded C TR 18037:2004',
    'embc2008': 'Embedded C TR 18037:2008',
    'math2009': 'Mathematical special functions ISO/IEC 24747:2009',
    'dynalloc2010': 'Dynamic allocation functions TR 24731-2:2010',
    'prov2025': 'Provenance TS 6010:2025',
    # Included for completeness, these last three were superseded with
    # no issue lists ever created.
    'bounds2007': 'Bounds-checking interfaces TR 24731-1:2007 (superseded)',
    'char2004': 'New character data types TR 19769:2004 (superseded)',
    'dfp2009': 'Decimal floating-point TR 24732:2009 (superseded)'}


# Valid fixed-in values and human descriptions (including potential
# future standard versions).
FIXED_IN = {
    'c90': 'C90',
    'c90tc1': 'C90 TC1',
    'c90tc2': 'C90 TC2',
    'c99': 'C99',
    'c99tc1': 'C99 TC1',
    'c99tc2': 'C99 TC2',
    'c99tc3': 'C99 TC3',
    'c11': 'C11',
    'c11tc1': 'C11 TC1',
    'c17': 'C17',
    'c23': 'C23',
    'c2y': 'C2Y',
    'cfp4-c23': 'Floating-point TS 18661-4:2025',
    'cfp4-c2y': 'Floating-point TS 18661-4 (C2Y version)',
    'cfp5-c2y': 'Floating-point TS 18661-5 (C2Y version)',
    'cscr2013tc1': 'C Secure Coding Rules TS 17961:2013 TC1',
    'cscr202y': 'C Secure Coding Rules TS 17961:202y',
    'embc2008': 'Embedded C TR 18037:2008'}


# Valid issue statuses and human descriptions.
STATUSES = {
    'closed': 'Closed',
    'fixed': 'Fixed',
    'fixed-pending': 'Fixed (pending integration in working draft)',
    'review': 'Review',
    'open': 'Open'}


def get_data(dirname):
    """Get data for all issues."""
    out_data = {}
    issue_nums = os.listdir(dirname)
    for n in issue_nums:
        n_dir = os.path.join(dirname, n)
        with open(os.path.join(n_dir, 'metadata.json'), 'r',
                  encoding='utf-8') as f:
            data = json.load(f)
        with open(os.path.join(n_dir, 'issue.md'), 'r', encoding='utf-8') as f:
            data['content-md'] = f.read()
        for c in data['comments']:
            with open(os.path.join(n_dir, 'comments', c['filename']), 'r',
                      encoding='utf-8') as f:
                c['content-md'] = f.read()
        out_data[n] = data
    return out_data


def format_issue(num, data, for_single):
    """Produce formatted Markdown for a single issue, combining
    content and metadata.  This still uses the internal issue:
    notation for links to other issues.  If for_single, this is for
    outputting an MD file for just one issue (meaning some additional
    context should be included in that output); otherwise, it is for
    inclusion in a file listing all issues against some standard
    document."""
    out_list = []
    if not for_single:
        out_list.append('---\n\n')
        out_list.append('<div id="issue%s">\n\n' % num)
    out_list.append('## Issue %s: %s\n\n' % (num, data['summary-md']))
    if for_single and data['conversion-src']:
        out_list.append('**This issue has been automatically converted from '
                        'the original issue lists and some formatting may '
                        'not have been preserved.**\n\n')
    meta_list = []
    authors = []
    if 'author-md' in data:
        authors.append(data['author-md'])
    if 'submitter-md' in data:
        authors.append(data['submitter-md'])
    meta_list.append('Authors: %s' % ', '.join(authors))
    meta_list.append('Date: %s' % data['date'])
    if 'reference-doc-md' in data:
        meta_list.append('Reference document: %s' % data['reference-doc-md'])
    if for_single:
        meta_list.append('Submitted against: %s'
                         % SUBMITTED_AGAINST[data['submitted-against']])
    meta_list.append('Status: %s' % STATUSES[data['status']])
    if data['status'] in ('fixed', 'fixed-pending'):
        meta_list.append('Fixed in: %s'
                         % ', '.join(FIXED_IN[x] for x in data['fixed-in']))
    if data['crossref']:
        meta_list.append('Cross-references: %s'
                         % ', '.join('[%s](issue:%s)' % (n, n)
                                     for n in data['crossref']))
    if data['conversion-src']:
        meta_list.append('Converted from: %s'
                         % ', '.join('[%s](%s%s)' % (d, WG14_DOCS, d)
                                     for d in data['conversion-src']))
    out_list.append('  \n'.join(meta_list))
    out_list.append('\n\n')
    out_list.append(data['content-md'])
    for c in data['comments']:
        out_list.append('\n---\n\n')
        out_list.append('Comment from %s on %s:\n\n'
                        % (c['author-md'], c['date']))
        out_list.append(c['content-md'])
    if not for_single:
        out_list.append('\n\n</div>\n\n')
        out_list.append('\n---\n\n')
    if for_single:
        data['formatted-single-md'] = ''.join(out_list)
    else:
        data['formatted-list-md'] = ''.join(out_list)


def subst_md(content, for_single, link_suffix, issue_data):
    """Substitute for issue: links in Markdown."""
    if for_single:
        content = re.sub(r'\(issue:([0-9][.A-Z0-9]*)\)',
                         lambda m: (
                             '(../%s/issue%s%s)'
                             % (issue_data[m.group(1)]['submitted-against'],
                                m.group(1),
                                link_suffix)),
                         content)
    else:
        content = re.sub(r'\(issue:([0-9][.A-Z0-9]*)\)',
                         lambda m: (
                             '(../%s/log%s#issue%s)'
                             % (issue_data[m.group(1)]['submitted-against'],
                                link_suffix,
                                m.group(1))),
                         content)
    return content


def file_suffix(for_html):
    """Return suffix to use in filenames based on output format."""
    return '.html' if for_html else '.md'


def write_md(filename, content, title, for_single, for_html, issue_data):
    """Write Markdown to a file, substituting for issue: links."""
    suffix = file_suffix(for_html)
    out_dir = OUT_HTML_DIR if for_html else OUT_MD_DIR
    content = subst_md(content, for_single, suffix, issue_data)
    if for_html:
        with PygmentsRenderer() as renderer:
            doc = Document(content)
            css = renderer.formatter.get_style_defs()
            content = renderer.render(doc)
        with HtmlRenderer() as renderer:
            doc = Document(title)
            title = renderer.render_to_plain(doc)
        content = (
            '<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '<meta http-equiv="Content-Type" content="text/html; '
            'charset=UTF-8">\n'
            '<title>%s</title>\n'
            '<style>\n'
            '%s\n'
            '</style>\n'
            '</head>\n'
            '<body>\n'
            '%s\n'
            '</body>\n'
            '</html>\n'
            % (title, css, content))
    filename += suffix
    filename = os.path.join(out_dir, filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def action_format(for_html):
    """Format the issue lists.  The source data is in ISSUES_DIR; the
    formatted output goes to OUT_MD_DIR or OUT_HTML_DIR."""
    suffix = file_suffix(for_html)
    issues_data = get_data(ISSUES_DIR)
    by_submitted_against = collections.defaultdict(set)
    by_submitted_against_converted = collections.defaultdict(bool)
    for num, data in issues_data.items():
        by_submitted_against[data['submitted-against']].add(num)
        if data['conversion-src']:
            by_submitted_against_converted[data['submitted-against']] = True
        format_issue(num, data, False)
        format_issue(num, data, True)
        write_md('%s/issue%s' % (data['submitted-against'], num),
                 data['formatted-single-md'],
                 'C issue %s: %s' % (num, data['summary-md']), True,
                 for_html, issues_data)
    index_out_list = ['# C standard issues lists\n\n']
    index_out_list.append(
        '**Issue tracking for C is not currently in operation.  The\n'
        'following is a proposed process for issue submission, to be\n'
        'considered at the Graz meeting of the C standards committee.**\n\n'
        'The C standards committee considers issues reported against the\n'
        'C standard and other associated documents it has released.  Please\n'
        'send reports of issues to the issues list maintainer (*details to\n'
        'be inserted here*).  The data for the issues lists is maintained\n'
        'in JSON and Markdown format in a public git repository (*details to\n'
        'be inserted here*); issues may be submitted in Markdown format\n'
        'if you wish, but that is not required.  Note that the following\n'
        'principles apply to issue handling.\n\n'
        '* Submitted issues will be handled along the lines described in\n'
        '  [N3002](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3002'
        '.pdf).\n'
        '  As the C standards committee returns to issue tracking after a\n'
        '  hiatus from 2019 to 2025, the details of the process may evolve.\n'
        '* The issue tracking process is only suitable for problems in the\n'
        '  standard (and associated documents) that can be addressed with a\n'
        '  reasonably small, local fix.  Feature or enhancement requests\n'
        '  need to be submitted as papers through the standards development\n'
        '  process, not as issues for issue tracking.\n'
        '* The C standards committee does not maintain old versions of\n'
        '  standards or other superseded documents.  Thus, issues can only\n'
        '  be considered if they are present in the most recent version\n'
        '  of the relevant document to be officially published (or pending\n'
        '  publication) and that has not been superseded by another\n'
        '  document.  For example, issues with the C standard can only be\n'
        '  considered if they are present in C23; issues can no longer be\n'
        '  reported against C17.  However, if an issue is present in both\n'
        '  C17 and C23, it is likely many implementations will find it\n'
        '  useful to apply a resolution for C23 also in C17 mode.  If some\n'
        '  issues reported against C23 (and present in C2Y) remain open after\n'
        '  C2Y has been published, those will continue to be processed\n'
        '  alongside issues newly reported against the released version of\n'
        '  C2Y.\n'
        '* If an issue is not present in the most recent officially\n'
        '  published version of the relevant document, only in a subsequent\n'
        '  working draft, then it should be raised through the standards\n'
        '  development process, not through issue tracking.  For example,\n'
        '  issues present in a C2Y working draft but not in C23 should not\n'
        '  be raised here.  Instead, such an issue can be raised through a\n'
        '  paper proposing a fix, or a direct email to the author of the\n'
        '  paper that introduced the issue to start joint work with them on\n'
        '  a fix.  Depending on the stage of standard development, issues\n'
        '  may also be raised through NB comments on ballot drafts.\n'
        '* Fixes for typos, formatting and similar very straightforward\n'
        '  editorial issues (present in the latest working draft, whether or\n'
        '  not present in an officially published document) may be sent\n'
        '  direct to the editor (for the C standard or other documents with\n'
        '  an active editor) rather than needing to go through issue\n'
        '  tracking; see the [contact\n'
        '  list](https://www.open-std.org/jtc1/sc22/wg14/www/contacts.html).\n'
        '  This also includes cases where a mistake was made in\n'
        '  applying changes approved by the committee to the working draft.\n'
        '  (If such a mistake has technical impact and is present in an\n'
        '  officially published document rather than just a working draft,\n'
        '  then an actual issue report is a good idea, however.)\n'
        '* If an issue has already been fixed in the latest working draft\n'
        '  (for example, an issue present in C23 but fixed in C2Y), there\n'
        '  is limited value in also submitting it through issue tracking,\n'
        '  but if such an issue is submitted it may result in an opinion\n'
        '  from the committee on what fix would be appropriate for\n'
        '  implementations of the current release.\n\n')
    for std, desc in SUBMITTED_AGAINST.items():
        index_out_list.append('## %s\n\n' % desc)
        if std not in by_submitted_against:
            index_out_list.append('No issues recorded.\n\n')
            continue
        index_out_list.append(
            '* [Summary (one page per issue)](%s/summary%s)\n'
            '* [Full issue log (all issues on one page)](%s/log%s)\n\n'
            % (std, suffix, std, suffix))
        nums = sorted(by_submitted_against[std])
        was_converted = by_submitted_against_converted[std]
        summary_head = ['# %s: issue summary\n\n' % desc]
        log_head = ['# %s: issue log\n\n' % desc]
        if was_converted:
            summary_head.append(
                '**This issue summary has been automatically converted from '
                'the original issue lists and some formatting may '
                'not have been preserved.**\n\n')
            log_head.append(
                '**This issue log has been automatically converted from '
                'the original issue lists and some formatting may '
                'not have been preserved.**\n\n')
        table = ['|Issue|Summary|Status|\n|-|-|-|\n']
        for num in nums:
            data = issues_data[num]
            if data['status'] in ('fixed', 'fixed-pending'):
                status = ('%s in %s'
                          % (STATUSES[data['status']],
                             ', '.join(FIXED_IN[x] for x in data['fixed-in'])))
            else:
                status = STATUSES[data['status']]
            table.append(
                '|[%s](issue:%s)|%s|%s|\n'
                % (num, num, data['summary-md'], status))
        table.append('\n')
        issues = [issues_data[n]['formatted-list-md'] for n in nums]
        write_md('%s/summary' % std, ''.join(summary_head + table),
                 '%s: issue summary' % desc,
                 True, for_html, issues_data)
        write_md('%s/log' % std, ''.join(log_head + table + issues),
                 '%s: issue log' % desc,
                 False, for_html, issues_data)
    write_md('index', ''.join(index_out_list), 'C standard issues lists',
             False, for_html, issues_data)


def action_format_md():
    """Format the issue lists in Markdown."""
    action_format(False)


def action_format_html():
    """Format the issue lists in HTML."""
    action_format(True)


def main():
    """Main program."""
    parser = argparse.ArgumentParser(
        description='Format C issues in Markdown')
    parser.add_argument('action',
                        help='What to do',
                        choices=('format-md', 'format-html'))
    args = parser.parse_args()
    action_map = {'format-md': action_format_md,
                  'format-html': action_format_html}
    action_map[args.action]()


if __name__ == '__main__':
    main()
