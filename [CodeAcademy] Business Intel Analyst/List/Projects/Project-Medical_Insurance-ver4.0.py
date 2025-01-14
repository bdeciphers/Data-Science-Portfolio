# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking. \n")
  else:
    print("Smoking is not an issue for you.\n")

  return smoker_status


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(analyze_smoker(smoker)) + " dollars.")
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

# Estimate Andrew's insurance cost
andrew_insurance_cost = estimate_insurance_cost(name = 'Andrew', age = 39, sex = 1, num_of_children = 2, smoker = 0)