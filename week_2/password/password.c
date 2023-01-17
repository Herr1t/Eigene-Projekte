#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool valid(char password[]);

int main(void)
{
    char password[25];
    printf("Enter your password: ");
    scanf("%s", &password);
    if (valid(password) == true)
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number, symbol and 8 characters in length.\n");
    }
}

bool valid(char password[])
{
    int length = strlen(password);
    bool symbol = false;
    bool uppercase = false;
    bool lowercase = false;
    bool number = false;

    if (length < 8)
    {
        return false;
    }

    for (int i = 0; i < length; i++)
    {
        if (isdigit(password[i]))
        {
            number = true;
        }
        else if (isupper(password[i]))
        {
            uppercase = true;
        }
        else if (islower(password[i]))
        {
            lowercase = true;
        }
        else
        {
            symbol = true;
        }        
    }
    
    if (number && uppercase && lowercase && symbol == true)
    {
        return true;
    }
    else
    {
        return false;
    }   
}
