#include "FilesRepository.h"
#include <string>
#include <sstream>
#include <fstream>

using namespace std;
FileRepository::FileRepository(const std::string& name_of_file) {
	this->name_of_file = name_of_file;
	this->position_of_the_current = 0;
}
std::vector <Turret> FileRepository::read_from_file()
{
	std::vector<Turret>turrets{};
	Turret turret;
	std::ifstream fin(this->name_of_file);
	while (fin >> turret)
	{
		turrets.push_back(turret);
	}
	fin.close();
	return turrets;
}

void FileRepository::write_to_file(std::vector<Turret>turrets)
{
	std::ofstream out;
	out.open(this->name_of_file, std::ofstream::out | std::ofstream::trunc);
	out.close();
    std::ofstream fout(this->name_of_file);
	for (auto& turret : turrets)
		fout << turret<<endl;
	fout.close();
}
bool FileRepository::Add_turret(const Turret& new_turret)
{
	std::vector<Turret> turrets = this->read_from_file();
	std::vector<Turret>::iterator iterate = find(turrets.begin(), turrets.end(), new_turret);
	if (iterate == turrets.end())
	{
		turrets.push_back(new_turret);
		this->write_to_file(turrets);
		return true;
	}
	return false;
}
int FileRepository::next_turret_iterator() 
{
	std::vector<Turret> turrets = this->read_from_file();
	if (this->position_of_the_current == turrets.size())
			this->position_of_the_current = 0;
    return this->position_of_the_current++;
}
/*
This function gets the the index of the new_turret element and calls the dynamic array for update the element found at that index
*/
bool FileRepository::Update_turret(const Turret& new_turret)
{
	std::vector<Turret> turrets = this->read_from_file();
	if (turrets.empty())
	{
		return false;
	}
	std::vector<Turret>::iterator iterate = find(turrets.begin(), turrets.end(), new_turret);
	if (iterate != turrets.end())
	{
		*iterate = new_turret;
		return true;
	}
	return false;
}
/*
This function gets the the index of the turret and calls the dynamic array for delete the element found at that index
*/
bool  FileRepository::Delete_turret(const Turret& turret)
{
	std::vector<Turret> turrets = this->read_from_file();
	if (turrets.empty())
	{
		return false;
	}
	auto iterate = std::find(turrets.begin(), turrets.end(), turret);
	if (iterate != turrets.end())
	{
		turrets.erase(iterate);
		this->write_to_file(turrets);
		return true;
	}
	return false;
}