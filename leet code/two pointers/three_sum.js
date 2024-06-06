const threeSum = function(nums) {
    //brute force
    // let len = nums.length;
    // const res = [];
    // const seenTriplets = new Set();
    // for (let i = 0; i < len; i++) {
    //     const pairIdx = {};
    //     for (let j = i + 1; j < len; j++) {
    //         let t = -(nums[i] + nums[j]);
    //         if (t in pairIdx) {
    //             const triplet = [nums[i], nums[j], parseInt(t)];
    //             triplet.sort((a, b) => a - b);
    //             const tripletKey = triplet.join(',');
    //             if (!seenTriplets.has(tripletKey)) {
    //                 seenTriplets.add(tripletKey);
    //                 res.push(triplet);
    //             }
    //         }
    //         pairIdx[nums[j]] = j;
    //     }
    // }
    // return res;


    //optimal solution
    nums.sort((a,b)=>a-b)
    let len = nums.length;
    const res=[]
    for (let i = 0; i < len; i++) {
        if (i>=1){
            if (nums[i]===nums[i-1]){
                continue
            }
        }
        let l = i+1
        let r = len-1
        while (l<r){
            let sum = nums[i] + nums[r] + nums[l]
            if (sum > 0 ){
                r--
            }
            else if (sum < 0){
                l++
            }
            else {
              res.push([nums[i] ,nums[r] , nums[l]])
              l++
              while (nums[l] === nums[l-1] && l<r){
                  l++
              }
            }
        }
    }
    return res
};
console.log(threeSum([-2,0,1,1,2]))