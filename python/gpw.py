import string,random
password=""
def generatepassword(num):
	for n in range(num):
		x=random.randint(0,9)
		password=string.printable[x]
		return password
print(generatepassword(16))