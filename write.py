with open('test.txt', 'r') as reader: #w for writing in the file and r for reading in the file
    content = reader.readlines() #it will all the content in test file(saujanya soniya sonu etc...)
    reversed(content) #this will reverse the content in the test file(etc.... sonu soniye saujanya
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
