#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {

    int count[1000] = {0};

    for(int i = 0; i < array.size(); i++){
        count[array[i]]++;
    }

    int maxCount = 0;
    int answer = -1;

    for(int i = 0; i < 1000; i++){
        if(count[i] > maxCount){
            maxCount = count[i];
            answer = i;
        }
        else if(count[i] == maxCount){
            answer = -1;
        }
    }

    return answer;
}