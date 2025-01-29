import json

# Attempt to open and load as JSON
with open('2021-10-08-rtsw_atla', 'r') as file:
    try:
        data = json.load(file)
        print("This is valid JSON data!")
    except json.JSONDecodeError:
        print("This is not valid JSON.")