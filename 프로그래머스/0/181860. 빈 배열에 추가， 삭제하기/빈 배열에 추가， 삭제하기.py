def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == 1:
            answer.extend([arr[i]] * (arr[i] * 2))
        elif flag[i] == 0:
            answer = answer[:-arr[i]]
    return answer