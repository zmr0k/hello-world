
myfile = open("myfile.txt")

if myfile == True:
    print "File was opened: status", myfile
else:
        print "Error IO"
        exit(-1)

print "Read operation", myfile.read()

print "File was closed: status", myfile.close()