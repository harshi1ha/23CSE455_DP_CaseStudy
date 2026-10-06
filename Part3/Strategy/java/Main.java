import java.util.*;
class Event { String name,category; Event(String n,String c){name=n;category=c;} }
interface Strategy { List<Event> apply(List<Event> events,String value); }
class CategoryStrategy implements Strategy { public List<Event> apply(List<Event> e,String v){List<Event> r=new ArrayList<>(); for(Event x:e) if(x.category.equals(v)) r.add(x); return r;} }
class NameStrategy implements Strategy { public List<Event> apply(List<Event> e,String v){List<Event> r=new ArrayList<>(); for(Event x:e) if(x.name.toLowerCase().contains(v.toLowerCase())) r.add(x); return r;} }
public class Main { static String names(List<Event> e){StringBuilder s=new StringBuilder(); for(Event x:e){if(s.length()>0)s.append(',');s.append(x.name);}return s.toString();} public static void main(String[] a){List<Event> e=Arrays.asList(new Event("Python Workshop","tech"),new Event("Music Night","cultural"),new Event("Python Hackathon","tech")); System.out.println(names(new CategoryStrategy().apply(e,"tech"))); System.out.println(names(new NameStrategy().apply(e,"python")));}}
