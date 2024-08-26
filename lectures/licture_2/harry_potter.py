

        

names = [{'name': 'ali'}, {'name': 'haret'}, {'name': 'mahdi'}]

# Update and remove keys
for name in names:
    if name["name"] == "ali":
        name.update({"name": "yosra"})  # Update "ali" to "yosra"
    if name.get("name") == "mahdi":
        name.pop("name")  # Remove the "name" key from the dictionary

# Filter out dictionaries that no longer have the "name" key
names = [name for name in names if "name" in name]

print(names)




















# x = [1,5,12,9]

# for i in range(len(x)):
#     print(i)



# student = ['herry' , 'ron', 'haret']

# for i in range(len(student)):
#     print(student)