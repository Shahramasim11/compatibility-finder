Boy_name = str(input("Enter your name: ")).lower()
Girl_name = str(input("Enter girl name: ")).lower()
print("Boy_name is: ", Boy_name)
print("Girl_name: ", Girl_name)
combined_name = Boy_name + Girl_name
print("The combined name is: ", combined_name)
l = combined_name.count("l")
print("the number of l are: ", l)
o = combined_name.count("o")
print("the number of o are: ", o)
v = combined_name.count("v")
print("the number of v are: ", v)
e = combined_name.count("e")
print("the number of e are: ", e)
t = combined_name.count("t")
print("the number of t are: ", t)
r = combined_name.count("r")
print("the number of r are: ", r)
u = combined_name.count("u")
print("the number of u are: ", u)

adding_true = t+r+u+e
print("total number of true characters:", adding_true)
adding_love = l+o+v+e
print("total number of love characters: ", adding_love)
compatibility_percentage = str(adding_true) + str(adding_love)
print("Compatibility percentage is: ",compatibility_percentage)

if compatibility_percentage <= str(50):
    print("You are and average match: ", compatibility_percentage)
else:
    print("You are best match: ", compatibility_percentage)




