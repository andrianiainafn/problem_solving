def solution(a):
    i=0
    n=len(a)
    if a[::-1] == a :
        return True
    while i < n :
        f = list(a)
        for j in range(len(f)-1 ) :
            temp = f[j]
            f[j] = f[j+1]
            f[j+1] = temp
            print(f)
            if f[::-1] == f :
                return True
        i+=1
    return False

def solution2(a):
    char_count = {i: list(a).count(i) for i in a}
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1


if __name__ == '__main__':
    print(solution("abccba"))