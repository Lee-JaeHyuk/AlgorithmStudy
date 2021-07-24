def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p != c:
            return p
    return participant[-1]

a1 = ["lee", "kim", "park", "park"]
b1 = ["lee","kim", "park"]

print(solution(a1,b1))