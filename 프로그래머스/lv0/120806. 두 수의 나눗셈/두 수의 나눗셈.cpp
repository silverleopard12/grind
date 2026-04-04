#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    float a = num1;
    float b = num2;
    answer = floor((a / b) * 1000);
    return answer;
}