#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char ALPHb[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
char ALPHa[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int cypher(char key[])
{
    //char ALPHb = tolower(ALPHa);
    char input[26];
    int lengthi = strlen(input);
    int lengthk = strlen(key);
    int lengtha = strlen(ALPHa);
    //printf("%i\n", lengthk);
    if (lengthk < 26 || lengthk > 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    //printf("Test\n");
    for (int i = 0; i < lengthk; i++)
    {

    //printf("%i\n", lengtha);
        for (int l = 0; l < lengtha; l++)
        {
            if (key[i] == ALPHa[l])
            {
                
                printf("%c %c\n", key[i],ALPHa[l]);
            }
        }
    }

    printf("plain text:\t");
    fgets(input, 100, stdin);

    for (int i = 0; i < lengthi; i++)
    {
        //printf("%i\t", i);
        for (int a = 0; a < lengtha; a++)
        {
            //printf("%i\t", a);
            if (input[i] == ALPHa[a])
            {
                input[i] = key[a];    
            }
            else if (input[i] == ALPHb[a])
            {
                input[i] = key[a];
                input[i] =tolower(input[i]);
                //printf("%c\n", input[i]);
            }
        }
    }
    printf("cyper text:\t%s", input);
}

int main(int argc, char *argv[]) 
{
    if (argc == 2)
    {
        printf("Valid Key\n");
        printf("%s\n", argv[1]);
        cypher(argv[1]);
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}