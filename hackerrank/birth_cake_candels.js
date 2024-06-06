function birthdayCakeCandles(candles) {
    const max = Math.max(...candles)
    let c=0
    for (let i = 0; i < candles.length; i++) {
        if (candles[i]===max){
            c++
        }
    }
    return c
}
console.log(birthdayCakeCandles([3,2,1,3]))