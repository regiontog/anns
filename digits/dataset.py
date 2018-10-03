"""
Requires python-mnist
https://pypi.org/project/python-mnist/
"""

from it3105.abc import Dataset
from itertools import product

from mnist import MNIST
from os import path


def bitvec(n):
    return [1 if n == m else 0 for m in range(10)]


class MNISTDataset(Dataset):
    def __init__(self, path):
        self.mndata = MNIST(path)
        self.images, self.labels = self.mndata.load_training()

    def nth_case(self, n):
        return self.images[n], bitvec(self.labels[n])

    @property
    def size(self):
        return len(self.images)


mnist = MNISTDataset(path.join(path.dirname(__file__), "mnist"))
