const isValid = function(s) {
    let stack = []
    for (let i = 0; i < s.length; i++) {
        if(s[i] === '{' || s[i] === '(' || s[i] === '['){
            stack.unshift(s[i])
        }else{
            if( (s[i]==']' && stack[0] == '[') || (s[i]== '}' && stack[0] == '{') || (s[i] == ')' && stack[0] == '(') ){
                stack.shift()
            } else{
                console.log(s[i],stack[0])
                return  false
            }
        }
    }
    return stack.length === 0
};

console.log(isValid('{(([])[])[]}[]'))
// console.log(isValid('{(([])[])[]}[]'))