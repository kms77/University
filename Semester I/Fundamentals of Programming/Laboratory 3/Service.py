import datetime
def get_date():
    #function that gets the current date of the month and returns it
    y = datetime.datetime.now()
    x=int(y.strftime("%d"))
    return x
def set_value(List,x,y,value):
    #function that adds a value to a known element from list
    List[x][y]=List[x][y]+value
def add_expense(List,category,cmd,history):
    '''
    #function that represent the add command
    #input:List-the list of days and categories,cmd-the list formed from the inserted command, category-the list of expense types
    #output:nothing=the value was added, message=invalid command for add
    '''
    from Verification import verification_add
    if verification_add(cmd,category)==True:
        x=get_date()
        x-=1
        set_value(List,x,cmd[2],int(cmd[1]))
        from  Domain import add_to_history
        add_to_history(List,history)
    else:
        print("Invalid command!")
def insert_expense(List,category,cmd,history):
    '''
    #function that represent the insert command
    #input:List-the list of days and categories,cmd-the list formed from the inserted command, category-the list of expense types
    #output:nothing=the value was inserted, message=invalid command for add
    '''
    from Verification import verification_insert
    if verification_insert(cmd,category)==True:
        set_value(List,int(cmd[1])-1,cmd[3],int(cmd[2]))
        from Domain import add_to_history
        add_to_history(List,history)
    else:
        print("Invalid command!")
def remove_expense(List,category,cmd,history):
    '''
    #function that represent the remove function
    #input:List-the list of days and categories,cmd-the list formed from the inserted command, category-the list of expense types
    #output:nothing=the value was added, message=invalid command for remove 
    '''
    from Verification import verify_remove
    if verify_remove(cmd,category)==True:
        if len(cmd)==2:
            if cmd[1] in category:
                remove_category(List,cmd)
                from Domain import add_to_history
                add_to_history(List,history)
            else:
                remove_day(List,cmd)
                from Domain import add_to_history
                add_to_history(List,history)
        else:
            remove_days(List,cmd)
            from Domain import add_to_history
            add_to_history(List,history)
    else:
        print("Invalid command!")
def delete_expense(List,i,j):
    '''
    #function that asigns to an element from the list the null value
    #input:List-the list of days,i-the index of line,j-the index of column
    #output:-
    '''
    List[i][j]=0
def remove_day(List,cmd):
    '''
    #function that remove(give the value zero to all expenses from that day) a day
    #input:List-the list of days,cmd-the list formed from the inserted command
    #output:-
    '''
    category=["housekeeping","food","transport","clothing","internet","others"]
    for i in range(0,6):
        delete_expense(List,int(cmd[1])-1,category[i])
def remove_category(List,cmd):
    '''
    #function that gives the value zero to a whole category of expense
    #input:List-the list of days,cmd-the list formed from the inserted command
    #output:-
    '''
    for i in range(0,30):
        delete_expense(List,i,cmd[1])
def remove_days(List,cmd):
    '''
    #function that remove(gives the value 0) all expenses from an interval of days
    #input:List-the list of days,cmd-the list formed from the inserted command
    #output:-
    '''
    category=["housekeeping","food","transport","clothing","internet","others"]
    for i in range(int(cmd[1])-1,int(cmd[3])):
        for j in range(0,6):
            delete_expense(List,i,category[j])
def display_list1(List):
    '''
    #function which write the entire list of expenses
    #input:List-the list of days
    #output:it prints all the list
    #return:-
    '''
    for i in range(0,30):
         print("Day ",i+1,": ",List[i],sep='')
def list_category(List,cmd):
    '''
    #function which writes all the expenses for a category
    #input:List-the list of days,cmd-the list formed from the inserted command
    #output:message-if no one expense | or:the list of days with the expense for that category
    #return:-
    '''
    #function which writes all the expenses for a category
    g=0
    for i in range(0,30):
        if List[i][cmd[1]]>0:
           g=1
           print("Day ",i+1,": ",List[i][cmd[1]],sep='')
    if g==0:
        print("There is no one expense in this month for:",cmd[1])
def long_list(List,cmd):
    '''
    #function which find the correct call for the command
    #input:List-the list of days,cmd-the list formed from the inserted command
    #output:-
    #return:-
    '''
    if cmd[2]=='=':
        get_equality(List,cmd)
    elif cmd[2]=='<':
        get_less(List,cmd)
    else:
        get_large(List,cmd)
def get_equality(List,cmd):
    '''
    #function that writes the days which have an equal expense with a value
    #input:List-the list of days and categories,cmd-the list formed from the inserted command
    #output:nothing=the value was wrote, message=invalid command for list 
    '''
    g=0
    for i in range(0,30):
        if equality(List,i,cmd[1],int(cmd[3]))==True:
            print("Day ",i+1,": ",List[i][cmd[1]],sep='')
            g=1
    if g==0:
        print("There is no one expense from this category equal with this value!")
def equality(List,i,j,x):
    '''
    #function which verifies if an elemnt from the list has an equal value as x
    #input:List-the list of days and categories,i-index of lines,j-index of colums,x-the value
    #output:True-x is equal with the element from the list,False-it is not equal
    '''
    if int(List[i][j])==x:
        return True
    else:
        return False
def get_less(List,cmd):
    '''
    #function that writes the days which have a smaller expense than a value
    #input:List-the list of days and categories,cmd-the list formed from the inserted command
    #output:nothing=the value was wrote, message=invalid command for list
    '''
    g=0
    for i in range(0,30):
        if less_value(List,i,cmd[1],int(cmd[3]))==True:
            print("Day ",i+1,": ",List[i][cmd[1]],sep='')
            g=1
    if g==0:
        print("There is no one expense from this category smaller than this value!")
def less_value(List,i,j,x):
    '''
    #function which verifies if an elemnt from the list have a smaller value than x
    #input:List-the list of days and categories,i-index of lines,j-index of colums,x-the value
    #output:True-x is smaller with the element from the list,False-it is not smaller
    '''
    if int(List[i][j])<x:
        return True
    else:
        return False
def get_large(List,cmd):
    '''
    #function that writes the days which have a larger expense than a value
    #input:List-the list of days and categories,cmd-the list formed from the command
    #output:nothing=the value was wrote, message=invalid command for list 
    '''
    g=0
    for i in range(0,30):
        if large_value(List,i,cmd[1],int(cmd[3]))==True:
            print("Day ",i+1,": ",List[i][cmd[1]],sep='')
            g=1
    if g==0:
        print("There is no one expense from this category larger than this value!")
def large_value(List,i,j,x):
    '''
    #function which verifies if an elemnt from the list is higher then x
    #input:List-the list of days and categories,i-index of lines,j-index of colums,x-the value
    #output:True-x is higer than the element from the list,False-it is not higher
    '''
    if int(List[i][j])>x:
        return True
    else:
        return False
def display_list(List,category,cmd):
    '''
    #function that display the correct list after the list command
    #input:List-the list of days and categories,cmd-the list formed from the inserted command, category-the list of expense types
    #output:nothing=the value was wrote, message=invalid command for list
    '''
    from Verification import verification_list
    if verification_list(cmd,category)==True:
        if len(cmd)==1:
            display_list1(List)
        elif len(cmd)==2:
            list_category(List,cmd)
        else:
            long_list(List,cmd)
    else:
        print("Invalid command!")