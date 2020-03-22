#include<iostream>
using namespace std;
int t[21];
int p[21];
int n; // 퇴사까지 남은 날짜
int ans = 0;

void go(int day, int sum) { // 1 0
	if (day == n + 1) {
		if (sum > ans) ans = sum;
		return;
	}
	if (day > n + 1) {
		return;
	}
	go(day + t[day], sum + p[day]); // 날짜도 먹고 돈도 먹고
	go(day + 1, sum); // 날짜 안먹고 돈도 안먹고
}
int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> t[i] >> p[i];
	}
	go(1, 0);
	cout << ans << '\n';
	return 0;
	// add comment
}