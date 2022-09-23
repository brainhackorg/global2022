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

Team belonging is defined in that frontmatter.
Which group to display on the landing page is changed in the frontmatter of
`content/home/team.md`

An `avatar.jpg` can be added to the folder to be used as the profile picture.

The corresponding page will be found at `[base-url]/author/jane-smith/`.
