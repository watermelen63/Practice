#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;//座號
    if (n % 3 != 0){
        cout << n / 3 + 1 << endl;
    }else if (n % 3 == 0){
        cout << n / 3 << endl;
    }
}