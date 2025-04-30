```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 

#define SIZ 100

int main(int argc, char **argv){
    char input[SIZ];
    int i, j, k = 0;
    
    gets(input);
    
    for(i = strlen(input) - 1; i >= 0; i--){
        if(input[i] == ' '){
            for(j = i + 1; j <= k; j++)
                printf("%c", input[j]);
            printf(" ");
            k = i -1;
        }
    }
    for(j = 0; j <= k; j++)
        printf("%c", input[j]);
    printf("\n");

    return 0;
}
```