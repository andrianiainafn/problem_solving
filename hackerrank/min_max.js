function miniMaxSum(arr) {
    arr.sort()
    let len = arr.length
     const min = arr.reduce((acc,crr,index)=>{
        if (index === len - 1) {
            return acc;
        } else {
            return acc + crr;
        }
    },0)
    const max = arr.reduce((acc,crr,index)=>{
        if (index === 0) {
            return acc;
        } else {
            return acc + crr;
        }
    },0)
    console.log(min,max)
}
miniMaxSum([1,2,3,4,5])

