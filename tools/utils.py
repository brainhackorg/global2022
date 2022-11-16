from pathlib import Path

import ruamel.yaml
from rich import print




yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

def update_project_template(sites: list = None):

    root_dir = Path(__file__).parent.parent
    project_template_file = root_dir.joinpath(
        ".github", "ISSUE_TEMPLATE", "project-submission-template.yml"
    )

    with open(project_template_file, "r", encoding="utf8") as file:
        project_template = yaml.load(file)

    if sites is not None:
        project_template["body"][5]["attributes"]["options"] = sites

    with open(project_template_file, "w") as file:
        yaml.dump(project_template, file)
