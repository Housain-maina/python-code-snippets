def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    total = 0
    item_1 = item_2 = 1

    for _ in range(3, n + 1):
        total = item_1 + item_2
        item_1, item_2 = item_2, total

    return total


for i in range(1, 10):
    print(i, " -> ", fib(i))
