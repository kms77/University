#include "User_interface.h"
/*
user interface
 This function reads the command and calls the corrsponding command ;
*/
void UI_console::start_program()
{
    std::regex exit_command_format("exit");
    std::regex add_command_format("add(.+),(.+),(.+),(.+),(.+)");
    std::regex update_command_format("update(.+),(.+),(.+),(.+),(.+)");
    std::regex delete_command_format("delete(.+)");
    std::regex list_command_format("list");
    bool Admin_mode=false;
    std::string given_command_as_input;
    bool end_program = false;
    while (!end_program)
    {
        given_command_as_input = this->get_the_command();
        if (std::regex_match(given_command_as_input, exit_command_format))
        {
            end_program = true;
        }
        else if (Admin_mode == false)
        {
            Admin_mode = this->get_admin_mode(given_command_as_input);
            if (!Admin_mode)
            {
                std::cout << "Invalid mode" << endl;
            }
        }
        else if (Admin_mode)
        {
            if (std::regex_match(given_command_as_input, add_command_format))
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
    }
}
/*
Function which verifies if the adminstrator is the "A"- admin
Returns: True : is admin "A" mode
         False: it is not admin "A" mode
*/
bool UI_console::get_admin_mode(const std::string& mode_command)
{
    std::regex administrator_command_format("mode A");
    return regex_match(mode_command, administrator_command_format);
}

/*
Function which reads a command and return it
return :given_command- the input data
*/
std::string UI_console::get_the_command()
{
    std::string given_command;
    std::getline(cin,given_command);
    return given_command;
}
/*
Function which print all the elements of the dynamic vector(all the turrets)
*/
void UI_console::list_all_turrets()
{
    DynamicVector all_turrets = this->service.get_all_turrets();
    for (int i = 0; i < all_turrets.getSize(); i++)
    {
        Turret turret = all_turrets.get_element_by_index(i);
        std::cout << turret.toString() << std::endl;
    }
}
/*
Function which reads the input and try to update a turret by location 
Input: update_command - command to update the turret- it will be prepared
Output: a message if the command is not good
*/
void UI_console::update_turret(std::string update_command)
{
    std::string part_of_the_command = ", ";
    size_t position = 0;
    std::string word_from_command;
    int number_of_words = 0;
    std::string location_of_turret, vision, size_of_turret;
    int aura_level, separate_parts;
    while ((position = update_command.find(part_of_the_command)) != std::string::npos)
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
        update_command.erase(0, position + part_of_the_command.length());
        number_of_words++;
    }
    vision = update_command;
    bool truth_value=this->service.updateTurret(location_of_turret, size_of_turret, aura_level, separate_parts, vision);
    if (truth_value == false)
    {
        std::cout << "Element doesn't exist!" << endl;
    }
}
/*
Function which read the input for delete command;
It verifies if the turret is valid and calls the specific function;
*/
void UI_console::delete_turret(std::string delete_command)
{
    std::string location_of_turret = delete_command.substr(7);
    bool truth_value=this->service.deleteTurret(location_of_turret);
    if (truth_value == false)
    {
        std::cout << "Element doesn't exist!" << endl;
    }
}
/*
Function which add a turret to the dynamic array;
It verifies if the turret is valid and calls the specific function;
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
    bool truth_value=this->service.addTurret(location_of_turret, size_of_turret, aura_level, separate_parts, vision);
    if (truth_value == false)
    {
        std::cout << "Element exists!"<<endl;
    }
}
