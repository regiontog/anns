from it3105.abc import Dataset
from itertools import product

import random
import numpy as np


def gen_random_pieces(chunk_size, num_pieces):
    if num_pieces == 1:
        return [chunk_size]
    else:
        # the pts at which to cut up the chunk
        cut_points = list(np.random.choice(
            range(1, chunk_size), num_pieces-1, replace=False))
        lastloc = 0
        pieces = []
        cut_points.sort()  # sort in ascending order
        cut_points.append(chunk_size)
        for pt in cut_points:
            pieces.append(pt-lastloc)
            lastloc = pt
        return pieces


def gen_segment_locs(maxlen, seg_sizes):
    locs = []
    remains = sum(seg_sizes)
    gaps = len(seg_sizes) - 1
    start_min = 0

    for ss in seg_sizes:
        space = remains + gaps
        if start_min == maxlen - space + 1:
            break
        else:
            start = np.random.randint(start_min, maxlen - space + 1)

        locs.append(start)
        remains -= ss
        start_min = start + ss + 1
        gaps -= 1

    return locs


class SegmentedVectors(Dataset):
    def __init__(self, bitlen, n, minseg, maxseg):
        self.bitlen = bitlen
        self.n = n
        self.minseg = minseg
        self.maxseg = maxseg

    def numvec(self, n):
        return [1 if n == m else 0 for m in range(self.maxseg)]

    @staticmethod
    def num_chunks(l):
        chunks = "".join(map(str, l)).split('0')
        return sum(1 if x else 0 for x in chunks)

    def nth_case(self, n):
        """
        NOTE: This function is not pure, and may return the same result for two different inputs.
        This means that two equal cases might end up in both the training and the testing data when split.
        """

        num_segs = random.randint(self.minseg, self.maxseg)

        v = [0] * self.bitlen

        if num_segs > 0:
            min_gaps = num_segs - 1
            max_chunk_size = self.bitlen - min_gaps
            min_chunk_size = num_segs
            chunk_size = random.randint(min_chunk_size, max_chunk_size+1)
            seg_sizes = gen_random_pieces(chunk_size, num_segs)
            seg_start_locs = gen_segment_locs(self.bitlen, seg_sizes)

            for s0, size in zip(seg_start_locs, seg_sizes):
                v[s0:s0+size] = [1] * size

        return (v, self.numvec(self.num_chunks(v)))

    @property
    def size(self):
        return self.n


summed_bitvectors = SegmentedVectors(25, 10000, 0, 8)
