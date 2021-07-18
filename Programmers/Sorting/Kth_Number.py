def solution(array, commands):
    ans = []
    answer = []
    for i in commands:
        ans = array[i[0] - 1:i[1]]
        k = i[2]
        ans.sort()
        answer.append(ans[k - 1])
    return answer


array1 = [1, 5, 2, 6, 3, 7, 4]
array2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array1, array2))


# 우수 풀이
def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))
