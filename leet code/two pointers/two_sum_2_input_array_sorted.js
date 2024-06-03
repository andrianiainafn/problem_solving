const twoSum = function(numbers, target) {
    //brute force solution
    // for (let i = 0; i <numbers.length; i++) {
    //     for (let j = 0; j < numbers.length; j++) {
    //         if(i == j){
    //             continue
    //         }
    //         if (numbers[i] + numbers[j]=== target){
    //             return[i+1,j+1]
    //         }
    //     }
    // }
    // return []

    //optimal solution (binary search)
    // numbers.sort((a,b)=>a-b)
    // let n = numbers.length
    // for (let i = 0; i < n; i++) {
    //     let c = target - numbers[i]
    //     let r = n -1
    //     let l = i+1
    //     while (l<r){
    //         console.log(i,"c")
    //         let  m = Math.floor((r+l)/2)
    //         if (c == numbers[m]){
    //             return [i+1,m+1]
    //         }
    //         else if(numbers[m] < c){
    //             l = m+1
    //         }
    //         else if (numbers[m] > c){
    //             r = m-1
    //         }
    //     }
    // }

    //very optimal solution
    let  l = 0
    let r = numbers.length -1
    while (l<r){
        let t = numbers[l] + numbers[r]
        if (t===target){
            return [l+1,r+1]
        }else if (t> target){
            r--
        }else{
            l++
        }
    }
};

console.log(twoSum([2,7,11,15],9))