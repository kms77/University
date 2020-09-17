#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	//TODO - Implementation
	this->index = 0;
}

//Complexity: Theta(1)
void MapIterator::first() {
	//TODO - Implementation
	this->index = 0;
}

//Complexity: Theta(1)
void MapIterator::next() {
	//TODO - Implementation
	if (valid())
		this->index++;
	else
		throw exception();
}

//Complexity: Theta(1)
TElem MapIterator::getCurrent(){
	//TODO - Implementation
	if(valid())
		return map.DynamicArray[this->index];
	else 
		throw exception();
}

//Complexity: Theta(1)
bool MapIterator::valid() const {
	//TODO - Implementation
	return this->index>=0 && this->index < map.length;
}





