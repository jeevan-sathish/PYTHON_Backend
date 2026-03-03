class person:
    def __init__(self,name):
        self.name=name
        
    def greet(self):
        print(self.name)
        print(self.age)
        
    def call(self):
        print(self.age)
        
    
p=person("jeevan")
p.age=21
p.greet()
q=person("raj")
p.call()



       