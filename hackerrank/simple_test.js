function fizzBuzz(n) {
    let i=1
    while(i<=n){
        if(( (i% 3) == 0) && ( (i % 5) == 0)){
            console.log("fizzBuzz")
        }else if(( (i% 3) !== 0) && ( (i % 5) == 0)){
            console.log("Buzz")
        } else if(( (i% 3) == 0) && ( (i % 5) !== 0)){
            console.log("Fizz")
        }else if( ( (i% 3) !== 0) || ( (i % 5) !== 0)){
            console.log(i)
        }
        i++
    }
}
fizzBuzz(15)