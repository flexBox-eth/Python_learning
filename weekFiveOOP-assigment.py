# ===============================
# Assignment 1: Hustler OOP Challenge
# ===============================

# Part 1: Hustler Class 🏗️

# Parent class
class Hustler:
    def __init__(self, name, skill, city):
        self.name = name
        self.skill = skill
        self.city = city

    def show_info(self):
        print(f"{self.name} hustles hard in {self.city} with {self.skill}! 💪")

# Child class with inheritance and extra attribute
class FlyingHustler(Hustler):
    def __init__(self, name, skill, city, wingspan):
        super().__init__(name, skill, city)
        self.wingspan = wingspan

    # Method overriding (polymorphism)
    def show_info(self):
        print(f"{self.name} hustles while flying over {self.city} with {self.skill} 🕊️, wingspan: {self.wingspan} meters!")

# Creating objects
hustler1 = Hustler("Shadow", "Negotiation", "Metro City")
hustler2 = FlyingHustler("Skyblade", "Networking", "Sky City", 12)

# Displaying info
print("=== Hustlers Info ===")
hustler1.show_info()
hustler2.show_info()

print("\n")

# Part 2: Polymorphism Challenge 🎭

class Car:
    def move(self):
        print("Car is Driving 🚗")

class Plane:
    def move(self):
        print("Plane is Flying ✈️")

class Boat:
    def move(self):
        print("Boat is Sailing ⛴️")

# List of vehicle objects
vehicles = [Car(), Plane(), Boat()]

print("=== Vehicle Movements ===")
for vehicle in vehicles:
    vehicle.move()
