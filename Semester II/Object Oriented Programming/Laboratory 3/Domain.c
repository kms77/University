#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Domain.h"

File* create_new_element(int catalogueNumber, char* state, char* type, int value)
{
	File* new_input = (File*)malloc(sizeof(File));
	if (new_input == NULL)
	{
		return NULL;
	}
	new_input->catalogueNumber=catalogueNumber;
	new_input->state = NULL;
	new_input->type = NULL;

	set_catalogueNumber(new_input, catalogueNumber);
	set_the_state(new_input, state);
	set_the_type(new_input, type);
	set_the_value(new_input, value);

	return new_input;
}

void set_catalogueNumber(File* input, int catalogueNumber)
{
	input->catalogueNumber = catalogueNumber;
}

int get_catalogueNumber(File* input)
{
	return input->catalogueNumber;
}

void set_the_state(File* input, char* state)
{
	if (input->state && !strcmp(input->state, state))
	{
		return;
	}

	if (input->state != NULL)
	{
		free(input->state);
	}

	const int writable_Size_of_memory = strlen(state) * sizeof(char) + 1;
	input->state = (char*)malloc(writable_Size_of_memory);
	if (input->state == NULL)
	{
		return;
	}

	strcpy_s(input->state, writable_Size_of_memory, state);
}

char* get_the_state(File* input)
{
	return input->state;
}

void set_the_type(File* input, char* type)
{
	if (input->type && !strcmp(input->type, type))
	{
		return;
	}

	if (input->type != NULL)
	{
		free(input->type);
	}
	 
	const int writable_Size_of_memory = strlen(type) * sizeof(char) + 1;
	input->type = (char*)malloc(writable_Size_of_memory);

	if (input->type == NULL)
	{
		return;
	}

	strcpy_s(input->type, writable_Size_of_memory, type);
}

char* get_the_type(File* input)
{
	return input->type;
}

void set_the_value(File* input, int value)
{
	input->value = value;
}

int get_value(File* input)
{
	return input->value;
}

void destroy_file(File* input)
{
	if (input == NULL)
		return;
	free(input->state);
	free(input->type);
	free(input);
}

void to_String(File* input, char string_value[])
{
	if (input == NULL)
		return;
	sprintf(string_value, "Catalogue number: %d \nState: %s\nType: %s\nValue: %d\n", input->catalogueNumber, input->state, input->type, input->value);
}

File* copy_of_the_file(File* input)
{
    if(input == NULL)
	   return NULL;
	File* new_file = create_new_element(get_catalogueNumber(input), get_the_state(input), get_the_type(input), get_value(input));
	return new_file;
}
