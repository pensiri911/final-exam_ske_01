class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")
        
        
class Customer(Person):
    def __init__(self,name):
        super().__init__(name)

    def place_order(self,item):
        return DeliverOrder(self.name,item)
    
class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.vehicle = vehicle
        
    def deliver(self,order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")
        order.status = "delivered"
        
class DeliverOrder:
    def __init__(self,customer,item):
        self.customer = customer
        self.item = item
        self.status = "preparing"

    def assign_driver(self,driver):
        self.driver = driver
    
    def summary(self):
        if self.status == "preparing":
            return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver.name}"
        else:
            return f"Order for {self.item} → delivered"         
                    
    

customer1 = Customer("Alice")
customer2 = Customer("Bob",)
driver = Driver("David","motorcycle")

customer1.introduce()
customer2.introduce()
driver.introduce()
print()
order1 = customer1.place_order("Laptop")
order2 = customer2.place_order("Headphones")
order1.assign_driver(driver)
order2.assign_driver(driver)
print(order1.summary())
print()
print(order2.summary())
print()
driver.deliver(order1)
driver.deliver(order2)
print()
print("Final Status:")
print(order1.summary())
print(order2.summary())
#f"Item: {}\nCustomer: {}\nStatus: {self}\nDriver: {self.driver}"