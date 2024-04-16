#!/usr/bin/python3
"""Script to convert a Markdown file to HTML
"""

import sys
import os.path


def main():
    """Check number of arguments and if Markdown file exist"""
    if len(sys.argv) <= 2:
        print('Usage: ./markdown2html.py README.md '
              'README.html', file=sys.stderr)
        sys.exit(1)

    if os.path.isfile(sys.argv[1]) == False:
            print(f"Missing {sys.argv[1]}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
