// Allocate memory for a new Data instance
    struct Data* newData = (struct Data*)malloc(sizeof(struct Data));
    if (newData == NULL) {
        printf("Memory allocation failed.\n");
        exit(1); // Exit if memory allocation fails
    }

    // Initialize the Data instance with the provided id and name
    newData->id = id;
    strncpy(newData->name, name, sizeof(newData->name) - 1);
    newData->name[sizeof(newData->name) - 1] = '\0'; // Ensure null-termination

    return newData;
}

// Function to display the contents of a Data instance
void displayData(struct Data* data) {
    if (data == NULL) {
        printf("No data to display.\n");
        return;
    }
    printf("ID: %d, Name: %s\n", data->id, data->name);
}

// Function to free the memory allocated for a Data instance
void freeData(struct Data* data) {
    if (data != NULL) {
        free(data);
    }
}

int main() {
    // Create a new Data instance
    struct Data* person = createData(1, "John Doe");

    // Display the Data instance
    displayData(person);

    // Free the allocated memory
    freeData(person);

    return 0;
}
