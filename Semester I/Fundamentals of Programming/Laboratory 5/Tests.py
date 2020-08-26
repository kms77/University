from Domain import Expense
from Repository import RepoExpense
from Validator import ValidateExpense
from Service import ServiceExpense
class Test:
    def test_create_expense(self):
        expense=Expense(23,56,"transport")
        assert(expense.get_day()==23)
        assert(expense.get_money()==56)
        assert(expense.get_extype()=="transport")
        expense.set_day(3)
        assert(expense.get_day()==3)
        expense.set_money(50)
        assert(expense.get_money()==50)
        expense.set_extype("others")
        assert(expense.get_extype()=="others")
    def test_validator_expense(self):
        validExpense=ValidateExpense()
        expense=Expense(23,56,"transport")
        validExpense.validate(expense)
        expense2=Expense(-30,2,"food")
        try:
            validExpense.validate(expense2)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Invalid day!\n")
        expense3=Expense(20,-6,"")
        try:
            validExpense.validate(expense3)
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Invalid amount of money!\nInvalid type of expense!\n")
    def test_repo_expenses(self):
        repo=RepoExpense()
        assert(repo.size()==0)
        expense=Expense(23,56,"tranport")
        repo.add(expense)
        assert(repo.size()==1)
        expense=Expense(None,60,None)
        repo.remove(expense)
        assert(repo.size()==0)
    def test_service_books(self):
        repoExpense=RepoExpense()
        validExpense=ValidateExpense()
        serv=ServiceExpense(repoExpense,validExpense)
        assert(serv.get_no_of_expenses()==0)
        serv.add_expenses(3,20,"transport")
        assert(serv.get_no_of_expenses()==1)
        try:
            serv.add_expenses(-2,-4,"food")
            assert(False)
        except Exception as ex:
            assert(str(ex)=="Invalid day!\nInvalid amount of money!\n")
    def all_tests(self):
        self.test_create_expense()
        self.test_validator_expense()
        self.test_repo_expenses()
        self.test_service_books()


         