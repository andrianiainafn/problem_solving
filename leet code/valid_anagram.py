def isAnagram(s,t):
    if len(s) != len(t):
        return False
    sl = {i: s.count(i) for i in s}
    tl = {i: t.count(i) for i in t}
    for key in sl.keys():
        if sl[key] != tl[key]:
            return False
    return True


if __name__ == '__main__':
    print(isAnagram("",""))