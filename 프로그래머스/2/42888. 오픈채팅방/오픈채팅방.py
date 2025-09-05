def solution(record):
    answer = []
    
    users = {}
    
    for r in record:
        h = list(r.split())
        
        command = h[0]
        user_id = h[1]
        
        if command == 'Enter':
            answer.append(["*님이 들어왔습니다.", user_id])
            users[user_id] = h[2]
        elif command == 'Leave':
            answer.append(["*님이 나갔습니다.", user_id])
        else:
            users[user_id] = h[2]
        
    for a in answer:
        nick = users[a[1]]
        a[0] = a[0].replace("*", nick)        
        
    return [a[0] for a in answer]