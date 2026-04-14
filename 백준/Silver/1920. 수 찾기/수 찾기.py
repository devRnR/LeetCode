import sys

input = sys.stdin.readline
n = int(input())
n_arr = sorted(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

def bs_recur(arr, target, l, r):
    if l > r:
        return 0

    mid = l + (r - l) // 2

    if arr[mid] == target:
        return 1
    elif target < arr[mid]:
        return bs_recur(arr, target, l, mid - 1)
    else:
        return bs_recur(arr, target, mid + 1, r)

for num in m_arr:
    print(bs_recur(n_arr, num, 0, len(n_arr) - 1))


