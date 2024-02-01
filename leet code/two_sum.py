from typing import List


def solution(nums, target):
    j = 0
    a = 0
    while j < len(nums):
        for i in range(len(nums) - 1):
            if i != j:
                a = nums[i] + nums[j]
            if a == target:
                return [i, j]
        j += 1
    return [0, 0]


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = dict()
    for index, value in enumerate(nums):
        pairValue = target - value
        if pairValue in seen:
            return [seen[pairValue], index]
        seen[value] = index


if __name__ == '__main__':
    print(solution([3, 2, 4], 6))
    print(twoSum([3, 2, 4], 6))