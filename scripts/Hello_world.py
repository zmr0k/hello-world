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

