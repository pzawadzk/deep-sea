import glob
from PIL import Image
import os
import random

N = 1000
input_dir = "."
output_prefix = "sample_1"
output_dir = os.path.join(input_dir, output_prefix)

files = [f for f in glob.glob(input_dir + "/*.jpg", recursive=False)]


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

sample_files = random.sample(files, N)    
for f in sample_files:
    new_path = os.path.join(output_dir, f[2:])
    os.rename(f, new_path)
