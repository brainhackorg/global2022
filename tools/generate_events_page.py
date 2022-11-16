"""this script:
- loads the locations.yaml file
- creates a folder for each event
- copies the image of the event from the static folder to the event folder if there is one
- creates an index.md file for each event
- updates the publishDate of each event to be yesterday if the event is to be displayed
  otherwise it is set to a date far in the future
- updates missing fields in the locations.yaml file
- sort the fields in the locations.yaml file for each event
- saves the locations.yaml file
- updates the project issue form to only list available events
"""


import os
import shutil
from collections import OrderedDict
from datetime import datetime, timedelta
from pathlib import Path

import chevron
import ruamel.yaml
from rich import print

from utils import update_project_template

ORDER = [
    "title",
    "format",
    "display",
    "abstract",
    "summary",
    "organizers",
    "contact",
    "location",
    "address",
    "position",
    "date",
    "date_end",
    "mattermost_channel",
    "twitter_handle",
    "facebook",
    "instagram",
    "website",
    "github_username",
    "image",
    "image_caption",
    "publishDate",
]


def reorder_fields_event(event, order=ORDER):
    ordered = OrderedDict()
    for k in order:
        ordered[k] = event[k]
    return dict(ordered)


def return_publish_date(event):
    publish_date = datetime.now() + timedelta(days=3650)
    if event["display"]:
        publish_date = datetime.now() - timedelta(days=1)
    return publish_date.strftime("%Y-%m-%d")


def return_image_caption(this_event):
    if this_event["image_caption"] in [None, ""] and this_event["website"] is not None:
        return f"Image credit: [**{this_event['title']}**]({this_event['website']})"
    else:
        return ""


def main():

    root_dir = Path(__file__).parent.parent
    media_dir = root_dir.joinpath("static", "media", "events")

    template_file = root_dir.joinpath("content", "events", "index.mustache")

    locations_file = root_dir.joinpath("data", "locations.yaml")

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    with open(locations_file, "r", encoding="utf8") as file:
        locations = yaml.load(file)

    active_sites = []

    for i, this_event in enumerate(locations["events"]):

        print(f"[bold blue]Processing: {this_event['title']}[/bold blue]")

        for field in ORDER:

            # ensure that all fields are set in case manual editing forgot some
            if field not in this_event:
                this_event[field] = None

            # create an index.md file for each event and copy the image to the static folder
            output_dir = root_dir.joinpath(
                "content", "events", this_event["title"].lower().replace(" ", "_")
            )
            output_dir.mkdir(parents=True, exist_ok=True)

            this_event["publishDate"] = return_publish_date(this_event)

            # remove old image if it exists
            # and replace it with the new one if provided
            images = output_dir.glob("feature*")
            for image in images:
                image.unlink(missing_ok=True)

            if this_event["image"] is not None:

                image_file = media_dir.joinpath(this_event["image"])
                extension = os.path.splitext(image_file)[1]
                shutil.copyfile(image_file, output_dir.joinpath(f"featured{extension}"))

                if (
                    this_event["image_caption"] is None
                    and this_event["website"] is not None
                ):
                    this_event[
                        "image_caption"
                    ] = f"Image credit: [**{this_event['title']}**]({this_event['website']})"

            with open(template_file, "r") as template:
                text = chevron.render(template, this_event)
                # print(text)

            output_file = output_dir.joinpath("index.md")
            with open(output_file, "w") as output:
                print(text, file=output)

        locations["events"][i] = reorder_fields_event(event=this_event, order=ORDER)

        if this_event['display']:
            active_sites.append(this_event['title'])

    active_sites = sorted(active_sites)
    print(f"\nactive sites: {active_sites}")

    update_project_template(active_sites)

    with open(locations_file, "w") as output_file:
        yaml.dump(locations, output_file)


if __name__ == "__main__":
    main()
