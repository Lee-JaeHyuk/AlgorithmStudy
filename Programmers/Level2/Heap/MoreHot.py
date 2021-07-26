import heapq

# 효율성 테스트 실패
def solution(scoville, k):
    cnt = 0
    while min(scoville) < k:
        scoville.sort()
        scoville.append(scoville.pop(0) + (scoville.pop(0)*2))
        cnt+=1
    return cnt

def solution2(scoville, k):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) == 1:
            if scoville[0] < k:
                return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        cnt += 1
    return cnt


l = [1,2,3,9,10,12]
k = 7
print(solution2(l,k))
