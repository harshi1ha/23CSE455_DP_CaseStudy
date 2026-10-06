#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
struct Event{string name,category;};
class Strategy{public: virtual vector<Event> apply(const vector<Event>&,const string&)=0; virtual ~Strategy()=default;};
class CategoryStrategy:public Strategy{public:vector<Event> apply(const vector<Event>& e,const string& v) override{vector<Event> r;for(auto& x:e)if(x.category==v)r.push_back(x);return r;}};
class NameStrategy:public Strategy{public:vector<Event> apply(const vector<Event>& e,const string& v) override{vector<Event> r;for(auto& x:e)if(x.name.find(v)!=string::npos)r.push_back(x);return r;}};
void print(const vector<Event>& e){for(size_t i=0;i<e.size();i++){if(i)cout<<',';cout<<e[i].name;}cout<<'\n';}
int main(){vector<Event> e={{"Python Workshop","tech"},{"Music Night","cultural"},{"Python Hackathon","tech"}};CategoryStrategy c;NameStrategy n;print(c.apply(e,"tech"));print(n.apply(e,"Python"));}
