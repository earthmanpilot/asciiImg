from process import Converter

img_path = 'data/f9_rocket.jpg' #  'data/cat.webp'
img = Image.open(img_path)
img_np = np.array(img)
c = Converter(img_np)

print(c)
