#include "Repository.h"
#include <string.h>
using namespace std;
/*
  Add a new element to the dynamic array
  Input: Turret new_turret- the new turret to be added
  Output: index_of_turret- if turret already exist in the list of turrets
          else: turret does not exist and it is added
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
  Update an element of the dynamic array
  Input: Turret new_turret- the new turret to be updated
  Output: index_of_turret- if turret does not  exist in the list of turrets
		  else: turret exists and it is  updated
*/
int Repository::Update_turret(Turret& new_turret)
{
	int index_of_turret =get_index_by_location(new_turret);
	if (index_of_turret != NOT_FOUND)
	{
		this->turrets.update(new_turret,index_of_turret);
	}
	return index_of_turret;
}
/*
  Delete an element to the dynamic array
  Input: Turret turret- the turret to be deleted
  Output: index_of_turret- if turret does not exists in the list of turrets
		  else: turret exists and it is deleted
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
  Save a new element to the dynamic array
  Input: Turret new_save_turret- the new turret to be saved
  Output: an integer value
*/
int Repository::Save_turret(Turret& new_save_turret)
{
		return this->saved_turrets.save(new_save_turret);
}
/*
The function which returns the size of the dynamic array
Input:-
Output- integer value- the size of the array
*/
int Repository::get_size_of_list()
{
	return this->turrets.getSize();
}
/*
  Get the index in the array of a given turret
  Input: Turret current_turret- the given turret, we are looking for its index in the array
  Output: index_of_element- the index in the array of the given turret 
          else: NOT_FOUND- the given turret doesn't exist
*/
int Repository::get_index_by_location(Turret& current_turret)
{
	DynamicVector<Turret> all_turrets = this->getTurrets();
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