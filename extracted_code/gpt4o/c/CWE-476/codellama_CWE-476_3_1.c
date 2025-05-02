#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int n) {
    // Handle edge cases
    if (n <= 1) return false; // 0, 1, and negative numbers are not prime
    if (n == 2) return true;  // 2 is the only even prime number

    // Check if the number is a multiple of 2
    if (n % 2 == 0) return false;

    // Iterate from 3 to the square root of n
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false; // n is divisible by i, so it's not prime
        }
    }

    return true; // n is prime
}

int main() {
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    if (isPrime(number)) {
        printf("%d is a prime number.\n", number);
    } else {
        printf("%d is not a prime number.\n", number);
    }

    return 0;
}
