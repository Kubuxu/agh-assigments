import numpy as np
from multiprocessing import Pool

class Histogram:
    def __init__(self, buckets):
        self.buckets = buckets
        self.data = [0]*(len(buckets)+1)

    def addSample(self, sample):
        k = 0
        for b in self.buckets:
            if sample < self.buckets[k]:
                break
            k+=1

        self.data[k] += 1

    def combine(self, val):
        assert(self.buckets == val.buckets)
        for i in range(len(self.data)):
            self.data[i] += val.data[i]


# 64Mi samples
arr = np.random.standard_normal(64 * 2**20)/7+0.5

histBuckets = [0.1*n for n in range(1, 10)]

threads = 8
stride = len(arr)//threads
tasks = list(zip(range(0, len(arr), stride), range(stride, len(arr)+stride, stride)))

def do_calc(task):
    print("Startng task")
    hist = Histogram(histBuckets)
    for i in range(*task):
        hist.addSample(arr[i])
    return hist


with Pool(threads) as pool:
    outHist = Histogram(histBuckets)
    out_it = pool.imap_unordered(do_calc, tasks)

    for res in out_it:
        outHist.combine(res)

    print(outHist.data)



