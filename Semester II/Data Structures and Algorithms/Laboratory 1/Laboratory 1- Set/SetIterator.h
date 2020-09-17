#pragma once
#include "Set.h"

class SetIterator
{
	//DO NOT CHANGE THIS PART
	friend class Set;
private:
	//DO NOT CHANGE THIS PART
	Set& set;
	SetIterator(Set& s);

	//TODO - Representation
	int index;

public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
	TElem remove_current();
};
