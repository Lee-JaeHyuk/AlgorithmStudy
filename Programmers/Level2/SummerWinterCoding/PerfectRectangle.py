import math


def solution(w, h):
    gcd = math.gcd(w, h)
    if gcd == 1:
        answer = (w * h) - (w + h - 1)
    else:
        answer = (w * h) - (w + h - gcd)
    return answer

print(solution(12,8))