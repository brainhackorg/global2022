#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import requests
import re
import sys

extension_sep = "."
md_extension = "md"
underscore = "_"
website_project_fname_label = "project"


def request_issues(url):
    """Request issues from the given GitHub project URL.

    Parameters
    ----------
    url : str
        URL of GitHub project.

    Returns
    -------
    response : Response
        Response data.
    """

    response = requests.get(url)

    return response


def check_issue_data_request(response):
    """Check the issue request response success.

    Parameters
    ----------
    response : Response
        Response data.

    Returns
    -------
    success : bool
        `True` if  response was.
    """

    if response.status_code != 200:
        print(
            "Cannot continue: no issues found or request for issues unsuccessful.\nResponse:\n".format(
                response
            )
        )
        success = False

    else:
        success = True

    return success


def get_issue_data(response):
    """Get the issue data contained in the response.

    Parameters
    ----------
    response : Response
        Response data.

    Returns
    -------
    issues : list
        Issue data.
    """

    issues = json.loads(response.content.decode("utf-8"))

    return issues


def filter_issues_on_state(issues, value):
    """Filter issues based on the value of their state.

    Parameters
    ----------
    issues : list
        Issue data.
    value : str
        Value required for the state, e.g. "open".

    Returns
    -------
    filtered_issues : list
        Filtered issues.
    """

    filtered_issues = [issue for issue in issues if issue["state"] == value]

    return filtered_issues


def filter_issues_on_label_name(issues, value):
    """Filter issues based on their label name.

    Parameters
    ----------
    issues : list
        Issue data.
    value : str
        Value required for the label name, e.g. "status:web_ready".

    Returns
    -------
    filtered_issues : list
        Filtered issues.
    """

    filtered_issues = [
        issue for issue in issues for label in issue["labels"] if label["name"] == value
    ]

    return filtered_issues


def get_gh_label_data(issue):
    """Get `GitHub` issue label data contained in the issue.

    Parameters
    ----------
    issue : dict
        Issue data.

    Returns
    -------
    labels : dict
        `GitHub` issue label data.
    """

    labels = dict({"labels": []})

    for label in issue["labels"]:
        # TODO: Implement some conditionals to filter out irrelevant labels that we created. For now, HUGO can discard them.
        label_name = label["name"]
        label_description = label["description"]
        label_color = label["color"]
        label_dict = {
            "name": label_name,
            "description": label_description,
            "color": label_color,
        }
        labels["labels"].append(label_dict)

    return labels


def extract_website_project_data(issue):
    """Extract project data relevant for the website.

    Parameters
    ----------
    issue : dict
        Issue data.

    Returns
    -------
    project_data : dict
        Project data.
    """

    project_data = dict({})

    # Gather required data
    title = {"Title": issue["title"].strip()}
    project_data.update(title)

    link_to_issue = {"link_to_issue": issue["html_url"]}
    project_data.update(link_to_issue)

    issue_number = {"issue_number": issue["number"]}
    project_data.update(issue_number)

    # Get relevant GitHub issue label data
    labels = get_gh_label_data(issue)
    project_data.update(labels)

    content = {"content": issue["body"]}
    project_data.update(content)

    # Get project URL if provided

    # Get the body of the relevant section
    proj_url_re_match = re.search(
        "(?<=### Link to project repository/sources[^\v]{2})((?:.*\r?\n?)*)(?=[^\v]{2}###)",
        issue["body"],
    )
    # Get the URLs
    proj_url_re_match = re.search(
        "\b(http:|www\.)(?:[^\s,.;:!?]|[,.!?](?!\s))+",
        proj_url_re_match.group(),
    )
    if proj_url_re_match:
        project_url = {"project_url": proj_url_re_match.group()}
        project_data.update(project_url)

    # Get project description if provided
    proj_desc_re_match = re.search(
        "(?<=### Project Description[^\v]{2})((?:.*\r?\n?)*)(?=[^\v]{2}###)",
        issue["body"],
        flags=re.DOTALL,
    )
    if proj_desc_re_match:
        project_desc = {"project_description": proj_desc_re_match.group()}
        project_data.update(project_desc)

    # TODO: Grab other relevant terms such as Project leads, etc.

    return project_data


def gather_website_project_data(issues):
    """Gather the project data for the website by extracting the relevant data
    from the issues.

    Parameters
    ----------
    issues : list
        Issue data.

    Returns
    -------
    projects : dict
        Project data.
    """

    # Filter issues that are not open
    value = "open"
    issues_of_interest = filter_issues_on_state(issues, value)

    # Filter issues that do not have a published status
    value = "status:web_ready"
    issues_of_interest = filter_issues_on_label_name(issues_of_interest, value)

    projects = dict({})
    i = 0

    # Loop over issues to gather the relevant data
    for issue in issues_of_interest:
        i += 1

        project_data = extract_website_project_data(issue)
        projects.update({"project_{0}".format(i): project_data})

    return projects


def save_project_data(website_project_data, path):
    """Save the website project data as separate Markdown files.

    Parameters
    ----------
    website_project_data : dict
        Project data.
    path : str
        Path were project data will be saved.
    """

    for project in website_project_data.items():

        file_rootname = (
            website_project_fname_label + underscore + str(project[1]["issue_number"])
        )
        file_basename = file_rootname + extension_sep + md_extension
        fname = os.path.join(path, file_basename)

        with open(fname, "w") as json_file:
            json.dump(project[1], json_file, indent=2)


def main():

    # Request issues
    url = "https://api.github.com/repos/brainhackorg/global2021/issues?per_page=100"
    response = request_issues(url)

    # Check whether the response was successful
    success = check_issue_data_request(response)
    if not success:
        sys.exit()

    # Get issue data
    issues = get_issue_data(response)

    # Get the appropriate data for the website from the issues
    website_project_data = gather_website_project_data(issues)

    # Save the project data
    path = "content/project"
    save_project_data(website_project_data, path)


if __name__ == "__main__":
    main()
