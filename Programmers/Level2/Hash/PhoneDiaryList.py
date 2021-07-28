def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        t = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:t]:
            return False
    return True


p1 = ["119", "97674223", "1195524421"]
p2 = ["123","456","789"]
p3 = ["12","123","1235","567","88"]
print(solution(p1))