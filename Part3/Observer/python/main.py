class Observer:
    def update(self, user, event): raise NotImplementedError
class NotificationObserver(Observer):
    def update(self,user,event): print(f'NOTIFY:{user}:{event}')
class StatisticsObserver(Observer):
    def __init__(self): self.count=0
    def update(self,user,event): self.count+=1; print(f'COUNT:{self.count}')
class RegistrationService:
    def __init__(self): self.observers=[]
    def attach(self,o): self.observers.append(o)
    def register(self,user,event):
        for o in self.observers: o.update(user,event)
def main():
    s=RegistrationService(); s.attach(NotificationObserver()); s.attach(StatisticsObserver()); s.register('alice','Tech Talk')
if __name__=='__main__':main()
