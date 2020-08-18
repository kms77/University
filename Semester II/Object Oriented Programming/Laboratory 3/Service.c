#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "Service.h"

Service* create_service(Repository* repository)
{
	Service* newService = (Service*)malloc(sizeof(Service));
	if (newService == NULL)
	{
		return NULL;
	}
	newService->repository = repository;
	return newService;
}

int add_element_to_list(Service* service,int catalogueNumber,char* state,char* type,int value)
{
	File* newFile = create_new_element(catalogueNumber, state, type, value);
	return add_element_to_my_list(service->repository, newFile);
}

int update_element_from_list(Service* service, int catalogueNumber, char* state, char* type, int value)
{
	return update_element_from_my_list(service->repository,catalogueNumber,state,type,value);
}

Repository* get_repository(Service* service)
{
	return service->repository;
}
int delete_element_from_list(Service* service, int catalogueNumber)
{
	return delete_element_from_my_list(service->repository, catalogueNumber);
}
/*
int get_elements_number(Service* service)
{
	return get_size(service->repository);
}
File* get_file_index(Service* service, int current_element)
{
	Repository* repository = service->repository;
	File* currentFile = get_element_of_list_by_index(repository, current_element);
	return currentFile;
}
*/
void destroy_service(Service* service)
{
	destroy_repository(service->repository);
	free(service);
}