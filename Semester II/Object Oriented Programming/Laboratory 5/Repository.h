#pragma once
#include "Domain.h"
#include "DynamicVector.h"
#include <string.h>
using namespace std;
#define NOT_FOUND -1

class Repository
{
private:
	DynamicVector turrets;
public:
	Repository(){}
	Turret get_turret_by_location(Turret& current_turret);
	int  Add_turret(Turret& new_turret);
	int Update_turret(Turret& new_turret);
	DynamicVector getTurrets()const { return turrets; }
	int Delete_turret(Turret& turret);
	int get_size_of_list();
	int get_index_by_location(Turret& current_turret);
};