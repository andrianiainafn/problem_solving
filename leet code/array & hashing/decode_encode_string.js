function decode(str){
    let res = []
    let i = 0
    while (i < str.length){
        let j=i
        while(str[j] !== '#' && j < str.length){
            j++
        }
        let len = parseInt(str.slice(i,j),10)
        console.log(j,len)
        res.push(str.slice(j+1,len+j+1))
        i = j +  len + 1
    }
    return res
}
function encode(strs){
    let res = ""
    for (let i = 0; i < strs.length; i++) {
        res += `${strs[i].length}#${strs[i]}`
    }
    return res
}
const res = encode(["neet","code","love","you"])
console.log(res)
console.log(decode(res))