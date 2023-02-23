#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int n = 0;
    int count = 0;
    int max_count = 0;
    int max_i = 0;
    float start_time, end_time;

    start_time = clock();
    for (i = 1; i <= 1000000; i++) {
        n = i;
        count = 0;
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            count++;
        }
        if (count > max_count) {
            max_count = count;
            max_i = i;
        }
    }
    end_time = clock();
    cout << max_i << " " << max_count << endl;
    cout << "Time: " << (end_time - start_time) / CLOCKS_PER_SEC << "s" << endl;
}