# class Cow: 
#     @staticmethod 
#     def make_sound(): 
#         print("Мууу!") 
 
# cow = Cow() 
# cow.make_sound()


# class Cars: 
#     def __init__(self, brand, model, year, odometer=0, type_of="", volume=0, is_going=False): 
#         self.brand = brand 
#         self.model = model 
#         self.year = year 
#         self.odometer = odometer 
#         self.type_of = type_of 
#         self.volume = volume 
#         self.is_going = is_going 

#     def info_about_car(self): 
#         print("Car brand:", self.brand) 
#         print("Car model:", self.model) 
#         print("Car year of production:", self.year)

#     def car_is_going(self,km): 
#         self.odometer += km 
#         self.is_going = True 
#         return self.odometer, self.is_going 

#     def car_not_going(self): 
#         self.is_going = False 
#         return self.is_going 

# car = Cars("Honda", "Civic", 2015) 
# car.info_about_car() 
# odometer, is_going = car.car_is_going(100) 
# print("Odometer after driving 100 km:", odometer) 
# print("Is car going?", is_going) 
# is_going = car.car_not_going() 
# print("Is car going?", is_going)

# class Airplane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True

#     def fly(self, distance):
#         self.odometer += distance         

#     def land(self):
#         self.is_flying = False

#     def info_about_fly(self):
#         if self.is_flying == False:
#             print("The airplane is currently flying.")
#         else:
#             print("The airplane is currently not flying.")

#     def info_about_plane(self):
#         print("Make:", self.make)
#         print("Model:", self.model)
#         print("Year:", self.year)
#         print("Max Speed:", self.max_speed)
#         print("Odometer:", self.odometer)
#         print("Is Flying:", self.is_flying)

# airplane = Airplane("Boeing", "747", 2020, 900)

# airplane.info_about_plane()
# airplane.take_off()
# airplane.info_about_fly()
# airplane.fly(1000)
# airplane.info_about_plane()
# airplane.land()
# airplane.info_about_fly()

# class Math:
#     def addition(self, a, b):
#         print(a + b)
        
#     def multiplication(self, a, b):
#         print(a * b)


#     def division(self, a, b):
#         print(a // b)

#     def subtraction(self, a, b):
#         print(a - b)


# c = Math()
# c.addition(5, 7)
# c.multiplication(45, 6)
# c.division(120, 5)
# c.subtraction(149, 78)
      