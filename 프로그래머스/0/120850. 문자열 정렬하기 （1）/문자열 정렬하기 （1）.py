def solution(my_string):
    return sorted([ int(n) for n in my_string if n.isdigit()])