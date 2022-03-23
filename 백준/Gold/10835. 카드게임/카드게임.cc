#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> Left, Right;
int dp[2020][2020];

int solve(int i, int j){
	if(i>=n || j>=n) return dp[i][j] = 0;
	if(dp[i][j] != -1) return dp[i][j];
	if(Left[i] > Right[j]){
		dp[i][j] = max(dp[i][j], solve(i, j+1)+Right[j]);
	}
	dp[i][j] = max(dp[i][j], solve(i+1, j));
	dp[i][j] = max(dp[i][j], solve(i+1, j+1));
	return dp[i][j];
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n; Left = vector<int>(n); Right = vector<int>(n);
	for(int i=0; i<n; i++) cin >> Left[i];
	for(int j=0; j<n; j++) cin >> Right[j];
	memset(dp, -1, sizeof(dp));
	cout << solve(0, 0);
}