from Domain import Movie,Client
from Validate import Validator_movie,Validator_client
from Service import Construct_Movie,Construct_Client
from Repository import Repo_movie
from Exceptions import RepoError,ValidError
class Test(object):
    def __int__(self):
        pass
    def test_create_movie(self):
        movie=Movie(1,"The Lord of the Rings","The story of the hobbit Frodo Baggins in a fictional word.","epic fantasy adventure film")
        assert(movie.get_movieid()==1)
        assert(movie.get_title()=="The Lord of the Rings")
        assert(movie.get_description()=="The story of the hobbit Frodo Baggins in a fictional word.")
        assert(movie.get_genre()=="epic fantasy adventure film")
        movie.set_movieid(3)
        assert(movie.get_movieid()==3)
        movie.set_title("Avengers")
        assert(movie.get_title()=="Avengers")
        movie.set_description("The members of the Avengers attempt to reverse the damage caused by Thanos.")
        assert(movie.get_description()=="The members of the Avengers attempt to reverse the damage caused by Thanos.")
        movie.set_genre("superhero film")
        assert(movie.get_genre()=="superhero film")
        self.__movie=movie
    def test_validator_movie(self):
        validMovie=Validator_movie()            
        self.__movie=Movie(1,"The Lord of the Rings","The story of the hobbit Frodo Baggins in a fictional word.","epic fantasy adventure film")
        validMovie.validate_movie(self.__movie)
        self.__movie2=Movie(-2,"Home Alone","The eight year old Kevin McCaliister is mistakenly left behind by him family.","comedy film")
        try:
            validMovie.validate_movie(self.__movie2)
            assert(False)
        except ValidError as val:               
            assert(str(val)=="Invalid id!\n")
        self.__movie3=Movie(1,"The Lord of the Rings","","epic fantasy adventure film")
        try:
            validMovie.validate_movie(self.__movie3)
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid description!\n")
        self.__movie4=Movie(1,"The Lord of the Rings","The story of the hobbit Frodo Baggins in a fictional word.","")
        try:
            validMovie.validate_movie(self.__movie4)
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid genre!\n")
        self.__validMovie=validMovie
    def test_repo_movie(self):
        repo = Repo_movie()
        assert(repo.number_of_elements() == 0)
        repo.add(self.__movie)
        assert(repo.number_of_elements() == 1)
        keymovie = Movie(self.__movie.get_movieid(), None,None,None)
        findmovie = repo.search(keymovie)
        assert(findmovie.get_title() == self.__movie.get_title())
        self.__movie_dif_title_same_id=Movie(1,"Home Alone","The eight year old Kevin McCaliister is mistakenly left behind by him family.","comedy film")
        try:
            repo.add(self.__movie_dif_title_same_id)
            assert(False)
        except RepoError as re:
            assert(str(re) == "Existing id!\n")
        self.__inexisting_student = Movie(21,"Home Alone","The eight year old Kevin McCaliister is mistakenly left behind by him family.","comedy film")
        try:
            repo.search(self.__inexisting_student)
            assert(False)
        except RepoError as re:
            assert(str(re) == "Inexisting id!\n")
        movie=Movie(None,None,None,None)
        movies = repo.get_all()
        self.__repo=repo
    def test_service_movie(self):
        repoMovie = Repo_movie()
        validMovie = Validator_movie()
        self.__serv=Construct_Movie(validMovie,repoMovie)
        assert(self.__serv.all_movies()==0)
        self.__serv.add_movie_element(1,"The Lord of the Rings","The story of the hobbit Frodo Baggins in a fictional word.","epic fantasy adventure film")
        assert(self.__serv.all_movies()==1)
        movie=self.__serv.search_movie_by_id(1)
        assert(movie.get_title()=="The Lord of the Rings")
        assert(movie.get_description()=="The story of the hobbit Frodo Baggins in a fictional word.")
        assert(movie.get_genre()=="epic fantasy adventure film")
        try:
            self.__serv.add_movie_element(-2,"","Description","action")
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid id!\nInvalid title!\n")
        try:
            self.__serv.add_movie_element(1,"Zlatan","The story of Zlatan.","action film")
            assert(False)
        except RepoError as re:
            assert(str(re)=="Existing id!\n")
        try:
            self.__serv.update_movie_element(2,"Zlatan","The story of Zlatan.","action film")
            assert(False)
        except RepoError as re:
            assert(str(re)=="Inexisting id!\n")
        self.__serv.update_movie_element(1,"Zlatan","The story of Zlatan.","action film")
        assert(self.__serv.all_movies()==1)
        movie = self.__serv.search_movie_by_id(1)
        assert(movie.get_title()=="Zlatan")
        assert(movie.get_description()=="The story of Zlatan.")
        assert(movie.get_genre()=="action film")
        self.__serv.remove_movie_element(1)
        assert(self.__serv.all_movies()==0)
        try:
            self.__serv.remove_movie_element(1)
            assert(False)
        except RepoError as re:
            assert(str(re)=="Inexisting id!\n")
    def test_create_client(self):
        client_id=22
        name="Dan"
        client=Client(client_id,name)
        assert(client.get_clientid()==22)
        assert(client.get_name()=="Dan")
        client.set_clientid(21)
        assert(client.get_clientid()==21)
        client.set_name("Flavius")
        assert(client.get_name()=="Flavius")
        self.__client=client
    def test_validator_client(self):
        validatorClient=Validator_client()
        validatorClient.validate_client(self.__client)
        self.__clientid=Client(-23,"Dan")
        self.__clientname=Client(23,"")
        self.__client=Client(-23,"")
        try:
            validatorClient.validate_client(self.__clientid)
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid id!\n")
        try:
            validatorClient.validate_client(self.__clientname)
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid name!\n")
        try:
            validatorClient.validate_client(self.__client)
            assert(False)
        except ValidError as val:
            assert(str(val)=="Invalid id!\nInvalid name!\n")
    def test_repo_client(self):
        repo=Repo_movie()
        assert(repo.number_of_elements()==0)
        self.__client=Client(22,"Dan")
        repo.add(self.__client)
        assert(repo.number_of_elements()==1)
        keyClient=Client(self.__client.get_clientid(),None)
        foundClient=repo.search(keyClient)
        assert(foundClient.get_name()==self.__client.get_name())
        self.__clientSameid=Client(22,"Alex")
        try:
            repo.add(self.__clientSameid)
            assert(False)
        except RepoError as re:
            assert(str(re)=="Existing id!\n")
        self.__clientDifferentid=Client(10,"Alex")
        try:
            repo.search(self.__clientDifferentid)
            assert(False)
        except RepoError as re:
            assert(str(re)=="Inexisting id!\n")
    def test_service_client(self):
        validatorClient=Validator_client()
        repoClient=Repo_movie()
        self.__service=Construct_Client(validatorClient,repoClient)
        assert(self.__service.no_of_clients()==0)
        clientid=24
        name="Izabella"
        self.__service.add_client_element(clientid,name)
        assert(self.__service.no_of_clients()==1)
        foundClient=self.__service.search_client_by_id(24)
        assert(foundClient.get_name()=="Izabella")
        try:
            self.__service.add_client_element(-33,"")
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="Invalid id!\nInvalid name!\n")
        try:
            self.__service.add_client_element(24,"Alex")
            assert(False)
        except RepoError as re:
            assert(str(re)=="Existing id!\n")
        try:
            self.__service.update_client_element(2,"Claudiu")
            assert(False)
        except RepoError as re:
            assert(str(re)=="Inexisting id!\n")
        self.__service.update_client_element(24,"Dan")
        assert(self.__service.no_of_clients()==1)
        client=self.__service.search_client_by_id(24) 
        assert(client.get_name()=="Dan")
        try:
            self.__service.remove_client_element(2)
            assert(False)
        except RepoError as re:
            assert(str(re)=="Inexisting id!\n")
        self.__service.remove_client_element(24)
        assert(self.__service.no_of_clients()==0)
    def run_all_tests(self):
        self.test_create_movie()
        self.test_validator_movie()
        self.test_repo_movie()
        self.test_service_movie()
        self.test_create_client()
        self.test_validator_client()
        self.test_repo_client()
        self.test_service_client() 
            