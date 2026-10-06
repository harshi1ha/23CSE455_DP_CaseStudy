#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;
class EventRepository { unordered_map<int,string> events; public: void save(int id,string name){events[id]=name;} string* findById(int id){auto it=events.find(id); return it==events.end()?nullptr:&it->second;} };
int main(){EventRepository repo; repo.save(1,"Tech Talk"); repo.save(2,"Hackathon"); cout<<*repo.findById(2)<<"\n"<<boolalpha<<(repo.findById(99)==nullptr)<<"\n";}
