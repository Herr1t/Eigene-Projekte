#include <stdio.h>
#include <stdlib.h>

//Funktion für die Eingabe der Höhe der "Pyramide"
int iEingabe()
{
    //printf("%i", h);
    int h;  //Variable für die Höhe
    char input[50];
    do  //Schleife für die Eingabe der Höhe im Bereich 1-8
    {
        printf("Bitte geben Sie die Höhe von Welt 1-1 an (1-8): ");
        scanf("%s", &input);

        h = atoi(input);

        if (h == 0)
        {
            printf("Bitte geben Sie eine gültige Zahl an!\n");
        }
        else
        {
        }
    }
    while (h < 1 || h > 8);
    return h;
}

//Funktion für die Ausgabe/Anzeige der "Pyramide"
int iAusgabe(const int height)
{
    for (int i = 0; i < height; i++)   //Schleife für die Höhe
    {
        for (int s = 1; s <= height - i; s++)   //Schleife zum einrücken der Felder
        {
            printf(" ");
        }
        
        for (int j = 0; j <= i; j++)    //Schleife für die Platzierung auf der linken Hälfte
        {
            printf("#"); 
        }

        printf("  ");

        for (int e = 0; e <= i; e++)//Schleife für die Platzierung auf der rechten Hälfte
        {
            printf("#");
        }
        printf("\n");
    }
    //printf("%i", height);
    return 0;
}

//Funktion zum Aufrufen aderer Funktionen
int iController()
{
    //iEingabe();
    int h = iEingabe(); //Variable wird mit Funktion iEingabe gleichgesetzt

    iAusgabe(h);

    return 0;
}

//main Funktion
int main (void)
{
    iController();

    return 0;
}