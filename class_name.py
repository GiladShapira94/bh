class Test:
    def __init__(self):
        self.name = 'test'
    def func(self,event):
        print(self.name)
        print(event)
        return self.name
