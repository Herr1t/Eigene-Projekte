#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int a = 0;
int b = 0;
int c = 0;
int d = 0;
int i = 0;

int iStart()
{
    printf("Dies ist ein sehr simpler Taschenrechner.\nBitte geben Sie nun Ihre erste Zahl ein: \t");
    scanf("%i", &a);
    printf("Geben Sie nun Ihre zwweite Zahl ein: \t");
    scanf("%i", &b);
    printf("Wählen Sie nun die gewünschte Rechenoperation aus: \n");
    printf("1 Addition , 2 Subtraktion, 3 Division, 4 Multiplikation: \t");
    scanf("%i", &d);

    return a,b,d;
}

int iAddition(a,b)
{
    c = a + b;
    return c;
}

int iSubtraktion(a,b)
{
    c = a - b;
    return c;
}

int iDivision(a,b)
{
    c = a / b;
    return c;
}

int iMultiplikation(a,b)
{
    c = a * b;
    return c;
}

int iRechnung(a,b,d)
{
    //printf("%i", d);

    if (d==1)
    {
        iAddition(a,b);
    }
    else if(d==2)
    {
        iSubtraktion(a,b);
    }
    else if (d==3)
    {
        iDivision(a,b);
    }
    else if (d==4)
    {
        iMultiplikation(a,b);
    }
    
    return c;
}

int iLoesung(int l)
{
    printf("Die Lösung lautet %i\n", l);
}

int iController()
{
    printf("hello world\n");
    
    iStart();
    iRechnung(a,b,d);
    iLoesung(c);

    return 0;
}

int main(void)
{
    iController();

    return 0;
}