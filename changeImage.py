#!/usr/bin/env python3
from PIL import Image
import os

path = "./supplier-data/images/"
for file in os.listdir("./supplier-data/images"):
    if file.endswith(".tiff"):
        split_file = file.split(".")
        name = split_file[0] + ".jpeg"
        im = Image.open(path + file).convert("RGB")
        im.resize((600, 400)).save("./supplier-data/images/" + name, "JPEG")
