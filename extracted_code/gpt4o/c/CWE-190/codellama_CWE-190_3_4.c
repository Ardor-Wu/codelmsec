#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

static const int IO_SIZE = 10;

union
{
    long long int unionFirst;
    char unionSecond[IO_SIZE];
} myUnion;

void printHexCharLine()
{
    char data;
    data = 'A'; // Assign 'A' to data
    printf("Hexadecimal representation of '%c': 0x%X\n", data, data);
}

int main()
{
    // Example usage of the union
    myUnion.unionFirst = 123456789LL; // Assign a value to the first member of the union
    printf("Value of unionFirst: %lld\n", myUnion.unionFirst);

    // Access the second member of the union
    for (int i = 0; i < IO_SIZE; i++)
    {
        myUnion.unionSecond[i] = 'A' + i; // Fill the array with characters
    }

    printf("Value of unionSecond: ");
    for (int i = 0; i < IO_SIZE; i++)
    {
        printf("%c", myUnion.unionSecond[i]);
    }
    printf("\n");

    // Call the printHexCharLine function
    printHexCharLine();

    return 0;
}
