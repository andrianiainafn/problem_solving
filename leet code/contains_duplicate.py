from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    a = {i: nums.count(i) for i in nums}
    for c in a.values():
        if c > 1:
            return True
    return False


def containsDuplicate2(nums: List[int]) -> bool:
    a = {}
    for i in nums:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for c in a.values():
        if c > 1:
            return True
    return False


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))
