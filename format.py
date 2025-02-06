#! /usr/bin/env python3

import argparse
import collections
import json
import os
import os.path
import re


# The location of the WG14 documents site.
WG14_DOCS = 'https://www.open-std.org/jtc1/sc22/wg14/www/docs/'


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
    if data['status'] == 'fixed':
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


def write_md(filename, content, for_single, issue_data):
    """Write Markdown to a file, substituting for issue: links."""
    if for_single:
        content = re.sub(r'\(issue:([0-9][.A-Z0-9]*)\)',
                         r'(issue\1.md)',
                         content)
    else:
        content = re.sub(r'\(issue:([0-9][.A-Z0-9]*)\)',
                         lambda m: (
                             '(log_%s.md#issue%s)'
                             % (issue_data[m.group(1)]['submitted-against'],
                                m.group(1))),
                         content)
    out_dir = 'out_formatted'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, filename), 'w', encoding='utf-8') as f:
        f.write(content)


def action_format():
    """Format the issue lists.  The source data is in out/; the
    formatted output goes to out_formatted/."""
    issues_data = get_data('out')
    by_submitted_against = collections.defaultdict(set)
    by_submitted_against_converted = collections.defaultdict(bool)
    for num, data in issues_data.items():
        by_submitted_against[data['submitted-against']].add(num)
        if data['conversion-src']:
            by_submitted_against_converted[data['submitted-against']] = True
        format_issue(num, data, False)
        format_issue(num, data, True)
        write_md('issue%s.md' % num, data['formatted-single-md'], True,
                 issues_data)
    index_out_list = ['# C standard issues lists\n\n']
    for std, desc in SUBMITTED_AGAINST.items():
        index_out_list.append('## %s\n\n' % desc)
        if std not in by_submitted_against:
            index_out_list.append('No issues recorded.\n\n')
            continue
        index_out_list.append(
            '* [Summary (one page per issue)](summary_%s.md)\n'
            '* [Full issue log (all issues on one page)](log_%s.md)\n\n'
            % (std, std))
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
            if data['status'] == 'fixed':
                status = ('Fixed in %s'
                          % ', '.join(FIXED_IN[x] for x in data['fixed-in']))
            else:
                status = STATUSES[data['status']]
            table.append(
                '|[%s](issue:%s)|%s|%s|\n'
                % (num, num, data['summary-md'], status))
        table.append('\n')
        issues = [issues_data[n]['formatted-list-md'] for n in nums]
        write_md('summary_%s.md' % std, ''.join(summary_head + table),
                 True, issues_data)
        write_md('log_%s.md' % std, ''.join(log_head + table + issues),
                 False, issues_data)
    write_md('index.md', ''.join(index_out_list), False, issues_data)


def main():
    """Main program."""
    parser = argparse.ArgumentParser(
        description='Format C issues in Markdown')
    parser.add_argument('action',
                        help='What to do',
                        choices=('format'))
    args = parser.parse_args()
    action_map = {'format': action_format}
    action_map[args.action]()


if __name__ == '__main__':
    main()
