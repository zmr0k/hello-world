
# create new file
with open("file2", "a+") as file2:
    file2.write("Hello world 1\n")
    file2.write("Hello world 2\n")
#    file2.write("Hello world 3")
#    file2.write("Hello world 1\n")
    file2.close()

#try:
#    myfile = open("myfile.txt", "a+")
#    myfile.seek(0)
#    a = 8
#    print "Reading 1st", a, "chars", myfile.read(a)
#    myfile.seek(5)
#    myfile.write("New string\n")
#    print "Reading 2nd", a, "chars", myfile.read(a)

#    print myfile.readline()

#finally:
#    print "\nFile was closed correctly\n", myfile.close()
