def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        print("This is i: {}:".format(i))
        key = arr[i]
        print("This is key {}".format(key))
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]: # While key is less than to the number to its left
            print("This is j: {} and arr[j]: {}".format(j, arr[j]))
            arr[j + 1] = arr[j] # Swap values
            print("This is arr[j+1]: {}".format(arr[j+1]))
            j -= 1
            print("This is j: {}".format(j))
        arr[j + 1] = key
        print("This is arr[j + 1]: {}".format(arr[j+1]))
    print(arr)

insertionSort([12, 11, 13, 5, 6])