function compareTriplets(a, b) {
    let sa=0
    let sb=0
    for (let i = 0; i < 3; i++) {
        if(a[i] > b[i]){
            sa++
        }else if(a[i] < b[i]){
            sb++
        }
    }
    return[sa,sb]
}
console.log(compareTriplets([1, 2, 3],[3, 2, 1]) )