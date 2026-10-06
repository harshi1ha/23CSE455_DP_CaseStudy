#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Observer{public:virtual void update(const string&,const string&)=0;virtual~Observer()=default;};
class NotificationObserver:public Observer{public:void update(const string&u,const string&e)override{cout<<"NOTIFY:"<<u<<":"<<e<<"\n";}};
class StatisticsObserver:public Observer{int count=0;public:void update(const string&,const string&)override{cout<<"COUNT:"<<++count<<"\n";}};
class RegistrationService{vector<Observer*> obs;public:void attach(Observer*o){obs.push_back(o);}void reg(const string&u,const string&e){for(auto*o:obs)o->update(u,e);}};
int main(){RegistrationService s;NotificationObserver n;StatisticsObserver st;s.attach(&n);s.attach(&st);s.reg("alice","Tech Talk");}
