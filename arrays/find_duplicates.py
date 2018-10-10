
def find_duplicates(arr, n):

    for i in range(0, n):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
            print(arr)
        else:
            print (abs(arr[i]))

if __name__ == "__main__":
    arr = [1, 2, 1, 2]
    arr_size = len(arr)

    find_duplicates(arr, arr_size)
