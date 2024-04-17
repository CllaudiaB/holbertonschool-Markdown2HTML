#!/usr/bin/python3
"""Script to convert a Markdown file to HTML
"""

import sys
import os.path


def check():
    """Check number of arguments and if Markdown file exist"""
    if len(sys.argv) <= 2:
        print('Usage: ./markdown2html.py README.md '
              'README.html', file=sys.stderr)
        return sys.exit(1)

    if os.path.isfile(sys.argv[1]) is False:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        return sys.exit(1)


def parsing_headings(markdown):
    """Parsing headings Markdown for generating HTML"""
    file_markdown = open("README.md", "r")
    file_html = open("README.html", "w")

    for line in file_markdown:
        count_hashtag = line.count("#")
        remove_hashtag = line.strip(" #")

        print(f"<h{count_hashtag}>{remove_hashtag}</h{count_hashtag}>")


def main():
    check()
    parsing_headings(sys.argv[1])


if __name__ == "__main__":
    main()
