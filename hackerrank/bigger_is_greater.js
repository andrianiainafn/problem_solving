function biggerIsGreater(w) {
    w = w.split('')
    let len = w.length
    let i = len -1
    while (i>0 && w[i-1]>=w[i]){
        i--
    }
    if (i===0){
        return 'no answer'
    }
    let j = len-1
    while ( w[j] <= w[i-1] ){
        j--
    }
    let temp = w[j]
    w[j] = w[i-1]
    w[i-1]= temp
    let start = i
    let end = len -1
    while (start< end){
        let temp = w[start]
        w[start] = w[end]
        w[end]= temp
        start++
        end--
    }
    return w.join('')
}

console.log(biggerIsGreater('dkhhhc'))

//FIRST SOLUTION
// function biggerIsGreater(w) {
//     let tw = w.split('')
//     let res = ''
//     for (let i = tw.length-1; i >0; i--) {
//         if(tw[i].charCodeAt(0) > tw[i-1].charCodeAt(0)){
//             let temp = tw[i]
//             tw[i] = tw[i-1]
//             tw[i-1]= temp
//             if (i-1!== 0){
//                 return tw.join('')
//             }
//         }
//     }
//     tw  = tw.sort()
//     let index = tw.indexOf(w.charAt(0)) + 1
//     let f  = tw[index]
//     if (f === undefined){
//         return  'no answer'
//     }
//     tw.splice(index,1)
//     res = f + tw.join('')
//     return w.charAt(0)< res.charAt(0) ? res : 'no answer'
//
// }