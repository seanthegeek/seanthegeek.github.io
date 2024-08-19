#!/usr/bin/env python

import os
from glob import glob
import subprocess

file_extensions = [".png", ".jpg", ".jpeg" ".tiff",
                   ".pbm", ".pgm", ".ppm", ".pnm"]

image_paths = []

for ext in file_extensions:
    image_paths += glob(f"assets/**/*{ext}", recursive=True)

for image_path in image_paths:
    base_filename = ".".join(str(image_path).split(".")[:-1])
    output_path = f"{base_filename}.webp"
    if not os.path.exists(output_path):
        subprocess.run(["cwebp", image_path, "-o", output_path])

