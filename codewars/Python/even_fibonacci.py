def even_fib(n):
    ant, suc = 0, 2
    total = 0

    while ant < n:
        total += ant
        ant, suc = suc, 4*suc + ant

    return total
