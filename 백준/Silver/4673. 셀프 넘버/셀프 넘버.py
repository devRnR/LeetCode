def self_number(a):
    num = a
    num_list = list(str(a))
    for i in num_list:
        num += int(i)

    check.append(num)


check = []

for i in range(1,10001):
    self_number(i)

for j in range(1,10001):
    if j in check:
        continue
    print(j)