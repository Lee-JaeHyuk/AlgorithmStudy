def solution(n):
    array = ['1','2','4']
    if n <= 3:
        return array[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + array[r]

print(solution(8))
