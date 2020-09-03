from Domain import Movie,Client,Rent
from Validate import Validator_movie,Validator_client
from Validate import Validator_rent
from datetime import date
import random
import copy
class Construct_Movie(object):
    def __init__(self,valid,repo):
        self.__valid=valid
        self.__repo=repo
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
class Construct_Client(object):
    def __init__(self,validClient,repoClient):
        self.__validClient=validClient
        self.__repoClient=repoClient
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
    def remove_client_element(self,clientid):
        """
        this function create a client element
        then the client element is verificated
        if it is a good one then it is removed from the list
        otherwise an error is displayed
        """
        client=Client(clientid,None)
        client=self.__repoClient.remove(client)
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
    def no_of_clients(self):
        return self.__repoClient.number_of_elements()
    def search_client_by_id(self,clientid):
        client=Client(clientid,None)
        return self.__repoClient.search(client)
    def get_all_clients(self):
        return self.__repoClient.get_all()
    def get_client_history(self):
        return self.__repoClient.get_history()
class Construct_Rent(object):
    def __init__(self,validRent,repoMovie,repoClient,repoRent):
        self.__validRent=validRent
        self.__repoMovie=repoMovie
        self.__repoClient=repoClient
        self.__repoRent=repoRent
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
    def get_all_rents(self):
        return self.__repoRent.get_all()