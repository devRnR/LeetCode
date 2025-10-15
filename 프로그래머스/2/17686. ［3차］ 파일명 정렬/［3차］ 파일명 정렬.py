def divide(word):
    head = ""
    number = ""
    tail = ""
    flag = False
    

    for w in word:
        if w.isdigit() and not tail:
            flag = True
            number += w
        else:
            if flag:
                tail += w    
            else:
                head += w

    return (head, number, tail)

def solution(files):
    divided = list(map(lambda x: divide(x), files))
    sorted_list = sorted(divided, key = lambda x: (x[0].lower(), int(x[1])))
    answer = list(map(lambda x: x[0]+x[1]+x[2], sorted_list))
    return answer