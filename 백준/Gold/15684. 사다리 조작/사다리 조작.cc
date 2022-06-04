#include<bits/stdc++.h>
using namespace std;
#define MAX 31
int matrix[31][11];
int n,m,h;
int a,b;
int ans;
int dir[4][2] = {{0,1},{-1,0},{0,-1},{1,0}};
void input() {
    cin >> n >> m >> h;
    while(m--){
        cin >> a >> b;
        matrix[a][b] = 1;
    }
}
bool check() { //모든 출발지가 도착지와 같은가?
    for(int col = 1; col <=n; col++) {
        int currcol = col;
        for(int row = 0; row <= h; row++){
            if(matrix[row][currcol] == 1){
                currcol++;
            }else if(matrix[row][currcol-1] == 1){
                currcol--;
            }
        }
        if(currcol != col) return false;
    }
    return true;
}
void dfs(int cnt, int row, int col){
    if(cnt >= ans) return;
    if(check()){
        ans = cnt;
        return;
    }
    if(cnt == 3) return;
    for(int i = row; i<=h; i++){
        for(int j = col; j <n; j++){ //j가 n인 곳에 가로선을 넣으면 사다리 양쪽을 넘거갈 수도 있다!
            if(matrix[i][j] == 0 && matrix[i][j+1] != 1 && matrix[i][j-1] != 1){ //i j 에 사다리를 놓을 있다면!
                matrix[i][j] = 1;
                dfs(cnt+1, i, j);
                matrix[i][j] = 0;
            }
        }
        col = 1;
    }
}
void pro(){
    ans = 4;
    dfs(0,1,1);
    if(ans == 4){
        cout << -1;
    }else {
        cout << ans;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
//    int T; cin >> T;
//    while(T--) {
//        input();
//        pro();
//    }
    input();
    pro();
    return 0;
}