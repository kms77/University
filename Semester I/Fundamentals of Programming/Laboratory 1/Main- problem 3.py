# this function verifies if a number is prime or not
# 1- if the number is prime
# 0- if it is not a prime number
def prim(n):
  if n>1 :
      for i in range(2,n//2+1):
          if n%i==0:
              return 0
      return 1
  else :
     return 0
# this function return the n-th number of the sequence
# n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the
# sequence of natural numbers by replacing composed numbers with their prime divisors,
# without memorizing the elements of the sequence.
def function(n):
    a=1 #the current number
    b=1 #the number we have to return
    c=1 #the counter
    while c<n :
        a+=1
        b=a
        c+=1
        d=2
        g=0
        while (c<=n and d<=a/2) : #it is true only for numbers with divisors
            if (a%d==0 and prim(d)==1):
                c+=1
                b=d
                g=1
            d=d+1
        if g==1 : #it maintains the counting correct
            c-=1
    return b
if __name__=="__main__":
    n=int(input("n="))
    n=function(n)
    print("The n-th number of the sequence is ",n,";")
