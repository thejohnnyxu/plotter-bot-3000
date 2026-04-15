from skimage.measure import find_contours
import numpy as np

def generate_contours(field, levels):
    thresholds = np.linspace(field.min(), field.max(), levels)
    contours = []
    for threshold in thresholds:
        contours.extend(find_contours(field, threshold))
    return contours
    