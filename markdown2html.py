#!/usr/bin/python3
"""Script to convert a Markdown file to HTML
"""

import hashlib
import os.path
import re
import sys


def check():
    """Check number of arguments and if Markdown file exist"""
    if len(sys.argv) <= 2:
        print("Usage: ./markdown2html.py README.md " "README.html",
              file=sys.stderr)
        return sys.exit(1)

    if os.path.isfile(sys.argv[1]) is False:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        return sys.exit(1)


def parsing_headings(line):
    """Parsing headings Markdown for generating HTML"""

    count_hashtag = line.count("#")

    if 1 <= count_hashtag <= 6:
        remove_hashtag = line.lstrip("#").strip()

        return f"<h{count_hashtag}>{remove_hashtag}</h{count_hashtag}>\n"
    return line


def convert_md5_lowercase(line):
    """Convert in MD5 (lowercase) the content"""
    index_brackets_open = line.index("[")
    index_brackets_closed = line.index("]") + 2
    substring = line[index_brackets_open:index_brackets_closed]

    remove_brackets = substring.replace("[", "").replace("]", "")
    string_hashed = hashlib.md5(remove_brackets.encode("utf-8"))
    string_hashed = string_hashed.hexdigest().lower()

    return f"<p>{line[0:index_brackets_open]}{string_hashed}</p>"


def remove_all_c(line):
    """Remove all c(case insensitive) from the content"""
    string = re.sub(r"[()]", "", line)
    string = string.strip()
    if "c" or "C" in string:
        return f"<p>{string.replace('c', '').replace('C', '')}</p>\n"


def convert_md_to_html(markdown_file, html_file):
    """Convert Markdown to HTML"""
    with open(markdown_file, "r") as md, open(html_file, "w+") as html:
        for line in md:
            if "#" in line:
                line = parsing_headings(line)
            elif "(" in line:
                line = remove_all_c(line)
            elif "[" in line:
                line = convert_md5_lowercase(line)
            html.write(line)


def main():
    check()
    convert_md_to_html(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
