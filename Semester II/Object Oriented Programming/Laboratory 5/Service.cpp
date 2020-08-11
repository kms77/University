#include "Service.h"
/*
This function returns a dynamic vector with all the elements
*/
DynamicVector Service::get_all_turrets()const
{
	return this->repo.getTurrets();
}
/*
Add a new turret to the dynamic array;
It constructs the element and call the repository function for add operation
*/
bool Service::addTurret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision)
{
	Turret construct_turret{ location_of_turret,size_of_turret,aura_level,separate_parts,vision };
	int check_success=this->repo.Add_turret(construct_turret);
	if (check_success== NOT_FOUND)
		return true;
	else
		return false;
}
/*
Update a new turret from the dynamic array;
It constructs the element and call the repository for update operation
*/
bool Service::updateTurret(const std::string& location_of_turret, const std::string& new_size_of_turret, const int& new_aura_level, const int& new_separate_parts, const std::string& new_vision)
{
	Turret construct_turret{ location_of_turret,new_size_of_turret,new_aura_level,new_separate_parts,new_vision };
    int check_success=this->repo.Update_turret(construct_turret);
	if (check_success != NOT_FOUND)
		return true;
	else
		return false;
}
/*
Delete a element from dynamic array; 
It constructs the element and call the repository for delete operation
*/
bool Service::deleteTurret(const std::string& location_of_turret)
{
	Turret construct_turret{ location_of_turret,"",0,0,"" };
    int check_success=this->repo.Delete_turret(construct_turret);
	if (check_success != NOT_FOUND)
		return true;
	else
		return false;
}