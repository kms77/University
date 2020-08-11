#include "Repository.h"
/*
This function calls the dynamic array for adding the new element to it
*/
int Repository::Add_turret(Turret& new_turret)
{
	int index_of_turret = get_index_by_location(new_turret);
	if (index_of_turret == NOT_FOUND)
	{
		return this->turrets.add(new_turret);
	}
	return index_of_turret;
}
/*
This function got the the index of the new_turret element and calls the dynamic array for update the element found at that index
*/
int Repository::Update_turret(Turret& new_turret)
{
	int index_of_turret = get_index_by_location(new_turret);
	if (index_of_turret != NOT_FOUND)
	{
		this->turrets.update(new_turret,index_of_turret);
	}
	return index_of_turret;
}
/*
This function got the the index of a given turret and calls the dynamic array for delete the element found at that index
*/
int Repository::Delete_turret(Turret& turret)
{
	int index_of_turret = get_index_by_location(turret);
	if (index_of_turret != NOT_FOUND)
	{
		this->turrets.remove(index_of_turret);
	}
	return index_of_turret;
}
/*
This function get the turret found at the position of the current turret
*/
Turret Repository::get_turret_by_location(Turret& current_turret)
{
	for (int i = 0; i < this->turrets.getSize(); i++)
	{
		Turret turret_by_index = this->turrets.get_element_by_index(i);
		if (current_turret.get_location_of_turret() == turret_by_index.get_location_of_turret())
		{
			return turret_by_index;
		}
	}
}
/*
 Returns the size of the dynamic array
*/
int Repository::get_size_of_list()
{
	return this->turrets.getSize();
}
/*
This function get the index of turret  found at the position of the current turret
Returns : index_of_element- index of element we are looking for
          NOT_FOUND = -1 -if the input data is invalid
*/
int Repository::get_index_by_location(Turret& current_turret)
{
	DynamicVector all_turrets = this->getTurrets();
	for (int index_of_element = 0; index_of_element < this->turrets.getSize(); index_of_element++)
	{
		Turret turret = all_turrets.get_element_by_index(index_of_element);
		if (current_turret.get_location_of_turret() == turret.get_location_of_turret())
		{
			return index_of_element;
		}
	}
	return NOT_FOUND;
}