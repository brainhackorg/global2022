#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert relevant issue data to Markdown files so that they can be used to
populate the website project section.

Usage:
> python issues_to_pages.py "https://api.github.com/repos/brainhackorg/global2021/issues?per_page=100" "content/project"

"""

import argparse
import sys

from issues_to_pages import (
    check_issue_data_request,
    gather_website_project_data,
    get_issue_data,
    request_issues,
    save_project_data,
)


def _build_arg_parser():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=__doc__)

    parser.add_argument("url", help="URL where to fetch issues.")
    parser.add_argument(
        "path",
        help="Path where to write relevant issue data to Markdown files."
    )

    return parser


def main():

    parser = _build_arg_parser()
    args = parser.parse_args()

    # Request issues
    response = request_issues(args.url)

    # Check whether the response was successful
    success = check_issue_data_request(response)
    if not success:
        sys.exit()

    # Get issue data
    issues = get_issue_data(response)

    # Get the appropriate data for the website from the issues
    website_project_data = gather_website_project_data(issues)

    # Save the project data
    save_project_data(website_project_data, args.path)


if __name__ == "__main__":
    main()
