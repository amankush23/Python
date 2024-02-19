class car:
    def __init__(self,Car_Name,Model,Maker,Year,Price):
        self.Car_Name = Car_Name
        self.Model = Model
        self.Maker = Maker
        self.Year = Year
        self.Price = Price
        self.available= True
    def display_cars(self):
        return f''' 
        Car Name:{self.Car_Name},
        Car Model:{self.Model},
        Maker: {self.Maker},
        Manufacturing: {self.Year},
        Price: {self.Price}'''
class dealership:
    def __init__(self,dealer_name):
        self.dealer_name = dealer_name
        self.inventory = []
    def add_car_to_inventory(self,car):
        self.inventory.append(car)
    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_cars())
                print("")
                count+=1
    def sell_car(self,c,index):
        if 0 < index <len(self.inventory) and self.inventory[index - 1].available:
            c.purchase(self.inventory[index - 1])   
            return self.inventory[index - 1]

class customer:
    def __init__(self,name):
        self.name = name
        self.purchased_car = []
    def purchase(self,car):
        self.purchased_car.append(car)
        car.available = False


car1=car('hondacity','S98',"Honda","2018",100000)
car2=car('fortuner',"Supra","Toyota",2020,2500000)
car3=car('BMW', 'code F40',"Motoren Werke AG",2021,8000000 )

d1=dealership("ABC Motors")
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_available_car()
c1= customer('ravi')
ret=d1.sell_car(c1,2)
if ret:
    print(f'{c1.name} purchased Car\n {ret.display_cars()}')
else:
    print("Not available for selling")
print("After selling Display Available Cars")
d1.display_available_car()
