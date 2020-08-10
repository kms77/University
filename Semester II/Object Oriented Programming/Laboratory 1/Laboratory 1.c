/*
Laboratory 1
Create a new C / C++ project and a simple application, specifically read 
from the console, and write to the screen what you read.Upload below when done.
Important: For each test run durring your adventure, when the server is done 
with test input it will send "exit" to your application, at which point it must do so immediately.
Example test run :
⦁	Hi!
⦁	exit
Expected output :
Hi!
*/
#include <stdio.h>
#include <string.h>
int main() {
    char string_to_be_read[256];
    fgets(string_to_be_read, 256, stdin);  //read a string which can contain spaces
    printf("%s", string_to_be_read); //print the string on the screen 
    return 0;
}