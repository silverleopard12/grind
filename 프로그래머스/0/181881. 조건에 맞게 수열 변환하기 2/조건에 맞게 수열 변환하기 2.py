def solution(arr):
    answer = 0
    while True:
        pre_arr = arr
        nex_arr = []
        
        for i in pre_arr:
            if i >= 50 and i % 2 == 0:
                nex_arr.append(i // 2)
            elif i < 50 and i % 2 == 1:
                nex_arr.append(i * 2 + 1)
            else:
                nex_arr.append(i)
        
        if pre_arr == nex_arr:
            break
        
        arr = nex_arr
        answer += 1
        
    return answer