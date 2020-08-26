import copy
class RepoExpense:
    def __init__(self):
        self.__entities=[]
        self.__history=[]
    '''
    Function which adds 10 examples into the list 
    x: the list of expenses
    '''
    def ten_examples(self,x):
        for i in x:
            self.__entities.append(i)
        l=[]
        l=self.__entities.copy()
        self.__history.append(l)
    '''
    Returns the size of the list of expenses
    '''
    def size(self):
        return len(self.__entities)
    '''
    Function which adds a new element (expense) into the list
    x: the new expense which will be added
    return: -
    '''
    def add(self,x):
        self.__entities.append(x)
        l=[]
        l=self.__entities.copy()
        self.__history.append(l)

    '''
        Function which removes an element (expense) from the list
        expense: the expense which will be removed
        return: -
        '''
    def remove(self,expense):
        self.__history.append(self.__entities)
        i=0
        while i<int(len(self.__entities)):
            if self.__entities[i]<expense:
                del self.__entities[i]
            elif self.__entities[i]==expense:
                del self.__entities[i]
            else:
                i+=1

    '''
        Function which computes the undo operation
        return: -
    '''
    def undo(self):
        if len(self.__history)==0:
            print('No more undo steps!')
        else:
            del self.__history[-1]
            self.__entities=[]
            try:
                self.__entities=copy.deepcopy(self.__history[-1])
            except IndexError:
                pass
    '''
    Function which returns the list of expenses
    return: -
    '''
    def get_all(self):
        return self.__entities[:]
