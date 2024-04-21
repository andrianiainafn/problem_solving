def reverse_in_parentheses(inputString):
    s = list(inputString)
    while '(' in s or ')' in s:
        start = 0
        last = 0
        for i in range(len(s)):
            if s[i] == '(':
                start = i
            if s[i] == ')':
                last = i
                s[start:last + 1] = s[start:last + 1][::-1]
                break
        del s[start]
        del s[last-1]
        print(''.join(s))


if __name__ == '__main__':
    reverse_in_parentheses("foo(bar)baz(blim)")
