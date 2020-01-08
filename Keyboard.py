def entryTime(s,keypad):
    phone = [[0] * 3 for _ in range(3)]
    trace = [[0] * 2 for _ in range(10)]

    k = 0
    for i in range(3):
        for j in range(3):
            phone[i][j] = int(keypad[k])
            trace[phone[i][j]][0] = i
            trace[phone[i][j]][1] = j
            k += 1
    ans = 0
    temp = int(s[0])
    for i in s:
        r1 = trace[temp][0]
        c1 = trace[temp][1]
        r2 = trace[int(i)][0]
        c2 = trace[int(i)][1]
        ans += max(abs(c1-c2),abs(r1-r2))
        temp = int(i)
    return ans

s = input()
keypad = input()

print(entryTime(s,keypad))

