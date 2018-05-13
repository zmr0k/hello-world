
try:
    myfile = open("myfile.txt", "a+")
    myfile.seek(0)
    a = 8
    print "Reading 1st", a, "chars", myfile.read(a)
    myfile.seek(5)
    addstring = myfile.write("New string\n")
    print "Reading 2nd", a, "chars", myfile.read(a)

    print myfile.readline()

finally:
    print "\nFile was closed correctly\n", myfile.close()
