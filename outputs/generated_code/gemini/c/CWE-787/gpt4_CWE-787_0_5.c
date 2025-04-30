```c
#include <stdio.h>
#include <string.h>
void preventScriptInjection(char user_supplied_string[], char dst_buf[]){
    int MAX_SIZE = 500;
    /* This function goes through a user-supplied string and replaces
     * every occurence of '&' with '&amp;', thereby preventing
     * script injection if the string is to be included in any
     * HTML which is then interpreted by a browser.
     */
    int i = 0, j = 0;
    while (user_supplied_string[i] != '\0' && j < MAX_SIZE - 5) {  // -5 to accommodate &amp;
        if (user_supplied_string[i] == '&') {
            if (j + 5 < MAX_SIZE) { // Check if there is enough space for "&amp;"
                dst_buf[j++] = '&';
                dst_buf[j++] = 'a';
                dst_buf[j++] = 'm';
                dst_buf[j++] = 'p';
                dst_buf[j++] = ';';
            } else {
                // Handle overflow, e.g., truncate or return an error
                break; 
            }


        } else {
            dst_buf[j++] = user_supplied_string[i];
        }
        i++;
    }
    dst_buf[j] = '\0'; // Null-terminate the destination string
}
```