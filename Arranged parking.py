def minfuel(x,y):
    num = len(x)
    if num  == 1:
        return 0
    ans = float("inf")
    for i in range(num):
        tempx = x[i]
        tempy = y[i]
        distance = 0
        cnt = -1
        count = num - 1
        for j in range(num):
            if j != i:
                distance += (abs(tempx-x[j]) + abs(tempy-y[j]))
            if tempx == x[j]:
                cnt += 1
        count -= cnt
        distance -= minus(count,cnt)
        distance += add(cnt)
        ans = min(distance,ans)
    return ans

def minus(x,y):
    a = y // 2
    time = y % 2
    a += 1 
    res = 0
    for _ in range(x):
        res += a
        time += 1
        if time == 2:
            a += 1
            time = 0
    return res

def add(x):
    a = 1 
    res = 0
    time = 0
    for _ in range(x):
        res += a
        time += 1
        if time == 2:
            a += 1
            time = 0
    return res


x = list(map(int,input().split()))
y = list(map(int,input().split()))

print(minfuel(x,y))

