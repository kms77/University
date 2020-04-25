#include <vector>
#include <algorithm>
#include "Service.h"
/*
This function return a dynamic vector with all the elements from repository to domain
*/
std::vector<Turret> Service::get_all_turrets()const
{
	return this->repo.getTurrets();
}
/*
Add a new turret to the dynamic array; It constructs the element and call the repository function for adding
*/
bool Service::addTurret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision)
{
	Turret construct_turret{ location_of_turret,size_of_turret,aura_level,separate_parts,vision };
	bool check_success = this->repo.Add_turret(construct_turret);
	return check_success;
}
/*
Update a new turret from the dynamic array; It constructs the element and call the repository for update
*/
bool Service::updateTurret(const std::string& location_of_turret, const std::string& new_size_of_turret, const int& new_aura_level, const int& new_separate_parts, const std::string& new_vision)
{
	Turret construct_turret{ location_of_turret,new_size_of_turret,new_aura_level,new_separate_parts,new_vision };
	bool check_success = this->repo.Update_turret(construct_turret);
	return check_success;
}
/*
Delete a element from dynamic array; It constructs the element and call the repository for delete
*/
bool Service::deleteTurret(const std::string& location_of_turret)
{
	Turret construct_turret{ location_of_turret,"",0,0,"" };
	bool check_success = this->repo.Delete_turret(construct_turret);
	return check_success;
}
Turret Service::nextTurret()const
{
	int current_index = this->repo.next_turret_iterator();
	std::vector<Turret> all_turrets = this->repo.getTurrets();
	Turret current_turret = { "","",0,0,"" };
	for (int i = 0; i < all_turrets.size(); i++)
	{
		if (i == current_index)
			current_turret = all_turrets.at(i);
	}
	return current_turret;
}
std::vector<Turret> Service::mylist()const {
	return this->repo.getSevedTurrets();
}
std::vector<Turret> Service::special_list(const std::string& size, const int& separate_parts)
{
	std::vector<Turret> all_turrets = this->repo.getTurrets();
	std::vector<Turret> get_special_list(all_turrets.size());
	auto filter_by_size_and_separate_parts = [&size, &separate_parts](const Turret& turret)
	{
		return turret.get_size_of_turret() == size && turret.get_separate_parts() >= separate_parts;
	};
	auto iterate = copy_if(all_turrets.begin(), all_turrets.end(), get_special_list.begin(), filter_by_size_and_separate_parts);
	get_special_list.resize(distance(get_special_list.begin(), iterate));
	return get_special_list;
}
std::vector<Turret> Service::list_size(const std::string& size)
{
	std::vector<Turret> all_turrets = this->repo.getTurrets();
	std::vector<Turret> get_special_list(all_turrets.size());
	auto filter_by_size = [&size](const Turret& turret)
	{
		return turret.get_size_of_turret() == size;
	};
	auto iterate = copy_if(all_turrets.begin(), all_turrets.end(), get_special_list.begin(), filter_by_size);
	get_special_list.resize(distance(get_special_list.begin(), iterate));
	return get_special_list;
}
bool Service::saveTurret(const std::string& location_of_turret)
{
	std::vector<Turret> all_turrets = this->repo.getTurrets();
	Turret turret = { location_of_turret,"",0,0,"" };
	auto iterator = std::find(all_turrets.begin(), all_turrets.end(), turret);
	if (iterator != all_turrets.end())
	{
		auto index = std::distance(all_turrets.begin(), iterator);
		const Turret construct_turret=all_turrets.at(index);
		bool truth_value = this->repo.Save_turret(construct_turret);
		return truth_value;
	}
	return false;
}