// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <stdio.h>
#include <string.h>
int main() {
    char resumeOfStory[256];
    fgets(resumeOfStory,256,stdin);  //read a string with spaces
    printf("%s",resumeOfStory); //print that string 
    return 0;
}