groceries = {}

# want to store dict as number of times input, item



while True:
    try:
        item = input(":")
        item = item.lower()
        if item in groceries:
            groceries[item] = groceries[item] + 1
        else:
            groceries[item] = 1
    except EOFError:
        for _ in sorted(groceries):
            print(groceries[_], _)
        break
        