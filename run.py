from process import Converter
import numpy as np
from PIL import Image



img_path = 'data/f9_rocket.jpg' #  'data/cat.webp'
img = Image.open(img_path)
img_np = np.array(img)
c = Converter(img_np)

print(c)
