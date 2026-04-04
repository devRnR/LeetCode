from collections import defaultdict
from math import gcd
import sys

input = sys.stdin.readline
n = int(input())

cnt = defaultdict(int)

for _ in range(n):
    x, y = map(int, input().split())

    g = gcd(abs(x), abs(y))   # 길이 정보 제거[web:36]
    dx = x // g              # 방향만 남긴 x성분
    dy = y // g              # 방향만 남긴 y성분
    cnt[(dx, dy)] += 1       # 이 방향에 있는 풍선 하나 추가

print(max(cnt.values()))