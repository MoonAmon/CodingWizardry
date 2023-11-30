def exp_sum(n):
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            p[j] += p[j - i]
    print(p)
    return p[n]

exp_sum(50)