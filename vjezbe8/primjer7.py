import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

img = np.asarray(Image.open("python.jpg"))

print(f"type:  {type(img)}")
print(f"shape: {img.shape}")
print(f"dtype: {img.dtype}")

plt.imshow(img)
plt.title("Python — doslovno!")
plt.axis("off")
plt.show()