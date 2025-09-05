def solution(record):
    answer = []
    users = {}
    prints = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    for r in record:
        h = r.split()
        
        if h[0] == 'Enter' or h[0] == 'Change':
            users[h[1]] = h[2]
    
    for r in record:
        h = r.split()
        
        if h[0] != 'Change':
            answer.append(f'{users[h[1]]}{prints[h[0]]}')
        
    return answer