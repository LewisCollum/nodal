import numpy

class Annotator:
    def __init__(self, node, strategy):
        self.node = node
        self.strategy = strategy
                
    def __call__(self, annotatable):
        annotation = self.node.pull()
        annotated = self.strategy(annotatable, annotation)
        return annotated


