Itemsincart = 0
#2 items will be added to the cart
if Itemsincart != 2: #raise exception("products cart count not matching")
    pass

assert(Itemsincart == 0)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("hey bro!")

try:
    with open('filelog.txt', 'r') as reader: #so "text.txt" should be written to be print no error
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
