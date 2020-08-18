#pragma once
#include "Domain.h"
#include "DynamicArray.h"
#include <stdlib.h>
#include <string.h>

typedef struct
{
	DynamicArray* files;
}Repository;

Repository* create_repository();

int add_element_to_my_list(Repository* toRepo,File* newFile);

//File* get_the_file(Repository* inRepo, int catalogueNumber);

int delete_element_from_my_list(Repository* fromRepo, int catalogueNumber);

File* get_element_of_list_by_position(Repository* fromRepo, int position);

void destroy_repository(Repository* repository);

int get_size(Repository* inRepo);

int find_element_on_position(Repository* repository, int position);

int find_position_of_the_element(Repository* repository, int catalogue_number);

int update_element_from_my_list(Repository* fromRepo, int catalogueNumber, char* new_state, char* new_type, int value);