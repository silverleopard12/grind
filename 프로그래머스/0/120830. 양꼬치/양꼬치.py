def solution(n, k):
    answer = 0
    answer = 12000 * n + 2000 * k
    if n > 9:
        answer -= 2000 * (n // 10)
    return answer