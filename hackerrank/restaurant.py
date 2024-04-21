def solution(l, b):
    a=l
    c=b
    while b :
        l,b = b, l % b
    pgcd = l
    a = a // pgcd
    c = c // pgcd
    return a*c

if __name__ == "__main__":
    print(solution(6, 9))
