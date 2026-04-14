def solution(arr):
    answer = [[]]
    
    row = len(arr)
    col = len(arr[0])
    
    answer = [i[:] for i in arr]
    
    if row > col:
        for i in range(row):
            answer[i] += [0] * (row - col)
    elif row < col:
        for _ in range(col - row):
            answer.append([0] * col)
    
    return answer