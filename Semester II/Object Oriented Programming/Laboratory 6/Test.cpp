#include "Test.h" 
#include <assert.h>
using namespace std;

void AddTurret_ValidInput_ReturnsTrue(Service service)
{
	bool truth_value = service.addTurret("abc", "medium", 200, 500, "def");
	assert(truth_value == true);
}

void AddTurret_InvalidInput_ReturnsFalse(Service service)
{
	bool truth_value = service.addTurret("abc", "great", 300, 55, "daf");
	assert(truth_value == false);
}
void SaveTurret_ValidInput_ReturnsTrue(Service service)
{
	bool truth_value = service.saveTurret("abc");
	assert(truth_value == true);
}

void SaveTurret_InvalidInput_ReturnsFalse(Service service)
{
	bool truth_value = service.saveTurret("abb");
	assert(truth_value == false);
}

void UpdateTurret__ValidInput__Element_was_updated(Service service)
{
	service.updateTurret("abc", "great", 300, 55, "bbc");
	DynamicVector<Turret> turrets = service.get_all_turrets();
	Turret first_turret = turrets.get_element_by_index(0);
	assert(first_turret.get_size_of_turret() == "great");
}

void UpdateTurret__InvalidInput__Element_was_not_updated(Service service)
{
	bool truth_value = service.updateTurret("ddd", "medium", 123, 333, "vision");
	DynamicVector<Turret> turrets = service.get_all_turrets();
	Turret first_turret = turrets.get_element_by_index(0);
	assert(first_turret.get_size_of_turret() == "great");
}

void DeleteTurret_InvalidInput_ReturnsFalse(Service service)
{
	bool truth_value = service.deleteTurret("ddd");
	assert(truth_value == false);
}

void Get_size_of_list____Valid_Input_for_Remove____Get_the_size_null_for_list(Service service)
{
	service.deleteTurret("abc");
	DynamicVector<Turret> turrets = service.get_all_turrets();
	assert(turrets.getSize() == 0);
}

void Get_size_of_list___Valid_Input_Added_from_Repository___Size_of_list_one(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repository.Add_turret(add_new_turret);
	assert(repository.get_size_of_list() == 1);
}

void AddTurret___Invalid_Input_Added_from_Repository___Index_of_element_zero(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repository.Add_turret(add_new_turret);
	Turret add_second_turret{ "abc","medium",50,33,"vision" };
	int verity_index = repository.Add_turret(add_second_turret);
	assert(verity_index == 0);
}
void SaveTurret___Valid_Input_function_call_Repository___Save_to_List(Repository repository)
{
	Turret save_new_turret{ "abc","",0,0,"" };
	int verity_index = repository.Save_turret(save_new_turret);
	assert(verity_index == -1);
}

void UpdateTurret___Valid_Input_to_Update_an_element_call_Repository___Index_of_element_zero(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	int verity_index = repository.Add_turret(add_new_turret);
	Turret update_new_turret{ "abc","get",54,122,"vision" };
	verity_index = repository.Update_turret(update_new_turret);
	assert(verity_index == 0);
}

void UpdateTurret___Invalid_Input_to_Update_an_element_call_Repository___Index_of_element_not_found(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	int verity_index = repository.Add_turret(add_new_turret);
	Turret update_new_turret{ "abb","get",54,122,"vision" };
	verity_index = repository.Update_turret(update_new_turret);
	assert(verity_index == NOT_FOUND);
}

void DeleteTurret___Invalid_Input_to_Delete_an_element_call_Repository___Index_of_element_not_found(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repository.Add_turret(add_new_turret);
	Turret delete_turret{ "abb","",0,0,"" };
	int verify_index = repository.Delete_turret(delete_turret);
	assert(verify_index == NOT_FOUND);
}

void DeleteTurret___Valid_Input_to_Delete_an_element_call_Repository___Index_of_element_zero(Repository repository)
{
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repository.Add_turret(add_new_turret);
	Turret delete_turret{ "abc","",0,0,"" };
	int verify_index = repository.Delete_turret(delete_turret);
	assert(verify_index == 0);
}

void run_all_tests(Service service, Repository repository)
{
	AddTurret_ValidInput_ReturnsTrue(service);
	AddTurret_InvalidInput_ReturnsFalse(service);
	SaveTurret_ValidInput_ReturnsTrue(service);
	SaveTurret_InvalidInput_ReturnsFalse(service);
	UpdateTurret__ValidInput__Element_was_updated(service);
	UpdateTurret__InvalidInput__Element_was_not_updated(service);
	DeleteTurret_InvalidInput_ReturnsFalse(service);
	Get_size_of_list____Valid_Input_for_Remove____Get_the_size_null_for_list(service);
	Get_size_of_list___Valid_Input_Added_from_Repository___Size_of_list_one(repository);
	AddTurret___Invalid_Input_Added_from_Repository___Index_of_element_zero(repository);
	SaveTurret___Valid_Input_function_call_Repository___Save_to_List(repository);
	UpdateTurret___Valid_Input_to_Update_an_element_call_Repository___Index_of_element_zero(repository);
	UpdateTurret___Invalid_Input_to_Update_an_element_call_Repository___Index_of_element_not_found(repository);
	DeleteTurret___Invalid_Input_to_Delete_an_element_call_Repository___Index_of_element_not_found(repository);
	DeleteTurret___Valid_Input_to_Delete_an_element_call_Repository___Index_of_element_zero(repository);
}