def permute(a,b,c):
    if  a > c :
        temp = a
        a = c
        c= temp
    if b > c :
        temp = c
        c = b
        b = temp
    if a > b :
        temp = a
        a = b
        b = temp
    print(a,b,c)
if __name__ == '__main__':
    permute(3,1,2)