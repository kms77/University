#pragma once
#include "Domain.h"
#define NOT_FOUND -1

typedef Turret TElement;

class DynamicVector
{
private:
	TElement* elements;
	int size;
	int capacity;
public:
	DynamicVector(int capacity = 10);
	DynamicVector(const DynamicVector& vector_element);
	~DynamicVector();
	DynamicVector& operator=(const DynamicVector& vector_element);
	int add(const TElement& element);
	void update(TElement& element,int index_of_element);
	void remove(int index);
	int getSize() const;
	TElement get_element_by_index(int position);
private:
	void resize(double factor = 2);
};