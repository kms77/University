#pragma once
#include "Domain.h"
#define NOT_FOUND -1
template <typename TElement=int> 
class DynamicVector
{
private:
	TElement* elements;
	int size;
	int capacity;
	int current_index_of_iterator=-1;
public:
	DynamicVector(int capacity = 10);
	DynamicVector(const DynamicVector& vector_element);
	~DynamicVector();
	DynamicVector& operator=(const DynamicVector& vector_element);
	int add(const TElement& element);
	int save(TElement& element);
	void update(TElement& element,int index_of_element);
	void remove(int index);
	int getSize() const;
	TElement get_element_by_index(int position);
	void resize(double factor = 2);
	/*
	It returns the current element of the iteration
	Return: integer value- this->elements[this->current_index_of_iterator] the current element of the iteration
	*/
	TElement& getCurrent() { return this->elements[this->current_index_of_iterator]; }
	/*
	It intializes the iterator
	Return: -
	*/
	bool nextIterator()
	{
		if (this->size < 1)
		{
			return false;
		}
		else if (this->current_index_of_iterator == this->size - 1 )
		{
			this->current_index_of_iterator = 0;
			return true;
		}
		else
		{
			this->current_index_of_iterator++;
			return true;
		}
	}
};
/*
The constructor of the dynamic vector 
Input: capacity- initial capacity of the dynamic vector
Output: -
*/
template<typename TElement>
inline DynamicVector<TElement>::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elements = new TElement[capacity];
}
//Constrcut the vector with its elements, size, capacity
template<typename TElement>
inline DynamicVector<TElement>::DynamicVector(const DynamicVector<TElement>& vector_element)
{
	this->size = vector_element.size;
	this->capacity = vector_element.capacity;
	this->elements = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = vector_element.elements[i];
}
//Destructor of the dynamic vector
template<typename TElement>
inline DynamicVector<TElement>::~DynamicVector()
{
	delete[]this->elements;
}
/*
The equal operator between two elements of the dynamic vector 
*/
template<typename TElement>
inline DynamicVector<TElement>& DynamicVector<TElement>::operator=(const DynamicVector<TElement>& vector_element)
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
Input: TElement element_to_be_add - the new element which will be added into the dynamic vector
Output: NOT_FOUND - means that the new added element was a unique one -it has a unique id in the array
*/
template<typename TElement>
inline int DynamicVector<TElement>::add(const TElement& element_to_be_add)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = element_to_be_add;
	this->size++;
	return NOT_FOUND;
}
/*
The function which updates an element of the dynamic array
Input: TElement element_to_be_update - the element which will be add
       int index_of_element- index of the element we want to update
Output: -
*/
template<typename TElement>
inline void DynamicVector<TElement>::update(TElement& element_to_be_update,int index_of_element)
{
    this->elements[index_of_element] = element_to_be_update;
}
template<typename TElement>
/*
The function which updates an element of the dynamic array
Input: TElement element_to_be_update - the element which will be add
	   int index_of_element- index of the element we want to update
Output: - NOT_FOUND -means that the new saved element was a unique one -it has a unique id in the save array
*/
inline int DynamicVector<TElement>::save(TElement& element_to_be_saved)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = element_to_be_saved;
	this->size++;
	return NOT_FOUND;
}
/*
The function which removes an element of the dynamic array
Input: index- postion of the element we want to remove from the dynamic array
Output: -
*/
template<typename TElement>
inline void DynamicVector<TElement>::remove(int index)
{
	for (int i = index + 1; i < this->size; i++)
	{
		this->elements[i - 1] = this->elements[i];
	}
	this->size--;
}
/*
 The function which resize the dynamic array
 Return: -
*/
template<typename TElement>
inline void DynamicVector<TElement>::resize(double factor)
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
The function which returns the current size of the dynamic array
Return: size of the dynamic array
*/
template<typename TElement>
inline int DynamicVector<TElement>::getSize()const
{
	return this->size;
}
/*
The function which returns by position an element from the dynamic array
Input: position- the position of the element we are looking for
Output: element of the dynamic vector from that position
*/
template <typename TElement>
inline TElement DynamicVector<TElement>::get_element_by_index(int position)
{
	return this->elements[position];
}