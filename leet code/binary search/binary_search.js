const search = function(nums, target) {
    let l = 0
    let r = nums.length-1
    while (l<=r){
        let m = Math.floor((r+l)/2)
        if (target === nums[m]){
            return m
        }
        else if (nums[m]< target){
            l= m+1
        }else if (nums[m]>target){
            r= m-1
        }
    }
    return -1
};
console.log(search([-1,0,3,5,9,12],9))