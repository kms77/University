from Exceptions import ValidError
class Validator_movie:
    def __init__(self):
        pass
    def validate_movie(self,movie):
        """
        this is the function which validates a movie input
        it verifies the id,title,description,genre of a movie
        """
        errors=""
        if movie.get_movieid()<1:
            errors+="Invalid id!\n"
        if movie.get_title()=="":
            errors+="Invalid title!\n"
        if movie.get_description()=="":
            errors+="Invalid description!\n"
        if movie.get_genre()=="":
            errors+="Invalid genre!\n"
        if len(errors)>0:
            raise ValidError(errors)
class Validator_client:
    def __init__(self):
        pass
    def validate_client(self,client):
        """
        this is the function which validates a client input
        it verifies the id,title,description,genre of the client
        """
        errors=""
        if client.get_clientid()<1:
            errors+="Invalid id!\n"
        if client.get_name()=="":
            errors+="Invalid name!\n"
        if len(errors)>0:
            raise ValidError(errors)
class Validator_rent:
    def __init__(self):
        pass
    def validate_rent(self,rent,movies,clients):
        self.__months=[31,28,31,30,31,30,31,31,30,31,30,31]
        errors=""
        if rent.get_clientid()<1:
            errors+="Invalid client id!\n"
        if rent.get_movieid()<1:
            errors+="Invalid movie id!\n"
        if rent.get_rentalid()<1:
            errors+="Invalid rental id!\n"
        rental_date=rent.get_rented_date()
        if int(rental_date[1])<=0 or int(rental_date[1])>12:
            errors+="Invalid month rent!\n"
        if len(errors)>0:
                raise ValidError(errors)
        if int(rental_date[0])>self.__months[int(rental_date[1])-1] or int(rental_date[0])<=0:
            errors+="Invalid day rent!\n"
        due_date=rent.get_due_date()
        if int(due_date[0])>self.__months[int(due_date[1])-1] or int(due_date[0])<=0:
            errors+="Invalid day rent!\n"
        if int(due_date[1])<=0 or int(due_date[1])>12:
            errors+="Invalid month rent!\n"
        if int(rental_date[1])>int(due_date[1]):
            errors+="Invalid date!\n"
        if int(rental_date[1])==int(due_date[1]):
            if int(rental_date[0])>int(due_date[0]):
                errors+="Invalid date!\n"
        if len(errors)>0:
                raise ValidError(errors)
        else:
            for i in range(len(movies)):
                returned_date=movies[i].get_returned_date()
                if type(returned_date)==str:
                    due_date=movies[i].get_due_date()
                    rental_date=movies[i].get_rented_date()
                    rent_due=rent.get_due_date()
                    rent_rental=rent.get_rented_date()
                    if due_date[1]>rent_due[1]:
                        if rental_date[1]<rent_due[1]:
                            errors+="Invalid movie!\n"
                    if due_date[1]>rent_rental[1]:
                        if rental_date[1]<rent_rental[1]:
                            errors+="Invalid movie!\n"
                    if due_date[1]==rent_due[1] and due_date[0]>=rent_due[0] and rental_date[1]<=rent_due[1]:
                        errors+="Invalid movie!\n"
                    if due_date[1]==rent_rental[1] and due_date[0]>=rent_rental[0] and rental_date[1]<=rent_rental[1]:
                        errors+="Invalid movie!\n"
                else:
                    returned_date=movies[i].get_returned_date()
                    rental_date=movies[i].get_rented_date()
                    rent_due=rent.get_due_date()
                    rent_rental=rent.get_rented_date()
                    if returned_date[1]>rent_due[1]:
                        if rental_date[1]<rent_due[1]:
                            errors+="Invalid movie!\n"
                    if returned_date[1]>rent_rental[1]:
                        if rental_date[1]<rent_rental[1]:
                            errors+="Invalid movie!\n"
                    if returned_date[1]==rent_due[1] and returned_date[0]>=rent_due[0] and rental_date[1]<=rent_due[1]:
                        errors+="Invalid movie!\n"
                    if returned_date[1]==rent_rental[1] and returned_date[0]>=rent_rental[0] and rental_date[1]<=rent_rental[1]:
                        errors+="Invalid movie!\n"
            for i in range(len(clients)):
                returned_date=clients[i].get_returned_date()
                if type(returned_date)==list:
                    returned_date=clients[i].get_returned_date()
                    due_date=clients[i].get_due_date()
                    if due_date[1]<returned_date[1]:
                        errors+="Invalid client!\n"
                    if int(due_date[1])==int(returned_date[1]) and int(due_date[0])<int(returned_date[0]):
                        errors+="Invalid client!\n"
            if len(errors)>0:
                raise ValidError(errors)
    def validate_return(self,rent,l):
        self.__months=[31,28,31,30,31,30,31,31,30,31,30,31]
        errors=""
        if rent.get_rentalid()<1:
            errors+="Invalid client id!\n"
        returned_date=rent.get_returned_date()
        if int(returned_date[0])>int(self.__months[int(returned_date[1])-1]) or int(returned_date[0])<=0:
            errors+="Invalid day rent!\n"
        if int(returned_date[1])<=0 or int(returned_date[1])>12:
            errors+="Invalid month rent!\n"
        returned_date=rent.get_returned_date()
        rented_date=rent.get_rented_date()
        if int(returned_date[1])<int(rented_date[1]) or (int(returned_date[1])==int(rented_date[1]) and int(returned_date[0])<int(rented_date[0])):
            errors+="Invalid date!\n"
        if len(errors)>0:
            raise ValidError(errors)
