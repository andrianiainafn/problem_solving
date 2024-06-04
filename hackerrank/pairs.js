function pairs(k, arr) {
    //brute force
    let l = arr.length
    arr.sort((a,b)=>a-b)
     let c = 0
    for (let i = 0; i < l; i++) {
        for (let j = 0; j < l; j++) {
            if (arr[i]-arr[j] == k){
                c++
            }
        }
    }
    return c

    //optimal solution

}
console.log(pairs(2,[1, 5, 3, 4, 2]))