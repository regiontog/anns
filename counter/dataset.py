from it3105.abc import Dataset
from itertools import product


class BitCounter(Dataset):
    """
    Generates symmetric bit vectors
    """

    def __init__(self, len):
        self.len = len

    def bitvec(self, n):
        return [1 if digit == '1' else 0 for digit in format(n, '0={}b'.format(self.len))]

    def nth_case(self, n):
        v = self.bitvec(n)

        return (v, [sum(v)])

    @property
    def size(self):
        return 2**self.len


summed_bitvectors = BitCounter(15)
