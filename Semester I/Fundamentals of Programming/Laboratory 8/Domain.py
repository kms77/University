class Movie(object):
    """
    this is the class of movie objects 
    it contains getters and setters for a movie objects
    """
    def __init__(self,movieid,title,description,genre):
        self.__movieid=movieid
        self.__title=title
        self.__description=description
        self.__genre=genre
    def get_movieid(self):
        return self.__movieid
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_genre(self):
        return self.__genre
    def set_movieid(self,value):
        self.__movieid=value
    def set_title(self,value):
        self.__title=value
    def set_description(self,value):
        self.__description=value
    def set_genre(self,value):
        self.__genre=value
    def __eq__(self,other):
        return self.__movieid==other.__movieid
    def __hash__(self):
        return id(self)
    @staticmethod
    def read_movie(line):
        parts = line.split(",")
        return Movie(int(parts[0]), parts[1],parts[2],parts[3])
    @staticmethod
    def write_movie(movie):
        return str(movie.get_movieid()) + "," + str(movie.get_title())+","+str(movie.get_description())+","+str(movie.get_genre())
    def __str__(self):
        return "----------------"+'\n'+"Movie:"+'\n'+"Id:"+str(self.__movieid)+'\n'+"Title:"+str(self.__title)+'\n'+"Description:"+str(self.__description)+'\n'+"Genre:"+str(self.__genre)+'\n'+"----------------"
class Client(object):
    """
    this is the class of client objects 
    it contains getters and setters for a client object
    """
    def __init__(self,clientid,name):
        self.__clientid=clientid
        self.__name=name
    def get_clientid(self):
        return self.__clientid
    def get_name(self):
        return self.__name
    def set_clientid(self,value):
        self.__clientid=value
    def set_name(self,value):
        self.__name=value
    def __eq__(self,other):
        return self.__clientid==other.__clientid
    def __hash__(self):
        return id(self)
    def __str__(self):
        return "----------------"+'\n'+"Client:"+'\n'+"Id:"+str(self.__clientid)+'\n'+"Name:"+str(self.__name)+'\n'+"----------------"
    @staticmethod
    def read_client(line):
        parts = line.split(",")
        return Client(int(parts[0]), parts[1])
    @staticmethod
    def write_client(client):
        return str(client.get_clientid()) + "," + str(client.get_name())
class Rent(object):
    def __init__(self,rentalid,movieid,clientid,rented_date,due_date,returned_date):
        self.__rentalid=rentalid
        self.__movieid=movieid
        self.__clientid=clientid
        self.__rented_date=rented_date
        self.__due_date=due_date
        self.__returned_date=returned_date
    def get_clientid(self):
        return self.__clientid
    def get_movieid(self):
        return self.__movieid
    def get_rented_date(self):
        return self.__rented_date
    def get_due_date(self):
        return self.__due_date
    def get_returned_date(self):
        return self.__returned_date
    def get_rentalid(self):
        return self.__rentalid
    def set_clientid(self,value):
        self.__clientid=value
    def set_movieid(self,value):
        self.__movieid=value
    def set_rentalid(self,value):
        self.__rentalid=value
    def set_rented_date(self,value):
        self.__rented_date=value
    def set_due_date(self,value):
        self.__due_date=value
    def set_returned_date(self,value):
        self.__returned_date=value
    def __eq__(self,other):
        return self.__rentalid==other.__rentalid
    @staticmethod
    def read_rent(line):
        parts = line.split(",")
        return Rent(int(parts[0]),int(parts[1]),int(parts[2]),parts[3],parts[4],parts[5])
    @staticmethod
    def write_rent(rent):
        return str(rent.get_rentalid())+","+str(rent.get_movieid())+","+str(rent.get_clientid())+","+str(rent.get_rented_date())+","+str(rent.get_due_date())+","+str(rent.get_returned_date())
    def __str__(self):
        return "----------------"+'\n'+"Rent:"+'\n'+"Rent id:"+str(self.__rentalid)+'\n'+"Client id:"+str(self.__clientid)+'\n'+"Movie id:"+str(self.__movieid)+'\n'+"Rent date:"+str(self.__rented_date)+'\n'+"Due date:"+str(self.__due_date)+'\n'+"Returned date:"+str(self.__returned_date)+'\n'+"----------------"
class GradeDTO(object):
    
    def __init__(self, movie, client,value):
        self.__movie_name = movie
        self.__client_name = client
        self.__value=value
    def __str__(self):
        return self.__movie_name + " was rented by "+ self.__client_name + " in the date:"+ self.__value
class UndoAction:
    def __init__(self, action, rev_action, obj,obj2):
        self.__action = action
        self.__rev_action = rev_action
        self.__obj = obj
        self.__obj2=obj2
    def execute(self):
        self.__action(self.__obj)
    def execute2(self):
        if self.__obj2 is None:
            self.__action(self.__obj)
        else:
            self.__action(self.__obj2)
    def get_reverse(self):
            return UndoAction(self.__rev_action, self.__action, self.__obj,self.__obj2)