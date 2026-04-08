def solution(want, number, discount):
    memo = { k : v for k,v in zip(want, number)}
    total = sum(number)

    answer = 0
    l = 0
    r = 0
    
    while r < len(discount):
        if discount[r] in memo:
            if memo[discount[r]] > 0:
                    total -= 1
            memo[discount[r]] -= 1
        
        if r - l + 1 >  10:
            if discount[l] in memo:
                memo[discount[l]] += 1
                if memo[discount[l]] > 0:
                    total += 1
            l += 1        

        if r -l +1 == 10 and total == 0:
            answer += 1
        
        r += 1
            
    return answer