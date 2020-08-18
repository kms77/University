#pragma once

typedef struct {

	int catalogueNumber;
	char* state;
	char* type;
	int value;

}File;

File* create_new_element(int catalogueNumber,char* state,char* type, int value);

void set_catalogueNumber(File* input,int catalogueNumber);

int get_catalogueNumber(File* input);

void set_the_state(File* input, char* state);

char* get_the_state(File * input);

void set_the_type(File* input,char* type);

char* get_the_type(File* input);

int get_value(File* input);

void set_the_value(File* input,int value);

void destroy_file(File* input);

void to_String(File* input, char string_value[]);

File* copy_of_the_file(File* input);
