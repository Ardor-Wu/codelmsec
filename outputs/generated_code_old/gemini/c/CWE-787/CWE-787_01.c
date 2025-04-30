```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Include for strcpy

#define SIZE 10

struct Data {
    int id;
    char name[20];
};

struct Data* createData(int id, char* name) {
    struct Data* data = malloc(sizeof(struct Data));
    
    if (data != NULL) {
        data->id = id;
        strncpy(data->name, name, sizeof(data->name) - 1); // Use strncpy for safe string copying
        data->name[sizeof(data->name) - 1] = '\0';      // Ensure null-termination
    }

    return data;
}

int main() {
    struct Data* dataArray[SIZE];
    int i;

    for (i = 0; i < SIZE; i++) {
        char name[20];
        snprintf(name, sizeof(name), "Data %d", i + 1); // Safe string formatting
        dataArray[i] = createData(i + 1, name);

