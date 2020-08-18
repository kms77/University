#include "Repository.h"
#include <stdio.h>

Repository* create_repository()
{
	Repository* newRepository = (Repository*)malloc(sizeof(Repository));
	if (newRepository == NULL)
	{
		return NULL;
	}
	newRepository->files = create_dynamic_array(CAPACITY);
	return newRepository;

}

int add_element_to_my_list(Repository* toRepo, File* newFile)
{
	if (toRepo == NULL || newFile == NULL)
	{
		return 0;
	}
	if (find_position_of_the_element(toRepo, get_catalogueNumber(newFile)) == -1)
	{
		add_element(toRepo->files, newFile);
		return 1;
	}
	else
	{
		return 0;
	}
}
/*
File* get_the_file(Repository* inRepo, int catalogueNumber)
{
	int length = get_the_size_of_the_array(inRepo->files);
	for (int i = 0; i < length; i++)
	{
		File* index_of_file = get_element_of_list_by_index(inRepo, i);
		if (get_catalogueNumber(index_of_file) == catalogueNumber)
		{
			return index_of_file;
		}
	}
	return NULL;
}
*/

int delete_element_from_my_list(Repository* repository, int catalogueNumber)
{
	int position;
	position = find_position_of_the_element(repository, catalogueNumber);
	if (repository == NULL)
		return -1;
	if ( position== -1)
	{
		return -1;
	}
	return delete_element(repository->files, position);
}

File* get_element_of_list_by_position(Repository* fromRepo, int position)
{
	if(fromRepo==NULL)
	   return NULL;
	return get_element_by_position(fromRepo->files,position);
}

int get_size(Repository* inRepo)
{
	if (inRepo == NULL)
		return -1;
	return get_the_size_of_the_array(inRepo->files);
}

int find_element_on_position(Repository* repository, int position) {
	if (repository == NULL)
	{
		return NULL;
	}
	return get_element_by_position(repository->files, position);
}

int find_position_of_the_element(Repository* repository, int catalogue_number)
{
	int length = get_the_size_of_the_array(repository->files);
	for (int i = 0; i < length; ++i)
		if (get_element_by_position(repository->files, i)->catalogueNumber == catalogue_number)
			return i;
	return -1;
}

int update_element_from_my_list(Repository* fromRepo, int catalogueNumber, char* new_state, char* new_type, int value)
{
	File* file = update_element(fromRepo->files, catalogueNumber, new_state, new_type, value);
	return file;
}
void destroy_repository(Repository* repository)
{
	if (repository == NULL)
	{
		return;
	}
	destroy(repository->files);
	free(repository);
}