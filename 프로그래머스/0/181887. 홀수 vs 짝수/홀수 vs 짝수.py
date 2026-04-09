def solution(num_list):
    answer = 0
    odd_list=[]
    even_list=[]
    for i in range(len(num_list)):
        if i % 2 == 0:
            even_list.append(num_list[i])
        else:
            odd_list.append(num_list[i])
            
    if sum(even_list) > sum(odd_list):
        answer = sum(even_list)
        
    elif sum(even_list) < sum(odd_list):
        answer = sum(odd_list)
        
    else:
        answer = sum(even_list)
    return answer