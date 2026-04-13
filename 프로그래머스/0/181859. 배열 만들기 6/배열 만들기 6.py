def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1

        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1

        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1

    answer = stk

    if len(stk) == 0:
        answer = [-1]

    return answer