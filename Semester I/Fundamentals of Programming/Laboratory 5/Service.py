from Domain import Expense
from Repository import RepoExpense
from Validator import ValidateExpense
class ServiceExpense:
    def __init__(self,repo,valid):
       self.__repo=repo
       self.__valid=valid
    '''
    Get the number of expenses from the list
    '''
    def get_no_of_expenses(self):
        return self.__repo.size()
    '''
    Adds 10 expenses into the list
    x: the list were we add the examples
    '''
    def examples(self,x):
        expense=Expense(1,40,"transport")
        x.append(expense)
        expense=Expense(29,8,"internet")
        x.append(expense)
        expense=Expense(19,10,"internet")
        x.append(expense)
        expense=Expense(6,100,"others")
        x.append(expense)
        expense=Expense(22,55,"transport")
        x.append(expense)
        expense=Expense(9,60,"food")
        x.append(expense)
        expense=Expense(9,40,"housekeeping")
        x.append(expense)
        expense=Expense(3,21,"transport")
        x.append(expense)
        expense=Expense(5,77,"internet")
        x.append(expense)
        expense=Expense(30,5,"others")
        x.append(expense)
        self.__repo.ten_examples(x)
    '''
    Function which validate and if true call repository to add an expense into the list
    day: day in which it is added
    money: amount of money
    extype: type of the expense
    return: -
    '''
    def add_expenses(self,day,money,extype): 
        expense=Expense(day,money,extype)
        self.__valid.validate(expense)
        self.__repo.add(expense)
    '''
       Function which filter the list of expenses by a given amount of money
       x: amount of money we filter by
       return: -
       '''
    def filter_list(self,x):
        expense=Expense(None,x,None)
        self.__repo.remove(expense)
    '''
       Function which execute the undo operation
       return: -
       '''
    def undo_list(self):
        self.__repo.undo()
    '''
       Function which returns the list of expenses
       return: list of all expenses
    '''
    def get_all_expenses(self):
        return self.__repo.get_all()