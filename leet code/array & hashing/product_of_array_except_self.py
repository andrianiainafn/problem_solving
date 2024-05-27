def productExceptSelf(nums):
    pre = [0] * len(nums)
    pre[0] = nums[0]
    suf = [0] * len(nums)
    suf[-1] = nums[-1]
    res=[0]*len(nums)
    for i in range(1, len(nums)):
        pre[i] = pre[i - 1] * nums[i]
    for i in range(len(nums)-2,-1,-1):
        suf[i] = suf[i+1] * nums[i]
    for i in range(len(nums)):
        if i == 0 :
            res[i] = 1 * suf[i + 1]
        elif i == len(nums) - 1 :
            res[i] = pre[i - 1] * 1
        else:
            res[i] = pre[i - 1] * suf[i + 1]

    return nums,suf,pre,res
def productExceptSelf2(nums):
    pre= 1
    res=[1]*len(nums)
    suf=1
    for i in range(len(res)):
        res[i] = pre
        pre *= nums[i]
    for i in range(len(res)-1,-1,-1):
        res[i] *= suf
        suf *= nums[i]
    return res


if __name__ == '__main__':
    print(productExceptSelf2([1,2,3,4]))
    print(productExceptSelf2([-1,1,0,-3,3]))