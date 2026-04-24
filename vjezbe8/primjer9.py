import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# --- DODAJ OVAJ DIO ---
# Učitaj sliku i pretvori je u niz
img = np.array(Image.open('python.jpg')) # Zamijeni sa stvarnim imenom tvoje slike
# Izdvoji crveni kanal (0 = red, 1 = green, 2 = blue)
red_channel = img[:, :, 0]
# ----------------------

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Prikaz originalne slike
axes[0].imshow(img)
axes[0].set_title("Originalna slika")
axes[0].axis("off")

# Prikaz histograma crvenog kanala
# .ravel() "ispravlja" 2D sliku u 1D niz brojeva za histogram
axes[1].hist(red_channel.ravel(), bins=range(256),
             color="red", alpha=0.7)
axes[1].set_title("Histogram crvenog kanala")
axes[1].set_xlabel("Vrijednost piksela (0-255)")
axes[1].set_ylabel("Broj piksela")

plt.tight_layout()
plt.show()