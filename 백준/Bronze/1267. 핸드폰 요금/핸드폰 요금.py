import sys

my_input = sys.stdin.readline

def calc(std, price, arr):
	amount = 0

	for a in arr:
		amount += ((a+1) // std) * price

		if (a+1) % std != 0:
			amount += price

	return amount

N = int(my_input())
arr = list(map(int, my_input().split()))

y_amount = calc(30, 10, arr)
m_amount = calc(60, 15, arr)

if y_amount == m_amount:
	print('Y M', y_amount)
elif y_amount > m_amount:
	print('M', m_amount)
else:
	print('Y', y_amount)
