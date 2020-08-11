#pragma once
#include "Domain.h"
#include "Repository.h"
#include "DynamicVector.h"
#include "Service.h"
#include <assert.h>
using namespace std;
/*
Tests for all the functions of the program: add, update, delete, size od list etc.
*/
void AddTurret_ValidInput_ReturnsTrue(Service service);
void AddTurret_InvalidInput_ReturnsFalse(Service service);
void UpdateTurret__ValidInput__Element_was_updated(Service service);
void UpdateTurret__InvalidInput__Element_was_not_updated(Service service);
void DeleteTurret_InvalidInput_ReturnsFalse(Service service);
void Size_of_List____ValidInput_for_Remove____Get_the_size_of_list_null(Service service);
void Get_size_of_list___Valid_Input_Added_from_Repository___Size_of_list_one(Repository repository);
void AddTurret___Invalid_Input_Added_from_Repository___Index_of_element_zero(Repository repository);
void UpdateTurret___Valid_Input_to_Update_an_element_call_Repository___Index_of_element_zero(Repository repository);
void UpdateTurret___Invalid_Input_to_Update_an_element_call_Repository___Index_of_element_not_found(Repository repository);
void DeleteTurret___Invalid_Input_to_Delete_an_element_call_Repository___Index_of_element_not_found(Repository repository);
void DeleteTurret___Valid_Input_to_Delete_an_element_call_Repository___Index_of_element_zero(Repository repository);
void run_all_tests(Service service, Repository repository);