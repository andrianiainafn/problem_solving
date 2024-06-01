function diagonalDifference(arr) {
    let leftDiag=0
    let rightDiag =0
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (i== j){
                leftDiag += arr[i][j]
            }
            if(i+j == arr.length -1){
                rightDiag += arr[i][j]
            }
        }
    }
    return rightDiag > leftDiag? (rightDiag - leftDiag)  : (leftDiag - rightDiag)
}
console.log(diagonalDifference([[1 ,2 ,3],[4,5,6],[9,8,9 ]]))