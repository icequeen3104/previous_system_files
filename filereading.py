file = open('test.txt')
#read all the contents of file
#read n number of characters using parameters
#print(file.read(5))
#print(file.readline())
#print(file.readline())
#print(file.readline())

#read file in while loop
line = file.readline()
while line!="":
    print(line)
    line = file.readline()

#read file in for loop
for line in file.readline():
    print(line)
file.close()
