#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n, num;
	int max, min;
	cin >> n;
	cin >> num;
	max = num;
	min = num;
	for (int i=1; i < n; i++) {
		cin >> num;
		if (max < num) max = num;
		if (min > num) min = num;
	}
	cout << min << " " << max;
	return 0;
};
