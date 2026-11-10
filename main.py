
class Vehicle:
    color = "White"

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"{self.brand} - Color: {self.color}, Speed: {self.speed}")


# Create two vehicle objects
v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

# Display default shared color
v1.display_info()
v2.display_info()

# Change the class attribute
Vehicle.color = "Red"

# Display updated shared color
v1.display_info()
v2.display_info()
