import sys

file = open(sys.argv[1])
input_1 = sys.argv[2]
set_1 = {}

for i in file:


    list1 = i[:-1].split(":")
    set_1[list1[0]] = list1[1].split(",")

for j in input_1.split(","):
    try:


        print("Name = %s\nUniversity = %s\nDepartment = %s\n" % (j, set_1[j][0], set1[j][1]))

    except KeyError:


        print("No record of ‘%s’ was found!\n" % j)
