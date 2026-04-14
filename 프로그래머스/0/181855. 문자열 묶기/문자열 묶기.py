def solution(strArr):
    answer = 0
    dic = {}
    
    for i in strArr:
        length = len(i)
        if length in dic:
            dic[length] += 1
        else:
            dic[length] = 1
    
    for v in dic.values():
        if v > answer:
            answer = v
            
    return answer