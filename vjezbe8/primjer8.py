import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# 1. DEFINIŠI 'img' (Učitaj sliku i pretvori u niz)
# Pazi da je slika u istom folderu gdje i tvoja skripta
img = np.array(Image.open('python.jpg'))

# 2. EKSTRAKCIJA CRVENOG KANALA
red_channel = img[:, :, 0]
print(f"Red channel shape: {red_channel.shape}")

# Prikaz sa 'viridis' (default) mapom boja
plt.imshow(red_channel)
plt.colorbar()
plt.title("Crveni kanal — viridis colormap")
plt.show()

# Prikaz sa 'hot' mapom boja
plt.imshow(red_channel, cmap="hot")
plt.colorbar()
plt.title("Crveni kanal — hot colormap")
plt.show()