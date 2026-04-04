#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    int sum = stoi(to_string(a) + to_string(b));
    int sum2 = a * b * 2;
    if (sum < sum2) return sum2;
    else return sum;
    return answer;
}