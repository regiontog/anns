from it3105.abc import Dataset
from itertools import product

import math




class AutoencodeBitvector(Dataset):
    def __init__(self, len):
        self.len = len

    def bitvec(self, n):
        return [1 if n == m else 0 for m in range(self.len)]

    #def bitvec(self, n):
    #    return [1 if digit == '1' else 0 for digit in format(n, '0={}b'.format(self.len))]

    def nth_case(self, n):
        v = self.bitvec(n % self.len)
        return (v, v)

    @property
    def size(self):
        return self.len * 100 # 2**self.len


def factoradic(n):
    factors = []
    i = 0

    while n != 0:
        if len(factors) <= i:
            factors.append(0)

        n, factors[i] = divmod(n, i + 1)
        i += 1

    return list(reversed(factors))


def nth_permutation(n, list):
    factors = factoradic(n)
    factors = [0] * (len(list) - len(factors)) + factors

    return [list[i] for i in factors]


class DenseAutoencodeBitvector(Dataset):
    def __init__(self, denseness, len):
        self.len = len

        num_ones = int(len*denseness)
        num_zeroes = self.len - num_ones

        self.base_case = [0] * num_zeroes + [1] * num_ones

    def bitvec(self, n):
        return [1 if digit == '1' else 0 for digit in format(n, '0={}b'.format(self.len))]

    def nth_case(self, n):
        v = nth_permutation(n, self.base_case)

        return (v, v)

    @property
    def size(self):
        return math.factorial(self.len)


autoencode = AutoencodeBitvector(8)
autoencode_dense = DenseAutoencodeBitvector(0.7, 8)
