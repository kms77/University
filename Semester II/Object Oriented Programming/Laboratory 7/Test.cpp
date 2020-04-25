#include "Test.h" 
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <assert.h>
using namespace std;

void AddTurret_ValidInput_ReturnsTrue()
{
	FileRepository repo{"file.txt"};
	Service service{repo};
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	bool truth_value = service.addTurret("abc", "medium", 200, 500, "def");
	assert(truth_value == true);
}
void AddTurret_InvalidInput_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.addTurret("abc", "great", 300, 55, "daf");
	assert(truth_value == false);
}
void SaveTurret_ValidInput_ReturnsTrue()
{
	FileRepository repo{"file.txt"};
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.saveTurret("abc");
	assert(truth_value == true);
}
void SaveTurret_InvalidInput_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.saveTurret("abb");
	assert(truth_value == false);
}
void SaveTurret_ExistingInput_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	service.saveTurret("abc");
	bool truth_value = service.saveTurret("abc");
	assert(truth_value == false);
}
void UpdateTurret__ValidInput__ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value=service.updateTurret("abc", "great", 300, 55, "bbc");
	assert(truth_value == true);
}

void UpdateTurret__InvalidInput__ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.updateTurret("ddd", "medium", 123, 333, "vision");
	assert(truth_value == false);
}

void DeleteTurret_InvalidInput_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.deleteTurret("ddd");
	assert(truth_value == false);
}

void DeleteTurret__ValidInput__ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.deleteTurret("abc");
	assert(truth_value == true);
}

void Get_Turrets___Vector_is_empty___Size_is_zero()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::vector<Turret> get_all_turrets = service.get_all_turrets();
	assert(get_all_turrets.size() == 0);
}

void Get_Turrets___Vector_get_one_element___Verify_the_content_of_vector()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	std::vector<Turret> get_all_turrets = service.get_all_turrets();
	Turret turret("abc", "medium", 200, 500, "def");
	std::vector<Turret> truth_value;
	truth_value.push_back(turret);
	assert(truth_value[0]==get_all_turrets[0]);
}

void Get_Saved_Turrets___Vector_is_empty___Size_is_zero()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	std::vector<Turret> all_saved_turrets = service.mylist();
	assert(all_saved_turrets.size()==0);
}

void Get_Saved_Turrets___Vector_get_one_element___Verify_the_content_of_vector()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	service.saveTurret("abc");
	std::vector<Turret> all_saved_turrets = service.mylist();
	std::vector<Turret> truth_value;
	Turret turret{ "abc", "medium", 200, 500, "def" };
	truth_value.push_back(turret);
	assert(all_saved_turrets[0]== truth_value[0]);
}

void NextTurret__EmptyVector__VerifyOutput()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret next_turret=service.nextTurret();
	Turret turret_when_list_is_emplty{"", "", 0, 0, ""};
	assert(next_turret == turret_when_list_is_emplty);
}

void NextTurret____Not_an_Empty_Vector____Verify_the_content_of_output()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	Turret next_turret = service.nextTurret();
	Turret next_turret_result{ "abc", "medium", 200, 500, "def" };
	assert(next_turret == next_turret_result);
}

void NextTurret__Not_Empty_Vector__Verify_if_index_statred_again_from_first_element()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "medium", 200, 500, "def");
	service.addTurret("defg", "medium", 20330, 5500, "dgf");
	Turret a=service.nextTurret();
	Turret b=service.nextTurret();
	Turret next_turret = service.nextTurret();
	Turret next_turret_result{ "abc", "medium", 200, 500, "def" };
	assert(next_turret == next_turret_result);
}

void Get_Turrets_by_Size___Vector_is_Empty___Size_is_zero()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::vector<Turret> list_of_turrets_sorted_by_size = service.list_size("abb");
	assert(list_of_turrets_sorted_by_size.size()== 0);
}

void Get_Turrets_by_Size___Vector_is_Not_Empty___Verify_the_content_of_vector()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "big", 200, 500, "def");
	service.addTurret("defg", "medium", 20330, 5500, "dgf");
	std::vector<Turret> list_of_turrets_sorted_by_size = service.list_size("medium");
	Turret expected_result{ "defg", "medium", 20330, 5500, "dgf" };
	assert(list_of_turrets_sorted_by_size[0] == expected_result);
}

void Get_Turrets_by_Size_and_Parts___Vector_is_Empty___Size_is_zero()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::vector<Turret> list_of_turrets_sorted_by_size_and_parts = service.special_list("abb",3000);
	assert(list_of_turrets_sorted_by_size_and_parts.size() == 0);
}

void Get_Turrets_by_Size_and_Parts___Vector_is_not_Empty___Verify_the_content_of_vector()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	service.addTurret("abc", "big", 200, 500, "def");
	service.addTurret("defg", "medium", 20330, 5500, "dgf");
	std::vector<Turret> list_of_turrets_sorted_by_size_and_parts = service.special_list("medium", 3000);
	Turret expected_result{ "defg", "medium", 20330, 5500, "dgf" };
	assert(list_of_turrets_sorted_by_size_and_parts[0] == expected_result);
}

void AddTurret___Valid_Input_Added_from_Repository___ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	bool truth_value=repo.Add_turret(add_new_turret);
	assert(truth_value==true);
}

void AddTurret___Invalid_Input_Added_from_Repository___ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
    repo.Add_turret(add_new_turret);
	Turret add_second_turret{ "abc","medium",50,33,"vision" };
	bool truth_value = repo.Add_turret(add_second_turret);
	assert(truth_value==false);
}
void SaveTurret___Existing_Input_function_call_Repository___ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret save_new_turret{ "abc","medium",50,33,"vision" };
	repo.Save_turret(save_new_turret);
	Turret save_second_turret{ "abc","medium",50,33,"vision" };
	bool truth_value=repo.Save_turret(save_new_turret);
	assert(truth_value == false);
}
void Get_Turrets___Vector_is_empty_call_Repository___Size_is_zero()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::vector<Turret> get_all_turrets = repo.getTurrets();
	assert(get_all_turrets.size() == 0);
}
void Get_Turrets___Vector_is_empty__call_Repository__Size_is_one()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret turret("abc", "medium", 200, 500, "def");
	repo.Add_turret(turret);
	std::vector<Turret> get_all_turrets = repo.getTurrets();
	Turret second_turret("abc", "medium", 200, 500, "def");
	std::vector<Turret> truth_value;
	truth_value.push_back(second_turret);
	assert(truth_value[0] == get_all_turrets[0]);
}
void SaveTurret___Valid_Input_function_call_Repository___ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret save_new_turret{ "abc","medium",50,33,"vision" };
	bool truth_value = repo.Save_turret(save_new_turret);
	assert(truth_value == true);
}
void UpdateTurret___Valid_Input_to_Update_an_element_call_Repository___ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret update_new_turret{ "abb","great",0,10,"bcc" };
	bool truth_value = repo.Update_turret(update_new_turret);
	assert(truth_value == false);
}

void UpdateTurret___Invalid_Input_to_Update_an_element_call_Repository___ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret update_new_turret{ "abc","great",0,10,"bcc" };
	bool truth_value = repo.Update_turret(update_new_turret);
	assert(truth_value == true);
}

void DeleteTurret___Invalid_Input_to_Delete_an_element_call_Repository___ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret delete_turret{ "abb","",0,0,"" };
	bool truth_value = repo.Delete_turret(delete_turret);
	assert(truth_value == false);
}

void DeleteTurret___Valid_Input_to_Delete_an_element_call_Repository___ReturnsTrue()
{
	FileRepository repo{ "file.txt" };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	Turret add_new_turret{ "abc","medium",50,33,"vision" };
	repo.Add_turret(add_new_turret);
	Turret delete_turret{ "abc","",0,0,"" };
	bool truth_value = repo.Delete_turret(delete_turret);
	assert(truth_value == true);
}
void UpdateTurret_EmptyVector_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	bool truth_value = service.updateTurret("abc", "great", 300, 55, "bbc");
	assert(truth_value == false);
}
void DeleteTurret_Emptyector_ReturnsFalse()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	bool truth_value = service.deleteTurret("abc");
	assert(truth_value == false);
}
void toString___ValidInput___Returns_a_String()
{
	Turret turret{ "abc", "great", 300, 55, "bbc" };
	assert(turret.toString() == "abc, great, 300, 55, bbc");
}
void SaveTurret_ValidInput_MultipleTurretsSaved()
{
	FileRepository repo{ "file.txt" };
	Service service{ repo };
	std::ofstream out;
	out.open("file.txt", std::ofstream::out | std::ofstream::trunc);
	out.close();
	std::ofstream out_mylist;
	out_mylist.open("mylist.txt", std::ofstream::out | std::ofstream::trunc);
	out_mylist.close();
	service.addTurret("abb", "medium", 200, 500, "def");
	bool value = service.saveTurret("abb");
	service.addTurret("abc", "medium", 200, 500, "def");
	bool truth_value = service.saveTurret("abc");
	assert(truth_value == true);
}
void filelocation___Get_the_Path__Verify_the_Path()
{

}
void run_all_tests()
{
	AddTurret_ValidInput_ReturnsTrue();
	AddTurret_InvalidInput_ReturnsFalse();
	SaveTurret_ValidInput_ReturnsTrue();
	SaveTurret_InvalidInput_ReturnsFalse();
	SaveTurret_ExistingInput_ReturnsFalse();
	UpdateTurret__ValidInput__ReturnsTrue();
	UpdateTurret__InvalidInput__ReturnsFalse();
	DeleteTurret_InvalidInput_ReturnsFalse();
	DeleteTurret__ValidInput__ReturnsTrue();
	Get_Turrets___Vector_is_empty___Size_is_zero();
	Get_Turrets___Vector_get_one_element___Verify_the_content_of_vector();
	AddTurret___Valid_Input_Added_from_Repository___ReturnsTrue();
	AddTurret___Invalid_Input_Added_from_Repository___ReturnsFalse();
	SaveTurret___Valid_Input_function_call_Repository___ReturnsTrue();
	SaveTurret___Existing_Input_function_call_Repository___ReturnsFalse();
	UpdateTurret___Valid_Input_to_Update_an_element_call_Repository___ReturnsTrue();
	UpdateTurret___Invalid_Input_to_Update_an_element_call_Repository___ReturnsFalse();
	DeleteTurret___Invalid_Input_to_Delete_an_element_call_Repository___ReturnsFalse();
	DeleteTurret___Valid_Input_to_Delete_an_element_call_Repository___ReturnsTrue();
	Get_Turrets___Vector_is_empty__call_Repository__Size_is_one();
	Get_Turrets___Vector_is_empty__call_Repository__Size_is_one();
	Get_Turrets_by_Size_and_Parts___Vector_is_not_Empty___Verify_the_content_of_vector();
	Get_Turrets_by_Size_and_Parts___Vector_is_Empty___Size_is_zero();
	Get_Turrets_by_Size___Vector_is_Not_Empty___Verify_the_content_of_vector();
	Get_Turrets_by_Size___Vector_is_Empty___Size_is_zero();
	NextTurret__Not_Empty_Vector__Verify_if_index_statred_again_from_first_element();
	NextTurret____Not_an_Empty_Vector____Verify_the_content_of_output();
	NextTurret__EmptyVector__VerifyOutput();
	Get_Saved_Turrets___Vector_get_one_element___Verify_the_content_of_vector();
	Get_Saved_Turrets___Vector_is_empty___Size_is_zero();
	Get_Turrets___Vector_get_one_element___Verify_the_content_of_vector();
	Get_Turrets___Vector_is_empty___Size_is_zero();
	Get_Turrets___Vector_is_empty_call_Repository___Size_is_zero();
	UpdateTurret_EmptyVector_ReturnsFalse();
	SaveTurret_ValidInput_MultipleTurretsSaved();
	toString___ValidInput___Returns_a_String();
	DeleteTurret_Emptyector_ReturnsFalse();
	filelocation___Get_the_Path__Verify_the_Path();
}