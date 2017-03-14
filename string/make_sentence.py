"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.

// eg: for given string -> "appletablet"
// "apple", "tablet"
// "applet", "able", "t"
// "apple", "table", "t"
// "app", "let", "able", "t"

// "applet", {app, let, apple, t, applet} => 3
// "thing", {"thing"} -> 1
"""

// Example program
#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;


bool foo(string s, set<string> dic, int &cnt){
    if(s.empty())
        return true;

    for(int i=0;i<s.length();++i){
        string prefix = s.substr(0,i), suffix = s.substr(i);
       if((dic.count(prefix)&&dic.count(suffix))
            ||(dic.count(prefix)&&foo(suffix,dic,cnt))){

            cnt++;
        }
    }
    return true;
}
int main()
{
    string s = "applet";
    set<string> dic{"","app","let","t","apple","applet"};
    int cnt = 0;
    foo(s,dic,cnt);
    cout<<cnt;
}
