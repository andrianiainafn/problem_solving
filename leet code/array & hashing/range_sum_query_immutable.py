from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        num = [0] * (right + 1)
        for i in range(left, right + 1):
            num[i] = self.nums[i]
        pre = [0] * len(num)
        pre[0] = num[0]
        for i in range(1, len(num)):
            pre[i] = num[i] + pre[i - 1]
        return pre[-1]


if __name__ == '__main__':
    input = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    obj = NumArray(input[0][0])
    for i in range(1, len(input)):
        print(obj.sumRange(input[i][0], input[i][1]))
