def solution(wallet, bill):
    answer = 0
    
    mi = min(wallet)
    mx = max(wallet)
    
    bi = min(bill)
    bx = max(bill)
    
    while mi < bi or mx < bx:
        bx //= 2
        bi, bx = min(bi,bx), max(bi, bx)
        answer += 1
    
    return answer