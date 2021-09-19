# How to contribute to the Brainhack global 2021 website

Hugo based static website: https://gohugo.io/documentation/

Uses the wowchemy theme:https://wowchemy.com/
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

## Projects

Projects were updated dynamically in `content/project` using the github workflow
`workflows/issue-to-page.yml` that calls the script `issues_to_pages.py`.

