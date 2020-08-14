#include "Service.h"
/*
This function returns a dynamic vector with all the elements
Return: a dynamic array with all the turrets
*/
DynamicVector<Turret> Service::get_all_turrets()const
{
	return this->repo.getTurrets();
}
/*
Add a new turret to the dynamic array; It constructs the element and call the repository function to add the element
Input: std::string location_of_turret- location of turret we are looking to update
	   std::string new_size_of_turret- the new size of the turret with the given location
	   int new_aura_level- the new aura level of the turret with the given location
	   int new_separate_parts- the new separate parts of the turret with the given location
	   std::string vision- the new vision of the turret with the given location
Output: a boolen value
       false- turret already exists
	   true- turret was added successfully
*/
bool Service::addTurret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision)
{
	Turret construct_turret{ location_of_turret,size_of_turret,aura_level,separate_parts,vision };
	int check_success = this->repo.Add_turret(construct_turret);
	if (check_success == NOT_FOUND)
		return true;
	else
		return false;
}
/*
Update a new turret from the dynamic array; It constructs the element and call the repository to update the element
Input: std::string location_of_turret- location of turret we are looking to update
       std::string new_size_of_turret- the new size of the turret with the given location
	   int new_aura_level- the new aura level of the turret with the given location
	   int new_separate_parts- the new separate parts of the turret with the given location
	   std::string vision- the new vision of the turret with the given location
Output: a boolean value
		false- turret does not exist
		true- turret was updated
*/
bool Service::updateTurret(const std::string& location_of_turret, const std::string& new_size_of_turret, const int& new_aura_level, const int& new_separate_parts, const std::string& new_vision)
{
	Turret construct_turret{ location_of_turret,new_size_of_turret,new_aura_level,new_separate_parts,new_vision };
	int check_success = this->repo.Update_turret(construct_turret);
	if (check_success != NOT_FOUND)
		return true;
	else
		return false;
}
/*
Delete an element from dynamic array; It constructs the element and call the repository to delete the element
Input: std::string location_of_turret- location of turret we are looking to delete
Output: a boolean value
		false- turret does not exist
	    true- turret was deleted
*/
bool Service::deleteTurret(const std::string& location_of_turret)
{
	Turret construct_turret{ location_of_turret,"",0,0,"" };
	int check_success = this->repo.Delete_turret(construct_turret);
	if (check_success != NOT_FOUND)
		return true;
	else
		return false;
}
/*
Save an element from dynamic array; It constructs the element and call the repository to save it
Input: std::string location_of_turret- location of turret we are looking to save
Output: a boolean value
        false- turret already saved or turret does not exist
        true- turret was saved
*/
bool Service::saveTurret(const std::string& location_of_turret)
{
	Turret construct_turret{ location_of_turret,"",0,0,"" };
	DynamicVector<Turret> all_turrets = this->repo.getTurrets();
	int index_of_turret = this->repo.get_index_by_location(construct_turret);
	if (index_of_turret == NOT_FOUND)
	{
		return false;
	}
	else
	{
		construct_turret = all_turrets.get_element_by_index(index_of_turret);
		index_of_turret=this->repo.Save_turret(construct_turret);
		return true;
	}
}
/*
Call the repository function to iterate to next element 
Input:-
Return: bool- true -successfull iteration through the elements of the array
              false -the array is empty
*/
bool Service::nextTurret()const 
{
	return this->repo.next_turret_iterator();
}
/*
This function returns a dynamic vector with all the saved elements
Return : a dynamic array with all the saved turrets
*/
DynamicVector<Turret> Service::mylist()const {
	return this->repo.getSevedTurrets();
}
/*
This function returns a dynamic vector with all the elements after 
Input : std::string size - the size we are filtering by
        int separate parts - value we are filtering by
Output : a dynamic array with turrets after filtering by size anfd separate parts
*/
DynamicVector<Turret> Service::filter_by_size_and_parts(std::string& size, int& separate_parts)
{
	DynamicVector<Turret> all_turrets = this->repo.getTurrets();
	DynamicVector<Turret>  turrets_from_filter_size_and_parts{};
	for (int i = 0; i < all_turrets.getSize(); i++)
	{
		Turret turret = all_turrets.get_element_by_index(i);
		if ((turret.get_size_of_turret() == size) && (turret.get_separate_parts()>=separate_parts))
		{
			turrets_from_filter_size_and_parts.add(turret);
		}
	}
	return turrets_from_filter_size_and_parts;
}
/*
This function returns a dynamic vector with all the saved elements
Input : std::string size - the size we are filtering by
		int separate parts - value we are filtering by
Output : a dynamic array with turrets after filtering by size
*/
DynamicVector<Turret> Service::list_size(const std::string& size)
{
	DynamicVector<Turret> all_turrets = this->repo.getTurrets();
	DynamicVector<Turret>  turrets_from_filter_size{};
	for (int i = 0; i < all_turrets.getSize(); i++)
	{
		Turret turret = all_turrets.get_element_by_index(i);
		if (turret.get_size_of_turret() == size)
		{
			turrets_from_filter_size.add(turret);
		}
	}
	return turrets_from_filter_size;
}
/*
Call the repository function to get the current element of the iteration
Input:-
Return: turret- the iterated turret
*/
Turret Service::get_current_turret() const
{

	return this->repo.Get_current_turret();
}
