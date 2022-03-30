"""Demonstrations of dictionary capabilities."""

# Declaring the type of a 
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()  # constructor function

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dic
# by its key.
schools.pop("Duke")

# test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"is_duke_present: {is_duke_present}")

# Update/reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200  

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()


# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a kay does not exist?
print(schools["UNCC"])  # This will resilt in "KeyError: 'UNCC'" -> We will be told on what line this occurs by the error