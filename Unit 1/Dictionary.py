# creating and accessing the element:
my_dict = {
    "name": "ABC",
    "age": 19,
    "city": "LONDON"
}
print(my_dict)

print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])

#update dictionary:
my_dict['age']=20
print(my_dict)

# removing element:
del my_dict['city']
print(my_dict)

# merging dictionary:
dict1 = {'a':1}
dict2 = {'b':2}
dict1.update(dict2)
print(dict1)
