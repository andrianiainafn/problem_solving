function valid_sudoku(board){
    let cols = {}
    let rows = {}
    let square = {}
    for (let i = 0; i < 9; i++){
        for (let j = 0; j < 9; j++){
            if(board[i][j] === '.'){
                continue
            }
            if(!cols[j]) {
                cols[j] = new Set()
            }
            if(!rows[i]) {
                rows[i] = new Set()
            }if (!square[`${Math.floor(i / 3)}-${Math.floor(j / 3)}`]){
                square[`${Math.floor(i / 3)}-${Math.floor(j / 3)}`] = new Set()
            }
            if (cols[j].has(board[i][j]) || rows[i].has(board[i][j]) || square[`${Math.floor(i / 3)}-${Math.floor(j / 3)}`].has(board[i][j])){
                return  false
            }
            cols[j].add(board[i][j])
            rows[i].add(board[i][j])
            square[`${Math.floor(i / 3)}-${Math.floor(j / 3)}`].add(board[i][j])
        }
    }
    return  true

}
console.log(valid_sudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))


// row = {}
// col = {}
// sub = {}
// for (let i = 0; i < 9; i++) {
//     for (let j = 0; j < 9; j++){
//         if(board[i][j] in row && board[i][j] !== '.'){
//             row[board[i][j]]  += 1
//         }else{
//             row[board[i][j]] = 0
//         }
//     }
//
// }
// const sub_list = Array.from({ length: 9 }, () => ({ set: new Set(), dot: 0 }));
//      for (let i=0; i<9; i++){
//         const row = new Set()
//         const col = new Set()
//         let col_dot =0
//         let row_dot = 0
//         for (let j=0; j<9; j++){
//             if(board[i][j] === '.'){
//                 row_dot++
//             }else{
//                 row.add(board[i][j])
//             }
//             if(board[j][i] === '.'){
//                 col_dot++
//             }else{
//                 col.add(board[j][i])
//             }
//         }
//         if (row.size !== 9-row_dot || col.size !== 9-col_dot){
//             return false
//         }
//     }