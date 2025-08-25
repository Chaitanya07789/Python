class Vehicle:
    def __init__(self,name,model_no):
        self.name = name
        self.model_no = model_no

    company_name = "TATA"

    @staticmethod
    def engine_start():
        print("Engine Starting...")

    @classmethod
    def press_accerator(cls):
        print("Vehicle is speeding ..")

    def details(self):
        print(f"Vehicle name is {self.name} and it's modelnumber is {self.model_no}")


        
car = Vehicle("NEXON", "NE-6547")

car.details()
Vehicle.engine_start()
Vehicle.press_accerator()

print(Vehicle.company_name)
print(car.company_name)