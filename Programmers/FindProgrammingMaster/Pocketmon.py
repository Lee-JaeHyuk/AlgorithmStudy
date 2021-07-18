def solution(nums):
    k = len(nums)/2
    my_set = set(nums)
    my_list = list(my_set)
    if len(my_set) >= k:
        return int(k)
    elif len(my_set) < k:
        return len(my_set)
