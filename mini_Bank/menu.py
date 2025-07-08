

def list():
	li = ["1.Profile","2.Check Balance","3.Deposit","4.Withdrawl","5.TransHistory",'6.Exit']
	
	for i in range(len(li)):
		print(li[i],end="\t")
		if (i+1)%2==0:
			print(" ")
	print()
	n = input("Select an Option: ")
	return ([n,li])

	
