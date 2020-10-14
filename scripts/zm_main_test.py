def mystring(str):
    return "Returned string is", str

if __name__ == '__main__':
    rstr = mystring("This string is passing to function \"mystring()\"")
    print rstr

    str = "mystring"
    print "{} Pre inserting".format(str)