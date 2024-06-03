function plusMinus(arr) {
    let p=0
    let n = 0
    let z = 0
    const len = arr.length
    for (let i = 0; i < len; i++) {
        if (arr[i] > 0){
            p++
        }else if(arr[i]< 0){
            n++
        }else{
            z++
        }
    }
    console.log((p/len).toFixed(6))
    console.log((n/len).toFixed(6))
    console.log((z/len).toFixed(6))
}

plusMinus([1,1,0,-1,-1])