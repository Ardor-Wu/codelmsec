```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 

char* strtok1(char* str, char* delimiters)
{
    static char* src = NULL;
    int i, j;
    if(str!= NULL)
        src = str;
    else
    {
        if(src == NULL)
            return NULL;
    }

    for(i = 0; src[i] != '\0'; i++)
    {
        for(j = 0; delimiters[j] != '\0'; j++)
        {
            if(src[i] == delimiters[j])
                break;
        }
        if(delimiters[j] != '\0')
            break;
    }


    if(src[i] == '\0')
    {
        src = NULL;
        return NULL;
    }

    char* start = src + i;

    // Find the end of the token
    for(i++; src[i] != '\0'; i++)
    {
        for(j = 0; delimiters[j] != '\0'; j++)
        {
            if(src[i] == delimiters[j])
                break;
        }
        if(delimiters[j] != '\0')
            break;
    }

    
    if(src[i] == '\0')
    {
        src = NULL;
    }
    else
    {
        src[i] = '\0';
        src = src + i + 1;
    }


    return start;
}

int main()
{
    char str[] = "This is a-string. Hello, world!";
    char delimiters[] = " -.,";

    char *token = strtok1(str, delimiters);

    while (token != NULL) {
        printf("%s\n", token);
        token = strtok1(NULL, delimiters);
    }

    return 0;
}
```