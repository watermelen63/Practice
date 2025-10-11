#include<bits/stdc++.h>
using namespace std;
int main(){
    string confirm;
    int m ,n;
    //confirm為確認是否開啟，m & n 為 m x n 階的矩陣
    cout << "是否開啟矩陣計算機(yes or no)" << endl;
    cin >> confirm;
    if (confirm != "no"){
        cout << "計算機開啟"<< endl << "請輸入你要幾乘幾的矩陣" << endl;
        cin >> m >> n;
        cout << "請輸入你的數據(以空格隔開)" <<endl;
        int num[m][n];
        for (int row = 0;row < m;row++){
            for (int i = 0;i < n;i++){
                cin >> num[row][i];
            }
        }
        cout << "數據:" << endl;
        for (int row2 = 0; row2 < m;row2++){
            for (int j = 0;j < n;j++){
                cout << num[row2][j] << " ";
            }
            cout << endl;
        }
    }else{
        cout << "計算機關閉" << endl;
    }
}