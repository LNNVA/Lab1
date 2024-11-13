#include <stdlib.h>
#include <stdbool.h>
#include "calculate_primesH.h"

bool is_prime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}
int* calculate_primes(int n, int* count) {
    *count = 0;
    int* primes = (int*) malloc(n * sizeof(int));

    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) {
            primes[*count] = i;
            (*count)++;
        }
    }
    return primes;
}
