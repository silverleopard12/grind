def solution(order):
    answer = 0
    ame = 0
    cafe = 0
    
    for i in order:
        if "cafe" in i:
            cafe +=1
        else:
            ame +=1
    
    answer = ame * 4500 + cafe * 5000
    
    return answer