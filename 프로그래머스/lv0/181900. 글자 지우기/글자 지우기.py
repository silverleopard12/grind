def solution(my_string, indices):
    remove = set(indices)
    answer = ''
    
    for i in range(len(my_string)):
        if i not in remove:
            answer += my_string[i]
    
    return answer