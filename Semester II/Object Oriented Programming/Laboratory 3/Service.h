#pragma once
#include "Repository.h"

typedef struct
{
	Repository* repository;
}Service;

Service* create_service(Repository* repository);

int delete_element_from_list(Service* service,int element);

int add_element_to_list(Service* service,int catalogueNumber,char* state,char* type,int value);

int update_element_from_list(Service* service, int catalogueNumber, char* state, char* type, int value);

void destroy_service(Service* service);

Repository* get_repository(Service* service);

//File* get_file_index(Service* service,int current_element);

//int get_elements_number(Service* service);

