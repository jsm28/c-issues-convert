#! /usr/bin/env python3

import argparse
import os.path
import subprocess
import time
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


def download_wg14_doc(doc):
    """Download a file from the WG14 website."""
    urllib.request.urlretrieve(
        'https://www.open-std.org/jtc1/sc22/wg14/www/docs/%s' % doc,
        filename=input_filename(doc))
    time.sleep(1)


def action_download():
    """Download old issue lists from the WG14 website.  Since the lists
    are checked into git, it should not be necessary to run this action
    again."""
    download_wg14_doc(C90_INDEX)
    for n in range(C90_FIRST, C90_LAST + 1):
        download_wg14_doc('dr_%03d.html' % n)
    download_wg14_doc(C99_INDEX)
    for n in range(C99_FIRST, C99_LAST + 1):
        download_wg14_doc('dr_%03d.htm' % n)
    download_wg14_doc(C11_ALL)
    download_wg14_doc(CFP_ALL)
    download_wg14_doc(CSCR_ALL)
    download_wg14_doc(EMBC_2004_ALL_PDF)
    # Convert the Embedded C list to HTML for subsequent processing.
    subprocess.run(['pdftohtml', '-noframes', '-q',
                    input_filename(EMBC_2004_ALL_PDF),
                    input_filename(EMBC_2004_ALL)], check=True)


def main():
    """Main program."""
    parser = argparse.ArgumentParser(
        description='Convert old C standard issues to JSON + Markdown')
    parser.add_argument('action',
                        help='What to do',
                        choices=('download',))
    args = parser.parse_args()
    action_map = {'download': action_download}
    action_map[args.action]()


if __name__ == '__main__':
    main()
