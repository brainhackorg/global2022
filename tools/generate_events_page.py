from asyncore import file_dispatcher
from pathlib import Path
from rich import print
import ruamel.yaml
import chevron
from datetime import datetime
from datetime import timedelta
import shutil
import os


def main():

    root_dir = Path(__file__).parent.parent
    media_dir = root_dir.joinpath("static", "media", "events")

    template_file = root_dir.joinpath("content", "events", "index.mustache")
    locations_file = root_dir.joinpath("data", "locations.yaml")

    yesterday = datetime.now() - timedelta(days=1)
    publishDate = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

    yaml = ruamel.yaml.YAML()
    with open(locations_file, "r", encoding="utf8") as file:
        locations = yaml.load(file)

    fields_to_check = ["image_caption", "image", "website"]

    for this_event in locations["events"]:

        for field in fields_to_check:
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
                print(text)

            output_file = output_dir.joinpath("index.md")
            with open(output_file, "w") as output:
                print(text, file=output)

    with open(citation_file, "w") as output_file:
        yaml.dump(citation, output_file)


if __name__ == "__main__":
    main()
