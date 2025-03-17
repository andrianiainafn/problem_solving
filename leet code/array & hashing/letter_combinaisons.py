def letterCombinations(digits):
    if not digits:
        return []
    number = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    path=[]
    for i in digits:
        path.append(number[i])
    print(path)
if __name__ == '__main__':
    letterCombinations("23")