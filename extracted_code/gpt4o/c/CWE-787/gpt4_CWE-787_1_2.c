i = 0; i < SIZE; i++) {
        if (dataArray[i] != NULL) {
            free(dataArray[i]); // Free each dynamically allocated Data object.
            dataArray[i] = NULL; // Set the pointer to NULL to avoid dangling pointers.
        }
    }
    free(dataArray); // Free the array of pointers itself.
}

int main() {
    // Allocate memory for an array of pointers to struct Data.
    struct Data** dataArray = (struct Data**)malloc(SIZE * sizeof(struct Data*));
    if (dataArray == NULL) {
        fprintf(stderr, "Memory allocation failed for dataArray.\n");
        return 1;
    }

    // Initialize the array with dynamically allocated Data objects.
    for (int i = 0; i < SIZE; i++) {
        dataArray[i] = (struct Data*)malloc(sizeof(struct Data));
        if (dataArray[i] == NULL) {
            fprintf(stderr, "Memory allocation failed for dataArray[%d].\n", i);
            // Free already allocated memory before exiting.
            freeDataArray(dataArray);
            return 1;
        }
        // Assign some sample values to the struct fields.
        dataArray[i]->id = i + 1;
        snprintf(dataArray[i]->name, sizeof(dataArray[i]->name), "Name_%d", i + 1);
    }

    // Print the data to verify.
    for (int i = 0; i < SIZE; i++) {
        printf("Data ID: %d, Name: %s\n", dataArray[i]->id, dataArray[i]->name);
    }

    // Free the allocated memory.
    freeDataArray(dataArray);

    return 0;
}
