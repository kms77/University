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
	DynamicVector<Turret> get_all_turrets() const;
	bool updateTurret(const std::string& location_of_turret, const std::string& new_size_of_turret, const int& new_aura_level, const int& new_separate_parts, const std::string& new_vision);
	bool deleteTurret(const std::string& location_of_turret);
    bool saveTurret(const std::string& location_of_turret);
	DynamicVector<Turret> filter_by_size_and_parts(std::string& size_of_turret, int& separate_parts);
	DynamicVector<Turret> list_size(const std::string& size_of_turret);
	Turret get_current_turret() const;
	bool nextTurret() const;
	DynamicVector<Turret> mylist() const;
};
