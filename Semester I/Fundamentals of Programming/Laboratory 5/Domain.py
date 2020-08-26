class Expense:
    """
     the class of getters and setters
     every function provides a getter or a setter for an element of the object
    """
    def __init__(self,day,money,extype):
        self.__day=day
        self.__money=money
        self.__extype=extype
    def get_day(self):
        return self.__day
    def get_money(self):
        return self.__money
    def get_extype(self):
        return self.__extype
    def set_day(self,value):
        self.__day=value
    def set_money(self,value):
        self.__money=value
    def set_extype(self,value):
        self.__extype=value
    def __eq__(self, value):
        return self.__money==value.__money
    def __lt__(self,other):
        return self.__money<other.__money
    def __str__(self):
        return "Day:"+str(self.__day)+" || "+"Amount of money:"+str(self.__money)+"||"+"Type of expense:"+self.__extype
    