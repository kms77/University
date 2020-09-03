import collections
from Exceptions import RepoError,ValidError,UndoError
class Console:
    def __init__(self,Movie,Client,Rent,Undo):
        self.__Movie=Movie
        self.__Client=Client
        self.__Rent=Rent
        self.__Undo=Undo
    def __printMenu(self):
        print("------------------------------------")
        print("------------Movie-rental------------")
        print("------------------------------------")
        print("1.Manage the list of movies;")
        print("2.Manage the list of clients;")
        print("------------------------------------")
        print("3.Rent a movie;")
        print("4.Return a movie;")
        print("5.Display the list of rents;")
        print("------------------------------------")
        print("6.Search for a client;")
        print("7.Search for a movie;")
        print("------------------------------------")
        print("8.Most rented movies;")
        print("9.Most active client;")
        print("10.Late rentals;")
        print("------------------------------------")
        print("11.Undo;")
        print("12.Redo;")
        print("------------------------------------")
        print("x.To close the program;")
        print("------------------------------------")
    def __menu_movie(self):
        print("------------------------------------")
        print("1.Add a new movie;")
        print("2.Remove a movie;")
        print("3.Update a movie;")
        print("4.Display the list of movies;")
        print("x.Exit")
        print("------------------------------------")
    def __menu_client(self):
        print("------------------------------------")
        print("1.Add a new client;")
        print("2.Remove a client;")
        print("3.Update a client;")
        print("4.Display the list of client;")
        print("x.Exit")
        print("------------------------------------")
    def __menu_search_client(self):
        print("------------------------------------")
        print("1.Search client by id;")
        print("2.Search client by name;")
        print("x.Exit")
        print("------------------------------------")
    def __menu_search_movie(self):
        print("------------------------------------")
        print("1.Search movie by id;")
        print("2.Search movie by title;")
        print("3.Search movie by description;")
        print("4.Search movie by genre;")
        print("x.Exit")
        print("------------------------------------")
    def __add_movie(self):
        """
        this function calls the add function from service 
        if the input is invalid than ui errors is show 
        """
        movie_id=input("Movie id:")
        try:
            movie_id=int(movie_id)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        title=input("Title:")
        description=input("Description:")
        genre=input("Genre:")
        self.__Movie.add_movie_element(movie_id,title,description,genre)
    def __remove_movie(self):
        """
        this function calls the remove function from service 
        if the input is invalid than ui errors is show 
        """
        idmovie=input("Movie id:")
        try:
            idmovie=int(idmovie)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        self.__Movie.remove_movie_element(idmovie)
    def __update_movie(self):
        """
        this function calls the update function from service 
        if the input is invalid than ui errors is show 
        """
        movie_id=input("Movie id:")
        try:
            movie_id=int(movie_id)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        title=input("Title:")
        description=input("Description:")
        genre=input("Genre:")
        self.__Movie.update_movie_element(movie_id,title,description,genre)
    def __display_movie(self):
        """
        this function display the list of movies 
        if the list is empty than an error message is show
        """
        movies=self.__Movie.get_all_movies()
        if len(movies)==0:
            raise ValueError("The list of movies is empty!\n")
        else:
            for movie in movies:
                print(movie)
    def __add_client(self):
        """
        this function calls the add function from service 
        if the input is invalid than ui errors is show 
        """
        client_id=input("Client id:")
        try:
            client_id=int(client_id)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        name=input("Name:")
        self.__Client.add_client_element(client_id,name)
    def __remove_client(self):
        """
        this function calls the remove function from service 
        if the input is invalid than ui errors is show 
        """
        idclient=input("Movie id:")
        try:
            idclient=int(idclient)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        self.__Client.remove_client_element(idclient)
    def __update_client(self):
        """
        this function calls the update function from service 
        if the input is invalid than ui errors is show 
        """
        client_id=input("Client id:")
        try:
            client_id=int(client_id)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        name=input("Name:")
        self.__Client.update_client_element(client_id,name)
    def __display_client(self):
        """
        this function display the list of clients 
        if the list is empty an error message is show 
        """
        clients=self.__Client.get_all_clients()
        if len(clients)==0:
            raise ValueError("The list of clients is empty!\n")
        else:
            for client in clients:
                print(client)
    def __rent_movie(self):
        rentid=input("Id of the rent:")
        try:
            rentid=int(rentid)
        except ValueError as ve:
            raise ValueError("Invalid rent id!\n")
        movieid=input("Id of the movie:")
        try:
            movieid=int(movieid)
        except ValueError as ve:
            raise ValueError("Invalid movie id!\n")
        clientid=input("Id of the client:")
        try:
            clientid=int(clientid)
        except ValueError as ve:
            raise ValueError("Invalid client id!\n")
        rented_date=input("Rented date(day/month):")
        rented_date=rented_date.split('/')
        if len(rented_date)!=2:
            raise ValueError("Invalid data!\n")
        try:
            rented_date[0]=int(rented_date[0])
        except ValueError as ve:
            raise ValueError("Invalid day!\n")
        try:
            rented_date[1]=int(rented_date[1])
        except ValueError as ve:
            raise ValueError("Invalid month!\n")
        due_date=input("Due date(day/month):")
        due_date=due_date.split('/')
        if len(due_date)!=2:
            raise ValueError("Invalid data!\n")
        try:
            due_date[0]=int(due_date[0])
        except ValueError as ve:
            raise ValueError("Invalid day!\n")
        try:
            due_date[1]=int(due_date[1])
        except ValueError as ve:
            raise ValueError("Invalid month!\n")
        returned_date="Not returned!"
        self.__Rent.add_rent(rentid,movieid,clientid,rented_date,due_date,returned_date)
    def __return_movie(self):
        rentid=input("Id of the rent:")
        try:
            rentid=int(rentid)
        except ValueError as ve:
            raise ValueError("Invalid rentid id!\n")
        returned_date=input("Returned date(day/month):")
        returned_date=returned_date.split('/')
        if len(returned_date)!=2:
            raise ValueError("Invalid data!\n")
        try:
            returned_date[0]=int(returned_date[0])
        except ValueError as ve:
            raise ValueError("Invalid day!\n")
        try:
            returned_date[1]=int(returned_date[1])
        except ValueError as ve:
            raise ValueError("Invalid month!\n")
        clientid=0
        movieid=0
        rented_date="Empty"
        due_date="Empty"
        self.__Rent.return_movie(rentid,movieid,clientid,rented_date,due_date,returned_date)
    def __print_rents(self):
            rents=self.__Rent.get_all_rents()
            if len(rents)==0:
                raise ValueError("The list of rentals is empty!\n")
            else:
                for rent in rents:
                    print(rent)
    def __clientId_search(self):
        clientid=input("Id:")
        try:
            clientid=int(clientid)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        l=[]
        l=self.__Client.search_clientid(clientid)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one id!\n")
    def __clientName_search(self):
        clientName=input("Name:")
        if clientName=="":
            raise ValueError("Invalid name!\n")
        l=[]
        l=self.__Client.search_name(clientName)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one name!\n")
    def __movieId_search(self):
        movieid=input("Id:")
        try:
            movieid=int(movieid)
        except ValueError as ve:
            raise ValueError("Invalid id!\n")
        l=[]
        l=self.__Movie.search_movieid(movieid)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one id!\n")
    def __movieTitle_search(self):
        movieTitle=input("Title:")
        if movieTitle=="":
            raise ValueError("Invalid title!\n")
        l=[]
        l=self.__Movie.search_title(movieTitle)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one title!\n")
    def __movieDescription_search(self):
        movieDescription=input("Description:")
        if movieDescription=="":
            raise ValueError("Invalid description!\n")
        l=[]
        l=self.__Movie.search_description(movieDescription)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one desciption!\n")
    def __movieGenre_search(self):
        movieGenre=input("Genre:")
        if movieGenre=="":
            raise ValueError("Invalid name!\n")
        l=[]
        l=self.__Movie.search_genre(movieGenre)
        if len(l)!=0:
            for i in l:
                print(i)
        else:
            print("No one genre!\n")
    def __most_rented_movies(self):
        List=self.__Rent.most_rented()
        if len(List)!=0:
            List=self.__Movie.most_rented(List)
            for i in range(len(List)):
                print("----------------"+'\n'+"Movie:"+str(List[i][0])+'\n'+"Number of days:"+str(List[i][1])+'\n'+"----------------")
        else:
            print("The list is empty!\n")
    def __most_active_clients(self):
        List=self.__Rent.active_clients()
        if len(List)!=0:
            List=self.__Client.most_active(List)
            for i in range(len(List)):
                print("----------------"+'\n'+"Client name:"+str(List[i][0])+'\n'+"Number of days:"+str(List[i][1])+'\n'+"----------------")
        else:
            print("The list is empty!\n")
    def __late_rentals(self):
        List=self.__Rent.late_rentals()
        if len(List)!=0:
            List=self.__Movie.late_rentals(List)
            for i in range(len(List)):
                print("----------------"+'\n'+"Movie:"+str(List[i][0])+'\n'+"Number of days:"+str(List[i][1])+'\n'+"----------------")
        else:
            print("The list is empty!\n")
    def __undo(self):
        self.__Undo.undo()
    def __redo(self):
        self.__Undo.redo()
    def start(self):
        x=10
        self.__Movie.random_movie(x)
        self.__Client.random_client(x)
        while True:
            list_of_options=["1","2","3","4","5","6","7","8","9","10","11","12"]
            self.__printMenu()
            m=input("Choose from 1 to 12:").strip()
            if (m=="x"):
                print("Program closed!")
                return 
            if m not in list_of_options:
                print("Invalid command !")
            else:
                if m=='1':
                    self.__commands={'1':self.__add_movie,'2':self.__remove_movie,'3':self.__update_movie,'4':self.__display_movie}
                    while True:
                        self.__menu_movie()
                        n=input("Choose from 1 to 4:").strip()
                        if (n=="x"):
                            print("Exit")
                            break
                        if n not in self.__commands:
                            print("Not a valid command")
                        else:
                            try:
                                self.__commands[n]()
                            except ValueError as ve:
                                print("UI error:\n"+str(ve))
                            except ValidError as val:
                                print("Value error:\n"+str(val))
                            except RepoError as re:
                                print("Repo error:\n"+str(re))
                elif m=='2':
                    self.__commands={'1':self.__add_client,'2':self.__remove_client,'3':self.__update_client,'4':self.__display_client}
                    while True:
                        self.__menu_client()
                        n=input("Choose from 1 to 4:").strip()
                        if (n=="x"):
                            print("Exit")
                            break
                        if n not in self.__commands:
                            print("Not a valid command")
                        else:
                            try:
                                self.__commands[n]()
                            except ValueError as ve:
                                print("UI error:\n"+str(ve))
                            except ValidError as val:
                                print("Value error:\n"+str(val))
                            except RepoError as re:
                                print("Repo error:\n"+str(re))
                elif m=='3':
                    try:
                        self.__rent_movie()
                    except ValueError as ve:
                            print("UI error:\n"+str(ve))
                    except ValidError as val:
                            print("Value error:\n"+str(val))
                    except RepoError as re:
                            print("Repo error:\n"+str(re))
                elif m=='4':
                    try:
                        self.__return_movie()
                    except ValueError as ve:
                            print("UI error:\n"+str(ve))
                    except ValidError as val:
                            print("Value error:\n"+str(val))
                    except RepoError as re:
                            print("Repo error:\n"+str(re))
                elif m=="5":
                    try:
                        self.__print_rents()
                    except ValueError as ve:
                        print("UI error:\n"+str(ve))
                elif m=='6':
                    self.__commands={'1':self.__clientId_search,'2':self.__clientName_search}
                    while True:
                        self.__menu_search_client()
                        n=input("Choose from 1 to 2:").strip()
                        if (n=="x"):
                            print("Exit")
                            break
                        if n not in self.__commands:
                            print("Not a valid command")
                        else:
                            try:
                                self.__commands[n]()
                            except ValueError as ve:
                                print("UI error:\n"+str(ve))
                            except ValidError as val:
                                print("Value error:\n"+str(val))
                            except RepoError as re:
                                print("Repo error:\n"+str(re))
                elif m=='7':
                    self.__commands={'1':self.__movieId_search,'2':self.__movieTitle_search,'3':self.__movieDescription_search,'4':self.__movieGenre_search}
                    while True:
                        self.__menu_search_movie()
                        n=input("Choose from 1 to 4:").strip()
                        if (n=="x"):
                            print("Exit")
                            break
                        if n not in self.__commands:
                            print("Not a valid command")
                        else:
                            try:
                                self.__commands[n]()
                            except ValueError as ve:
                                print("UI error:\n"+str(ve))
                            except ValidError as val:
                                print("Value error:\n"+str(val))
                            except RepoError as re:
                                print("Repo error:\n"+str(re))
                elif m=='8':
                    self.__most_rented_movies()
                    pass
                elif m=='9':
                    self.__most_active_clients()
                elif m=='10':
                    self.__late_rentals()
                elif m=='11':
                    try:
                        self.__undo()
                    except UndoError as un:
                        print("Undo error:\n"+str(un))
                else:
                    try:
                        self.__redo()
                    except UndoError as un:
                        print("Redo error:\n"+str(un))