import mysql.connector as mysql
from mysql.connector import Error
import random 

#get(accNo,mobNo)
#accountNum_gen()
#add_user(name,mbl,dob,addr)
#update_user(option,values,accnt)
class db:
	def __init__(self):
		try:
			self.__mydb = mysql.connect(
			host = "localhost",
			user = "venky",
			password = "Venky@44",
			database = "Mini_Bank_db")
			if self.__mydb.is_connected:
				self.cursor = self.__mydb.cursor()
		except Error as e:
			print("there some issues on MySQL db connection",e)
			
	def get(self,accNo,mobNo):
			self.accNo = accNo
			self.mobNo = mobNo
			query = '''select * from user_table where accountNum = %s && mobile_no = %s'''
			val = (self.accNo,self.mobNo)
			self.cursor.execute(query,val)
			j=[]
			for i in self.cursor:
				j.append(i)
			if len(j)>0:
				return j[0]
			else:
				return j
			
	def accountNum_gen(self):
			query = '''select accountNum from user_table'''
			self.cursor.execute(query)
			accnt_data=[]
			for i in self.cursor:
				accnt_data.append(i[0])
		
			while True:
				random_accnt=random.randrange(10000,99999)
				random_accnt = int(random_accnt)
				if random_accnt not in accnt_data:
					return random_accnt
			self.cursor.close()
			
	def add_user(self,name,mobile,dob,addr,passwd):
		self.name = name
		self.mobi = mobile
		self.dob = dob
		self.addr = addr
		self.accntNo = self.accountNum_gen()
		mq = 'select mobile_no from user_table'
		self.cursor.execute(mq)
		l = []
		for i in self.cursor:
			l.append(i[0])

		if self.mobi not in l and len(str(self.mobi)) >= 3 and len((self.mobi))<=10:
			q = 'insert into user_table (full_name,mobile_no,dob,address,accountNum,password) values(%s,%s,%s,%s,%s,%s)'
			values = (self.name,self.mobi,self.dob,self.addr,self.accntNo,passwd)
			self.cursor.execute(q,values)
			self.__mydb.commit()
			print('Your account has been created, Your account number :',self.accntNo)
			return True
		else:
			print('user already exists')
			return False
	
	def update_user(self,option,values,accnt):
		
		if option =='name':
			q = '''UPDATE user_table SET full_name = %s where accountNum = %s'''
		elif option == 'mobile':
			q = '''UPDATE user_table SET mobile_no = %s where accountNum = %s'''
		elif option == 'passwd':
			q = '''UPDATE user_table SET password = %s where accountNum = %s'''
		else:
			q=''
			print("invalid")
		fq = (values,accnt)
		self.cursor.execute(q,fq)
		self.__mydb.commit()
		
	def get_accnt(self,mobile,paswd):
		q='''select accountNum from user_table where mobile_no = %s && password = %s'''
		v=(mobile,paswd)
		self.cursor.execute(q,v)
		for i in self.cursor:
			return i
	
	def mdb(self):
		return self.__mydb
		
	
	
m = db()


#m.cursor.execute('delete from user_table where mobile_no=67')

#m.update_user('name','krishna','13737')




#m.update_user("passwd",9000,18181)