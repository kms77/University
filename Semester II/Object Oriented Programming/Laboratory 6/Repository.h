#pragma once
#include "Domain.h"
#include "DynamicVector.h"

class Repository
{
private:
	DynamicVector<Turret> turrets;
	DynamicVector<Turret> saved_turrets;
public:
	Repository() {}
	int Add_turret(Turret& new_turret);
	int Update_turret(Turret& new_turret);
	int Save_turret(Turret& new_save_turret);
	DynamicVector<Turret> getTurrets()const { return turrets; }
	DynamicVector<Turret> getSevedTurrets()const { return saved_turrets; }
	int get_size_of_dynamic_vector() { return this->turrets.getSize(); }
	int Delete_turret(Turret& turret);
	Turret Get_current_turret() { return this->turrets.getCurrent(); }
	bool next_turret_iterator() { return this->turrets.nextIterator(); }
	int get_size_of_list();
	int get_index_by_location(Turret& turret);
};