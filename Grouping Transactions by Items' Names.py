def groupTransactions(transactions):
    dic = {}
    for i in transactions:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = list(sorted(dic.items(), key = lambda x : x[0]))
    dic = list(sorted(dic, key = lambda x : x[1], reverse = True))

    ans = []
    
    for k,v in dic:
        ans.append(str(k)+' '+str(v))
    return ans


count = int(input())
transactions = []
for _ in range(count):
    item = input()
    transactions.append(item)

print('\n'.join(groupTransactions(transactions)))

