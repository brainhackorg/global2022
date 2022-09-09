+++
# Hero widget.
widget = "hero"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "Brainhack Global 2022"

# Hero image (optional). Enter filename of an image in the `static/media/` folder.
hero_media = "headers/brain.png"

[design]
  clip_path = "polygon(0% 0%, 100% 0, 100% 80%, 0% 100%)"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  color = "#2a4644"

  # Background gradient.
  gradient_start = "#2a4644"
  gradient_end = "#64a19d"

  # Background image.
 # image = "headers/brain.png"  # Name of image in `static/media/`.
 # image_darken = 0.0  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
 # image_size = "actual"  #  Options are `cover` (default), `contain`, or `actual` size.
 # image_position = "center"  # Options include `left`, `center` (default), or `right`.
 # image_parallax = true  # Use a fun parallax-like fixed background effect? true/false

  # Text color (true=light or false=dark).
  text_color_light = true

# Call to action links (optional).
#   Display link(s) by specifying a URL and label below. Icon is optional for `[cta]`.
#   Remove a link/note by deleting a cta/note block.
# [cta]
#   url = "/events#host-your-own-local-brainhack"
#   label = "Host your own local Brainhack"
#   icon_pack = "fas"
#   icon = "map-pin fa-fw"
#
# [cta_alt]
#   url = "#projects"
#   label = "Show the projects"

# Note. An optional note to show underneath the links.
#[cta_note]
#  label = '<a class="js-github-release" href="https://sourcethemes.com/academic/updates" data-repo="gcushen/hugo-academic">Latest releaseV</a>'
+++

<br>

## **November 28th - December 11th**

<br>

<p class="cta-btns">
  <a href="events#host-your-own-local-brainhack"
    class="btn bg.text_color_light btn-light btn-primary btn-lg"
    style="text-decoration: none">
    <i class="fas fa-map-pin pr-2" aria-hidden="true"></i>
    Host your own local Brainhack
  </a>
</p>

<p class="cta-btns">
  <a href="events"
      class="btn bg.text_color_light btn-light btn-primary btn-lg"
      style="text-decoration: none">
    <i class="fas fa-globe pr-2" aria-hidden="true"></i>
    Register for a local event
  </a>
</p>

<p class="cta-btns">
  <a href="https://github.com/brainhackorg/global2022/issues/new?assignees=&labels=project&template=project-submission-template.yml"
      class="btn bg.text_color_light btn-light btn-primary btn-lg"
      style="text-decoration: none"
      target="_blank">
    <i class="fas fa-file-import pr-2" aria-hidden="true"></i>
    Submit a project
  </a>
</p>

<p class="cta-btns">
  <a href="projects"
      class="btn bg.text_color_light btn-light btn-primary btn-lg"
      style="text-decoration: none">
    <i class="fas fa-thumbs-up pr-2" aria-hidden="true"></i>
    Join a project
  </a>
</p>
