#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repo;
public:
	Service(Repository& repository) :repo{ repository } {}
	Repository& get_repository() { return repo; }
	bool addTurret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision);
	std::vector<Turret> get_all_turrets() const;
	bool updateTurret(const std::string& location_of_turret, const std::string& new_size_of_turret, const int& new_aura_level, const int& new_separate_parts, const std::string& new_vision);
	bool deleteTurret(const std::string& location_of_turret);
	bool saveTurret(const std::string& location_of_turret);
	std::vector<Turret> special_list(const std::string& location_of_turret, const int& separate_parts);
	std::vector<Turret> list_size(const std::string& location_of_turret);
	Turret nextTurret() const;
	std::vector<Turret> mylist() const;
};
