import copy


def isPalindrome(s:str):
    s = ''.join([char.lower() for char in s if char.isalpha() or char.isnumeric()])
    cp = ([char.lower() for char in s if char])
    cp.reverse()
    return ''.join(cp) == s
    # cop = copy.copy(s)
    # s =  list(s)
    # j = len(s) - 1
    # while i < j:
    #     i+=1
    #     j-=1
    #     swap(s,i,j)
    # print(''.join(s))
    # print(''.join(cop))
    # return ''.join(s) == ''.join(cop)


def swap(s, i, j):
    temp= s[i]
    s[i] = s[j]
    s[j] = temp

if __name__ == '__main__':
    print(isPalindrome("0P"))
