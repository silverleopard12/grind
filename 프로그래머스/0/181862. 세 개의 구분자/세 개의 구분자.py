def solution(myStr):
    answer = []
    k = 0
    
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            if myStr[k:i] != "":
                answer.append(myStr[k:i])
            k = i + 1
    
    if myStr[k:] != "":
        answer.append(myStr[k:])
    
    if answer == []:
        return ["EMPTY"]
    return answer
