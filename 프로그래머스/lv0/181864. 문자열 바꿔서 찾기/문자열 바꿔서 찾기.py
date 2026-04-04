def solution(myString, pat):
    answer = 0
    changed = ''
    
    for ch in myString:
        if ch == 'A':
            changed += 'B'
        else:
            changed += 'A'
    
    if pat in changed:
        answer = 1
        
    return answer