def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):

        money = amount[i] * 100
        cur = seller[i]

        while money > 0 and cur != "-":

            total[cur] += money - money // 10
            cur = parent[cur]
            money //= 10

    return [total[name] for name in enroll]
