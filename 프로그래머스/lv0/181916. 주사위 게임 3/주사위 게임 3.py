def solution(a, b, c, d):
    answer = 0
    
    dice = [a, b, c, d]

    count = {}
    
    for x in dice:
        count[x] = count.get(x, 0) + 1
    
    keys = list(count.keys())
    values = list(count.values())

    if len(count) == 1:
        answer = 1111 * keys[0]

    elif len(count) == 2 and 3 in values:
        for k in count:
            if count[k] == 3:
                p = k
            else:
                q = k
        answer = (10 * p + q) ** 2

    elif len(count) == 2 and 2 in values:
        p, q = keys
        answer = (p + q) * abs(p - q)

    elif len(count) == 3:
        singles = []
        for k in count:
            if count[k] == 1:
                singles.append(k)
        answer = singles[0] * singles[1]

    else:
        answer = min(dice)
    
    return answer