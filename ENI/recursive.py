def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

def sayAlgorithm(n):
    for i in  range(0,n):
        print("Algorithme")

if __name__ == '__main__':
    print(sum(5))
    sayAlgorithm(5)