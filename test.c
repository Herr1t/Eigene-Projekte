#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main (void)
{
    /*long int number;
    int integer;
    char input[50];

    scanf("%s", &input);

    integer = atoi(input);

    while(true)
    {
    if (integer == 0)
    {
        printf("false");
    }
    else
    {
        printf("true");
        break;
    }
    }*/

    unsigned long long i = 5232277223094098;
    unsigned long long tmp = 0;
    unsigned long long sum = 0;
    printf("%llu\n", i);
    for (int n = 0;n < 8;n++)   //Schleife zum erfassen aller zweiten Ziffern von hinten, multiplizierung und addierung
    {
        //printf("%li\n", f);
        tmp = i % 100 / 10;
        tmp = tmp * 2;
        sum = sum + tmp /** 2*/;
        if (tmp >= 9)
        {
            sum = sum - 9;
        }
        i = i / 100;
        printf("sum: %llu\n", sum);
        printf("tmp: %llu\n", tmp);
        printf("i: %llu\n", i);
    }
    printf("%llu", sum);
}