import json

# JSON data:
x = '{ "organization":"GeeksForGeeks","city": "Noida","country": "India"}'



# python object to be appended
y = {"pin": 110096}
y1 = '{ "organization":"GeeksForGeeks","city": "Noida","country": "India"}'


# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y1)

# the result is a JSON string:
print(json.dumps(z))




print('Successfully appended to the JSON file')