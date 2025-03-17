def merge(nums1, m, nums2, n):
    nums1 = [nums1[i] for i in range(0, m)]
    for i in range(0, n):
        nums1.append(nums2[i])
    nums1.sort()
    return nums1

if __name__ == '__main__':
    print(merge([1,2,3,0,0,0],3,[2,5,6],3))
    print(merge([0],0,[1],1))