def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)

    for i in range(len(age)):
        answer += alpha[int(age[i])]
    
    return answer