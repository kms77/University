#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "UI.h"
#define true 1
#define _CRT_SECURE_NO_WARNINGS

User_Interface* createUIconsole(Service* service)
{
    User_Interface* newUIconsole = (User_Interface*)malloc(sizeof(User_Interface));
    newUIconsole->service = service;
    return newUIconsole;
}

void destroy_UIconsole(User_Interface* ui_console)
{
    destroy_service(ui_console->service);
    free(ui_console);
}

void  delete_command(User_Interface* ui)
{
	int catalogue_number = 0;
	char user_command_as_input[100];
	char* token_from_the_user_input;
	char catalogue_number_from_command[50];
	int checker = 0;
	fgets(user_command_as_input, 100, stdin);
	token_from_the_user_input = strtok(user_command_as_input, " ,");
	strcpy(catalogue_number_from_command, token_from_the_user_input);
	catalogue_number = atoi(catalogue_number_from_command);
	checker = delete_element_from_list(ui->service, catalogue_number);
	if (checker == -1)
		printf("Can not delete the element!\n");
}



void add_command(User_Interface* ui)
{
	int catalogue_number = 0;
	int value = 0;
	char user_command_as_input[100];
	char* token_from_the_user_input;
	char catalogue_number_from_command[50];
	char state_from_command[50];
	char type_from_command[50];
	char value_from_command[50];

	fgets(user_command_as_input, 100, stdin);
	token_from_the_user_input = strtok(user_command_as_input, " ,");
	strcpy(catalogue_number_from_command, token_from_the_user_input);
	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(state_from_command, token_from_the_user_input);

	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(type_from_command, token_from_the_user_input);

	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(value_from_command, token_from_the_user_input);

	catalogue_number = atoi(catalogue_number_from_command);
	value = atoi(value_from_command);
	int result = add_element_to_list(ui->service, catalogue_number, state_from_command, type_from_command, value);
	if (result == -1)
		printf("Can not add the element!\n");
}

void list_command(User_Interface* ui)
{
	if (ui == NULL)
		return;
	Repository* repository = get_repository(ui->service);
	int length = get_size(repository);
	char check_if_there_are_parameters;
	char file_object[50];
	int input_as_int;
	File* list_maximum_value[200];
	File* auxiliar;

	int length_of_the_list = 0;


	scanf("%c", &check_if_there_are_parameters);
	if (check_if_there_are_parameters == '\n') {
		for (int index = 0; index < length; index++)
		{
			File* file = get_element_of_list_by_position(repository, index);
			char file_string[200];
			to_String(file, file_string);
			printf("%s\n", file_string);
		}
	}
	else if (check_if_there_are_parameters != '\n') {
		int second_index = 0;
		scanf("%s", file_object);
		input_as_int = atoi(file_object);
		if (input_as_int > 0 && input_as_int < 1000)
		{
			for (int index = 0; index < length; index++) {
				File* file = get_element_of_list_by_position(repository, index);
				if (file->value < input_as_int)
				{
					list_maximum_value[length_of_the_list] = file;
					length_of_the_list++;
				}
			}
			for (int index = 0; index < length_of_the_list - 1; index++)
				for (second_index = index + 1; second_index < length_of_the_list; second_index++)
					if (strcmp(list_maximum_value[index]->state, list_maximum_value[second_index]->state) > 0)
					{
						auxiliar = list_maximum_value[index];
						list_maximum_value[index] = list_maximum_value[second_index];
						list_maximum_value[second_index] = auxiliar;
					}
			for (int i = 0; i < length_of_the_list; i++)
				printf("%d %s %s %d\n", list_maximum_value[i]->catalogueNumber, list_maximum_value[i]->state, list_maximum_value[i]->type, list_maximum_value[i]->value);
		}
		else {
			for (int i = 0; i < length; i++)
			{
			 File* file = get_element_of_list_by_position(repository, i);
				char personString[200];
				if (strcmp(file->state, file_object) == 0) {
					to_String(file, personString);
					printf("%s\n", personString);
				}
			}
		}
	}
}

void  update_command(User_Interface* ui)
{
	int catalogue_number = 0;
	int value = 0;
	char user_command_as_input[100];
	char* token_from_the_user_input;
	char catalogue_number_from_command[50];
	char state_from_command[50];
	char type_from_command[50];
	char value_from_command[50];

	fgets(user_command_as_input, 100, stdin);
	token_from_the_user_input = strtok(user_command_as_input, " ,");
	strcpy(catalogue_number_from_command, token_from_the_user_input);
	catalogue_number = atoi(catalogue_number_from_command);
	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(state_from_command, token_from_the_user_input);

	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(type_from_command, token_from_the_user_input);

	token_from_the_user_input = strtok(NULL, " ,");
	if (NULL != token_from_the_user_input)
		strcpy(value_from_command, token_from_the_user_input);

	value = atoi(value_from_command);

	update_element_from_list(ui->service, catalogue_number, state_from_command, type_from_command, value);
}

void start_program(User_Interface* ui)
{
	while (true)
	{
		char command[20];
		scanf("%s", &command);

		if (strcmp(command, "exit") == 0)
			break;
		else if (strcmp(command, "add") == 0)
			add_command(ui);
		else if (strcmp(command, "list") == 0)
			list_command(ui);
		else if (strcmp(command, "delete") == 0)
			delete_command(ui);
		else if (strcmp(command, "update") == 0)
			update_command(ui);
	}
	return 0;
}