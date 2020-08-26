from Tests import Test
from Service import ServiceExpense
from Validator import ValidateExpense
from Repository import RepoExpense
from UI import Console
test=Test()
test.all_tests()
validExpense=ValidateExpense()
repoExpense=RepoExpense()
serviceExpense=ServiceExpense(repoExpense,validExpense)
ui=Console(serviceExpense)
ui.run()