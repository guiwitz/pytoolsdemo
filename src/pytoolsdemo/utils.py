import numpy as np

def gaussian(x, mu, sigma):

    x = np.array(x)
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))