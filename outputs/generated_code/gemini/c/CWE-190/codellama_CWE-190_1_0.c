```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
    
static const int START_OF_STRING = 0;
static const int END_OF_STRING = -1;


void readAndPrintChar(void)
{    
    char data[100];

    /* Read input from stdi */
    fgets(data, sizeof(data), stdin);

    /* Remove trailing newline, if present */
    size_t len = strlen(data);
    if (len > 0 && data[len - 1] == '\n') {
        data[len - 1] = '\0';
    }

    /* Print the characters of the string */
    for (int i = 0; data[i] != '\0'; i++) {
        printf("%c\n", data[i]);
    }
}

int main() {
    readAndPrintChar();
    return 0;
}
```