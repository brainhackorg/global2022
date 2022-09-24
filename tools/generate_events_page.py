from pathlib import Path
from rich import print
import ruamel.yaml
import chevron
from datetime import datetime
from datetime import timedelta
import shutil
import os

from collections import OrderedDict


def main():

    root_dir = Path(__file__).parent.parent
    media_dir = root_dir.joinpath("static", "media", "events")

    template_file = root_dir.joinpath("content", "events", "index.mustache")
    locations_file = root_dir.joinpath("data", "locations.yaml")

    yesterday = datetime.now() - timedelta(days=1)
    publishDate = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    with open(locations_file, "r", encoding="utf8") as file:
        locations = yaml.load(file)

    order = [
        "title",
        "format",
        "display",
        "abstract",
        "summary",
        "organizers",
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
        "image",
        "image_caption",
        "publishDate",
    ]

    for i, this_event in enumerate(locations["events"]):

        for field in order:
            if field not in this_event:
                this_event[field] = None

        if this_event["display"]:

            output_dir = root_dir.joinpath(
                "content", "events", this_event["title"].lower().replace(" ", "_")
            )
            output_dir.mkdir(parents=True, exist_ok=True)

            this_event["publishDate"] = publishDate

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

        ordered = OrderedDict()
        for k in order:
            ordered[k] = this_event[k]

        locations["events"][i] = dict(ordered)

    with open(locations_file, "w") as output_file:
        yaml.dump(locations, output_file)

if __name__ == "__main__":
    main()
