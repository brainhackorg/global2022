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

    yesterday = datetime.now() - timedelta(days = 1)
    publishDate = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

    yaml = ruamel.yaml.YAML()
    with open(root_dir.joinpath("data", "locations.yaml"), "r", encoding="utf8") as locations_file:
        locations = yaml.load(locations_file)          

    template_file = root_dir.joinpath("content", "events", "index.mustache")
    for loc in locations["events"]:
        if loc["display"]:

            loc["publishDate"] = publishDate

            with open(template_file, 'r') as template:
                text = chevron.render(template, loc) 
                print(text)  

            output_dir = root_dir.joinpath("content", "events", loc["title"].lower().replace(" ", "_"))
            output_dir.mkdir(parents=True, exist_ok=True)   

            output_file = output_dir.joinpath("index.md")
            with open(output_file, 'w') as output:
                print(text, file=output)

            if "image" in loc:
                image_file = media_dir.joinpath(loc["image"])
                extension = os.path.splitext(image_file)[1]
                shutil.copyfile(image_file, output_dir.joinpath(f"featured{extension}"))  
  




if __name__ == '__main__':
    main()
