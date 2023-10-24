#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define BASE_BITS 8
#define BASE (1 << BASE_BITS)
#define MASK (BASE - 1)
#define DIGITS(v, shift) (((v) >> shift) & MASK)

void omp_lsd_radix_sort(size_t n, unsigned data[n]) {
    unsigned *buffer = malloc(n * sizeof(unsigned));
    int total_digits = sizeof(unsigned) * 8;

    for (int shift = 0; shift < total_digits; shift += BASE_BITS) {
        size_t bucket[BASE] = {0};
        size_t local_bucket[BASE] = {0};

        // 1st pass, scan whole and check the count
#pragma omp parallel firstprivate(local_bucket)
        {
#pragma omp for schedule(static) nowait
            for (size_t i = 0; i < n; i++) {
                local_bucket[DIGITS(data[i], shift)]++;
            }

#pragma omp critical
            for (size_t i = 0; i < BASE; i++) {
                bucket[i] += local_bucket[i];
            }

#pragma omp barrier

#pragma omp single
            for (size_t i = 1; i < BASE; i++) {
                bucket[i] += bucket[i - 1];
            }

            int nthreads = omp_get_num_threads();
            int tid = omp_get_thread_num();

            for (int cur_t = nthreads - 1; cur_t >= 0; cur_t--) {
                if (cur_t == tid) {
                    for (size_t i = 0; i < BASE; i++) {
                        bucket[i] -= local_bucket[i];
                        local_bucket[i] = bucket[i];
                    }
                } else {
#pragma omp barrier
                }
            }

#pragma omp for schedule(static)
            for (size_t i = 0; i < n; i++) {
                buffer[local_bucket[DIGITS(data[i], shift)]++] = data[i];
            }
        }
        // Now move data
        unsigned *tmp = data;
        data = buffer;
        buffer = tmp;
    }
    free(buffer);
}

int main() {
    printf("Enter array length ");
    int n;
    scanf("%d", &n);
    unsigned arr[n];
    for (int i = 0; i < n; i++)
        arr[i] = rand();

    omp_lsd_radix_sort(n, arr);

    for (int i = 0; i < n; i++)
        printf("%d\n", arr[i]);

    return 0;
}
