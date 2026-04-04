def solution(intStrs, k, s, l):
    answer = []
    for i in range(0, len(intStrs)):
        intStrs[i] = intStrs[i][s:s+l]
    for i in intStrs:
        if (k < int(i)):
            answer.append(int(i))
            
    return answer