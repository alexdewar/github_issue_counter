"""The entry point for the GitHub Issue Counter program."""

import sys

import dateparser

from . import count_issues


def main() -> None:
    """The main entry point to the program."""
    from_date = dateparser.parse(sys.argv[2]).astimezone()
    count = count_issues(sys.argv[1], from_date)
    print(count)


if __name__ == "__main__":
    main()
