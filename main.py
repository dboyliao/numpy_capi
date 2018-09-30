from mylib import cos_double, print_strs, to_gray
import numpy as np
from PIL import Image

print_strs([b"Hello", b"my friend"])
print_strs(np.array(["Hello", "my friend"], dtype=np.character))
print(cos_double(range(10)))

color_img = np.array(Image.open('color_img.jpg').convert('RGB'))
gray_img = Image.fromarray(to_gray(color_img))

gray_img.save('gray.png')
