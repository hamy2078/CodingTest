#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int a[5] = { 0 };
	int sum = 0;
	for(int i = 0; i < 5; i++ )
	{
		cin >> a[i];
		sum += pow(a[i],2); // pow 제곱
	}
	cout << sum % 10;
	return 0;
};
