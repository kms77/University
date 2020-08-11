#pragma once
#include "Service.h"
#include <iostream>
#include <sstream>
#include <string>
#include <regex>
using namespace std;
class UI_console
{
private:
        Service service;
public:
        UI_console(const Service& s): service(s){}
        void start_program();
private:
    void add_turret(std::string given_command_as_input);
    void update_turret(std::string given_command_as_input);
    void delete_turret(std::string given_command_command_as_input);
    void list_all_turrets();
    bool get_admin_mode(const std::string& given_command_as_input);
    std::string get_the_command();
};