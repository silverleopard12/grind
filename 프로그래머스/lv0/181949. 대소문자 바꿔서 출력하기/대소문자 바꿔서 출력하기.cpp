#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string str;
    cin >> str;

    for(char &c : str){
        if(islower(c))
            c = toupper(c);
        else
            c = tolower(c);
    }

    cout << str << endl;
}