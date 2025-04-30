```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* This function trims space and newline characters at the end of user supplied command line argument */

void trimCharsFromEnd(char** argv) {
    char *input = argv[1];
    
    printf("'%s'\n", input);

    // Iterate from end of string
    for(int i = strlen(input) - 1; i >= 0; i--) {
        if (input[i] == ' ' || input[i] == '\n') {
            input[i] = '\0';
        } else {
            break;  // Stop when a non-space/newline character is encountered
        }
    }
    printf("'%s'\n", input);
}

int main(int argc, char *argv[])
{
    if(argc < 2){
        printf("Please provide a command line argument.\n");
        return 1;
    }
    trimCharsFromEnd(argv);
    return 0;
}
```