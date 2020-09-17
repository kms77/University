#include "SetIterator.h"
#include "Set.h"


SetIterator::SetIterator(Set& m) : set(m)
{
	//TODO - Implementation
	index = 0;
}

TElem SetIterator::remove_current() //tests for this operation are in tests iterator
{
	if (!valid()) 
		throw ("Exception");
	TElem n=getCurrent();
	set.remove(n);
	return n;
}
void SetIterator::first() 
{
	//TODO - Implementation
	index = 0;
}


void SetIterator::next() {

	//TODO - Implementation
	if (valid()) {
		index++;
	}
}


TElem SetIterator::getCurrent()
{
	//TODO - Implementation
	return set.array[index];
}

bool SetIterator::valid() const {
	//TODO - Implementation
	return 0 <= index && index < set.length;
}