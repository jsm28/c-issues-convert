#! /usr/bin/env python3

import argparse
import json
import os
import os.path
import re
import subprocess
import time
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup
from markdownify import ATX, abstract_inline_conversion, MarkdownConverter


# Filenames for DR lists and indices, and numbers of C90 and C99 DRs.
C90_INDEX = 'dr.htm'
C90_FIRST = 1
C90_LAST = 178
C99_INDEX = 'summary-c99.htm'
C99_FIRST = 201
C99_LAST = 345
C11_ALL = 'n2396.htm'
CFP_ALL = 'n2397.htm'
CSCR_ALL = 'n2150.htm'
# These are successive versions of the issue list, since the Embedded
# C lists edited the original description and proposed solution rather
# than just appending text from each meeting, so the closest
# equivalence to the other lists involves using the older versions
# rather than just the most recent one.
EMBC_2004_ALL_PDF = ('n1071.pdf', 'n1087.pdf', 'n1096.pdf', 'n1180.pdf')
EMBC_2004_ALL = ('n1071.html', 'n1087.html', 'n1096.html', 'n1180.html')


# The location of the WG14 documents site.
WG14_DOCS = 'https://www.open-std.org/jtc1/sc22/wg14/www/docs/'


def input_filename(doc):
    """Return the local filename of a WG14 document."""
    return os.path.join('in', doc)


def doc_url(doc):
    """Return the WG14 website URL of a WG14 document."""
    return WG14_DOCS + doc


def download_wg14_doc(doc):
    """Download a file from the WG14 website."""
    urllib.request.urlretrieve(doc_url(doc), filename=input_filename(doc))
    time.sleep(1)


def list_docs(for_download):
    """List all the WG14 documents being processed.  If for_download, list
    the files to download; otherwise, list the HTML files for subsequent
    processing."""
    ret = []
    ret.append(C90_INDEX)
    for n in range(C90_FIRST, C90_LAST + 1):
        ret.append('dr_%03d.html' % n)
    ret.append(C99_INDEX)
    for n in range(C99_FIRST, C99_LAST + 1):
        ret.append('dr_%03d.htm' % n)
    ret.append(C11_ALL)
    ret.append(CFP_ALL)
    ret.append(CSCR_ALL)
    if for_download:
        ret.extend(EMBC_2004_ALL_PDF)
    else:
        ret.extend(EMBC_2004_ALL)
    return ret


def is_c90_dr(doc):
    """Return whether a document is a C90 DR."""
    return bool(re.fullmatch(r'dr_[01][0-9][0-9]\.html', doc))


def action_download():
    """Download old issue lists from the WG14 website.  Since the lists
    are checked into git, it should not be necessary to run this action
    again."""
    for doc in list_docs(True):
        download_wg14_doc(doc)
    # Convert the Embedded C lists to HTML for subsequent processing.
    for pdf_doc in EMBC_2004_ALL_PDF:
        subprocess.run(['pdftohtml', '-noframes', '-q',
                        input_filename(pdf_doc),
                        input_filename(pdf_doc.replace('.pdf', '.html'))],
                       check=True)


def clean_amp(doc, text):
    """Clean up unescaped '&' and HTML entities not terminated by ';',
    ensuring that the resulting text only has '&' in a known entity."""
    text = text.replace('&&', '&amp;&amp;')
    text = text.replace('&<', '&amp;<')
    text = text.replace('&(', '&amp;(')
    text = text.replace('&*', '&amp;*')
    text = text.replace('&=', '&amp;=')
    text = text.replace('& ', '&amp; ')
    text = text.replace('&a)', '&amp;a)')
    text = text.replace('&a<', '&amp;a<')
    text = text.replace('&A)', '&amp;A)')
    text = text.replace('&A;', '&amp;A;')
    text = text.replace('&fp1;', '&amp;fp1;')
    text = text.replace('&desired,', '&amp;desired,')
    text = text.replace('&c;', '&amp;c;')
    text = text.replace('&time_str)', '&amp;time_str)')
    text = text.replace('&ltstdatomic.', '&lt;stdatomic.')
    text = text.replace('&gt<', '&gt;<')
    text = text.replace('&sect7', '&sect;7')
    known_entities = {
        # Known named entities used in these lists.
        'amp', 'lt', 'gt', 'quot', 'nbsp', 'ndash', 'mdash', 'para', 'plusmn',
        'ldquo', 'rdquo', 'lsquo', 'rsquo', 'pi', 'sect', 'hellip', 'ne',
        'infin', 'emsp', 'frac34', 'times',
        # Known numerical entities used in these lists.
        # "
        '#34',
        # '
        '#39',
        # [
        '#91',
        # ]
        '#93',
        # Control character, not actually valid; removed in a later step.
        '#157',
        # nbsp
        '#160',
        # ndash
        '#8211',
        # mdash
        '#8212',
        # rsquo
        '#8217',
        # ldquo
        '#8220',
        # rdquo
        '#8221',
        # minus
        '#8722'
    }
    rtext = text
    while '&' in rtext:
        m = re.search('&([^;]*);', rtext)
        if not m:
            raise ValueError("unmatched '&' in %s" % doc)
        if m.group(1) not in known_entities:
            raise ValueError('unknown entity &%s; in %s' % (m.group(1), doc))
        rtext = rtext[m.end(0):]
    return text


def clean_ltgt(doc, text):
    """Clean up unescaped '<' and '>', ensuring that the resulting text
    only has those characters as delimiters for valid tags.  (The
    actual check that they only occur as delimiters for tags occurs in
    a later step.)"""
    # This is a clear typo for '->' in dr_051.html.
    text = text.replace('->>', '-&gt;')
    # This is a stray '>' twice in dr.htm.
    text = text.replace('parameter>?', 'parameter?')
    # This is a stray '>' in dr_169.html.
    text = text.replace('Submis>sion Date', 'Submission Date')
    # n2396.htm has this spurious text part way through the file.
    text = text.replace(' </body>\n</html\n<!--', '<!--')
    # These are used twice for </p> in n2396.htm.
    text = text.replace('</>', '</p>')
    # This invalid tag is used in n2396.htm and should be <ul>.
    text = text.replace('<bl>', '<ul>')
    text = text.replace('</bl>', '</ul>')
    # This invalid tag is used in n2396.htm and should be <dfn>.
    text = text.replace('<def>', '<dfn>')
    text = text.replace('</def>', '</dfn>')
    # This invalid tag is used in n2396.htm and should be <blockquote>.
    text = text.replace('<stdquote>', '<blockquote>')
    text = text.replace('</stdquote>', '</blockquote>')
    # This invalid tag is used in n2396.htm and n2397.htm and doesn't
    # appear to be needed.
    text = text.replace('<o:p>', '')
    text = text.replace('</o:p>', '')
    # n2396.htm uses these tags that should be entities.
    text = text.replace('<ldquo>', '&ldquo;')
    text = text.replace('<rdquo>', '&rdquo;')
    # This does not make sense as an end tag, but should be an empty
    # tag, in n2396.htm.
    text = text.replace('</br>', '<br>')
    # Fix this badly quoted link for proper parsing in n2396.htm.
    # (Doesn't actually involve '<' or '>', but fixing here seems an
    # appropriate place as it's relevant to subsequent tag parsing.)
    text = text.replace(
        'href=https://en.wikipedia.org/wiki/'
        'Volatile_%28computer_programming%29""',
        'href="https://en.wikipedia.org/wiki/'
        'Volatile_%28computer_programming%29"')
    # These are missing '<' in n2397.htm.
    text = text.replace('inclusions/p>', 'inclusions</p>')
    text = text.replace('name/p>', 'name</p>')
    # This URL is given literally in n2397 surrounded by <>, not as a
    # proper link.
    text = text.replace(
        '<http://www.open-std.org/jtc1/sc22/wg14/13831>',
        '&lt;<a href="http://www.open-std.org/jtc1/sc22/wg14/13831">'
        'http://www.open-std.org/jtc1/sc22/wg14/13831</a>&gt;')
    # These constructs appear in n2397.htm and should be removed.
    text = re.sub(r'<!\[if.*?<!\[endif\]>', '', text, flags=re.DOTALL)
    text = re.sub(r'<!--\[if.*?<!\[endif\]-->', '', text, flags=re.DOTALL)
    text = text.replace('>>', '&gt;&gt;')
    text = text.replace('<<', '&lt;&lt;')
    text = text.replace(' >=', ' &gt;=')
    text = text.replace('<threads.h>', '&lt;threads.h&gt;')
    text = text.replace('.h>', '.h&gt;')
    text = text.replace('.h >', '.h &gt;')
    text = text.replace(' > ', ' &gt; ')
    text = text.replace(' < ', ' &lt; ')
    text = text.replace(')->', ')-&gt;')
    text = text.replace('a->', 'a-&gt;')
    text = text.replace('b->', 'b-&gt;')
    text = text.replace('L->', 'L-&gt;')
    text = text.replace(' ->', ' -&gt;')
    text = text.replace(' c>d)', ' c&gt;d)')
    text = text.replace(' || c>', ' || c&gt;')
    return text


def clean_chars(doc, text):
    """Clean up use of entities and direct use of Unicode characters, in
    cases where there may be subsequent processing related to a particular
    character and so it is convenient to have all uses in a consistent
    form."""
    # This is never used in a context where escaping is actually
    # needed (i.e. inside a double-quoted attribute value).
    text = text.replace('&quot;', '"')
    text = text.replace('&#34;', '"')
    # This is never used in a context where escaping is actually
    # needed (i.e. inside a single-quoted attribute value).
    text = text.replace('&#39;', "'")
    # Not valid, doesn't seem to be expected to produce output.
    text = text.replace('&#157;', '')
    # Non-breaking spaces used in formatting to clean up later.
    text = text.replace('&#160;', '&nbsp;')
    text = text.replace('\u00a0', '&nbsp;')
    # Em dashes used in what are logically bulleted lists.
    text = text.replace('&#8212;', '&mdash;')
    text = text.replace('\u2014', '&mdash;')
    # Bullets used in what are logically bulleted lists.
    text = text.replace('\u2022', '&bull;')
    return text


# Textual replacements to apply in the given input file.
TEXT_REPLACE = {'dr.htm': (('<BR>\nQ15: When do array parameters',
                            # The summary in dr.htm fails to include
                            # Q14 of this DR, so insert the summary
                            # used in the DR itself.  (The summaries
                            # in the DRs themselves aren't always the
                            # same as in dr.htm, and those in dr.htm
                            # are used in preference to generate
                            # output metadata, but the ones in the DRs
                            # are suitable substitutes when needed.)
                            '<BR>\nQ14: <TT><B>const void</B></TT> type '
                            'as a parameter\n'
                            '<BR>\nQ15: When do array parameters'),
                           ('<A HREF="dr_014.html#Question14"> Defect '
                            'Report #014, Question 2</A>',
                            '<A HREF="dr_014.html#Question2"> Defect '
                            'Report #014, Question 2</A>'),
                           ('<I>Type categories</I>',
                            '``<I>Type categories</I>')),
                'dr_001.html': (('str\nucture', 'structure'),
                                ('structur\ne', 'structure'),
                                ('toan', 'to an')),
                'dr_002.html': (('c haracter', 'character'),
                                ('esc aped', 'escaped'),
                                ('directiv es', 'directives'),
                                ('characte r', 'character'),
                                ('constru cted', 'constructed')),
                'dr_003.html': (('composin g', 'composing'),
                                ('lif e', 'life'),
                                ('responees', 'responses'),
                                ('withou ', 'without '),
                                ('#el se', '#else'),
                                (' b e ', ' be '),
                                ('\n<A HREF="dr_002.html">',
                                 '\n<BR>\n<A HREF="dr_002.html">')),
                'dr_006.html': (('<B>Question</B> 1   ',
                                 '<B>Question</B> 1\n<BR>\n'),),
                'dr_007.html': (('constrai nt', 'constraint'),),
                'dr_008.html': (('volat ile', 'volatile'),
                                ('volati lity', 'volatility'),
                                ('qual ified', 'qualified'),
                                ('optimiza tions', 'optimizations'),
                                ('compi\nler', 'compiler')),
                'dr_009.html': (('contai n', 'contain'),
                                ('returni ng', 'returning')),
                'dr_010.html': (('typ e', 'type'),),
                'dr_012.html': (('Plau\nger', 'Plauger'),
                                ('succe\nssfully', 'successfully')),
                'dr_013.html': (('occurr ence', 'occurrence'),
                                ('declara tion', 'declaration')),
                'dr_014.html': (('affe cted', 'affected'),),
                'dr_015.html': (('Defect Repost #015', 'Defect Report #015'),
                                ('val ues', 'values'),
                                ('ca n', 'can'),
                                ('promoti on', 'promotion')),
                'dr_016.html': (('<B>Submittor</B>',
                                 '<BR>\n<B>Submittor</B>'),),
                'dr_017.html': (('<A HREF="dr_013.html">Defect Report #013, '
                                 'Question 1</A>',
                                 '<A HREF="dr_013.html#Question1">Defect '
                                 'Report #013, Question 1</A>'),),
                'dr_019.html': (('Defect Report #XXX', 'Defect Report #019'),),
                'dr_033.html': ((' `shall', ' &lsquo;shall'),),
                'dr_034.html': (('<A HREF="dr_011.html">Defect '
                                 'Report #011</A>',
                                 '<A HREF="dr_011.html#Question1">Defect '
                                 'Report #011</A>'),),
                'dr_038.html': (('Previous Defect Rep8rt',
                                 'Previous Defect Report'),),
                'dr_040.html': (('envrionment', 'environment'),
                                ('previosly', 'previously'),
                                ('withrdaw', 'withdraw'),
                                ('<A HREF="dr_013.html">Defect\n'
                                 'Report #013, Question 1</A>',
                                 '<A HREF="dr_013.html#Question1">Defect\n'
                                 'Report #013, Question 1</A>'),
                                # An ordered list wrongly starts in
                                # the response to Question 7 and
                                # continues in the statement of
                                # Question 8.  It appears that the
                                # "c)" and "e)" in Question 8 should
                                # actually be <LI> markers, which
                                # would be consistent with the actual
                                # <LI> there being items a, b and d.
                                ('<BR>\n<B>Question</B> 8',
                                 '<BR></OL>\n<B>Question</B> 8'),
                                ('Refer to subclause 6.1.2.5, page 22, '
                                 'lines 32-36: <BR>\n<BR>',
                                 'Refer to subclause 6.1.2.5, page 22, '
                                 'lines 32-36: <BR>\n<BR><OL TYPE=a>'),
                                ('</TT>c) <BR>', '</TT><LI><BR>'),
                                ('</TT>e) <BR>', '</TT><LI><BR>')),
                'dr_051.html': (('</TT>\n<A HREF="dr_050.html">',
                                 '</TT>\n<BR>\n<A HREF="dr_050.html">'),),
                'dr_054.html': (('<A HREF="dr_042.html"> Defect '
                                 'Report #042 Question 1</A>',
                                 '<A HREF="dr_042.html#Question1"> Defect '
                                 'Report #042 Question 1</A>'),),
                'dr_072.html': (('<A HREF="dr_044.html">Defect '
                                 'Report #044, question 1</A>',
                                 '<A HREF="dr_044.html#Question1">Defect '
                                 'Report #044, question 1</A>'),),
                'dr_074.html': (('sublause', 'subclause'),),
                'dr_088.html': (('preceeded', 'preceded'),),
                'dr_096.html': (('occuring', 'occurring'),),
                'dr_098.html': (('Posfix', 'Postfix'),),
                'dr_105.html': (('compatability', 'compatibility'),),
                'dr_108.html': (('preceeding', 'preceding'),),
                'dr_109.html': (('evaulation', 'evaluation'),),
                'dr_110.html': (('<A HREF="dr_013.html">RFI #13, '
                                 'question #1</A>',
                                 '<A HREF="dr_013.html#Question1">RFI #13, '
                                 'question #1</A>'),),
                'dr_114.html': (('initialiers', 'initializers'),),
                'dr_116.html': (('considerd', 'considered'),),
                'dr_117.html': (('preceeding', 'preceding'),),
                'dr_119.html': (('Submission Daee', 'Submission Date'),),
                'dr_130.html': (('implemetation', 'implementation'),),
                'dr_144.html': (('preceeding', 'preceding'),),
                'dr_145.html': (('Sematics', 'Semantics'),
                                ('consant', 'constant'),
                                ('implicity', 'implicitly'),
                                ('desingator', 'designator')),
                'dr_157.html': (('</TT> <I>Invalid</I><TT>',
                                 ' <I>Invalid</I>'),
                                ('</TT><I> Invalid</I> <TT>',
                                 '<I> Invalid</I> ')),
                'dr_160.html': (('stddef.h &gt;', 'stddef.h&gt;'),
                                ('reseved', 'reserved')),
                'dr_162.html': (('retruned', 'returned'),),
                'dr_165.html': (('identifer', 'identifier'),),
                'dr_166.html': (('Subclasue', 'Subclause'),),
                'dr_167.html': (('<A HREF="dr_014.html#Question14"> Defect '
                                 'Report #014, Question 2</A>',
                                 '<A HREF="dr_014.html#Question2"> Defect '
                                 'Report #014, Question 2</A>'),),
                'dr_170.html': (('occurence', 'occurrence'),),
                'dr_171.html': (('Commitee', 'Committee'),),
                'dr_172.html': (('\n<A HREF="dr_171.html">',
                                 '\n<BR>\n<A HREF="dr_171.html">'),),
                'dr_201.htm': (('</tt> <i>make P1', ' <i>make P1'),
                               ('array</i><tt>', 'array</i>')),
                'dr_202.htm': (('20001-01-22', '2001-01-22'),),
                'dr_235.htm': (('Sumitter', 'Submitter'),
                               ('<br>\n     <a href="dr_234.htm">',
                                '\n     <p><a href="dr_234.htm">')),
                'dr_264.htm': (('<ol>\n      <li value="4">',
                                '<ol start="4">\n      <li>'),),
                'dr_282.htm': (('<br>\n     <b>Summary</b>',
                                '\n     <p><b>Summary</b>'),),
                'dr_289.htm': (('<tt><i>direct-abstract-declarator</i></tt>',
                                '<i>direct-abstract-declarator</i>'),
                               ('<tt><i>direct-abstract-declarator'
                                '<sub>opt</sub></i> ',
                                '<i>direct-abstract-declarator'
                                '<sub>opt</sub></i> <tt>'),
                               ('<i>type-qualifier-list<sub>opt</sub>\n      '
                                'assignment-expression<sub>opt</sub></i>',
                                '</tt><i>type-qualifier-list<sub>opt</sub>\n'
                                '      assignment-expression<sub>opt</sub>'
                                '</i><tt>'),
                               ('<i>type-qualifier-list<sub>opt</sub>\n      '
                                'assignment-expression</i>',
                                '</tt><i>type-qualifier-list<sub>opt</sub>\n'
                                '      assignment-expression</i><tt>'),
                               ('<i>type-qualifier-list</i>',
                                '</tt><i>type-qualifier-list</i><tt>'),
                               ('<i>assignment-expression</i>',
                                '</tt><i>assignment-expression</i><tt>'),
                               ('<i>assignment-expression<sub>opt</sub></i>',
                                '</tt><i>assignment-expression<sub>opt</sub>'
                                '</i><tt>')),
                'dr_307.htm': (('<var>', '</code><var>'),
                               ('</var>', '</var><code>')),
                'dr_311.htm': (('Commitee', 'Committee'),),
                'dr_315.htm': (('<br>\n    <a href="dr_314.htm">',
                                '</blockquote>\n    <p><a href="dr_314.htm">'),
                               ('</blockquote>\n</body>', '</body>')),
                'dr_318.htm': (('<b>Reference Document:</b> Version:',
                                '<b>Reference Document:</b><br>'
                                '<b>Version:</b>'),),
                'dr_331.htm': (('2006/08/01', '2006-08-01'),),
                'dr_337.htm': (('Austin Group<br>\n  <br>\n',
                                'Austin Group<br>\n'),),
                'dr_341.htm': (('2007-03-24&gt;', '2007-03-24'),),
                'dr_343.htm': (('<b>Date: 2007-09-07</b>',
                                '<b>Date:</b> 2007-09-07'),
                               ('<b>Subject: Initializing qualified '
                                'wchar_t arrays</b>',
                                '<b>Subject:</b> Initializing qualified '
                                'wchar_t arrays')),
                # The DR submitter for CSCR DR#1 was lost at some
                # point in the defect report summary, but is present
                # in N1891 (version 1.1 of that summary).
                'n2150.htm': (('<b>Submission Date:</b> 2014-03-11<br>',
                               '<b>Submitter:</b> Clive Pygott<br>'
                               '<b>Submission Date:</b> 2014-03-11<br>'),),
                'n2396.htm': (('<code>Note </code>', '<b>Note</b> '),
                              ('<code>Note 11:</code>', '<b>Note 11:</b>'),
                              ('<code>Note 13:</code>', '<b>Note 13:</b>'),
                              ('<b>Submission Date:</b> 2012-1-11',
                               '<b>Submission Date:</b> 2012-01-11'),
                              # DR #417; use the date of the start of
                              # the October 2012 meeting.
                              ('<b>Submission Date:</b> Oct 2012',
                               '<b>Submission Date:</b> 2012-10-22'),
                              ('<b>Submission Date:</b> 2012-9-13<br>',
                               '<b>Submission Date:</b> 2012-09-13<br>'),
                              ('<b>Submission Date:</b> 2013/07/21<br>',
                               '<b>Submission Date:</b> 2013-07-21<br>'),
                              ('can not be cyclic', 'cannot be cyclic'),
                              ('<pre>\n        <dfn>struct-declaration:\n'
                               '               specifier-qualifier-list '
                               'struct-declarator-list<sub>opt</sub> ;\n'
                               '               static_assert-declaration'
                               '</dfn>\n</pre>',
                               '<blockquote>\n<dfn>struct-declaration:\n<br>'
                               '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                               'specifier-qualifier-list&nbsp;'
                               'struct-declarator-list<sub>opt</sub></dfn>'
                               '&nbsp;<code>;</code><dfn>\n<br>'
                               '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                               'static_assert-declaration'
                               '</dfn>\n</blockquote>'),
                              ('a href="#dr_493">CR 479</a>',
                               'a href="#dr_493">CR 493</a>')),
                'n2397.htm': (('macro-\nreplacement', 'macro-replacement'),
                              ('macro- replacement', 'macro-replacement'))}


def clean_per_file(doc, text):
    """Clean up unambiguous typos, formatting inconsistencies, and (if
    they affect subsequent processing) HTML inconsistencies, where a
    hardcoded change specific to a given file is more appropriate than a
    broader algorithmic change."""
    replacements = TEXT_REPLACE.get(doc, ())
    for x, y in replacements:
        text = text.replace(x, y)
    if doc in EMBC_2004_ALL:
        # The Embedded C files are very differently structured from
        # the rest because of the conversion from PDF to HTML; fix up
        # issues here.
        # First, remove page breaks.
        if doc == 'n1180.html':
            text = re.sub(
                '<br/>\n'
                '[0-9]&nbsp;<br/>\n'
                '<hr/>\n'
                '<a name=[0-9]></a>WG14&nbsp;N1180&nbsp;<br/>\n',
                '<br/>\n',
                text)
        else:
            text = re.sub(
                '</b><br/>\n'
                '<hr/>\n'
                '<a name=[0-9]></a><b>',
                '<br/>\n',
                text)
            text = re.sub(
                '<br/>\n'
                '<hr/>\n'
                '<a name=[0-9]></a>',
                '<br/>\n',
                text)
        text = text.replace('<br/>\n8&nbsp;<br/>\n<hr/>\n</body>', '</body>')
        text = text.replace('<hr/>\n', '')
        text = text.replace('<br/>&nbsp;<br/>', '<p>')
        text = text.replace('<br/>\n&nbsp;<br/>', '<p>')
        text = text.replace('&nbsp;', ' ')
        # Overlapping text in PDF.
        if doc == 'n1096.html':
            text = text.replace("value b i(ts<br/>\ns '<br/>\nee",
                                "value bits ' (see")
        text = re.sub('<br/>\n(<b>Issue .*?)<br/></b>',
                      r'\n<p>\1</b><p>\n',
                      text)
        text = text.replace('<br/>\nProposed solution:',
                            '\n<p>Proposed solution:')
        text = text.replace('<br/>\n<b>Email crossreference',
                            '\n<p><b>Email crossreference')
        text = text.replace('<br/>\n<b>Defect ', '\n<p><b>Defect ')
        text = re.sub('(?:<p>|<br/>)<b>Defect ([0-9]+): ?<br/></b>',
                      r'<p><b>Defect \1:</b><p>',
                      text)
        text = re.sub('(?:<p>|<br/>)<b>Defect ([0-9]+) ?<br/></b>Problem',
                      r'<p><b>Defect \1</b><p>Problem',
                      text)
        text = text.replace('<br/>\nSolution: ', '\n<p>Solution: ')
        text = text.replace('<br/>\nChanges:<br/>\n', '\n<p>Changes:\n<p>')
        text = text.replace('<br/>\nChanges: ', '\n<p>Changes: ')
        text = text.replace('<br/>\nChange: ', '\n<p>Change: ')
        text = text.replace('<br/>\nAffected sections',
                            '\n<p>Affected sections')
        text = text.replace('<br/>\nProssible solution: ',
                            '\n<p>Possible solution: ')
        text = text.replace('to read:<br/>', 'to read:\n<p>')
        # Issue 1 in N1071.
        if doc == 'n1071.html':
            text = re.sub("<br/>\n?- ?(use|change|'q'|'y')", r'<li>\1', text)
            text = text.replace('solutions:<li>', 'solutions:<ul><li>')
            text = text.replace("<li>'q'", "<ul><li>'q'")
            text = text.replace("'w');<li>", "'w');</ul><li>")
            text = text.replace('else.\n<p><b>Issue 2',
                                'else.</ul>\n<p><b>Issue 2')
        # Issue 2 in N1071.
        text = text.replace('for overflow handling.<br/>',
                            'for overflow handling.\n<p>')
        # Issue 4 in N1071.
        text = text.replace('possibly wrong.<br/>\n',
                            'possibly wrong.\n<p>')
        # Issue 7 in N1071.
        text = re.sub(r'require that<br/>\n(Fractional.*?result\.)<br/>\n',
                      r'require that\n<blockquote>\1</blockquote>\n',
                      text)
        text = re.sub(
            r'offending text by:<br/>\n'
            r'(When saturation.*?in the result\.)\n<p>',
            r'offending text by:\n<blockquote>\1</blockquote>\n<p>',
            text)
        # Issue 11 in N1071.
        text = re.sub('\n(register.*?= 32;)<br/>\n',
                      r'<pre>\1</pre>',
                      text)
        # Issue 12 in N1071.
        text = re.sub(
            r'\n(The <i>specifier-qualifier-list.*?qualifier\.)<br/>\n',
            r'\n<blockquote>\1</blockquote>\n',
            text)
        text = re.sub('\n(struct one.*?;)(?:<br/>\n|\n<p>)',
                      r'<pre>\1</pre>',
                      text)
        text = re.sub(
            r'\n(Within a structure.*?address space qualifier\.)\n<p>',
            r'\n<blockquote>\1</blockquote>\n<p>',
            text)
        # Email cross-reference in N1071.
        text = re.sub('\n([0-9][0-9]?):<br/>\n',
                      r'<p>\1: ',
                      text)
        # Defects 2, 4 and 8.
        text = re.sub('<br/>\n?&bull; ?', '<li>', text)
        text = re.sub('<p>&bull; ?', '<li>', text)
        text = text.replace('Changes: <li>', 'Changes: <ul><li>')
        text = text.replace('Changes:\n<li>', 'Changes:\n<ul><li>')
        text = text.replace('Replacement text for 5.2.4.2.3:',
                            '<li>Replacement text for 5.2.4.2.3:\n<ul>')
        text = text.replace('text for 7.18a.6.7: <li>',
                            'text for 7.18a.6.7: <ul><li>')
        text = text.replace('text for 7.18a.6.7:<li>',
                            'text for 7.18a.6.7:<ul><li>')
        text = text.replace('Add to 7.18a.6.7:',
                            'Add to 7.18a.6.7:\n<blockquote>')
        text = re.sub('\n(If an object is declared.*?)\n',
                      r'\n<blockquote>\1</blockquote>\n',
                      text)
        text = text.replace('<p><b>Defect 3', '</ul></ul><p><b>Defect 3')
        text = text.replace('<p><b>Defect 5',
                            '</blockquote></ul><p><b>Defect 5')
        text = text.replace('<p><b>Defect 9', '</ul><p><b>Defect 9')
        # Defect 9.
        text = re.sub(
            r'(<b>Clause 6\.5.*?not modify the stored(?: |<br/>)value\.)',
            r'<blockquote>\1</blockquote>',
            text,
            flags=re.DOTALL)
        text = text.replace('.72)', '.<sup>72)</sup>')
        # Defects 20, 21 and 22.
        if doc in ('n1096.html', 'n1180.html'):
            text = re.sub('<br/>\n?- ?if', '<li>if', text)
            text = re.sub('<br/>\n?- ?change', '<li>change', text)
            text = re.sub('<br/>\n?- ?remove', '<li>remove', text)
            text = re.sub('<p>- ?if', '<li>if', text)
            text = re.sub('<p>- ?change', '<li>change', text)
            text = re.sub('<p>- ?remove', '<li>remove', text)
            text = text.replace('Solution: <li>', 'Solution: <ul><li>')
            text = text.replace('Solution:<li>', 'Solution:<ul><li>')
            text = text.replace(': <li>if', ': <ul><li>if')
            text = text.replace(':<li>if', ':<ul><li>if')
            text = text.replace('7.18a.6.4 reads:',
                                '7.18a.6.4 reads:<blockquote>')
            text = text.replace('Note: if the value of the fixed-point',
                                '</ul>Note: if the value of the fixed-point')
            text = text.replace('exactly N-1.', 'exactly N-1.</blockquote>')
            text = text.replace('Note as follows:',
                                'Note as follows:<blockquote>')
            text = text.replace('Note as<br/>follows:',
                                'Note as follows:<blockquote>')
            text = text.replace('is exactly N.', 'is exactly N.</blockquote>')
            text = text.replace('is <br/>exactly N.',
                                'is exactly N.</blockquote>')
            text = text.replace('<br/>\n</body>', '</ul>\n</body>')
            text = text.replace('<p> </body>', '</ul>\n</body>')
        # Defect 8.
        m = re.search(r'// file 1.*?return reg_a; \}', text, flags=re.DOTALL)
        if m:
            codetxt = m.group(0)
            codetxt = codetxt.replace('<br/>', '\n')
            codetxt = codetxt.replace('<p>', '\n\n')
            text = (text[:m.start(0)]
                    + '<pre>' + codetxt + '</pre>'
                    + text[m.end(0):])
        # Defect 9.
        m = re.search('_X char a.*?p = &amp;a;', text, flags=re.DOTALL)
        if m:
            codetxt = m.group(0)
            codetxt = codetxt.replace('<br/>\n', '\n')
            codetxt = codetxt.replace('<br/>', '\n')
            codetxt = codetxt.replace('<p>', '\n\n')
            text = (text[:m.start(0)]
                    + '<pre>' + codetxt + '</pre>'
                    + text[m.end(0):])
        # Defect 19.
        m = re.search('<b>(uint_uhr_t.*?)</b>', text, flags=re.DOTALL)
        if m:
            text = (text[:m.start(0)]
                    + '<pre>' + m.group(1).replace('<br/>', '\n') + '</pre>'
                    + text[m.end(0):])
        # Defect 21.
        text = re.sub('<br/>( +countls.*?)<br/>',
                      r'<pre>\1</pre>',
                      text)
        # Defect 22.
        m = re.search('<b>(#include.*?)</b>', text, flags=re.DOTALL)
        if m:
            text = (text[:m.start(0)]
                    + '<pre>' + m.group(1).replace('<br/>', '\n') + '</pre>'
                    + text[m.end(0):])
        # Remove remaining hard line breaks.
        text = text.replace('<br/>\n', '\n')
        text = text.replace('<br/>', '\n')
    return text


def get_one_tag(doc, rtext):
    """Process rtext up to the next tag, returning (a) text before that
    tag, (b) text to output for that tag, if it's a comment, (c) the
    tag name (or None), (d) whether an end tag, (e) the tag attributes
    (or None), (f) the text after that tag."""
    if '<' not in rtext and '>' not in rtext:
        return (rtext, '', None, False, None, '')
    m = re.search('<([^<>]*)>', rtext)
    if not m:
        raise ValueError("unmatched '<' or '>' in %s [%s]" % (doc, rtext))
    before = rtext[:m.start(0)]
    tag = m.group(0)
    tag_contents = m.group(1)
    after = rtext[m.end(0):]
    if '<' in before or '>' in before:
        raise ValueError("unmatched '<' or '>' in %s [%s]" % (doc, before))
    if tag.startswith('<!DOCTYPE'):
        # Discard the DOCTYPE.
        return before, '', None, False, None, after
    if tag.startswith('<!--') and tag.endswith('-->'):
        # Pass through the comment (may be relevant for splitting
        # individual issues out of multi-issue files, though not
        # for the final output).
        return before, tag, None, False, None, after
    tag_contents = tag_contents.strip()
    tag_contents = re.sub(r'\s+', ' ', tag_contents, flags=re.ASCII)
    if tag_contents.startswith('/'):
        end_tag = True
        tag_contents = tag_contents[1:].lstrip()
    else:
        end_tag = False
    m = re.match('[0-9A-Za-z:]+', tag_contents)
    if not m:
        raise ValueError('unknown tag %s in %s' % (tag, doc))
    tag_name = m.group(0).lower()
    tag_contents = tag_contents[m.end(0):]
    if end_tag:
        if tag_contents not in ('', ' '):
            raise ValueError('bad end tag %s in %s' % (tag, doc))
        tag_attrs = None
    else:
        seen_attrs = set()
        tag_attrs = []
        while tag_contents not in ('', ' ', '/', ' /'):
            if not tag_contents.startswith(' '):
                raise ValueError('missing space in tag %s in %s'
                                 % (tag, doc))
            tag_contents = tag_contents[1:]
            m = re.match('[-0-9A-Za-z:]+', tag_contents)
            if not m:
                raise ValueError('unknown tag attribute %s in %s'
                                 % (tag, doc))
            attr_name = m.group(0).lower()
            if attr_name in seen_attrs:
                raise ValueError('duplicate tag attribute %s in %s'
                                 % (tag, doc))
            seen_attrs.add(attr_name)
            tag_contents = tag_contents[m.end(0):]
            have_value = False
            if tag_contents.startswith('='):
                have_value = True
                tag_contents = tag_contents[1:].lstrip()
            elif tag_contents.startswith(' ='):
                have_value = True
                tag_contents = tag_contents[2:].lstrip()
            if have_value:
                if tag_contents.startswith('"'):
                    m = re.match('"[^"]*"', tag_contents)
                    if not m:
                        raise ValueError(
                            'unclosed attribute value %s in %s'
                            % (tag, doc))
                    value = m.group(0)
                    tag_contents = tag_contents[m.end(0):]
                elif tag_contents.startswith("'"):
                    m = re.match("'[^']*'", tag_contents)
                    if not m:
                        raise ValueError(
                            'unclosed attribute value %s in %s'
                            % (tag, doc))
                    value = m.group(0)
                    tag_contents = tag_contents[m.end(0):]
                    if '"' not in value:
                        value = '"%s"' % value[1:-1]
                else:
                    m = re.match('[^ ]+', tag_contents)
                    if not m:
                        raise ValueError(
                            'missing attribute value %s in %s'
                            % (tag, doc))
                    value = m.group(0)
                    tag_contents = tag_contents[m.end(0):]
                    if '"' not in value:
                        value = '"%s"' % value
                    elif "'" not in value:
                        value = "'%s'" % value
                    else:
                        raise ValueError(
                            'cannot quote attribute value %s in %s'
                            % (tag, doc))
                tag_attrs.append((attr_name, value))
            else:
                tag_attrs.append((attr_name, None))
    return before, '', tag_name, end_tag, tag_attrs, after


def text_for_tag(tag_name, end_tag, tag_attrs):
    """Return text to output for one tag."""
    if end_tag:
        return '</%s>' % tag_name
    new_text_list = []
    new_text_list.append('<%s' % tag_name)
    for attr_name, value in tag_attrs:
        if value is None:
            new_text_list.append(' %s' % attr_name)
        else:
            new_text_list.append(' %s=%s' % (attr_name, value))
    new_text_list.append('>')
    return ''.join(new_text_list)


# Known HTML tags accepted in input.  Any tag that won't be adequately
# processed into Markdown by default needs manual processing in this
# script to ensure a good conversion.
KNOWN_TAGS = {
    # Tags we discard early on, as not having any semantics relevant
    # to our processing.
    'meta', 'thead', 'tbody', 'small',
    # Tags that are discarded later because only content extracted
    # from the <body> ever gets converted.
    'html', 'head', 'title', 'body', 'style',
    # Tags with some handling by markdownify that should be more or
    # less OK (possibly with some customization needed).
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'li', 'blockquote',
    'pre', 'br', 'a', 'code', 'b', 'i', 'del', 'sup', 'sub', 'table', 'tr',
    'td', 'th', 'hr',
    # Tags markdownify handles as aliases (but we canonicalize to
    # simplify subsequent processing).
    'strong', 'em',
    # Tags we can handle as aliases ourselves.
    'tt', 'var', 'strike', 'dfn',
    # Custom handling needed (output HTML): <u> and <ins> have no
    # direct Markdown equivalent.
    'u', 'ins',
    # Custom handling needed: no direct Markdown equivalent.
    'dl', 'dt', 'dd',
    # Custom handling needed: may discard or convert into other tags
    # depending on attributes (this also applies to style attributes
    # on other tags).
    'span', 'center', 'div', 'font'}

# Known tags discarded early on.
KNOWN_TAGS_DISCARD = {'meta', 'thead', 'tbody', 'small'}


# Known tags handled as aliases early on.
KNOWN_TAGS_ALIAS = {
    'tt': 'code', 'strong': 'b', 'em': 'i', 'var': 'i', 'strike': 'del',
    'dfn': 'i', 'ins': 'u'}


# Known tags that are empty so should only have opening tags.
KNOWN_TAGS_EMPTY = {'br', 'hr'}


# Known tags that are considered inline tags.  <uncode> is a
# pseudo-tag used internally to translate <span
# style="font-family:serif">, which in turn is used for all
# non-monospace font-family styles, to handle cases where such a style
# is specified inside <code>.
KNOWN_TAGS_INLINE = {'br', 'a', 'code', 'b', 'i', 'del', 'sup', 'sub', 'u',
                     'span', 'uncode'}


# Known non-inline tags that should not contain other non-inline tags.
KNOWN_TAGS_LEAF = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre'}


# Attributes to discard on certain tags (regardless of the attribute
# value).
KNOWN_ATTRS_DISCARD = {
    # <a name> is only ever linked to when it's a link to a question
    # within an issue, and those links are reprocessed, so the <a
    # name> are redundant.  <a id> is only used for links to Suggested
    # Technical Corrigendum within a C11 issue (and indeed one link to
    # #tc is incorrect as #tc is for a different issue), which doesn't
    # seem to be a necessary link; likewise, <li id> is for links to
    # references within an issue, which also seem unnecessary.
    'a': {'id', 'name'},
    'b': {'style'},
    'body': {'bgcolor', 'link', 'vlink'},
    'br': {'style'},
    'dl': {'compact'},
    'h2': {'align', 'id'},
    'h3': {'align'},
    'hr': {'style'},
    'html': {'lang', 'xml:lang', 'xmlns'},
    'i': {'style'},
    'li': {'id'},
    'p': {'align'},
    'pre': {'class'},
    'span': {'lang'},
    'table': {'bgcolor', 'border', 'cellpadding', 'cellspacing', 'class',
              'style', 'summary'},
    'td': {'style', 'valign', 'width'},
    'th': {'align', 'style'},
    'tr': {'style'},
    'ul': {'type'}}


# Attributes to keep on certain tags (possibly after custom logic to
# remap or discard certain cases).
KNOWN_ATTRS_KEEP = {
    'a': {'href', 'title'},
    'center': {'class'},
    'div': {'style'},
    'ol': {'start', 'type'},
    'p': {'class', 'style'},
    'span': {'class', 'style'},
    'style': {'type'},
    'sup': {'style'}}


def clean_tags(doc, text):
    """Clean up HTML tags, putting them in a canonical form where possible
    and removing attributes not relevant for subsequent processing.  This
    only makes changes that can be done locally on a single tag, not
    changes that would involve modifying earlier or later text or looking
    at the whole of an element's content at once.  This is also the point
    where it is checked that '<' and '>' only appear as delimiters for
    known tags."""
    new_text_list = []
    rtext = text
    while '<' in rtext or '>' in rtext:
        before, tag_text, tag_name, end_tag, tag_attrs, rtext = get_one_tag(
            doc, rtext)
        new_text_list.append(before)
        new_text_list.append(tag_text)
        if tag_name is None:
            continue
        if tag_name not in KNOWN_TAGS:
            raise ValueError('unknown tag %s in %s' % (tag_name, doc))
        if end_tag and tag_name in KNOWN_TAGS_EMPTY:
            raise ValueError('bad end tag %s in %s' % (tag_name, doc))
        if tag_name in KNOWN_TAGS_DISCARD:
            continue
        if tag_name in KNOWN_TAGS_ALIAS:
            tag_name = KNOWN_TAGS_ALIAS[tag_name]
        if tag_name == 'font':
            # Remap to <span>, with attributes remapped to style=.
            tag_name = 'span'
            if not end_tag:
                new_style = []
                for attr_name, value in tag_attrs:
                    if value is None or not (value.startswith('"')
                                             and value.endswith('"')):
                        raise ValueError('bad font attribute %s in %s'
                                         % (attr_name, doc))
                    value = value[1:-1]
                    if attr_name == 'size':
                        continue
                    if attr_name == 'color':
                        new_style.append('color:%s' % value)
                    elif attr_name == 'face':
                        new_style.append('font-family:%s' % value)
                    else:
                        raise ValueError('bad font attribute %s in %s'
                                         % (attr_name, doc))
                if new_style:
                    tag_attrs = [('style', '"%s"' % ';'.join(new_style))]
                else:
                    tag_attrs = []
        if not end_tag:
            to_discard = KNOWN_ATTRS_DISCARD.get(tag_name, set())
            to_keep = KNOWN_ATTRS_KEEP.get(tag_name, set())
            cleaned_tag_attrs = []
            for attr_name, value in tag_attrs:
                if attr_name in to_discard:
                    continue
                if attr_name == 'class':
                    if value in ('"MsoNoSpacing"', '"MsoNormal"',
                                 '"MsoNormalCxSpMiddle"', '"GramE"',
                                 '"SpellE"'):
                        continue
                if tag_name == 'a' and attr_name == 'href':
                    # Put URLs for WG14 website in a consistent canonical form.
                    value = value.replace('std.dkuug.dk', 'www.open-std.org')
                    value = value.replace('www.dkuug.dk', 'www.open-std.org')
                    value = value.replace('http://www.open-std.org',
                                          'https://www.open-std.org')
                    value = value.replace(
                        'https://www.open-std.org/JTC1/SC22/WG14',
                        'https://www.open-std.org/jtc1/sc22/wg14')
                    value = value.replace(
                        'https://www.open-std.org/jtc1/sc22/WG14',
                        'https://www.open-std.org/jtc1/sc22/wg14')
                    if not value.startswith('"http'):
                        if not (value.startswith('"') and value.endswith('"')):
                            raise ValueError(
                                'bad href %s in %s' % (value, doc))
                        if value == '"#tc"':
                            # Discard these within-issue links.
                            continue
                        if re.fullmatch('"#[1-9][0-9]*"', value):
                            # Discard these within-issue links.
                            continue
                        value = '"%s"' % urllib.parse.urljoin(
                            doc_url(doc), value[1:-1])
                    # There are several typos in links to the WG14 website.
                    if value.startswith('"https://www.open-std.org/'):
                        value = value.replace('dr_340.htm:', 'dr_340.htm')
                        value = value.replace('n1138.txt', 'n1138.pdf')
                        value = value.replace('n1987.html ', 'n1987.pdf')
                        value = value.replace('n2007."', 'n2007.pdf"')
                        value = value.replace('n2025."', 'n2025.htm"')
                        value = value.replace('n2027."', 'n2025.htm"')
                        value = value.replace('n2031."', 'n2031.htm"')
                        value = value.replace('n2032."', 'n2032.htm"')
                        value = value.replace('n2037."', 'n2037.htm"')
                        value = value.replace('n2038."', 'n2038.htm"')
                        value = value.replace('n2077.html ', 'n2077.pdf')
                    # Replace issue references with an issue: URL.
                    if value.startswith('"' + WG14_DOCS):
                        tvalue = value[1+len(WG14_DOCS):-1]
                        m = re.fullmatch(r'dr_([0-9][0-9][0-9])\.html?',
                                         tvalue)
                        if m:
                            value = 'issue:0%s' % m.group(1)
                        else:
                            m = re.fullmatch(
                                r'dr_([0-9][0-9][0-9])\.html#Question([0-9]+)',
                                tvalue)
                            if m:
                                value = '"issue:0%s.%02d"' % (
                                    m.group(1), int(m.group(2)))
                            else:
                                # There are no internal links to
                                # Embedded C or C Secure Coding Rules
                                # issues other than from the tables of
                                # contents in the issue lists, so the
                                # remaining cases are C11/C17 and CFP.
                                m = re.fullmatch(
                                    r'(n2396|n2397|summary)\.htm#dr_([0-9]+)',
                                    tvalue)
                                if m:
                                    if m.group(1) in ('n2396', 'summary'):
                                        value = '"issue:0%s"' % m.group(2)
                                    else:
                                        value = ('"issue:0CFP.%02d"'
                                                 % int(m.group(2)))
                if attr_name == 'style':
                    if (tag_name == 'ol'
                        and value == '"list-style-type: upper-alpha"'):
                        attr_name = 'type'
                        value = '"A"'
                    else:
                        # Discard all styles except those indicating
                        # colours, basic text styling or the use of a
                        # fixed-width font.  margin-left is kept as an
                        # indicator of block quoting.
                        if (value is None
                            or (not (value.startswith('"')
                                     and value.endswith('"'))
                                and not (value.startswith("'")
                                         and value.endswith("'")))):
                            raise ValueError('bad style attribute %s in %s'
                                             % (value, doc))
                        value = value[1:-1].replace(' ', '')
                        styles_list = [x for x in value.split(';') if x]
                        styles_new = []
                        for s in styles_list:
                            k, v = s.split(':')
                            if k.startswith('mso-'):
                                continue
                            if k == 'color':
                                if v not in ('black', '#000000'):
                                    styles_new.append('%s:%s' % (k, v))
                            elif k == 'font-weight':
                                if v != 'normal':
                                    styles_new.append('%s:%s' % (k, v))
                            elif k == 'font-family':
                                if 'monospace' in v or 'Courier' in v:
                                    styles_new.append('%s:monospace' % k)
                                else:
                                    styles_new.append('%s:serif' % k)
                            elif k in ('margin-left', 'text-decoration',
                                       'background-color'):
                                styles_new.append('%s:%s' % (k, v))
                            elif k in ('font-size', 'line-height',
                                       'margin-bottom', 'margin-right',
                                       'margin-top', 'page-break-after',
                                       'tab-stops', 'text-autospace',
                                       'text-indent'):
                                continue
                            else:
                                raise ValueError('unknown style %s in %s'
                                                 % (k, doc))
                        if not styles_new:
                            continue
                        value = '"%s"' % ';'.join(styles_new)
                if attr_name not in to_keep:
                    raise ValueError('unknown attribute %s on %s tag in %s'
                                     % (attr_name, tag_name, doc))
                cleaned_tag_attrs.append((attr_name, value))
            tag_attrs = cleaned_tag_attrs
        new_text_list.append(text_for_tag(tag_name, end_tag, tag_attrs))
    new_text_list.append(rtext)
    return ''.join(new_text_list)


class ProcessNesting:

    """Process the document based on the nested structure of HTML tags."""

    def __init__(self, doc, text):
        self.doc = doc
        self.new_text_list = []
        self.rtext = text
        self.open_tags = []
        self.wrap_text_in = []
        self.end_wrap = []
        self.tag_outside = []
        self.tag_inside = []
        self.replace_end = []

    def handle_before_tag(self, before):
        """Handle the text coming before a tag."""
        should_wrap = (self.wrap_text_in
                       and self.wrap_text_in[-1]
                       and before.strip())
        if should_wrap:
            for t in self.wrap_text_in[-1]:
                self.handle_start_tag(t, [])
        self.new_text_list.append(before)
        if should_wrap:
            for t in reversed(self.wrap_text_in[-1]):
                self.handle_end_tag(t)

    def handle_comment(self, tag_text):
        """Handle an HTML comment."""
        self.new_text_list.append(tag_text)

    def push_tag(self, tag_name):
        """Add a tag to the stack of open tags."""
        self.open_tags.append(tag_name)
        if self.wrap_text_in:
            self.wrap_text_in.append(self.wrap_text_in[-1])
        else:
            self.wrap_text_in.append([])
        self.end_wrap.append([])
        self.tag_outside.append([])
        self.tag_inside.append([])
        self.replace_end.append(None)

    def pop_tag(self):
        """Remove a tag from the stack of open tags."""
        self.open_tags = self.open_tags[:-1]
        self.wrap_text_in = self.wrap_text_in[:-1]
        self.end_wrap = self.end_wrap[:-1]
        self.tag_outside = self.tag_outside[:-1]
        self.tag_inside = self.tag_inside[:-1]
        self.replace_end = self.replace_end[:-1]

    def check_nesting(self, tag_name):
        """Check for a tag inappropriately contained in another tag."""
        if tag_name not in KNOWN_TAGS_INLINE:
            for t in self.open_tags:
                if t in KNOWN_TAGS_INLINE or t in KNOWN_TAGS_LEAF:
                    raise ValueError(
                        '<%s> inside <%s> in %s [%s]'
                        % (tag_name, t, self.doc, self.rtext[:200]))
        if ((tag_name == 'li' and self.open_tags[-1] not in ('ol', 'ul'))
            or (tag_name in ('dt', 'dd') and self.open_tags[-1] != 'dl')
            or (tag_name == 'tr' and self.open_tags[-1] != 'table')
            or (tag_name in ('td', 'th') and self.open_tags[-1] != 'tr')):
            raise ValueError(
                '<%s> inside <%s> in %s [%s]'
                % (tag_name, self.open_tags[-1], self.doc, self.rtext[:200]))

    def handle_empty_tag(self, tag_name, end_tag, tag_attrs):
        """Handle an empty tag."""
        self.check_nesting(tag_name)
        self.new_text_list.append(text_for_tag(tag_name, end_tag, tag_attrs))

    def handle_start_tag_internal(self, tag_name, tag_attrs):
        """Output a start tag."""
        self.new_text_list.append(text_for_tag(tag_name, False, tag_attrs))

    def handle_start_tag(self, tag_name, tag_attrs, replace_tag=None):
        """Handle a start tag."""
        self.check_nesting(tag_name)
        if replace_tag != '':
            self.handle_start_tag_internal(
                replace_tag if replace_tag is not None else tag_name,
                tag_attrs)
        self.push_tag(tag_name)
        self.replace_end[-1] = replace_tag

    def handle_end_tag_internal(self, tag_name):
        """Output an end tag."""
        self.new_text_list.append(text_for_tag(tag_name, True, None))

    def handle_end_tag(self, tag_name):
        """Handle an end tag."""
        if not self.open_tags:
            raise ValueError('no open tag at </%s> in %s [%s]'
                             % (tag_name, self.doc, self.rtext[:200]))
        if tag_name != self.open_tags[-1]:
            raise ValueError('<%s> closed by </%s> in %s [%s]'
                             % (self.open_tags[-1], tag_name, self.doc,
                                self.rtext[:200]))
        for t in self.tag_inside[-1]:
            self.handle_end_tag_internal(t)
        if self.replace_end[-1]:
            tag_name = self.replace_end[-1]
        if self.replace_end[-1] != '':
            self.handle_end_tag_internal(tag_name)
        end_wrap = self.end_wrap[-1]
        tag_outside = self.tag_outside[-1]
        self.pop_tag()
        for t in tag_outside:
            self.handle_end_tag_internal(t)
        if end_wrap:
            for t in end_wrap:
                self.handle_start_tag(t, [])

    def run(self):
        """Execute the document processing.  Subclasses may act on the input
        as it is processed; this class itself just carries out checks while
        passing the input through."""
        while self.rtext:
            before, tag_text, tag_name, end_tag, tag_attrs, self.rtext = \
                get_one_tag(self.doc, self.rtext)
            self.handle_before_tag(before)
            # Handle HTML comments.
            if tag_text != '':
                self.handle_comment(tag_text)
            if tag_name is None:
                continue
            # Handle empty, start and end tags.
            if tag_name in KNOWN_TAGS_EMPTY:
                self.handle_empty_tag(tag_name, end_tag, tag_attrs)
            elif end_tag:
                self.handle_end_tag(tag_name)
            else:
                self.handle_start_tag(tag_name, tag_attrs)
        if self.open_tags:
            raise ValueError('%s ends without closing all tags' % self.doc)
        return ''.join(self.new_text_list)


class FixInvalidNesting(ProcessNesting):

    """Fix certain cases of badly nested tags or missing end tags."""

    def handle_before_tag(self, before):
        """Handle the text coming before a tag."""
        # Insert explicit paragraphs in certain contexts.
        if (before.strip()
            and self.open_tags
            and self.open_tags[-1] in ('body', 'blockquote', 'div')):
            self.handle_start_tag('p', [])
        super().handle_before_tag(before)

    def handle_comment(self, tag_text):
        """Handle an HTML comment."""
        if self.doc == 'n2396.htm':
            # Close <blockquote> tags crossing issue boundaries.
            # (Actually the original file has more </blockquote> than
            # <blockquote>, but heuristic replacement of some of those
            # by <blockquote> sometimes results in this issue.)
            if tag_text.startswith('<!-- LINKAGE'):
                while 'blockquote' in self.open_tags:
                    self.handle_end_tag('blockquote')
        if self.doc == 'n2397.htm':
            if self.open_tags and self.open_tags[-1] == 'p':
                self.handle_end_tag('p')
        super().handle_comment(tag_text)

    def maybe_close_p(self, tag_name, end_tag):
        """Close an unterminated <p> when any non-inline tag starts or ends."""
        if (self.open_tags
            and self.open_tags[-1] == 'p'
            and not (end_tag and tag_name == 'p')
            and tag_name not in KNOWN_TAGS_INLINE):
            self.handle_end_tag('p')

    def maybe_insert_p_for_tag(self, tag_name):
        """Insert explicit paragraphs for inline tags in certain contexts."""
        if (tag_name in KNOWN_TAGS_INLINE
            and self.open_tags
            and self.open_tags[-1] in ('body', 'blockquote', 'div')):
            self.handle_start_tag('p', [])

    def handle_empty_tag(self, tag_name, end_tag, tag_attrs):
        """Handle an empty tag."""
        self.maybe_close_p(tag_name, end_tag)
        self.maybe_insert_p_for_tag(tag_name)
        super().handle_empty_tag(tag_name, end_tag, tag_attrs)

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        self.maybe_close_p(tag_name, False)
        self.maybe_insert_p_for_tag(tag_name)
        # Close an unterminated <li> when another <li> starts.
        if (tag_name == 'li'
            and self.open_tags
            and self.open_tags[-1] == 'li'):
            self.handle_end_tag('li')
        # Fix specific invalid nesting cases from specific input files.
        wrap_num = 0
        if (self.doc == 'n2150.htm'
            and tag_name == 'ul'
            and self.open_tags[-1] == 'i'):
            wrap_num = 1
        if (self.doc in ('dr_025.html', 'dr_069.html', 'n2150.htm',
                         'n2396.htm', 'n2397.htm')
            and tag_name == 'pre'
            and self.open_tags[-1] in ('b', 'code')):
            wrap_num = 1
            if self.open_tags[-2] in ('b', 'code'):
                wrap_num = 2
        if self.doc == 'n2396.htm':
            if (tag_name == 'ul'
                and self.open_tags[-1] == 'ul'):
                self.handle_end_tag('ul')
                return
            if (tag_name == 'pre'
                and self.open_tags[-1] == 'pre'):
                self.handle_end_tag('pre')
                return
            if (tag_name == 'i'
                and self.open_tags[-1] == 'i'
                and self.new_text_list[-1] == 'struct-declarator-lists,'):
                self.handle_end_tag('i')
                return
            if (tag_name == 'blockquote'
                and self.open_tags[-1] == 'span'
                and self.open_tags[-2] == 'span'
                and self.open_tags[-3] == 'span'
                and self.open_tags[-4] == 'p'):
                self.handle_end_tag('span')
                self.handle_end_tag('span')
                self.handle_end_tag('span')
                self.handle_end_tag('p')
            if (tag_name == 'body'
                and self.open_tags[-1] != 'html'):
                return
        if (self.doc == 'n2397.htm'
            and tag_name == 'b'
            and self.open_tags[-1] == 'b'
            and self.new_text_list[-1] == 'fesetmode'):
            self.handle_end_tag('b')
            return
        if wrap_num:
            wrap_tags = self.open_tags[-wrap_num:]
            for t in reversed(wrap_tags):
                self.handle_end_tag(t)
            self.maybe_close_p(tag_name, False)
        super().handle_start_tag(tag_name, tag_attrs)
        if wrap_num:
            self.wrap_text_in[-1] = wrap_tags
            self.end_wrap[-1] = wrap_tags

    def handle_end_tag(self, tag_name):
        """Handle an end tag."""
        self.maybe_close_p(tag_name, True)
        # Close an unterminated <li> when a list ends.
        if (self.open_tags
            and self.open_tags[-1] == 'li'
            and tag_name in ('ol', 'ul')):
            self.handle_end_tag('li')
        # Fix specific invalid nesting cases from specific input files.
        if (self.doc in ('dr_003.html', 'dr_015.html')
            and tag_name == 'b'
            and self.open_tags[-1] == 'code'
            and self.rtext.startswith('</code>')):
            return
        if (self.doc == 'dr_045.html'
            and tag_name == 'b'
            and self.open_tags[-1] == 'code'
            and self.rtext.startswith('</code>')):
            tag_name = 'code'
            self.rtext = '</b>' + self.rtext[len('</code>'):]
        if (self.doc == 'dr_055.html'
            and tag_name == 'code'
                and self.open_tags[-1] == 'b'
            and self.rtext.startswith('</b>')):
            tag_name = 'b'
            self.rtext = '</code>' + self.rtext[len('</b>'):]
        if (self.doc == 'dr_121.html'
            and tag_name == 'b'
            and self.open_tags[-1] == 'i'):
            tag_name = 'i'
        if self.doc == 'n2396.htm':
            if (tag_name == 'blockquote'
                and self.open_tags[-1] == 'body'):
                self.handle_start_tag('blockquote', [])
                return
            if (tag_name == 'h2'
                and self.open_tags[-1] == 'h3'):
                tag_name = 'h3'
            if (tag_name == 'span'
                and self.open_tags[-1] == 'li'
                and self.rtext.startswith('<span>')):
                return
            if (tag_name == 'span'
                and self.open_tags[-1] == 'blockquote'
                and self.rtext.startswith('</span></span></p>')):
                self.rtext = self.rtext[len('</span></span></p>'):]
                return
            if (tag_name == 'p'
                and self.open_tags[-1] == 'span'):
                while self.open_tags[-1] == 'span':
                    self.handle_end_tag('span')
            if (tag_name == 'blockquote'
                and self.open_tags[-1] == 'u'
                and self.new_text_list[-2] == '<u>'
                and self.open_tags[-2] == 'p'):
                self.new_text_list[-2] = ''
                self.pop_tag()
                self.handle_end_tag('p')
            if (tag_name == 'code'
                and self.open_tags[-1] == 'b'
                and self.rtext.startswith('</b>')):
                return
            if (tag_name == 'p'
                and self.open_tags[-1] in ('blockquote', 'body', 'li')):
                return
            if (tag_name == 'span'
                and self.open_tags[-1] == 'p'):
                return
        if (self.doc in ('n2396.htm', 'n2397.htm')
            and tag_name == 'div'
            and self.open_tags[-1] in ('body', 'blockquote')):
            return
        if (self.doc == 'n2397.htm'
            and tag_name == 'pre'
            and self.open_tags[-1] == 'b'
            and self.rtext.startswith('</code></b>')):
            tag_name = 'b'
            self.rtext = '</pre></code>' + self.rtext[len('</code></b>'):]
        super().handle_end_tag(tag_name)


def clean_nesting(doc, text):
    """Clean up invalid testing of tags and missing end tags."""
    return FixInvalidNesting(doc, text).run()


# Tags to use outside for p class= attributes
P_CLASS_OUTSIDE = {'quote': 'blockquote', 'stdtext': 'blockquote'}


# Tags to use inside for p class= attributes
P_CLASS_INSIDE = {'alternative': 'u', 'inserted': 'u', 'strike': 'del'}


# Replacement tags for span class= attributes.
SPAN_CLASS_REPLACE = {'alternative': 'u', 'inserted': 'u', 'deleted': 'del'}


class ReplaceClass(ProcessNesting):

    """Replace 'class=' attributes by simpler markup."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        tclass = None
        if tag_name in ('p', 'span', 'center'):
            for tn, tv in tag_attrs:
                if tn == 'class':
                    tclass = tv[1:-1]
        tag_outside = None
        tag_inside = None
        tag_replace = None
        if tclass:
            if tag_name == 'p':
                tag_outside = P_CLASS_OUTSIDE.get(tclass, None)
                tag_inside = P_CLASS_INSIDE.get(tclass, None)
                tag_attrs = [t for t in tag_attrs if t[0] != 'class']
            if tag_name == 'span':
                tag_replace = SPAN_CLASS_REPLACE.get(tclass, None)
                if len(tag_attrs) != 1:
                    raise ValueError(
                        'replacing tag with multiple attributes: %s'
                        % repr(tag_attrs))
                if tag_replace:
                    tag_attrs = []
            if tag_name == 'center' and tclass == 'quote':
                tag_replace = 'blockquote'
                tag_inside = 'p'
                if len(tag_attrs) != 1:
                    raise ValueError(
                        'replacing tag with multiple attributes: %s'
                        % repr(tag_attrs))
                tag_attrs = []
        if tag_outside:
            super().handle_start_tag_internal(tag_outside, [])
        super().handle_start_tag(tag_name, tag_attrs, tag_replace)
        if tag_inside:
            super().handle_start_tag_internal(tag_inside, [])
        if tag_outside:
            self.tag_outside[-1] = [tag_outside]
        if tag_inside:
            self.tag_inside[-1] = [tag_inside]


def clean_class(doc, text):
    """Clean up use of class= on tags."""
    return ReplaceClass(doc, text).run()


class ReplaceColor(ProcessNesting):

    """Replace 'color' and 'background-color' CSS styles by simpler markup."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        tstyle = None
        if tag_name in ('span', 'sup'):
            for tn, tv in tag_attrs:
                if tn == 'style':
                    tstyle = tv[1:-1].split(';')
        tag_outside = None
        if tstyle:
            colors = [c for c in tstyle if 'color' in c]
            if len(colors) > 1:
                raise ValueError('multiple color styles: %s' % repr(tag_attrs))
            tstyle = [x for x in tstyle if 'color' not in x]
            if len(tag_attrs) != 1:
                raise ValueError(
                    'replacing tag with multiple attributes: %s'
                    % repr(tag_attrs))
            if tstyle:
                tag_attrs = [('style', '"%s"' % ';'.join(tstyle))]
            else:
                tag_attrs = []
            if colors and colors[0] in ('background-color:rgb(51,204,0)',
                                        'color:#C00000'):
                tag_outside = 'u'
            # All other color styles are appropriately discarded.
        if tag_outside:
            super().handle_start_tag_internal(tag_outside, [])
        super().handle_start_tag(tag_name, tag_attrs)
        if tag_outside:
            self.tag_outside[-1] = [tag_outside]


def clean_color(doc, text):
    """Clean up use of color CSS styles on tags."""
    return ReplaceColor(doc, text).run()


# Replacement tags for font-related CSS styles.
FONT_STYLES = {'font-family:monospace': 'code', 'font-family:serif': 'uncode',
               'font-weight:bold': 'b', 'text-decoration:underline': 'u'}


class ReplaceFont(ProcessNesting):

    """Replace font-related CSS styles by simpler markup."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        tstyle = None
        if tag_name == 'span':
            for tn, tv in tag_attrs:
                if tn == 'style':
                    tstyle = tv[1:-1].split(';')
        tag_replace = None
        if tstyle:
            if len(tstyle) > 1:
                raise ValueError('multiple font styles: %s' % repr(tag_attrs))
            if len(tag_attrs) != 1:
                raise ValueError(
                    'replacing tag with multiple attributes: %s'
                    % repr(tag_attrs))
            tag_replace = FONT_STYLES[tstyle[0]]
            if tag_replace == 'uncode' and 'code' not in self.open_tags:
                tag_replace = None
            tag_attrs = []
        super().handle_start_tag(tag_name, tag_attrs, tag_replace)


class ReplaceUncode(ProcessNesting):

    """Replace <uncode> pseudo-tags."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        tag_replace = None
        close_tags = []
        reopen_tags = []
        if tag_name == 'uncode':
            tag_replace = ''
            # End inline tags out to the furthest <code> not contained
            # in another <uncode>, and restart them, except <code>,
            # for contained content.
            last_uncode = 0
            for i in range(len(self.open_tags)):
                if self.open_tags[i] == 'uncode':
                    last_uncode = i
            first_code = 0
            for i in range(last_uncode, len(self.open_tags)):
                if self.open_tags[i] == 'code':
                    first_code = i
                    break
            if first_code > last_uncode:
                close_tags = self.open_tags[first_code:]
                reopen_tags = [t for t in close_tags if t != 'code']
                for t in reopen_tags:
                    if t in ('a', 'sup', 'sub'):
                        raise ValueError('<uncode> in <%s> in %s'
                                         % (t, self.doc))
        for t in reversed(close_tags):
            self.handle_end_tag(t)
        super().handle_start_tag(tag_name, tag_attrs, tag_replace)
        self.wrap_text_in[-1] = reopen_tags
        self.end_wrap[-1] = close_tags


def clean_font(doc, text):
    """Clean up use of font-related CSS styles on tags."""
    text = ReplaceFont(doc, text).run()
    return ReplaceUncode(doc, text).run()


# CSS length units in points.
CSS_LENGTHS = {'in': 72, 'cm': 72 / 2.54, 'px': 0.75, 'pt': 1}


def css_len(number, unit):
    """Calculate a CSS length in points."""
    return float(number) * CSS_LENGTHS[unit]


def clean_margin_left(doc, text):
    """Clean up use of margin-left CSS styles on tags."""
    if doc not in ('n2396.htm', 'n2397.htm'):
        return text
    if doc == 'n2396.htm':
        # This is the only <div> tag.
        text = text.replace('<div style="margin-left:40px">', '<blockquote>')
        text = text.replace('</div>', '</blockquote>')
    text = text.replace('<p style="margin-left:0in">', '<p>')
    rtext = text
    new_text_list = []
    while rtext:
        # Look for a sequence of consecutive paragraphs with
        # margin-left styles, and replace those styles with
        # appropriate numbers of <blockquote>.
        m = re.search(
            '<p style="margin-left:([0-9.]+)(in|cm|px|pt)">(.*?)</p>',
            rtext, flags=re.DOTALL)
        if not m:
            break
        cur_paras = []
        new_text_list.append(rtext[:m.start(0)])
        while m:
            cur_paras.append((css_len(m.group(1), m.group(2)), m.group(3)))
            rtext = rtext[m.end(0):]
            m = re.search(
                '<p style="margin-left:([0-9.]+)(in|cm|px|pt)">(.*?)</p>',
                rtext, flags=re.DOTALL)
            if m and rtext[:m.start(0)].strip():
                # The next paragraph found is in a separate sequence
                # of consecutive paragraphs with margin-left
                # specified.
                break
        indents = {}
        for i, clen in enumerate(sorted({x[0] for x in cur_paras}), start=1):
            indents[clen] = i
        for clen, content in cur_paras:
            indent = indents[clen]
            new_text_list.append('%s<p>%s</p>%s\n'
                                 % ('<blockquote>' * indent,
                                    content,
                                    '</blockquote>' * indent))
    new_text_list.append(rtext)
    return ''.join(new_text_list)


class RemoveRedundantTags(ProcessNesting):

    """Remove tags that are redundant based on their context."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        tag_replace = None
        # The remaining <center> are around headers and give no
        # information useful for the conversion.  <span> with no
        # attributes is useless, and code style tags inside the same
        # tag are useless, as is <code> inside <pre>.  <b> inside
        # <code> or <pre> is a stylistic choice for formatting C code,
        # used inconsistently in some of the input files; rather than
        # representing it in issue tracker data, it's better for any
        # such styling to be done at the point where issue tracker
        # data is presented to the user (converted back to HTML for
        # display).  <a name> is only ever linked to when it's a link
        # to a question within an issue, and those links are
        # reprocessed, so the <a name> are redundant.
        if tag_name == 'center':
            tag_replace = ''
        elif tag_name == 'span' and not tag_attrs:
            tag_replace = ''
        elif tag_name == 'a':
            href = None
            for attr, value in tag_attrs:
                if attr == 'href':
                    href = value
            if href is None:
                tag_replace = ''
                tag_attrs = []
            elif len(tag_attrs) > 1 and href.startswith('"issue:'):
                # An issue link with title specified.  Remove that
                # title as redundant with the actual metadata for the
                # issue linked to (titles on links to issues should be
                # inserted at display time, not stored in the data
                # with the link itself).
                tag_attrs = [('href', href)]
        elif tag_name in ('code', 'b', 'i', 'del', 'u'):
            if tag_name in self.open_tags:
                tag_replace = ''
            elif tag_name in ('b', 'code') and 'pre' in self.open_tags:
                tag_replace = ''
            elif tag_name == 'b' and 'code' in self.open_tags:
                tag_replace = ''
        super().handle_start_tag(tag_name, tag_attrs, tag_replace)


def clean_redundant_tags(doc, text):
    """Remove tags that are redundant based on their context."""
    rtext = RemoveRedundantTags(doc, text).run()
    # Now remove <b> around <code>, if <code> is the only
    # non-whitespace content inside that <b>.
    new_text_list = []
    while rtext:
        m = re.search('<b>(.*?)</b>', rtext, flags=re.DOTALL)
        if not m:
            break
        new_text_list.append(rtext[:m.start(0)])
        bcontent = m.group(0)
        content = m.group(1)
        rtext = rtext[m.end(0):]
        rcontent = re.sub('<code>.*?</code>', '', content, flags=re.DOTALL)
        if re.fullmatch(r'(<[^!>][^>]*>|\s|&nbsp;)*', rcontent):
            # No non-whitespace non-tag non-code content; remove <b>.
            new_text_list.append(content)
        else:
            # Preserve <b>.
            new_text_list.append(bcontent)
    new_text_list.append(rtext)
    return ''.join(new_text_list)


def replace_empty(text, tag, replacement):
    """Replace instances of the given tag that are empty (apart from
    whitespace and other tags) by the replacement text.  All instances of
    the tag to be replaced must be properly closed, and not have any
    attributes."""
    start_tag = '<%s>' % tag
    tag_re = '<%s>(.*?)</%s>' % (tag, tag)
    rtext = text
    new_text_list = []
    while rtext:
        m = re.search(tag_re, rtext, flags=re.DOTALL)
        if not m:
            break
        if start_tag in m.group(1):
            # Nested copies of the tag; the end tag found does not
            # match the opening tag found.
            new_text_list.append(rtext[:m.start(1)])
            rtext = rtext[m.start(1):]
            continue
        if re.fullmatch(r'(<[^!>][^>]*>|\s|&nbsp;)*', m.group(1)):
            # Tag contains only whitespace and other tags.
            new_text_list.append(rtext[:m.start(0)])
            new_text_list.append(replacement)
            rtext = rtext[m.end(0):]
        else:
            mc = re.fullmatch(
                r'(?:<[^!>][^>]*>|\s|&nbsp;)*'
                r'(<!--[^>]*-->)'
                r'(?:<[^!>][^>]*>|\s|&nbsp;)*', m.group(1))
            if mc:
                # Tag contains a comment but no other content to preserve.
                new_text_list.append(rtext[:m.start(0)])
                new_text_list.append(mc.group(1))
                new_text_list.append(replacement)
                rtext = rtext[m.end(0):]
            else:
                # Tag contains other content, so cannot be removed.
                new_text_list.append(rtext[:m.end(0)])
                rtext = rtext[m.end(0):]
    new_text_list.append(rtext)
    return ''.join(new_text_list)


class FixParagraphs(ProcessNesting):

    """Insert missing <p> and </p> tags."""

    def handle_before_tag(self, before):
        """Handle the text coming before a tag."""
        # Insert explicit paragraphs in certain contexts.
        if (before.strip()
            and self.open_tags
            and self.open_tags[-1] in ('body', 'blockquote', 'div')):
            self.handle_start_tag('p', [])
        super().handle_before_tag(before)

    def maybe_close_p(self, tag_name, end_tag):
        """Close an unterminated <p> when any non-inline tag starts or ends."""
        if (self.open_tags
            and self.open_tags[-1] == 'p'
            and not (end_tag and tag_name == 'p')
            and tag_name not in KNOWN_TAGS_INLINE):
            self.handle_end_tag('p')

    def maybe_insert_p_for_tag(self, tag_name):
        """Insert explicit paragraphs for inline tags in certain contexts."""
        if (tag_name in KNOWN_TAGS_INLINE
            and self.open_tags
            and self.open_tags[-1] in ('body', 'blockquote', 'div')):
            self.handle_start_tag('p', [])

    def handle_empty_tag(self, tag_name, end_tag, tag_attrs):
        """Handle an empty tag."""
        self.maybe_close_p(tag_name, end_tag)
        self.maybe_insert_p_for_tag(tag_name)
        super().handle_empty_tag(tag_name, end_tag, tag_attrs)

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        self.maybe_close_p(tag_name, False)
        self.maybe_insert_p_for_tag(tag_name)
        super().handle_start_tag(tag_name, tag_attrs)

    def handle_end_tag(self, tag_name):
        """Handle an end tag."""
        self.maybe_close_p(tag_name, True)
        super().handle_end_tag(tag_name)


def clean_general(doc, text, multiline_code_converted=False,
                  combine_code=True):
    """Apply various general local cleanups.  If multiline_code_converted
    is False (the default), some whitespace-related cleanups are not
    applied to <code> in some places because whitespace may be
    significant there until multiline <code> has been turned into
    <pre>.  If combine_code is False, adjacent <code> are not combined;
    this is for when <pre> needs to be split into <code> for each line because
    of <u> contained therein."""
    clean_code_whitespace = multiline_code_converted or not is_c90_dr(doc)
    # Applying some of these cleanups may open opportunities for
    # applying further instances of the same or another cleanup, so
    # this function iterates until no more changes are made.
    orig_text = text
    # Remove empty paragraphs, <pre> and <blockquote>.  Because there
    # are contexts (such as in <li>) where we allow text not in a
    # paragraph, an empty paragraph, <pre> or <blockquote> might serve
    # as a separator between two pieces of inline text in such a
    # context.  Thus we do this cleanup in multiple stages: first
    # replace the empty paragraph, <pre> or <blockquote> by a <p>
    # opening tag, then insert missing </p> tags, then remove any
    # empty paragraphs left afterwards.
    text = replace_empty(text, 'p', '<p>')
    text = replace_empty(text, 'blockquote', '<p>')
    text = replace_empty(text, 'pre', '<p>')
    text = FixParagraphs(doc, text).run()
    text = replace_empty(text, 'p', '')
    # Combine adjacent blockquotes.
    text = re.sub(r'</blockquote>\s*<blockquote>', '', text)
    # Combine adjacent copies of the same inline tag (preserving
    # whitespace between those copies).
    for tag in ('b', 'code', 'i', 'u', 'del'):
        if tag == 'code' and not combine_code:
            continue
        text = re.sub(r'</%s>((?:\s|<br>|&nbsp;)*)<%s>' % (tag, tag), r'\1',
                      text)
    # Migrate whitespace at the start or end of an inline tag outside
    # that tag.
    ws_clean_tags = ['b', 'i', 'u', 'del']
    if clean_code_whitespace:
        ws_clean_tags.append('code')
    ws_clean_tags_a = ws_clean_tags + ['a']
    for tag in ws_clean_tags:
        if tag == 'code' and not multiline_code_converted:
            # Do not move &nbsp; out of the start of <code> yet; it
            # may be significant here even outside C90 DRs.
            text = re.sub(r'<code>((?:\s|<br>)+)', r'\1<code>', text)
            pass
        else:
            text = re.sub(r'<%s>((?:\s|<br>|&nbsp;)+)' % tag, r'\1<%s>' % tag,
                          text)
    text = re.sub(r'<a ([^>]*)>((?:\s|<br>|&nbsp;)+)', r'\2<a \1>',
                  text)
    for tag in ws_clean_tags_a:
        text = re.sub(r'((?:\s|<br>|&nbsp;)+)</%s>' % tag, r'</%s>\1' % tag,
                      text)
    # Remove empty inline tags.
    for tag in ('b', 'code', 'i', 'u', 'del'):
        text = text.replace('<%s></%s>' % (tag, tag), '')
    # Remove <br> at the start of paragraphs, and <br> and &nbsp; at
    # the end of paragraphs.  (We don't remove plain whitespace at
    # this point if not mixed with <br> or &nbsp;.)
    text = re.sub(r'<p>\s*<br>(\s|<br>)*', '<p>', text)
    text = re.sub(r'\s*(<br>|&nbsp;)(\s|<br>|&nbsp;)*</p>', '</p>', text)
    if text == orig_text:
        return text
    else:
        return clean_general(doc, text, multiline_code_converted,
                             combine_code)


class MoveCodeOut(ProcessNesting):

    """Where <code> appears inside inline style tags, move those tags
    inside <code>.  This enables conversion of multi-line <code> to <pre>,
    although it is the opposite direction to what is representable in
    Markdown (where <code> can be inside but not outside such tags)."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        wrap_num = 0
        if tag_name == 'code':
            for outer_tag in reversed(self.open_tags):
                if outer_tag in ('b', 'i', 'del', 'u'):
                    wrap_num += 1
                else:
                    break
        if wrap_num:
            wrap_tags = self.open_tags[-wrap_num:]
            for t in reversed(wrap_tags):
                self.handle_end_tag(t)
        super().handle_start_tag(tag_name, tag_attrs)
        if wrap_num:
            self.wrap_text_in[-1] = wrap_tags
            self.end_wrap[-1] = wrap_tags


class MoveCodeIn(ProcessNesting):

    """Where inline tags (<style>, <sub> or <sup>) appear inside <code>,
    move <code> inside those tags."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        wrap_num = 0
        if (tag_name in ('a', 'b', 'i', 'del', 'u', 'sub', 'sup')
            and self.open_tags[-1] == 'code'):
            wrap_num = 1
        if wrap_num:
            wrap_tags = self.open_tags[-wrap_num:]
            for t in reversed(wrap_tags):
                self.handle_end_tag(t)
        super().handle_start_tag(tag_name, tag_attrs)
        if wrap_num:
            self.wrap_text_in[-1] = wrap_tags
            self.end_wrap[-1] = wrap_tags


class MoveBrOutsideCode(ProcessNesting):

    """Move <br> outside <code> (for cases where <pre> can't be used)."""

    def handle_empty_tag(self, tag_name, end_tag, tag_attrs):
        """Handle an empty tag."""
        if tag_name != 'br':
            super().handle_empty_tag(tag_name, end_tag, tag_attrs)
            return
        num_inlines = 0
        seen_code = False
        for outer_tag in reversed(self.open_tags):
            if outer_tag in ('b', 'code', 'i', 'del', 'u'):
                num_inlines += 1
                if outer_tag == 'code':
                    seen_code = True
                    break
            else:
                break
        if seen_code:
            inline_tags = self.open_tags[-num_inlines:]
            for t in reversed(inline_tags):
                self.handle_end_tag(t)
        super().handle_empty_tag(tag_name, end_tag, tag_attrs)
        if seen_code:
            for t in inline_tags:
                self.handle_start_tag(t, [])


def code_to_pre(text, is_c90):
    """Convert <code> contents to a <pre> element."""
    if is_c90:
        # Treat whitespace as significant; it appears to be intended
        # to be (possibly as a result of original conversion from a
        # non-HTML format).
        text = text.replace('\n', ' ')
        text = text.replace('<br>', '\n')
    else:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'<br>\s*', '\n', text)
    return '<pre>%s</pre>' % text


def clean_code_to_pre(doc, text):
    """Convert multi-line or whole-line <code> to <pre>."""
    is_c90 = is_c90_dr(doc)
    text = MoveCodeOut(doc, text).run()
    text = clean_general(doc, text, False)
    rtext = text
    new_text_list = []
    while rtext:
        m = re.search('<code>(.*?)</code>', rtext, flags=re.DOTALL)
        if not m:
            break
        code_content = m.group(1)
        break_in = '<br>' in m.group(1)
        break_after = bool(re.match(r'(\s|&nbsp;)*(<br>|</p>|</li>)',
                                    rtext[m.end(0):]))
        li_after = bool(re.match(r'(\s|&nbsp;)*(</li>)', rtext[m.end(0):]))
        mb = re.search(r'(?:<br>|<p>|</p>|<li>)((?:\s|&nbsp;)*)\Z',
                       rtext[:m.start(0)])
        break_before = bool(mb)
        li_before = bool(re.search(r'(?:<li>)((?:\s|&nbsp;)*)\Z',
                                   rtext[:m.start(0)]))
        if break_before:
            code_content = mb.group(1).lstrip() + code_content
        if break_before and break_in and not break_after:
            mc = re.search(r'<br>(\s|&nbsp;)*\Z', code_content)
            if mc:
                break_after = True
                if '<br>' not in code_content[:mc.start(0)]:
                    break_in = False
        if (break_before
            and break_after
            and not (li_before and li_after and not break_in)):
            new_text_list.append(rtext[:mb.start(1)])
            new_text_list.append(code_to_pre(code_content, is_c90))
            new_text_list.append('<p>')
        else:
            new_text_list.append(rtext[:m.end(0)])
        rtext = rtext[m.end(0):]
    new_text_list.append(rtext)
    text = ''.join(new_text_list)
    text = FixParagraphs(doc, text).run()
    text = MoveCodeIn(doc, text).run()
    return clean_general(doc, text, True)


def clean_pre(doc, text, insert_blank_line=True, to_code_for_u=False):
    """Clean up <pre> contents and combine consecutive <pre> blocks.  If
    insert_blank_line is True (the default), a blank line is inserted
    between such blocks being combined unless the first ends with a
    backslash.  If to_code_for_u is True, convert such a block to <code>
    if it contains <u> tags, to avoid those tags being lost in Markdown."""
    rtext = text
    new_text_list = []
    while rtext:
        m = re.search('<pre>(.*?)</pre>', rtext, flags=re.DOTALL)
        if not m:
            break
        new_text_list.append(rtext[:m.start(0)])
        pre_content = m.group(1)
        rtext = rtext[m.end(0):]
        pre_content = pre_content.replace('<br>', '\n')
        pre_content = pre_content.replace('&nbsp;', ' ')
        pre_content = pre_content.rstrip()
        pre_content = re.sub(r'^\s*\n', '', pre_content)
        pre_lines = []
        have_u = False
        for line in pre_content.split('\n'):
            line = line.rstrip()
            if '<u>' in line:
                have_u = True
            line_chars = []
            num_cols = 0
            while line:
                m = re.match('(.*?)[<\t]', line)
                if not m:
                    break
                line_chars.append(m.group(1))
                num_cols += len(m.group(1))
                line = line[m.end(1):]
                if line.startswith('\t'):
                    line_chars.append(' ' * (8 - num_cols % 8))
                    line = line[1:]
                    num_cols = 0
                else:
                    m = re.match('<[^>]*>', line)
                    line_chars.append(m.group(0))
                    line = line[m.end(0):]
            line_chars.append(line)
            pre_lines.append(''.join(line_chars))
        if to_code_for_u and have_u:
            # At this point, there are no <a href> or other cases
            # where replacing a space would be inappropriate.
            code_lines = [line.replace(' ', '&nbsp;') for line in pre_lines]
            code_lines = ['&nbsp;' if line == '' else line
                          for line in code_lines]
            new_text_list.append('<p><code>%s</code></p>'
                                 % '<br>\n'.join(code_lines))
        else:
            new_text_list.append('<pre>%s</pre>' % '\n'.join(pre_lines))
    new_text_list.append(rtext)
    text = ''.join(new_text_list)
    text = re.sub(r'\\</pre>\s*<pre>', r'\\' '\n', text)
    if insert_blank_line:
        text = re.sub(r'</pre>\s*<pre>', '\n\n', text)
    else:
        text = re.sub(r'</pre>\s*<pre>', '\n', text)
    return text


class BrToP(ProcessNesting):

    """Convert all <br> to paragraph breaks.  This is for C90 DRs that
    rarely use <p> at all but generally use <br> to indicate a paragraph
    break instead.  Uses inside code blocks have already been converted to
    <pre>."""

    def handle_empty_tag(self, tag_name, end_tag, tag_attrs):
        """Handle an empty tag."""
        if tag_name != 'br':
            super().handle_empty_tag(tag_name, end_tag, tag_attrs)
            return
        num_inlines = 0
        for outer_tag in reversed(self.open_tags):
            if outer_tag in ('b', 'code', 'i', 'del', 'u'):
                num_inlines += 1
            elif outer_tag in KNOWN_TAGS_INLINE:
                raise ValueError('<br> inside <%s> cannot be converted to <p>'
                                 % outer_tag)
            else:
                break
        if num_inlines:
            inline_tags = self.open_tags[-num_inlines:]
            for t in reversed(inline_tags):
                self.handle_end_tag(t)
        self.handle_start_tag_internal('p', [])
        super().handle_empty_tag(tag_name, end_tag, tag_attrs)
        if num_inlines:
            for t in inline_tags:
                self.handle_start_tag(t, [])


def clean_br(doc, text):
    """In C90 DRs, convert remaining <br> to paragraph breaks."""
    if not is_c90_dr(doc):
        return text
    text = BrToP(doc, text).run()
    text = FixParagraphs(doc, text).run()
    # The conversion to paragraph breaks may have opened up more
    # opportunities to turn <p><code>...</code></p> into a use of
    # <pre>, and then to combine such <pre>.
    text = clean_code_to_pre(doc, text)
    return clean_pre(doc, text, False)


def clean_quotes(doc, text):
    """Convert LaTeX-style quotes to Unicode quotes."""
    text = text.replace('``', '&ldquo;')
    # '' is used in a few places as an opening quote, otherwise as a
    # closing quote.
    text = text.replace(" ''", ' &ldquo;')
    text = text.replace("''", '&rdquo;')
    return text


class CleanBlockquote(ProcessNesting):

    """Fix redundantly nested <blockquote>."""

    def __init__(self, doc, text):
        super().__init__(doc, text)
        self.open_tag_pos = []

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        super().handle_start_tag(tag_name, tag_attrs)
        self.open_tag_pos.append(len(self.new_text_list) - 1)

    def handle_end_tag(self, tag_name):
        """Handle an end tag."""
        if (tag_name == 'blockquote'
            and self.open_tags[-1] == 'blockquote'
            and self.open_tags[-2] == 'blockquote'
            and self.open_tag_pos[-2] == self.open_tag_pos[-1] - 2
            and not self.new_text_list[self.open_tag_pos[-1] - 1].strip()
            and self.rtext.lstrip().startswith('</blockquote>')):
            self.new_text_list[self.open_tag_pos[-1]] = ''
            self.pop_tag()
        else:
            super().handle_end_tag(tag_name)
        self.open_tag_pos = self.open_tag_pos[:-1]


def clean_blockquote(doc, text):
    """Fix redundantly nested <blockquote>."""
    old_text = text
    text = CleanBlockquote(doc, text).run()
    if old_text == text:
        return text
    else:
        return clean_blockquote(doc, text)


class OLLetterToP(ProcessNesting):

    """Replace <ol type="a"> and <ol type="A"> with plain paragraphs."""

    def __init__(self, doc, text):
        super().__init__(doc, text)
        self.ol_values = []

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        replace_tag = None
        ol_type = None
        ol_start = None
        existing_li_p = False
        if tag_name == 'ol' and tag_attrs:
            for attr_name, value in tag_attrs:
                if attr_name == 'type':
                    ol_type = value[1:-1]
                if attr_name == 'start':
                    ol_start = value[1:-1]
            if ol_type == '1':
                ol_type = None
            if ol_type is not None and ol_start is not None:
                raise ValueError('<ol> with both type and start in %s'
                                 % self.doc)
            if ol_type is not None:
                replace_tag = ''
                if ol_type not in ('a', 'A'):
                    raise ValueError('unknown <ol> type %s in %s'
                                     % (ol_type, self.doc))
        if (tag_name == 'li'
            and self.ol_values
            and self.ol_values[-1] is not None):
            replace_tag = ''
            self.new_text_list.append('<p>%s. ' % self.ol_values[-1])
            self.ol_values[-1] = chr(ord(self.ol_values[-1]) + 1)
            self.rtext = self.rtext.lstrip()
            if self.rtext.startswith('<p>'):
                self.rtext = self.rtext[len('<p>'):]
                existing_li_p = True
        super().handle_start_tag(tag_name, tag_attrs, replace_tag)
        self.ol_values.append(ol_type)
        if existing_li_p:
            self.push_tag('p')
            self.ol_values.append(None)

    def handle_end_tag(self, tag_name):
        """Handle an end tag."""
        super().handle_end_tag(tag_name)
        self.ol_values = self.ol_values[:-1]


class CheckPreInline(ProcessNesting):

    """Check for inline markup inside preformatted text."""

    def handle_start_tag(self, tag_name, tag_attrs):
        """Handle a start tag."""
        if tag_name in ('a', 'sub', 'sup', 'i', 'del', 'u', 'b'):
            if 'pre' in self.open_tags:
                if tag_name in ('b', 'i'):
                    # Ignore bold and italics inside <pre> (will be
                    # lost in Markdown conversion, but that's fairly
                    # harmless).  Most bold was already removed, but
                    # some remains in conjunction with italics.
                    pass
                else:
                    print('%s has <%s> inside <pre>' % (self.doc, tag_name))
            if 'code' in self.open_tags:
                # These should all have been fixed earlier.
                raise ValueError(
                    '%s has <%s> inside <code>' % (self.doc, tag_name))
        super().handle_start_tag(tag_name, tag_attrs)


def clean_for_md(doc, text):
    """Rewrite HTML constructs not represented in Markdown."""
    # Markdown does not have equivalents to <dl> <dt> <dd>.  Represent
    # <dt> as a paragraph and <dd> as a blockquote, with the whole
    # list inside a blockquote.
    text = text.replace('<dt>', '<p>')
    text = text.replace('</dt>', '</p>')
    text = text.replace('<dd>', '<blockquote>')
    text = text.replace('</dd>', '</blockquote>')
    text = text.replace('<dl>', '<blockquote>')
    text = text.replace('</dl>', '</blockquote>')
    text = FixParagraphs(doc, text).run()
    text = re.sub(r'</blockquote>\s*<blockquote>', '', text)
    text = clean_blockquote(doc, text)
    # Markdown does not have equivalents to <ol type="a"> and <ol
    # type="A">.  Represent those using hardcoded letters at the start
    # of paragraphs.
    text = OLLetterToP(doc, text).run()
    text = FixParagraphs(doc, text).run()
    # Convert <pre> containing <u> to <code>, then check for
    # unsupported markup inside <pre>.
    text = clean_pre(doc, text, False, True)
    text = MoveCodeIn(doc, text).run()
    text = MoveBrOutsideCode(doc, text).run()
    text = clean_general(doc, text, True, False)
    CheckPreInline(doc, text).run()
    return text


# List of functions for cleaning HTML issue lists.
CLEAN_FUNCS_LIST = (
    clean_amp, clean_ltgt, clean_chars, clean_per_file, clean_tags,
    clean_nesting, clean_class, clean_color, clean_font, clean_margin_left,
    clean_redundant_tags, clean_general, clean_code_to_pre, clean_pre,
    clean_br, clean_quotes, clean_blockquote, clean_for_md)


def clean_doc(doc):
    """Pass an HTML input document through a series of cleaning steps,
    returning the cleaned document, and writing out the output of each
    step."""
    encoding = 'cp1252' if doc == CSCR_ALL else 'utf-8'
    # To handle \r\r\n as well as \r, \n and \r\n as a line ending, we
    # handle newline translation outselves.
    with open(input_filename(doc), 'r', encoding=encoding, newline='') as f:
        text = f.read()
    text = text.replace('\r\r\n', '\r\n')
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    for n, clean_func in enumerate(CLEAN_FUNCS_LIST):
        text = clean_func(doc, text).strip() + '\n'
        out_dir = 'tmp/clean-%02d' % n
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, doc), 'w', encoding='utf-8') as f:
            f.write(text)
    return text


# Months for parsing C90 DR list.
MONTHS = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
          'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
          'Nov': '11', 'Dec': '12'}


def clean_for_metadata(text):
    """Clean some HTML text to go in JSON metadata."""
    return re.sub(r'(\s|&nbsp;)+', ' ', text).strip()


# C90 issues fixed in C90 itself.
C90_FIXED_IN_C90 = {'0004'}


# C90 issues fixed in C90 TC1.  Includes duplicates of issues that
# give the actual TC: 0017.12, 0017.15, 0017.26, 0017.29, 0034.01,
# 0040.01, 0100, 0105.
C90_FIXED_IN_TC1 = {
    '0001', '0009', '0011.01', '0011.02', '0011.04', '0013.01', '0013.04',
    '0013.05', '0014.02', '0016.02', '0017.01', '0017.02', '0017.03',
    '0017.06', '0017.09', '0017.12', '0017.14', '0017.15', '0017.16',
    '0017.17', '0017.19', '0017.22', '0017.24', '0017.26', '0017.29',
    '0017.30', '0017.37', '0017.38', '0017.39', '0021', '0022', '0027',
    '0034.01', '0040.01', '0040.02', '0043.01', '0052.01', '0052.02', '0053',
    '0054', '0055', '0100', '0105'}


# C90 issues fixed in C90 TC2.
C90_FIXED_IN_TC2 = {
    '0060', '0065', '0071', '0080', '0082', '0083', '0085', '0089', '0093',
    '0101', '0118', '0124', '0131', '0138', '0139'}


# C90 issues fixed (apparently as defects rather than new features) in
# C99.  Includes cases where the C90 issue did not provide specific
# wording or where the C99 wording was significantly different but
# still appears intended to address the issue.
C90_FIXED_IN_C99 = {
    '0142', '0143', '0144', '0145', '0146', '0147', '0149', '0150', '0155',
    '0156', '0157', '0158', '0159', '0160', '0162', '0165', '0166', '0167',
    '0168', '0170', '0171', '0172', '0174', '0175', '0177'}


def extract_c90_issues(docs_content, issues_data):
    """Extract C90 issue data from the source documents."""
    dr_index = docs_content[C90_INDEX]
    last_dr = 0
    c90_issues = set()
    while True:
        m = re.search(
            r'<a href="issue:(0[0-1][0-9][0-9])">'
            r'Defect Report Number ([0-1][0-9][0-9])</a>\s+'
            r'([0-3][0-9]) ([A-Z][a-z][a-z]) (9[2-6])\s+'
            r'([A-Z][^\n<]*\S)\s*<br>\s*(.*?)(?:</p>|<br> *\n?<a href="issue)',
            dr_index, flags=re.DOTALL)
        if not m:
            if last_dr != C90_LAST:
                raise ValueError('found C90 DRs up to %d' % last_dr)
            break
        dr_num_1 = m.group(1)
        dr_num_2 = m.group(2)
        day = m.group(3)
        month = m.group(4)
        year = m.group(5)
        author = m.group(6)
        date = '19%s-%s-%s' % (year, MONTHS[month], day)
        summaries = m.group(7)
        dr_index = dr_index[m.end(7):]
        last_dr += 1
        if dr_num_1 != '0' + dr_num_2 or dr_num_1 != '%04d' % last_dr:
            raise ValueError('inconsistent DR numbers %d %s %s'
                             % (last_dr, dr_num_1, dr_num_2))
        last_q = 0
        summaries = summaries.strip() + '<br>'
        summaries_list = []
        while True:
            m = re.search('<br>', summaries)
            if not m:
                break
            next_summary = summaries[:m.start(0)].strip()
            summaries = summaries[m.end(0):]
            m = re.fullmatch(r'Q([1-9][0-9]*):\s*(.*)', next_summary,
                             flags=re.DOTALL)
            if not m:
                raise ValueError('issue %d: failed to parse summary %s'
                                 % (last_dr, next_summary))
            last_q += 1
            if m.group(1) != str(last_q):
                raise ValueError(
                    'issue %d: inconsistent question numbers %d %s'
                    % (last_dr, last_q, m.group(1)))
            this_q_summary = clean_for_metadata(m.group(2))
            summaries_list.append(this_q_summary)
        for qnum, summary in enumerate(summaries_list, start=1):
            if qnum == 1 and len(summaries_list) == 1:
                full_issue_num = '%04d' % last_dr
            else:
                full_issue_num = '%04d.%02d' % (last_dr, qnum)
            if full_issue_num in issues_data:
                raise ValueError('issue %s already seen' % full_issue_num)
            summary_orig = summary
            summary = re.sub(' See .*', '', summary).rstrip('.')
            issues_data[full_issue_num] = {
                'date': date,
                'author-html': author,
                'x-summary-author-html': author,
                'submitted-against': 'c90',
                'summary-html': summary,
                'x-orig-summary-html': summary_orig,
                'status': 'unknown',
                'conversion-src': [C90_INDEX],
                'crossref': []}
            fix_vers = None
            if full_issue_num in C90_FIXED_IN_C90:
                fix_vers = 'c90'
            elif full_issue_num in C90_FIXED_IN_TC1:
                fix_vers = 'c90tc1'
            elif full_issue_num in C90_FIXED_IN_TC2:
                fix_vers = 'c90tc2'
            elif full_issue_num in C90_FIXED_IN_C99:
                fix_vers = 'c99'
            if fix_vers is None:
                issues_data[full_issue_num]['status'] = 'closed'
            else:
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = [fix_vers]
            c90_issues.add(full_issue_num)
    for dr_num in range(C90_FIRST, C90_LAST + 1):
        dr_doc = 'dr_%03d.html' % dr_num
        dr_body = docs_content[dr_doc]
        m = re.fullmatch(
            r'<html>\s*<head><title>Defect\s+Report\s+#%03d</title></head>\s*'
            r'<body>\s*<h2>Defect\s+Report\s+#%03d\s*</h2>\s*'
            r'<p><b>Submission Date</b>: '
            r'([0-3][0-9]) ([A-Z][a-z][a-z]) (9[2-6])\s*</p>\s*'
            r'<p><b>Submittor</b>:\s*([^<]*\S)\s*</p>\s*'
            r'<p><b>Source</b>:\s*([^<]*\S)\s*</p>\s*'
            r'(.*)<p>\s*'
            r'(?:<a href="issue:....">Previous Defect Report</a>\s*)?'
            r'(?:(?:&lt;)?\s+-\s+(?:&gt;)?\s*)?'
            r'(?:<a href="issue:....">Next Defect Report</a>\s*)?'
            r'</p>\s*</body></html>\n'
            % (dr_num, dr_num), dr_body, flags=re.DOTALL)
        if not m:
            raise ValueError('failed to match issue %d body' % dr_num)
        day = m.group(1)
        month = m.group(2)
        year = m.group(3)
        submitter = m.group(4)
        source = m.group(5)
        content = m.group(6).strip()
        date = '19%s-%s-%s' % (year, MONTHS[month], day)
        m = re.fullmatch(r'(X3J11/\S*)\s+\((.*)\)', source)
        if m:
            refdoc = m.group(1)
            author = m.group(2)
        else:
            author = source
            refdoc = None
        last_q = 0
        while content:
            if dr_num >= 60:
                m = re.match(
                    r'<p>\s*<b>Question</b>\s*</p>\s*',
                    content)
            else:
                m = re.match(
                    r'<p>\s*<b>Question</b>\s*([1-9][0-9]*)\s*</p>\s*',
                    content)
            if not m:
                raise ValueError('failed to match issue %d Q %d'
                                 % (dr_num, last_q + 1))
            last_q += 1
            if dr_num < 60 and m.group(1) != str(last_q):
                raise ValueError(
                    'issue %d (body): inconsistent question numbers %d %s'
                    % (dr_num, last_q, m.group(1)))
            content = content[m.end(0):]
            if dr_num >= 60:
                this_content = content.strip()
                content = ''
            else:
                m = re.search(
                    r'<p>\s*<b>Question</b>\s*([1-9][0-9]*)\s*</p>\s*',
                    content)
                if m:
                    this_content = content[:m.start(0)].strip()
                    content = content[m.start(0):]
                else:
                    this_content = content.strip()
                    content = ''
            full_issue_num = '%04d' % dr_num
            if last_q != 1 or full_issue_num not in issues_data:
                full_issue_num = '%s.%02d' % (full_issue_num, last_q)
            if full_issue_num not in issues_data:
                raise ValueError('issue %s in content but not summary'
                                 % full_issue_num)
            if 'content-html' in issues_data[full_issue_num]:
                raise ValueError('issue %s already processed'
                                 % full_issue_num)
            m = re.search(
                r'<p>\s*(?:<b>)?(?:Correction|Response|Open Issue'
                r'|Technical Corrigendum|Suggested Future Change'
                r'|Future Change|Proposed Response)(?:</b>)?\s*</p>',
                this_content)
            if m:
                comment = ('<html><body>%s</body></html>'
                           % this_content[m.start(0):])
                this_content = this_content[:m.start(0)]
                # C90 defect reports do not come with dates for their
                # responses; use 1997-09-23 as the most recent
                # timestamp in defect_reports.tar.gz (a downloadable
                # version of the full set that is or was available on
                # the WG14 website).
                comments = [{'date': '1997-09-23',
                             'filename': '1.html',
                             'author-html': 'WG14',
                             'content-html': comment}]
            else:
                comments = []
            issues_data[full_issue_num]['content-html'] = (
                '<html><body>%s</body></html>' % this_content)
            issues_data[full_issue_num]['comments'] = comments
            issues_data[full_issue_num]['submitter-html'] = submitter
            if date != issues_data[full_issue_num]['date']:
                raise ValueError('%s: date %s -> %s'
                                 % (full_issue_num,
                                    issues_data[full_issue_num]['date'],
                                    date))
            if author != issues_data[full_issue_num]['author-html']:
                if ((issues_data[full_issue_num]['author-html'], author)
                    not in (('Ron Gulmette', 'Ron Guilmette'),
                            ('P. J. Plauger', 'Project Editor (P.J. Plauger)'),
                            ('Clive Feather', 'Clive D.W. Feather'))):
                    raise ValueError(
                        '%s: author %s -> %s'
                        % (full_issue_num,
                           issues_data[full_issue_num]['author-html'],
                           author))
            issues_data[full_issue_num]['author-html'] = author
            issues_data[full_issue_num]['conversion-src'].append(dr_doc)
            if refdoc is not None:
                issues_data[full_issue_num]['reference-doc-html'] = refdoc
    for issue in sorted(c90_issues):
        if 'content-html' not in issues_data[issue]:
            raise ValueError('content of issue %s not found' % issue)


def extract_c99_issues(docs_content, issues_data):
    """Extract C99 issue data from the source documents."""
    dr_index = docs_content[C99_INDEX]
    last_dr = 200
    while True:
        m = re.search(
            r'<p><a href="issue:(0[2-3][0-9][0-9])">'
            r'Defect Report #([2-3][0-9][0-9])</a>\s+'
            r'(\S.*?\S)\s*&nbsp;&ndash;&nbsp;'
            r'<span class="(closed|published|review)">([^<]*)</span><br>'
            r'\s*(Q.*?\S)\s*</p>',
            dr_index, flags=re.DOTALL)
        if not m:
            if last_dr != C99_LAST:
                raise ValueError('found C99 DRs up to %d' % last_dr)
            break
        dr_num_1 = m.group(1)
        dr_num_2 = m.group(2)
        date_and_author = clean_for_metadata(m.group(3))
        status_class = m.group(4)
        status_text = clean_for_metadata(m.group(5))
        summary = clean_for_metadata(m.group(6))
        dr_index = dr_index[m.end(0):]
        last_dr += 1
        if dr_num_1 != '0' + dr_num_2 or dr_num_1 != '%04d' % last_dr:
            raise ValueError('inconsistent DR numbers %d %s %s'
                             % (last_dr, dr_num_1, dr_num_2))
        full_issue_num = '%04d' % last_dr
        if full_issue_num in issues_data:
            raise ValueError('issue %s already seen' % full_issue_num)
        m = re.fullmatch('([1-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]) (.*)',
                         date_and_author)
        if m:
            date = m.group(1)
            author = m.group(2)
        else:
            date = None
            author = date_and_author
        # For C99 DRs, we prefer the summary from the DR itself (a
        # single summary even for DRs with multiple questions; those
        # multiple-question DRs also have a single response, so are
        # not split up into separate issues, unlike multiple-question
        # C90 DRs) over the one from the summary page, so the one from
        # the summary page is only stored as x-index-summary-html.
        issues_data[full_issue_num] = {
            'x-summary-author-html': author,
            'submitted-against': 'c99',
            'x-index-summary-html': summary,
            'x-orig-status-class': status_class,
            'status': 'unknown',
            'conversion-src': [C99_INDEX],
            'crossref': []}
        if date is not None:
            issues_data[full_issue_num]['date'] = date
            issues_data[full_issue_num]['x-summary-date'] = date
        if status_class not in ('published', 'closed', 'review'):
            raise ValueError('C99 DR #%d: unknown status %s'
                             % (last_dr, status_class))
        if status_class == 'published':
            m = re.fullmatch('Closed, published in TC ([123])', status_text)
            if m:
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = ['c99tc'
                                                           + m.group(1)]
            elif status_text == 'Closed, published in 9899:1999':
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = ['c99']
            else:
                raise ValueError('C99 DR #%d: cannot parse published status %s'
                                 % (last_dr, status_text))
        else:
            m = re.fullmatch('%s, (2[0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9])'
                             % status_class.capitalize(),
                             status_text)
            if not m:
                raise ValueError('C99 DR #%d: cannot parse %s status %s'
                                 % (last_dr, status_class, status_text))
            issues_data[full_issue_num]['x-status-date'] = m.group(1)
            if last_dr in (315, 326, 327, 328, 329, 330, 336, 338, 339, 340,
                           341, 342, 343, 344, 345):
                # These DRs were not fixed in a TC, but have some form
                # of TC or similar fix text in the DR that was applied
                # for C11.  (In the case of DR #339, the fix text is
                # in DR #328, and in the case of DR #342, the fix text
                # is in DR #340.)
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = ['c11']
            else:
                issues_data[full_issue_num]['status'] = 'closed'
    for dr_num in range(C99_FIRST, C99_LAST + 1):
        dr_doc = 'dr_%03d.htm' % dr_num
        dr_body = docs_content[dr_doc]
        dr_body = re.sub('<!--.*?-->', ' ', dr_body)
        if 'Reference Document' in dr_body:
            refdoc_re_frag = (
                r'(?:<b>)?Reference Documents?:(?:</b>)?\s*(.*?)\s*<br>\s*')
        else:
            refdoc_re_frag = '()'
        m = re.fullmatch(
            (r'<html>\s*<head>.*?<title>Defect\s+[Rr]eport\s+#%03d</title>.*?'
             r'</head>\s*<body>\s*<h2>Defect\s+Report\s+#%03d\s*</h2>\s*'
             r'<p><a href="issue:....">(?:Last|Previous) Defect Report</a>\s+'
             r'&lt; -\s+&gt;\s*<a href="issue:....">'
             r'(?:Previous|Next|First) Defect Report</a>\s*</p>'
             r'\s*<p>\s*<b>Submitter:(?:</b>)?\s*(\S[^<]*)<br>\s*'
             r'(?:<b>)?Submission Date:(?:</b>)?(?:\s|&nbsp;)*'
             r'((?:[1-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9])?)\s*<br>\s*'
             r'(?:<b>)?Source:(?:</b>)?\s*(.*?)<br>\s*'
             % (dr_num, dr_num))
            + refdoc_re_frag
            + r'(?:<b>)?Version:</b>\s*(\S[^< ]*)\s*<br>\s*'
            r'<b>Date:</b>(?:\s|&nbsp;)*'
            r'([1-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'
            r'(?: [0-2][0-9]:[0-5][0-9](?::[0-5][0-9])?)?)\s*<br>\s*'
            r'<b>Subject:</b>\s*(\S.*?)</p>\s*'
            r'(.*)<p>\s*'
            r'<a href="issue:....">(?:Last|Previous) Defect Report</a>\s+'
            r'&lt;\s+- &gt;\s+<a href="issue:....">'
            r'(?:Previous|Next|First) Defect Report</a>\s*</p>'
            r'\s*</body>\s*</html>\n',
            dr_body, flags=re.DOTALL)
        if not m:
            raise ValueError('failed to match issue %d body' % dr_num)
        submitter = clean_for_metadata(m.group(1))
        date = m.group(2)
        if not date:
            if dr_num == 245:
                # This DR lacks a submission date in both the summary
                # list and the DR itself.  In the set of C99 DRs
                # version 1.7 (pre-redmond-drs.zip, distributed 25 Sep
                # 2001), the Date (not Submission Date) of version 1.0
                # of this DR was given as 2001-09-21, so use that as a
                # submission date.
                date = '2001-09-21'
            else:
                raise ValueError('missing submission date in DR #%d'
                                 % dr_num)
        author = clean_for_metadata(m.group(3))
        refdoc = clean_for_metadata(m.group(4))
        if refdoc in ('', 'N/A'):
            refdoc = None
        version = clean_for_metadata(m.group(5))
        version_date = m.group(6)
        summary = clean_for_metadata(m.group(7)).rstrip('.')
        content = m.group(8).strip()
        full_issue_num = '%04d' % dr_num
        if 'content-html' in issues_data[full_issue_num]:
            raise ValueError('issue %s already processed' % full_issue_num)
        issues_data[full_issue_num]['summary-html'] = summary
        content_list = ['<html><body>%s</body></html>' % s
                        for s in re.split(r'\s*<hr>\s*', content)]
        issues_data[full_issue_num]['content-html'] = content_list[0]
        comments_list = [{'date': version_date[:10],
                          'filename': '%d.html' % c[0],
                          'author-html': 'WG14',
                          'content-html': c[1]}
                         for c in enumerate(content_list[1:], start=1)]
        issues_data[full_issue_num]['comments'] = comments_list
        issues_data[full_issue_num]['submitter-html'] = submitter
        # Submission dates are not always consistent between the
        # summary (where listed at all) and the individual issues;
        # prefer the individual issue versions.
        # if ('date' in issues_data[full_issue_num]
        #     and date != issues_data[full_issue_num]['date']):
        #     print('%s: date %s -> %s'
        #           % (full_issue_num,
        #              issues_data[full_issue_num]['date'],
        #              date))
        issues_data[full_issue_num]['date'] = date
        # Authors are not generally listed in consistent forms in
        # summary and individual issues; prefer the individual issue
        # versions.
        # print('%s: author %s -> %s'
        #       % (full_issue_num,
        #          issues_data[full_issue_num]['x-summary-author-html'],
        #          author))
        if author:
            issues_data[full_issue_num]['author-html'] = author
        issues_data[full_issue_num]['conversion-src'].append(dr_doc)
        if refdoc is not None:
            issues_data[full_issue_num]['reference-doc-html'] = refdoc
        issues_data[full_issue_num]['x-dr-version'] = version
        issues_data[full_issue_num]['x-dr-version-date'] = version_date


# Mapping from mm/yyyy dates used in single-document issue lists (the
# date of the last change to an issue) to yyyy-mm-dd dates to
# associate with committee responses extracted as comments from the
# issue text.  Issue status changes generally occurred at meetings, so
# use the nominal last day of that month's meeting if available.
# Status changes may not reflect the actual date of the text in the
# extracted comment (especially when the status change came with a
# much later publication of a TC or revised standard), but seem to be
# the closest we can readily get without a lot more case-by-case
# investigation of the history of each issue.
DR_DATE_MAP = {
    '02/2012': '2012-02-17',
    '04/2013': '2013-04-26',
    '10/2013': '2013-10-03',
    '04/2014': '2014-04-11',
    '10/2014': '2014-10-31',
    '04/2015': '2015-04-17',
    '10/2015': '2015-10-29',
    '04/2016': '2016-04-14',
    '10/2016': '2016-10-21',
    '04/2017': '2017-04-07',
    '10/2017': '2017-11-03',
    '04/2018': '2018-04-26',
    '10/2018': '2018-10-18',
    '04/2019': '2019-05-03'}


def extract_single_doc_issues(docs_content, issues_data, doc_name,
                              submitted_against, first_num_expected,
                              last_num_expected, issue_num_format,
                              closed_issue_fix_vers):
    """Extract issue data from a single-document list."""
    all_drs = docs_content[doc_name]
    m = re.fullmatch(
        r'<html>.*?<table>\s*<tr>\s*<th>(?:Request|Defect)</th>\s*'
        r'<th>Summary</th>\s*<th>Date</th>\s*<th>Status</th>\s*</tr>\s*'
        r'(.*?)\s*</table>\s*<hr>\s*(.*?)</body>\s*</html>\s*',
        all_drs, flags=re.DOTALL)
    if not m:
        raise ValueError('failed to parse overall %s content' % doc_name)
    summary_table = m.group(1)
    all_drs = m.group(2)
    prev_dr = first_num_expected - 1
    while True:
        m = re.match(
            r'<tr>\s*<td><a href="[^"]*">DR ([1-9][0-9]*)</a></td>\s*'
            r'<td>(.*?)</td>\s*'
            r'<td>(.*?)</td>\s*'
            r'<td><span class="([^"]*)">(.*?)</span></td>\s*'
            r'</tr>\s*',
            summary_table, flags=re.DOTALL)
        if not m:
            if prev_dr != last_num_expected:
                raise ValueError('summary table in %s parsed up to %d'
                                 % (doc_name, prev_dr))
            break
        prev_dr += 1
        dr_num = m.group(1)
        summary = clean_for_metadata(m.group(2))
        version_date = m.group(3)
        status_class = m.group(4)
        status_text = m.group(5)
        summary_table = summary_table[m.end(0):]
        if dr_num != str(prev_dr):
            raise ValueError('inconsistent DR numbers %s %d %d'
                             % (doc_name, prev_dr, dr_num))
        full_issue_num = issue_num_format % prev_dr
        if full_issue_num in issues_data:
            raise ValueError('issue %s already seen' % full_issue_num)
        issues_data[full_issue_num] = {
            'submitted-against': submitted_against,
            'x-table-summary-html': summary,
            'x-dr-version-date': version_date,
            'x-orig-status-class': status_class,
            'status': 'unknown',
            'conversion-src': [doc_name],
            'crossref': []}
        summary = summary.replace('Proposed defect report regarding ', '')
        issues_data[full_issue_num]['summary-html'] = summary
        if status_class not in ('published', 'closed', 'c17', 'c2x'):
            raise ValueError('%s %d: unknown status %s'
                             % (doc_name, prev_dr, status_class))
        if status_text != status_class.capitalize():
            raise ValueError('%s %d: status %s %s mismatch'
                             % (doc_name, prev_dr, status_class,
                                status_text))
        if status_class != 'closed':
            issues_data[full_issue_num]['status'] = 'fixed'
            if status_class == 'c17':
                fixed_in = 'c17'
            elif status_class == 'c2x':
                fixed_in = 'c23'
            else:
                if doc_name == C11_ALL:
                    fixed_in = 'c11tc1'
                else:
                    fixed_in = 'cscr2013tc1'
            issues_data[full_issue_num]['fixed-in'] = [fixed_in]
        elif closed_issue_fix_vers is not None:
            if prev_dr in closed_issue_fix_vers:
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = \
                    closed_issue_fix_vers[prev_dr]
            else:
                issues_data[full_issue_num]['status'] = 'closed'
    prev_dr = first_num_expected - 1
    while all_drs.startswith('<!-- DRNUM -->'):
        m = re.match('(<!-- DRNUM -->.*?)<!-- DRNUM -->',
                     all_drs, flags=re.DOTALL)
        if m:
            this_dr = m.group(1)
            all_drs = all_drs[m.end(1):]
        else:
            this_dr = all_drs
            all_drs = ''
        prev_dr += 1
        full_issue_num = issue_num_format % prev_dr
        expect_status = (issues_data[full_issue_num]
                         ['x-orig-status-class'].capitalize())
        m = re.fullmatch(
            r'<!-- DRNUM --><p> <b><u>DR %d</u></b></p>\n'
            r'<!-- LINKAGE -->\s*<p>\s*<a href="[^"]*">[^<]*</a>\s*'
            r'Prev &lt;&mdash; %s &mdash;&gt; Next '
            r'<a href="[^"]*">[^<]*</a>\s*, or summary at\s*'
            r'<a href="[^"]*">top</a>\s*</p>\s*'
            r'<p>\s*<b>Submitter:</b>\s*(.*?)<br>\s*'
            r'<b>Submission Date:</b>\s*'
            r'(?:<!--[^>]*-->)?\s*'
            r'(2[0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9])\s*<br>\s*'
            r'(?:<!--[^>]*-->)?\s*'
            r'<b>Source:</b>\s*(.*?)<br>\s*'
            r'<b>Reference Documents?:</b>\s*(.*?)<br>\s*'
            r'<b>Subject:</b>\s*(.*?)</p>\s*'
            r'(.*?)'
            r'<!-- LINKAGE -->\s*(?:</p>)?<p>\s*<a href="[^"]*">[^<]*</a>\s*'
            r'Prev &lt;&mdash; %s &mdash;&gt; Next '
            r'<a href="[^"]*">[^<]*</a>\s*, or summary at\s*'
            r'<a href="[^"]*">top</a>\s*</p>\s*(?:<hr>\s*)?'
            % (prev_dr, expect_status, expect_status),
            this_dr, flags=re.DOTALL)
        if not m:
            raise ValueError('failed to parse %s %d content: [[%s]]'
                             % (doc_name, prev_dr, this_dr[:500]))
        submitter = clean_for_metadata(m.group(1))
        date = m.group(2)
        author = clean_for_metadata(m.group(3))
        refdoc = m.group(4)
        refdoc = re.sub('<!--.*?-->', ' ', refdoc, flags=re.DOTALL)
        refdoc = clean_for_metadata(refdoc)
        if refdoc in ('', 'N/A'):
            refdoc = None
        summary = clean_for_metadata(m.group(5))
        content = m.group(6)
        content = re.sub('<!--.*?-->', ' ', content, flags=re.DOTALL)
        content = content.strip()
        if 'content-html' in issues_data[full_issue_num]:
            raise ValueError('issue %s already processed' % full_issue_num)
        issues_data[full_issue_num]['x-dr-summary-html'] = summary
        summary = summary.replace('Possible defect report: ', '')
        summary = re.sub('<br> <b>Related:</b>.*', '', summary)
        if summary != issues_data[full_issue_num]['summary-html']:
            if len(summary) > len(issues_data[full_issue_num]['summary-html']):
                # Prefer the longer version of the summary.
                issues_data[full_issue_num]['summary-html'] = summary
        content_list = re.split(r'\s*<hr>\s*', content)
        if full_issue_num == '0433':
            # This issue uses <hr> in the original statement.
            content_list = ['<hr>'.join(content_list[:-1]), content_list[-1]]
        content_list = ['<html><body>%s</body></html>' % s
                        for s in content_list]
        issues_data[full_issue_num]['content-html'] = content_list[0]
        version_date = issues_data[full_issue_num]['x-dr-version-date']
        comments_list = [{'date': DR_DATE_MAP[version_date],
                          'filename': '%d.html' % c[0],
                          'author-html': 'WG14',
                          'content-html': c[1]}
                         for c in enumerate(content_list[1:], start=1)]
        issues_data[full_issue_num]['comments'] = comments_list
        issues_data[full_issue_num]['author-html'] = author
        issues_data[full_issue_num]['submitter-html'] = submitter
        issues_data[full_issue_num]['date'] = date
        if refdoc is not None:
            issues_data[full_issue_num]['reference-doc-html'] = refdoc
    if prev_dr != last_num_expected:
        raise ValueError('content in %s parsed up to %d' % (doc_name, prev_dr))


def extract_c11_issues(docs_content, issues_data):
    """Extract C11 issue data from the source documents."""
    extract_single_doc_issues(
        docs_content, issues_data, C11_ALL, 'c11c17',
        400, 503, '%04d',
        # A version of the example from DR#413 was added in C17,
        # despite the issue being listed as closed.
        # DR#424 was addressed in C17 together with DR#416.
        # DR#440 was addressed as a new feature in C23; DRs addressed
        # as new features are listed here as closed not fixed.
        # DR#467 was addressed as a new feature in C23.
        {413: ['c17'], 424: ['c17']})


def extract_cfp_issues(docs_content, issues_data):
    """Extract CFP issue data from the source documents."""
    extract_single_doc_issues(docs_content, issues_data, CFP_ALL, 'cfp-c11',
                              1, 25, '0CFP.%02d', {18: ['c23', 'cfp4-c23']})


def extract_cscr_issues(docs_content, issues_data):
    """Extract C Secure Coding Rules issue data from the source documents."""
    extract_single_doc_issues(docs_content, issues_data, CSCR_ALL, 'cscr2013',
                              1, 2, '0SCR.%02d', {2: ['cscr202y']})


def extract_embc_one(docs_content, issues_data, doc_name,
                     first_num_expected, last_num_expected, issue_num_format,
                     doc_date):
    """Extract issue data from one Embedded C list."""
    all_drs = docs_content[doc_name]
    if doc_name == EMBC_2004_ALL[0]:
        tail_re = (r'<p><b>Email crossreference list:</b>\s*Item\s*'
                   r'Embedded-c emailnumber\s*</p>(.*?)')
    else:
        tail_re = ''
    m = re.fullmatch(
        r'<html>.*?(<p><b>(?:Issue|Defect) %d(?::|</b>).*)%s'
        r'(</body>\s*</html>\s*)'
        % (first_num_expected, tail_re),
        all_drs, flags=re.DOTALL)
    if not m:
        raise ValueError('failed to parse overall %s content' % doc_name)
    all_drs = m.group(1)
    email_data = {}
    if tail_re:
        prev_dr = first_num_expected - 1
        email_list = m.group(2)
        while email_list:
            m = re.match('<p>([1-9][0-9]*): ([^\n]*)\n</p>', email_list)
            if not m:
                raise ValueError('failed to parse email list: %s' % email_list)
            if m.group(1) in email_data:
                raise ValueError('duplicate email data: %s' % m.group(1))
            prev_dr += 1
            if int(m.group(1)) != prev_dr:
                raise ValueError('unexpected email list entry: %s != %d'
                                 % (m.group(1), prev_dr))
            email_data[m.group(1)] = re.sub(
                '([1-9][0-9]*)',
                r'<a href="https://www.open-std.org/jtc1/sc22/wg14/embedded-c/'
                r'\1">\1</a>',
                clean_for_metadata(m.group(2)))
            email_list = email_list[m.end(0):]
        if prev_dr != last_num_expected:
            raise ValueError('email list unexpected ending: %d %d'
                             % (prev_dr, last_num_expected))
    prev_dr = first_num_expected - 1
    while True:
        m = re.match(r'<p><b>(?:Issue|Defect) %d(.*?)\s*</b>\s*</p>\s*'
                     r'(.*?)\s*'
                     r'(<p><b>(?:Issue |Defect )|\Z)'
                     % (prev_dr + 1),
                     all_drs, flags=re.DOTALL)
        if not m:
            if prev_dr == last_num_expected and not all_drs:
                break
            else:
                raise ValueError('failed to parse issue list after %d'
                                 % prev_dr)
        all_drs = all_drs[m.start(3):]
        prev_dr += 1
        full_issue_num = issue_num_format % prev_dr
        summary = m.group(1)
        if summary.startswith(':'):
            summary = summary[1:]
        summary = clean_for_metadata(summary)
        if not summary:
            # Only the first 12 issues have summaries because only the
            # first version of the defect list provides such
            # summaries.
            summary = '[Embedded C 2004 DR#%d]' % prev_dr
        content = m.group(2)
        if full_issue_num in issues_data:
            if email_data:
                raise ValueError('unexpected email data: %s in %s'
                                 % (full_issue_num, doc_name))
            content_html = '<html><body>%s</body></html>' % content
            if issues_data[full_issue_num]['comments']:
                last_is_comment = True
                last_content_html = \
                    issues_data[full_issue_num]['comments'][-1]['content-html']
            else:
                last_is_comment = False
                last_content_html = issues_data[full_issue_num]['content-html']
            compare_content = re.sub(r'(\s|<p>|</p>)', '', content_html)
            compare_last_content = re.sub(r'(\s|<p>|</p>)', '',
                                          last_content_html)
            issues_data[full_issue_num]['conversion-src'].append(
                doc_name.replace('.html', '.pdf'))
            if compare_content == compare_last_content:
                # No non-whitespace differences from the previous
                # version; prefer the whitespace in this version in
                # case of any differences, but keep other metadata
                # from the previous version.
                if last_is_comment:
                    (issues_data[full_issue_num]['comments'][-1]
                     ['content-html']) = content_html
                else:
                    issues_data[full_issue_num]['content-html'] = content_html
            else:
                this_comment = {
                    'date': doc_date,
                    'filename': '%d.html' % (len(
                        issues_data[full_issue_num]['comments']) + 1),
                    'author-html': 'WG14',
                    'content-html': '<html><body>%s</body></html>' % content}
                issues_data[full_issue_num]['comments'].append(this_comment)
        else:
            issues_data[full_issue_num] = {
                'submitted-against': 'embc2004',
                'conversion-src': [doc_name.replace('.html', '.pdf')],
                'crossref': [],
                'summary-html': summary,
                'content-html': '<html><body>%s</body></html>' % content,
                'comments': [],
                'author-html': 'WG14',
                'date': doc_date}
            if prev_dr == 10:
                issues_data[full_issue_num]['status'] = 'closed'
            else:
                issues_data[full_issue_num]['status'] = 'fixed'
                issues_data[full_issue_num]['fixed-in'] = ['embc2008']
            if email_data:
                issues_data[full_issue_num]['reference-doc-html'] = \
                    'Embedded-c email list %s' % email_data[str(prev_dr)]


def extract_embc_issues(docs_content, issues_data):
    """Extract Embedded C issue data from the source documents."""
    # The Embedded C lists are different from the other lists in that
    # rather than having a fixed issue statement, from which WG14 then
    # iterated towards a solution that appeared together with the
    # issue statement in the DR list, the issue statement and solution
    # were edited together (including in one case removing the
    # statement when something was marked as not a defect).  To
    # approximate the structure of the other lists more closely,
    # process multiple versions of the Embedded C list, whereas only
    # the most recent version is processed for other lists.
    extract_embc_one(docs_content, issues_data, EMBC_2004_ALL[0], 1, 12,
                     '0EMB.%02d', '2004-09-23')
    extract_embc_one(docs_content, issues_data, EMBC_2004_ALL[1], 1, 18,
                     '0EMB.%02d', '2004-11-15')
    extract_embc_one(docs_content, issues_data, EMBC_2004_ALL[2], 19, 22,
                     '0EMB.%02d', '2005-03-03')
    extract_embc_one(docs_content, issues_data, EMBC_2004_ALL[3], 1, 22,
                     '0EMB.%02d', '2006-09-25')


def extract_crossrefs(issues_data):
    """Add cross-references between issues based on links in HTML data."""
    for issue_num, issue_content in issues_data.items():
        issue_content['crossref'] = set(issue_content['crossref'])
        html_values = []
        for k, v in issue_content.items():
            if k.endswith('-html'):
                html_values.append(v)
        for c in issue_content['comments']:
            for k, v in c.items():
                if k.endswith('-html'):
                    html_values.append(v)
        for v in html_values:
            for m in re.finditer('<a href="issue:([0-9A-Z.]*)">', v):
                issue_content['crossref'].add(m.group(1))
        if issue_num in issue_content['crossref']:
            if issue_num in ('0469', '0479', '0493'):
                # Valid (if useless) link in a list of some related
                # issues, that is repeated in the response to each of
                # those issues.
                issue_content['crossref'].remove(issue_num)
            else:
                raise ValueError('self-reference from issue %s' % issue_num)
    # Add backward cross-references as well.
    for issue_num, issue_content in issues_data.items():
        for v in issue_content['crossref']:
            issues_data[v]['crossref'].add(issue_num)
    for issue_content in issues_data.values():
        issue_content['crossref'] = sorted(issue_content['crossref'])


def clean_headers(issue_num, text):
    """Clean up header levels."""
    # This is run on issue and comment bodies, not full HTML input
    # files, so that the changes can depend on the header levels used
    # for a given issue.
    # Reserve <h1> and <h2> for issue-list and whole-issue headers
    # rather than using them in individual issue data.
    if '<h1>' in text or '<h2>' in text:
        if '<h4>' in text or '<h5>' in text or '<h6>' in text:
            raise ValueError('unexpected header levels for %s' % issue_num)
        if '<h1>' in text:
            text = text.replace('<h3>', '<h5>')
            text = text.replace('</h3>', '</h5>')
            text = text.replace('<h2>', '<h4>')
            text = text.replace('</h2>', '</h4>')
            text = text.replace('<h1>', '<h3>')
            text = text.replace('</h1>', '</h3>')
        else:
            text = text.replace('<h3>', '<h4>')
            text = text.replace('</h3>', '</h4>')
            text = text.replace('<h2>', '<h3>')
            text = text.replace('</h2>', '</h3>')
    # Convert headers handled through bold text to proper headers.
    text = re.sub(
        r'<p>\s*(Response|Suggested\s+Future\s+Change)\s*</p>',
        r'<p><b>\1</b></p>',
        text)
    text = re.sub(
        r'<p>\s*<b>((?:'
        r'Committee\s+[dD]iscussion'
        r'|Response'
        r'|Committee\s+Response'
        r'|(?:Suggested|Proposed)\s+Committee\s+Response'
        r'|Summary'
        r'|Details'
        r'|Problem'
        r'|Suggested\s+Correction'
        r'|Suggested\s+Changes?'
        r'|Correction'
        r'|Future\s+Change'
        r'|Suggested\s+Future\s+Change'
        r'|Proposed\s+Change'
        r'|(?:Suggested\s+|Proposed\s+)?Technical\s+Corrigendum(?:[^<]*)'
        r'):?)</b>\s*<br>',
        r'<p><b>\1</b></p><p>',
        text)
    text = re.sub(
        r'<p>\s*<b>((?:'
        r'Committee\s+[dD]iscussion'
        r'|Response'
        r'|Committee\s+Response'
        r'|(?:Suggested|Proposed)\s+Committee\s+Response'
        r'|Summary'
        r'|Details'
        r'|Problem'
        r'|Suggested\s+Correction'
        r'|Suggested\s+Changes?'
        r'|Correction'
        r'|Future\s+Change'
        r'|Suggested\s+Future\s+Change'
        r'|Proposed\s+Change'
        r'|(?:Suggested\s+|Proposed\s+)?Technical\s+Corrigendum(?:[^<]*)'
        r'):?)</b>\s*</p>',
        r'<h3>\1</h3>',
        text)
    text = re.sub(
        r'<p>\s*<b>(Committee\s+Discussion)</b>'
        r'\s+(\(for\s+history\s+only\))\s*</p>',
        r'<h3>\1 \2</h3>',
        text)
    # Validate that the text is still properly nested HTML.
    ProcessNesting(issue_num, text).run()
    return text


class CMarkdownConverter(MarkdownConverter):

    """Convert HTML to Markdown for C issues."""

    class Options(MarkdownConverter.DefaultOptions):
        heading_style = ATX
        code_language = 'c'
        wrap = True
        sub_symbol = '<sub>'
        sup_symbol = '<sup>'
        escape_misc = True

    convert_u = abstract_inline_conversion(
        lambda self: '<ins>')

    convert_del = abstract_inline_conversion(
        lambda self: '<del>')


def convert_to_md(content):
    """Convert some HTML content to Markdown."""
    soup = BeautifulSoup(content, 'html5lib')
    return CMarkdownConverter().convert_soup(soup).strip()


def process_issue(issue_num, issue_content):
    """Store and convert the data from an extracted issue."""
    out_dir_html = os.path.join('tmp/out-html', issue_num)
    os.makedirs(out_dir_html, exist_ok=True)
    for k in ('date', 'submitted-against', 'summary-html', 'status',
              'content-html', 'comments', 'crossref', 'conversion-src'):
        if k not in issue_content:
            raise ValueError('issue %s missing key %s' % (issue_num, k))
    if ('author-html' not in issue_content
        and 'submitter-html' not in issue_content):
        raise ValueError('issue %s missing author and submitter')
    if issue_content['submitted-against'] not in (
            'c90', 'c99', 'c11c17', 'cfp-c11', 'cscr2013', 'embc2004'):
        raise ValueError('issue %s bad submitted-against %s'
                         % (issue_num, issue_content['submitted-against']))
    if issue_content['status'] not in ('fixed', 'closed'):
        # fixed = there has been a change in a subsequent document (as
        # specified in fixed-in) to address the issue as a defect fix.
        #
        # closed = resolved without any textual change (answered with
        # interpretation given, not a defect, etc.; it's possible
        # there was also a subsequent textual change, considered a
        # feature change rather than a defect fix, that addressed the
        # issue, but such feature changes are not tracked in issue
        # status)
        raise ValueError('issue %s bad status %s'
                         % (issue_num, issue_content['status']))
    if issue_content['status'] == 'fixed':
        if 'fixed-in' not in issue_content:
            raise ValueError('issue %s missing key fixed-in' % issue_num)
        for c in issue_content['fixed-in']:
            if c not in (
                    'c90', 'c90tc1', 'c90tc2', 'c99', 'c99tc1', 'c99tc2',
                    'c99tc3', 'c11', 'c11tc1', 'c17', 'c23', 'cfp4-c23',
                    'cscr2013tc1', 'cscr202y', 'embc2008'):
                raise ValueError('issue %s bad fixed-in %s'
                                 % (issue_num, issue_content['fixed-in']))
    for c in issue_content['comments']:
        for k in ('date', 'filename', 'content-html'):
            if k not in c:
                raise ValueError('issue %s comment missing key %s'
                                 % (issue_num, k))
        if 'author-html' not in c and 'submitter-html' not in c:
            raise ValueError('issue %s comment missing author and submitter')
    issue_json = issue_content.copy()
    del issue_json['content-html']
    issue_json['comments'] = [c.copy() for c in issue_json['comments']]
    for c in issue_json['comments']:
        del c['content-html']
    with open(os.path.join(out_dir_html, 'metadata.json'), 'w',
              encoding='utf-8') as f:
        json.dump(issue_json, f, indent=4, sort_keys=True)
    with open(os.path.join(out_dir_html, 'issue.html'), 'w',
              encoding='utf-8') as f:
        issue_content['content-html'] = clean_headers(
            issue_num, issue_content['content-html'])
        f.write(issue_content['content-html'])
    for c in issue_content['comments']:
        os.makedirs(os.path.join(out_dir_html, 'comments'), exist_ok=True)
        with open(os.path.join(out_dir_html, 'comments', c['filename']), 'w',
                  encoding='utf-8') as f:
            c['content-html'] = clean_headers(
                issue_num, c['content-html'])
            f.write(c['content-html'])
    out_dir_md = os.path.join('out', issue_num)
    os.makedirs(out_dir_md, exist_ok=True)
    html_keys = [k for k in issue_content if k.endswith('-html')]
    for k in html_keys:
        k_md = k[:-len('-html')] + '-md'
        issue_content[k_md] = convert_to_md(issue_content[k])
        del issue_content[k]
    # A single author list is more meaningful for use in a tracker for
    # future issues than separate author and submitter, so convert
    # that data here.
    authors = []
    if 'author-md' in issue_content:
        authors.append(issue_content['author-md'])
        issue_content['x-author-md'] = issue_content['author-md']
        del issue_content['author-md']
    if 'submitter-md' in issue_content:
        authors.append(issue_content['submitter-md'])
        issue_content['x-submitter-md'] = issue_content['submitter-md']
        del issue_content['submitter-md']
    issue_content['authors-md'] = authors
    for c in issue_content['comments']:
        html_keys = [k for k in c if k.endswith('-html')]
        for k in html_keys:
            k_md = k[:-len('-html')] + '-md'
            c[k_md] = convert_to_md(c[k])
            del c[k]
        c['filename'] = c['filename'][:-len('.html')] + '.md'
    issue_json = issue_content.copy()
    del issue_json['content-md']
    issue_json['comments'] = [c.copy() for c in issue_json['comments']]
    for c in issue_json['comments']:
        del c['content-md']
    with open(os.path.join(out_dir_md, 'metadata.json'), 'w',
              encoding='utf-8') as f:
        json.dump(issue_json, f, indent=4, sort_keys=True)
    with open(os.path.join(out_dir_md, 'issue.md'), 'w',
              encoding='utf-8') as f:
        f.write(issue_content['content-md'] + '\n')
    for c in issue_content['comments']:
        os.makedirs(os.path.join(out_dir_md, 'comments'), exist_ok=True)
        with open(os.path.join(out_dir_md, 'comments', c['filename']), 'w',
                  encoding='utf-8') as f:
            f.write(c['content-md'] + '\n')


def action_convert():
    """Convert the issue lists.  The source data is in in/; the results of
    the conversion are written to out/; intermediate files are left in
    tmp/ to help in checking and debugging the conversion."""
    docs_content = {}
    for doc in list_docs(False):
        docs_content[doc] = clean_doc(doc)
    issues_data = {}
    extract_c90_issues(docs_content, issues_data)
    extract_c99_issues(docs_content, issues_data)
    extract_c11_issues(docs_content, issues_data)
    extract_cfp_issues(docs_content, issues_data)
    extract_cscr_issues(docs_content, issues_data)
    extract_embc_issues(docs_content, issues_data)
    extract_crossrefs(issues_data)
    for issue_num, issue_content in sorted(issues_data.items()):
        process_issue(issue_num, issue_content)


def main():
    """Main program."""
    parser = argparse.ArgumentParser(
        description='Convert old C standard issues to JSON + Markdown')
    parser.add_argument('action',
                        help='What to do',
                        choices=('download', 'convert'))
    args = parser.parse_args()
    action_map = {'download': action_download, 'convert': action_convert}
    action_map[args.action]()


if __name__ == '__main__':
    main()
