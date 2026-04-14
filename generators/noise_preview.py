import numpy as np

# field here is literally the variable name, not a first class thing in numpy
def noise_to_image(field: np.ndarray):
    field = field + 1
    # the insutrction was very literal, literally how does it go from 0,2 to 0,255 -- so you multipy by 255/2
    field = field * 127.5
    # converts to int
    field = field.astype(np.uint8)
    return field