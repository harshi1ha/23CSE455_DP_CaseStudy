class NotificationObserver { update(user,event){ console.log(`NOTIFY:${user}:${event}`); } }
class StatisticsObserver { constructor(){this.count=0;} update(user,event){this.count++; console.log(`COUNT:${this.count}`);} }
class RegistrationService { constructor(){this.observers=[];} attach(o){this.observers.push(o);} register(user,event){for(const o of this.observers)o.update(user,event);} }
const s=new RegistrationService(); s.attach(new NotificationObserver()); s.attach(new StatisticsObserver()); s.register('alice','Tech Talk');
