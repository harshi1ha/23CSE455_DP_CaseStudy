class CategoryStrategy { apply(events,value){ return events.filter(e=>e.category===value); } }
class NameStrategy { apply(events,value){ return events.filter(e=>e.name.toLowerCase().includes(value.toLowerCase())); } }
const events=[{name:'Python Workshop',category:'tech'},{name:'Music Night',category:'cultural'},{name:'Python Hackathon',category:'tech'}];
console.log(new CategoryStrategy().apply(events,'tech').map(e=>e.name).join(','));
console.log(new NameStrategy().apply(events,'python').map(e=>e.name).join(','));
