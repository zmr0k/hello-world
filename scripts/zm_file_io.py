
try:
    myfile = open("myfile.txt", "a+")

    print "Read operation", myfile.read(10)
    addstring = myfile.write("New string\n")
    print "New line was added", addstring

finally:
    print "\nFile was closed correctly\n", myfile.close()
