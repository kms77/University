#include "DynamicArray.h"
#include <stdio.h>

DynamicArray* create_dynamic_array(int capacity)
{
	DynamicArray* dynamic_array = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (dynamic_array == NULL)
		return NULL;
	dynamic_array->capacity = capacity;
	dynamic_array->length = 0;
	dynamic_array->elements=(TElement*) malloc(capacity * sizeof(TElement));
	if (dynamic_array->elements==NULL)
		return NULL;
	return dynamic_array;
}

void destroy(DynamicArray* array)
{
	if (array == NULL)
	{
		return;
    }
	for (int i = 0; i < array->length; i++)
	{
		destroy_file(array->elements[i]);
	}
	free(array->elements);
	array->elements = NULL;
	free(array);
}

int resize(DynamicArray* array)
{
	if (array == NULL)
		return -1;
	array->capacity = array->capacity * 2;
	TElement* auxilar = (TElement*)malloc(array->capacity * sizeof(TElement));
	if (auxilar == NULL)
	{
		return -1;
	}
	for (int i = 0; i < array->length; i++)
	{
		auxilar[i] = array->elements[i];
	}
	free(array->elements);
	array->elements = auxilar;
	return 0;
}

void add_element(DynamicArray* array, TElement element)
{
	if (array == NULL)
		return;
	if (array->elements == NULL)
	{
		return;
	}
	if (array->length == array->capacity)
		resize(array);
	array->elements[array->length++] = element;
	printf("Element was added \n");
}
int delete_element(DynamicArray* array, int position)
{
	if (position < 0 || position >= array->length || array->length == 0)
		return -1;
	destroy_file(array->elements[position]);
	for (int i = position; i < array->length - 1; i++)
		array->elements[i] = array->elements[i + 1];
     array->length --;
	 return 1;
}

int update_element(DynamicArray* array, int catalogue_number, char* new_state, char* new_type, int new_value)
{
	int position = 0;
	for (int i = 0; i < array->length; i++)
	{
		if (array->elements[i]->catalogueNumber == catalogue_number)
		{
			position = i;
			strcpy(array->elements[i]->state, new_state);
			strcpy(array->elements[i]->type, new_type);
			array->elements[i]->value = new_value;
		}
	}
    return array->elements[position];
}

int get_the_size_of_the_array(DynamicArray* element)
{
	if (element == NULL)
	{
		return -1;
	}
	return element->length;
}

TElement get_element_by_position(DynamicArray* element, int position)
{
	if (element == NULL)
	{
		return NULL;
	}
	if (position < 0 || position >= element->length)
	{
		return NULL;
	}
	return element->elements[position];
}
