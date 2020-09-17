#include "Map.h"
#include "MapIterator.h"

Map::Map() {
	//TODO - Implementation
	this->capacity = 5;
	this->length = 0;
	this->DynamicArray = new TElem[this->capacity];
}

Map::~Map() {
	delete[] this->DynamicArray;
}
//Complexity: Theta(n) (we add at the final, so we must iterate the whole map)
TValue Map::add(TKey c, TValue v){
	//TODO - Implementation
	for (int i = 0; i < this->length; i++) {
		if (this->DynamicArray[i].first == c)
		{
			TValue old_value = this->DynamicArray[i].second;
			this->DynamicArray[i].second = v;
			return old_value;
		}
	}

	if (this->length == this->capacity)
	{
		this->capacity *= 2;
		TElem* newArray = new TElem[this->capacity];
		for (int i = 0; i < this->length; i++)
			newArray[i] = this->DynamicArray[i];
		delete[] this->DynamicArray;
		this->DynamicArray = newArray;

	}
	TElem element = TElem(c, v);
	this->DynamicArray[this->length] = element;
	this->length++;
	return NULL_TVALUE;
}

//BC - Theta(1) - the first element
//WC - Theta(n) - the last element
//Complexity - O(n)
TValue Map::search(TKey c) const{
	//TODO - Implementation
	for (int i = 0; i < this->length; i++) {
		if (this->DynamicArray[i].first == c)
			return this->DynamicArray[i].second;

	}
	return NULL_TVALUE;
}

//Complexity: Theta(n)
TValue Map::remove(TKey c){
	//TODO - Implementation
	int index = 0;
	while (index < this->length)
	{
		if (this->DynamicArray[index].first == c)
			break;
		index += 1;
	}
	if (index == this->length)
		return NULL_TVALUE;

	TValue old_value = this->DynamicArray[index].second;
	for (int i = index; i < length - 1; ++i)
		this->DynamicArray[i] = this->DynamicArray[i + 1];
	this->length--;
	return old_value;
}

//Complexity: Theta(1)
int Map::size() const {
	//TODO - Implementation
	return this->length;
}

//Complexity: Theta(1)
bool Map::isEmpty() const{
	//TODO - Implementation
	if(this->length==0)
		return true;
	return false;
}

//returns the difference between the maximum and the minimum key (assume integer keys)
//if the Map is empty the range is -1
//Complexity: Theta(n), we do not have BC or WC
int Map::getKeyRange() const
{
	int maxKey = -999;
	int minKey = 999;
	int keyRange = 0;

	if (isEmpty() == true)
		return -1;


	for (int i = 0; i < this->length; i++) {
		if (this->DynamicArray[i].first >= maxKey)
			maxKey = this->DynamicArray[i].first;
		if (this->DynamicArray[i].first <= minKey)
			minKey = this->DynamicArray[i].first;
	}

	keyRange = maxKey - minKey;
	return keyRange;
}

MapIterator Map::iterator() const {
	return MapIterator(*this);
}



