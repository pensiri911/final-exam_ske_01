# Create code for checking delivery

# Project overview
    This project is about writing oop 
    coding to create code for checking delivery
    
# Features
    we have class "Person", "Customer", "Driver", "DeliveryOrder"

    Person
    Person is mother class of "Customer" and "driver" 
    have method introduce to show name

    Customer
    In this class have name and can use Method: introduce() 
    to show name 
    and have Method: place_order(item) 
    to create order type object with item

    Driver
    Driver have name and vihecle and have Method:
    deliver(order) print summary and 
    change order status to delivered
    
    DeliveryOrder
    create from customer having customer name and item
    Method: assign_driver(driver)
    add driver object
    Method: summary():
    show order status if still prepare then show prepare summary 
    if already deliver then show deliverd status

# How to run
    create customer object first then create driver
    can use introduce to check person name
    then we can use place_order from customer to order item
    add driver to order object first
    use summary to check order status
    use deliver(order) to change status of order object
    use summary to check order status

# Project structure
    quiz_compro
    |-quiz03.py
    |-README.md
    |-iutput.txt

# Some Error
    In google doc in class customer there attribute address but i didn't put it in code because i didn't see any thing relate to address in output example
