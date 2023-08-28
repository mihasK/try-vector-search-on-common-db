import numpy as np

def cos_dist(e1,e2):
    return 1 - np.dot(e1,e2) / np.sqrt(np.dot(e1,e1) * np.dot(e2, e2))
