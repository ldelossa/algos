def largest(arr, k):
    # sor descending
    arr.sort(reverse=True)

    # print the first kth largest elements
    for i in range(k):
        print(arr[i])


def smallest(arr, k):
    # sor descending
    arr.sort()

    # print the first kth largest elements
    for i in range(k):
        print(arr[i])


arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(largest(arr, k))
print(smallest(arr, k))
