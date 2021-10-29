---
# An instance of the Blank widget.
# Documentation: https://sourcethemes.com/academic/docs/page-builder/
widget: "blank"

# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 22

title: "Schedule"
subtitle: "Don't miss out on the next coming events!"
# Hero image (optional). Enter filename of an image in the `static/media/` folder.
# hero_media: "virtualbh_2.png"
design:
  columns: "1"
  clip_path: "polygon(0% 0%, 100% 0%, 100% 95%, 0% 100%)"
  background:
    image: laptop_world.svg
    image_darken: 0.0
    image_parallax: true
    image_position: center
    image_size: contain
    text_color_light: false
    color: "#e3eeed"

  spacing:
    padding: ["100px", "0", "100px", "0"]

advanced:
 # Custom CSS.
 css_style: ""

 # CSS class.
 css_class: "text-center"

---
<div id='calendar-container'>
  <iframe
    src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=2&amp;bgcolor=%23ffffff&amp;ctz=America%2FToronto&amp;src=OG11bTdlM2ptOTYyOHExbTZ1cnBrdGJmMXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%234285F4&amp;mode=AGENDA&amp;showCalendars=0&amp;showNav=1&amp;showPrint=0" style="border:solid 1px #777"
    width="100%"
    height="700"
    frameborder="0"
    scrolling="no">
  </iframe>
</div>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.4/jstz.min.js'></script>
<script type="text/javascript">
  var timezone = jstz.determine();
  var pref = '<iframe src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=2&amp;bgcolor=%23ffffff&amp;src=OG11bTdlM2ptOTYyOHExbTZ1cnBrdGJmMXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%234285F4&amp;mode=AGENDA&amp;showCalendars=0&amp;showNav=1&amp;showPrint=0&amp;ctz=';
  var suff = '" style="border:solid 1px #777" width="100%" height="700" frameborder="0" scrolling="no"></iframe>';
  var iframe_html = pref + timezone.name() + suff;
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>
