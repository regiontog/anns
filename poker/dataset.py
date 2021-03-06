from it3105.abc import Dataset
from os import path
import csv
import random


def bitvec(n):
    return [1 if n == m else 0 for m in range(10)]


class WineDataset(Dataset):
    def __init__(self, path):
        with open(path) as f:
            data = [row for row in csv.reader(
                f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)]

            random.shuffle(data)
            self.samples = [row[:-1] for row in data]
            self.labels = [bitvec(row[-1]) for row in data]

    def nth_case(self, n):
        return self.samples[n], self.labels[n]

    @property
    def size(self):
        return len(self.samples)


wine = WineDataset(path.join(path.dirname(__file__),
                             'poker/poker-hand-training-true.data'))
