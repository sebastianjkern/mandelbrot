# %%
# Calculate the mandelbrot set

ITERATIONS_PER_PIXEL = 100

WIDTH = int(1920 / 2)
HEIGHT = int(1200 / 2)

palette = [(255 / ITERATIONS_PER_PIXEL * x, 0, 0) for x in range(ITERATIONS_PER_PIXEL)]

import numpy as np

image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

for i in range(WIDTH):
    for ii in range(HEIGHT):
        x0 = (3.5 / WIDTH) * int(i) - 2.5
        y0 = (2 / HEIGHT) * int(ii) - 1

        iteration = 0

        x = 0
        y = 0

        while iteration < ITERATIONS_PER_PIXEL and x*x + y*y <= 2*2:
            xTemp = x*x - y*y + x0
            y = 2*x*y + y0
            x = xTemp
            iteration += 1

        if len(palette)-1 < iteration:
            color = (255, 0, 0)
        else:
            color = palette[iteration]
        image[ii, i] = color

from PIL import Image
im = Image.fromarray(image, mode="RGB")
im.show()
im.save("mandelbrot.png")

# %%
