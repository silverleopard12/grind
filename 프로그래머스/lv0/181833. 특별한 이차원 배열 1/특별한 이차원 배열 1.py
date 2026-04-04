def solution(n):
    answer = [[]]
    
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        
        if i == 0:
            answer[0] = row
        else:
            answer.append(row)
    
    return answer