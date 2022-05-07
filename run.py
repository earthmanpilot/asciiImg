from process import Converter
import numpy as np
from PIL import Image
from pathlib import Path
from load import load_image


img_path = "data/f9_rocket.jpg"  #  'data/cat.webp'
img = Image.open(img_path)
img_np = np.array(img)

img_np = load_image(
    "https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max"
)


c = Converter(img_np)
c.ascii_print()
# print(c)
