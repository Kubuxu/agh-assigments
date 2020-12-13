from PIL import Image
import glob
import os

for jpg in glob.iglob("*.jpg"):
    img = Image.open(jpg)
    p, _ = os.path.splitext(jpg)
    img.save(p+".png")

