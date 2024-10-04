import sys

def check_ps(arr, char):
    if (char == ')' and arr[-1] == '(') or (char == ']' and arr[-1] == '['):
        return True
    else:
        return False

while True:
    str_arr = list(str(sys.stdin.readline().rstrip()))
    ps_arr = []
    isBreak = False

    if str_arr[-1] == '.' and str_arr[0] == str_arr[-1]:
        break

    for v in str_arr:
        if v == '(' or v == '[':
            ps_arr.append(v)
        elif v == ')' or v == ']':
            if ps_arr:
                temp = check_ps(ps_arr, v)

                if temp is True:
                    ps_arr.pop()
                else:
                    isBreak = True
                    break
            else:
                isBreak = True
                break

    print("no") if ps_arr or isBreak is True else print("yes")