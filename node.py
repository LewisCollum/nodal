def addObserverToSubjects(observer, *subjects):
    for subject in subjects: subject.addObservers(observer)

class Node:
    def __init__(self, subject, strategy):
        self.subject = subject
        self.strategy = strategy        
        self.observers = set()
        self.output = None

        if subject is not None:
            try:
                iter(self.subject)
                addObserverToSubjects(self, *self.subject)
            except:
                addObserverToSubjects(self, self.subject)

    def remove(self):
        self.subject.addObservers(*self.observers)
        self.subject.removeObservers(self)

    def put(self):
        self.subject.removeObservers(*self.observers)
        self.subject.addObservers(self)        
                
    def addObservers(self, *observers):
        for observer in observers:
            self.observers.add(observer)

    def removeObservers(self, *observers):
        for observer in observers:
            self.observers.discard(observer)
        
    def __call__(self, package):
        self.output = self.strategy(package)
        for observer in self.observers:
            observer(self.output)

    def pull(self):
        return self.output


if __name__ == '__main__':
    subject = Node(None, lambda x: x)    
    node1 = Node(subject, lambda x: x + " is good")
    node2 = Node(node1, lambda x: x + " for you")
    tail = Node(node2, print)

    subject("pizza")

    node1.remove()

    subject("pizza")

    node1.put()
    node2.remove()

    subject("pizza")
