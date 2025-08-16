class Bike :
    def __init__(self, modelname):
        self.modelname = modelname

    def start_engine(self):
        print("engine started ...")

    def details(self):
        print(f"{self.modelname} is a nice bike. ")

    
obj = Bike("Shine")
obj.details()
print(obj.modelname)


