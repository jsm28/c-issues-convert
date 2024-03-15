#! /usr/bin/env python3

import argparse
import os
import os.path
import re
import subprocess
import time
import urllib.parse
import urllib.request


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
EMBC_2004_ALL_PDF = 'n1180.pdf'
EMBC_2004_ALL = 'n1180.html'


def input_filename(doc):
    """Return the local filename of a WG14 document."""
    return os.path.join('in', doc)


def doc_url(doc):
    """Return the WG14 website URL of a WG14 document."""
    return 'https://www.open-std.org/jtc1/sc22/wg14/www/docs/%s' % doc


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
        ret.append(EMBC_2004_ALL_PDF)
    else:
        ret.append(EMBC_2004_ALL)
    return ret


def action_download():
    """Download old issue lists from the WG14 website.  Since the lists
    are checked into git, it should not be necessary to run this action
    again."""
    for doc in list_docs(True):
        download_wg14_doc(doc)
    # Convert the Embedded C list to HTML for subsequent processing.
    subprocess.run(['pdftohtml', '-noframes', '-q',
                    input_filename(EMBC_2004_ALL_PDF),
                    input_filename(EMBC_2004_ALL)], check=True)


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
    'h1', 'h2', 'h3', 'h4', 'p', 'ol', 'ul', 'li', 'blockquote', 'pre', 'br',
    'a', 'code', 'b', 'i', 'del', 'sup', 'sub', 'table', 'tr', 'td', 'th',
    'hr',
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


# Attributes to discard on certain tags (regardless of the attribute
# value).
KNOWN_ATTRS_DISCARD = {
    'a': {'title'},
    'b': {'style'},
    'body': {'bgcolor', 'link', 'vlink'},
    'br': {'style'},
    'dl': {'compact'},
    'h2': {'align', 'id'},
    'h3': {'align'},
    'hr': {'style'},
    'html': {'lang', 'xml:lang', 'xmlns'},
    'i': {'style'},
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
    'a': {'href', 'id', 'name'},
    'center': {'class'},
    'div': {'style'},
    'li': {'id', 'value'},
    'ol': {'type'},
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
        m = re.search('<([^<>]*)>', rtext)
        if not m:
            raise ValueError("unmatched '<' or '>' in %s [%s]" % (doc, rtext))
        before = rtext[:m.start(0)]
        tag = m.group(0)
        tag_contents = m.group(1)
        after = rtext[m.end(0):]
        if '<' in before or '>' in before:
            raise ValueError("unmatched '<' or '>' in %s [%s]" % (doc, before))
        new_text_list.append(before)
        rtext = after
        if tag.startswith('<!DOCTYPE'):
            # Discard the DOCTYPE.
            continue
        if tag.startswith('<!--') and tag.endswith('-->'):
            # Pass through the comment (may be relevant for splitting
            # individual issues out of multi-issue files, though not
            # for the final output).
            new_text_list.append(tag)
            continue
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
                        value = ';'.join(styles_new)
                if attr_name not in to_keep:
                    raise ValueError('unknown attribute %s on %s tag in %s'
                                     % (attr_name, tag_name, doc))
                cleaned_tag_attrs.append((attr_name, value))
            tag_attrs = cleaned_tag_attrs
        if end_tag:
            new_text_list.append('</%s>' % tag_name)
        else:
            new_text_list.append('<%s' % tag_name)
            for attr_name, value in tag_attrs:
                if value is None:
                    new_text_list.append(' %s' % attr_name)
                else:
                    new_text_list.append(' %s=%s' % (attr_name, value))
            new_text_list.append('>')
    new_text_list.append(rtext)
    return ''.join(new_text_list)


# List of functions for cleaning HTML issue lists.
CLEAN_FUNCS_LIST = (clean_amp, clean_ltgt, clean_chars, clean_tags)


def clean_doc(doc, write_out):
    """Pass an HTML input document through a series of cleaning steps,
    returning the cleaned document, and writing out the output of each
    step if requested."""
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
        if write_out:
            out_dir = 'clean-%d' % n
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, doc), 'w', encoding='utf-8') as f:
                f.write(text)
    return text


def action_clean():
    """Test the process of cleaning the HTML issue lists, writing out the
    state of the files after each cleaning step.  The actual issue
    conversion does the cleaning without writing out intermediate files;
    this action is only intended for test purposes."""
    for doc in list_docs(False):
        clean_doc(doc, True)


def main():
    """Main program."""
    parser = argparse.ArgumentParser(
        description='Convert old C standard issues to JSON + Markdown')
    parser.add_argument('action',
                        help='What to do',
                        choices=('download', 'clean'))
    args = parser.parse_args()
    action_map = {'download': action_download, 'clean': action_clean}
    action_map[args.action]()


if __name__ == '__main__':
    main()
