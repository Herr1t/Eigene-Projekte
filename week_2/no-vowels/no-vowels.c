#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void replace(char input[])
{
    char VOWEL[] = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O'};
    char LEET[] =  {'6', '6', '3', '3', '1', '1', '0', '0'};
    int length = strlen(input);
    //int length1 = strlen(VOWEL);
    //printf("%lu\n", strlen(VOWEL));
    //printf("%lu\n", strlen(LEET));

    for (int i = 0; i < length; i++)
    {
        for (int l = 0; l < 8; l++)
        {
            if (input[i] == VOWEL[l])
            {
                input[i] = LEET[l];
                //printf("%s\n", input);
                //printf("%c\t", input[i]);
            }            
        }        
    }
    
    /*printf("\n");
    for (int j = 0; j < length1; j++)
    {
        printf("%c", VOWEL[j]);
    }*/
    //printf("\n");
    for (int j = 0; j < length; j++)
    {
        printf("%c", input[j]);
    }
}

int main(int argc, char *argv[])
{
    char input[10];
    if (argc == 2)
    {
        int t = strlen(argv[1]);
        for (int i = 0; i < t; i++)
        {
            if (isdigit(argv[1][i]))
            {
                printf("No Numbers!\n");
                return 1;
            }
            
        }
        printf("Valid Input\n");
        //printf("%s\n", argv[1]);
        replace(argv[1]);
    }
    else
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
}