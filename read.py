coun_file = open("c:/Users/TOMAS/Documents/Projects/python/text.txt", "r")
for lines in coun_file.readlines():
    print(lines)
coun_file.close()