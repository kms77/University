#include <iostream>
#include "User_interface.h"
#include <string>
#include <algorithm>
#include <vector>
#include <regex>
using namespace std;

/*
 This function read the command, print the output and call the add,remove,update and list commands;
 It represents the ui of the project;
*/
void UI_console::start_program()
{
    std::regex exit_command_format("exit");
    std::regex add_command_format("add(.+),(.+),(.+),(.+),(.+)");
    std::regex update_command_format("update(.+),(.+),(.+),(.+),(.+)");
    std::regex delete_command_format("delete(.+)");
    std::regex admin_mode_command("mode(.+)");
    std::regex next_command_format("next");
    std::regex list_command_format("list");
    std::regex list_size_command_format("list(.+)");
    std::regex mylist_command_format("mylist");
    std::regex special_list_command_format("list(.+),(.+)");
    std::regex save_command_format("save(.+)");
    std::regex admin_mode_a("mode A");
    std::regex admin_mode_b("mode B");
    bool Admin_mode_A = false;
    bool Admin_mode_B = false;
    bool end_program = false;
    std::string given_command_as_input;
    while (!end_program)
    {
        given_command_as_input = this->get_the_command();
        if (std::regex_match(given_command_as_input, exit_command_format))
        {
            end_program = true;
        }
        else if (Admin_mode_A == false && Admin_mode_B == false)
        {
            Admin_mode_A = this->get_admin_mode_A(given_command_as_input);
            Admin_mode_B = this->get_admin_mode_B(given_command_as_input);
        }
        else if (Admin_mode_A)
        {
            if (std::regex_match(given_command_as_input, admin_mode_b))
            {
                Admin_mode_B = this->get_admin_mode_B(given_command_as_input);
                Admin_mode_A = false;
            }
            else if (std::regex_match(given_command_as_input, add_command_format))
                this->add_turret(given_command_as_input);
            else if (std::regex_match(given_command_as_input, list_command_format))
                this->list_all_turrets();
            else if (std::regex_match(given_command_as_input, update_command_format))
                this->update_turret(given_command_as_input);
            else if (std::regex_match(given_command_as_input, delete_command_format))
                this->delete_turret(given_command_as_input);
            else
                std::cout << "Invalid command" << endl;
        }
        else if (Admin_mode_B)
        {
            if (std::regex_match(given_command_as_input, admin_mode_a))
            {
                Admin_mode_A = this->get_admin_mode_A(given_command_as_input);
                Admin_mode_B = false;
            }
            else if (std::regex_match(given_command_as_input, next_command_format))
                this->next_turret();
            else if (std::regex_match(given_command_as_input, special_list_command_format))
                this->special_list_of_turret(given_command_as_input);
            else if (std::regex_match(given_command_as_input, list_command_format))
                this->list_all_turrets();
            else if (std::regex_match(given_command_as_input, list_size_command_format))
                this->list_size(given_command_as_input);
            else if (std::regex_match(given_command_as_input, mylist_command_format))
                this->mylist_of_turret();
            else if (std::regex_match(given_command_as_input, save_command_format))
                this->save_turret(given_command_as_input);
            else
                std::cout << "Invalid mode" << endl;
        }
        else
        {
            std::cout << "Invalid mode" << endl;
        }
    }
}
/*
Function which verifies if the adminstrator is the "A" admin
True : is admin A mode
False: it is not admin A mode
*/
bool UI_console::get_admin_mode_A(const std::string& mode_command)
{
    std::regex administrator_command_format("mode A");
    return regex_match(mode_command, administrator_command_format);
}
bool UI_console::get_admin_mode_B(const std::string& mode_command)
{
    std::regex administrator_command_format("mode B");
    return regex_match(mode_command, administrator_command_format);
}

/*
Function which reads a command and return it
return :given_command- the input data
*/
std::string UI_console::get_the_command()
{
    std::string given_command;
    std::getline(cin, given_command);
    return given_command;
}
/*
Function which print all the elements of the dynamic vector(all the turrets)
*/
void UI_console::list_all_turrets()
{
    std::vector<Turret> all_turrets = this->service.get_all_turrets();
    if (all_turrets.size() == 0)
    {
        std::cout << "The list is empty!\n";
    }
    else
    {
        for (int i = 0; i < all_turrets.size(); i++)
        {
            Turret turret = all_turrets.at(i);
            std::cout << turret.toString() << std::endl;
        }
    }
}
void UI_console::list_size(std::string list_by_size_command)
{
    std::string size_of_turret = list_by_size_command.substr(5);
    std::vector<Turret> turrets_filter_by_size = this->service.list_size(size_of_turret);
    if (turrets_filter_by_size.size() == 0)
    {
        std::cout << "The list is empty!\n";
    }
    else
    {
        for (int i = 0; i < turrets_filter_by_size.size(); i++)
        {
            Turret turret = turrets_filter_by_size.at(i);
            std::cout << turret.toString() << std::endl;
        }
    }
}
/*
Function which reads all the specification in order tu update a turret by location
*/
void UI_console::update_turret(std::string update_command)
{
    std::string parts_command = ", ";
    size_t position = 0;
    std::string word_from_command;
    int number_of_words = 0;
    std::string location_of_turret, vision, size_of_turret;
    int aura_level, separate_parts;
    while ((position = update_command.find(parts_command)) != std::string::npos)
    {
        word_from_command = update_command.substr(0, position);
        switch (number_of_words)
        {
        case 0:
        {
            location_of_turret = word_from_command.substr(7);
            break;
        }
        case 1:
        {
            size_of_turret = word_from_command;
            break;
        }
        case 2:
        {
            aura_level = std::stoi(word_from_command);
            break;
        }
        case 3:
        {
            separate_parts = std::stoi(word_from_command);
            break;
        }
        default:
            break;
        }
        update_command.erase(0, position + parts_command.length());
        number_of_words++;
    }
    vision = update_command;
    bool truth_value = this->service.updateTurret(location_of_turret, size_of_turret, aura_level, separate_parts, vision);
    if (truth_value == false)
    {
        std::cout << "Element doesn't exist!" << endl;
    }
}
/*
Function which read the input for delete command;
It reads athe lication of the turret and call the specific function;
*/
void UI_console::delete_turret(std::string delete_command)
{
    std::string location_of_turret = delete_command.substr(7);
    bool truth_value = this->service.deleteTurret(location_of_turret);
    if (truth_value == false)
    {
        std::cout << "Element doesn't exist!" << endl;
    }
}
/*
Function which add a turret to the dynamic array;
It read the input and call the service function for adding
*/
void UI_console::add_turret(std::string add_command)
{
    std::string parts_command = ", ";
    size_t position = 0;
    std::string word_from_command;
    int number_of_words = 0;
    std::string location_of_turret, vision, size_of_turret;
    int aura_level, separate_parts;
    while ((position = add_command.find(parts_command)) != std::string::npos)
    {
        word_from_command = add_command.substr(0, position);
        switch (number_of_words)
        {
        case 0:
        {
            location_of_turret = word_from_command.substr(4);
            break;
        }
        case 1:
        {
            size_of_turret = word_from_command;
            break;
        }
        case 2:
        {
            aura_level = std::stoi(word_from_command);
            break;
        }
        case 3:
        {
            separate_parts = std::stoi(word_from_command);
            break;
        }
        }
        add_command.erase(0, position + parts_command.length());
        number_of_words++;
    }
    vision = add_command;
    bool truth_value = this->service.addTurret(location_of_turret, size_of_turret, aura_level, separate_parts, vision);
    if (truth_value == false)
    {
        std::cout << "Element exists!" << endl;
    }
}
void UI_console::next_turret()
{
    Turret current_turret = this->service.nextTurret();
    if (current_turret.get_location_of_turret() == "")
        std::cout << "The list is empty!\n";
    else
        std::cout << current_turret.toString() << endl;
}
void UI_console::mylist_of_turret()
{
    std::vector<Turret> mylist_of_saved_turrets = this->service.mylist();
    if (mylist_of_saved_turrets.size() == 0)
    {
        std::cout << "The lsit is empty!\n";
    }
    else
    {
        for (int i = 0; i < mylist_of_saved_turrets.size(); i++)
        {
            Turret turret = mylist_of_saved_turrets.at(i);
            std::cout << turret.toString() << std::endl;
        }
    }
}
void UI_console::save_turret(std::string save_command)
{
    std::string location_of_turret = save_command.substr(5);
    bool truth_value = this->service.saveTurret(location_of_turret);
    if (truth_value == false)
    {
        std::cout << "Element do not exist or already saved!" << endl;
    }
}
void UI_console::special_list_of_turret(std::string special_list_command)
{
    std::string parts_command = ", ";
    size_t position = 0;
    std::string size_of_turret;
    int separate_parts;
    position = special_list_command.find(parts_command);
    size_of_turret = special_list_command.substr(0, position);
    size_of_turret = size_of_turret.substr(5);
    special_list_command.erase(0, parts_command.length() + position);
    separate_parts = std::stoi(special_list_command);
    std::vector<Turret> turrets_filter_by_size_and_separate_parts = this->service.special_list(size_of_turret, separate_parts);
    if (turrets_filter_by_size_and_separate_parts.size() == 0)
    {
        std::cout << "The list is empty!\n" << endl;
    }
    else
    {
        for (int i = 0; i < turrets_filter_by_size_and_separate_parts.size(); i++)
        {
            Turret turret = turrets_filter_by_size_and_separate_parts.at(i);
            std::cout << turret.toString() << std::endl;
        }
    }
}