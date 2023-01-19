#include <ctype.h>
#include <string.h>
#include <stdio.h>

char ALPHb[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
char ALPHa[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int cypher(char key[])
{
    //char ALPHb = tolower(ALPHa);
    int c = 0;
    char input[26];
    char check[26] = {};
    int lengthc = strlen(check);
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
                check[l] = ALPHa[l];
                //printf("%c %c\n", key[i],ALPHa[l]);
            }
        }
    }

    for (int i = 0; i < lengtha; i++)
    {
        if (check[i] == ALPHa[i])
        {
            c++;
        }
    }

    if (c != 26)
    {
        printf("Key must contain every Letter of the alphabet once.\n");
        return 1;
    }

    printf("plain text:\t");
    fgets(input, 100, stdin);
    int lengthi = strlen(input);

    for (int i = 0; i < lengthi; i++)
    {
        //printf("%i\t", i);
        for (int a = 0; a < lengtha; a++)
        {
            //printf("%i\t", a);
            if (input[i] == ALPHa[a])
            {
                input[i] = key[a];
                break;
            }
            else if (input[i] == ALPHb[a])
            {
                input[i] = key[a];
                input[i] = tolower(input[i]);
                //printf("%c\n", input[i]);
                break;
            }
        }
    }
    printf("cyper text:\t%s", input);
}

int main(int argc, char *argv[]) 
{
    if (argc == 2)
    {
        int t = strlen(argv[1]);
        for (int i = 0; i < t; i++)
        {
            if (isdigit(argv[1][i]))
            {
                printf("Key must contain of onl Letters from the Alphabet:\n");
                return 1;
            }
            
        }
        printf("Valid Key\n");
        //printf("%s\n", argv[1]);
        cypher(argv[1]);
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}