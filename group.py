"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill":[26,"Biologist",{"Zalika":"friend","John":"partner"}],
            
            "Zalika":[28,"Artist",{"Jills":"friend"}],

            "John":[38,"Student",{"Jill":"partner"}]
            
            }

print(my_group["Jill"][2]["Zalika"])

max_age=0

for names in my_group:
    if my_group[names][0]>max_age:
        max_age=my_group[names][0]

print(max_age)

relations = 0

for names in my_group:
    relations+=len(my_group[names][2])

relations=relations/len(my_group)
print(relations)

# print(len(my_group["Jill"][2]))
# print(len(my_group["John"][2]))



