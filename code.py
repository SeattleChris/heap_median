#!/bin/python3

import os
from heapq import heappush as happend, heappushpop as htrade

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(arr):
    hi, lo, bal, result = [], [arr[0] * -1], -1, [arr[0]]
    for val in arr[1:]:
        target = lo[0] * -1
        if bal > 0 and val > target:  # val goes on overfull hi
            happend(lo, -1 * htrade(hi, val))
            bal -= 1
        elif val > target:
            happend(hi, val)
            bal += 1
        elif bal < 0:  # val goes on overfull lo
            happend(hi, -1 * htrade(lo, val * -1))
            bal += 1
        else:
            happend(lo, val * -1)
            bal -= 1
        med = hi[0] if bal > 0 else lo[0] * -1
        if bal == 0:
            med = (med + hi[0]) / 2
        result.append(f"{med:.1f}")
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)
    result = runningMedian(a)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
