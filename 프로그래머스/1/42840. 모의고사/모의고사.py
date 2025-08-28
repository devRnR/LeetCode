def solution(answers):
    patterns= [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0, 0, 0]
    for i in range(len(answers)):
        
        scores[0] += 1 if patterns[0][i % len(patterns[0])] == answers[i] else 0
        scores[1] += 1 if patterns[1][i % len(patterns[1])] == answers[i] else 0
        scores[2] += 1 if patterns[2][i % len(patterns[2])] == answers[i] else 0
        
    answer = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)
    
    
    return answer