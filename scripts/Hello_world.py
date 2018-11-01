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

fruit = ["apple", "orange", "watermelon"]
adj = ["welloy", "big", "tasty"]

for a in fruit:
	for b in adj:
		print(b, a)
else:
	print("Finished.")
