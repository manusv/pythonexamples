<<<<<<< HEAD
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:12:43 2018

@author: manusv
"""
=======
>>>>>>> 381217dda6bb732151ced02048b9afd54b058045
import requests
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")


# Print the status code of the response.
print(response.status_code)


response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.status_code)


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
<<<<<<< HEAD
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters) 
=======
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
>>>>>>> 381217dda6bb732151ced02048b9afd54b058045

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)
type(response.content)
<<<<<<< HEAD



# Get the response from the API endpoint.
import requests
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data["number"])
print(data)
print(type(data))
=======
#####
# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

# This is a list.
print(type(best_food_chains)) 

# Import the json library
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)

# We've successfully converted our list to a string.
print(type(best_food_chains_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {"Subway": 24722, "McDonalds": 14098, "Starbucks": 10821, "Pizza Hut": 7600}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
>>>>>>> 381217dda6bb732151ced02048b9afd54b058045
