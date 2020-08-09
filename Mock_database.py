#Mock Database
import hashlib
import os
import random

def generateHash(SIN): 
	#Using Blake2 hash with RFC7693
	userID = hashlib.blake2b(os.urandom(5), digest_size=5)
	userID.update(b'SIN')

	return userID.hexdigest()


class User:
	def __init__(self, e_id, name, address, dob, SIN, licenseNum, licenseIssue, licenseExp, licenseRef, height, sex, licenseClass, healthNum, healthIssue, healthExp, healthRef):
		self.id = e_id 
		self.name = name                     #0
		self.address = address               #1
		self.dob = dob                       #2
		self.sin = SIN                       #3
		self.licenseNum = licenseNum         #4
		self.licenseIssue = licenseIssue     #5
		self.licenseExp = licenseExp         #6
		self.licenseRef = licenseRef         #7
		self.height = height                 #8
		self.licenseClass = licenseClass     #9
		self.sex = sex                       #10
		self.healthNum = healthNum           #11
		self.healthIssue = healthIssue       #12
		self.healthExp = healthExp           #13
		self.healthRef = healthRef           #14
	

userList = []
#other users
#u1 = User(generateHash(123456789), 'John Smith', '124 Temp Street, London ON Canada, L4S 4R8', '1986-03-14', 123456789,'AB123-45672-89012', '2002-06-16', '2021-05-15', 'AB1234567', '180', 'M', 'G', '2134-456-789-AB', '2004-07-16', '2022-06-16', 'AB3252554')

u2_id = generateHash(227463396)
u3_id = generateHash(148205297)
u4_id = generateHash(120144095)
print("Test users: ", u2_id, u3_id, u4_id)

u2 = User(u2_id, 'Jane Doe', '452 Test Road, Kitcher ON Canada, G4H 4U3', '1992-12-21', "227463396",'CD456-78905-12345', '2015-10-23', '2024-07-19', 'CD4567890', '154', 'F', 'G', '4567-889-012-CD', '2010-06-15', '2024-07-16', 'CD4352157')
u3 = User(u3_id, 'Jake Jones', '542 Maple Boulevard, Toronto ON Canada, M8G 8B2', '1996-09-28', "148205297",'GH859-5920-58293', '2018-04-25', '2025-02-14', 'BR9205824', '152', 'M', 'G2', '5929-452-859-RE', '2014-06-19', '2026-10-25', 'RK2958125')
u4 = User(u4_id, 'James Jaques', '582 Brook Crescent, Sarnia ON Canada, H3R 5T3', '1975-07-22', "120144095",'UG385-5285-62862', '2006-11-23', '2020-12-16', 'KE38158135', '160', 'M', 'G', '5920-683-592-RK', '2005-09-16', '2021-05-15', 'WH21348159')

userList.append(u2)
userList.append(u3)
userList.append(u4)

def registration(SIN):

	mylines = []

	for user in userList:
		if(SIN == int(user.sin)):
			return "Account already exists"

	try:
		with open (str(SIN) + ".txt", 'rt') as myfile: 
			for myline in myfile:
				mylines.append(myline)
	except FileNotFoundError:
		return "False"

	e_ID = generateHash(SIN)
	print(e_ID)

	new_user = User(e_ID, mylines[0], mylines[1], mylines[2], mylines[3], mylines[4], 
		mylines[5], mylines[6], mylines[7], mylines[8], mylines[9], mylines[10], 
		mylines[11], mylines[12], mylines[13], mylines[14])

	userList.append(new_user)

	return "Your account has been registered! A letter with your Unique Identification will be sent to your address: " + new_user.address 


def database(SIN, e_ID):

	
	for user in userList:
		if(int(user.sin) == SIN and user.id == e_ID):
			print("Electronic Identification: "+ user.id)
			print("Name: " + user.name)
			print("Address: " + user.address)
			print("Data of Birth: "+user.dob)
			print("SIN: "+user.sin)
			print("Lincense Number: "+user.licenseNum)
			print("Lincense Issue Date: "+user.licenseIssue)
			print("Lincense Expiry Date: "+user.licenseExp)
			print("Lincense Reference Number: "+user.licenseRef)
			print("Lincense Class: "+user.licenseClass)
			print("Height: "+user.height)
			print("Sex: "+user.sex)
			print("Health Card Number: "+user.healthNum)
			print("Health Card Issue Date: "+user.healthIssue)
			print("Health Card Expiry Date: "+user.healthExp)
			print("Health Card Reference Number: "+user.healthRef)
			return "True"
	return "False"


if __name__ == '__main__':

	flag_reg = True
	flag_data = True
	reg = True
	data = True
	regist = None

	if(reg == True):
		while (flag_reg == True):
			try:
				SIN = int(input("Enter your SIN to register for e-ID: "))
				flag_reg = False
				regist = registration(SIN)
				if(regist == "False"):
					flag_reg = True
					print("SIN not found")
				else:
					print(regist)
			except ValueError:
				print("Please enter a valid number")
		
	if(data == True):
		while (flag_data == True):
			try:
				SIN = int(input("Enter your SIN to check in the government database: "))
				e_ID = input("Enter your Electronic Identification (e-ID): ")
				flag_data = False
				if(database(SIN, e_ID) == "False"):
					flag_data = True
					print("SIN or e_ID not found!")
			except ValueError:
				print("Please enter a valid number")
