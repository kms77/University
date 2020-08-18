#pragma once
#include "Domain.h"
#include <stdlib.h>
#include <string.h>
#define CAPACITY 10

typedef File* TElement;

typedef struct {
	TElement* elements;
	int length;
	int capacity;
}DynamicArray;

DynamicArray* create_dynamic_array(int capacity);
void destroy(DynamicArray* array);
int resize(DynamicArray* array);
void add_element(DynamicArray* array, TElement element);
int delete_element(DynamicArray* array, int position);
int update_element(DynamicArray* array, int catalogue_number, char* new_state, char* new_type, int new_value);
int get_the_size_of_the_array(DynamicArray* element);
TElement get_element_by_position(DynamicArray* element, int position);