def positive_sum(arr):
    totalSum = 0
    for a in arr:
        if a > 0:
            totalSum += a
    return totalSum
