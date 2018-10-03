from it3105.abc import Dataset
from itertools import product


class SymmetricVectors(Dataset):
    """
    Generates symmetric bit vectors
    """

    def __init__(self, len):
        self.len = len

    @staticmethod
    def symmetric(v):
        return sum(v) % 2

    def bitvec(self, n):
        return [1 if digit == '1' else 0 for digit in format(n, '0={}b'.format(self.len))]

    def nth_case(self, n):
        v = self.bitvec(n)

        if n % 2:
            i = 0

            while self.symmetric(v):
                v = self.bitvec(self.size + n + i)
                i += 1

            return (v, [1, 0])
        else:
            a = v[:self.len//2]
            if self.len % 2:
                b = a + [v[self.len//2+1]] + a[::-1]
            else:
                b = a + a[::-1]

            return (b, [0, 1])

    @property
    def size(self):
        return 2000


symmetric_vec = SymmetricVectors(101)
