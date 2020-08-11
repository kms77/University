#include "Domain.h"
/*
constructor- define a turret object
*/
Turret::Turret():location_of_turret(""),size_of_turret(""),aura_level(),separate_parts(),vision(""){}
Turret::Turret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision)
{
	this->location_of_turret = location_of_turret;
	this->size_of_turret =size_of_turret;
	this->aura_level = aura_level;
	this->separate_parts = separate_parts;
	this->vision = vision;
}

/*
Function that returns a method of printing an element(a turret) 
*/
std::string Turret::toString()
{
	return this->get_location_of_turret() + ", " + this->get_size_of_turret() + ", " + std::to_string(this->get_aura_level()) + ", " + std::to_string(this->get_separate_parts()) + ", " + this->get_vision();
}