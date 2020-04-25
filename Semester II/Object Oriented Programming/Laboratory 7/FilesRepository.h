#pragma once
#include "Repository.h"
#include "Domain.h"
#include <string>

using namespace std;

class FileRepository :public Repository {
private:
	string name_of_file;
	std::vector<Turret>turrets;
	void write_to_file(std::vector<Turret>turrets);
	std::vector <Turret> read_from_file();
	int position_of_the_current;
public:
	FileRepository(const string& name_of_file);
	bool Add_turret(const Turret& new_turret);
	bool Update_turret(const Turret& new_turret);
	std::vector<Turret> getTurrets() { return read_from_file(); };
	int next_turret_iterator();
	bool Delete_turret(const Turret& turret);
};