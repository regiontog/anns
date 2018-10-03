from it3105.abc import Dataset
from itertools import product


class AllPairityCases(Dataset):
    """
    Produce a list of pairs, with each pair consisting of a num_bits bit pattern and a singleton list containing
    the parity bit: 0 => an even number of 1's, 1 => odd number of 1's.  When double=True, a 2-bit vector is the
    target, with bit 0 indicating even parity and bit 1 indicating odd parity.
    """

    def __init__(self, len):
        self.len = len

    @staticmethod
    def parity(v):
        return sum(v) % 2

    def bitvec(self, n):
        return [1 if digit == '1' else 0 for digit in format(n, '0={}b'.format(self.len))]

    def nth_case(self, n):
        v = self.bitvec(n)
        return (v, [1, 0] if self.parity(v) else [0, 1])

    @property
    def size(self):
        return 2**self.len


parity_cases = AllPairityCases(10)
