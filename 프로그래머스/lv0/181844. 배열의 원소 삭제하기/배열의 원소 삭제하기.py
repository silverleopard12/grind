def solution(arr, delete_list):
    answer = []
    
    delete_set = set(delete_list)
    for s in arr:
        if s not in delete_set:
            answer.append(s)
    
    return answer