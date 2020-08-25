# this function verifies if a number is prime or not
# It returns : 1- if the number is prime
#              0- the number is not prime
def prim(n):
  if n>1 :
      for i in range(2,n//2):
          if n%i==0:
              return 0
      return 1
  else :
     return 0
if __name__=="__main__":
    n=int(input("n="))
    if n%2==0: # we have to work only with odd numbers
       p1=n+1
    else:
       p1=n+2
    g=0
    while g==0: #still were not found the two numbers
         if prim(p1)==1:
            p2=p1+2;
            if prim(p2)==1:
                g=1
         if g==0:
             p1+=2
    print("The twin numbers are: ",p1," and ",p2,";")
