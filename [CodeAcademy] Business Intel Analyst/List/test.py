incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]

names = []
location = []
age = []

for record in incoming_class:
  # append the name, age, BMI, and insurance cost from the current medical record 
  names.append(record[0])
  location.append(record[1])
  age.append(record[2])
  
  
print(names)
print(location)
print(age)