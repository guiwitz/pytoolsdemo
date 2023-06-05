from .utils import gaussian

def double_gaussian(x, mu1, sigma1, mu2, sigma2):
    return gaussian(x, mu1, sigma1) + gaussian(x, mu2, sigma2)