from Domain import Movie,Client,Rent,UndoAction
from Validate import Validator_movie,Validator_client
from Validate import Validator_rent
from datetime import date
import random
import copy
class Construct_Movie(object):
    def __init__(self,valid,repo,undoActions,redoActions):
        self.__valid=valid
        self.__repo=repo
        self.__undoActions=undoActions
        self.__redoActions=redoActions
    def search_movieid(self,movied):
        l=self.get_all_movies()
        List=[]
        for i in l:
            if str(i.get_movieid()).find(str(movied))!=-1:
                List.append(i)
        return List
    def search_title(self,movieTitle):
        l=self.get_all_movies()
        List=[]
        for i in l:
            if str(i.get_title()).lower().find(str(movieTitle).lower())!=-1:
                List.append(i)
        return List
    def search_description(self,movieDescription):
        l=self.get_all_movies()
        List=[]
        for i in l:
            if str(i.get_description()).lower().find(str(movieDescription).lower())!=-1:
                List.append(i)
        return List
    def search_genre(self,movieGenre):
        l=self.get_all_movies()
        List=[]
        for i in l:
            if str(i.get_genre()).lower().find(str(movieGenre).lower())!=-1:
                List.append(i)
        return List
    def random_movie(self,x):
        t=["The Hobbit","Avengers","Robinson Crusoe","Spider-Man","Divergent","A Star is born","The Maze Runner"]
        d=["amazing","awesome","captivating","boring","interesting"]
        g=["adventure movie","sf movie","romantic movie","horror movie","dystopian world"]
        for i in range(x):
            movie_id=random.randint(1,1000)
            title=t[random.randint(0,int(len(t))-1)]
            description=d[random.randint(0,int(len(d))-1)]
            genre=g[random.randint(0,int(len(g))-1)]
            movie=Movie(movie_id,title,description,genre)
            self.__repo.add(movie)
    def add_movie_element(self,movie_id,title,description,genre):
        """
        this function create a movie element
        then the movie element is verificated
        if it is a good one then it is added to list
        otherwise an error is displayed
        """
        movie=Movie(movie_id,title,description,genre)
        self.__valid.validate_movie(movie)
        self.__repo.add(movie)
        action = UndoAction(self.__repo.remove,self.__repo.add,movie,None)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def remove_movie_element(self,idmovie):
        """
        this function remove a movie element
        then the movie element is verificated
        if it is a good one then it is removed from list
        otherwise an error is displayed
        """
        movie=Movie(idmovie,None,None,None)
        movie2=self.__repo.search(movie)
        self.__repo.remove(movie)
        action=UndoAction(self.__repo.add, self.__repo.remove,movie2,None)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def update_movie_element(self,movied,title,description,genre):
        """
        this function update a movie element
        then the movie element is verificated
        if it is a good one then it is updated
        otherwise an error is displayed
        """
        movie=Movie(movied,title,description,genre)
        self.__valid.validate_movie(movie)
        movie3=Movie(movied,title,description,genre)
        movie2=self.__repo.search(movie3)
        self.__repo.update(movie)
        action=UndoAction(self.__repo.update, self.__repo.update,movie2,movie)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def search_movie_by_id(self,movid):
        """
        this function search a movie element
        if the movie element exists then it is returned
        otherwise an error message is displayed
        """
        movie=Movie(movid,None,None,None)
        return self.__repo.search(movie)
    def all_movies(self):
        return self.__repo.number_of_elements() 
    def get_all_movies(self):
        return self.__repo.get_all()
    def most_rented(self,List):
        movie_list=List
        all_movies=self.__repo.get_all()
        for i in range(len(movie_list)):
            for j in all_movies:
                if j.get_movieid()==movie_list[i][0]:
                    movie_list[i][0]=j.get_title()
        return movie_list
    def late_rentals(self,List):
        movie_list=List
        all_movies=self.__repo.get_all()
        for i in range(len(movie_list)):
            for j in all_movies:
                if j.get_movieid()==movie_list[i][0]:
                    movie_list[i][0]=j.get_title()
        return movie_list
class Construct_Client(object):
    def __init__(self,validClient,repoClient,undoActions,redoActions):
        self.__validClient=validClient
        self.__repoClient=repoClient
        self.__undoActions=undoActions
        self.__redoActions=redoActions
    def search_clientid(self,clientid):
        l=self.get_all_clients()
        List=[]
        for i in l:
            if str(i.get_clientid()).find(str(clientid))!=-1:
                List.append(i)
        return List
    def search_name(self,clientName):
        l=self.get_all_clients()
        List=[]
        for i in l:
            if str(i.get_name()).lower().find(str(clientName).lower())!=-1:
                List.append(i)
        return List
    def random_client(self,x):
        n=["Vlad","Georgiana","Ana","Calin","Andrei","Izabella"]
        for i in range(x):
            client_id=random.randint(1,1000)
            name=n[random.randint(0,int(len(n))-1)]
            client=Client(client_id,name)
            self.__repoClient.add(client)
    def add_client_element(self,clientid,name):
        """
        this function create a client element
        then the cleint element is verificated
        if it is a good one then it is added to list
        otherwise an error is displayed
        """
        client=Client(clientid,name)
        self.__validClient.validate_client(client)
        self.__repoClient.add(client)
        action = UndoAction(self.__repoClient.remove, self.__repoClient.add,client,None)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def remove_client_element(self,clientid):
        """
        this function create a client element
        then the client element is verificated
        if it is a good one then it is removed from the list
        otherwise an error is displayed
        """
        client=Client(clientid,None)
        client=self.__repoClient.remove(client)
        action = UndoAction(self.__repoClient.add, self.__repoClient.remove,client,None)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def update_client_element(self,clientid,name):
        """
        this function update a client element
        a client element is created
        if it is a good one then it is updated
        otherwise an error is displayed
        """
        client=Client(clientid,name)
        self.__validClient.validate_client(client)
        client3=Client(clientid,None)
        client2=self.__repoClient.search(client3)
        self.__repoClient.update(client)
        action = UndoAction(self.__repoClient.update, self.__repoClient.update,client2,client)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def no_of_clients(self):
        return self.__repoClient.number_of_elements()
    def search_client_by_id(self,clientid):
        client=Client(clientid,None)
        return self.__repoClient.search(client)
    def get_all_clients(self):
        return self.__repoClient.get_all()
    def most_active(self,List):
        client_list=List
        all_clients=self.__repoClient.get_all()
        for i in range(len(client_list)):
            for j in all_clients:
                if j.get_clientid()==client_list[i][0]:
                    client_list[i][0]=j.get_name()
        return client_list
    def get_client_history(self):
        return self.__repoClient.get_history()
class Construct_Rent(object):
    def __init__(self,validRent,repoMovie,repoClient,repoRent,undoActions,redoActions):
        self.__validRent=validRent
        self.__repoMovie=repoMovie
        self.__repoClient=repoClient
        self.__repoRent=repoRent
        self.__undoActions=undoActions
        self.__redoActions=redoActions
    def add_rent(self,rentid,movieid,clientid,rented_date,due_date,returned_date):
        rent=Rent(rentid,movieid,clientid,rented_date,due_date,returned_date)
        clientidd=Client(clientid,None)
        self.__repoClient.search(clientidd)
        movieid=Movie(movieid,None,None,None)
        self.__repoMovie.search(movieid)
        clients=[]
        l=self.__repoRent.get_all()
        for i in range(len(l)):
            if l[i].get_clientid()==rent.get_clientid():
               clients.append(l[i])
        movies=[]
        l=self.__repoRent.get_all()
        for i in range(len(l)):
            if l[i].get_movieid()==rent.get_movieid():
                movies.append(l[i])
        self.__validRent.validate_rent(rent,movies,clients)
        self.__repoRent.add(rent)
        rent=copy.deepcopy(rent)
        action = UndoAction(self.__repoRent.remove, self.__repoRent.add,rent,None)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def return_movie(self,rentid,movieid,clientid,rented_date,due_date,returned_date):
        q=Rent(rentid,movieid,clientid,rented_date,due_date,returned_date)
        k=Rent(rentid,None,None,None,None,None)
        rent2=self.__repoRent.search(q)
        rent3=copy.deepcopy(rent2)
        rent=self.__repoRent.search(k)
        rent.set_returned_date(returned_date)
        l=self.__repoRent.search(q)
        self.__validRent.validate_return(rent,l)
        self.__repoRent.update(rent)
        rent=copy.deepcopy(rent)
        action = UndoAction(self.__repoRent.update, self.__repoRent.update,rent3,rent)
        self.__undoActions.push(action)
        self.__redoActions.clear()
    def get_all_rents(self):
        return self.__repoRent.get_all()
    def most_rented(self):
        movies=self.__repoRent.get_all()
        movie_list=[]
        for l in movies:
            returned_date=l.get_returned_date()
            if type(returned_date)==str:
                due_date=l.get_due_date()
            else:
                due_date=l.get_returned_date()
            d=date(2019,int(due_date[1]),int(due_date[0]))
            rent_date=l.get_rented_date()
            r=date(2019,int(rent_date[1]),int(rent_date[0]))
            delta=d-r
            nr_of_days=delta.days
            nr_of_days+=1
            i=0
            g=0
            while i<len(movie_list):
                if movie_list[i][0]==l.get_movieid():
                    movie_list[i][1]+=nr_of_days
                    i=len(movie_list)
                    g=1
                else:
                    i+=1
            if g==0:
                movieId=l.get_movieid()
                movie_list.append([movieId,nr_of_days])
        for i in range(len(movie_list)-1):
            for j in range(i+1,len(movie_list)):
                if movie_list[i][1]<movie_list[j][1]:
                    aux=[]
                    aux=movie_list[i]
                    movie_list[i]=movie_list[j]
                    movie_list[j]=aux
        return movie_list
    def active_clients(self):
        clients=self.__repoRent.get_all()
        client_list=[]
        for l in clients:
            returned_date=l.get_returned_date()
            if type(returned_date)==str:
                due_date=l.get_due_date()
            else:
                due_date=l.get_returned_date()
            d=date(2019,int(due_date[1]),int(due_date[0]))
            rent_date=l.get_rented_date()
            r=date(2019,int(rent_date[1]),int(rent_date[0]))
            delta=d-r
            nr_of_days=delta.days
            nr_of_days+=1
            i=0
            g=0
            while i<len(client_list):
                if client_list[i][0]==l.get_clientid():
                    client_list[i][1]+=nr_of_days
                    i=len(client_list)
                    g=1
                else:
                    i+=1
            if g==0:
                clientId=l.get_clientid()
                client_list.append([clientId,nr_of_days])
        for i in range(len(client_list)-1):
            for j in range(i+1,len(client_list)):
                if client_list[i][1]<client_list[j][1]:
                    aux=[]
                    aux=client_list[i]
                    client_list[i]=client_list[j]
                    client_list[j]=aux
        return client_list
    def late_rentals(self):
        movies=self.__repoRent.get_all()
        movie_list=[]
        for l in movies:
            returned_date=l.get_returned_date()
            if type(returned_date)!=str:
                due_date=l.get_returned_date()
                d=date(2019,int(due_date[1]),int(due_date[0]))
                rent_date=l.get_rented_date()
                r=date(2019,int(rent_date[1]),int(rent_date[0]))
                delta=d-r
                nr_of_days=delta.days
                nr_of_days+=1
                i=0
                g=0
                while i<len(movie_list):
                    if movie_list[i][0]==l.get_movieid():
                        movie_list[i][1]+=nr_of_days
                        i=len(movie_list)
                        g=1
                    else:
                        i+=1
                if g==0:
                    movieId=l.get_movieid()
                    movie_list.append([movieId,nr_of_days])
        for i in range(len(movie_list)-1):
            for j in range(i+1,len(movie_list)):
                if movie_list[i][1]<movie_list[j][1]:
                    aux=[]
                    aux=movie_list[i]
                    movie_list[i]=movie_list[j]
                    movie_list[j]=aux
        return movie_list
class Construct_Undo(object):
    
    def __init__(self, undoActions, redoActions):
        self.__undoActions = undoActions
        self.__redoActions = redoActions

    def undo(self):
        action = self.__undoActions.pop()
        action.execute()
        rev_action = action.get_reverse()
        self.__redoActions.push(rev_action)
    
    def redo(self):
        action = self.__redoActions.pop()
        action.execute2()
        rev_action = action.get_reverse()
        self.__undoActions.push(rev_action)