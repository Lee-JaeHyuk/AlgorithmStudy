def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        print(i)
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            right = i
        else:
            i = 11 if i==0 else i
            absL = abs(i-left)
            absR = abs(i-right)

            if sum(divmod(absL,3)) > sum(divmod(absR,3)):
                answer += 'R'
                right = i
            elif sum(divmod(absL,3)) < sum(divmod(absR,3)):
                answer += 'L'
                left = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer


number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(number, hand))
