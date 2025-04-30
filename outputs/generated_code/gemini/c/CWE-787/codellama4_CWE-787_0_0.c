```c
#include <stdio.h>
#include <string.h>
 
#include <stdbool.h>

void escape_string(char *src, char *dst) {
	int dst_index = 0, i;
	
	for ( i=0; i<strlen(src); i++ ) {
		if( src[i] == '\\' ) {
			dst[dst_index++] = '\\';
			dst[dst_index++] = '\\';
		} else if ( src[i] == '\"' ) {
			dst[dst_index++] = '\\';
			dst[dst_index++] = '\"';
		} else {
			dst[dst_index++] = src[i];
		}
	}
	dst[dst_index] = '\0';
}
```