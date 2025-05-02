Below is the completed C code based on the provided structure definitions. I have added functionality to create, add, and display nodes in a linked list. Let me know if you need additional features or modifications.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

struct Data {
    char name[10];
    int id;
};

struct Node {
    struct Node* next;
    struct Data data;
};

struct List {
    struct Node* head;
};

// Function to create a new node
struct Node* createNode(const char* name, int id) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    strncpy(newNode->data.name, name, sizeof(newNode->data.name) - 1);
    newNode->data.name[sizeof(newNode->data.name) - 1] = '\0'; // Ensure null termination
    newNode->data.id = id;
    newNode->next = NULL;
    return newNode;
}

// Function to initialize a list
struct List* createList() {
    struct List* list = (struct List*)malloc(sizeof(struct List));
    if (list == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    list->head = NULL;
    return list;
}

// Function to add a node to the list
void addNode(struct List* list, const char* name, int id) {
    struct Node* newNode = createNode(name, id);
    if (list->head == NULL) {
        list->head = newNode;
    } else {
        struct Node* temp = list->head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to display the list
void displayList(struct List* list) {
    struct Node* temp = list->head;
    while (temp != NULL) {
        printf("Name: %s, ID: %d\n", temp->data.name, temp->data.id);
        temp = temp->next;
    }
}

// Function to free the list
void freeList(struct List* list) {
    struct Node* temp = list->head;
    while (temp != NULL) {
        struct Node* next = temp->