#include <stdlib.h>
#include <stdio.h>
#include <math.h>

unsigned long long i=0;   //Variable für die Kreditkartennummer
void flush(void);   //Initialisierung der flush Funktion

//Funktion für die Eingabe der Kreditkartennummer
int iEingabe(void)
{
    printf("Bitte geben Sie ein gültige Kreditkartennummer ein (zwischen 13 - 16 stellig): ");
    //scanf("%llu", &i);

    while (!scanf("%llu", &i))  //Schleife zum Überprüfen der Eingabe
    {
        printf("Bitte geben Sie ein gültige Kreditkartennummer ein (zwischen 13 - 16 stellig): ");
        flush();    //Aufruf der Funktion flush
    }
    
    return i;
    //printf("%li", i);
}

//Funktion zum leeren des Inputs
void flush()
{   
    int c;
    while((c=getchar())!='\n' && c!=EOF);
    return;
}

//Funktion für die Überprüfung der Kreditkartennummer auf Länge und Zugehörigkeit
int iPruefen(unsigned long long l)
{
    int count = 0;
    unsigned long long f = l;   //Kopie von l

    while (l != 0)      //Ermittlung der Menge an Stellen
    {
        l = l/10;
        count ++;
    }
    //printf("Die Nummer ist %istellig\n", count);

    if (count < 13) //Schleife für Längenerfassung
    {
        printf("INVALID\n");
    }
    else if (count > 16)
    {
        printf("INVALID\n");
    }
    else
    {
        while(f >= 100) //Schleife zum erfassen de forderen zwei Ziffern
        {
            f = f/10;
        }

        int g = f;

        //printf("Die ersten Ziffern sind: %li\n", f);

        //Schleife zum Zuordnen der Kreditkartennummer
        if (count <= 16 && count >= 13) //VISA Schleife
        {
            g = g/10;
            if (g == 4)
            {
                printf("VISA\n");
            }
            else if (count == 15)   //AMERICAN EXPRESS Schleife
            {  
                if (f == 34 || f == 37)
                {
                    printf("AMEX\n");
                }
            }  
            else if (count == 16)   //MASTERCARD Schleife
            {
                if (f == 51 || f == 52 || f == 53 || f == 54 || f == 55)
                {
                    printf("MASTERCARD\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
        }               
    }
}

//Funktion für die Anwendung des Luhn Algorithmus
int iLuhn(unsigned long long e)
{
    unsigned long long sum = 0;    //Variable für Summe
    unsigned long long sol = 0;    //Variable für Modulo der Summe
    unsigned long long tmp;   //Variable zum zwischenspeichern von Integern
    unsigned long long f = e; //Kopie von long int e

    for (int n = 0;n < 8;n++)   //Schleife zum erfassen aller zweiten Ziffern von hinten, multiplizierung und addierung
    {
        //printf("%li\n", f);
        tmp = f % 100 / 10;
        tmp = tmp * 2;
        sum = sum + tmp;
        if (tmp >= 9)
        {
            sum = sum - 9;
        }
        f = f / 100;
    }
    //printf("%i\n", sum);

    for (int n = 0;n < 8;n++)   //Schleife zum erfassen aller nicht multipliezierten Ziffern und addierung
    {
        tmp = e % 10;
        sum = sum + tmp;
        e = e / 100;
    }
    //printf("%i", sum);
    sol = sum % 10; 
    
    if (sol == 0)   //Wenn Modulo von Summe 0 dann Valide
    {
        return 0;
    }
    else    //Wenn Modulo von Summe != 0 dann Invalide
    {
        printf("INVALID\n");
        exit(1);
    }
    //printf("%li", e);
}

//Funktion zum aufrufen anderer Funktionen
int iController()
{
    iEingabe();
    iLuhn(i);
    iPruefen(i);

    return 0;
}

//main Funktion
int main(void) 
{
    iController();

    return 0;
}