#creating and accesing set element:
my_tuple = (10,20,30,40,50)
print(my_tuple[0])   
print(my_tuple[2])   

# nested tuple:
nested_tuple = ((1,2),(3,4))
print(nested_tuple[1][0])

# repetition of tuple:
repeated_tuple = my_tuple * 2
print(repeated_tuple)

# concatenation of tuple
new_tuple = my_tuple + (60,70)
print(new_tuple)
