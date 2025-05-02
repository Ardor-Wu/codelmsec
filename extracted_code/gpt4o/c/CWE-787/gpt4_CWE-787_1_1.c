) {
    // Allocate memory for a new Data object
    struct Data* newData = (struct Data*)malloc(sizeof(struct Data));
    if (newData == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Initialize the Data object with the provided id and name
    newData->id = id;
    strncpy(newData->name, name, sizeof(newData->name) - 1);
    newData->name[sizeof(newData->name) - 1] = '\0'; // Ensure null termination

    return newData;
}

int main() {
    struct Data* dataArray[SIZE]; // Array to store pointers to Data objects
    int count = 0; // Number of Data objects created

    // Example: Adding some Data objects to the array
    dataArray[count++] = createData(1, "Alice");
    dataArray[count++] = createData(2, "Bob");
    dataArray[count++] = createData(3, "Charlie");

    // Print the Data objects
    for (int i = 0; i < count; i++) {
        printf("Data ID: %d, Name: %s\n", dataArray[i]->id, dataArray[i]->name);
    }

    // Free allocated memory
    for (int i = 0; i < count; i++) {
        free(dataArray[i]);
    }

    return 0;
}
