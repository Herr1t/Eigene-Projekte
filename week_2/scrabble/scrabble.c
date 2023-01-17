#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
const char LETTERS[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int compute_score(char word[]);

int main(void)
{

    char word1[50];
    char word2[50];
    printf("Player 1: ");
    scanf("%s", &word1);
    printf("Player 2: ");
    scanf("%s", &word2);

    //compute_score(word1);
    //compute_score(word2);

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    //printf("%i", score1);
    //printf("%i", score2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }    
}

int compute_score(char word[])
{
    int sum = 0;
    int length = strlen(word);
    for (int i = 0; i < length; i++)
    {
        if (islower(word[i]))
        {
            word[i] = word[i] - 32;
        }
    }

    for (int l = 0; l < length; l++)
    {
        //printf("%s\n", word);
        for (int p = 0; p < 25; p++)
        {
            if (word[l] == LETTERS[p])
            {
                //printf("%i ", p);
                sum = sum + POINTS[p];
            }
        }
    }
    //printf("%i\t", sum);
}
