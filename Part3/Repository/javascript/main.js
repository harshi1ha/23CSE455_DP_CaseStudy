class EventRepository {
  constructor(){ this.events = new Map(); }
  save(event){ this.events.set(event.id, event); }
  findById(id){ return this.events.get(id); }
}
const repo = new EventRepository();
repo.save({id:1,name:'Tech Talk'}); repo.save({id:2,name:'Hackathon'});
console.log(repo.findById(2).name); console.log(repo.findById(99) === undefined);
