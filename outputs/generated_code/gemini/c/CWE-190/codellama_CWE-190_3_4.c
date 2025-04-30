```c
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

void printHaxCharLine(){

    char data; 
    data = 'A';

    for (int i = 0; i < IO_SIZE; i++)
    {
        myUnion.unionSecond[i] = data + i; // Fill with characters 'A' to 'J'
    }

    printf("0x");
    for (int i = 0; i < IO_SIZE; i++)
    {
        printf("%02X", (unsigned char)myUnion.unionSecond[i]); // Print each byte as hex
    }
    printf("\n");

}

int main() {
    printHaxCharLine();
    return 0;
}
```