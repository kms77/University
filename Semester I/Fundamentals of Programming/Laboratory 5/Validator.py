class ValidateExpense:
    def validate(self,expense):
        """
         the function which verifies if an element is valid or not
         raise an exception if it is not a good element
        otherwise-add to list of elements
        """
        errors=""
        if expense.get_day()<1 or expense.get_day()>30:
            errors+="Invalid day!\n"
        if expense.get_money()<1:
            errors+="Invalid amount of money!\n"
        if expense.get_extype()=="":
            errors+="Invalid type of expense!\n"
        if len(errors)>0:
            raise Exception(errors)