/*
Laboratory 2
For a list of birth dates, determine the persons who have not lived more than 10.000 days. 
Remember to "exit" when prompted.
Example test run:
01-01-2019 17-03-1983
exit
Expected output:
01-01-2019
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int day_integer, month_integer, year_integer;
    char day_char_value[3], month_char_value[3], year_char_value[5], date[20], * parts_the_date, answers[100][100], row_of_matrix = 0, copy_of_date[20];
    while (scanf("%s", date))
    {
        strcpy(copy_of_date, date); // we make a copy of date. It will be use into the list of answers
        if (strcmp(date, "exit") == 0)  //exit case - app is finished
            break;
        else
        {
            parts_the_date = strtok(date, "-");  //we split the date into: day-month-year 
            strcpy(day_char_value, parts_the_date);
            parts_the_date = strtok(NULL, "-");
            if (NULL != parts_the_date)
                strcpy(month_char_value, parts_the_date);
            parts_the_date = strtok(NULL, "-");
            if (NULL != parts_the_date)
                strcpy(year_char_value, parts_the_date);
            day_integer = atoi(day_char_value);    //we convert the day, the month and the year from char to integer
            month_integer = atoi(month_char_value);
            year_integer = atoi(year_char_value);
            if (validate_date(day_integer, month_integer, year_integer) == 1)   // verifies if the date is correct/ if the date exists
                if (number_of_days(day_integer, month_integer, year_integer) <= 10000) //verifies if the number of dayes is less than 10000
                {
                    for (int i = 0; i < 10; i++)          //add the date into a array of dates , maximum lenght of a string is 10
                        answers[row_of_matrix][i] = copy_of_date[i];
                    row_of_matrix++;
                }
        }
    }
    for (int i = 0; i < row_of_matrix; i++)   //print the correct dates
    {
        for (int j = 0; j < 10; j++)  //add the date into a array of dates , maximum lenght of a string is 10
        {
            printf("%c", answers[i][j]);
        }
        printf("\n");
    }
    return 0;
}
int number_of_days(int day, int month, int year) {
    /*
    The function which computes the number of days from a given date to the current date
    Input: day-day of the date / month-month of the date / year-year of the date
    Output: resultNrOfDays: number of days from given date to current date
    */
    int numberOfDays = 55, resultNumberOfDays = 0; //number of days from the start of the year and the date: 24-02-2020 is 55 (value of variable numberOfDays)
    int daysPassed = 0;
    for (int i = 1; i < month; i++) {
        if (i == 2)
            daysPassed += 28;  //month with 29 days
        else if (i < 8 && i % 2 == 1)   // from 1 to 12 there are the  months of the year
            daysPassed += 31;  //month with 31 days
        else if (i < 7)
            daysPassed += 30;  //month with 30 days
        else if (i % 2 == 0)
            daysPassed += 31;  //month with 31 days
        else
            daysPassed += 30;  //month with 30 days
    }
    daysPassed += day - 1;
    if (year == 2020)
        resultNumberOfDays = numberOfDays - daysPassed;  //decrese the days of the current year 
    else
    {
        resultNumberOfDays = 365 - daysPassed + numberOfDays;
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))  // from 1 to 12 there are the  months of the year
            if (month >= 3 || (month == 2 && day == 29))
                resultNumberOfDays = resultNumberOfDays + 1;
        year += 1;
        while (year < 2020)
        {
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
                resultNumberOfDays += 366;  //year with February having 29 days
            else
                resultNumberOfDays += 365;  //number of days in a year
            year += 1;
        }
    }
    return resultNumberOfDays;
}
int validate_date(int day, int month, int year) {
    /*
    The function which verifies if a given date exists
    Input:  day-day of the date / month-month of the date / year-year of the date
    Output: 1-the date exists
            0-the date doesn't exist
    */
    if (month < 1 || month > 12) // from 1 to 12 there are the  months of the year
    {
        return 0;
    }
    if (day < 1) { //verifies if the day is valid
        return 0;
    }
    int days = 31;   //maximum number of days in a month
    if (month == 2)
    {
        days = 28;
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))   //special year with 29 days in February month  
        {
            days = 29;   //special year with 29 days in February month
        }
    }
    else if (month == 4 || month == 6 || month == 9 || month == 11) { // from 1 to 12 there are the  months of the year 
        days = 30;   //month with 30 days
    }
    if (day > days) {
        return 0;   // not a valid date
    }
    if ((year > 2020) || (year == 2020 && month > 2) || (year == 2020 && month == 2 && day > 24)) //special case if date is from current year
        return 0;   // not a valid date
    return 1;
}