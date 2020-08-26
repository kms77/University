from Service import ServiceExpense
class Console:
    '''
    Add a new expense to the list if it is a valid one
    return: -
    '''
    def __ui_add_expense(self):
        try:
            day=int(input("Day:"))
        except ValueError as ve:
            print("Invalid day!\n")
            return
        try:
            money=int(input("Amount of money:"))
        except ValueError as ve:
            print("Invalid money!\n")
            return
        extype=str(input("Type of expense:"))
        self.__serv.add_expenses(day,money,extype)
    '''
    This function prints the list of expenses
    '''
    def __ui_print_expense(self):
        expenses=self.__serv.get_all_expenses()
        if len(expenses)==0:
            print("The list is empty!\n")
        else:
            for expense in expenses:
                print(expense)
    '''
    It filters the list of elements by a given input
    '''
    def __ui_filter_list(self):
        try:
            x=int(input("Choose the value:"))
        except ValueError as ve:
            print("Invalid value!\n")
        self.__serv.filter_list(x)
    '''
    Function which is called for undo operation
    '''
    def __ui_undo(self):
        self.__serv.undo_list()
    '''
    This function generates 10 examples of inputs
    '''
    def __examples(self):
        x=[]
        self.__serv.examples(x)
    def __init__(self,serv):
        self.__serv=serv
    def print_menu(self):
        print("---------List of Expenses-----------")
        print("------------------------------------")
        print("1.Add a new expense;")
        print("2.Display the list of expenses;")
        print("3.Filter by amount of money;")
        print("4.Undo")
        print("x.Exit")
        print("------------------------------------")
    def run(self):
        self.__examples()
        self._commands={'1':self.__ui_add_expense,'2':self.__ui_print_expense,'3':self.__ui_filter_list,'4':self.__ui_undo}
        while True:
            self.print_menu()
            cmd=str(input("Choose a command:")).strip()
            if (cmd=='x'):
                print("Program closed ")
                return
            if cmd not in self._commands:
                print("It is not a valid command")
            else:
                try:
                    self._commands[cmd]()
                except Exception as ex:
                    print(ex)
