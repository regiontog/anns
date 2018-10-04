from it3105.abc import Dataset
from os import path
import csv
import math


def bitvec(n):
    return [1 if n == m else 0 for m in range(6)]


def mean(vec):
    return sum(vec) / len(vec)


def std_deviation(vec, mean):
    return math.sqrt((1 / (len(vec) - 1)) * sum([(x - mean) ** 2 for x in vec]))


def normalize(samples):
    feature_factors = []
    for i in range(len(samples[0])):
        feature_column = [vec[i] for vec in samples]
        fmean = mean(feature_column)
        fsdev = std_deviation(feature_column, fmean)
        feature_factors.append((fmean, fsdev))

    for i in range(len(samples)):
        samples[i] = [(samples[i][j] - feature_factors[j][0]) /
                      feature_factors[j][1] for j in range(len(feature_factors))]

    return samples


class WineDataset(Dataset):
    def __init__(self, path):
        with open(path) as f:
            data = [row for row in csv.reader(
                f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)]

            self.samples = [row[:-1] for row in data]
            self.labels = [bitvec(row[-1]) for row in data]

    def nth_case(self, n):
        return self.samples[n], self.labels[n]

    @property
    def size(self):
        return len(self.samples)


wine = WineDataset(path.join(path.dirname(
    __file__), 'wine/winequality_red.txt'))
