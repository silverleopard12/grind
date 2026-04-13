def solution(arr, k):
    answer = []
    
    for i in arr:
        if i not in answer:
            answer.append(i)
    
    while k > len(answer):
        answer.append(-1)
    
    while k < len(answer):
        answer.pop()
    
    return answer