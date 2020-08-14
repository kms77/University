#pragma once
#include <iostream>
class Turret
{
private:
	std::string location_of_turret;
	std::string size_of_turret;
	int aura_level;
	int separate_parts;
	std::string vision;
public:
	Turret();
	Turret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separte_parts, const std::string& vision);
	std::string get_location_of_turret()const { return location_of_turret; }
	std::string get_size_of_turret()const { return size_of_turret; }
	int get_aura_level()const { return aura_level; }
	int get_separate_parts()const { return separate_parts; }
	std::string get_vision()const { return vision; }
	std::string toString();
};