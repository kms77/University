#include "Repository.h"
#include <string.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
using namespace std;


std::vector <Turret> Repository::read_mylist()
{
	std::vector<Turret>saved_turrets{};
	Turret turret;
	std::ifstream fin("mylist.txt");
	while (fin >> turret)
	{
		saved_turrets.push_back(turret);
	}
	fin.close();
	return saved_turrets;
}

void Repository::write_to_mylist(std::vector<Turret>saved_turrets)
{
	std::ofstream out;
	out.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
    std::ofstream fout("mylist.txt");
	for (auto& turret : saved_turrets)
		fout << turret<<endl;
	fout.close();
}
bool Repository::Save_turret(const Turret& new_save_turret)
{
	std::vector<Turret> saved_turrets = this->read_mylist();
	std::vector<Turret>::iterator iterate = find(saved_turrets.begin(), saved_turrets.end(),new_save_turret);
	if (iterate == saved_turrets.end())
	{
		saved_turrets.push_back(new_save_turret);
		this->write_to_mylist(saved_turrets);
		return true;
	}
	return false;
}