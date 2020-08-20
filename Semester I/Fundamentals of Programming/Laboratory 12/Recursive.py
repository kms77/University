def backTrackingRec(x, SUM):
    if len(x) > SUM:
        return
    if solution(x, SUM):
        solutionFound(x, SUM)
        return
    x.append(0)
    for i in range(2, SUM):
        x[-1] = i
        if consistent(x):
            backTrackingRec(x, SUM)
    x.pop()
def isPrime(number):
    if number == 1:
        return False
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True

def sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

def solution(x, SUM):
    return sum(x) == SUM

def consistent(x):
    return isPrime(x[-1])

def solutionFound(x, SUM):
    print(x, "= ", SUM)

x=[]
SUM = int(input("n="))
backTrackingRec(x,SUM)