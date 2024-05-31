function checkValid(nums){

    for (let i=0; i<nums.length; i++){
        const row = new Set()
        const col = new Set()
        for (let j=0; j<nums[i].length; j++){
            row.add(nums[i][j])
            col.add(nums[j][i])
        }
        if (row.size !== nums.length || col.size !== nums.length){
            return false
        }
    }
    return  true
}

console.log(checkValid([[1,1,1],[1,2,3],[1,2,3]]))