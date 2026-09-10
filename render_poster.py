from html2image import Html2Image
import os

h2i = Html2Image()
h2i.output_path = '.'

# Convert the poster to a premium image at 3:4 aspect ratio (high resolution 2400x3200 for prints)
h2i.screenshot(
    html_file='presentation_poster.html',
    save_as='presentation_poster.jpg',
    size=(1200, 1600)
)
print("Poster generated successfully as presentation_poster.jpg")
