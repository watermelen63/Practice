#include<bits/stdc++.h>
using namespace std;
int main(){
    int h,m,s,temp;
    // hours, minutes, seconds
    string T,h1,s1,m1;
    // T for AM/PM, h1 for hours, s1 for seconds, m1 for minutes
    // 24小時制轉換為12小時制
    cout <<"請輸入時間(24小時制)：" << endl;
    cout << "時 分 秒" << endl;
    cin >> h >> m >> s;
    while (1){
        if (h >= 0 and h <= 24){
            if (h > 12){
                temp = h - 12;
                if (temp < 10){
                    h1 = "0" + to_string(temp);
                }else{
                    h1 = to_string(temp);
                }
                T = "PM";
            }else{
                h1 = to_string(h);
                T = "AM";
            }
        }else{
            cout << "error" << endl;
            break;
        }
        if (m >= 0 and m <= 60){
            if (m < 10){
                m1 = "0" + to_string(m);
            }else{
                m1 = to_string(m);
            }
        }else{
            cout << "error" << endl;
            break;
        }
        if (s >= 0 and s <= 60){
            if (s < 10){
                s1 = "0" + to_string(s);
            }else{
                s1 = to_string(s);
            }
        }else{
            cout << "error" << endl;
            break;
        }
        cout << h1 << ":" << m1 << ":" << s1 << " " << T << endl;
        break;
    }
}