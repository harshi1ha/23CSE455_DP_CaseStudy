class EventRepository:
    def __init__(self): self.events = {}
    def save(self, event): self.events[event['id']] = event
    def find_by_id(self, event_id): return self.events.get(event_id)

def main():
    repo = EventRepository()
    repo.save({'id': 1, 'name': 'Tech Talk'})
    repo.save({'id': 2, 'name': 'Hackathon'})
    print(repo.find_by_id(2)['name'])
    print(repo.find_by_id(99) is None)
if __name__ == '__main__': main()
