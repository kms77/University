def validation_filter(cmd,category):
    '''
    #function which verifies if the command for filter is a valid one
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True-ti is a valid command,False-it is not  a valid command
    '''
    if len(cmd)==2:
        if cmd[1] in category:
            return True
        else:
            return False
    elif len(cmd)==4:
        try:
           if ((cmd[1] in category) and (cmd[2]=='=' or cmd[2]=='<' or cmd[2]=='>') and (int(cmd[3])>0)):
               return True
           else:
               return False
        except ValueError:
           return False
    else:
        return False
def verification_sort(cmd,category):
    '''
    #function which verifies if the command for sort is a valid one
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True-ti is a valid command,False-it is not  a valid command
    '''
    if len(cmd)==2:
        if cmd[1]=='day':
            return True
        elif cmd[1] in category:
            return True
        else:
            return False
    else:
        return False
def verification_max(cmd,category):
    '''
    #function which verifies if the command for max is a valid one
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True-ti is a valid command,False-it is not  a valid command
    '''
    if len(cmd)==2:
        if cmd[1]=='day':
           return True
        else:
             return False
    return False
def verification_sum(cmd,category):
    '''
    #function which verifies if the command for sum is a valid one
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True-ti is a valid command,False-it is not  a valid command
    '''
    if len(cmd)==2:
        if cmd[1] in category:
            return True
        else:
            return False
    else:
        return False
def verification_list(cmd,category):
    '''
    #function that gets a boolean value about the list command
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True- a valid command, False-an invalid command
    '''
    if len(cmd)==1:
       return True 
    elif len(cmd)==2:
       if cmd[1] in category:
           return True
       else:
           return False
    elif len(cmd)==4:
       try:
           if ((cmd[1] in category) and (cmd[2]=='=' or cmd[2]=='<' or cmd[2]=='>') and (int(cmd[3])>0)):
               return True
           else:
               return False
       except ValueError:
           return False
    else:
        return False
def verify_remove(cmd,category):
   '''
   #function that gets a boolean value about the remove function
   #input:cmd-the list formed from the inserted command, category-the list of expense types
   #output:True- a valid command, False-an invalid command
   '''
   if len(cmd)==2:
     try:
         if cmd[1] in category:
             return True
         elif int(cmd[1])>=1 and int(cmd[1])<=30:
             return True
         else:
             return False
     except ValueError:
         return False
   elif len(cmd)==4:
     try:
         if (int(cmd[1])>=1 and int(cmd[1])<=30 and int(cmd[3])>=1 and int(cmd[3])<=30 and int(cmd[1])<=int(cmd[3]) and cmd[2]=='to'):
             return True
         else:
             return False
     except ValueError:
             return False
   else:
        return False
def verification_add(cmd,category):
    '''
    #function that gets a boolean value about the add function
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True- a valid command, False-an invalid command
    '''
    if len(cmd)==3:
        if cmd[2] in category:
            try:
                if int(cmd[1])>0:
                   return True
                else:
                   return False
            except ValueError:
                return False
        else:
            return False
    else:
        return False
def verification_insert(cmd,category):
    '''
    #function that gets a boolean value about the insert function
    #input:cmd-the list formed from the inserted command, category-the list of expense types
    #output:True- a valid command, False-an invalid command
    '''
    if len(cmd)==4:
        try:
              if int(cmd[1])<1 or int(cmd[1])>30:
                  return False
        except ValueError:
                  return False
        if cmd[3] in category:
              try:
                  if int(cmd[2])>0:
                     return True
                  else:
                     return False
              except ValueError:
                  return False
        else:
              return False
    else:
        return False