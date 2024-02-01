def solution(s):
    start = 0
    last = 0
    for i in range(len(s) - 1):
        if (s[i] == '{' and s[i + 1] == '}') or (s[i] == '[' and s[i + 1] == ']') or (s[i] == '(' and s[i + 1] == ')'):
            last = i + 1
            start = i
            print(str(last) + " " + str(start))
            break
    j = 0
    if last == 0 and last == 0:
        return "No"
    while j > len(s) // 2:
        if start - 1 != last + 1:
            return "NO"
        j += 1
    return "YES"


def solution2(s):
    l = {'{': 0, '}': 0, '[': 0, ']': 0, '(': 0, ')': 0}
    for i in range(len(s) - 1):
        if s[i] == ')' or s[len(s)-1] == ')':
            l[')'] += 1
        if s[i] == '{' and (s[i + 1] == ']' or s[i + 1] == ')'):
            return "NO"
        elif s[i] == '[' and (s[i + 1] == ')' or s[i + 1] == '}'):
            return "NO"
        elif s[i] == '(' and (s[i + 1] == ']' or s[i + 1] == '}'):
            return "NO"
    for i in s:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    if l['['] != l[']'] or l['{'] != l['}'] or l['('] != l[')']:
        return "NO"
    return "YES"


if __name__ == "__main__":
    print(solution2("{  ( ([]) [] ) [] ]  }"))  # NO
    # print(solution("{(([])[])[]}[]")) #YES
    # print(solution2("{(([])[])[]]}")) #NO
