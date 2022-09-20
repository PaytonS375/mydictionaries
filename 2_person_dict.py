person = {} # <-- creates an empty dictionary with no elements
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] # <-- this is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} # <-- this is a dictionary

print(person)

print(person['children'][1]) # <-- bracket gives the specific index value within the list

print(person['pets']['cat']) # <-- giving specific name value in key, will provide the name of the cat

for child in person['children']:
    print(child)

for pet in person['pets']:
    print(person['pets'][pet])