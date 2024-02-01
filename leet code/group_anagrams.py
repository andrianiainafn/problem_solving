def solution(s):
    if all(element == s[0] for element in s):
        return [s]
    res = {}
    result =[]
    for i in range(len(s)):
        if s[i] not in res.keys():
            res[s[i]] = [s[i]]
        for key in res.items():
            r = isAnagram(key, s[i])
            if r:
                if s[i] not in res[key]:
                    res[key].append(s[i])
    seen_elements = set()
    for values in res.values():
        unique_values = []
        for value in values:
            if value not in seen_elements:
                unique_values.append(value)
                seen_elements.add(value)
        result.append(unique_values)
    return sorted([x for x in result if x != []],key=len)

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sl = {i: s.count(i) for i in s}
    tl = {i: t.count(i) for i in t}
    for key in sl.keys():
        if key not in tl:
            return False
        if sl[key] != tl[key]:
            return False
    return True





if __name__ == '__main__':
    print(solution(["","b",""]))
