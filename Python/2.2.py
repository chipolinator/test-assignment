def missing_number(arr):

    s = 0

    for x in arr:
        s += x

    n = len(arr) + 1

    should_be = n * (n + 1) // 2

    return should_be - s


nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]

print(missing_number(nums))
