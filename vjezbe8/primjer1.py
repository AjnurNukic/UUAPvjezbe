import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


# ================================================================
# DIO 1: DEMONSTRACIJA — Osnove Matplotlib
# ================================================================

# ---------------------------------------------------------------
# Primjer 1 — Import i prvi graf
# ---------------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [2, 4, 7, 11, 16]

plt.plot(x, y)
plt.title("Moj prvi graf")
plt.xlabel("X osa")
plt.ylabel("Y osa")
plt.show()
