# How to contribute to the Brainhack global 2021 website

## Content and what to modify where

- Event location data for the map:

```
data/locations.yaml
```

- Event details:

```
content/events
```

- Projects were updated dynamically:

```
content/project
```

- I guess using this action:

```
workflows/issue-to-page.yml
```

- Some config options:

```
static/admin/config.yml
```

- Author data/pictures:

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
