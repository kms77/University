#pragma once
#include "Domain.h"
#include <vector>
class Repository
{
private:
	std::vector<Turret> turrets{};
	std::vector<Turret> saved_turrets{};
	int position_of_the_current=0;
public:
	Repository() {}
	virtual bool Add_turret(const Turret& new_turret)=0;
	virtual bool Update_turret(const Turret& new_turret)=0;
	virtual bool Delete_turret(const Turret& turret) = 0;
	bool Save_turret(const Turret& new_save_turret);
	virtual std::vector<Turret> getTurrets() = 0;
	std::vector<Turret> getSevedTurrets() { return read_mylist(); };
    virtual int next_turret_iterator()=0;
	std::vector <Turret> read_mylist();
	void write_to_mylist(std::vector<Turret>saved_turrets);
};