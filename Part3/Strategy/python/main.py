class Event:
    def __init__(self, name, category): self.name, self.category = name, category
class Strategy:
    def apply(self, events, value): raise NotImplementedError
class CategoryStrategy(Strategy):
    def apply(self, events, value): return [e for e in events if e.category == value]
class NameStrategy(Strategy):
    def apply(self, events, value): return [e for e in events if value.lower() in e.name.lower()]
def main():
    events=[Event('Python Workshop','tech'),Event('Music Night','cultural'),Event('Python Hackathon','tech')]
    print(','.join(e.name for e in CategoryStrategy().apply(events,'tech')))
    print(','.join(e.name for e in NameStrategy().apply(events,'python')))
if __name__=='__main__': main()
