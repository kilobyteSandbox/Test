spam = []

print("Enter item names.  Press enter when done.")

while True:
	itemName = input()
	if itemName == '':
		break
	spam += [itemName]

def listList(list):
        stringX = ''
        for i in range(len(list)):
                if i < len(list) - 1:
                        stringX += (list[i] + ', ')
                else:
                        stringX += ("and " + list[i])
        return stringX


print(listList(spam))

