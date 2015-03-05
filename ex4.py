# Exercise 4: Variables and Names

# Variables == A name for something ex. kris = the coolest person ever.

kris = "the coolest person ever"

print kris

# the amount of cars
cars = 100

# the amount of seats in each car
space_in_a_car = 4.0

# the amount of drivers 
drivers = 30

# the amount of passengers
passengers = 90

# the difference between how many cars are available and drivers available to drive them
cars_not_driven = cars - drivers

# names the amount of cars driven based on the amount of drivers
cars_driven = drivers

# shows the amount of space in a car 
carpool_capacity = cars_driven * space_in_a_car

# finds the amount of people per car minus the driver
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Study Drill:

# In the study drill Zed's code produces an error that says name 'car_pool_capacity' is not defined. The reason he got this error is because he added an extra _ vs that he actually named the variable 'carpool_capacity' when he called that variable


#rate per mile

ny_rate = 4.0
rate = 2.3
miles = 1055

rate_per_mile = ny_rate * miles 

print rate_per_mile














