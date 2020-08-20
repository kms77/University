def succes(n,List):
    sum=0
    for i in range(len(List)):
        sum+=List[i]
    if sum==n:
        return True
    return False
def prime(x):
    if (x%2==0 and x!=2) or x==1:
        return False
    for i in range(3,int(x/2)+1):
        if x%i==0:
            return False
    return True
def not_in_interval(n,List):
    sum = 0
    for i in range(len(List)):
        sum += List[i]
    if sum >n:
        return True
    return False
def is_solution(List,n):
    print(str(List), "=" ,str(n))
def backtracking(n):
    List=[]
    for i in range(n):
        if prime(i)==True:
           List.append(i)
           for j in range(int(n/2)):
               List.append(2)
           while(len(List)!=1):
               while not_in_interval(n,List)==False:
                  while succes(n, List) == False and not_in_interval(n,List)==False:
                     List[-1]+=1
                  if succes(n,List)==True:
                     if prime(List[-1])==True:
                       is_solution(List,n)
                  if len(List)==2:
                      List[-2]=n
                  List[-2]+=1
                  while(prime(List[-2])==False):
                        List[-2]+=1
                  List[-1]=2
               List=List[:-1]
        List=[]
    if prime(n)==True:
        List.append(n)
        print(List)
def main():
    n=int(input("n="))
    backtracking(n)
main()
