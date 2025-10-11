#include<bits/stdc++.h>
using namespace std;
int main(){
    int k,x1,x2,y1,y2,temp;
    cout << "請輸入生命值" << endl;
    cin >> k;
    cout << "請輸入陷阱間隔以及陷阱攻擊力" << endl;
    cin >> x1 >> y1;
    cout << "請輸入第二個陷阱間隔以及陷阱攻擊力" << endl;
    cin >> x2 >> y2;
    while (k > 0){
        temp += k;
        if (temp % x1 == 0){k -= y1;}
        if (temp % x2 == 0){k -= y2;}
    }cout << "你可移動的最大距離為:" << endl << temp << endl;
}