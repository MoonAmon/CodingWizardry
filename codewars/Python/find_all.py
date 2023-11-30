def find_all(sum_dig, digs):
    def helper(sum_dig, digs, start=1):
        if digs == 0:
            return [[]] if sum_dig == 0 else []
        if digs == 1:
            return [[sum_dig]] if start <= sum_dig <= 9 else []
        return [[i] + j for i in range(start, 10) for j in helper(sum_dig - i, digs - 1, i)]
    
    combinations = helper(sum_dig, digs)
    if not combinations:
        return []
    numbers = [int(''.join(map(str, combination))) for combination in combinations]
    return [len(numbers), min(numbers), max(numbers)]