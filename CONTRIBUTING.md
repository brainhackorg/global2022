- [How to contribute to the Brainhack global 2022 website](#how-to-contribute-to-the-brainhack-global-2022-website)
  - [Run the website locally](#run-the-website-locally)
  - [Configuration](#configuration)
  - [Content and what to modify where](#content-and-what-to-modify-where)
    - [Partners](#partners)
  - [Projects](#projects)
  - [Images](#images)
  - [Team](#team)
  - [Updating events](#updating-events)
    - [Requirements](#requirements)
    - [Procedure](#procedure)
  - [Updating the calendar](#updating-the-calendar)


# How to contribute to the Brainhack global 2022 website

Hugo based static website: https://gohugo.io/documentation/

Uses the wowchemy theme: https://wowchemy.com/

Based on bootstrap for the layout: https://getbootstrap.com/

## Run the website locally

1. Install hugo

See the instruction related to the operatiing system you are using on the
[hugo documentation](https://gohugo.io/getting-started/installing/).

2. Fork and clone this repository

3. Run the site locally

```
hugo server -D
```

## Configuration

- config options: `static/admin/config.yml`
- navigation bar: `config/_default/menus.toml`
- default CSS can be "overwritten" in: `assets/scss/custom.scss`.

## Content and what to modify where

Pretty much all the content of the website is either in the `data` or the
`content` folder.

- Event location data for the map: `data/locations.yaml`
- Event details: `content/events`
- Contributors details: `content/authors`

### Partners

- new partner details should be added in `data/partners.yml`
- new images for partners should be added in `static/media/partners`

You can toggle off the partner section
by settting `active = true` in yml front matter of
`content/home/partner.md`.

## Projects

Projects are updated dynamically using the
[`braintransform`](https://github.com/brainhackorg/braintransform) Python
package. The package provides the `transform_issues_to_pages.py` script, which
parses the GitHub issues in a given repository, filters the issues that
correspond to projects, and scrapes the relevant data to generate project
Markdown files that are written to the specified folder. For the current
website, the files are written to the `content/project` folder: the website
generator framework reads the contents of the folder and appropriately renders
the project data. The process is automated using the
`.github/workflows/issue-to-page.yml` GitHub workflow.

## Images

Images from the brain art competition are stored in `static/media/brain-art`.

Extra information about the images is stored in `data/brain-art.yaml`.

You also decide where each image is to be used as background in the yml
frontmatter of the page you want to use it in.

For example in `content/home/team.md`:

```yaml
  # Background image.
  image = "brain_art/jungles_brain.jpeg" # Name of image in `static/media/`.
  image_darken = 0.5  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
  image_size = "cover"  #  Options are `cover` (default), `contain`, or `actual` size.
  image_position = "center"  # Options include `left`, `center` (default), or `right`.
  image_parallax = true  # Use a fun parallax-like fixed background effect? true/false
```

## Team

The details for each team member is in `content/authors` folder.

For team member Jane Smith, the details will be in the frontmatter of
`content/authors/Jane-Smith/_index.md`.

Team belonging is defined in that frontmatter. Which group to display on the
landing page is changed in the frontmatter of `content/home/team.md`

An `avatar.jpg` can be added to the folder to be used as the profile picture.

The corresponding page will be found at `[base-url]/author/jane-smith/`.

## Updating events

### Requirements

This must be done locally on your computer.

This requires python 3.6 or higher.

Make sure to install all the packages from the `requirements.txt` files before
running the main script.

```bash
pip install -r requirements.txt
```

### Procedure

All the information about the events is centralized in: `data/locations.yaml`

Any image for an event must go in `static/media/events`.

Pages for each event are generated in the folder `content/events` by running the
script `tools/generate_events_page.py`  from the root of the repository

```bash
python tools/generate_events_page.py
```

This script uses the mustache template `content/events/index.mustache` to create
the pages by completing with the info from `data/locations.yaml`.

To add new events you can use the commented templates at the top of
`data/locations.yaml`.

If you want to remove an event from the website, you can simply set its
`display` field to `false`.

Commit the newly generated files, push and open a pull request to update the website.


## Updating the calendar

To do so you should have been granted access to this google calendar:

https://calendar.google.com/calendar/embed?src=8mum7e3jm9628q1m6urpktbf1s%40group.calendar.google.com&ctz=Europe%2FBrussels

To add all the google calendar events of a brainhack site,
you must have an `.ics` file that lists all the events of that site.

You should ask the organizers of the brainhack site to provide you with that.

The content should look like a series of events delimited by a `BEGIN:VEVENT`
and `END:VEVENT` tags (see below)

Before adding these events to the global calendar, make sure that the `SUMMARY:`
field of each event starts with the name of the brainhack site (see below).

A quick search and replace should help you fix that.

```text
BEGIN:VEVENT
DTSTART:20221124T123000Z
DTEND:20221124T170000Z
DTSTAMP:20221122T121943Z
UID:3eafiooin01uhfgdg9q7qqekao@google.com
CREATED:20220920T092305Z
DESCRIPTION:
LAST-MODIFIED:20221109T142705Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY: Donostia - Time to Work on Projects (Coffee Break @ 3:00pm)
TRANSP:OPAQUE
END:VEVENT

BEGIN:VEVENT
DTSTART:20221124T110000Z
DTEND:20221124T123000Z
DTSTAMP:20221122T121943Z
UID:5c4i70k4a4b4q4jlgonhpu17gq@google.com
CREATED:20220920T092236Z
DESCRIPTION:
LAST-MODIFIED:20221109T142655Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY: Donostia - Lunch Break
TRANSP:OPAQUE
END:VEVENT
```

Once this is done you can import the `.ics` file into the google calendar:

https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop
