#1 너무 막무가내로 진행함
def stonum(expression):
    num = []
    me = []
    s = ''
    for i in expression:
        if i == "+" or i == "-" or i == "*":
            me.append(i)
            num.append(int(s))
            s = ''
        else:
            s = s + i
    num.append(int(s))
    return num, me

def calculate_product(num, me):
    for i in range(0, len(me)):
        if me[i] == '*':
            n = num[i] * num[i + 1]
            num.pop(i)
            num.pop(i)
            num.insert(i, n)
            i -=1
    while '*' in me:
        me.remove('*')
    return num, me


def calculate_plus(num, me):
    for i in range(0, len(me)):
        if me[i] == '+':
            n = num[i] * num[i + 1]
            num.pop(i)
            num.pop(i)
            num.insert(i, n)
            i -=1
    while '+' in me:
        me.remove('+')
    return num, me


def calculate_minus(num, me):
    for i in range(0, len(me)):
        if me[i] == '-':
            n = num[i] - num[i + 1]
            num.pop(i)
            num.pop(i)
            num.insert(i, n)
            i -=1
    while '-' in me:
        me.remove('-')
    return num, me


def solution(expression):
    num, me = stonum(expression)
    result = []
    if len(set(me)) == 3:
        #a1, b1 = calculate_product(num,me)
        #print(a1,b1)
        a1, b1 = calculate_minus(num,me)
        print(a1,b1)
    # elif len(set(me)) == 2:

    # else:

    answer = 0
    return a1


expression = "100-200*300-500+20"
expression2 = "100-300-400-500+100-200"
#print(solution(expression2))
li = [1, 2, 3, 4, 5, 6]
li.pop(2)
# print(li)

def minu(num, me):
    lt = 0
    for i in range(len(me)):
        if me[i] == '-':
            print(num,me)
            n = num[i-lt] - num[i+1-lt]
            num.pop(i)
            num.pop(i)
            num.insert(i, n)
            lt += 1
    while '-' in me:
        me.remove('-')
    return num,me

num = [100,300,400,500,100,200]
me = ['-','-','-','+','-']
print(minu(num,me))












