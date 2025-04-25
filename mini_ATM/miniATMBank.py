import samp as li
import mysql_connector as sql

class UserData(sql):
	def __init__(self):
		pass
		
	def login(self):
		self.mobile_no = int(input("Enter Mobile Number: "))
		self.account = input("Enter Account Number: ")
		
		for i in self.__userData:
			if self.mobile_no and self.account in i:
				print("Hii!",i)
		
		

obj = UserData()
print(obj.login())

choice = li.list()

def profile():
	p = sql.db('select * from user_table')
	
	print(p)

if choice[0] == "1":
	print(choice[1][0])
	profile()
	