import glob
from PIL import Image
import os

input_dir = "."
output_prefix = "resize"
output_dir = os.path.join(input_dir, output_prefix)

def resize_image(path, output_dir):
    img = Image.open(path)
    new_img = img.resize((256, 256))
    new_file = os.path.join(output_dir + f[1:])
    new_img.save(new_file)


files = [f for f in glob.glob(input_dir + "/*.jpg", recursive=False)]


if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
for f in files:
    try:
        resize_image(f, output_dir)
    except:
        print(f)
