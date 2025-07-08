import mysql.connector as sql
from mysql_connector import db
from mysql.connector import Error
from datetime import datetime

class transactions(db):
	def __init__(self):
		super().__init__()
		
	def transaction(self,type,amount,accnt):
		o = datetime.now()
		q = '''insert into transactions (transactionId,transactionType,amount,accountNum) values(%s,%s,%s,%s)'''
		if type == 'deposit':
			tid = "dpst" + str(o.second)+str(int(o.microsecond/1000))
			v = (tid,"deposit",amount,accnt)

		elif type == 'withdrawl':
			tid = "wtdl" + str(o.second)+str(int(o.microsecond/1000))
			amount = amount*(-1)
			v = (tid,"withdrawl",amount,accnt)
	
		self.cursor.execute(q,v)
		s = self.mdb()
		s.commit()

	def trans_history(self,accntNum):
			try:
				q = 'select transactionType ,amount ,time_stamp from transactions where accountNum = %s order by time_stamp desc'
				v = (accntNum,)
			
				self.cursor.execute(q,v)
				l= []
				
				for i in self.cursor:
						l.append(list(i))
				for j in range(len(l)):
							if l[j][-2]<0:
								l[j][-2] = (-1)*(l[j][-2])
							l[j][-2] = float(l[j][-2])
							l[j][-1] = str(l[j][-1])
							
							
				
				
				return l
			except Error as e:
				print(e)
			
		
	
	def blnce(self,accnt):
		q = '''select sum(amount) from transactions where accountNum = %s'''
		#q= 'select * from transactions'
		v = (accnt,)
		self.cursor.execute(q,v)
		for i in self.cursor:
			pass
		if i[0] == None:
			return 0
		else:
			return i[0]
		
	def cd(self):
		q='select * from transactions'
		self.cursor.execute(q)
		for i in self.cursor:
			print(i)
		
		
		