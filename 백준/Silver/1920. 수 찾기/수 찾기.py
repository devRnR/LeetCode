import sys

input = sys.stdin.readline
n = int(input())
n_arr = sorted(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

def bs(arr, target):

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == target:
            return 1
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return 0

for num in m_arr:
    print(bs(n_arr, num))


