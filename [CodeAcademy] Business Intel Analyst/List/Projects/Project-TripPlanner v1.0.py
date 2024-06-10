# TripPlanner v1.0

# Welcome Users
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

# Call the function Trip_Planner_Welcome
trip_planner_welcome("B.Davis")

# Calculate Rounded time value
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Assign the function to a variable
estimate = estimated_time_rounded(2.55)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Cali", "Africa", estimate, "Plane")