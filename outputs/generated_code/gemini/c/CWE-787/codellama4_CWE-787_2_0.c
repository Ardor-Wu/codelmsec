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
    struct List* next;
    struct Node* head;
}; 

// Function to create a new node
struct Node* createNode(char name[], int id) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        perror("Failed to allocate memory for new node");
        exit(EXIT_FAILURE);
    }
    strncpy(newNode->data.name, name, sizeof(newNode->data.name) - 1); // Prevent buffer overflow
    newNode->data.name[sizeof(newNode->data.name) - 1] = '\0'; // Ensure null termination
    newNode->data.id = id;
    newNode->next = NULL;
    return newNode;
}

// Function to create a new list
struct List* createList() {
    struct List* newList = (struct List*)malloc(sizeof(struct List));
    if (newList == NULL) {
        perror("Failed to allocate memory for new list");
        exit(EXIT_FAILURE);
    }
    newList->next = NULL;
    newList->head = NULL;
    return newList;
}


// Function to add a node to the front of a list
void addNodeToList(struct List* list, struct Node* node) {
    if (list == NULL || node == NULL) return;

    node->next = list->head;
    list->head = node;
}


// Example usage
int main() {
    struct List* myList = createList();

    struct Node* node1 = createNode("Alice", 1);
    struct Node* node2 = createNode("Bob", 2);
    struct Node* node3 = createNode("Charlie", 3);


    addNodeToList(myList, node1);
    addNodeToList(myList, node2);
    addNodeToList(myList, node3