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


def parsing_headings(line):
    """Parsing headings Markdown for generating HTML"""

    count_hashtag = line.count("#")
    remove_hashtag = line.strip(" #")

    return f"<h{count_hashtag}>{remove_hashtag}</h{count_hashtag}>"


def convert_md_to_html(markdown_file, html_file):
    with open(markdown_file, "r") as md, open(html_file, "w") as html:
        for line in md:
            line = parsing_headings(line)
            html.write(line)

def main():
    check()
    convert_md_to_html(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
