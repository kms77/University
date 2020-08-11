#include <iostream>
#include "User_Interface.h"
#include "Test.h"
#define _CRTDBG_MAP_ALLOC
/*
 call the start_program function 
*/
int main()
{
	Repository repo{};
	Service service{ repo };
	UI_console ui{ service };
    run_all_tests(service,repo);
	ui.start_program();
	_CrtDumpMemoryLeaks();
	return 0;
}