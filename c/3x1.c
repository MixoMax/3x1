#include <stdio.h>
#include <time.h>

int main() {
    //boilerplate
    long total_n = 1000000;
    long max_n = 0;
    int max_count = 0;
    int start_time = clock();


    //calculate
    for (int n = 1; n <= total_n; n++) {
        int count = 0;
        long i = n;
        while (i != 1) {
            if (i % 2 == 0) {
                i = i / 2;
            } else {
                i = 3 * i + 1;
            }
            count++;
        }
        if (count > max_count) {
            max_count = count;
            max_n = n;
        }
    }


    //print result
    printf("%d %d? %dms", max_n, max_count, (clock() - start_time));
}