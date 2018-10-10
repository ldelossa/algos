from collections import defaultdict


def pairSum1(arr, k):
    if len(arr) < 2:
        return
    arr.sort()

    left, right = (0, len(arr) - 1)
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == k:
            print(arr[left], arr[right])
            left += 1
        elif currentSum < k:
            left += 1
        else:
            right -= 1


def pairSum2(arr, k):
    seen = defaultdict(bool)
    output = {}

    for i in range(0, len(arr)):
        target = k - arr[i]

        if not seen[target]:
            seen[arr[i]] = True
        else:
            # add pair to output hash to eliminate dupliate output
            pair = (min(target, arr[i]), max(target, arr[i]))
            output[pair] = "_"

    for kk in output:
        print("Found pair {} that sums to {}".format(kk, k))


if __name__ == "__main__":
    arr = [1, 3, 4, 10, 2, 4, 3, 2]
    s = 5
    pairSum2(arr, s)
