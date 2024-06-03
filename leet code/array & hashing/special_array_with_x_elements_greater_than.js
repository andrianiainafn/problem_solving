const specialArray = function(nums) {
    nums.sort((a,b)=> a-b)
    let l= 0
    let r= nums.length
    let x= 1
    if(nums.length == 1 && nums[0] !=0 ){
        return 1
    }
   while (l < r){
       if(nums[l] >= x && x == r-l){
           return x
       }
        else if(nums[l] >= x && x != r-l){
           x++
       }
       if (nums[l]<x){
           l++
       }

   }
    return -1
};

console.log(specialArray([3,5]))