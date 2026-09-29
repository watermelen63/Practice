#include<bits/stdc++.h>
using namespace std;

int region(int x1, int y1, int x2, int y2){
    return abs((x1 - x2) * (y1 - y2));
}

int main(){
    int total_region = 100 * 100, N, strongly_region, weakly_region, unsecured_region;
    cin >> N;
    int x1, x2, x3, x4, y1, y2, y3, y4;
    for (int i = 0; i < N; i++){
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
        strongly_region = region(x2, y2, x3, y3);
        weakly_region = region(x2, y2, x1, y1) + region(x4, y4, x3, y3) - strongly_region * 2;
        unsecured_region = total_region - weakly_region - strongly_region;
        cout << "Night " << i + 1 << ": " << strongly_region << " " << weakly_region << " " << unsecured_region << "\n";
    }
}