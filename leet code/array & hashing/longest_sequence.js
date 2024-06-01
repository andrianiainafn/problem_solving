const longest_sequence = (nums)=>{
    let max =  0
    let cur = 1
    let num =  nums.sort((a, b) => a - b);
    num = [...new Set(num)]
    for (let i = 0; i < num.length; i++) {
        diff =  num[i+1] - num[i]
        if(cur > max){
            max = cur
        }
        if(diff > 1 ){
            cur = 1
        }else{
            cur++
        }
    }
    return max
}

console.log(longest_sequence([100,4,200,1,3,2]))
console.log(longest_sequence([0,3,7,2,5,8,4,6,0,1]))
console.log(longest_sequence([1,2,0,1]))