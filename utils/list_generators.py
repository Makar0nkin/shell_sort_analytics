import numpy as np
from utils.constants import MEAN, SCALE, SIZE


def normal_list_generator():
    return np.random.normal(loc=MEAN, scale=SCALE, size=SIZE).astype(int)


def uniform_list_generator():
    return np.random.uniform(low=-4*SCALE + MEAN, high=4*SCALE + MEAN, size=SIZE).astype(int)
