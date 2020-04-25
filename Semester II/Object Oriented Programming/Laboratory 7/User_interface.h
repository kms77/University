#pragma once
#include "Service.h"
#include <iostream>
#include <sstream>

class UI_console
{
private:
    Service service;
public:
    UI_console(const Service& s) : service(s) {}
    void start_program();
private:
    void add_turret(std::string given_command_as_input);
    void update_turret(std::string given_command_as_input);
    void delete_turret(std::string given_command_command_as_input);
    void list_all_turrets();
    void next_turret();
    void mylist_of_turret();
    void list_size(std::string given_command_command_as_input);
    void special_list_of_turret(std::string given_command_command_as_input);
    void save_turret(std::string given_command_command_as_input);
    bool get_admin_mode_A(const std::string& given_command_as_input);
    bool get_admin_mode_B(const std::string& given_command_as_input);
    std::string get_the_command();
};