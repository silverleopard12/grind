def solution(l, r):
    answer = []
    for j in range(l, r+1):
        if str(j).replace('5', '').replace('0', '') == '':
            answer.append(j)
    if answer == []:
        answer = [-1]
    return answer