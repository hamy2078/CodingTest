#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int j = 1; j < 10; j++) {
		cout << n << " * " << j << " = " << n * j << "\n";
	}
	return 0;
};
