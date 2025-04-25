





def list():
	li = ["1.Profile","2.Check Balance","3.Deposit","4.Withdrawl","5.Loan","6.Transaction History"]
	
	for i in range(len(li)):
		print(li[i],end="\t")
		if (i+1)%2==0:
			print("\n")
	
	n = input("Select an Option: ")
	return ([n,li])	

