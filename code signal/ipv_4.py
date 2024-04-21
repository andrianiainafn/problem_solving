def solution(inputString):
    s = inputString.split(".")
    print(len(s))
    if len(s) !=4 :
        return  False
    for i in s :
        if not i.isdigit() :
            return False
        if i.startswith('0'):
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True


if __name__ == "__main__":
    print(solution("1.1.1.1.1"))
