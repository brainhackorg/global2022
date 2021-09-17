# How to contribute to the Brainhack global 2021 website

## Content and what to modify where

Pretty much all the content of the website is either in the `data` or the
`content` folder.

### config options

```
static/admin/config.yml
```

Default CSS can be "overwritten" in the `assets/scss/custom.scss`.

### Event location data for the map

```
data/locations.yaml
```

### Event details:

```
content/events
```

### Projects

Projects were updated dynamically in `content/project` using this action
`workflows/issue-to-page.yml` that calls the script `issues_to_pages.py`.

### Contributors details

```
content/authors
```

## Run the website locally

1. Install hugo

See the instruction related to the operatiing system you are using on the
[hugo documentation](https://gohugo.io/getting-started/installing/).

2. Fork and clone this repository

3. Run the site locally

```
hugo server
```

issue_to_pages
