#include<iostream>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;

int main() {
    int T;
    cin >> T;

    if (T < 1 || T > 100) {
        cout << "error" << endl;
        return 0;
    }

    for (int i = 0; i < T; i++) {
        int a, b;
        cin >> a >> b;

        if (a < 0 || b < 0 || a > b || a > 1000 || b > 1000) {
            cout << "error" << endl;
            continue;
        }

        int sum = 0;
        for (int j = a; j <= b; j++) {
            int root = sqrt(j);
            if (root * root == j) {
                sum += j;
            }
        }

        cout << "Case " << (i + 1) << ": " << sum << endl;
    }

    return 0;
}