#include<bits/stdc++.h>
using namespace std;
int main(){
    int i, j = 0, test = 0;
    for (i = 0; i < 128; i = i + j) {
        j = i + 1;
        test ++;
        cout << "Case" << test << ':' << endl << "j = " << j << " i = " << i << endl;
    }
}