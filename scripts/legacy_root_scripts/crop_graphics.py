from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

# Crop Figure 1
# Based on visual, Figure 1 is in middle-bottom
img3 = Image.open('figure_page-3.png')
w, h = img3.size
# Crop to roughly where the box/diagram is
# Diagram is below "UTAUT resolves a critical flaw..."
# Manual crop based on visual guess: bottom half
figure_box = img3.crop((0, int(h*0.58), w, int(h*0.75)))
trim(figure_box).save('figure_utaut.png')

# Crop Output Boxes
img8 = Image.open('output_page-8.png')
w, h = img8.size
# Boxes are below "Expected Output" header
output_box = img8.crop((0, int(h*0.60), w, int(h*0.80)))
trim(output_box).save('expected_outputs.png')

# Crop Impact Pathway Box (the green one) at bottom of page 8
impact_box = img8.crop((0, int(h*0.80), w, int(h*0.93)))
trim(impact_box).save('impact_pathway.png')

print("Graphics cropped successfully.")
