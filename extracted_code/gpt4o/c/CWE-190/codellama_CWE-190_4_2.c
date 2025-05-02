#define SLEEP(n) Sleep(n)
#endif

int main() {
    // Seed the random number generator
    srand((unsigned int)time(NULL));

    // Loop for a maximum of MAX_LOOPS iterations
    for (int i = 0; i < MAX_LOOPS; i++) {
        // Generate a random number between 0 and 100
        int random_number = rand() % 101;

        // Print the random number
        printf("Random number: %d\n", random_number);

        // Sleep for a short duration (e.g., 100 milliseconds)
        SLEEP(100);
    }

    return 0;
}
