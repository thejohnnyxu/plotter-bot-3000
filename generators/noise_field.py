import numpy as np
from noise import pnoise2

# numpy does rows first, rows at y
# scale is made up, its so we can turn ints into decimals and smaller scale numbers
# seed is a pnoise2 parameter  
def generate_noise_field(width, height, scale, seed):
    grid = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            grid[y,x] = pnoise2(y/scale, x/scale, base=seed)

    return(grid)