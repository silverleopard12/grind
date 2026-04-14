def solution(rank, attendance):
    answer = 0
    k = 0
    for i in range(len(rank)):
        num = rank.index(i+1)
        
        if attendance[num] == 1 and k == 0:
            answer += num * 10000
            k += 1
            
        elif attendance[num] == 1 and k == 1:
            answer += num * 100
            k += 1
            
        elif attendance[num] == 1 and k == 2:
            answer += num
            k += 1
        
    return answer