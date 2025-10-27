def solution(A, B):
    answer = 0
    sorted_a = sorted(A)[::-1]
    sorted_b = sorted(B)[::-1]
    
    l_idx = 0
    r_idx = 0
    while l_idx < len(sorted_a):
        
        cl = sorted_a[l_idx]
        cr = sorted_b[r_idx]
        
        if cl < cr:
            l_idx += 1
            r_idx += 1
            
            answer += 1
        else:
            l_idx += 1
    return answer


# 승리 조건

# 수가 큰 경우
# 근소한 차이로 이길 수 있는 수가 있는지를 확인하는게 어떨까?

# A의 순서가 나왔다는건 값을 안다는 것
# 큰 숫자 부터 봐야 하는가?


# 9 8 7 6 5
# 8 7 6 5 4

