const twoSum = function(nums, target) {
    const pairIdx = {};
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (target - num in pairIdx) {
            return [i, pairIdx[target - num]];
        }
        pairIdx[num] = i;
        console.log(pairIdx)
    }
};
console.log(twoSum([3,2,4],6))