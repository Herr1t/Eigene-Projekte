#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

int main (void)
{
    char input[] = {'H', 'a', 'l', 'l', 'o'};
    //char input[0] = {'B'};
    input[0] = 'B';
    printf("%s\n", input);
}