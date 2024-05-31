def binarySearch(arr,target):
    l, r = 0, len(arr) - 1
    while (l <= r):
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target :
            r = m - 1
        else:
            return m
    return -1


if __name__ == '__main__':
    print(binarySearch([-1,0,3,5,9,12],9))
