from Tests import Test
from Exceptions import RepoError,ValidError
from Domain import Movie,Client,Rent
from Validate import Validator_movie,Validator_client,Validator_rent
from Repository import Repo_movie
from Service import Construct_Movie,Construct_Client,Construct_Rent
from Presentation import Console 
test=Test()
test.run_all_tests()
validator_movie=Validator_movie()
validator_client=Validator_client()
validator_rent=Validator_rent()
repo_movie=Repo_movie()
repo_client=Repo_movie()
repo_rent=Repo_movie()
service_movie=Construct_Movie(validator_movie,repo_movie)
service_client=Construct_Client(validator_client,repo_client)
service_rent=Construct_Rent(validator_rent,repo_movie,repo_client,repo_rent)
ui=Console(service_movie,service_client,service_rent)
ui.start()
