import java.util.*;
class EventRepository { private final Map<Integer,String> events = new HashMap<>(); void save(int id,String name){events.put(id,name);} String findById(int id){return events.get(id);} }
public class Main { public static void main(String[] args){ EventRepository repo=new EventRepository(); repo.save(1,"Tech Talk"); repo.save(2,"Hackathon"); System.out.println(repo.findById(2)); System.out.println(repo.findById(99)==null); } }
