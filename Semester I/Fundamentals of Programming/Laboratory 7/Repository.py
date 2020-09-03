from Exceptions import RepoError
import copy
class Repo_movie(object):
        def __init__(self):
            self.__movie_entities=[]
        def number_of_elements(self):
            return len(self.__movie_entities)
        def add(self,x):
            if x in self.__movie_entities:
                raise RepoError("Existing id!\n")
            self.__movie_entities.append(x)
        def remove(self,k):
            if k not in self.__movie_entities:
                raise RepoError("Inexisting id!\n")
            for i in range(len(self.__movie_entities)):
                if self.__movie_entities[i]==k:
                    del self.__movie_entities[i]
                    return
        def update(self,k):
            if k not in self.__movie_entities:
                raise RepoError("Inexisting id!\n")
            for i in range(len(self.__movie_entities)):
                if self.__movie_entities[i]==k:
                    self.__movie_entities[i]=k
                    return
        def search(self,movie):
            if movie not in self.__movie_entities:
                raise RepoError("Inexisting id!\n")
            for x in self.__movie_entities:
                if x==movie:
                    return x
        def get_all(self):
            return self.__movie_entities