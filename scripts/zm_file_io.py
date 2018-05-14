
filename = "block_bruteforce_ips"

try:
    myfile = open(filename, "r")
    myfile.seek(0)
    print myfile.read()
    myfile.seek(0)
    print "reading line(s):\n"
    print myfile.readlines(4)

finally:
    print "\nFile was closed correctly\n", myfile.close()
