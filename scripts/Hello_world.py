#!/usr/bin/python
file = "C:\\Users\\vklaniuk\\tmp\\transactions.txt"


file_handle = open(file, "r+")
transactions = file_handle.readlines()

for transaction in transactions:
	print (transaction)

k = 0
i = 0
for i in range(90, 100, 2):
	print ("k=", k, "|| i=", i)
	i -= 1
	k += 1
else:
	print("Loop finished.")

fruit = ["apple", "orange", "watermelon", "lemon"]
adj = ["welloy", "big", "tasty"]

for a in fruit:
	for b in adj:
		print(b, a)
else:
	print("Finished.")

for i in fruit:
    if (i == "orange"):
        continue
    print("fruit is:", i)

print(20 % 3, 18 / 3, 2**4)

print((0.1+0.2)-0.3)
print((0.1+0.2)-0.3)

i = 2
for k in range(3):
    print(i**k)

sum = 0.0
for i in range(10):
    sum += 0.1
    print(sum)

print(type(sum))

my_string = "Vadim learns python"
if (len(my_string) > 10):
    print("Lenght:", my_string, "is", len(my_string))
else: print("Lenght is <10", len(my_string))
print(my_string[::-1])

my_string = "z" + my_string[1:]
print(my_string.split())

for i in my_string.split():
    if i == "zadim":
        continue
        print (i)

print("Att{1} {2} {0}".format("ention", "python", "learner"))

name = "Vadzim"
age = 9
print(f"Hi, {name} is {age} years old")

my_first_list = [1, 2.0, "Three"]
print ("Lenght of my list is: %f" %len(my_first_list))
print ("Taking 2nd and 3rd index:", my_first_list[1:])

mod_list = my_first_list.append("new_object")
mod_list = my_first_list.append({'k0':"string"})
print(my_first_list)
print(type(my_first_list))

print("<<< Dictionary unordered mappings, index can be changed : {} is used\n>>>\n")
my_first_dic = {'k1':1.0, 'k2':2, 'k3':"char", 'k4':['A','b',4.0,900,'z']}
print (my_first_dic['k4'][4].upper())
print(my_first_dic['k4'])
print(type(my_first_dic))

print("\n << TUPLES (similar lists)>>\n1. Immutable\n2. () is used\n")
my_first_tuple = (1.0, "string", 55, ["1st index string_in_list_and_in_tuple", 2.0,990], {'k1':"Key1_dic", 'k2':"Key2_dic"})
print(my_first_tuple[3][0])
print("Count elements in tuples", my_first_tuple.count(555.0), "index", my_first_tuple.index({'k1':"Key1_dic", 'k2':"Key2_dic"}))
# my_first_tuple[0] = 2.0


print("\nSet - unordered uniq collection of any data\nUsage: function set() is used")
my_first_set = set()
my_first_set.add("string")
my_first_set.add("String")
print("Set is:", my_first_set)
print(set('Mississippi'))

print("\nBooleans : True, False, None\nNone is used if we don't know which logic should be defined")
b = None
print(b)

print("Let's work with IO")
with open('C:\\Users\VKLANIUK\\tmp\\transactions.txt',mode='r') as file1:
    print(file1.read())
    print("\n\n===========================================\n\n")
    file1.seek(0)
    print(file1.read())

counter = 0
while counter <= 10:
    counter += 1
    with open('C:\\Users\VKLANIUK\\tmp\\transactions.txt',mode='a') as file2:
        file2.write("New data " + str(counter) + "\n")

#    with open('C:\\Users\VKLANIUK\\tmp\\transactions.txt',mode='r+') as file2:
#        print(file2.read())

i = 0
k = 0
for i in range(9):
    for k in range(9):
        print(i+k)
        k += 1
    i+=1


