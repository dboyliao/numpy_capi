from mylib import cos_double, print_strs
import numpy as np

print_strs([b"Hello", b"my friend"])
print_strs(np.array(["Hello", "my friend"], dtype=np.character))
print(cos_double(range(10)))
