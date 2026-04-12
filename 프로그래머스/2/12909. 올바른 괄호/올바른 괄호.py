def solution(s):
    stack = []
    new_s = list(map(str, s.strip()))
    result = False
    for c in new_s:
        # 빈 왼, 빈 오, 찬 왼, 찬 오
        if not stack:
            stack.append(c)
            if c == ")":
                break
        else:
            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    break
            else:
                stack.append(c)
    
    return result if stack else not result