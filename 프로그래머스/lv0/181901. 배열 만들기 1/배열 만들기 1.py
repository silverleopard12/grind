def solution(n, k):
    answer = []
    for i in range(0, n+1, k):
        answer.append(i)
    answer.remove(0)
    return answer