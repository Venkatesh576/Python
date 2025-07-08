import menu as li
from transactionsData import transactions

class UserData(transactions):
	
	def register(self):
		try:
			
			fname = input('Enter firstName :')
				
			sname = input('Enter Surname :')
			mobile = input('Enter Mobile Num :')
			fullname = fname +' '+sname
			dob = input('Enter DateOfBirth(dd/mm/yyyy :')
			addr = input('Enter address :')
			passwd = input('create Passwd :')
			errs=0
			val = [fname,sname,mobile,dob,addr,passwd]
			errMsg=['First Name','Surname','Mobile','DoB','addr','Password']
			for i in range(len(val)):
				if(not val[i]):
					print(errMsg[i],'should not be empty')
					errs+=1
				
			if(mobile.isdigit() and errs<1):
				isCreated = self.add_user(fullname,mobile,dob,addr,passwd)
				if isCreated:
					return True
				if not isCreated:
					print('user already exists, please login')
					return False
			else:
				print('not valid mobile number')
		except OSError as e:
			print('invalid',e.messege)
			
	def login(self):
		try:
		
			self.mobile_no = input("Enter Mobile Number: ")
			self.account = input("Enter Account Number: ")
			self.userData = self.get(self.account,self.mobile_no)
		
			while True:
				if self.mobile_no and self.account in self.userData:
					[self.u_name,
					self.u_mobile,
					self.u_date,
					self.u_addrs,
					self.u_accnt,
					self.passwd]=self.userData
					print(self.u_name)
					return True
				else:
					print('Wrong credentials ')
					return False
		except OSError as e:
			print("wrong Number",e)
	def profile(self):
		dt = self.get(self.account,self.mobile_no)
		print('Hello..',dt[0])
		print('Mobile No.: ',dt[1])
		print('account Number: ',dt[4])
		
		want_edit = input("Yes/No (default=No): ")
		want_edit = want_edit.lower()
		if want_edit == 'yes':
			print('1.Change Name\n2.Change Mobile Number\n3.Change Password')
			Echoice = input("1/2/3 :")
			acnt = input('Account No.:')
			if acnt == self.u_accnt:
				if Echoice == '1':
					name = input('full Name:')
					if(len(name)>0):
						self.update_user('name', name,acnt)
					else:
						print('full Name should be more than 1 character')
		
				elif Echoice == '2':
					try:
						num = input("Enter new Mobile No. :")
						if len(num) ==10 and num.isdigit():
							self.update_user('mobile',num,acnt)
							self.mobile_no = num
						else:
							print("mobile number should be 10 digits")
					except OSError as e:
							print("invalid number")
				elif Echoice == '3':
							passwd = input("Enter new Passwd: ")
							if(len(passwd)>=4 and len(passwd)<=8):
								self.update_user("passwd",passwd,acnt)
							else:
								print('the length of password must be between 4 and 8 characters ')
				else:
							print("not in option")
							
		
	def check_blnc(self):
		
		print('available Balance :',self.blnce(self.u_accnt))
		
		
	def deposit(self):
		
		try:
			amount = float(input('Enter amount:'))
			if amount > 0:
				self.transaction('deposit',amount,self.u_accnt)
				print("The money has been deposited successfully")
				
		except OSError as e:
			print("not valid",e)

	def withdrawal(self):
		try:
			amount = float(input('Enter Amount :'))
			Eaccnt= input('Enter account Num :')
			if Eaccnt == self.u_accnt:
				if amount<=self.blnce(self.u_accnt):
					self.transaction('withdrawl',amount,self.u_accnt)
					print("The requested amount has been withdrawn.")
				else:
					print("Not sufficient amount, please check your balance")
			else:
				print("wrong account number")
		except:
			print("invalid")
	def history(self):
			l=self.trans_history(self.u_accnt)
			
			print('\t-------   ---------')
			for i in l:
				for j in range(len(i)):
				
					if type(i[j]) == 0:
						print(i)
					print(i[j],end=" ")
					if i[j]==i[-1]:
						print()
			


obj = UserData()
print(':: Welcome to miniATMBank ::')
print('1.login\n2.register')
echoice = input('choose an option (default=1):')
if echoice == '2':
	print("Register")
	isRegistered = obj.register()
	if isRegistered:
		u_inp = input("Do you want to login Now (y/n): ")
		if u_inp == "y":
			echoice = "1"
			
		
if echoice !='2':
    print("Login")
    isT =obj.login()
    if(isT==False):
    	print('forgot your account number?')
    	mobile=input('Enter Mobile No.: ')
    	passwd = input('Enter Password :')
    	accnt=obj.get_accnt(mobile,passwd)
    	if(accnt!=None):
    		print('This is your Account No.',accnt[0])
    		lgn = input('Do you want to login(default:yes) :')
    		lgn = lgn.lower()
    		if(lgn=='yes' or lgn==''):
    			isT =obj.login()
    	else:
    		print('wrong credentials')
    def l():
    	choice = li.list()
    	if choice[0] == '1':
    		print('\tProfile')
    		obj.profile()
    		
    	elif choice[0] == '2':
    		print('\tCheck Balance')
    		obj.check_blnc()
    		
    	elif choice[0] == '3':
    		print('\tDeposit')
    		obj.deposit()
    		
    	elif choice[0] == '4':
    		print('\tWithdrawal')
    		obj.withdrawal()
    		
    #	elif choice[0] == '5':
    	#	print('\tLoan')
    	
    	elif choice[0] == '5':
    		print('\tTransaction History')
    		obj.history()
    	elif choice[0] == '6':
    		return True
    	else:
    		print("Invalid Choice")
    
    while isT:
    	e = l()
    	enter = input('◀️')
    	if e:
    		break
    

	
	
