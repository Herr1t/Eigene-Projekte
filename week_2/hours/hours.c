#include <ctype.h>
#include <math.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output, float sum);

int main(void)
{
    int sum = 0;
    int weeks = 0;
    printf("Number of weeks taking CS50: ");
    scanf("%i", &weeks);
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        printf("Week %i HW Hours: ", i);
        scanf("%i", &hours[i]);
    }

    char output;
    do
    {
        printf("Enter T for total hours, A for average hours per week: ");
        toupper(scanf("%c", &output));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output, sum));
}

float calc_hours(int hours[], int weeks, char output, float sum)
{
    if (output == 'A')
    {
        for (int i = 0; i < weeks; i++)
        {
            sum = sum + hours[i];
        }
        sum = sum / weeks;
    }
    else if (output == 'T')
    {
        for (int i = 0; i < weeks; i++)
        {
            sum = sum + hours[i];
        }
    }
    return sum;
}