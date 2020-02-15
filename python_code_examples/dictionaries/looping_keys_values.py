# to extract data from a dictionary - use a for-loop!

# below is a Python dictionary - note how it differs in structure from
# a Python list - a dictionary stores key-value PAIRS
cat = {'eyes': 'green', 'fur': 'brown', 'name': 'Furball', 'nose': 'pink', 'tail': 'short'}

# we have 3 different ways to extract data from a dictionary
# each one requires a for-loop

# 1. we extract only the dict keys
print("The keys:")
for k in cat.keys():
  print(k)

# 2. we extract only the dict values
print("\nThe values:")
for v in cat.values():
  print(v)

# 3. we extract both the dict keys and the dict values
print("\nThe items:")
for k, v in cat.items():
  print(k + " is key, " + v + " is value")
