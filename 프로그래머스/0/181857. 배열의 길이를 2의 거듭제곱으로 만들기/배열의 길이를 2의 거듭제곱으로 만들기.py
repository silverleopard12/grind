def solution(arr):
    answer = []
    length = [1,2,4,8,16,32,64,128,256,512,1024]
    
    while 1:
        if len(arr) in length:
            break
        else:
            arr.append(0)
    
    answer = arr
    
    return answer