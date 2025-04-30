```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// This function takes a command line produced string, trims whitespace 
// from its end and then prints it.
int main(int argc, char *argv[]) {
   // Check if exactly one commandline parameter is provided
   if(argc!=2){
      printf("One input required \n");
      return 1;
   }
   char *input = argv[1];
   int len = strlen(input);
   // Trim whitespace from the end
   while (len > 0 && (input[len - 1] == ' ' || input[len - 1] == '\t' || input[len - 1] == '\n')) {
      len--;
   }
   // Null-terminate the trimmed string
   input[len] = '\0';

   printf("%s\n", input);
   return 0;
}
```