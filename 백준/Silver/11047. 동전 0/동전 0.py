# 뒤에서 부터 대입해서 아니면 pop하는 식으로 k 가 0이 되면 종료 (arr[0] = 1 고정)
n, k = map(int, input().split())
arr, count = [], 0
for _ in range(n):
    arr.append(int(input()))

while k > 0:
    tmp1 = arr[-1]
    if k < tmp1:
        arr.pop()
    else:
        tmp2 = k // tmp1
        k = k % tmp1
        count += tmp2

print(count)