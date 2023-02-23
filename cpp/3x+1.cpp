#include <iostream>
#include <ctime>
using namespace std;

int main() {
    //boilerplate
    int_fast64_t total_n = 1000000;
    int_fast64_t max_n = 0;
    int max_count = 0;
    int start_time = clock();


    //calculate
    for (int n = 1; n <= total_n; n++) {
        int count = 0;
        int_fast64_t i = n;
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
    cout << max_n << " " << max_count << endl;
    cout << clock() - start_time << "ms" << endl;
}