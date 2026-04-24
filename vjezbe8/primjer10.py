import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# --- OVO MORAŠ DODATI DA BI DEFINISAO red_channel ---
img = np.array(Image.open('python.jpg')) # Provjeri da li se fajl zove slika.jpg
red_channel = img[:, :, 0]
# --------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Puni raspon boja (standardno)
axes[0].imshow(red_channel, cmap="gray")
axes[0].set_title("Puni raspon (0-255)")

# Sužavanje na 50-200 (veći kontrast)
axes[1].imshow(red_channel, cmap="gray", clim=(50, 200))
axes[1].set_title("clim=(50, 200)")

# Ekstremno sužavanje (ističu se samo specifični tonovi)
axes[2].imshow(red_channel, cmap="gray", clim=(100, 180))
axes[2].set_title("clim=(100, 180)")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()