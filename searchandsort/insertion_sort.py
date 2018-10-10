def insertion_sort(arr):
    # iterate over 1 thru n
    for i in range(1, len(arr)):
        # get the current value
        value = arr[i]
        # hole is used to track where our value will go
        hole = i

        while (hole > 0) and (arr[hole - 1] > value):
            # push hole-1 into hole
            arr[hole] = arr[hole - 1]
            # decrement hole
            hole = hole - 1

        # place value in hole
        arr[hole] = value

    return arr


if __name__ == "__main__":
    arr = [1, 25, 18, 192, 12, 413, 1, 13414, 43, 53]
    print(insertion_sort(arr))
