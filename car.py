class Car(object):
    def __init__(self,model,color,design,company,price):
        self.model = model
        self.color = color
        self.design = design
        self.company = company
        self.price = price

    def start(self):
        print("Started")
    
    def stop(self):
        print("Stopped")
    
    def accelerate(self):
        print("Accelerated")
    
mustang = Car("F12","Red","Camouflage","Mustang",2000000)
print(mustang.start())
print(mustang.stop())
print(mustang.accelerate())
print(mustang.model)



