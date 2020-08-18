#include "Service.h"
#include "Repository.h"
#include "UI.h"
#include<stdlib.h>
#include<crtdbg.h>
#define _CRTDBG_MAP_ALLOC
int main()
{
	Repository* repository = create_repository();
	Service* service = create_service(repository);
	User_Interface* ui= createUIconsole(service);
	start_program(ui);
	destroy_UIconsole(ui);
	_CrtDumpMemoryLeaks();
	return 0;
}