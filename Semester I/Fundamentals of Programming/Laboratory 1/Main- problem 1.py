#this function verifies if a number is prime or not
# it returns: 1 if the number is prime
#             0 it is not a prime number
def prime(n): 
 if n>1 :
     for i in range(2,n//2+1):
         if n%i == 0:
             return 0
     return 1
 else :
    return 0
if __name__ == '__main__':
    n=int(input("n="))
    p1=2
    g=0
    while p1<=n and g==0 :
       p2=n-p1
       if(prime(p1)==1 and prime(p2)==1):  #we found the numbers
          g=1
          print("Numbers are: ",p1," and ",p2,";")
       else:
          p1+=1
    if g==0:  #if we did not find the numbers
       print("The number",n,"can't be obtain from the additon of 2 prime numbers;")
