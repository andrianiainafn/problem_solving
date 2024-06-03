function staircase(n) {
    for (let i = 0; i < n; i++) {
        let j = i
        let k  = n-i-1
        console.log(k)
        while (k>0){
            process.stdout.write(" ");
            k--
        }
        while (j >= 0){
            process.stdout.write("#");
            j--
        }
        console.log()
    }
}

staircase(6)