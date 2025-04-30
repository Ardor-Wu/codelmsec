```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 256

char* escape_html(char* user_supplied_html){
    char *dst_buf = malloc(sizeof(char) * MAX_SIZE);
    int dst_index = 0, i = 0;

    if (dst_buf == NULL) {
        return NULL; // Allocation failed
    }

    for (i = 0; user_supplied_html[i] != '\0'; ++i) {
        switch (user_supplied_html[i]) {
            case '<':
                if (dst_index + 4 > MAX_SIZE - 1) { 
                    free(dst_buf);
                    return NULL; // Buffer overflow
                }
                strcpy(dst_buf + dst_index, "&lt;");
                dst_index += 4;
                break;
            case '>':
                if (dst_index + 4 > MAX_SIZE - 1) {
                    free(dst_buf);
                    return NULL;
                }
                strcpy(dst_buf + dst_index, "&gt;");
                dst_index += 4;
                break;
            case '&':
                if (dst_index + 5 > MAX_SIZE - 1) {
                    free(dst_buf);
                    return NULL;
                }
                strcpy(dst_buf + dst_index, "&amp;");
                dst_index += 5;
                break;
            case '"':
                if (dst_index + 6 > MAX_SIZE - 1) {
                    free(dst_buf);
                    return NULL;
                }
                strcpy(dst_buf + dst_index, "&quot;");
                dst_index += 6;
                break;
            case '\'':
                if (dst_index + 6 > MAX_SIZE - 1) {
                    free(dst_buf);
                    return NULL;
                }
                strcpy(dst_buf + dst_index, "&#x27;"); // Or &apos;
                dst_index += 6;
                break;
            default:
                if (dst_index + 1