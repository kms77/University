#include <iostream>
#include <sstream>
#include "FilesRepository.h"
#include "User_Interface.h"
#include "Test.h"
#include <regex>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#define _CRTDBG_MAP_ALLOC

//fileLocation C:\Users\komsa\OneDrive\Documents\file.txt
std::string file_location()
{
    std::regex file_location_command_format("fileLocation(.+)");
    std::string given_command_as_input;
    std::string filename;
    do
    {
        std::getline(cin, given_command_as_input);
        if (std::regex_match(given_command_as_input, file_location_command_format))
        {
            filename = given_command_as_input.substr(13);
            std::ifstream in(filename);
            if (!in.is_open())
            {
                std::ofstream out(filename);
                out.close();
            }
            in.close();
        }
    } while (!std::regex_match(given_command_as_input, file_location_command_format));
    return filename;
}
int main()
{
    run_all_tests();
    /*std::string location_of_the_file = file_location();
	FileRepository repo{ location_of_the_file };
	Service service{ repo };
	UI_console ui{ service };
	ui.start_program();
	_CrtDumpMemoryLeaks();
	return 0;
    */
}