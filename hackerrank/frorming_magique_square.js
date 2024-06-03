function formingMagicSquare(s) {
    const allMagicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ];
    let minCost = Infinity;
    for (let magic of allMagicSquares) {
        let cost = 0;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                cost += Math.abs(s[i][j] - magic[i][j]);
            }
        }
        if (cost < minCost) {
            minCost = cost;
        }
    }

    return minCost;

}
console.log(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    // let c = s[1][1]
    // let a = s[2][0]-c
    // let b =c- s[0][0]
// const sum = [0,0,0,0,0,0,0,0]
// for (let i = 0; i < 3; i++) {
//     for (let j = 0; j < 3; j++) {
//         if (i==j){
//             sum[6]+=s[i][j]
//         }
//         if(i+j == 2){
//             sum[7] += s[i][j]
//         }
//         sum[i]+=s[i][j]
//         sum[j+3]+=s[j][i]
//     }
// }