#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import json
import os
import pytest
import requests

from scripts.issues_to_pages import (
    request_issues,
    check_issue_data_request,
    get_issue_data,
    filter_issues_on_state,
    filter_issues_on_label_name,
    get_gh_label_data,
    find_target,
    find_project_link,
    find_project_description,
    extract_website_project_data,
    gather_website_project_data,
    save_project_data,
)

project_keys = sorted([
    "Title",
    "link_to_issue",
    "issue_number",
    "labels",
    "content",
    "project_url",
    "project_description",
])

url = "https://api.github.com/repos/brainhackorg/global2021/issues?per_page=100"


@pytest.fixture
def issue_data():

    issue_data_fname = os.path.join(
        os.path.dirname(__file__), "../data/issue_data.json")

    with open(issue_data_fname, "r") as f:
        issues = json.load(f)

    return issues


def test_request_issues():

    response = request_issues(url)
    assert isinstance(response, requests.Response)


def test_check_issue_data_request():

    response = requests.Response()

    response.status_code = 400
    success = check_issue_data_request(response)

    assert not success

    response.status_code = 200
    success = check_issue_data_request(response)

    assert success


def test_get_issue_data():

    response = request_issues(url)
    issues = get_issue_data(response)

    # In case issues are found (and we have not exceeded the number of
    # requests), check the type and the necessary contents
    api_rate_exceeded_issue_key = "documentation_url"
    issue_keys = ["body", "labels", "number", "state", "title"]
    label_keys = ["color", "description", "name"]
    if issues and api_rate_exceeded_issue_key not in issues[0].keys():
        assert [isinstance(elem, dict) for elem in issues]
        assert [True if key in issue_keys else False for elem in issues for key in elem.keys()]
        assert [True if key in label_keys else False for elem in issues for key in elem["labels"]]


def test_filter_issues_on_state(issue_data):

    issues = list(issue_data.values())
    value = "open"
    filtered_issues = filter_issues_on_state(issues, value)

    expected_open_issues = [issue for issue in issues if issue["state"] == value]

    assert filtered_issues == expected_open_issues


def test_filter_issues_on_label_name(issue_data):

    issues = list(issue_data.values())
    value = "status:published"
    filtered_issues = filter_issues_on_label_name(issues, value)

    expected_open_issues = [issue for issue in issues for label in issue["labels"] if label["name"] == value]

    assert filtered_issues == expected_open_issues


def test_get_gh_label_data(issue_data):

    issue = list(issue_data.values())[0]
    obtained_labels = get_gh_label_data(issue)

    expected_labels = dict({"labels": []})
    for label in issue["labels"]:
        label_name = label["name"]
        label_description = label["description"]
        label_color = label["color"]
        label_dict = {
            "name": label_name,
            "description": label_description,
            "color": label_color,
        }
        expected_labels["labels"].append(label_dict)

    assert obtained_labels == expected_labels


def test_find_target():

    text = "Section1 my text Section2"
    pattern = "(?<=Section1)(.*)[^Section2]"
    obtained_target = find_target(pattern, text)

    expected_target = " my text "
    assert obtained_target == expected_target

    text = "Section my text Section2"
    pattern = "(?<=Section1)(.*)[^Section2]"
    obtained_target = find_target(pattern, text)

    assert not obtained_target


def test_find_project_link():

    text = """### Link to project repository/sources

    https://www.projecturl.com

    ### Another section
    """
    obtained_target = find_project_link(text)

    expected_target = "https://www.projecturl.com"
    assert obtained_target == expected_target

    text = """### Link to project

    https://www.projecturl.com

    ### Another section
    """
    obtained_target = find_project_link(text)

    assert not obtained_target


def test_find_project_description():

    text = """### Project Description

    The project description is a short text.

    ### Another section
    """
    obtained_target = find_project_description(text)

    expected_target = "\n\n    The project description is a short text.\n\n    "
    assert obtained_target == expected_target

    text = """### Description

    https://www.projecturl.com

    ### Another section
    """
    obtained_target = find_project_link(text)

    assert not obtained_target


def test_extract_website_project_data(issue_data):

    issue = list(issue_data.values())[0]
    obtained_project_data = extract_website_project_data(issue)

    assert len(obtained_project_data) == len(project_keys)
    assert sorted(obtained_project_data.keys()) == project_keys

    # Test with an issue that does not have a project URL / description
    issue = list(issue_data.values())[1]
    obtained_project_data = extract_website_project_data(issue)

    no_url_desc_proj_keys = copy.deepcopy(project_keys)
    no_url_desc_proj_keys.remove("project_url")
    no_url_desc_proj_keys.remove("project_description")
    assert len(obtained_project_data) == len(no_url_desc_proj_keys)
    assert sorted(obtained_project_data.keys()) == no_url_desc_proj_keys

    # ToDo
    # Test further cases


def test_gather_website_project_data(issue_data):

    issues = list(issue_data.values())
    obtained_project_data = gather_website_project_data(issues)

    assert len(obtained_project_data) == len(issues)

    assert [True if sorted(list(obtained_project_data.values())[0]) == project_keys else False]


def test_save_project_data(tmp_path, issue_data):

    issues = list(issue_data.values())
    website_project_data = gather_website_project_data(issues)
    save_project_data(website_project_data, tmp_path)

    # Only check the number of files written
    expected_file_count = len(issues)
    obtained_file_count = sum(1 for item in os.listdir(tmp_path) if os.path.isfile(os.path.join(tmp_path, item)))

    assert obtained_file_count == expected_file_count
