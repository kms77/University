#pragma once
#include "Service.h"

typedef struct
{
	Service* service;
}User_Interface;

void start_program(User_Interface* ui);
void delete_command(User_Interface* ui);
void add_command(User_Interface* ui);
void list_command(User_Interface* ui);
void update_command(User_Interface* ui);
User_Interface* createUIconsole(Service* service);
void destroy_UIconsole(User_Interface* ui_console);