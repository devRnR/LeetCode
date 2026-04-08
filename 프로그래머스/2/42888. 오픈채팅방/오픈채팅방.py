def solution(record):
    answer = []
    users = {}
    prints = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
      
    for r in record:
        behave = r.split()
        
        if behave[0] == 'Leave':
            answer.append((behave[1], 'Leave'))
        elif behave[0] == 'Enter':
            users[behave[1]] = behave[2]
            answer.append((behave[1], 'Enter'))
        else:
            users[behave[1]] = behave[2]
    answer = [f'{users[i]}{prints[c]}' for i, c in answer]
        
    return answer