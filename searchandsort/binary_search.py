
def binarySearch(arr, item):
    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end)//2

        if arr[midpoint] == item:
            found = True
        
        if item > arr[midpoint]:
            start = midpoint + 1
        if item < arr[midpoint]:
            end = midpoint - 1

    return found


if __name__ == "__main__":
    arr1 = [1, 6, 10, 22, 40]
    print(binarySearch(arr1, 10))
