from collections import Counter

def intersection(arrays):
    count = 0
    inter = []

    for i in arrays:
        if isinstance(i, list):
            arr1 = Counter(i)
            count += 1
            inter.append(arr1)

    result = Counter()

    ans = []
    for i in inter:
        result += i

    for (key, value) in result.items():
        if value == count:
            ans.append(key)

    return ans


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))