#include "Domain.h"
#include <Windows.h>
#include <shellapi.h>
#include <string>
#include <vector>
#include <sstream>

Turret::Turret() :location_of_turret(""), size_of_turret(""), aura_level(), separate_parts(), vision("") {}
Turret::Turret(const std::string& location_of_turret, const std::string& size_of_turret, const int& aura_level, const int& separate_parts, const std::string& vision)
{
	this->location_of_turret = location_of_turret;
	this->size_of_turret = size_of_turret;
	this->aura_level = aura_level;
	this->separate_parts = separate_parts;
	this->vision = vision;
}
bool Turret::operator==(const  Turret& Turret)
{
    return this->location_of_turret == Turret.get_location_of_turret(); /*&&
        this->size_of_turret == Turret.get_size_of_turret() &&
        this->aura_level == Turret.get_aura_level()&&
        this->separate_parts == Turret.get_separate_parts() &&
        this->vision == Turret.get_vision();
        */
}
/*
Function that returns a method of printing an element(a turret)
*/
std::string Turret::toString()
{
	return this->get_location_of_turret() + ", " + this->get_size_of_turret() + ", " + std::to_string(this->get_aura_level()) + ", " + std::to_string(this->get_separate_parts()) + ", " + this->get_vision();
}
std::vector<std::string> Split(const std::string& s, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    bool ok = false;
    while (std::getline(tokenStream, token, delimiter))
    {
        ok = true;
        tokens.push_back(token);
    }
    return tokens;
}

std::ostream& operator<<(std::ostream& os, Turret& turret) {
    os << turret.get_location_of_turret() << "," << turret.get_size_of_turret() << "," << turret.get_aura_level() << ","
        << turret.get_separate_parts() << "," << turret.get_vision();
    return os;
}

std::istream& operator>>(std::istream& in, Turret& turret) {
    std::vector<std::string> tokens;
    std::string line;

    getline(in, line);
    if (!line.empty()) {
        tokens = Split(line, ',');
        turret.location_of_turret = tokens[0];
        turret.size_of_turret = tokens[1];
        turret.aura_level = stoi(tokens[2]);
        turret.separate_parts = stoi(tokens[3]);
        turret.vision = tokens[4];
    }
    return in;
}