"""Run mandelbrot.sql in SQLite and color the result with smooth (continuous) iteration count."""
import sqlite3
import sys
import time

import numpy as np
from PIL import Image

W, H, SS = 960, 540, 2          # output size and supersampling factor
X0, X1 = -2.62, 1.18            # real axis
Y0, Y1 = -1.06875, 1.06875      # imaginary axis (keeps the 16:9 aspect)
MAX_ITER = 200

sql = open("mandelbrot.sql", encoding="utf-8").read()
w, h = W * SS, H * SS
t = time.time()
rows = sqlite3.connect(":memory:").execute(
    sql, {"w": w, "h": h, "x0": X0, "x1": X1, "y0": Y0, "y1": Y1, "max_iter": MAX_ITER}
).fetchall()
print(f"{len(rows):,} pixels in {time.time() - t:.1f}s", file=sys.stderr)

a = np.array(rows, dtype=np.float64)
i, j, n, r2 = a[:, 0].astype(int), a[:, 1].astype(int), a[:, 2], a[:, 3]
inside = n >= MAX_ITER
# nu = n + 1 - log2(log|z_n|)
nu = np.where(inside, 0.0, n + 1 - np.log2(np.log(np.sqrt(np.maximum(r2, 1.0001)))))

# palette: GitHub-dark background -> night blue -> teal -> gold -> ivory near the boundary
stops = np.array([
    [0.00, 13, 17, 23], [0.30, 20, 34, 70], [0.55, 28, 120, 150],
    [0.75, 236, 190, 90], [0.90, 252, 244, 222], [1.00, 255, 255, 255],
])
s = np.clip((np.log(np.maximum(nu, 2.2)) - np.log(2.2)) / (np.log(60) - np.log(2.2)), 0, 1)
rgb = np.stack([np.interp(s, stops[:, 0], stops[:, k]) for k in (1, 2, 3)], axis=1)
rgb[inside] = (13, 17, 23)

img = np.zeros((h, w, 3), dtype=np.float64)
img[h - 1 - j, i] = rgb
img = img.reshape(H, SS, W, SS, 3).mean(axis=(1, 3))
Image.fromarray(img.clip(0, 255).astype(np.uint8)).save("../assets/mandelbrot.png", optimize=True)
