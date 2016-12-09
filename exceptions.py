try:
    fi = open('myFile.txt')
    s = file.readline()
    i = int(s.strip())
except ValueError:
    print "Could not convert"
except IOError:
    print "Could not find file. As it is named, it does not exist.\n"


try:
    num = raw_input("Type a number here\n")
    int_num = int(num)
    print int_num
except ValueError:
    print "The character you've entered is invalid."

