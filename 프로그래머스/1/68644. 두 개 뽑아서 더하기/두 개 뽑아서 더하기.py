def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
            
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next
            
def solution(numbers):
    answer = set()
    
    for c in combination(numbers, 2):
        answer.add(sum(c))
    return sorted(list(answer))