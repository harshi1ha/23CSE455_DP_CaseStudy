import java.util.*;
interface Observer { void update(String user,String event); }
class NotificationObserver implements Observer { public void update(String u,String e){System.out.println("NOTIFY:"+u+":"+e);} }
class StatisticsObserver implements Observer { int count=0; public void update(String u,String e){count++;System.out.println("COUNT:"+count);} }
class RegistrationService { List<Observer> observers=new ArrayList<>(); void attach(Observer o){observers.add(o);} void register(String u,String e){for(Observer o:observers)o.update(u,e);} }
public class Main {public static void main(String[] a){RegistrationService s=new RegistrationService();s.attach(new NotificationObserver());s.attach(new StatisticsObserver());s.register("alice","Tech Talk");}}
