import mysql.connector as mysql
from mysql.connector import Error
import random 
class db:
	def __init__(self):
		try:
			self.__mydb = mysql.connect(
			host = "localhost",
			user = "venky",
			password = "Venky@44",
			database = "Mini_Bank_db")
		except Error as e:
			print("there some issues on MySQL db connection",e)
			
	def get(self,accNo,mobNo):
			self.accNo = accNo
			self.mobNo = mobNo
			self.cursor = self.__mydb.cursor()
			query = '''select * from user_table where accountNum = %s && mobile_no = %s'''
			val = (self.accNo,self.mobNo)
			self.cursor.execute(query,val)
			j=[]
			for i in self.cursor:
				j.append(i)
			return j
			
	def accountNum_gen(self):
			query = '''select number from nums'''
			self.cursor.execute(query)
			accnt_data=[]
			for i in self.cursor:
				accnt_data.append(i[0])
			print(accnt_data)
			while True:
				random_accnt=random.random()*10000+10000
				random_accnt = int(random_accnt)
				if random_accnt not in accnt_data:
					return random_accnt
			self.cursor.close()
	
	
	
	
	