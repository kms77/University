#include "DynamicVector.h"

DynamicVector::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elements = new TElement[capacity];
}

DynamicVector::DynamicVector(const DynamicVector& vector_element)
{
	this->size=vector_element.size;
	this->capacity = vector_element.capacity;
	this->elements = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = vector_element.elements[i];
}

DynamicVector::~DynamicVector()
{
	delete[]this->elements;
}

DynamicVector& DynamicVector::operator=(const DynamicVector& vector_element)
{
	if (this == &vector_element)
		return *this;
	this->size = vector_element.size;
	this->capacity = vector_element.capacity;
	delete[] this->elements;
	this->elements = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
	{
		this->elements[i] = vector_element.elements[i];
	}
	return *this;
}
/*
The function which adds a new element to the dynamic array
*/
int DynamicVector::add(const TElement& element_to_be_add)
{
		if (this->size == this->capacity)
			this->resize();
		this->elements[this->size] = element_to_be_add;
		this->size++;
		return NOT_FOUND;
}
/*
This function removes an element found at a specific index from dynmaic array
*/
void DynamicVector::remove(int index)
{
	for (int i = index + 1; i < this->size; i++)
	{
		this->elements[i - 1] = this->elements[i];
	}
	this->size--;
}
/*
This function update an element from the dynamic array
*/
void DynamicVector::update(TElement& element_to_be_update,int index_of_element)
{
	this->elements[index_of_element] = element_to_be_update;
}
/*
 The function which resize the dynamic array 
*/
void DynamicVector::resize(double factor)
{
	this->capacity *= static_cast<int>(factor);
	TElement* elements = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
	{
		elements[i] = this->elements[i];
	}
	delete[]this->elements;
	this->elements = elements;
}
/*
The function which return the current size of the dynamic array
*/
int DynamicVector::getSize()const
{
	return this->size;
}
/*
The function which return by position an element from the dynamic array
*/
TElement DynamicVector::get_element_by_index(int position)
{
	return this->elements[position];
}
/*
Function which return the index from dynamic array of an element given as parameter 
*/