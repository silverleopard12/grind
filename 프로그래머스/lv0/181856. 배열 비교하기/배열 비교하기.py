def solution(arr1, arr2):
    
    answer = 0
    sum1 = 0
    sum2 = 0
    
    if(len(arr1) > len(arr2)):
        answer = 1
    elif(len(arr1) < len(arr2)):
        answer = -1
    else:
        for i in arr1:
            sum1 += i
        for j in arr2:
            sum2 += j
        if sum1 > sum2:
            answer = 1
        elif sum1 == sum2:
            answer = 0
        else:
            answer = -1
    return answer