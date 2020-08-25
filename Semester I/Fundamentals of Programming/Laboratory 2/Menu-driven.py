import math #This library provides access to the mathematical functions 
def add_to_list(List,x,y): #add a new elemnt to the list
   List.append((x,y))
def increase(a,b): #this function verifies if a number is smaller or equal than other number(float numbers)
   if a<=b:
       return True
   else:
        return False
def sequence2(List,a):
   '''
   this function find the position of last element of the sequence in the List
   input: List-the list of complex numbers, a-position of first element of the sequence in the List
   output: the position of last element of the sequence in the List
   '''
   b=a+1
   g=0
   x=module(List[a][0],List[a][1])
   y=module(List[b][0],List[b][1])
   while g==0 and b<(len(List)-1):
        x=y
        if b!=(len(List)-1):    #for index out of range error
           y=module(List[b+1][0],List[b+1][1])
        if increase(x,y)==False:
           g=1
        else:   
            b+=1   
   return b                                  
def increasing_moduls(List,seq):
   '''
   this function find  the longest sequence which contains numbers having increasing modulus.

   input: List-the list of complex numbers,seq-the sequence which will contain all the complex numbers
          with incresing modulus
   output:a message if there was no one sequence or the sequence printed
   '''
   seq=[]
   maxa=-1
   maxb=-1
   i=0
   while i<(len(List)-1):
      x=module(List[i][0],List[i][1])
      y=module(List[i+1][0],List[i+1][1])
      if increase(x,y)==True:
         j=sequence2(List,i)
         if j-i>maxb-maxa:
            maxa=i  #the ends of the longest sequence
            maxb=j
         i=j
      else:
         i+=1
   if maxa==-1:
      print("There are no one sequence of increasing modulus;")
   else:
      form_sequence(List,seq,maxa,maxb)
def form_sequence(List,seq,maxa,maxb):  #this function create the longest sequence from a List
   for i in range(maxa,maxb+1):         #it uses the parameters maxa and maxb for the ends of the sequence
      seq.append(List[i])
   print("The longest sequence is:\n",seq)  #the function prints the sequence
def module(a,b):  #this function returns the modulus of two numbers without them square root
    c=(a*a+b*b)
    return c
def verif_real(List,i): #this function verifies if two consecutive numbers are real
   if (int(List[i][1])==0 and int(List[i+1][1])==0):
      return True
   else:
      return False
def real_sequence(List,i):           #this function return the last element of a sequence which
   b=i+1                             #contains real numbers
   while b<(len(List)-1) and True:
        if verif_real(List,b)==True:
           b+=1
        else:   
           return b
   return b      
def max_sequence(List,seq):
   '''
   this function find  the longest sequence which contains consecutive real numbers

   input: List-the list of complex numbers,seq-the sequence which will contain all
          consecutive real numbers
   output:a message if there are no one sequence or the sequence 
   '''
   seq=[]
   maxa=-1
   maxb=-1
   i=0
   while i<(len(List)-1):
      if verif_real(List,i)==True:
         j=real_sequence(List,i)
         if j-i>maxb-maxa:
            maxa=i
            maxb=j
         i=j
      else:
         i+=1
   if maxa==-1:
      print("There are no one sequence of real numbers;")
   else:
      form_sequence(List,seq,maxa,maxb)
def verification_print(List,i):
    '''
    the function prints in a correct way all the numbers from the List. It
    verifies all the special cases(if the complex numbers is just 2,etc.)

    input: List-the list of complex numbers,i-the index of the element from the List
    output:a number printed in a correct way
    '''
    if List[i][0]==0:
        if List[i][1]==1:
            print("i")
        elif List[i][1]==-1:
            print("-i")
        elif List[i][1]==0:
            print("0")
        else:
            print(List[i][1],"i",sep='')
    else:
        if List[i][1]==1:
            print(List[i][0],"+","i",sep='')
        elif List[i][1]==-1:
            print(List[i][0],"-","i",sep='')
        elif List[i][1]==0:
            print(List[i][0])
        elif List[i][1]<0:
            print(List[i][0],List[i][1],"i",sep='')
        else:
            print(List[i][0],"+",List[i][1],"i",sep='')
def read_number1():
   x=str(input("imaginary number:"))
   x=test_imaginary_number(x)
   return x
def test_imaginary_number(x):      #this  function assures a correct input for the imaginary part of a complex number
    while True:
        if x=='i':
            l1=('1','i') 
            x=''.join(l1)   #convert a tuple in a list
        else: 
            if x=='-i':
               l1=('-1','i')
               x=''.join(l1)       
        try:
            if x[-1]=='i':
               y=float(x[:-1])
            else:
               y=float(x)
            return y
        except ValueError as ve:
            print("Please input the imaginary part!")
            x=str(input("imaginary number:"))
def read_number2():
   x=str(input("real number:"))
   x=test_real_number(x)
   return x
def test_real_number(x):    #this  function assures a correct input for the real part of a complex number
    while True:
        try:
            x=float(x)
            return x
        except ValueError as ve:
            print("Please input a float value!")
            x=input("real number:")
def test_natural_number():    #this  function assures a correct input for the n(the number of complex numbers) 
    n=input("The number of complex numbers are:")
    while True:
        try:
            n=int(n)
            if n<0:
                print("Please input a natural value!")
                n=input("The number of complex numbers are:")
            else:    
                return n
        except ValueError as ve:
            print("Please input a natural value!")
            n=input("The number of complex numbers are:")
def test_increase():
   assert(increase(0,0)==True)
   assert(increase(-4.2,3)==True)
   assert(increase(2,10)==True)
   assert(increase(2,1)==False)
   assert(increase(-2,-4)==False)
   assert(increase(3,0)==False)
def test_real():
   assert(test_real_number('4')==4)
   assert(test_real_number('0')==0)
   assert(test_real_number('-2')==-2)
   assert(test_real_number('2')==2)
   assert(test_real_number('-1')==-1)
   assert(test_real_number('-6')==-6)
def test_imaginary():
   assert(test_imaginary_number('2i')==2)
   assert(test_imaginary_number('3')==3)
   assert(test_imaginary_number('0i')==0)
   assert(test_imaginary_number('7i')==7)
   assert(test_imaginary_number('-1i')==-1)
   assert(test_imaginary_number('-i')==-1)
def all_tests():
   test_increase()
   test_real()
   test_imaginary()
def integer(x): #if a float number can be represent at an integer than this function
    y=float(x)  #transforms it from float to integer
    if  x==int(float(x)):
        y=int(float(x))
    return y
def suitable_numbers():  #the function which assigns to List 10 suitable complex numbers 
   List=[(1,2),(-1,1),(2,0),(0,2),(1,-3),(2,6),(4,0),(5,0),(6,0),(0,0)]
   print("The list was read;\n")
   return List
def create_list(n,List):
     '''
      This function create a List of tuples. A tuple will have the form (a,b)
      Where a-is the real part and b-is the imaginary part of a complex number
     '''
     n=test_natural_number()
     for i in range(0,n):
         x=read_number2()
         y=read_number1()
         x=integer(x)
         y=integer(y)
         add_to_list(List,x,y)
     print("The list was created!")
def dysplay_numbers(List): #this function display the List of complex numbers
    for i in range(len(List)):
        verification_print(List,i)	
def menu_driven(): #the principal menu with the  functionalities
           print("MENU-DRIVEN") 
           print("\n1.The list of complex numbers;")
           print("\n2.Display the list;")
           print("\n3.The longest sequence that observes the numbers having increasing moduls;")
           print("\n4.The longest sequence that observes the numbers having real numbers;")
           print("\n5.Exit;")
def menu_driven_2(): #the second menu use for reading a list
           print("\n1.Read a list of n elements;")
           print("\n2.List of 10 suitable complex numbers;")
           print("\n3.Back;")
if __name__=="__main__":
    '''
     The main contains the cases which can be appeal by the user
     If the user choosed a wrong number than he/she will get a message
     and  should choose again
    '''
    all_tests()
    List=[]
    n=0
    seq=[]
    g=0
    while True:
         try:
             menu_driven()
             choice=int(input("Choose a number from 1 to 5:"))
             if choice==5:
                 print("The program was closed")
                 break
             elif choice==1:
                 suitable_numbers()
                 while True:
                     try:
                        menu_driven_2()
                        choice2=int(input("Choose a number from 1 to 3:"))
                        if choice2==1:
                             if g==1:
                                List=[]
                                create_list(n,List)
                             else:
                                g=1
                                create_list(n,List)
                        elif choice2==2:
                             if g==1:
                                List=[]
                                List=suitable_numbers()
                             else:
                                g=1
                                List=suitable_numbers()
                        elif choice2==3:
                             break
                             choice=input("Choose a number from 1 to 5:")
                        else:
                             print("Wrong choice.\nChoose again!")
                     except ValueError as ve:
                        print("Wrong choice.\nChoose again!")
             elif choice==2:
                 if g==1:
                    dysplay_numbers(List)
                 else:
                    print("You do not read any list;\n")
                    print("Choose a number from 1 to 5:")
             elif choice==3:
                if g==1:
                    increasing_moduls(List,seq)
                else:
                    print("You do not read any list;\n")
                    print("Choose a number from 1 to 5:")
             elif choice==4:
                 if g==1:
                    seq=[]
                    max_sequence(List,seq)
                 else:
                    print("You do not read any list;\n")
                    print("Choose a number from 1 to 5:")
             else:
                 print("Wrong choice.\nChoose again!")    
         except ValueError as ve:
             print("Wrong choice.\nChoose again!")
 #sequence=at least two elements
